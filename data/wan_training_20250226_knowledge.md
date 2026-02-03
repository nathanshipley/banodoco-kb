# Wan Training Knowledge Base
*Extracted from Discord discussions: 2025-02-26 to 2026-02-03*


## Technical Discoveries

- **WAN 2.1 LoRA training works well with images only while preserving motion**
  - Multiple users confirmed that training LoRAs on images only still maintains motion capabilities in generated videos
  - *From: mamad8*

- **14B T2V LoRAs work on I2V model**
  - LoRAs trained on the 14B T2V model can be applied to the I2V model with some compatibility
  - *From: Cubey*

- **WAN LoRAs are significantly better than Hunyuan LoRAs**
  - Multiple users report WAN LoRAs produce much better results than equivalent Hunyuan training
  - *From: Cubey*

- **T2V LoRAs don't work well on I2V models**
  - LoRAs trained on T2V model perform poorly when applied to I2V model, requiring separate I2V training
  - *From: mamad8*

- **WAN model is very forgiving with LoRA weights**
  - Can use extremely high LoRA weights like 2, 3, or even 5 without quality degradation
  - *From: mamad8*

- **First 2 epochs show huge improvement, then convergence**
  - Training often converges quickly in first 2 epochs, with minimal improvement afterward
  - *From: samurzl*

- **480p training works better than 720p for WAN**
  - Model produces better results when trained on 480p images rather than higher resolution
  - *From: comfy*

- **Wan 2.1 can be trained with FP8 quantization using musubi-tuner**
  - FP8 support now available in musubi-tuner for memory savings during training
  - *From: mamad8*

- **I2V LoRAs don't transfer well between different models**
  - LoRAs trained on i2v-480P don't work on i2v-720P, and i2v LoRAs don't work well on t2v models
  - *From: codexq*

- **Training on quantized base models can compensate for quantization accuracy loss**
  - LoRA seems to compensate for some of the accuracy lost by quantization at inference when trained on quantized base
  - *From: spacepxl*

- **Wan requires more careful face dataset curation than other models**
  - Unlike Flux/Hunyuan that average faces well, Wan needs only the best headshots where you can definitively say 'this is how I want the person to appear'
  - *From: mamad8*

- **I2V models can be trained as image-to-image tasks for instant style transfers**
  - Training i2v model to output init frame + 4 identical frames works extremely well for tasks like relighting rooms, emptying rooms, changing skies. Only needs 2-5000 steps at 384x256 resolution
  - *From: mamad8*

- **Wan models learn very quickly and converge before 1 epoch**
  - Wan converges before 1 epoch but you can still get better results with more training
  - *From: Juampab12*

- **Low resolution training works extremely well for video LoRAs**
  - Training at 280x190 or similar low resolution produces results that look like 1080p model quality. Don't need to train higher than 384x384 for videos except for character training
  - *From: mamad8*

- **WAN generates by latents, one latent = 4 frames, you can't generate 1/4 latent to generate 1 frame, you need the whole latent**
  - Explains why cakify made the whole latent the same frame for better quality, then wants to finetune the VAE to generate 4 frames in 1 latent to have 4 images
  - *From: Juampab12*

- **Training duration timing varies significantly during training**
  - Training run didn't get the right duration until after 700 steps. Before that it either played it multiple times, or stretched it too long
  - *From: Benjaminimal*

- **Alpha affects learning rate based on square root calculation**
  - You can calculate the influence of alpha on learning rate based on the square root of the change in alpha. If you change alpha from 1 to 32, you should divide lr by sqrt(32) ~= 5.6 to get the same effective learning rate
  - *From: spacepxl*

- **WAN learns extremely fast**
  - 20 minutes to train 16 epochs with impressive results. Training speed described as 'insane'
  - *From: Juampab12*

- **Low resolution video + high resolution images strategy works well**
  - Motion from videos, quality from images. Used 19 videos at 128x170 and 20 images at 720x960 for HD inference without losing resolution
  - *From: Juampab12*

- **Caption technique helps with motion degradation**
  - Captioning 'an image of' tends to help with motion degradation somewhat
  - *From: Faust-SiN*

- **VAE compression causes artifacts with rapidly changing frames**
  - When training on videos with rapidly changing frames (like aging timelapses), VAE compression creates artifacts because 4 different frames in one latent are too different
  - *From: Juampab12*

- **Duplicating frames solves VAE compression issues**
  - Training with repeated frames (1,2,2,2,2,5,5,5,5...) where each latent contains the same frame 4 times prevents compression artifacts
  - *From: spacepxl*

- **First frame doesn't need repetition in VAE**
  - The first frame is compressed differently (4x less compression) so it shouldn't be repeated 4 times like the other frames
  - *From: spacepxl*

- **Causal VAE architecture explanation**
  - Each frame depends on the last, but not on the next. First frame gets compressed to 1 frame with 16ch, then each chunk of 4 frames after gets compressed to another 1 frame with 16ch
  - *From: spacepxl*

- **LoRA alpha=1 provides numerical stability with fp32 weights**
  - spacepxl found no benefit to changing alpha as long as LR is adjusted appropriately, and alpha=1 should help with numerical stability but with fp32 lora weights that really doesn't matter
  - *From: spacepxl*

- **HUD elements learn poorly at low resolutions**
  - When training on video game HUD overlays, the HUD elements didn't appear in outputs, likely due to low resolution training
  - *From: Mngbg*

- **Stuttery motion can be learned before age transitions**
  - During aging timelapse training, the model learned to make videos stuttery before learning actual aging transitions
  - *From: Juampab12*

- **TeaCache affects I2V LoRA performance**
  - I2V LoRAs worked significantly less when TeaCache started at first step, not just movement quality
  - *From: mamad8*

- **Frame bucket conflicts cause I2V training failure**
  - Using frame buckets like [1, 24, 33, 49] for I2V training causes conflicting conditioning signals because buckets 1, 24, 49 don't use the first frame as conditioning
  - *From: mamad8*

- **RTX 5090 generates 81 frames, 30 steps in ~209 seconds on Wan 1.3B T2V**
  - Bare wan setup without optimizations on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **T2V LoRAs work directly in I2V workflows**
  - Can use text-to-video trained LoRAs in image-to-video generation workflows
  - *From: ArtOfficial*

- **Training with only trigger words (no full captions) can work for Wan LoRAs**
  - Similar to SDXL training, using just trigger words maintains motion and gets overall style
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lower learning rates can converge faster and with better stability**
  - At rank=128 and alpha=128 for depth control LoRA, 2e-6 LR converged faster than 1e-5 with less noise/variance
  - *From: spacepxl*

- **Block swapping enables 14B training on local hardware**
  - Both musubi and diffusion-pipe support block-swapping for 14B model training with 4090/128GB RAM setup
  - *From: JohnDopamine*

- **T5 and LLM conditioned models work better with natural language captions than unique tokens**
  - Wan2 appreciates natural language similar to Flux, not unique trigger tokens like CLIP models
  - *From: Mint*

- **Training with generic style anchors improves results**
  - Including generic style words like 'illustration style' helps anchor the training and provides noticeable improvement
  - *From: Mint*

- **Token calculation formula for VRAM requirements**
  - Formula: width/16 * height/16 * (1 + (frames - 1) / 4) = tokens. 16 comes from 8x spatial in VAE plus 2x patch embedding
  - *From: spacepxl*

- **Best captioning approach for style training**
  - Caption as if the style doesn't exist so it becomes the new reality. Makes it easier for users to prompt without weird triggers
  - *From: spacepxl*

- **CLIP vision encoding is weak but image conditioning latent is very strong in I2V**
  - Can disable CLIP and it stays on image, but the encoded image conditioning latent dominates. This may make camera movement training difficult
  - *From: Kijai*

- **Training loss is mostly meaningless without validation set**
  - Raw training loss is random due to timestep sampling. Need separate validation set to measure over/underfitting properly
  - *From: spacepxl*

- **Loss chart jumps at epoch changes can indicate overfitting**
  - User observed loss jumps at each epoch boundary with gradient norm spikes, suggesting the model was learning dataset without generalizing
  - *From: Juampab12*

- **Evaluation loss is better indicator than training loss for model performance**
  - User found that while normal loss was all over the place, evaluation loss was a much better indicator of training progress
  - *From: Payuyi*

- **Timestep shift helps stubborn depth control training**
  - Adding timestep shift=5 finally made depth signal work after it was being ignored for a long time
  - *From: spacepxl*

- **Diffusion models outperform specialized architectures for watermark detection**
  - Flux and Wan models significantly outperformed YOLO and Uniformer models for watermark detection, especially for differentiating watermarks from legitimate text and low opacity watermarks
  - *From: mamad8*

- **Control LoRAs work better with early model blocks**
  - Early blocks do most of the work for control, suggesting depth signal is only needed for early timesteps once structure is determined
  - *From: spacepxl*

- **Wan model can be converted to image-only use**
  - Converting video model to image model just requires finetuning on images without architecture changes
  - *From: spacepxl*

- **Pan camera movement LoRA training works with consistent Blender-generated datasets**
  - Using Blender to create consistent camera movement with HDRI lighting, training on exact same movement every time. Different panning speeds would be best done with different LoRAs. Wan is very sensitive to needing exact same camera movement for training to work
  - *From: ArtOfficial*

- **Time-lapse and drawing undo LoRAs possible with minimal data**
  - Successfully trained time-lapse LoRA and drawing undo LoRA with only 2 videos each. Can create reverse playback videos using various images
  - *From: 852話 (hakoniwa)*

- **Face/emotion changing LoRA trained successfully**
  - Trained LoRA that can change camera angle and emotion (angry, surprised, sad, happy, neutral) using 9k 5-frame videos over 65 hours. Works at native 960x960 in 1 minute
  - *From: Juampab12*

- **Wan 2.1 has incredible prompt adherence for camera motions**
  - Training with captions describing camera motions like 'pan around subject, pan right, pan left, tilt up, tilt down, zoom in, zoom out, following subject' works well
  - *From: Amirsun(Papi)*

- **Evaluation datasets more reflective than training loss**
  - Pull out 10% of samples for evaluation instead of training to get better sense of how training is actually fitting rather than relying on training loss
  - *From: ArtOfficial*

- **Video files at exactly 81 frames work best, others get dropped**
  - Videos that were 80 frames rather than 81 got dropped during training, explaining reduced LoRA effect. Training works best at 81 frames
  - *From: DevouredBeef*

- **Training specific modules instead of full blocks for camera movement**
  - Training only self_attn, cross_attn, time_embedding, time_projection modules can create focused camera movement LoRAs that work across different subjects. Results in smaller 65MB LoRAs that are more generalizable.
  - *From: Amirsun(Papi)*

- **1.3B model requires different approach than 14B for character training**
  - 14B model works well for character training, but 1.3B struggles with character likeness even with similar settings
  - *From: mamad8*

- **Gemini can caption entire videos up to 45 minutes**
  - GoogleOne membership provides significant token allowances for video captioning with Gemini
  - *From: Kytra*

- **Fun model LoRA conversion works**
  - Script can convert regular WAN LoRAs to WAN Fun format by removing incompatible keys, producing good results after conversion
  - *From: Benjimon*

- **Block swapping affects VRAM usage patterns**
  - Recent wrapper changes show VRAM gradually increasing during sampling and TeaCache skipping fewer steps than before
  - *From: DevouredBeef*

- **Low learning rates work well for Wan training**
  - Testing shows 2e-5 LR (avr_loss=0.0744) vs 3e-5 LR (avr_loss=0.0759) - Wan really likes low learning rates
  - *From: Benjimon*

- **VACE finetunes work with existing 1.3B model finetunes**
  - Finetunes for the 1.3B model seem to work just fine with VACE
  - *From: Piblarg*

- **Low learning rate captures rapid movement with better fidelity**
  - A low learning rate (2e-5) captures rapid movement with better fidelity in the Wan2.1 14B model - only 2,500 steps at 256×256 resolution, physics dynamics and fine motion captured exceptionally well
  - *From: Amirsun(Papi)*

- **Extremely low resolution training can work for motion**
  - Success reported as low as 64x64 for motion LoRAs on HunyuanVideo, similar results expected for Wan
  - *From: CJ*

- **Simple motion LoRAs possible with few clips**
  - Motion LoRA successfully made with like 11 3-second clips
  - *From: Benjimon*

- **Wan + VACE can remove watermarks effectively**
  - Used WAN + VACE + DiffSynth Lora (for 8 steps inference) to remove watermarks from 600 videos found on pinterest
  - *From: Alisson Pereira*

- **Training LoRAs with as few as 2 videos/images is possible but quality depends on base model understanding**
  - Training a LoRA is possible with even 2 videos/images, but there is a difference between training a LoRA and training a well-trained LoRA. Training a LoRA in a concept that the base model does not understand much will require more examples. About 50 samples recommended for quality results.
  - *From: Alisson Pereira*

- **1.3B model sometimes has less concept understanding than 720 model**
  - Because it is 1.3B, sometimes the concept is more unknown for this model than for the 720, besides the fact that 1.3B is txt 2 video, providing a base image helps a lot
  - *From: Alisson Pereira*

- **Camera movement LoRAs are very difficult to train effectively**
  - Camera zoom LoRAs failed even with 20 videos of zooming motion. User spent a week training zoom LoRAs but couldn't tell if results were from the LoRA or the prompt. When removing zoom from prompt, it stopped working but removing LoRA completely also generated different results.
  - *From: ingi // SYSTMS*

- **WAN results can be highly seed-dependent**
  - Results can be highly dependant on seed (i.e. luck) - changing seed can produce great results where different prompts failed
  - *From: MilesCorban*

- **Gradient accumulation steps affects actual training steps significantly**
  - Step count was 4x what user thought it was due to gradient accumulation step setting, causing massive overcooking of LoRAs
  - *From: ingi // SYSTMS*

- **Gemma3 model works well for captioning without censorship**
  - Found gemma3 very good for captioning, follows instructions well, no censorship so you can caption anything including blood, nsfw content
  - *From: Alisson Pereira*

- **WAN training particle artifacts look similar to HunyuanVideo patterns**
  - User noted that WAN particle/artifact issues resemble the pattern problems seen in HunyuanVideo
  - *From: seitanism*

- **FramePack allows 1-minute video generation with 6GB VRAM**
  - 13B model can generate 60 seconds at 30fps (1800 frames) with minimal 6GB GPU memory requirement, even laptop GPUs work
  - *From: lovis.io*

- **WAN 1.3B character LoRAs show strong likeness after first epoch**
  - Character LoRA training with HunyuanVideo shows strong likeness after first epoch, but same dataset with WAN shows 0% likeness after 100 epochs with same settings
  - *From: Mads Hagbarth Damsbo*

- **Block swap doesn't noticeably affect training speed**
  - Block swapping has minimal impact on training performance, maybe 1% difference
  - *From: Piblarg*

- **14B model takes 5x longer per step than 1.3B**
  - Training speed comparison shows significant difference between model sizes
  - *From: Piblarg*

- **Gradient accumulation acts similar to batch size but is less expensive**
  - Accumulates N gradients before backpropagation, helps stabilize training by reducing abrupt weight changes
  - *From: Alisson Pereira*

- **Block swap doesn't affect training speed**
  - For training, block swap appears to be a free lunch with no marginal slowdown, especially at lower it/s like 5s/it. Things can get swapped faster than training is happening
  - *From: Piblarg*

- **Training on SkyReels T2V instead of base Wan 2.1 T2V gives better results**
  - Had poor results training on base Wan 2.1 t2v model with both Musubi and DP. Training on Skyreels t2v instead produces much better character likeness
  - *From: JohnDopamine*

- **Single video training works well for consistent actions**
  - If you want to see someone perform the same action every time you generate something, training on a single video is the only way to go
  - *From: Kytra*

- **14B vs 1.3B requires different captioning approaches**
  - 14B is more flexible but sometimes captioning that works for 1.3B doesn't work for 14B. Usually captions work for both but sometimes requires adjustment
  - *From: Piblarg*

- **Musubi Tuner uses --fp8_scaled for efficient fp8 training**
  - Already implemented more efficiently with --fp8_scaled option. Quantizes weights to fp8 with higher precision, then converts back to fp16/bf16 during calculation. Originally from HunyuanVideo
  - *From: kohya*

- **LoRAs trained on T2V models work with I2V models**
  - A LoRA trained on the T2V model will work with the I2V model, so probably not much benefit training with the I2V model specifically
  - *From: ingi // SYSTMS*

- **Training on images only reduces movement in video output**
  - Images only training will start to lose motion beyond 20-40 epochs for HunyuanVideo, and similar behavior expected for Wan
  - *From: Thom293*

- **Trigger word placement doesn't seem to matter much**
  - Used triggers at start and middle of text file, honestly cannot tell a difference with HunyuanVideo
  - *From: Thom293*

- **Wan model knows a lot already, quality should not suffer with float8 training**
  - Quality should not suffer too much if you make a lora and set it to like .5-.7 strength. The model should 'take over' any potential quality loss
  - *From: Thom293*

- **Training without captions can work for style LoRAs**
  - Trained 10 epochs of 148 images with NO captions at all. No keyword, nothing. Results were pretty decent for style training
  - *From: Thom293*

- **Opposing LoRA training technique creates better sliders**
  - Generate 2 opposing LoRAs (Big Boobs and Small Boobs), merge with one at negative scale, unwanted behavior cancels out while desired behavior gets stronger
  - *From: Piblarg*

- **Wan may work better with phrases instead of full sentences**
  - Asked ChatGPT about prompting style, seems like wan does better with phrases, not sentences. Switching to phrases showed improvement
  - *From: the_darkwatarus_museum*

- **SkyReels models give better training results than base Wan**
  - Best results training on SkyReels models specifically ckpt_path = '/mnt/g/Wan2.1/SkyReels-V2-T2V-14B-540P'. Had real shit results training on Wan base
  - *From: JohnDopamine*

- **Block swapping is essentially free performance-wise**
  - Block swapping doesn't slow down iterations and allows training larger datasets
  - *From: Piblarg*

- **Training on images only does not blunt motion in generated videos**
  - Multiple users confirmed that training LoRAs on still images maintains or even improves motion quality in video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multiple-overlapping training method can cause stuttering effects**
  - Training with longer clips using multiple-overlapping resulted in stuttering that couldn't be smoothed with frame interpolation, likely from overlapping sections
  - *From: Zlikwid*

- **Very low quality training data can still work effectively**
  - Small, grainy internet GIFs converted to MP4 without cleanup still produced working LoRAs, though with a smaller training sweet spot
  - *From: Thom293*

- **SkyReels models produce better likeness results than Wan base for character training**
  - Training LoRAs on SkyReels models and using them with Wan models yielded significantly better human likeness results
  - *From: JohnDopamine*

- **Graphic novel style LoRA trained successfully without captions**
  - 150 images, no video, no captions/keywords, resolution 1024, default LR, 5 repeats, 25 epochs produced good style results
  - *From: Thom293*

- **SkyCaptioner works locally with DeZoomer nodes**
  - Can run SkyCaptioner locally through modified DeZoomer nodes, with fp8 and 4bit options available
  - *From: Thom293*

- **Automagic optimizer converges super fast**
  - Uses individual learning rates per parameter instead of single rate for all parameters, brings new metrics to tensorboard
  - *From: Alisson Pereira*

- **Can remove dataset images mid-training**
  - Deleted about 15 images mid-training and resumed successfully
  - *From: Thom293*

- **720p training possible locally on 5090**
  - Achieved 640p training on 5090 with block swap maxed, 720p may be possible with memory tweaks
  - *From: Thom293*

- **WSL2 block swapping issues on Windows**
  - Block swapping fails in WSL2 environment but works fine on native Windows
  - *From: MOV*

- **LoRAs work directly in ComfyUI without conversion**
  - Musubi/Kohya output LoRAs work directly in ComfyUI, no conversion needed
  - *From: Piblarg*

- **Training images first then adding videos later for motion works well**
  - Train with images first until they get stiff, then add a folder of videos for movement at the end for like 10 epochs
  - *From: Thom293*

- **Can modify training datasets mid-run by adding/removing folders**
  - Successfully stacked 4 different datasets and added them over time - landscapes/random images first for 20 epochs, then faces for 10 epochs, then 4k wallpapers for 25 epochs, then videos from epoch 55-63, then removed videos for last 2 epochs to clean up blur
  - *From: Thom293*

- **Automagic optimizer assigns separate learning rate to each scalar parameter**
  - Unlike standard optimizers that use single global learning rate per parameter group, automagic gives each individual number within model weights its own learning rate - more fine-grained than per-neuron
  - *From: Alisson Pereira*

- **Images + videos combination is the real training method for T2V**
  - Images provide quality while videos provide movement - removing images at end for memory purposes works but images are key to quality
  - *From: Thom293*

- **Flash attention wheel for torch 2.7 works with torch 2.8**
  - Successfully used torch 2.7 flash attention wheel with torch 2.8 on runpod template
  - *From: Persoon*

- **Flash attention wheel for torch 2.7 and cuda 12.8 works with torch 2.8 on runpod**
  - The flash-attn wheel for torch 2.7, cu128 works for the torch 2.8 cu128 runpod starter template
  - *From: Persoon*

- **Sigmoid timestep sampling gives better character details**
  - Using Sigmoid instead of shift for training in musubi tuner gives much better details for character LoRAs, similar to what was seen in Flux
  - *From: hablaba*

- **Two-pass captioning improves results**
  - Caption with Qwen VL first, then refine with Qwen Instruct model for better quality captions
  - *From: Cseti*

- **Frame bucket buffer needed for exact frame counts**
  - Videos with exactly 33 frames get rounded down to 32 and discarded, need to add buffer frame buckets like [30,31,32,33,34,35] to avoid empty dataset
  - *From: crinklypaper*

- **Logit_normal is default sampling method in diffusion-pipe**
  - Diffusion pipe suggests logit_normal as default sampling method, which is equivalent to 'sigmoid' in musubi tuner
  - *From: hablaba*

- **Captions vs trigger words show different training outcomes**
  - Training with actual captions vs just trigger words in caption files produces different results - trigger word only captured more of the LUT and color theme
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN LoRAs work on both T2V and I2V models with cross-compatibility**
  - T2V LoRAs generally work on I2V models, but I2V LoRAs may not work properly on T2V models
  - *From: crinklypaper*

- **Aspect ratio affects convergence significantly**
  - 5:7 aspect ratio datasets won't converge at 100 epochs, but 16:9 or 9:16 converges at 20 epochs with same settings
  - *From: jikan*

- **Batch size 1 eliminates need for repeats**
  - If batch size is 1, no need for repeats - can train 23 videos at repeat 1 and gradient accumulation 1 for 23 steps per epoch
  - *From: CJ*

- **100 steps per image is good starting point for training**
  - Math: 63 images x 100 steps = 6300 steps, with batch size 16 and grad accum 2 (effective batch 8), ideal epoch around 787 steps or epoch 262
  - *From: MilesCorban*

- **Fast steps are images, slow steps are videos during training**
  - Some training steps take 1 second (images), others take 30+ seconds (videos) - this is normal behavior
  - *From: Thom293*

- **Wan 2.1 LORAs work on Wan 2.2 low noise model**
  - The low noise model is like a retrain of 2.1, so existing LORAs are compatible
  - *From: jikan*

- **Wan 2.1 LORAs benefit from higher weight on high noise model**
  - Character LORAs need approximately 2x weight on high noise model, otherwise they appear weak
  - *From: hablaba*

- **Training on distilled models is not optimal**
  - You will get worse LORAs by training with distilled models - they're only for inference. Always train on base models
  - *From: yi*

- **Wan 2.2 training uses same VRAM as 2.1**
  - Features like fp8 training, block swapping and flash-attn work as previously, keeping VRAM usage similar
  - *From: seruva19*

- **Training LoRA only on low model with full timestep range (0-1) works for both high and low models**
  - Instead of training separate LoRAs for high (0.875-1) and low (0-0.875) models, training just the low model with min_t=0 and max_t=1 covers the entire timestep range and can be applied to both models
  - *From: Alisson Pereira*

- **High noise model LoRA should only be used for limited inference steps**
  - Since high model is trained on timestep 0.875-1 (1/8 of range), it should only be used for 1/8 of inference steps to avoid deviating from character
  - *From: ArtOfficial*

- **LoKR performs better than LoRA for concept bleeding prevention**
  - LoKR shows better results than LoRA for preventing character bleeding to other characters, though takes 20-30% longer to train
  - *From: jikan*

- **Automagic optimizer works well with dynamic learning rate adjustment**
  - Automagic optimizer adjusts learning rate per parameter based on gradient direction consistency - lr_bump controls adaptation speed
  - *From: Alisson Pereira*

- **Beta scheduler works better than Karras for Wan 2.2 MoE**
  - Beta scheduler stays at high noise longer in initial timesteps, while Karras starts with little noise in the high model, making it less effective
  - *From: Alisson Pereira*

- **Character LoRAs should be trained on low noise model only**
  - Low model focuses on final timesteps that add details. High model handles general shapes/motion, but character identity/likeness comes from low noise training
  - *From: Alisson Pereira*

- **5B model may be better than 14B for some use cases**
  - Training on 5B model shows better results than 14B in testing, can generate 24fps videos at 720p
  - *From: Alisson Pereira*

- **Character LoRAs can be trained effectively in 30 minutes**
  - Good facial feature recognition achieved in 30 minutes of training on 4090, though longer training (5+ hours) gives best results for complex features like tattoos
  - *From: Kenk*

- **FP8 scaled models cannot be used for training**
  - Training fails with NaN values on fp8_scaled models, must use fp16 models for training
  - *From: MilesCorban*

- **Training high and low noise models separately produces best results for style training**
  - High model picks up composition, low model picks up small details
  - *From: jikan*

- **Low LoRA on high model at 0.3 strength helps with character identity**
  - High model alone doesn't recreate identity well in first sampler
  - *From: Kenk*

- **Low noise model training has different loss characteristics**
  - High LoRAs can train down to 0.04-0.05 loss, but sweet spot for low noise LoRAs is 0.07 range. Lower than 0.07 starts to lose detail and get hazy
  - *From: CJ*

- **High variance is normal for low noise training**
  - High noise training is more stable, low shows ridiculous difference in variance
  - *From: CJ*

- **Tag-based captioning can work effectively**
  - Using Florence for basic tagging with trigger word and 5-word position description instead of natural language captions
  - *From: Cubey*

- **WAN 2.2 Lightning LoRAs reduce effectiveness of trained LoRAs**
  - New LightX2V LoRAs for 2.2 reduce effectiveness of custom trained LoRAs at 0.125 weight
  - *From: _Djent_*

- **Diffusion-pipe supports video training for 5B model**
  - Confirmed that diffusion-pipe can train video datasets on WAN 2.2 5B model, showing 5 samples/sec for images and 67 samples/sec for videos
  - *From: crinklypaper*

- **WAN 2.2 14B I2V works better with fp32 weights**
  - Dramatically better performance with fp32 weights, bf16 beats fp16, analyzing weights shows bf16 fits with less loss
  - *From: Persoon*

- **Character LoRAs affect all similar subjects in scene**
  - When training person LoRA for WAN, it makes every person in scene that same person, same issue occurs with objects like motorbikes
  - *From: Ruairi Robinson*

- **Low noise model training alone gives half-decent likeness in 15 minutes**
  - Training only low noise model provides good character likeness quickly, low noise LoRA works on high model like 2.1 LoRA
  - *From: Critorio*

- **Wan 2.2 character LoRAs learn likeness very quickly**
  - Character likeness starts appearing at epoch 10, with apparent resemblance by epoch 24
  - *From: Critorio*

- **Low noise LoRA affects high model significantly**
  - Low noise LoRA makes relatively big difference on high model, affects composition, shapes, and object sizes
  - *From: Critorio*

- **High model handles motion and composition, not just motion exclusively**
  - High model creates base of composition and shapes, not only motion as previously thought
  - *From: Critorio*

- **Training at higher resolution (720p) with rank 16 LoRAs possible**
  - Managed to train at 720p with frame_bucket=16 using 1 second videos, rank 16 and rank 32 both work
  - *From: Kenk*

- **Multiple overlapping uses more VRAM than single beginning**
  - Multiple overlapping processes 2 clips in same step when clip is longer than bucket, doubling VRAM usage
  - *From: MilesCorban*

- **Automagic optimizer learns very fast**
  - Training with automagic is 'really, really fast' on 4090, described as '15 minute loras'
  - *From: Critorio*

- **Loss stuck around 0.14-0.135 indicates potential local minimum**
  - When loss plateaus at ~15% error, changing lr_bump can help escape local minimum
  - *From: Alisson Pereira*

- **Flow shift parameters crucial for training success**
  - Flow shift 1.0 creates rough sketching, 3.0 for sketching and details (Low noise model), and 7.0 for overall composition and movement (high model). Setting flow shift to 1 caused disastrous loras
  - *From: uff*

- **High noise model converges much faster than low noise**
  - High noise model plateaus at 3-5k steps around 30-60 epochs, while low noise takes much longer to plateau on same dataset
  - *From: tarn59*

- **Low loss values may indicate overtraining**
  - 0.05 loss resulted in fuzzy/grainy outputs, while loss over 0.1 worked better for low noise model with crystal clear results at epoch 8
  - *From: CJ*

- **Resolution training strategy matters**
  - Training low resolution first then bumping to high resolution around epoch 35 improved loss curves
  - *From: crinklypaper*

- **Hardware performance comparison**
  - H200 takes 4 hours for training, RTX Pro 6000 takes 4.5 hours, but H200 is twice the price. 5090 vs Pro 96GB perform similarly for image training as VRAM isn't fully utilized
  - *From: Ruairi Robinson*

- **Low noise LoRA for Wan 2.2 takes much longer to train and loss doesn't drop as readily as high noise**
  - Multiple users experienced low noise training getting stuck at 0.1xxx loss values for extended periods, while high noise trains quickly with clear downward trends
  - *From: screwfunk, crinklypaper, mrassets*

- **High noise LoRA can be tested independently with lightning LoRA**
  - You can test high noise alone using lightning LoRA with 4 steps starting from 0 - it will be blurry but show outlines and training progress
  - *From: flo1331*

- **Wan 2.2 5B model offers more control and faster training**
  - Community member suggests moving to 5B model because it's faster and provides more control over training
  - *From: Kiwv*

- **Loss graphs by steps vs epochs can be misleading**
  - Looking at loss by epochs is more accurate than by steps for determining training progress
  - *From: Alisson Pereira*

- **Diverse datasets cause higher loss values that don't drop significantly**
  - When dataset contains very different styles/characters grouped by one concept (like 360 rotation), the model struggles to predict noise consistently, keeping loss higher around 0.1
  - *From: Alisson Pereira, mrassets*

- **Character LoRAs trained on only images lose motion in WAN 2.2**
  - Training character LoRAs exclusively on static images results in no movement/animation in generated videos, similar to WAN 2.1 behavior
  - *From: crinklypaper*

- **Motion can be recovered through detailed prompting**
  - Using more specific motion descriptions like 'striding quickly toward the camera before leaning in close' and 'rapid dolly-in from full body to extreme close-up' can restore movement even with image-only trained LoRAs
  - *From: crinklypaper*

- **High noise model trains extremely fast compared to low noise**
  - High noise LoRAs train in 30-40 minutes while low noise LoRAs take several hours on similar datasets
  - *From: screwfunk*

- **Low noise model degrades with overtraining**
  - Higher epochs on low noise model result in worse motion quality - 12 epochs had much better motion than 51 epochs, despite similar likeness
  - *From: el marzocco*

- **AdamW optimizer works better than Automagic for low noise training**
  - Multiple users found AdamW optimizer performs better for low noise model training, while Automagic works fine for high noise
  - *From: screwfunk*

- **Single LoRA training for both High/Low noise models possible with Musubi**
  - Musubi can train both Wan 2.2 high and low noise models simultaneously, producing a single LoRA instead of two separate ones. Uses logsnr sampling to switch between experts during training.
  - *From: artificial_fungi*

- **AdamW8bit optimizer works well for Wan 2.2 training**
  - Multiple users report success with AdamW8bit optimizer, particularly for low noise model training
  - *From: screwfunk*

- **Lightning LoRA causes distortion and ghosting effects**
  - Lightning LoRA creates transparent ghosting effects and weird lines. LightX2V produces better results but with darker/muted colors
  - *From: crinklypaper*

- **Standalone trigger words can be detrimental**
  - Using trigger words in natural context works better than standalone triggers. Model can better attribute content when used contextually
  - *From: flo1331*

- **Mixed resolution training improves low model results**
  - Training with mixed 640x360 and few high res samples works better than high res low fps extraction for low model
  - *From: flo1331*

- **Wan 2.1 LoRAs work effectively on Wan 2.2**
  - 2.1 character LoRAs produce similar results when used on 2.2 models, suggesting good backward compatibility
  - *From: artificial_fungi*

- **WAN 2.2 dual LoRA training now available through Musubi**
  - Musubi officially pushed code for dual LoRA training on Saturday, allowing single LoRA training for both high and low noise models
  - *From: artificial_fungi*

- **WAN 2.2 low model slightly better than 2.1 base**
  - According to testing, the 2.2 low model performs slightly better than the 2.1 base model
  - *From: artificial_fungi*

- **WAN 2.2 Low is basically WAN 2.1 with more training**
  - WAN 2.2 Low model is fundamentally WAN 2.1 with additional training data
  - *From: flo1331*

- **Lightning LoRAs need different strengths on high vs low**
  - LightX2V needs more strength on high noise model, suggesting character LoRAs might need similar approach
  - *From: JalenBrunson*

- **Block swap doesn't work with dual training**
  - Musubi's dual LoRA training mode cannot use block swap functionality, limiting VRAM efficiency
  - *From: flo1331*

- **Sigmoid timestep sampling ignores timestep split**
  - When using sigmoid timestep sampling, it ignores the defined timestep boundary splits
  - *From: JalenBrunson*

- **K3NK achieves 8-9 minute character LoRAs with specific settings**
  - Uses rank 16, low resolution (512 max), ~30 images with repeat 1, gas 3-4, resulting in 10-13 steps per epoch. Fast training because he isn't doing repeats and uses small datasets
  - *From: Alisson Pereira, CJ*

- **Lower rank trains faster and can avoid overfitting issues**
  - Rank 16 trains much faster than rank 128. Higher rank can learn unwanted details like lighting, lower rank focuses on essential character details. For characters, overfitting is sometimes welcome
  - *From: Alisson Pereira*

- **Wan 2.2 requires less training due to extensive pretraining**
  - Model was trained on monstrous amount of data, so you don't need to teach basic human anatomy, just specific character details
  - *From: Alisson Pereira*

- **Single LoRA can work for both high and low noise models**
  - Training method that puts both high and low into single LoRA works well, achieved good likeness in 24 minutes on 3090 with 30 pictures
  - *From: screwfunk*

- **WAN 2.2 High model converges extremely fast - can achieve good style in just 2-3 epochs**
  - crinklypaper found that epoch 2-3 on high model already captured the anime style well, much faster than expected
  - *From: crinklypaper*

- **Loss graphs are not reliable indicators for WAN 2.2 training**
  - screwfunk noted you cannot go by loss numbers for high lora and MilesCorban observed that LOW will continue to drop even when overtrained
  - *From: screwfunk*

- **High model puts down base composition and motion, Low model fills in details**
  - screwfunk explained that high noise creates fuzzy baseline of motion/composition, while low noise adds all the detail and clarity
  - *From: screwfunk*

- **Musubi dual training can produce single LoRA file for both high and low models**
  - screwfunk achieved crazy good likeness within 30 minutes using musubi's dual option that trains into one lora file applied to both models
  - *From: screwfunk*

- **Higher resolution training significantly improves results**
  - crinklypaper changed from fixed 896x504 to [512] resolutions and commented out ar_buckets, leading to much better training outcomes
  - *From: crinklypaper*

- **Wan 2.2 high noise LoRA trains extremely fast**
  - 1 epoch (150 steps, 25 minutes) can be sufficient for high noise training
  - *From: crinklypaper*

- **Loss graphs are meaningless for Wan 2.2 training**
  - Multiple users confirm loss values don't correlate with actual model quality - need to test outputs instead
  - *From: CJ*

- **Wan 2.2 high noise can achieve 0.4 loss after 300 steps while others take ages to reach 0.9**
  - The loss behavior is very different between high and low noise models
  - *From: flo1331*

- **Caption stuff you don't want to see, not what you want**
  - For character training, caption elements you want to remove rather than preserve
  - *From: Ryzen*

- **WAN 2.2 high noise model trains extremely fast and converges quickly**
  - High model learns very quickly, trains super fast and does not need much training. Got good likeness in 200 steps on high
  - *From: screwfunk*

- **WAN 2.2 training requires visual evaluation over metrics**
  - Charts, steps, or loss don't indicate good vs bad results like they did in WAN 2.1. Best metric is using your eyes and testing
  - *From: screwfunk*

- **Musubi can train both high and low into single LoRA**
  - With musubi you train both high and low in 1 lora, not two separate loras. Take that one lora and put it in both high and low slots
  - *From: screwfunk*

- **CAME optimizer uses 1GB less VRAM**
  - CAME is same as adamw8bit except more memory efficient, takes around 1gb less vram
  - *From: flo1331*

- **33 frame videos yield better results than longer videos**
  - Sticking with 33 frames max yielded far better results than longer videos, also easier to setup and caption
  - *From: flo1331*

- **High noise model primarily handles shapes, colors, placements, and motions while low noise model handles detailed character features**
  - High model gives basic structure and movement, low model refines character details and fidelity. You can visualize what high model does by using tinyvae after high pass with denoised_latents
  - *From: mamad8*

- **Low model can work alone without high model but high model cannot work alone**
  - Low model trained on full timestep range (0 to 1) can play role of high model. Low works independently but high doesn't
  - *From: Alisson Pereira*

- **Training low model on full timestep range may be beneficial**
  - Theory that training low model to start from t=0.875 with fully noised latent won't learn properly how to denoise from high model outputs
  - *From: MilesCorban*

- **Low noise LoRA only approach works best**
  - Best results achieved using epoch 15 low noise only, despite training both high and low noise
  - *From: el marzocco*

- **Overtrained low LoRA symptoms**
  - At 50 epochs with 10 repeats, low noise LoRA becomes overtrained
  - *From: el marzocco*

- **High noise LoRA reduces motion**
  - High noise LoRAs lose motion capabilities as training progresses
  - *From: el marzocco*

- **High noise LoRA can change ethnicity**
  - Adding high LoRA makes character look Asian, while low LoRA fights to maintain original ethnicity
  - *From: el marzocco*

- **Shift parameter critically affects LoRA performance**
  - Shift 5 causes distortion, shift 8 works well for style LoRAs
  - *From: crinklypaper*

- **Sampler affects LoRA strength requirements**
  - DPM++_SDE requires strength of 1 to activate style, while Euler works with low strength
  - *From: crinklypaper*

- **Training on full timestep for low noise**
  - Training low noise on full timestep doesn't hurt performance
  - *From: CJ*

- **Lightning LoRAs work well with I2V**
  - Lightning performs great for image-to-video tasks
  - *From: crinklypaper*

- **Loss graphs are largely unreliable for WAN 2.2 training - earlier epochs often produce better results despite higher loss values**
  - Unlike WAN 2.1 where loss graphs were predictive, 2.2 requires manual testing to determine quality. Users found good results even above 0.1 loss, and earlier epochs (like epoch 50) often outperformed later ones (epoch 300) despite flattened loss
  - *From: screwfunk*

- **Different shift values work better for high vs low noise models**
  - 8 shift for high noise, 6 shift for low noise produces good results. 5 shift causes distortions, but 8/6 split maintains good movement and camera work while avoiding artifacts
  - *From: crinklypaper*

- **Training on video sequences vs images affects optimal epoch selection**
  - Users training on videos found later epochs work better, while those training on images found earlier epochs optimal
  - *From: screwfunk*

- **High noise model trains much faster than low noise model**
  - High noise typically completes in 20-30 minutes (epoch 10 on 40 images), while low noise takes significantly longer
  - *From: screwfunk*

- **WAN can be trained beyond 81 frames**
  - Some LoRAs successfully trained at 97 frames, though not recommended unless for specific use cases
  - *From: flo1331*

- **Training High LoRA with additional epochs on still images at 768 resolution**
  - Adding an epoch of 768 resolution still images to HIGH model captures style more effectively
  - *From: Zlikwid*

- **High LoRA has significant impact beyond motion and shape**
  - High stage influences final details like expression and eyes, not just motion
  - *From: MilesCorban*

- **TREAD implementation for Wan 2.2 training**
  - Implemented TREAD (https://arxiv.org/pdf/2501.04765) for Wan2.2, provides fast convergence and motion learning with 35% VRAM reduction
  - *From: Ada*

- **High noise model trains much faster than low noise model**
  - High noise typically requires around 400-800 steps for characters, while low noise needs 800-3000 steps. High noise was observed learning at around 1500 steps vs 3500 steps for low noise
  - *From: Gentleman bunny, flo1331*

- **Wan 2.2 5B Turbo achieves very fast generation**
  - T2V generation with style LoRA took only 90 seconds including VAE encode
  - *From: crinklypaper*

- **High noise model is crucial for proper character proportions**
  - High noise model affects basic foundation of character including face shape, proportions, and size. Even for character training, high model has larger impact on final details than initially thought
  - *From: MilesCorban, screwfunk*

- **Character LoRA can be effective with very few training steps**
  - 300 steps produced good results for character LoRA training, much faster than expected
  - *From: Ryzen*

- **Training multiple characters in single LoRA works very well**
  - Putting two character datasets with separate triggers into same LoRA eliminates character bleeding issues that occur when applying two separate character LoRAs to the same scene
  - *From: screwfunk*

- **Video training converges much faster than image training**
  - Training on videos converges far better than images, training is faster relatively speaking, and provides crazy good likeness with no movement issues
  - *From: flo1331*

- **LoRA+ significantly improves training convergence**
  - LoRA+ allows good results after 400-800 steps vs normal training taking up to 20k steps. Recommended ratio is 4 instead of the standard 16
  - *From: flo1331*

- **GAS=4 dramatically reduces training time**
  - Using gradient_accumulation_steps=4 allows great character likeness after only 13 minutes for high model and 31 minutes for low model
  - *From: DennisM*

- **Linux training is faster and uses less VRAM than Windows**
  - Training on Mint Linux with Nvidia 575 open drivers is noticeably faster and uses less VRAM compared to Windows setup
  - *From: Kierkegaard*

- **Training videos with mixed frame lengths works well**
  - Using 81 frame 16fps low res videos for motion paired with hi-res still images works pretty well
  - *From: Gentleman bunny*

- **Splitting videos into sections may act like increasing repeats**
  - Splitting video datasets into more sections appears to be acting as if I had selected 3 repeats, definitely seems to be over cooking the model more
  - *From: Kierkegaard*

- **Training high noise model extensively improves results**
  - 117.5K steps on high model with no signs of overtraining - eyes better looking, motion distortion less. High model is very important for both style and motion if not present in base model
  - *From: crinklypaper*

- **Training with wrong timesteps can still produce decent results**
  - Accidentally trained high with min=0 max=875 instead of correct min=0.875 max=1, but LoRA still turned out okay despite wrong timesteps
  - *From: samurzl*

- **Minimal vs detailed captions show similar results**
  - Did A/B test comparing minimal captions with rich detailed captions - loss curves were nearly identical, results too. Captioning may not be as important as thought
  - *From: samurzl*

- **Full fine-tuning is possible on single GPU**
  - Currently experimenting with full fine-tuning on single GPU using bf16 checkpoint + fused backwards pass. RTX 3090 runs at about 15s/it for 720p images
  - *From: seruva19*

- **Character LoRAs trained on 2.2 T2V don't work well for I2V**
  - Character lora trained on 2.2 t2v doesn't work well for i2v, but works great for t2v. Lora trained for 2.1 works for 2.2 i2v better than 2.2 lora
  - *From: scf*

- **Wan 2.2 High/Low training timestep issue discovered**
  - Logit_normal timestep sampling favors middle timesteps, but timesteps are defined as 0.85-1.0 for high model, meaning most training is cancelled out. Switching to uniform sampling works better.
  - *From: ingi // SYSTMS*

- **High model timestep range too narrow for style training**
  - Limiting timesteps to 1.0-0.85 focuses training on motion only in 'pure noise' stage. For style training, need to widen timestep range or remove parameter completely.
  - *From: ingi // SYSTMS*

- **Low model training epoch range for character LoRAs**
  - Best character LoRAs achieved by picking epoch between 15-20 with lowest dip on tensorboard graph, though lower dips don't impact motion and likeness much.
  - *From: el marzocco*

- **Facial likeness quality with small datasets**
  - Facial likeness can be nearly perfect with a dataset of just 30 images using Wan 2.2.
  - *From: artificial_fungi*

- **Wan 2.1 character LoRAs work with Wan 2.2 by injecting only in the low ksampler**
  - For character LoRAs trained on Wan 2.1, they only need to be injected in the low noise sampler in Wan 2.2. Motion LoRAs would require training on both high and low models.
  - *From: Tachyon*

- **Wan 2.2 low model is essentially Wan 2.1 + finetune with more data**
  - The low model can generate videos on its own without the high model and knows very well what the high model does. They separated into two models and specialized each in different parts of the denoising process.
  - *From: Alisson Pereira*

- **Training timestep ranges can be adjusted**
  - Default ranges are 1-0.875 for high and 0.875-0 for low (normalized values), but low model can be trained in full range (1-0) which should be sufficient for characters.
  - *From: Alisson Pereira*

- **Trigger words may be detrimental to training**
  - The model thinks the trigger word is written text somewhere in the image/video, so it tries to render that during training and inference. Using descriptive captions without trigger words leads to better results.
  - *From: flo1331*

- **Video training produces better results than image training**
  - Videos are far better than images for everything, including character LoRAs. Image training degrades motion quality.
  - *From: flo1331*

- **Character bleeding into background characters is unavoidable**
  - It's not possible to train character LoRAs without them bleeding onto other people in the scene - this is normal and expected behavior.
  - *From: flo1331*

- **People commonly use 0.0003 learning rate for LoRAs which can destroy training**
  - Using learning rates around 0.00002 works better for character LoRAs
  - *From: shotgun messiah*

- **Overclocking 5090 speeds up training by 10%**
  - Iteration time reduced from 10.7s to 9.7s
  - *From: el marzocco*

- **High noise LoRA is necessary to see effects for style training**
  - Low noise only training showed almost no impact until high noise was added
  - *From: oumoumad*

- **Training images from single photo shoot with different poses works better than random images**
  - 12 images from one photo shoot had much lower loss than 30 random images of same person
  - *From: el marzocco*

- **force_constant_lr parameter for Diffusion Pipe**
  - You can add 'force_constant_lr = 6e-5' (whatever LR you want) in the .toml file to change learning rate when resuming training
  - *From: JohnDopamine*

- **AI Toolkit has built-in VAE and encoder for training**
  - AI toolkit doesn't use separate VAE and encoder files - it only uses the base model for training since it has its own built in VAE and encoder
  - *From: Ryzen*

- **init_from_existing parameter for continuing training**
  - Use init_from_existing = '/data/diffusion_pipe_training_runs/something/epoch50' to take the previous trained lora as the start of next training run
  - *From: jikan*

- **Different rank settings for high vs low noise LoRAs**
  - Training Wan 2.2 High Noise loras at rank 8 and low noise loras at rank 32 - high noise loras barely need to know about your concept/character
  - *From: Kytra*

- **High noise model training duration**
  - Training high noise loras for like 2 epochs appears sufficient as long as the low noise lora is trained adequately
  - *From: Kytra*

- **BF16 training mode uses FP8 scaled models**
  - BF16 is for fp8 scaled models, FP16 is for fp16 models - this was causing training failures when using wrong combination
  - *From: Ryzen*

- **Video training resolution limit**
  - Video training should be at 256x resolution max, not 512x, to avoid VRAM issues and stalling
  - *From: Ryzen*

- **Wan frame rate calculation**
  - Wan uses 16 fps base, so for 3 second videos use 16x3=48 frames. 41 frames equals 2 seconds
  - *From: Ryzen*

- **Trigger words don't work well**
  - Trigger words don't really work in Wan training. Motion LoRAs work even without them if you describe the action
  - *From: Tachyon*

- **Wan 2.2 high model affects motion quality even for single image training**
  - Using both high and low models together increases motion quality, even when training on images
  - *From: Dream Making*

- **High model is responsible for motion, camera control and basic shapes**
  - The high model handles all the motion, camera control and basic shape of things in Wan 2.2
  - *From: crinklypaper*

- **Low model handles face details for character LoRAs**
  - The face details are handled by the low model, while high model picks up hairstyle and other features
  - *From: Dream Making*

- **Training loss in Wan 2.2 shows different patterns than 2.1**
  - 2.2 loss graphs zigzag up and down but average drops over time, unlike 2.1 where flatlining indicated overtraining
  - *From: crinklypaper*

- **JoyCaption has memory management between captions**
  - JoyCaption has a way of dumping memory between captions, preventing OOM issues that affect Qwen captioning
  - *From: el marzocco*

- **AI Toolkit now supports multi-model training**
  - Latest version of AI Toolkit supports training multiple models simultaneously
  - *From: Ryzen*

- **Wan 2.1 character LoRAs can achieve 100% resemblance**
  - User reports excellent character likeness with 2.1 training
  - *From: Tachyon*

- **Wan 2.2 low noise curve zigzags wildly during training**
  - Training loss shows erratic patterns with spikes and dips
  - *From: Tachyon*

- **Wan 2.2 high noise shows gradual slope loss pattern**
  - More predictable training curve compared to low noise
  - *From: Tachyon*

- **Training video-only datasets takes longer to converge than image datasets**
  - Video-only training requires more steps compared to image training
  - *From: Ryzen*

- **AI Toolkit now has RamTorch built-in**
  - Added 2 weeks ago, attempts to offload linear functions in models as they are used from ram to vram to increase speed
  - *From: Ryzen/Kiwv*

- **More captions speed up model training**
  - Having no prompt requires the lora to do much more work
  - *From: Kiwv*

- **BF16 training works for both FP8 and FP8_scaled models**
  - If you train BF16 it also works for FP8 models
  - *From: Ryzen*

- **I2V training takes first frame of video and tells model to predict the rest**
  - When you train a video on image to video, it takes the first frame of that video then tells the model predict the rest
  - *From: Kiwv*

- **Learning rate 2e-5 is more stable than 1e-4 for Wan LoRA training**
  - 1e-4 was unstable and caused overfitting, while 2e-5 provided stable results
  - *From: Ryzen*

- **5e-5 learning rate causes overfitting around 700 steps with 4 videos**
  - Started overfitting too quickly compared to 2e-5
  - *From: Ryzen*

- **Multi-dataset LoRAs optimize more prevalent concepts first**
  - When training multiple concepts, the model optimizes the more common one until it becomes too hard, then moves to other concepts
  - *From: Kiwv*

- **I2V training is faster than T2V training**
  - I2V trains much faster than T2V according to user experience
  - *From: Kiwv*

- **Hand captioning causes faster convergence in training**
  - Manual captioning leads to quicker model convergence compared to automated methods
  - *From: Kiwv*

- **LoRAs can work in both high and low WAN 2.2 slots**
  - Same LoRA can be plugged into both high and low model slots for better results
  - *From: Thom293*

- **WAN 2.2 high+low setup works for images**
  - Use high model without LoRA + low model with LoRA, or same LoRA in both slots
  - *From: Thom293*

- **Dataset size doesn't affect training time**
  - Step time depends on batch size, not total video count. Batch size of 2 means each step processes 2 videos regardless of dataset size
  - *From: Kiwv*

- **Regular T2V LoRAs work with WAN Animate**
  - Normal WAN 2.2 T2V LoRAs are compatible with WAN Animate, though animate-specific training is better
  - *From: Kiwv*

- **AdamW optimizer generalizes well at batch size 1 due to EMAs**
  - Default betas [0.9, 0.999] means it's influenced by approximately the last 10 and 1000 steps for gradients and squared gradients respectively. Equivalent results from lr=1e-4, batchsize=1, steps=1000 vs lr=2e-4, batchsize=4, steps=250
  - *From: spacepxl*

- **Proper captioning and sufficient data is crucial for LoRA training success**
  - Data quality and quantity matters more than just training parameters
  - *From: Kiwv*

- **256x256 resolution is sufficient for effective LoRA training**
  - Can train locally on 4080 with 16GB in half the time compared to higher resolution training
  - *From: oskarkeo*

- **Resolution stepping works in ai-toolkit**
  - Can train lower resolution and increase it for last couple thousand steps - delete cached embeddings first and load from checkpoint
  - *From: crinklypaper*

- **Gemini 3.0 Pro provides excellent video comprehension for captioning**
  - First good video captioner available, can be used to improve WAN prompt adherence
  - *From: Juampab12*

- **Training only low noise model works well**
  - Can train just the low noise model instead of both high and low, works effectively for some use cases
  - *From: Thom293*

- **Wan 2.2 can be trained in dual mode on 12gb 3060**
  - Can train Wan 2.2 LoRA on a 12gb 3060 with 32gb RAM in dual mode, produces one file that works in both high and low
  - *From: artificial_fungi*

- **Pixel space training breakthrough**
  - New method allows training diffusion models directly on pixels without VAE, using naive patching and reparameterizing clean output to velocity during training
  - *From: spacepxl*

- **Character consistency in multi-character scenes**
  - Using character tags + detailed descriptions (outfit, appearance) at end of prompt gives near 100% character accuracy
  - *From: crinklypaper*

- **Context windows can be used with pipe separators for smooth multi-prompt generation**
  - Using | to separate prompts allows generating multiple video segments in one workflow (e.g., 81 frames * 9 generate = 729 frames/45sec)
  - *From: avataraim*

- **Training on 256 resolution with finishing on higher resolution works well**
  - Train on 256 for 100+ epochs, then finish with higher res (640p/800x512) for just a few epochs to add detail
  - *From: Thom293*

- **Mixed character/group shots help reduce bleeding in character LoRAs**
  - Dataset should include both solo characters and mixed group scenes to prevent all characters looking the same
  - *From: crinklypaper*

- **Full timestep range (0-1000) training for low model covers gaps with speed LoRAs**
  - Training low model on 0-1000 instead of 0-875 covers missing timesteps when using lightning LoRAs that have fewer steps
  - *From: crinklypaper*

- **Living LoRAs allow mid-training adjustments**
  - Can add/remove dataset folders during training to tweak results, fix issues like blockiness from bad data
  - *From: Thom293*

- **Dyno high model performs best structurally**
  - User found Dyno lora on high makes things more stable structurally compared to other options
  - *From: b̶̈́͠o̶̗̅n̶̽̒k̵̽̿*

- **Training 256x256 resolution gives acceptable quality for character loras**
  - Character loras trained at 256x256 resolution look fine and train much faster locally
  - *From: oskarkeo*

- **Resume training with lower learning rate for better results**
  - Start with high LR, when reaching overfitting go back 1/4 or 1/2 steps and resume with half the LR or lower for extremely good loras
  - *From: mrassets*

- **Training on full timestep range works for simple concepts**
  - You can train the low model on full range, works fine for simple stuff if you don't want to train both models
  - *From: Thom293*

- **Mixed caption length strategy improves flexibility**
  - 20-30% very long captions (500 tokens), 25% medium length, 50% shorter captions makes model less dependent on big detailed prompts but capable of using them
  - *From: shotgun messiah*

- **NF4 quantization provides significantly higher quality than unscaled fp8**
  - NF4 version of 14b model is only 7.3 GB and uses essentially the QLora recipe
  - *From: spacepxl*

- **Around 18 clips is usually enough for motion training**
  - Based on experience making more than 10 LoRAs
  - *From: vuuw*


## Troubleshooting & Solutions

- **Problem:** Diffusion-pipe seeing wrong frame count (40 instead of 41)
  - **Solution:** Leave videos slightly longer than target bucket size or lower bucket size below the actual frame count
  - *From: Cseti*

- **Problem:** LoRA not showing any effect during training
  - **Solution:** Increase LoRA rank (32 may not be enough), try rank 64-128, and test with basic workflows without custom nodes
  - *From: DiXiao*

- **Problem:** ModuleNotFoundError: No module named 'wan' in diffusion-pipe
  - **Solution:** Run 'git submodule update' to get wan2_1>wan folder in submodules directory
  - *From: Hashu*

- **Problem:** StopIteration error in diffusion-pipe training
  - **Solution:** Frame count mismatch - videos need to match or exceed the frame bucket size specified
  - *From: DiXiao*

- **Problem:** LoRA format incompatibility between trainers
  - **Solution:** Use conversion script to convert between Diffusers format and ComfyUI format
  - *From: DiXiao*

- **Problem:** Double diffusion_model key appears after LoRA conversion
  - **Solution:** Add replacement: fixed = fixed.replace('diffusion_model.diffusion_model.', 'diffusion_model.')
  - *From: DiXiao*

- **Problem:** Memory leak in Musubi trainer causing OOM after 241 steps
  - **Solution:** Issue reported, may need different memory management approach
  - *From: 片ヨ亡亡丹片*

- **Problem:** RuntimeError about tensor size mismatch during training
  - **Solution:** Crop all images so their sizes are divisible by 16
  - *From: seitanism*

- **Problem:** LoRA weight needs to be set to 0.02 instead of 1.0 due to alpha settings
  - **Solution:** In musubi-tuner alpha=1 by default vs alpha=rank in other trainers, adjust LoRA weight accordingly
  - *From: mamad8*

- **Problem:** Model not learning anything with 13 frames after 1000 steps
  - **Solution:** Bumping learning rate to 1e-4, 13 frames seems problematic compared to 33 frames or 1 frame
  - *From: mamad8*

- **Problem:** Generated video not finishing completely, only learning half the motion despite training on full 48 frames
  - **Solution:** Potentially needs some clips of the latter half of the motion in training data
  - *From: DevouredBeef*

- **Problem:** I2V LoRA showing no change when applied
  - **Solution:** Test with image in style of training data to see difference. For style training, use realistic first frame then switch to target style from frame 2
  - *From: spacepxl*

- **Problem:** OOM errors with diffusion-pipe default block-swapping value of 20
  - **Solution:** Increase block-swapping value to 32
  - *From: JohnDopamine*

- **Problem:** Continue training from safetensors checkpoints in musubi
  - **Solution:** Use --network_weights parameter (undocumented feature)
  - *From: mamad8*

- **Problem:** KeyError: 'latents_image' when training I2V without image dataset
  - **Solution:** Use --clip in the latent cache, and for I2V training with musubi just set one dataset for videos - it will pick up the first frame as the init image
  - *From: Juampab12*

- **Problem:** LoRA only learning half the motion/video length
  - **Solution:** 
  - *From: Juampab12*

- **Problem:** Image resolution squishing in diffusion-pipe
  - **Solution:** Set resolution parameter as [512][1024] instead of [512, 1024] to avoid squishing images
  - *From: Cubey*

- **Problem:** Training on pure images results in very static video generations
  - **Solution:** Caption images as 'an image of...' or 'a still image of...' to avoid static generation issue
  - *From: CJ*

- **Problem:** Musubi trainer broke without changing anything
  - **Solution:** Issue was incompatibility with latest pydantic version, despite no version being listed in requirements.txt
  - *From: Juampab12*

- **Problem:** Pipeline parallelism failing in diffusion-pipe
  - **Solution:** Still working on fixes, consistently fails for some users while working for others with identical configs
  - *From: Benjaminimal*

- **Problem:** Training on aging timelapse videos produced poor results
  - **Solution:** Use frame repetition technique (1,2,2,2,2,5,5,5,5...) to avoid VAE compression artifacts from rapidly changing frames
  - *From: Juampab12*

- **Problem:** Discord videos not loading properly
  - **Solution:** Appeared to be a Discord issue affecting multiple users, not related to encoding
  - *From: Jas*

- **Problem:** I2V LoRA not learning grid transformation effect
  - **Solution:** Remove frame bucket '1' and use only frame counts that match video lengths (e.g., [25, 33]). Also change video_clip_mode setting and use descriptive captions instead of triggers
  - *From: mamad8*

- **Problem:** Training on wrong dataset accidentally
  - **Solution:** Always verify you're running from correct folder with intended dataset
  - *From: Juampab12*

- **Problem:** Runpod loading page stuck
  - **Solution:** Check if antivirus (like Avast) or adblock is blocking runpod
  - *From: mamad8*

- **Problem:** Cloud training setup issues
  - **Solution:** Use 'screen' command in terminal to prevent losing training progress when connection drops, use 'screen -r' to reconnect
  - *From: mamad8*

- **Problem:** KeyError: 'y' when training Wan LoRA
  - **Solution:** Found solution in GitHub issue #136
  - *From: Aleksei Naumov*

- **Problem:** Training loss not decreasing after 30 epochs
  - **Solution:** Loss being noisy is normal, check for average decrease trend and use tensorboard smoothing
  - *From: Cseti*

- **Problem:** WSL performance issues
  - **Solution:** Always have models inside WSL and not on Windows, as this impacts speed extremely
  - *From: Alisson Pereira*

- **Problem:** 14B T2V style LoRA not working after 3k steps on 150 images
  - **Solution:** Various potential causes: 1.3B too small, low rank, wrong learning rate, not enough data
  - *From: ingi // SYSTMS*

- **Problem:** Person LoRA producing only backs of heads, avoiding faces
  - **Solution:** No definitive solution provided, likely training data or settings issue
  - *From: ingi // SYSTMS*

- **Problem:** Multiple trigger words not working in 1.3B LoRA
  - **Solution:** 10 images with second trigger word out of 150 total may not be enough data
  - *From: ingi // SYSTMS*

- **Problem:** Block swapping breaks validation set in diffusion-pipe
  - **Solution:** Bug reported on GitHub, fix expected soon
  - *From: Payuyi*

- **Problem:** Camera movement LoRA training very difficult
  - **Solution:** May be limitation of I2V implementation where clip_vision focuses heavily on subject, making it hard to break away
  - *From: ArtOfficial*

- **Problem:** Gemini API limiting to ~5 videos before hitting free tier limit
  - **Solution:** Use Qwen2.5-VL locally instead for larger datasets
  - *From: Cseti*

- **Problem:** Runpod H100 instances being extremely slow
  - **Solution:** Create new pod before destroying old one to avoid getting slow instance again
  - *From: Cseti*

- **Problem:** Loss jumping at epoch boundaries
  - **Solution:** Increase warm up steps and lower learning rate
  - *From: JohnDopamine*

- **Problem:** Depth control being ignored during training
  - **Solution:** Add timestep shift (shift=5) to make model pay attention to depth signal
  - *From: spacepxl*

- **Problem:** OOM issues with 24GB VRAM for captioning
  - **Solution:** Lower fps parameter or max_pixels parameter in config
  - *From: Cseti*

- **Problem:** Control LoRA training on base Flux giving catastrophic results
  - **Solution:** Use Wan instead or try different training approach
  - *From: mamad8*

- **Problem:** Mixed aspect ratios in dataset when expecting squares
  - **Solution:** Check dataset pipeline - bucketing should crop to square if set correctly. Consider leaving mixed ratios as they may generalize better
  - *From: Juampab12*

- **Problem:** Training loss appears too low for meaningful training
  - **Solution:** For image-to-image LoRAs, low loss is normal since output is very similar to input. Test after first epoch to evaluate actual performance
  - *From: Juampab12*

- **Problem:** LoRA not showing adherence to trigger word
  - **Solution:** Make trigger word the first token in captions, followed by 'in the style of [trigger word]'. Ensure trigger word is consistently at beginning of all captions
  - *From: Kytra*

- **Problem:** Camera movement training not converging with mixed movements
  - **Solution:** Train exact same movement every time. Mixed pan directions resulted in stationary camera with objects panning instead. Need consistent movement in dataset
  - *From: ArtOfficial*

- **Problem:** Half of training videos dropped unexpectedly
  - **Solution:** Check that all videos are exactly 81 frames - videos with 80 frames or other counts get dropped by the trainer
  - *From: DevouredBeef*

- **Problem:** Only getting .pt files instead of .safetensors
  - **Solution:** Check save_every_n_epochs setting in config - need to complete at least one epoch to get .safetensors output
  - *From: JohnDopamine*

- **Problem:** 1.3B LoRA training producing noise/bad results
  - **Solution:** Issue may be related to overfitting or dataset preparation. 14B model works fine with same settings
  - *From: Dream Making*

- **Problem:** Dataset cropping to square causing quality issues
  - **Solution:** Default diffusion-pipe crops to square - non-square videos don't look great. Longer training may partially overcome this
  - *From: TimHannan*

- **Problem:** High loss during training
  - **Solution:** Loss trending down significantly but may need more training time to get below 1.0
  - *From: Kytra*

- **Problem:** Converting diffusers LoRA format to ComfyUI
  - **Solution:** Need conversion script, but no standard solution provided
  - *From: Juampab12*

- **Problem:** Training loss not decreasing after 5000 steps
  - **Solution:** Learning rate might be too low, or could be stuck in local minimum - try increasing LR, modifying dataset, changing resolutions
  - *From: Piblarg/Amirsun(Papi)*

- **Problem:** Videos counted as wrong frame count in diffusion-pipe
  - **Solution:** Convert videos to proper 16fps first, trainer takes first frame as still and rest as video frames, need one extra frame than bucket setting
  - *From: ingi // SYSTMS*

- **Problem:** Bitsandbytes installation errors
  - **Solution:** Uninstall and reinstall bitsandbytes
  - *From: Piblarg*

- **Problem:** Video training errors with 'not long enough' despite 5 seconds
  - **Solution:** Bucket settings were wrong, need to match video frame count properly
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** RAM offloading during training
  - **Solution:** It just slows training down by about 20%, doesn't break anything
  - *From: Benjimon*

- **Problem:** LoRA trained on Replicate only works with I2V not T2V despite selecting T2V
  - **Solution:** Bug in trainer - need to set it to I2V then back to T2V again or it trains with I2V even when default shows T2V
  - *From: Fabricatedgirls*

- **Problem:** LoRA contains unexpected module keys error
  - **Solution:** Issue with LoRAs trained on different platforms - use conversion scripts or musubi converter: python convert_lora.py --input input_lora.safetensors --output converted_lora.safetensors --target default
  - *From: Benjimon*

- **Problem:** Size buckets being dropped during training
  - **Solution:** Issue was gradient_accumulation_steps being set to 4 - if batch_size is effectively higher than available samples in bucket, bucket gets dropped. Set gradient_accumulation_steps to 1.
  - *From: Alisson Pereira*

- **Problem:** Training error with size mismatch warnings
  - **Solution:** Image sizes must be divisible by 16. Also check for correct frame counts - videos need specific frame counts (multiple of 16 +1). Delete cache folder if issues persist.
  - *From: seitanism*

- **Problem:** Slow download speeds on Runpod (55kb/s)
  - **Solution:** Use AWS S3 for transfers - achieved 350 mb/s vs 55kb/s direct download. Issue seems to be specific server location for network storage.
  - *From: ingi // SYSTMS*

- **Problem:** CUDA 12.4 compatibility issues with 5090
  - **Solution:** Support issue is complicated but can run everything on 5090 by compiling some things and using packages from Kijai. Musubi-tuner runs fine on 5090.
  - *From: Alisson Pereira*

- **Problem:** WAN particle and artifact issues in generations
  - **Solution:** Use higher resolution and/or more steps, though it can never be completely avoided
  - *From: TK_999*

- **Problem:** WAN LoRA training showing 0% likeness after 100 epochs
  - **Solution:** Use correct WAN caching commands (wan_cache_latents instead of HV), try lower learning rates like 2e-5 or 3e-5, check dataset with debug mode
  - *From: Benjimon*

- **Problem:** Loss going up during training indicates bad training
  - **Solution:** Adjust learning rate down, target loss should be 0.04-0.1 range
  - *From: Benjimon*

- **Problem:** FAL-trained LoRAs not working locally
  - **Solution:** Issue was fixed by FAL, LoRAs now work right away locally
  - *From: NebSH*

- **Problem:** Diffusion pipe ModuleNotFoundError for wandb despite disable setting
  - **Solution:** Install wandb module even when disabled in config
  - *From: Critorio*

- **Problem:** Git pull conflicts with local changes
  - **Solution:** Move the conflicting file (don't copy it) before pulling
  - *From: Benjimon*

- **Problem:** CUDA compilation error with Triton
  - **Solution:** Ensure CUDA v11.6 is installed with full toolkit, set environment variables, install Visual Studio Build Tools with C++ workload, reinstall Triton with correct CUDA support
  - *From: 1338823500949098526*

- **Problem:** Massive loss values during training
  - **Solution:** Check for extra transformer model files in the wan-14b-t2v folder - even removed from config, they can still be included in checkpoint and cause issues
  - *From: MatiaHeron*

- **Problem:** Captions not matching images after batch resize
  - **Solution:** Batch resizing reordered images differently than text captions, causing mismatched pairs
  - *From: gshawn*

- **Problem:** MoviiGen training metadata error
  - **Solution:** Modify musubi-tuner/wan/modules/model.py line 930 to 'info = model.load_state_dict(sd, strict=False, assign=True)' to skip validation of metadata keys
  - *From: BondoMan*

- **Problem:** OOM on 24GB for 14B training
  - **Solution:** Use block swapping optimization, memory optimization changes to train.py file, or train at lower resolution first
  - *From: Thom293*

- **Problem:** Multiple resolutions training setup confusion
  - **Solution:** Copy the 'directory' section at the bottom and point it at a different folder with different settings. Also need to match frame_buckets array length to resolution array length
  - *From: Thom293 and crinklypaper*

- **Problem:** OOM errors on 24GB cards
  - **Solution:** Use float8, reduce rank from 32 to 16, resize images from 512 to 256, add memory enhancement line, use blocks_to_swap
  - *From: crinklypaper*

- **Problem:** LoRA training not working, loss randomly fluctuating
  - **Solution:** Check dataset config file - make sure frame_buckets is properly set, uncomment the correct sections, set proper directory paths
  - *From: Thom293*

- **Problem:** Block swap triggering OOM even with available VRAM on WSL
  - **Solution:** Switch to Musubi Tuner on Windows or turn block swap to zero
  - *From: Neex*

- **Problem:** Slow training iterations on 4090
  - **Solution:** Increase blocks to swap - went from 45-90s/it to 2.9s/it by changing blocks to swap to 14
  - *From: Think*

- **Problem:** SkyCaptioner OOM errors
  - **Solution:** Couldn't get it running locally without OOM, alternative is using Gemini Pro 2.5 for video captioning
  - *From: crinklypaper*

- **Problem:** RuntimeError with missing keys when loading Wan2_1-T2V-14B_fp8_e4m3fn.safetensors
  - **Solution:** Switch to using Wan2.1-T2V-14B-FP16.safetensors instead of the fp8 version
  - *From: Piblarg*

- **Problem:** Musubi Tuner showing 0 samples error
  - **Solution:** Add resolution parameter to dataset config and ensure proper image directory paths
  - *From: Piblarg*

- **Problem:** Musubi Tuner resume shows epoch 1/10 instead of correct resumed epoch
  - **Solution:** This is a cosmetic display issue - training actually resumes correctly from checkpoint despite misleading display
  - *From: Piblarg*

- **Problem:** Training taking 9 hours for one epoch with 3090
  - **Solution:** User miscalculated - actual epoch time was 2.5 hours, which is more reasonable for the dataset size
  - *From: crinklypaper*

- **Problem:** Musubi Tuner not generating samples during training
  - **Solution:** Check sample_every_n_epochs setting and ensure sufficient epochs between sample generation
  - *From: Gill Bastar*

- **Problem:** RTX 5090 not compatible with PyTorch 2.4.1
  - **Solution:** Need torch >= 2.7.0 for Blackwell architecture (RTX 5000 series)
  - *From: Alisson Pereira*

- **Problem:** WSL block swapping OOM errors
  - **Solution:** Use native Windows instead of WSL2 for block swapping functionality
  - *From: MOV*

- **Problem:** Model appears cropped after training
  - **Solution:** Enable bucketing with enable_ar_bucket = true to maintain aspect ratios
  - *From: DiXiao*

- **Problem:** Training on mounted Windows drives in WSL2 is very slow
  - **Solution:** Move all data inside WSL native storage for 4x speed improvement
  - *From: MilesCorban*

- **Problem:** Automagic optimizer requires additional packages
  - **Solution:** Install optimum and optimum-quanto packages: pip install optimum optimum-quanto
  - *From: Alisson Pereira*

- **Problem:** CUDA out of memory error trying to allocate 343.78 GiB
  - **Solution:** Caused by forgetting to do 'accelerate config' step first before starting training on Musubi Tuner - need to run accelerate config
  - *From: Persoon*

- **Problem:** LoRA doesn't activate for certain prompts even at 20k steps
  - **Solution:** Add 'animation' to trigger words as workaround, or make prompts more literal/simple to avoid base model bias toward realistic over animated style
  - *From: Cseti*

- **Problem:** Blurry outputs after resizing videos too much with ffmpeg
  - **Solution:** Generate on 720p with lightx lora removed blur, or use higher bitrate when resizing
  - *From: crinklypaper*

- **Problem:** Training showing one epoch every 24 minutes with 72 steps per epoch
  - **Solution:** Check if gradient_accumulation_steps = 4 is making it take 4 steps before updating weights
  - *From: Persoon*

- **Problem:** DeepSpeed NCCL backend fails on WSL2 with RTX 5000 Ada
  - **Solution:** Issue with NCCL incompatibility on sm_89 architecture - may need different approach or direct python train.py instead of deepspeed launcher
  - *From: 674183054125694987*

- **Problem:** RuntimeError: Processed dataset was empty due to frame bucket mismatch
  - **Solution:** Add buffer frame buckets around target frame count (e.g., [30,31,32,33,34,35] for 33-frame videos) or use catchall bucket [1,33,65]
  - *From: crinklypaper*

- **Problem:** Flash attention compilation sits for hours doing nothing
  - **Solution:** Use prebuilt wheels instead - found working wheel at https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.3.12/flash_attn-2.8.0+cu128torch2.7-cp311-cp311-linux_x86_64.whl
  - *From: Persoon*

- **Problem:** Torch 2.6 and torchvision 0.21.0 dependency conflicts
  - **Solution:** Use torch 2.7 with cuda 12.8 instead, prebuilt wheels available on PyTorch GitHub
  - *From: Faust-SiN*

- **Problem:** Automagic doesn't work with WAN training initially
  - **Solution:** Remove 'stabilize' and 'betas' parameters to get Automagic working with WAN training
  - *From: MatiaHeron*

- **Problem:** Merging two LoRAs gives worse results than running separately
  - **Solution:** No specific solution provided, appears to be inherent limitation
  - *From: Persoon*

- **Problem:** Training errors with torch compile
  - **Solution:** Install Visual Studio 2022 and use proper launch script with xformers or sdpa attention
  - *From: Guey.KhalaMari*

- **Problem:** Diffusion-pipe extremely slow on 4090
  - **Solution:** Don't use AI-generated settings, use blockswap properly, separate image/video folders, use gradient accumulation 1-2 not 4, train at 480p not 1024p
  - *From: Thom293*

- **Problem:** LoRA overtraining with bright flickering
  - **Solution:** High resolution training makes WAN latch onto imperfections more - be careful with very high res datasets
  - *From: Persoon*

- **Problem:** Character identity not appearing in training
  - **Solution:** Need more steps - character LoRAs typically stabilize around 1400 steps, best results around 2700 steps with similar dataset size
  - *From: crinklypaper*

- **Problem:** DiffSynth training on Wan 2.2 producing LORAs with no effect
  - **Solution:** Switch to diffusion-pipe instead of DiffSynth for better results. Multiple users reported DiffSynth waste of time for 2.2
  - *From: mamad8*

- **Problem:** Training extremely slow at 74s/it on 5090
  - **Solution:** Use diffusion-pipe instead of DiffSynth, and enable block swapping for VRAM management
  - *From: mamad8*

- **Problem:** fp8 scaled keys not working in Musubi with 14b high noise
  - **Solution:** Use fp16 checkpoints with fp8 scaled training flag, don't use pre-scaled checkpoints
  - *From: seruva19*

- **Problem:** Flash attention compilation fails on RTX 5090 with kernel errors
  - **Solution:** Use torch 2.7.0+cu128 and install specific wheel: flash_attn-2.8.1+cu12torch2.7cxx11abiTRUE-cp311-cp311-linux_x86_64.whl from official flash-attention repo
  - *From: mamad8*

- **Problem:** WSL training performance issues
  - **Solution:** Keep all files (dataset, models) inside WSL, allocate sufficient RAM, and avoid reading from Windows filesystem due to huge slowdown
  - *From: Alisson Pereira*

- **Problem:** RuntimeError: stack expects different tensor sizes in dataset
  - **Solution:** Use double brackets for resolution specification: [[1024, 1024]] instead of [1024, 1024]
  - *From: crinklypaper*

- **Problem:** transformers PreTrainedModel import error
  - **Solution:** Install missing dependencies: pip install optimum and pip install optimum-quanto
  - *From: crinklypaper*

- **Problem:** High model LoRA training not working effectively
  - **Solution:** High model LoRA should only be used for 1/8 of inference steps since it's trained on small timestep range (0.875-1)
  - *From: ArtOfficial*

- **Problem:** Training produces NaN values and fails
  - **Solution:** Use fp16 models instead of fp8_scaled models for training
  - *From: MilesCorban*

- **Problem:** Tensorboard not loading on mobile
  - **Solution:** Use desktop/PC to view tensorboard graphs properly, mobile has display issues
  - *From: CJ*

- **Problem:** Character LoRA making fingers instead of male genitals
  - **Solution:** Train LoRA specifically with 2.2 models instead of using 2.1 trained LoRAs, or the model may be censored
  - *From: Kenk*

- **Problem:** High noise character LoRA not recognizable even at 8 steps
  - **Solution:** Use low noise model for character training, high noise is for motion/shapes
  - *From: Kenk*

- **Problem:** VRAM residue left after caching process
  - **Solution:** Stop and restart the process after caching is complete to free up more VRAM
  - *From: Kenk*

- **Problem:** Low noise model training not smooth compared to high noise
  - **Solution:** Consider training low noise for full 0-1 timestep range instead of restricted range
  - *From: CJ*

- **Problem:** Training both high and low timesteps together can mess with optimizer
  - **Solution:** Train high and low models separately with appropriate timestep ranges
  - *From: mamad8*

- **Problem:** Character LoRA appears overcooked and hazy
  - **Solution:** Check loss values - may need to stop training earlier around 0.07 for low noise models
  - *From: CJ*

- **Problem:** NSFW LoRA trained on only images loses motion physics
  - **Solution:** Include some video data to maintain proper physics during motion
  - *From: CJ*

- **Problem:** fp8_scaled format won't work for training
  - **Solution:** Must use bf16 or regular fp8 weights, not fp8_scaled format which has wrong weight values and scaling factors
  - *From: mrassets*

- **Problem:** Testicles getting deformed during NSFW training
  - **Solution:** Model appears heavily censored, need to include more penis closeups in dataset and describe genitals explicitly in captions
  - *From: Kenk*

- **Problem:** Skycaptioner hallucinating too much
  - **Solution:** Adjust fps, resolution parameters, and use repetition penalty to control hallucinations
  - *From: mrassets*

- **Problem:** UMT5 missing error in diffusion-pipe
  - **Solution:** Need full folder structure with config files and VAE, use huggingface-cli download excluding large model files
  - *From: MilesCorban*

- **Problem:** Wrong model error when switching from low to high model training
  - **Solution:** Need to update timesteps for high model: min_t=0.875, max_t=1.0, not just swap the model
  - *From: aipmaster*

- **Problem:** ValueError about tensor shape mismatch when loading high model
  - **Solution:** Was accidentally using I2V model instead of T2V model - check model file carefully
  - *From: Critorio*

- **Problem:** Face merging into blobby faces with big heads after epoch 80
  - **Solution:** Likely overfitting - test LoRA at earlier epochs like epoch 20, or adjust lr_bump to escape local minimum
  - *From: Alisson Pereira*

- **Problem:** LoRA not showing trained image concepts/outfits
  - **Solution:** Training images at 768 resolution with videos may not be effective - need more testing
  - *From: mrassets*

- **Problem:** UMT5 tokenizer destroying custom trigger words
  - **Solution:** Use trigger words that survive UMT5 processing, like 'sucking a lolipop' instead of explicit terms, test tokens beforehand
  - *From: mrassets*

- **Problem:** Penis appearing as extraterrestrial/weird shapes in NSFW LoRAs
  - **Solution:** WAN censorship converts penises to fingers, need to use euphemisms like 'human-lolipop' that UMT5 understands
  - *From: Kenk*

- **Problem:** Blurry results when training at higher resolution
  - **Solution:** Training at 720 can look worse than 512 - resolution needs to match dataset quality
  - *From: Kenk*

- **Problem:** Flash attention installation failures
  - **Solution:** Use conda instead of pip, or try pip install flash-attn --no-build-isolation, or install with --no-deps flag
  - *From: WorldX, Cseti*

- **Problem:** Noisy output when merging Wan 2.2 loras
  - **Solution:** May need to use ComfyUI 'native' model instead of split version, or use KJ nodes lora extractor with adjustable rank
  - *From: Kenk, mrassets*

- **Problem:** I2V training errors in Musubi
  - **Solution:** Change task to i2v-14b (drop the A), ensure proper model files are present for I2V
  - *From: screwfunk*

- **Problem:** Runpod template setup issues
  - **Solution:** Must use GPU with CUDA 12.8 or greater, install miniconda, use Python 3.12 environment
  - *From: CJ*

- **Problem:** Diffusion-pipe config errors
  - **Solution:** Use proper paths - ckpt_path points to base HuggingFace folder, transformer_path points to specific model version
  - *From: Kytra, Alisson Pereira*

- **Problem:** Diffusion-pipe not finding captions despite correct .txt file naming
  - **Solution:** Remove any existing captions.json file - diffusion-pipe looks to this file by default and if misformatted, it ignores individual .txt caption files
  - *From: Kiwv*

- **Problem:** Low noise LoRA training produces fuzzy, faded results
  - **Solution:** Try switching from automagic optimizer to adamw_optimi optimizer, and consider training low noise with only images rather than videos
  - *From: crinklypaper, CJ*

- **Problem:** Training loss staying flat and not decreasing
  - **Solution:** This could indicate overfitting. Test early epochs to see if model already learned the concept. May need to adjust learning rate or increase batch size
  - *From: Alisson Pereira*

- **Problem:** Character LoRA works on T2V but requires very high strength on I2V causing artifacts
  - **Solution:** Switch training approach or try different training frameworks like Diffusion-pipe instead of Musubi
  - *From: screwfunk*

- **Problem:** Missing transformer_path causing potential issues
  - **Solution:** Add transformer_path to .toml config pointing to specific high_noise_model or low_noise_model directory
  - *From: screwfunk, crinklypaper*

- **Problem:** Low noise model refuses to learn or trains poorly
  - **Solution:** Switch from Automagic to AdamW optimizer, use lower batch sizes (2-4), and train for more epochs than with 2.1
  - *From: screwfunk*

- **Problem:** Character LoRAs appear transparent or blurry when moving
  - **Solution:** Could be overfitting on motion blur from dataset, especially with low noise training
  - *From: Persoon*

- **Problem:** LoRA appears to do nothing/no effect
  - **Solution:** Test with lightning LoRAs or 2.1 LoRAs to isolate if the issue is with the low noise model training
  - *From: crinklypaper*

- **Problem:** Training crashes when deleting files during training
  - **Solution:** Be careful not to delete files that are still needed during training process
  - *From: screwfunk*

- **Problem:** OOM errors when training LoRA on 4080 16GB VRAM
  - **Solution:** Use blockswap=36 in musubi, depends on resolution and clip length
  - *From: flo1331*

- **Problem:** Musubi dual training OOM on lower VRAM
  - **Solution:** Add --fp8_scaled flag to arguments to enable training
  - *From: MilesCorban*

- **Problem:** Cannot train on scaled fp8 models
  - **Solution:** Use normal fp16 safetensors instead of scaled versions for training
  - *From: flo1331*

- **Problem:** Training randomly stops progressing
  - **Solution:** Issue may be related to musubi updates, training eventually resumes on its own
  - *From: flo1331*

- **Problem:** OOM issues with dual LoRA training on 32GB VRAM
  - **Solution:** Remove videos from dataset and use only images, or use separate high/low training instead
  - *From: 557733681767120896*

- **Problem:** Musubi compatibility issues with RTX 5090
  - **Solution:** Problem stems from xformers and PyTorch compatibility on Windows - xformers not needed, can use SDPA instead
  - *From: GOD_IS_A_LIE*

- **Problem:** High noise model overtraining when dual training
  - **Solution:** Use separate training for high and low models, or use earlier epochs for high model
  - *From: MilesCorban*

- **Problem:** Motion distortion in trained LoRAs
  - **Solution:** May be caused by undertrained low model - train low model more extensively
  - *From: crinklypaper*

- **Problem:** Cached latents from scaled model causing errors
  - **Solution:** Delete cached latents and regenerate with correct text encoder when switching models
  - *From: Alisson Pereira*

- **Problem:** Motion distortion at 75th epoch with 10k steps
  - **Solution:** Use automatic aspect ratio buckets instead of fixed resolutions, let model determine AR buckets automatically
  - *From: Alisson Pereira*

- **Problem:** Outfit overfitting in character training
  - **Solution:** Caption all clothing details even if you like them, otherwise character trigger gets linked to specific outfit. Describe everything you want to be changeable
  - *From: MilesCorban, GOD_IS_A_LIE*

- **Problem:** JoyCaption node not appearing in ComfyUI
  - **Solution:** Node was restructured - now search for 'JoyCaption' and 'JoyCaption Extra Options' as separate nodes. Try updating to nightly build
  - *From: Canin17*

- **Problem:** Auto split sigma splitting one step past 0.875 mark
  - **Solution:** Noticed issue with automatic sigma splitting timing
  - *From: CJ*

- **Problem:** LoRA overfitting to outfit from training data instead of following prompts
  - **Solution:** Use more diverse dataset (20+ videos with different outfits), describe everything in detail in captions, and lower learning rate to 2e-5
  - *From: flo1331*

- **Problem:** Motion distortion in WAN 2.2 training
  - **Solution:** Fixed by changing resolution settings from fixed aspect ratios to [512] and adjusting ar_buckets to defaults
  - *From: crinklypaper*

- **Problem:** High model overtraining despite loss not flattening
  - **Solution:** Test much lower epochs (2-5) on high model and focus training effort on low model which takes longer to converge
  - *From: screwfunk*

- **Problem:** Character not looking right at normal shift values, only at very high shift like 20
  - **Solution:** May need to readjust timesteps being trained at
  - *From: mamad8*

- **Problem:** Changing dataset mid-training causes issues
  - **Solution:** Better to go full send from start rather than adding videos later - leads to loss spikes and later convergence
  - *From: flo1331*

- **Problem:** RTX 5090 insufficient VRAM for 512 video training
  - **Solution:** Use 256 resolution for video training on 5090
  - *From: Ryzen*

- **Problem:** Motion issues with character LoRA
  - **Solution:** Remove words like 'photograph' from captions as they are detrimental to motion
  - *From: flo1331*

- **Problem:** Poor character LoRA results
  - **Solution:** Try using square 1:1 aspect ratio images instead of portrait mode, and don't let trainer do automatic cropping
  - *From: WorldX*

- **Problem:** Understanding dual training parameters
  - **Solution:** Use 'cache text embeddings' to load captions to disk and offload from GPU when using 'unload TE'
  - *From: Ryzen*

- **Problem:** Training not working with default 0.001 LR
  - **Solution:** LR 0.001 is way too high, should use 1e-6 or 2e-5 for WAN. Default starting point is 2e-5
  - *From: MilesCorban*

- **Problem:** Can't get xformers working
  - **Solution:** With pytorch 2.7.1 it's easier to install xformers. First tried with 2.7.0 and it was horrible
  - *From: Guey.KhalaMari*

- **Problem:** LoRA can't change outfits
  - **Solution:** Caption what you want to be able to change. May be overtrained - try earlier checkpoint or lower strength
  - *From: hablaba*

- **Problem:** Character LoRA showing stomach all the time
  - **Solution:** Need to add images of fully clothed to the dataset for diversity
  - *From: Ryzen*

- **Problem:** Fuzzy/blurry lines in video outputs that appear fine in previews
  - **Solution:** Use dpm++_sde scheduler with shift 8 instead of euler with shift 5. The blur appears to be related to scheduler and shift settings
  - *From: crinklypaper*

- **Problem:** Style LoRA not picking up with dpm++_sde initially
  - **Solution:** Use higher epoch checkpoints (epoch 30 vs epoch 1) and proper shift settings. Style is heavily influenced by shift parameter
  - *From: crinklypaper*

- **Problem:** LoRA overtraining after just 200 steps
  - **Solution:** Use lower rank (16-32 instead of 64), proper learning rate (2e-5), and save checkpoints frequently to use earlier epochs
  - *From: flo1331*

- **Problem:** Motion distortion and fuzzy lines with Lightning/LightX LoRAs
  - **Solution:** Avoid using Lightning/LightX LoRAs for testing as they're broken in many ways with Wan 2.2 T2V, though they work well for I2V
  - *From: crinklypaper*

- **Problem:** Blurry results with motion LoRAs
  - **Solution:** Adjust inference setup to auto switch sigma at 0.875 timestep and use earlier epochs
  - *From: CJ*

- **Problem:** Lightning LoRAs getting bad reputation
  - **Solution:** Issue is lower steps give less room for hitting right timestep - can only hand off at full steps
  - *From: CJ*

- **Problem:** Split sigma node not working
  - **Solution:** Disconnect steps module and set steps manually, turn off noise on second sampler
  - *From: screwfunk*

- **Problem:** I2V training showing no movement
  - **Solution:** Need proper video dataset and sufficient training steps - 5000 steps may not be enough
  - *From: Ryzen*

- **Problem:** AI Toolkit crashing with memory issues
  - **Solution:** Keep restarting job as it gets further each time, uses full fp16 model and quantizes in memory
  - *From: MilesCorban*

- **Problem:** Musubi resolution configuration errors
  - **Solution:** Use brackets instead of quotes: resolution = [256, 256] and edit the .sh script properly
  - *From: Guey.KhalaMari*

- **Problem:** I2V training datasets not working in ComfyUI despite showing success in training samples
  - **Solution:** No definitive solution provided, user still struggling with this issue
  - *From: Ryzen*

- **Problem:** Hand and eye distortions in generated videos
  - **Solution:** Often due to fast movement + low resolution. Close-up shots of eyes moving have no problems
  - *From: crinklypaper*

- **Problem:** White pimples/artifacts appearing in training
  - **Solution:** Lower the low noise model strength, adjust seed, though somewhat random occurrence
  - *From: Kenk*

- **Problem:** Multiple character LoRAs blend together when used simultaneously
  - **Solution:** Training dual character datasets into single LoRA to try maintaining separation (experimental approach)
  - *From: screwfunk*

- **Problem:** KeyError: 'bfloat1' in diffusion pipe training
  - **Solution:** Fix typo in config - change 'type = "van"' to correct model type and check for other typos
  - *From: crinklypaper*

- **Problem:** OOM when training 640x960 at 97 frames
  - **Solution:** Add export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
  - *From: Persoon*

- **Problem:** 2.2 LoRAs not working well for I2V workflows
  - **Solution:** Need to adjust LoRA strength significantly or train character specifically for I2V
  - *From: screwfunk*

- **Problem:** CUDA out of memory errors during training
  - **Solution:** Reduce resolution to 256 or lower, remove videos longer than frame buckets, use single resolution instead of multiple, reduce frame bucket sizes (remove 121 frame bucket)
  - *From: crinklypaper, MilesCorban*

- **Problem:** RuntimeError about expected device type 'float'
  - **Solution:** Use correct syntax without transformer_path pointing to wrong location, ensure no trailing slashes in paths
  - *From: crinklypaper*

- **Problem:** AI toolkit generates videos at freakishly fast speed with plastic anatomy
  - **Solution:** Switch to Diffusion-pipe which produces better results despite being slower and using more VRAM. Ensure frames match to avoid speedup issues
  - *From: mrassets, JohnDopamine*

- **Problem:** Character LoRA appearing static and expressionless
  - **Solution:** Reduce training steps - overtraining on static images causes loss of emotions and motion. 300 steps worked better than 1000 steps
  - *From: MilesCorban, Ryzen*

- **Problem:** Port conflict error EADDRINUSE on port 8675
  - **Solution:** Change port in ui/package.json file by modifying the start script
  - *From: mamad8*

- **Problem:** Wan 2.2 T2V LoRAs don't work on I2V while 2.1 LoRAs work fine
  - **Solution:** No definitive solution found. Suggested checking timestep sampling (use sigmoid instead of logsnr for characters) and ensuring proper inference timestep splits
  - *From: screwfunk*

- **Problem:** I2V training fails with missing key errors
  - **Solution:** Check musubi-tuner GitHub issues for similar errors, try rolling back to previous commit, verify using correct I2V model
  - *From: Kierkegaard*

- **Problem:** Training OOMs with sigmoid timestep sampling
  - **Solution:** Switch to CAME optimizer which takes less memory than Adam with no downside
  - *From: flo1331*

- **Problem:** Loss spikes and goes over 1 with LoRA+
  - **Solution:** Adjust base learning rate when using LoRA+ since it influences the B matrices. Remove LoRA+ temporarily to isolate the issue
  - *From: Kierkegaard*

- **Problem:** Video frames being skipped as too short
  - **Solution:** Issue with Diffusion Pipe frame bucket requirements. Found solution at https://github.com/tdrussell/diffusion-pipe/issues/391#issuecomment-3208653177
  - *From: ingi // SYSTMS*

- **Problem:** Character LoRA bleeding across all people on screen
  - **Solution:** Add regularization data - few clips of other random people without trigger word in caption. Should make loss higher if bleed happens
  - *From: samurzl*

- **Problem:** Captioning mistakes causing unwanted features
  - **Solution:** Forgot to caption studded belt and all people started getting studded belts. Fixed captions and no more belts appearing
  - *From: crinklypaper*

- **Problem:** Training loss showing unexpected patterns
  - **Solution:** For 2.2, ignore the actual loss numbers and focus only on the trend. High model shows C-shape (smooth), low model shows jagged staircase pattern
  - *From: crinklypaper*

- **Problem:** Hand and face issues in generated videos
  - **Solution:** Lower LoRA strength to 0.5-0.6 for low noise model can fix hand and face distortion issues caused by overtraining
  - *From: Kierkegaard*

- **Problem:** Wan 2.2 High LoRA not working/no effect visible
  - **Solution:** Change timestep_sample_method from 'logit_normal' to 'uniform' in training config
  - *From: ingi // SYSTMS*

- **Problem:** Error with Wan 2.2 VACE - skip first frames pushed past end of video
  - **Solution:** Set frame rate to native video fps or force to 16 to compute offset correctly
  - *From: spacemathapocalypse*

- **Problem:** JoyCaption nodes completely broken/not loading
  - **Solution:** Issue appears related to recent ComfyUI frontend changes, recommend asking in ComfyUI channel
  - *From: Thom293*

- **Problem:** Wan 2.1 LoRA works fine for 2.2 T2V but needs higher strength for 2.2 I2V
  - **Solution:** Wan 2.1 T2V LoRAs work enough for Wan 2.2 T2V Low Model but are weaker on Wan 2.2 I2V models. Increasing strength didn't work well as a patch.
  - *From: Guey.KhalaMari*

- **Problem:** Character likeness bleeding into background characters
  - **Solution:** Use more detailed captioning instead of just trigger words. However, some bleeding is unavoidable and normal.
  - *From: Tachyon*

- **Problem:** OOM error when resuming from checkpoint but not on initial training
  - **Solution:** User got it working again but unclear on exact solution
  - *From: crinklypaper*

- **Problem:** CMAKE and llama-cpp errors when installing JoyCaption2 in ComfyUI
  - **Solution:** Use a virtual environment (venv) to alleviate dependency issues, or try the standalone GitHub version instead
  - *From: shotgun messiah*

- **Problem:** Wan LoRA showing no impact when applied
  - **Solution:** Need to train high noise model in addition to low noise, especially for style effects
  - *From: oumoumad*

- **Problem:** Docker volume growing and not shrinking when files deleted
  - **Solution:** Move files to Trash-0 folder and empty it, or use CLI deletion instead of JupiterLab
  - *From: el marzocco*

- **Problem:** Learning rate graph showing weird behavior when resuming training in Musubi
  - **Solution:** Potential bug when resuming from previous state
  - *From: Persoon*

- **Problem:** OOM errors during training
  - **Solution:** Don't put videos in images folder - separate them properly
  - *From: crinklypaper*

- **Problem:** Diffusion Pipe attention_dispatch module error
  - **Solution:** Downgrade diffusers from 0.35.1 to 0.34.0 or between 0.32.2-0.34.0 due to recent changes in diffusers library that diffusion-pipe hasn't caught up to
  - *From: Kytra*

- **Problem:** AI Toolkit transformer config.json not found error
  - **Solution:** AI toolkit requires the entire diffusers repo format, not just safetensors files - need to clone the entire repo from HuggingFace
  - *From: Tachyon*

- **Problem:** RAM filling up during training causing crashes
  - **Solution:** Issue likely caused by model switch feature - try training without switching models every 10 steps
  - *From: crinklypaper*

- **Problem:** Overcooked LoRA from limited second run data
  - **Solution:** When resuming training with limited data (all close-ups of fruit), the resulting LoRA put way too many fruits all over scenes
  - *From: ingi // SYSTMS*

- **Problem:** Wan 2.1 LoRAs not working well with Wan 2.2 I2V
  - **Solution:** Boost lora strength to 1.5+ when using Wan 2.1 T2V loras with Wan 2.2 I2V
  - *From: Tachyon*

- **Problem:** Windows command line syntax error with backslashes
  - **Solution:** Replace backslashes (\) at end of lines with ^ for Windows, or put entire command on single line and remove backslashes
  - *From: Tachyon*

- **Problem:** 5090 VRAM stalling during video training
  - **Solution:** Lower video resolution to 256x256 and reduce fps from 48 to 16
  - *From: Tachyon*

- **Problem:** No movement learning in LoRA after 4000+ steps
  - **Solution:** Use BF16 instead of FP16, and use shift timestep sampling for motion capture
  - *From: Ryzen*

- **Problem:** LoRA not working in Wan 2.2
  - **Solution:** Put LoRA only in low noise sampler, not high noise sampler. Also need minimum 1800 steps (increase epochs)
  - *From: Tachyon*

- **Problem:** Training on Wan 2.1 settings with Wan 2.2 model doesn't work
  - **Solution:** Use Wan 2.1 model with 2.1 settings, or adjust settings for 2.2
  - *From: Tachyon*

- **Problem:** Character doesn't appear after 4.5k steps and 70 epochs
  - **Solution:** Need to train both high and low models, not just one
  - *From: Dream Making*

- **Problem:** No movement/results after 7k steps in AI Toolkit
  - **Solution:** Change learning rate from 2e-5 to 0.0001
  - *From: Ryzen*

- **Problem:** Qwen captioning runs OOM after 5-10 captions
  - **Solution:** Use JoyCaption instead which has better memory management
  - *From: el marzocco*

- **Problem:** Lightning LoRAs cause weird behavior during testing
  - **Solution:** Test LoRAs without lightning LoRAs first
  - *From: crinklypaper*

- **Problem:** Loss stops decreasing for 10-20 epochs or starts going up
  - **Solution:** Training is overtrained, stop and test earlier epochs
  - *From: flo1331*

- **Problem:** Training loss stuck at 1.48 after 38 epochs with 11 images
  - **Solution:** Check dataset captioning, paths, decimals, or switch to different trainer like AI toolkit
  - *From: flo1331*

- **Problem:** AI toolkit recovery adapters don't work for Wan training on 8GB GPU
  - **Solution:** Use float8 quantization or switch to diffusion-pipe, minimum 5090 recommended
  - *From: Kiwv*

- **Problem:** AI toolkit downloading models to C: drive .cache folder
  - **Solution:** Manually download models and modify package to change download location
  - *From: xwsswww*

- **Problem:** AI Toolkit jobs get stuck when trying to stop
  - **Solution:** You have to let it finish before you close the cmd, but it won't stop until a step is completed. Need 24gb minimum GPU, 8gb is too low
  - *From: Kiwv*

- **Problem:** LoRA works in training samples but not ComfyUI
  - **Solution:** Try using default ComfyUI template, check file paths, ensure .safetensors format. Issue may be with FP8 models vs FP16
  - *From: Thom293/Kiwv*

- **Problem:** LoRA only works when trained on high noise but not both high and low
  - **Solution:** Unclear cause, may be configuration issue
  - *From: Ryzen*

- **Problem:** Inconsistent character LoRA results
  - **Solution:** Make character descriptions identical for each image rather than letting Florence2 handle captioning differently
  - *From: metaphysician*

- **Problem:** Gradient accumulation 2 causes OOM errors
  - **Solution:** Use batch size 2 with gradient accumulation 1 instead, or enable layer swapping
  - *From: Ryzen*

- **Problem:** Fuzzy artifacts in I2V output
  - **Solution:** More training steps - this is an artifact of undertraining that resolves with additional steps
  - *From: Kiwv*

- **Problem:** LoRA works on front view but not side view
  - **Solution:** More training steps needed, as long as side view videos aren't less than 5% of dataset
  - *From: Kiwv*

- **Problem:** Multi-dataset LoRA not working well
  - **Solution:** Set caption dropout to 0.5 for trigger words, or train datasets separately then merge
  - *From: Ryzen*

- **Problem:** LoRA still fuzzy after 5000 steps
  - **Solution:** Issue is likely dataset size - need minimum 60 videos, not 20. Most LoRAs require 60+ videos to generalize properly
  - *From: Kiwv*

- **Problem:** Bad image quality at CFG 1.5 with 30 steps
  - **Solution:** CFG 1 and 1.5 are only for fast LoRAs. At 30 steps use CFG 4+ for images
  - *From: Thom293*

- **Problem:** Body distortion in generated images
  - **Solution:** LoRA needs to be trained on target resolutions or it will stretch like SDXL
  - *From: Thom293*

- **Problem:** AI Toolkit showing 124 hours for 11 images on 8GB
  - **Solution:** Training largely on CPU due to VRAM limitations - consider renting GPU or switching to lighter models
  - *From: Kiwv*

- **Problem:** AI toolkit training crashing with 'element 0 of tensors does not require grad' error
  - **Solution:** If everything is default and dataset is correct, try reinstalling AI toolkit
  - *From: Kiwv*

- **Problem:** Learning rate 2e-4 causing training issues
  - **Solution:** Use much lower learning rate like 5e-5. 2e-4 is too high
  - *From: Kiwv*

- **Problem:** AI toolkit training very slow at 50s/it
  - **Solution:** Disable sampling (was defaulted to 1024x1024) and set steps properly when using lowVram setting
  - *From: Baku*

- **Problem:** LoRA only learning one video out of 20
  - **Solution:** Likely all your data is wildly different - training can't find common denominator. You need more consistent data
  - *From: Kiwv*

- **Problem:** All characters in scene looking like LoRA character
  - **Solution:** Caption 'lizardman is a man who has a lizards face' is confusing - describe more literally like 'a lizard man wearing a police uniform sitting at drivers seat'. Describe everything but the aspect you want to learn
  - *From: crinklypaper*

- **Problem:** Training fails due to insufficient data and poor captions
  - **Solution:** Need more videos and better captions - data is key
  - *From: Kiwv*

- **Problem:** ComfyUI breaks when installing QwenVL node due to outdated transformers
  - **Solution:** Update transformers dependency
  - *From: Ryzen*

- **Problem:** LoRA applies to everyone when trained on single person
  - **Solution:** Need data where that doesn't happen or better prompting - partly training a character lora
  - *From: Kiwv*

- **Problem:** ai-toolkit error with WAN 2.2 T2V 14B fp8 model path
  - **Solution:** Use diffusers format model from HuggingFace: Wan-AI/Wan2.2-T2V-A14B-Diffusers or leave link as default and toolkit will download automatically
  - *From: Guey.KhalaMari*

- **Problem:** RuntimeError: DataLoader worker killed by Bus error due to shared memory limit
  - **Solution:** Shared memory issue on /dev/shm - need to configure TEMP dir properly
  - *From: HeadOfOliver*

- **Problem:** High VRAM usage and slow training on 5090
  - **Solution:** Try turning layer offloading to true if not enough RAM to hold 2x14B models
  - *From: oskarkeo*

- **Problem:** 5090 won't train with low vram off
  - **Solution:** Model swapping between high/low requires significant VRAM, use separate training or different setup
  - *From: oskarkeo*

- **Problem:** AI-toolkit gets stuck at 'starting job'
  - **Solution:** Usually downloading 65GB of model files - check network activity, initial download takes time
  - *From: b̶̈́͠o̶̗̅n̶̽̒k̵̽̿*

- **Problem:** Windows page file OOM error during training
  - **Solution:** Increase page file from default 10GB to 32GB to handle RAM requirements
  - *From: Juan Gea*

- **Problem:** RuntimeError: element 0 of tensors does not require grad
  - **Solution:** Error occurs with adamw8bit with sigmoid, common crash during training
  - *From: Albert*

- **Problem:** Resume training causes LR dip in tensorboard
  - **Solution:** Remove warmup steps from config when resuming training
  - *From: flo1331*

- **Problem:** OOM with 16GB VRAM training character LoRA on Wan2.1 14B
  - **Solution:** Use lower resolution, reduce batch size, or try quantization settings
  - *From: Léon*

- **Problem:** Wan2.2 training going from progressing to garbage
  - **Solution:** Monitor for overtraining signs, may need to stop earlier or adjust learning rate
  - *From: boorayjenkins*

- **Problem:** Slow motion outputs from Wan2.2 even with LightX2V
  - **Solution:** Try different LightX2V versions or train motion-specific LoRA
  - *From: dj47*

- **Problem:** Blockiness in outputs from bad training data
  - **Solution:** Remove pixelated/low quality videos from dataset and replace with cleaned versions
  - *From: Thom293*

- **Problem:** Wan Animate doesn't like LoKr format
  - **Solution:** Use standard LoRA format instead
  - *From: boorayjenkins*

- **Problem:** uvloop module not found on Windows
  - **Solution:** uvloop is Linux-only, use LM Studio with 'Enable CORS' toggle for Windows compatibility
  - *From: Gleb Tretyak*

- **Problem:** Training samples corrupted/distorted
  - **Solution:** Issue was not enough training steps
  - *From: Ryzen*

- **Problem:** LM Studio 'messages field is required' error
  - **Solution:** Enable CORS toggle in LM Studio settings
  - *From: Gleb Tretyak*

- **Problem:** Dec17 Lightx2v messing up contrast
  - **Solution:** Issue wasn't just on low model, might be okay when used specifically on low
  - *From: JohnDopamine*

- **Problem:** 5090 bug with LLM backend preventing captioner from working
  - **Solution:** No current fix mentioned, user had to use alternative captioner
  - *From: Thom293*

- **Problem:** Out of memory error during training
  - **Solution:** Lower resolution or split video into smaller clips
  - *From: Duckers McQuack*

- **Problem:** Motion not sticking in training despite detailed descriptions
  - **Solution:** Likely need more training clips - around 18 clips is usually enough for motion
  - *From: vuuw*

- **Problem:** Airbrushy skin texture in LoRAs
  - **Solution:** Use bigger dataset, train longer with network dropout
  - *From: vuuw*


## Model Comparisons

- **WAN vs Hunyuan LoRA quality**
  - WAN LoRAs are much better and easier to train than Hunyuan
  - *From: Cubey*

- **480p vs 720p training resolution**
  - 480p produces better results than 720p for WAN training
  - *From: comfy*

- **1.3B vs 14B training speed**
  - 1.3B is much faster, 14B is slower but works on 24GB VRAM
  - *From: mamad8*

- **WAN vs HYV character distance shots**
  - WAN has issues with character likeness in distant shots that HYV didn't have
  - *From: Cseti*

- **Wan 14B vs 1.3B for character training**
  - 14B produces much better likeness than 1.3B for character LoRAs
  - *From: anever*

- **Hunyuan vs Wan character training results**
  - Hunyuan produced better results with same dataset and fewer training steps
  - *From: zezo*

- **Wan vs Hunyuan training difficulty**
  - Hunyuan more forgiving, but Wan has better likeness when it works
  - *From: Titomus Maximus*

- **NFP4 vs system memory offloading speed**
  - NFP4 quantization 3x faster than offloading to system RAM during inference
  - *From: spacepxl*

- **T2V vs I2V LoRA compatibility**
  - Some movements don't work at all from t2v to i2v (like camera zoom-in). Characters also don't work well in i2v. May need to finetune t2v LoRAs on i2v model
  - *From: mamad8*

- **Trainer comparison for i2v**
  - mamad8 had problems with musubi, moving back to diffusion-pipe for t2v and DiffSynth for i2v. Only worked directly with i2v lora, not needing conversion
  - *From: mamad8*

- **Musubi vs DiffSynth for training**
  - DiffSynth works better - musubi had issues with only learning half the motion, same dataset worked perfectly in diffsynth
  - *From: Juampab12*

- **Training on images vs short videos for character likeness**
  - Short video training (9-13 frames) gives much better results than image-only training. Training on images long enough for likeness causes massive motion problems, while short videos achieve better likeness without motion issues
  - *From: spacepxl*

- **Diffusion-pipe vs other trainers for multi-GPU**
  - Diffusion-pipe consistently uses ~100% of all 8 GPUs, whereas Diffsynth Studio has inconsistent utilization and is slower. Finetrainers is the slowest by far
  - *From: Benjaminimal*

- **Trainer ease of use**
  - Finetrainers takes top marks for ease-of-use with example scripts vs fumbling with 100 flags in others
  - *From: Benjaminimal*

- **Pre-computation speed across trainers**
  - Finetrainers pre-computation takes 30 minutes on 8 GPUs while other trainers take minutes or seconds
  - *From: Benjaminimal*

- **14B vs 1.3B model for LoRA training**
  - 14B model produces much better LoRA results than 1.3b
  - *From: Juampab12*

- **Diffusion-pipe vs Musubi for I2V training**
  - Both work but diffusion-pipe requires additional video_clip_mode setting changes
  - *From: mamad8*

- **RTX 5090 vs RTX 3080ti**
  - Only about 1 minute faster for basic inference, main benefit is VRAM not speed
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 1.3B vs 14B inference speed**
  - 1.3B much faster - 89 frames takes 16 minutes on 14B with 24GB VRAM vs ~3.5 minutes on 1.3B
  - *From: CJ*

- **Training on images vs videos for motion**
  - Training on videos produces more fluid motion, images can make movements more static
  - *From: Alisson Pereira*

- **HYV vs Wan for celebrity/likeness training**
  - HYV produces better recognizable results for human likenesses, Wan results weren't even recognizable
  - *From: JohnDopamine*

- **Musubi vs diffusion-pipe**
  - Musubi was only trainer that worked for one user, but they're all very similar in the end
  - *From: Juampab12*

- **Qwen2.5-VL vs Florence for captioning**
  - Florence makes basic errors like haircolor/position and can't caption videos, while Qwen2.5-VL can handle both images and videos
  - *From: seitanism*

- **Gemini vs Qwen2.5-VL for captioning**
  - Gemini has strict rate limits (~5 videos per minute), Qwen2.5-VL better for large datasets
  - *From: ArtOfficial*

- **Trigger words vs descriptive prompts in Wan**
  - Descriptive prompts work better than trigger words because T5 is too smart and prefers concepts it already knows
  - *From: Juampab12*

- **Network storage vs local storage on Runpod**
  - Network storage is slower but works well, local storage at pod root is faster for model reading
  - *From: Alisson Pereira*

- **Diffusion models vs specialized models for watermark detection**
  - Flux and Wan significantly outperformed YOLO and Uniformer for watermark detection tasks
  - *From: mamad8*

- **Wan 1.3B vs 14B training speed**
  - 1.3B is much easier to work with and faster than 14B
  - *From: mamad8*

- **Wan vs Hunyuan training speed**
  - Hunyuan was much faster and more linear in training progress compared to Wan
  - *From: Dream Making*

- **Multiple GPU training vs single GPU**
  - Training on multiple GPUs is same cost but much faster - 8x H100s for $12/hour vs single GPU for 8+ hours. 10x 3090s available for $2.2/hour on runpod for 1.3B model
  - *From: Kytra*

- **Wan prompt adherence vs other models**
  - Wan 2.1 has incredible adherence to prompts, making detailed captions very useful in training
  - *From: Amirsun(Papi)*

- **14B vs 1.3B for character training**
  - 14B works much better for human likeness training, 1.3B struggles with character consistency
  - *From: JohnDopamine*

- **WAN vs Hunyuan for human training**
  - Hunyuan is much better for training human likenesses, WAN better for I2V
  - *From: JohnDopamine*

- **Different training methods in Musubi**
  - Head method works better than Full method for maintaining likeness in source images
  - *From: JohnDopraine*

- **Fal.ai vs Replicate for training**
  - Replicate has more settings exposed and allows saving checkpoints compared to fal.ai
  - *From: pom*

- **Many Civitai LoRAs vs well-trained LoRAs**
  - Many of these Civitai Loras are poorly trained. They train just to gain visibility/buzz rather than for perfection
  - *From: Alisson Pereira*

- **RTX Pro 6000 vs dual 5090 setup**
  - Could buy 2 5090s and a whole computer and do more things than with 1 RTX 6000 Pro, though RTX 6000 Pro allows HD training
  - *From: Benjimon*

- **RTX Pro 6000 vs 5090 performance**
  - RTX Pro 6000 is 5% faster than 5090 but costs $8500 vs potential $6000 for equivalent 96GB VRAM setup
  - *From: Fabricatedgirls*

- **Musubi Tuner vs Diffusion Pipe**
  - Musubi Tuner easier to install on Windows, Diffusion Pipe harder to set up but more popular
  - *From: Piblarg*

- **Diffusion Pipe vs Kohya's**
  - Diffusion Pipe easiest, Kohya's best/harder with more settings
  - *From: Benjimon*

- **WAN 14B vs 1.3B training memory**
  - 1.3B can be trained on a potato from VRAM perspective, 14B more demanding
  - *From: Piblarg*

- **Musubi Tuner vs Diffusion Pipe**
  - Musubi defaults to Alpha=1 (slower learning, higher LR like 2e-4), Diffusion Pipe uses Alpha=DIM (faster learning, lower LR like 2e-5). Musubi allows video sampling during training
  - *From: JohnDopamine*

- **Base Wan 2.1 vs SkyReels for character training**
  - SkyReels produces much better character likeness results, especially for human faces. Base Wan yielded horrible results for character training
  - *From: JohnDopamine*

- **14B vs 1.3B training**
  - 1.3B sometimes produces better results than 14B on same dataset. 14B requires different captioning approach and more care
  - *From: sneako1234*

- **Float8 vs Float16 training**
  - Float8 works for training with no noticeable quality difference, Float16 may not fit in 24GB VRAM
  - *From: crinklypaper*

- **I2V vs T2V training for motion vs style**
  - I2V is best for motion independent from style, T2V is better for style or character training
  - *From: Piblarg*

- **Diffusion Pipe vs Musubi Tuner**
  - Musubi Tuner worked when Diffusion Pipe had WSL block swap issues
  - *From: Neex*

- **Base Wan vs SkyReels models for training**
  - SkyReels V2 gives much better training results than base Wan
  - *From: JohnDopamine*

- **CAME vs AdamW8bit optimizer**
  - CAME optimizer preferred for results but usually a bit strong so need to compensate with learning rate
  - *From: Persoon*

- **Training 380 images on 3090 vs 5090 performance**
  - 3090 taking 2.5 hours per epoch at 576x768 resolution, while 5090 handles 1024x1024 images at ~7 minutes per epoch
  - *From: crinklypaper*

- **A6000 48GB vs RTX 5090 training speed**
  - RTX 5090 was faster than A6000 despite having less VRAM
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid v1.5 vs v2 for merging**
  - CausVid v2 works better when mixing with other LoRAs, v1.5 gave bad results in combinations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan vs Hunyuan prompt following**
  - Wan has really good prompt following, better at complex multi-character scenes
  - *From: Thom293*

- **T2V vs I2V models**
  - I2V is far superior to T2V according to user experience
  - *From: Amirsun(Papi)*

- **RTX PRO 6000 vs 5090**
  - 5090 is faster than RTX PRO 6000 despite latter having 96GB VRAM
  - *From: Testes*

- **Diffusion-pipe vs Musubi Tuner**
  - Windows best is Musubi, Linux use diffusion pipe - diffusion pipe works great for video models
  - *From: crinklypaper*

- **Training on I2V vs T2V models**
  - Most people gen with 480p model so train on that if you want people to use the lora, but generally train on T2V - T2V lora might work on I2V but I2V lora won't work on T2V
  - *From: CJ*

- **WAN vs HunyuanVideo for training**
  - HunyuanVideo was much better for training, WAN training can be more challenging
  - *From: JohnDopamine*

- **Training on base model vs FusionX**
  - LoRAs perform differently on models they're not trained on - training on base shows LoRA actually works, FusionX may already handle some styles well
  - *From: MilesCorban*

- **1.3B vs 14B model training settings**
  - Settings for 1.3B will not work for 14B model - need different configurations
  - *From: Guey.KhalaMari*

- **AI Toolkit vs Diffusion Pipe for resolution capability**
  - AI Toolkit can train 1280x768 on 5090 with blockswap, while Diffusion Pipe maxes at 640p on same hardware
  - *From: Ryzen*

- **DiffSynth vs Diffusion Pipe for Wan 2.2 training**
  - Diffusion Pipe recommended over DiffSynth for better VRAM management and results
  - *From: mamad8*

- **Hunyuan vs Wan motion retention**
  - Hunyuan kept motion well even with image training, Wan is 'a different beast' - more sensitive to image/video balance
  - *From: CJ*

- **LoKR vs LoRA for Wan training**
  - LoKR produces better quality and prevents concept bleeding better than LoRA, but takes 20-30% longer to train
  - *From: jikan*

- **Training only low model vs training both high and low**
  - Training only low model with full timestep range (0-1) can work for both models, potentially easier than training separate LoRAs
  - *From: Alisson Pereira*

- **Wan 2.1 LoRA on Wan 2.2**
  - 2.1 LoRAs work on 2.2 but not well - either not very effective or need strength turned up, need to use higher strength like 3.0
  - *From: MilesCorban*

- **Wan 2.2 vs Wan 2.1 LoRAs**
  - Training same dataset on Wan 2.2 yields better results than using Wan 2.1 LoRAs on Wan 2.2
  - *From: chancelor*

- **5B model vs 14B model for LoRA training**
  - 5B model appears to give better training results than 14B model
  - *From: Alisson Pereira*

- **High noise vs Low noise for character training**
  - Low noise is much better for character identity/likeness, high noise fails to capture recognizable features
  - *From: Kenk*

- **Wan 2.1 vs 2.2 LoRAs**
  - Wan 2.1 trained LoRAs work on Wan 2.2
  - *From: Lodis*

- **High vs Low noise training stability**
  - High noise training is more stable, low noise shows higher variance
  - *From: CJ*

- **High vs Low noise model training stability**
  - High noise training is much more stable with less loss variance, easier to generate motions and blurry blobs than fine details
  - *From: MilesCorban*

- **WAN 2.1 LoRAs vs 2.2 high/low split**
  - Old 2.1 LoRAs trained on ai-toolkit work better than new high/low split approach
  - *From: aipmaster*

- **Qwen 2.5 VL vs Skycaptioner**
  - Skycaptioner slightly NSFW, never misses anything but has hallucination problems, Qwen 2.5 VL better for images with proper system prompting
  - *From: mrassets*

- **WAN LoRA training vs Illustrious XL**
  - WAN needs 3000+ steps while Illustrious XL can achieve good character at 600 steps due to different architecture
  - *From: TekeshiX*

- **WAN 2.2 vs Hunyuan for NSFW**
  - Hunyuan had NSFW in base model making it easier to train explicit content, WAN is heavily censored
  - *From: Kenk*

- **2.1 LoRA vs 2.2 combination**
  - Using 2.1 LoRA with 2.2 affects quality, better to train dedicated 2.2 LoRAs for both high and low
  - *From: Gentleman bunny*

- **Wan 2.2 vs 2.1 lora compatibility**
  - Using old 2.1 character loras with 2.2 models requires increasing strength, not ideal compatibility
  - *From: Kenk*

- **Tencent Hunyuan vs Wan 2.2 NSFW**
  - Hunyuan appears more NSFW-friendly than Wan 2.2
  - *From: Kenk*

- **GPU cost efficiency for training**
  - H200 vs RTX Pro 6000: similar performance but H200 costs twice as much. 5090 vs Pro 96GB similar for image training
  - *From: Ruairi Robinson*

- **Automagic vs AdamW optimizers for Wan 2.2**
  - Automagic is superior and designed to avoid overfitting on certain dataset aspects, self-adjusts learning rate over time. AdamW keeps same learning rate throughout
  - *From: MatiaHeron*

- **Images vs videos for low noise character training**
  - Low noise benefits simply from images, eliminates headache of two full training runs
  - *From: CJ*

- **Musubi vs Diffusion-pipe for Wan 2.2**
  - Diffusion-pipe reported as 'way better' than ai-toolkit, with faster character training
  - *From: Kiwv, screwfunk*

- **WAN 2.1 vs WAN 2.2 training difficulty**
  - WAN 2.1 was much easier and more reliable for training, especially character LoRAs. WAN 2.1 LoRAs often work better on 2.2 than newly trained 2.2 LoRAs
  - *From: aipmaster*

- **Automagic vs AdamW for low noise training**
  - AdamW performs better for low noise model training, while Automagic works well for high noise
  - *From: screwfunk*

- **High vs Low noise model training speed**
  - High noise trains in minutes (30-40 min), low noise takes hours
  - *From: screwfunk*

- **LightX2V vs Lightning v1.1**
  - LightX2V produces better details but darker/muted colors, Lightning has its own style shift
  - *From: crinklypaper*

- **Wan 2.1 vs 2.2 dual vs musubi dual LoRAs**
  - All three methods produce very similar results for character likeness
  - *From: JalenBrunson*

- **Single LoRA vs separate High/Low LoRAs**
  - Single LoRA is simpler with no quality loss, reduces complexity and storage
  - *From: artificial_fungi*

- **Dual training vs separate training**
  - Mixed results - dual training can cause high model overtraining while low is still good, separate training gives more control
  - *From: MilesCorban*

- **CAME vs Adam optimizer**
  - CAME should be equal to Adam in results but uses less VRAM, helps squeeze out more frames for video training
  - *From: flo1331*

- **High+Low models vs Low only**
  - Camera movement and motions are far better with high model included, but low-only can work for simple concepts
  - *From: flo1331*

- **Rank 16 vs Rank 128 for character training**
  - Rank 16 much faster, focuses on essential details. Higher rank takes longer and can learn unwanted elements like scene lighting
  - *From: Alisson Pereira*

- **K3NK's approach vs traditional character LoRAs**
  - K3NK trains ethnicity/concept rather than specific character consistency, uses generated faces from thispersondoesnotexist.com
  - *From: Alisson Pereira*

- **ai-toolkit vs musubi/diffusion-pipe**
  - ai-toolkit succeeded on first attempt after multiple failed runs with other trainers
  - *From: aipmaster*

- **Musubi vs AI-toolkit for WAN training**
  - Musubi produces better results faster but harder to set up without GUI experience, while AI-toolkit is more user-friendly but may have issues
  - *From: GOD_IS_A_LIE*

- **High vs Low model training importance**
  - Low model is much more important and takes longer - high trains in ~30 minutes, low needs much more time and attention
  - *From: screwfunk*

- **Training with videos vs images only**
  - Videos consistently produce better, more flexible and detailed results without degrading motion
  - *From: flo1331*

- **Wan 2.1 vs 2.2**
  - 2.2 is significantly better quality but 2.1 still needed for users with less powerful hardware
  - *From: WorldX*

- **AI Toolkit vs other trainers**
  - AI Toolkit easier to use but missing features like epochs, LR loss charts. 90% of people use Musubi Tuner instead
  - *From: Ryzen*

- **Training with images+videos vs images only**
  - Images alone are sufficient for character training
  - *From: WorldX*

- **Musubi vs Diffusion Pipe training time**
  - Musubi gives much better results in fraction of the time. Both high and low trained in about 30 minutes each
  - *From: screwfunk*

- **WAN 2.1 vs WAN 2.2 training**
  - WAN 2.2 is completely different from 2.1 - graphs and loss metrics that worked for 2.1 don't apply. 2.2 trains much faster
  - *From: screwfunk*

- **RTX 6000 Ada vs 5090**
  - 5090 is faster than the 6000 ada, even though 6000 ada has more cores
  - *From: WorldX*

- **SDPA vs xformers**
  - xformers is faster and more memory efficient than SDPA
  - *From: flo1331*

- **dpm++_sde vs euler scheduler**
  - dpm++_sde with shift 8 produces significantly less distorted results and fixes blur issues compared to euler
  - *From: crinklypaper*

- **Musubi vs other trainers**
  - Musubi considered best trainer by far, though diffusion-pipe is quite good with sooner updates but fewer options
  - *From: flo1331*

- **AI captioning vs manual captioning**
  - ChatGPT with WAN prompting guide better than JoyCaption for SFW images, though JoyCaption great for NSFW
  - *From: flo1331*

- **DPM++_SDE vs Euler sampler**
  - DPM++_SDE requires higher LoRA strength (1.0) while Euler works with lower strength
  - *From: crinklypaper*

- **High vs Low noise LoRA epochs**
  - High epoch 55 works with DPM++_SDE, epoch 1 works with Euler for different samplers
  - *From: crinklypaper*

- **Video vs image sequence training**
  - Videos are compressed and may not be as optimal as image sequences for quality
  - *From: Guey.KhalaMari*

- **Musubi vs AI-Toolkit vs DP for WAN 2.2**
  - Musubi works best for T2V training, produces cleanest results fastest on 3090. AI-Toolkit works well but re-quantizes models each launch causing delays
  - *From: screwfunk*

- **Training with vs without 'photo'/'video' in captions**
  - Better results without 'photo' or 'video' modifiers in captions - just describe the dataset content directly
  - *From: flo1331*

- **Wan 2.1 vs 2.2 LoRA compatibility**
  - 2.1 LoRAs used to work for both T2V and I2V, but 2.2 LoRAs require much lower strength for I2V workflows
  - *From: screwfunk*

- **Lightning vs LightX speed LoRAs on style**
  - Lightning makes everything bright and solid like poor animation, LightX gives flushed cinematic look but changes colors
  - *From: screwfunk*

- **5B vs 14B model quality and speed**
  - 14B has much better quality, but 5B with turbowan can generate 121 frames in 20 seconds plus 1-2 min VAE encode
  - *From: crinklypaper*

- **Diffusion-pipe vs AI toolkit for Wan 2.2**
  - Diffusion-pipe produces better quality results but trains slower and uses more VRAM. AI toolkit is faster and uses less VRAM but can produce plastic-looking results with anatomy issues
  - *From: mrassets*

- **High vs Low noise training requirements**
  - High noise trains faster (400-800 steps for characters) while low noise is slower (800-3000 steps) but handles fidelity/likeness
  - *From: flo1331, Gentleman bunny*

- **bf16 vs fp16 for Wan 2.2 training**
  - bf16 is better if hardware supports it, fp16 for older generation graphics cards. bf16 recommended for 2.2, fp16 was better for 2.1
  - *From: Persoon, Guey.KhalaMari*

- **Wan 2.1 vs 2.2 LoRA compatibility**
  - 2.1 T2V LoRAs work effortlessly on 2.1 I2V, but 2.2 T2V LoRAs don't work well on 2.2 I2V even with strength adjustments
  - *From: screwfunk*

- **Video vs image training datasets**
  - Video training converges faster, provides better likeness, eliminates movement issues. Recommend no more than 25% artificial content in datasets
  - *From: flo1331*

- **CAME vs Adam optimizer**
  - CAME takes less VRAM than Adam with no downside in quality
  - *From: flo1331*

- **Automagic vs Adam optimizer**
  - Wan 2.2 t2v lora with automagic looks much worse than 2.1 trained with adam. Testing adam on 2.2 to confirm if it's automagic's fault
  - *From: scf*

- **2.1 vs 2.2 LoRAs for I2V**
  - 2.1 LoRAs work better for 2.2 I2V than 2.2 LoRAs do
  - *From: scf*

- **Wan 2.2 vs 2.1 LoRA training difficulty**
  - 2.2 requires different approach - needs uniform timestep sampling and separate high/low training. 2.1 LoRAs work at expected epochs while 2.2 initially showed no effect.
  - *From: Thom293*

- **ReActor WebUI vs ComfyUI for face swapping**
  - ReActor WebUI works better than ComfyUI implementation
  - *From: Kenk*

- **AI-Toolkit vs Musubi-Tuner**
  - AI-Toolkit has better UI and 4-bit training with Accuracy Recovery Adapters, but Musubi-Tuner supports block swapping which is crucial for lower VRAM systems
  - *From: JohnDopamine*

- **Video vs Image training for character LoRAs**
  - Videos produce far better results than images for everything including character LoRAs, though images can produce okay results
  - *From: flo1331*

- **Wan 2.1 vs 2.2 LoRA compatibility**
  - Wan 2.1 character LoRAs work well with Wan 2.2 T2V but are weaker on I2V models
  - *From: Guey.KhalaMari*

- **Diffusion Pipe vs Musubi Tuner**
  - They're pretty similar, Musubi has more knobs/controls, Diffusion Pipe is more streamlined and user-friendly
  - *From: ArtOfficial*

- **AI Toolkit vs other trainers**
  - Good UI but no block swapping support
  - *From: xwsswww*

- **Wan 2.2 Low vs Wan 2.1**
  - Low model is essentially Wan 2.1 with finetune and more data, generates similar results
  - *From: Alisson Pereira*

- **AI Toolkit vs Musubi Tuner vs Diffusion Pipe**
  - AI toolkit is easier to use and gets new features weekly. Musubi tuner uses WSL which can be confusing. Diffusion Pipe works well for experienced users
  - *From: Ryzen*

- **Training with safetensors vs full repo**
  - Musubi-tuner works with just safetensors files, but AI toolkit requires cloning the entire repo
  - *From: Tachyon*

- **Local vs cloud training cost analysis**
  - For intermittent usage (450h/year), cloud rental at ~40c/h ($180/year) more cost effective than $2500 5090 with depreciation
  - *From: Muon*

- **Diffusion Pipe vs AI Toolkit training speed**
  - 2.2 training is insanely slow compared to 2.1
  - *From: Dream Making*

- **Sigmoid vs Shift timestep sampling**
  - Sigmoid focuses on character likeness, Shift focuses on video movement
  - *From: Ryzen*

- **High+Low vs Low-only training**
  - High+Low looks 'a lot' better than low-only, improves general shape, height and features
  - *From: flo1331*

- **JoyCaption vs Qwen for captioning**
  - JoyCaption works better for character LoRAs but has poor accuracy for style LoRAs like 'Danger Zone'
  - *From: el marzocco*

- **2.1 vs 2.2 character training**
  - Same dataset that worked flawlessly on 2.1 failed on 2.2 with same settings
  - *From: Dream Making*

- **Validation loss vs training loss**
  - Validation loss is a better signal than training loss, which will overfit forever
  - *From: spacepxl*

- **Training low-only vs low+high LoRAs for characters**
  - Training both yields better quality than low-only, conflicting reports on 2.2 improvement
  - *From: flo1331*

- **AI toolkit vs Musubi tuner**
  - AI toolkit more user-friendly but may have VRAM limitations, Musubi more flexible but command-line based
  - *From: Léon*

- **Real vs AI-generated training data**
  - Real preferred but AI-generated can work well, conflicting opinions on effectiveness
  - *From: Thom293*

- **AI Toolkit vs Diffusion Pipe VRAM efficiency**
  - Diffusion Pipe is slightly more VRAM efficient than AI Toolkit, but neither is doable on 8GB
  - *From: Kiwv*

- **5090 vs 3090 for Wan training**
  - 5090 is 2-3x faster than 3090 in inference and training, better energy efficiency, more VRAM
  - *From: Kiwv*

- **Batch size vs Gradient accumulation**
  - Mathematically the same but different memory usage patterns. Batch loads both into memory simultaneously, gradient loads sequentially
  - *From: Kiwv*

- **3090 vs 5090 for Wan training**
  - 3090 is too slow for Wan training, better for image training and inference. 5090 much faster with 90 minutes for 1.5k steps
  - *From: Kiwv*

- **Batch size 2 + GA 1 vs Batch size 1 + GA 2**
  - Batch size 2 with GA 1 is faster and uses less VRAM
  - *From: Ryzen*

- **Qwen vs Wan for character/style learning**
  - Qwen is near 1:1 perfect for picking up characters and style, really amazed how well it works
  - *From: crinklypaper*

- **AI toolkit vs Diffusion Pipe vs OneTrainer**
  - Diffusion Pipe and OneTrainer preferred, but OneTrainer lacks model support and Diffusion Pipe lacks Windows support. Toolkit has both but features are misimplemented
  - *From: Kiwv*

- **One Trainer vs AI Toolkit for small datasets**
  - One Trainer better - took 10 minutes on 8gb GPU, don't have to download whole model repo like AI toolkit requires
  - *From: xwsswww*

- **Gemini vs QWen for captioning**
  - Gemini 3 is miles ahead for captioning but not open source - consistency with QWen but Gemini is better
  - *From: crinklypaper*

- **H200 vs 5090 vs Pro 6000 for training**
  - 5090 has 22k CUDA cores, H200 has 16k, Pro 6000 has 24k - Pro 6000 is best single GPU option
  - *From: Kiwv*

- **Musubi-tuner vs AI-toolkit resource usage**
  - Musubi has tricks that are less demanding than standard dual training
  - *From: oskarkeo*

- **Gemini vs Qwen for captioning**
  - Gemini is better but Qwen is 100% free and can handle NSFW with obliterated models
  - *From: crinklypaper*

- **Wan vs Qwen for text generation**
  - Wan is not great with text in general, Qwen would handle text in images more easily
  - *From: spacepxl*

- **Wan2.1 vs Wan2.2 for character/style training**
  - Wan2.1 is easier/faster to train (single model), Wan2.2 is better quality but takes longer (high+low models)
  - *From: crinklypaper*

- **Musubi vs Diffusion Pipe training quality**
  - No significant difference in results, Musubi has more options for specific use cases
  - *From: crinklypaper*

- **Model vs LoRA for lightning acceleration**
  - Using lightning model for high + LoRA for low gives better motion than LoRA-only approach
  - *From: crinklypaper*

- **2.1 LoRAs vs 2.2 speed LoRAs with high model**
  - Using 2.1 loras with high makes it look more like 2.1, though 2.2 speed up loras also have trade-offs
  - *From: crinklypaper*

- **Wan 2.1 vs 2.2 for likeness**
  - If you want likeness use wan 2.1 and phantom, but 2.2 does a pretty good job already
  - *From: Thom293*

- **LTX 2 vs Wan quality**
  - Need >1080p with LTX to get close to quality of Wan at 720p, quality is not even close at equivalent settings
  - *From: spacepxl*

- **Cost comparison Wan 2.1 vs 2.2 training**
  - 2.1 cost $22.50 for 295 epochs vs 2.2 cost $29.92 for only 24 epochs with same dataset
  - *From: DevouredBeef*

- **NF4 vs unscaled fp8 quantization**
  - NF4 is significantly higher quality than unscaled fp8
  - *From: spacepxl*

- **AI Toolkit vs other training tools**
  - AI toolkit is generally slower and produces worse results for Wan
  - *From: vuuw*


## Tips & Best Practices

- **Use two-stage training: images first, then videos**
  - Context: Train with images for 15 epochs, then continue with videos for better motion and stability
  - *From: Cseti*

- **Use pretraining + finetuning approach for character LoRAs**
  - Context: Pretrain on 60 images until okayish, then finetune on 2 close-up and 2 medium shots, use 0.5 weight for both
  - *From: mamad8*

- **Add lots of regularization data for multi-character training**
  - Context: Use 500 reg images with 50 images per character, set repeat of 20 for character images
  - *From: mamad8*

- **Use detailed captions to prevent feature bleeding**
  - Context: Caption clothes, hair, position, location, background to prevent association with character
  - *From: mamad8*

- **Leave videos slightly longer than target bucket**
  - Context: Prevents frame count calculation issues in diffusion-pipe
  - *From: Cseti*

- **Test LoRAs with basic workflows first**
  - Context: Use wrapper or native ComfyUI without custom nodes to avoid key errors
  - *From: Cseti*

- **Use multi-resolution training for better results**
  - Context: For photo training use resolutions: 384, 512, 768, and 1024
  - *From: mamad8*

- **Don't train photos and videos together**
  - Context: Better to do photos first, then videos, then photos again
  - *From: mamad8*

- **Add 'close-up' or 'headshot' in captions when training on close-ups**
  - Context: Prevents model from generating close-ups when not requested
  - *From: mamad8*

- **Include regularization videos for movement**
  - Context: When LoRA produces static results, include reg videos with movement but no character faces
  - *From: mamad8*

- **Set alpha = rank and use learning rate 2e-5**
  - Context: For proper LoRA training, avoid musubi default alpha=1 which requires much higher LR
  - *From: mamad8*

- **Use masks for flow edit models**
  - Context: Nobody seems to use masks for flow edit, but you should. Maybe even soft masks like diffdiff
  - *From: spacepxl*

- **For preventing overfitting, use more data instead of clever tricks**
  - Context: Clever tricks will never prevent overfitting, it's purely a data size vs training time problem. In the limit, if you never go past 1 epoch it's not possible to overfit
  - *From: spacepxl*

- **Train low resolution first, then finetune at higher quality**
  - Context: Train at very low res like cakify (280x190), then do 1-2 epochs at higher quality on top
  - *From: Juampab12*

- **For character training, include character name in every caption**
  - Context: Use short captions including the name of the character each time, then finetune on 4-5 best headshots with 'close-up' or 'headshot' in caption
  - *From: mamad8*

- **Avoid using repeat values > 1 in dataset config**
  - Context: Model might see same image 5 times in a row by randomness. Better to use repeat < 1 for reg data instead
  - *From: mamad8*

- **Use detailed prompts with joycaption for better training results**
  - Context: When training character LoRAs
  - *From: chancelor*

- **Always check GitHub for latest fixes when encountering errors**
  - Context: When troubleshooting training issues
  - *From: Juampab12*

- **Set alpha to match rank**
  - Context: LoRA training configuration
  - *From: Ada*

- **Use validation loss to troubleshoot order of magnitude issues**
  - Context: Small datasets are touchy, need balance between undertraining and overtraining
  - *From: spacepxl*

- **Crop images outside trainer to avoid potential squishing**
  - Context: When preparing datasets for training
  - *From: Juampab12*

- **Use different starting frames for I2V training data augmentation**
  - Context: When training I2V LoRAs on timelapse-style content
  - *From: spacepxl*

- **Use lower LR for larger datasets**
  - Context: When choosing learning rates based on dataset size
  - *From: spacepxl*

- **Set video repeats higher than image repeats**
  - Context: When training with mixed image/video datasets
  - *From: Persoon*

- **Skip some frames for age progression**
  - Context: When creating timelapse training data
  - *From: spacepxl*

- **For beginners: use 16 rank, 5e-5 lr, 1 alpha**
  - Context: Simple LoRA training settings for newcomers
  - *From: Juampab12*

- **Use descriptive captions instead of triggers for I2V**
  - Context: Better results with captions like 'a full size video transforming into a grid of small videos' rather than trigger words
  - *From: mamad8*

- **Train at multiple frame lengths for better motion**
  - Context: Using varied frame buckets helps with motion learning
  - *From: Benjaminimal*

- **Use T2V LoRAs on I2V model for character training**
  - Context: You can train character likeness on T2V with images and use the LoRA with I2V model
  - *From: Kijai*

- **Train T2V for likeness, I2V for movements**
  - Context: Train actions/movements on I2V with low res videos and train likeness on T2V with high res images
  - *From: Ada*

- **When training on still images, mention it's a still image in captions**
  - Context: Prevents LoRA from baking in no movement
  - *From: Screeb*

- **Use lower ranks when training for movement only**
  - Context: Avoids capturing too many visual details when focus is on motion
  - *From: Alisson Pereira*

- **Caption the movement in training data**
  - Context: Allows users to request specific movements in prompts
  - *From: Alisson Pereira*

- **Generalize datasets as much as possible**
  - Context: Include different camera movements, colors, styles, clothes to avoid overfitting
  - *From: Alisson Pereira*

- **Install optimizations like triton, sage, tea cache for better performance**
  - Context: Will notice significant speed differences especially on high-end GPUs
  - *From: Alisson Pereira*

- **Use natural language captions instead of unique tokens**
  - Context: For T5/LLM conditioned models like Wan2
  - *From: Mint*

- **Remove style descriptions from captions when training style LoRAs**
  - Context: Let the trigger word absorb everything not described
  - *From: spacepxl*

- **Don't chase the lowest loss number**
  - Context: Test checkpoints and use the one with best output, not just smallest loss
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use validation split to properly measure training progress**
  - Context: Training loss alone is meaningless for determining over/underfitting
  - *From: spacepxl*

- **Mix small res videos for motion with high res images for detail**
  - Context: 20 videos + 10 images worked well for motion LoRA training
  - *From: Juampab12*

- **Caption manually for character training with few images**
  - Context: Only need about 20 images, can manually caption for better control
  - *From: Juampab12*

- **Use epochs instead of num_repeat unless you know exactly why**
  - Context: More predictable training behavior
  - *From: Mngbg*

- **Use descriptive prompts instead of trigger words**
  - Context: When training Wan LoRAs, T5 encoder prefers known concepts over trigger words
  - *From: Benjaminimal*

- **Filter Runpod servers by fast internet speed**
  - Context: When not using network storage, fast internet helps with quick model downloads
  - *From: Cseti*

- **Start with default config before making changes**
  - Context: For captioning scripts, try defaults first before modifying parameters
  - *From: ArtOfficial*

- **Increase learning rate when validation loss decreases linearly**
  - Context: Linear decrease means model is still learning fast and can handle higher LR for faster convergence
  - *From: spacepxl*

- **Use latent noise for training regularization**
  - Context: 0.1 latent noise factor helps with low quality input videos without losing much detail
  - *From: spacepxl*

- **Use consistent captioning patterns for all images in dataset**
  - Context: Most important factor for LoRA training success. Use same captioning structure and token order throughout dataset
  - *From: Kytra*

- **Caption everything EXCEPT the concept you're training**
  - Context: For character LoRAs, don't mention character aesthetic in captions so trigger word learns character design. For style LoRAs, don't mention the style
  - *From: Kytra*

- **Future-proof datasets by saving at high resolutions and frame counts**
  - Context: Save clips at multiple resolutions and excessive frame counts, let trainer crop as needed. Reuse datasets for future models like SD1.5>SDXL>Flux progression
  - *From: Persoon*

- **Don't use repeats for single concept datasets**
  - Context: Repeats are just epochs in disguise for single concepts. Use 0 repeats and adjust epochs instead. Repeats risk bad distribution with images repeating multiple times in row
  - *From: spacepxl*

- **Group similar scenes for custom prompting**
  - Context: For complex LoRAs, group similar videos/images and create custom prompts for each group rather than batch processing everything
  - *From: Amirsun(Papi)*

- **Use explicit camera motion captions, avoid describing subject actions**
  - Context: When training camera movement LoRAs, focus captions on camera dynamics rather than subject behavior
  - *From: Amirsun(Papi)*

- **Training novel concepts requires more steps and lower LR**
  - Context: More familiar concepts to the model need fewer steps (~3000), novel concepts need higher steps and careful tuning
  - *From: Amirsun(Papi)*

- **Use real names instead of rare tokens**
  - Context: With T5 models, rare tokens are unnecessary - real names work fine for trigger words
  - *From: spacepxl*

- **Delete global_step folders after training**
  - Context: These can take 1+GB each and aren't needed once you have your final LoRA
  - *From: JohnDopamine*

- **Test extensively with different settings before discarding LoRAs**
  - Context: Same LoRA can give vastly different results with inference optimization and block selection
  - *From: Juampab12*

- **Train at lower resolution for faster/cheaper results**
  - Context: 256x256, 49 frames or less recommended for local training on 3090/4090
  - *From: Amirsun(Papi)*

- **Use high resolution stills combined with low resolution videos**
  - Context: Having low res video to capture unique motions combined with higher res pics to capture subjects likeness/details works better than just high-res videos
  - *From: MilesCorban*

- **Caption everything except what you want learned**
  - Context: For motion LoRAs, caption the image content and avoid mentioning the specific motion or quality issues like blurriness
  - *From: Piblarg*

- **Diverse dataset more important than high resolution**
  - Context: Make dataset as varied as possible - if only street walking videos, it may only do that, but 10 different videos of different things should work
  - *From: Juampab12*

- **Watch sample outputs over loss charts**
  - Context: Best to look at generated video samples every epoch rather than going solely off tensorboard loss charts
  - *From: JohnDopamine*

- **Mix videos and images for training**
  - Context: Use 244p resolution videos with 1024p images (can be first frame of video in higher res) to teach both movement and quality
  - *From: Alisson Pereira*

- **Use specific training parameters to limit scope**
  - Context: You can limit training unintended dynamics by focusing on specific modules, resulting in smaller LoRAs with focused impact
  - *From: Amirsun(Papi)*

- **Test base model capability before training**
  - Context: You can test if a concept is unknown to the model by asking the model to generate what you want to train
  - *From: Alisson Pereira*

- **Caption everything you possibly can for video LoRA training**
  - Context: For better training results, provide detailed captions differentiating styles, motions, etc between videos
  - *From: Benjimon*

- **Try different seeds when testing LoRAs**
  - Context: WAN results can be highly seed-dependent, so change seeds if getting poor results with same prompt
  - *From: MilesCorban*

- **Put camera movement prompts at end of prompt**
  - Context: Model likes subject-background-action format, so try putting camera zoom part at end
  - *From: ingi // SYSTMS*

- **Use regularization datasets when training on images only**
  - Context: Consider providing 5-10 regularization videos per image when training character LoRAs on images
  - *From: BondoMan*

- **Mix images with videos for better quality**
  - Context: Take the first frame of each video for image dataset at higher resolution (1024) since videos train at low resolution (244)
  - *From: Alisson Pereira*

- **Delete cache folders when changing datasets**
  - Context: If changing anything in datasets before restarting training, delete cache folders so they regenerate
  - *From: JohnDopamine*

- **Use Florence 2 for captioning then remove triggers like 'asian, black hair'**
  - Context: For character LoRA captioning
  - *From: Piblarg*

- **Use shorter captions for better results**
  - Context: Super long prompts worked worse than shorter ones in HyV, likely same for WAN
  - *From: MilesCorban*

- **Keep all resolutions divisible by 32, at least 16**
  - Context: When setting training resolutions
  - *From: Benjimon*

- **Save every epoch early in training to find sweet spot**
  - Context: Hard to tell when video LoRAs are overtrained, good results can come early or take long time
  - *From: Piblarg*

- **Be very careful with dataset selection for small datasets**
  - Context: Smaller datasets mean each video has greater influence, bad items have more negative impact
  - *From: seruva19*

- **Use higher learning rate with smaller datasets**
  - Context: 2e-4 learning rate works fine with smaller datasets and trains faster
  - *From: Piblarg*

- **Use basic token/class captioning for character LoRAs**
  - Context: For character training, simple trigger word approach works better than detailed descriptions
  - *From: JohnDopamine*

- **Add high-quality still frames to video datasets**
  - Context: Take stills from videos, enhance with SD if needed, add different backgrounds - significantly improves LoRA quality
  - *From: Thom293*

- **Don't blur or crop faces in training data**
  - Context: AI is smart enough to replace faces later, blurring/cropping degrades output quality
  - *From: Thom293*

- **Clean your model directory before training**
  - Context: Remove any extra model files from directory as they can be included in checkpoint even if removed from config
  - *From: MatiaHeron*

- **Train low resolution for motion, higher for details**
  - Context: Low res is fine for motion capture as it doesn't train resolution into LoRA, but higher res helps with details
  - *From: Piblarg*

- **Use opposing LoRA technique for slider creation**
  - Context: When making slider-type LoRAs, train two opposing concepts then merge with negative weights to cancel unwanted behavior
  - *From: Piblarg*

- **Start with default settings and change only paths and resolution**
  - Context: When troubleshooting training issues, go back to default config and only modify essential settings
  - *From: Thom293*

- **Save every 1 epoch for style LoRAs**
  - Context: For style LoRAs, sweetspot seems to be between 12-18 epochs, so save every epoch to test
  - *From: Thom293*

- **Use token/class captions for character training**
  - Context: For single human likeness training, token/class style (like 'ohwx man') converges much quicker and works well
  - *From: JohnDopamine*

- **Add video training to prevent motion loss**
  - Context: Start with images, then generate videos and add them to training to prevent image-only LoRAs from losing movement
  - *From: Thom293*

- **Close all background applications when training**
  - Context: To avoid OOM errors, close literally every single background application
  - *From: Thom293*

- **Check cache folder to verify training data processing**
  - Context: Inside the image or video folder there should be a cache folder with processed files if training data was loaded correctly
  - *From: Thom293*

- **Use dim==alpha for simplicity when training**
  - Context: Alpha scales learning rate during training and inference, setting equal to dim avoids complications
  - *From: hablaba*

- **Start with 2 examples per movement/emotion for specialized training**
  - Context: For training specific movements or emotions, 2 examples of each type worked well for SDXL and should work for video
  - *From: Thom293*

- **Train iteratively: images first, then add videos, finish with video-only**
  - Context: Best LoRAs started with images, added videos in different sets, finished on videos for final 25% of epochs
  - *From: Thom293*

- **Don't over-caption - models already know basic objects**
  - Context: Models know what red bows, coffee cups, etc. are - only caption 'the thing' you're teaching unless background elements are important
  - *From: Thom293*

- **Use Cursor IDE with LLM assistance for technical setup**
  - Context: Cursor provides contextual awareness of project files and can generate .bat files for commands
  - *From: Neex*

- **For style training, use varied dataset with different lighting conditions**
  - Context: Avoid two images from same scene, use descriptive captions with trigger words
  - *From: Zlikwid*

- **Use diverse backgrounds for character LoRAs**
  - Context: For training character LoRAs, vary backgrounds (living room, outdoors, etc) or use HDRI in DAZ for diverse lighting/backgrounds
  - *From: boorayjenkins*

- **More repeats focus on characters/elements, fewer on style**
  - Context: Higher repeats (like 10) make model learn characters/elements in images, lower repeats (like 5) focus more on style
  - *From: ingi // SYSTMS*

- **Use Handbrake for video preprocessing**
  - Context: Resize videos to specific training resolution using Handbrake to maintain bitrate quality instead of letting training software do default resizing
  - *From: Alisson Pereira*

- **Mix images and videos in training**
  - Context: Can use images at 1024 resolution and videos at 256/512 depending on VRAM, effective for character training
  - *From: Alisson Pereira*

- **Don't describe what you want permanent, do describe what you want changeable in captions**
  - Context: Character training - if you want scar always there don't mention it, if you want to remove it later then mention it
  - *From: mdkb*

- **Keep dataset content consistent to avoid high loss peaks**
  - Context: Instead of using effect on several different content types, try same content type like effect only on people
  - *From: Alisson Pereira*

- **Use 3-4 captions with slightly different prompts and tag camera movement**
  - Context: When using Ovis2 for captioning
  - *From: notid*

- **Cancel and restart training after first steps start for 2x speed**
  - Context: Weird quirk with trussell version - 8 hours became 4 hours
  - *From: mdkb*

- **Test lora at different epochs like every 5 epochs**
  - Context: For style lora, epoch 15-25 is usually fine, use tensorboard to find best around 400-500 steps
  - *From: Thom293*

- **Don't describe what you want permanent, do describe what you want changeable**
  - Context: When captioning for WAN training to control what the LoRA learns vs what stays flexible
  - *From: mdkb*

- **Use masked training to focus on specific parts without training backgrounds**
  - Context: When you want to train specific features like tattoos without including unwanted background elements
  - *From: hablaba*

- **Add emotional expressions to face training datasets**
  - Context: To avoid getting stuck with neutral face expressions that require lower LoRA strength
  - *From: mdkb*

- **Include one image with other people in character datasets**
  - Context: So the LoRA knows what multiple people look like and doesn't make everyone look the same
  - *From: mdkb*

- **Add frame buckets around your target for safety**
  - Context: Generally put frames right around target (like 30,33,36) in case of editing errors
  - *From: Thom293*

- **Start with shift 7 or 3, then train on top with shift 1/sigmoid for details**
  - Context: Mixed approach might be best - start with composition then add details training
  - *From: hablaba*

- **Use non-real words as trigger tokens**
  - Context: Training LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Save multiple epochs during training to test different stages**
  - Context: Avoiding overtraining
  - *From: MilesCorban*

- **Can resume training and switch datasets**
  - Context: Some recommend constantly switching datasets to steer training direction
  - *From: Persoon*

- **Add simple motion videos to fix image training stiffness**
  - Context: Walking and head movement videos, doesn't need to match style exactly
  - *From: Thom293*

- **Train motion at 256p, style at 512p if focusing on specific aspects**
  - Context: Video training optimization
  - *From: Thom293*

- **Convert dataset videos to 16fps to match WAN training**
  - Context: Video preprocessing
  - *From: crinklypaper*

- **Never go below rank 32 for LORAs**
  - Context: Rank 16 LORAs give poor results
  - *From: Thom293*

- **Use natural language captions, not tagging**
  - Context: DiT models work best with natural language due to T5 encoder
  - *From: CJ*

- **Keep incrementing batch size until OOM, then decrease by one**
  - Context: To maximize VRAM utilization when underutilizing GPU memory
  - *From: MilesCorban*

- **Train character LORAs with only character name in captions**
  - Context: For character training, use just the name like 'Elon' in captions, then prompt with 'a video of Elon skateboarding'
  - *From: MilesCorban*

- **Use 1:4 ratio of images to videos for motion concepts**
  - Context: Images for fidelity/definition, videos at lower resolution for motion
  - *From: CJ*

- **Fix slow motion issue by merging models**
  - Context: Merge base wan with skyreels, merge base wan with moviegen, then merge those two results
  - *From: Thom293*

- **Use automagic optimizer without changing default settings**
  - Context: For most training scenarios, just copy the basic automagic config without modifications
  - *From: Alisson Pereira*

- **Monitor loss trends over time, not individual spikes**
  - Context: Training loss can have peaks and instability - focus on overall decreasing trend rather than individual values
  - *From: Alisson Pereira*

- **Never use LoRA strength above 1.0 in normal cases**
  - Context: Properly trained LoRAs should work effectively at strength 1.0 or below
  - *From: mamad8*

- **Use pre-compiled flash attention wheels for Blackwell GPUs**
  - Context: Compiling flash attention from source takes hours on RTX 5090, use official repo wheels instead
  - *From: mamad8*

- **Use regularization images for character LoRAs**
  - Context: Include 40% reg images of same class (man/woman) to prevent model from making your character every time you ask for multiple people
  - *From: mamad8*

- **Train character LoRAs on low noise model with full timestep range**
  - Context: Use min_t = 0, max_t = 1 for character training on low model only
  - *From: Alisson Pereira*

- **Use euler + beta scheduler with specific CFG settings**
  - Context: High pass CFG = 3 without lightx2v, low pass CFG = 1 with lightx2v for best inference results
  - *From: mamad8*

- **Test LoRA strength to determine training completeness**
  - Context: If you need strength above 1.0 (like 1.2, 1.5) to get good results, the LoRA is still undertrained
  - *From: Alisson Pereira*

- **Use block swap to enable multitasking during training**
  - Context: Allows playing games or other activities while training without affecting learning quality
  - *From: Kenk*

- **Use lr_bump = 5e-6 to speed up convergence**
  - Context: Can dramatically speed up training - one user saw convergence at 80 epochs instead of hundreds
  - *From: MilesCorban*

- **Train different datasets for high and low models**
  - Context: Use longer videos at lower res for high, shorter videos at higher res for low
  - *From: mamad8*

- **15-30 minute training runs can produce good character results**
  - Context: 30 minutes is sweet spot, 1 hour is great, 5 hours creates clone-like results
  - *From: Kenk*

- **20-40 images sufficient for character training**
  - Context: Good results achievable with just 20 images if properly captioned
  - *From: Kenk*

- **Use lower quality videos and higher quality images in training**
  - Context: Balances speed of training with quality
  - *From: Piblarg*

- **Train both high and low models for best results**
  - Context: For style LoRAs dealing with prompt issues, training both high+low works better than low only
  - *From: jikan*

- **Normalize videos to 16fps for bucketing**
  - Context: When training with diffusion-pipe, normalize videos to 16fps to fit the bucketing setup
  - *From: Kenk*

- **Include penis closeups and explicit descriptions for NSFW**
  - Context: To avoid genital deformations, train with closeup clips and caption genitals as 'appendix attached to crotch'
  - *From: Critorio*

- **Use 1.3 strength to determine if more training needed**
  - Context: If LoRA works well at 1.3 strength, indicates training could benefit from more epochs
  - *From: Alisson Pereira*

- **Test LoRA at early epochs before assuming more training is better**
  - Context: When loss plateaus or faces start merging, earlier epochs may perform better
  - *From: Alisson Pereira*

- **Use different training strategies for high vs low models**
  - Context: High model with longer videos at lower res, low model with shorter videos at higher res
  - *From: Kenk*

- **Place faces partially out of frame and caption it to avoid face bias**
  - Context: When training non-face focused LoRAs, put 'face out of frame' in captions and use in negative prompt to counter bias
  - *From: crinklypaper*

- **Mix multiple faces with same characteristics for face-dependent LoRAs**
  - Context: Prevents outputting same people from training data, creates unique blended face
  - *From: Kenk*

- **Use GIMP smudge tool to remove watermarks and unwanted elements**
  - Context: Clean up training data by removing ugly piercings, tattoos, and watermarks
  - *From: crinklypaper*

- **Train character LoRA only on LOW model for better motion preservation**
  - Context: Placing character LoRA only on LOW model produces better results than on both high and low
  - *From: screwfunk*

- **Set discrete_flow_shift values correctly**
  - Context: High flow on 7 and low on 3 for proper training results
  - *From: uff*

- **Use different resolution strategies for high vs low noise**
  - Context: 256 or 384 for high noise, 512 for low noise models
  - *From: CJ*

- **Save frequently for high noise training**
  - Context: High noise drops to very low loss quickly, save every 2 epochs instead of 5 for better testing
  - *From: screwfunk*

- **Character lora training parameters**
  - Context: 22 images, 3 repeats, 16 epochs worked well for character lora
  - *From: uff*

- **Use weight staggering for 2.2 models**
  - Context: Weight of 3 on high noise, and 1 on low noise
  - *From: Fill*

- **Test LoRA at early epochs before continuing training**
  - Context: Essential to avoid overfitting - test around epoch 10-15 for character LoRAs to find optimal stopping point
  - *From: Alisson Pereira, screwfunk*

- **Use 50/50 ratio of images and videos for Wan 2.2 training**
  - Context: More videos help motion significantly and dictate how things work motion-wise in the generated universe
  - *From: Fill*

- **Don't use block swap unless necessary**
  - Context: Only use high block swap settings when doing super high resolution runs
  - *From: CJ*

- **For character LoRAs, trigger words are mostly placebo**
  - Context: Well-trained LoRAs don't need trigger words to work effectively
  - *From: Kenk, Piblarg*

- **Start with smaller, focused datasets before trying diverse ones**
  - Context: When training concepts like 360 rotation, test with similar style content first, then apply to other types
  - *From: Alisson Pereira*

- **Use steps instead of epochs for comparing training progress**
  - Context: Different users have different steps per epoch based on dataset size and batch settings, making epoch numbers unreliable for comparison
  - *From: screwfunk*

- **Test LoRAs during training by using cloud training and local testing**
  - Context: Train in cloud pods while testing epochs on local machine to monitor progress
  - *From: screwfunk*

- **Train high and low models separately with same dataset**
  - Context: Use separate scripts for high and low noise models, both pointing to the same dataset folder
  - *From: screwfunk*

- **Use lowest possible epoch for low noise that achieves likeness**
  - Context: Low noise model degrades with overtraining, so stop as early as possible while maintaining character likeness
  - *From: el marzocco*

- **Include detailed descriptions for character control**
  - Context: Long descriptions allow better control over hairstyle, clothing changes, etc., contrary to concerns about losing likeness
  - *From: crinklypaper*

- **Reference trigger multiple times in Wan prompting structure**
  - Context: For character LoRAs, helps with attribution
  - *From: flo1331*

- **Train face-only LoRA first, then resume with additional dataset**
  - Context: Mentioned as potential workflow for character training
  - *From: Guey.KhalaMari*

- **Add 'muted colors' to negative prompt when using LightX2V**
  - Context: Balances the darker colors produced by LightX2V
  - *From: crinklypaper*

- **Use conservative settings for first successful run**
  - Context: Start with low learning rates and simple configs to ensure training completes
  - *From: artificial_fungi*

- **Use --preserve_distribution_shape for training**
  - Context: Recommended in documentation though difference not immediately apparent
  - *From: JalenBrunson*

- **Train character LoRAs with very detailed prompts**
  - Context: LoRA can properly train on character and not the style of uploaded videos
  - *From: Kiwv*

- **Start with lower learning rate and 1 repeat for character training**
  - Context: WAN trains very well but overtrains quickly with images, find right epoch first
  - *From: MilesCorban*

- **Use Google Vertex API for video captioning**
  - Context: Get $300 free credit for 90 days to use Gemini for captioning large datasets
  - *From: Kiwv*

- **Test LoRAs without lightning LoRAs for accurate results**
  - Context: Lightning/LightX LoRAs can distort training results evaluation
  - *From: flo1331*

- **Caption everything you want to be changeable**
  - Context: For character training, describe outfit, lighting, scene details even if you like them, otherwise they get bound to character trigger
  - *From: MilesCorban, GOD_IS_A_LIE*

- **Use only one resolution dimension**
  - Context: Instead of fixed resolution like [288,162], just use [512] or [256] and let AR buckets handle the rest
  - *From: CJ, Alisson Pereira*

- **For motion LoRAs, describe the action simply**
  - Context: Start caption with action like 'a woman swimming in a lake', no need to caption individual strokes or second-by-second movements
  - *From: MilesCorban*

- **Low resolution works fine for motion training**
  - Context: 256 resolution does great job for motion, can supplement with high-res first frames for quality if needed
  - *From: Alisson Pereira*

- **Don't use Lightning models for testing during training**
  - Context: Lightning changes the style and isn't valid for testing - train on base model and test on base model
  - *From: crinklypaper*

- **Focus training effort on Low noise model, not High**
  - Context: High converges super fast in ~30 minutes, Low is where detail and quality comes from
  - *From: screwfunk*

- **Test as you train rather than relying on loss graphs**
  - Context: WAN 2.2 loss graphs don't reliably indicate training quality, need to generate samples regularly
  - *From: screwfunk*

- **Use detailed captions describing everything except the concept you want to train**
  - Context: For motion/style training, describe person, outfit, background, lighting in detail
  - *From: flo1331*

- **Don't chop video clips below 17 frames**
  - Context: Results have been disappointing with shorter clips
  - *From: flo1331*

- **Use very low strength values for high noise LoRAs**
  - Context: High noise LoRAs are extremely powerful - 0.01-0.001 strength can be effective
  - *From: crinklypaper*

- **Train high and low noise separately when learning**
  - Context: Easier to understand each component before attempting dual training
  - *From: Ryzen*

- **Focus on visual testing over metrics**
  - Context: For Wan 2.2, real-world testing is more valuable than loss charts or step counts
  - *From: screwfunk*

- **Use 640x360 resolution for good results**
  - Context: High resolution not necessary - can increase frames to 33 instead
  - *From: flo1331*

- **Test every 5 epochs to see biggest jumps**
  - Context: When training, save every epoch but test every 5 to see progression
  - *From: screwfunk*

- **Push training until it looks bad, then back off**
  - Context: Keep pushing past when things look good until it starts looking like crap, then you know your golden zone
  - *From: screwfunk*

- **Focus more attention on LOW lora training**
  - Context: High trains very fast, so spend more effort optimizing the low lora
  - *From: screwfunk*

- **Caption hair color for flexibility**
  - Context: Captioning hair allows you to change it, and if you want original style just don't mention it in prompt
  - *From: flo1331*

- **Set alpha equal to dim value when lowering LR**
  - Context: When using lower learning rates like 2e-5, need to set alpha to dim value or it won't train properly
  - *From: flo1331*

- **Use rank 16-20 for characters, maximum 32**
  - Context: WAN is different from SDXL and works fine with lower ranks. Higher ranks like 64-128 take much longer to train
  - *From: flo1331*

- **Don't use single rare tokens to carry style weight**
  - Context: Model needs to understand token meaning to make proper connections. Better to describe style or not caption it at all
  - *From: mamad8*

- **Train fewer epochs on high model than low model**
  - Context: Low noise model handles heavy character work, high model mainly does basic features and motion
  - *From: mamad8*

- **Use LLM to guide complex installations**
  - Context: When dealing with cutting-edge technology setup issues, use GPT-5 or Gemini with max context
  - *From: mamad8*

- **Train different strengths for different samplers**
  - Context: Same LoRA may need different strength values depending on sampler used
  - *From: crinklypaper*

- **Test LoRAs with different epochs systematically**
  - Context: Epoch performance varies significantly between samplers
  - *From: crinklypaper*

- **Build workflows from scratch rather than using complex multi-purpose ones**
  - Context: Easier to understand, maintain and troubleshoot when things change
  - *From: CJ*

- **Use single-purpose workflows**
  - Context: KISS principle - does one thing really well
  - *From: screwfunk*

- **Caption everything except what you want LoRA biased on**
  - Context: For character LoRAs, omit traits you want automatic (like hair color) but include changeable elements (clothing)
  - *From: crinklypaper*

- **Use different angles and environments for character training**
  - Context: Provides better dataset diversity for character LoRAs
  - *From: crinklypaper*

- **Low LoRA shouldn't overwhelm image input**
  - Context: When training motion I2V with different source images than training data
  - *From: CJ*

- **Use earlier epochs for high noise, later epochs for low noise when combining models**
  - Context: When using dual LoRAs, apply epoch ~100 to low noise and epoch ~200 to high noise for character training
  - *From: JalenBrunson*

- **Remove backgrounds from character training images**
  - Context: Reduces distractions and helps focus learning on the person
  - *From: Gill Bastar*

- **Don't caption images as 'image' or 'photograph' as it kills motion**
  - Context: For video training, avoid static descriptors that might interfere with motion learning
  - *From: flo1331*

- **Training images above 512px shows minimal benefit for image-only datasets**
  - Context: Higher resolutions mainly help with very fine details like moles, but 512px is generally sufficient
  - *From: screwfunk*

- **High noise model sets foundation - composition, motion, base face. Low noise fills in details**
  - Context: Think of high as building foundation, low as adding details. Can train low-only but high helps establish better base
  - *From: screwfunk*

- **Mix new high LoRA with old low LoRA for interesting effects**
  - Context: When experimenting with training techniques
  - *From: MilesCorban*

- **Over-train the high LoRA as much as possible, then train the low**
  - Context: For style LoRAs - you can see if style is captured from high's blurry output
  - *From: crinklypaper*

- **Use lower rank for Wan 2.2 training**
  - Context: Rank 16 or 20 max instead of 32 to help with movement impact
  - *From: flo1331*

- **Start with default settings before making changes**
  - Context: When getting training working for the first time
  - *From: crinklypaper*

- **Use different resolutions for videos vs images**
  - Context: Videos for motion don't need high resolution, images can be trained at higher resolutions
  - *From: crinklypaper*

- **Keep video frames under 81 and create bucket for that**
  - Context: When dealing with longer videos to avoid memory issues
  - *From: crinklypaper*

- **High noise model overtrains easily**
  - Context: If baseline foundation changes too much you lose likeness, especially for character training
  - *From: crinklypaper, flo1331*

- **For style training, high model needs much more training**
  - Context: Low model needs something to work off from the high model, opposite of character training
  - *From: crinklypaper*

- **Caption videos like prose, not word salad**
  - Context: When training video LoRAs, use descriptive captions rather than keyword lists
  - *From: crinklypaper*

- **Preprocess videos to 16fps before training**
  - Context: To avoid timing issues during training
  - *From: mamad8*

- **Use specific character naming in captions**
  - Context: For multi-character LoRAs, caption like 'A woman named TRIGGER1 is sitting on a couch talking to a woman named TRIGGER2'
  - *From: screwfunk*

- **Optimal video dataset composition**
  - Context: For character training: 2-3 full body (1 front, 1 back), 10 medium shots, 7 close ups. Include varied angles (low, high, side profile)
  - *From: flo1331*

- **Don't trust loss numbers with Wan 2.2**
  - Context: Unlike 2.1 where loss indicated quality, 2.2 loss is not a good metric for determining LoRA quality
  - *From: screwfunk*

- **Use GAS=4 for faster convergence**
  - Context: Gradient accumulation steps of 4 makes optimizer adjust after batches instead of individual images/videos
  - *From: flo1331*

- **Use 'screen' command when training on RunPod**
  - Context: Prevents losing training progress if pod times out in web terminal
  - *From: shotgun messiah*

- **Don't describe what you want the LoRA to learn**
  - Context: For character training - don't describe hair color, face, clothes, body in detail as it hinders training. Do describe background and changeable elements
  - *From: mdkb*

- **Include group shots in character dataset**
  - Context: Helps LoRA understand that other people exist and reduces character bleeding
  - *From: mdkb*

- **Add emotional expressions to character datasets**
  - Context: All blank-faced training images require weakening LoRA strength to get emotions during generation
  - *From: mdkb*

- **Test LoRA outputs in increments during training**
  - Context: Test every 5 epochs for high noise, every 10 for low noise (5/10, 10/20, 15/30 pattern) to find optimal stopping point
  - *From: PineAmbassador*

- **Use longer videos (81 frames) over higher resolution for motion training**
  - Context: When choosing between higher res shorter videos vs lower res longer videos for motion learning
  - *From: ingi // SYSTMS*

- **Extract screenshots from original videos as high-res training images**
  - Context: For training datasets - use original 1080p video screenshots as high-res images, then low-res versions of same videos
  - *From: Gentleman bunny*

- **Avoid 'photograph' in prompts for motion retention**
  - Context: Anything mentioning 'photograph' kills motion in generated videos
  - *From: Gentleman bunny*

- **T2V LoRAs work better than I2V LoRAs**
  - Context: T2V LoRAs are always the best choice and also work in I2V mode
  - *From: ZeusZeus (RTX 4090)*

- **Use Low model only by bypassing High model LoRA loader**
  - Context: For some workflows, can achieve good results using just the low model without high model complications
  - *From: el marzocco*

- **Train character LoRAs only on Wan 2.1 T2V 14B model for use in 2.2**
  - Context: When training character LoRAs that will be used in Wan 2.2
  - *From: Tachyon*

- **Use gradient accumulation steps (GAS) for better results**
  - Context: GAS of 4 leads to better results even though it's slower, as it only adjusts weights after multiple steps
  - *From: flo1331*

- **Aim for LoRA to be perfect at strength 1.0**
  - Context: LoRAs should work optimally at strength 1.0, typically achieved around 2400 steps or 800 steps with GAS 4
  - *From: flo1331*

- **Use unique, non-human readable trigger words**
  - Context: To avoid trigger words appearing as text in outputs, use complex triggers like '_1aDi3_!!_oohLaLa_'
  - *From: Guey.KhalaMari*

- **Test LoRA progress early and resume if needed**
  - Context: For image training, test after 200 steps to check progress and use --resume to continue from savestates
  - *From: flo1331*

- **Caption videos using single frame or temporal AI**
  - Context: For video training, either caption a single frame or use CogVLM2/QwenVL with temporal understanding
  - *From: shotgun messiah*

- **Use trigger descriptions instead of trigger words**
  - Context: Describe character exactly as you want in prompt, then use same description when prompting
  - *From: ArtOfficial*

- **Caption everything except the style for style LoRAs**
  - Context: When training animation style, describe everything but the style so it gets baked into the LoRA
  - *From: crinklypaper*

- **Can train images first, then reload checkpoint and add videos later**
  - Context: Iterative approach for style training
  - *From: crinklypaper*

- **Videos can be very low resolution as their main job is teaching motion**
  - Context: Use 256x resolution for videos in training
  - *From: crinklypaper*

- **Fill up VRAM as much as possible without blockswap**
  - Context: Increase resolution, more video frames, or GAS to maximize VRAM usage
  - *From: crinklypaper*

- **Caption everything except the style for style LoRAs**
  - Context: Whatever you don't caption will become baked into the lora and hard to prompt out. For style loras, caption characters, clothes, objects but not the style itself
  - *From: crinklypaper*

- **Better captions more important than more images**
  - Context: Balance is good - more variation leads to better output. 80 images can work for style lora but 200-500 recommended for animated style
  - *From: crinklypaper*

- **Natural language captions work best for Wan**
  - Context: Use natural language descriptions rather than tagging, but also include trigger words
  - *From: crinklypaper*

- **Train style and character LoRAs separately**
  - Context: Character loras separate from style loras are easier to manage and can be loaded alongside each other
  - *From: crinklypaper*

- **Include variety in style training datasets**
  - Context: Caption images of garbage, fruit, vehicles, mechas etc with no people. If it's not in training data, higher chance the high model won't trigger the style
  - *From: crinklypaper*

- **Pick epoch with lowest loss between 15-20**
  - Context: For Wan 2.2 training, train to 22 epochs and pick the epoch with lowest loss between 15 and 20
  - *From: el marzocco*

- **Use different timestep sampling for different goals**
  - Context: Use sigmoid for character likeness, shift for motion capture
  - *From: Ryzen*

- **Combine high resolution images with low resolution videos**
  - Context: For character training, use high quality images with low res videos to enhance similarity since 256px video resolution is hard for facial structure accuracy
  - *From: 🦙rishappi*

- **Check training at loss valleys**
  - Context: Test LoRAs at points where loss drops in the graph, especially bigger overall drops in the smoothed average
  - *From: crinklypaper*

- **Caption camera movements in videos**
  - Context: Include camera work like 'dolly in, medium shot, arc shot' and avoid directional specifics like left/right
  - *From: crinklypaper*

- **Use both high and low models for character LoRAs**
  - Context: For best quality character training
  - *From: flo1331*

- **Test LoRAs at low strength (0.4) and increase if needed**
  - Context: When LoRA shows no movement, may be burnt
  - *From: Thom293*

- **For real people use 'obese, flabby and overweight' together instead of 'fat'**
  - Context: When prompting for weight changes
  - *From: Thom293*

- **Keep datasets small and focused for style LoRAs**
  - Context: Less is more approach prevents messy results
  - *From: el marzocco*

- **Caption the background if you want to change it**
  - Context: Don't caption what you want embedded in the LoRA
  - *From: flo1331*

- **Remove warmup steps when resuming training**
  - Context: Also change seed when resuming from saved state
  - *From: flo1331*

- **Test earlier epochs as they might be better than later ones**
  - Context: Overtraining can degrade quality
  - *From: flo1331*

- **Use ambiguous trigger words worked into prompts naturally**
  - Context: For motion LoRAs, integrate trigger word into sentence rather than standalone
  - *From: Kiwv*

- **Never train on AI-generated video for best results**
  - Context: When creating motion LoRAs, use real video sources
  - *From: Kiwv*

- **Test LoRAs with bare minimum - just base model + your LoRA**
  - Context: Avoid using multiple LoRAs when testing to isolate performance
  - *From: Guey.KhalaMari*

- **Turn off caption dropout for Wan training**
  - Context: Set caption dropout to 0 because Wan prompts are sentence-based unlike SDXL
  - *From: Kiwv*

- **Use tensorboard to monitor training and pick best epochs**
  - Context: Don't just use final epoch, monitor loss curves and test dips
  - *From: Guey.KhalaMari*

- **Don't train images for I2V, only use videos**
  - Context: Images on I2V with 1 frame just waste compute as model outputs the input image
  - *From: Kiwv*

- **Use sample prompts every 100 steps during training**
  - Context: To make sure training is going in the direction you want
  - *From: Kiwv*

- **Make captions slightly different for each video even if similar content**
  - Context: If training multiple similar videos, differentiate with hair color, clothing, etc.
  - *From: Kiwv*

- **Caption everything the model already knows, then add new subject**
  - Context: Describe woman, red hair, position, etc, but let LoRA learn the new hairstyle
  - *From: Kiwv*

- **For character consistency, use identical character descriptions**
  - Context: When training character LoRAs, physical description should be identical across all images
  - *From: metaphysician*

- **Use effective batch size of 2 or more to prevent overfitting to individual videos**
  - Context: Helps model learn concepts rather than memorizing specific videos
  - *From: Kiwv*

- **For 3090, use batch size 1 with gradient accumulation 2**
  - Context: VRAM limitations on 3090
  - *From: Kiwv*

- **Training is about finding the highest learning rate without model explosion**
  - Context: Optimizing training efficiency
  - *From: Kiwv*

- **For character LoRAs, describe what character is doing/wearing, not appearance**
  - Context: Example: 'Joe is wearing a red hat while drinking water' vs 'A white man with blue eyes wearing red hat drinks water, joe'
  - *From: Kiwv*

- **Train separate LoRAs then merge for multi-concept training**
  - Context: Alternative to problematic multi-dataset training
  - *From: Kiwv*

- **Use detailed captions for T2V LoRA training**
  - Context: Need camera angle, style, character position, emotions, actions - small captions only work for I2V
  - *From: Kiwv*

- **Train LoRAs without trigger words for convenience**
  - Context: Requires good captioning but avoids having to remember trigger words in prompts
  - *From: Kiwv*

- **Use 50+ word captions for T2V training**
  - Context: Detailed descriptions help model learn properly instead of memorizing video-caption pairs
  - *From: Kiwv*

- **Multi-step LoRA training for realistic characters**
  - Context: 1. Train image LoRA 2. Make videos with Phantom 3. Train combined image+video LoRA 4. Repeat for best quality
  - *From: Thom293*

- **For character LoRAs, 15-30 images at different angles sufficient**
  - Context: 70+ images is more than enough, can even work with 8 images using multi-step process
  - *From: Thom293*

- **Caption checklist: watermark location, video style, character appearance/clothing, actions, spatial relationships, emotions, background**
  - Context: For improving captions
  - *From: Kiwv*

- **Use Joycaption for batch captioning, do 4-5 passes, pick most correct, then manually edit every caption**
  - Context: Most bang-for-buck effort in training
  - *From: shotgun messiah*

- **Go super detailed into everything that isn't the subject you're training**
  - Context: Car LoRA training with consistent background
  - *From: Kiwv*

- **Make up unique mashup word or name instead of descriptive terms like 'lizardman is a man'**
  - Context: Avoiding trigger word confusion
  - *From: Thom293*

- **Describe literally as if describing the dataset not explaining it**
  - Context: Character LoRA captioning
  - *From: crinklypaper*

- **Use trigger word and describe camera angle in prompt for multi-angle LoRAs**
  - Context: Training motion from multiple angles
  - *From: Kiwv*

- **Videos absolutely help, especially for high noise model if you want to influence character movement**
  - Context: Adding videos to T2V character training
  - *From: ingi // SYSTMS*

- **Avoid training on clips with cuts unless specifically training for cuts**
  - Context: Video preparation
  - *From: ingi // SYSTMS*

- **Use POV to fix character bleeding in specific LoRAs**
  - Context: When training very specific concepts like fetal movement
  - *From: Ryzen*

- **Start training parameters small and scale up**
  - Context: When testing AI training concepts
  - *From: artificial_fungi*

- **For genitalia LoRAs, crop out faces and describe 'upper face out of frame' in captions**
  - Context: Training adult content LoRAs - prevents face bias but may cause out-of-frame bias
  - *From: crinklypaper*

- **Use diverse datasets where same objects/people don't appear frequently**
  - Context: When training style LoRAs to prevent unwanted objects appearing
  - *From: Kiwv*

- **Use speedrun/baseline settings first**
  - Context: Start with lowest conservative settings to ensure functionality before optimizing
  - *From: artificial_fungi*

- **Use unique character names in training**
  - Context: Instead of 'a man', use names like 'B0b' or 'D4n' to avoid confusion with all men
  - *From: Thom293*

- **Mask backgrounds when training products**
  - Context: For exact product replication, especially with text/labels, mask everything except the subject
  - *From: spacepxl*

- **Use 'clutter in background' caption**
  - Context: For hard-to-describe backgrounds, then negative prompt 'clutter' during generation
  - *From: Thom293*

- **Convert training data to 16fps**
  - Context: Match Wan's native 16fps, use ~55 frames max (2 seconds) for training clips
  - *From: crinklypaper*

- **Use JSON instead of pipe separators for cleaner workflows**
  - Context: For multi-prompt context window generations
  - *From: Scruffy*

- **Train 2-second clips to translate fine to 5-second generations**
  - Context: Wan base model understands motion well, short clips teach motion style
  - *From: crinklypaper*

- **Weight videos much less than images in dataset**
  - Context: Example: 700 images vs 100 videos for balanced training
  - *From: crinklypaper*

- **Look for specific style indicators during training**
  - Context: Check for style elements like eye whites, chin shapes, colors to confirm style pickup
  - *From: crinklypaper*

- **Use generic person prompts to test true style pickup**
  - Context: Style LoRAs should work on non-character prompts, not just specific characters
  - *From: crinklypaper*

- **Train high model first, then alternate between high and low**
  - Context: High lays foundation, low is dependent on high, so troubleshoot high first
  - *From: crinklypaper*

- **Use same settings, just change timestep and model from high to low**
  - Context: When switching between high and low models in 2.2
  - *From: crinklypaper*

- **Test low first as standalone, then high, then both together**
  - Context: For testing high/low epoch combos for wan 2.2
  - *From: flo1331*

- **Fix seed for one sampler to account for seed variance**
  - Context: When testing epoch combinations
  - *From: flo1331*

- **Drop lightx loras at least once to ensure bad movement isn't from speed lora**
  - Context: When testing high model
  - *From: flo1331*

- **Always start simple, make sure you get a working lora, then tweak and expand**
  - Context: General lora training approach
  - *From: Thom293*

- **Use combo of sentences and keywords for different concepts**
  - Context: Captioning strategy for multi-concept loras
  - *From: Thom293*

- **Create blend images with multiple concepts to tie them together**
  - Context: Training multi-concept loras
  - *From: Thom293*

- **Caption everything in dataset as if you're prompting it**
  - Context: General captioning methodology
  - *From: crinklypaper*

- **Keep fp32 norms and use scaling when using fp8 quantization**
  - Context: For training or inference - naive unscaled fp8 is trash
  - *From: spacepxl*

- **When quantizing, only cast big matmul weights and keep everything else BF16**
  - Context: For VRAM-limited training scenarios
  - *From: Persoon*

- **Use network dropout for better skin texture in LoRAs**
  - Context: When getting airbrushy results
  - *From: vuuw*

- **Look for configs that worked for other people and check Civitai articles**
  - Context: When starting training since there's no gold standard
  - *From: BrainNXDomain*


## News & Updates

- **Musubi-tuner WAN support in development**
  - Kohya's musubi-tuner has WAN 2.1 inference branch available
  - *From: 片ヨ亡亡丹片*

- **DiffSynth-Studio PR for I2V training**
  - Pull request available for training I2V LoRAs with some modifications needed
  - *From: mamad8*

- **Finetrainers added WAN 1.3B support**
  - Support added but has format compatibility issues requiring conversion
  - *From: DiXiao*

- **Ostris AI-Toolkit now supports Wan training**
  - Support for both 1.3B and 14B models, works on 24GB VRAM
  - *From: happy.j*

- **Musubi-tuner added Wan 2.1 LoRA training support**
  - wan_train_network.py now available in main branch
  - *From: mamad8*

- **SVDQuant/Nunchaku offers 3x speedup on RTX 4090/5090**
  - New quantization method for 4-bit diffusion models with fused kernels
  - *From: Ada*

- **Diffusion-pipe added block-swapping code via Kohya's musubi repo**
  - Added yesterday to help with memory requirements
  - *From: JohnDopamine*

- **New interface being developed for diffusion-pipe**
  - Using Blazor instead of Gradio, adding caption tools and other features. Expected completion within a day
  - *From: Alisson Pereira*

- **First WAN I2V training completed and shared on Civitai**
  - Model 1264662 on Civitai, works with 480p model
  - *From: Alisson Pereira*

- **Reduced memory use in Wan training**
  - tdrussell added changes to remove forced casts to float32, enabling 512x512x81 video training on single 4090 with fp8 transformer, AdamW8bitKahan optimizer, and blocks_to_swap=32
  - *From: chancelor*

- **New LoRA shared**
  - Steamboat Willie style LoRA for 1.3B model released
  - *From: Benjaminimal*

- **Comprehensive trainer feature matrix created**
  - Detailed comparison matrix of different Wan training options including supported features, learning curve difficulty, and multi-GPU performance
  - *From: Benjaminimal*

- **Kohya merged fp8 optimization PR**
  - New flag for fp8 optimization added to musubi-tuner yesterday, fp16 source files also supported
  - *From: JohnDopamine*

- **DiffSynth Studio I2V training now in main branch**
  - No longer need special branch for I2V training
  - *From: Benjaminimal*

- **ComfyUI working on native training support**
  - Goal is to provide training for any supported model
  - *From: TK_999*

- **AI-toolkit added Wan support**
  - Ostris added Wan support to ai-toolkit
  - *From: JohnDopamine*

- **Diffusion-pipe updated example configs**
  - Changed default repeats from 10 to 1 in recent commit
  - *From: JohnDopamine*

- **New training interface being developed**
  - Alisson working on GUI redesign for diffusion-pipe with multiple dataset configurations
  - *From: Alisson Pereira*

- **Fal endpoint for Wan LoRA training coming soon**
  - Internal testing in progress, public release expected soon
  - *From: jfischoff*

- **Replicate has Wan LoRA trainer in testing**
  - Available at replicate.com/zsxkib/wan-lora-trainer/train but still in testing phase
  - *From: pom*

- **Krea AI now offers Wan LoRA training**
  - Fast training service but LoRAs cannot be downloaded, must use within Krea platform
  - *From: Nathan Shipley*

- **ai-toolkit added video training capability**
  - Tool now supports video LoRA training in addition to existing features
  - *From: Nathan Shipley*

- **Fal trainer passing review process**
  - Benjaminimal's trainer for fal passed functional review and awaiting front-end approval, allows LoRA download
  - *From: Benjaminimal*

- **VideoModelStudio now supports Wan 2.1**
  - Open source trainer now includes Wan 1.3B support with automated dataset creation
  - *From: LarpsAI*

- **New diffusion-pipe UI released**
  - Updated interface with model selection and improved functionality, new docker image and Runpod template available
  - *From: Alisson Pereira*

- **fal.ai added Wan LoRA training service**
  - Takes videos only, allows LoRA download. Update coming to auto-caption with qwen2.5 7b and deploy on 8xH100
  - *From: Benjaminimal*

- **ComfyUI added support for Lotus model for depth and normals**
  - New depth and normal estimation model available in ComfyUI
  - *From: TK_999*

- **Qwen2.5-VL video captioning tool updated to v2**
  - Added image captioning and fixed bugs, though still feels slow with bigger datasets
  - *From: Cseti*

- **Kohya added Fun control model training support**
  - Available in wan21-fun-control branch of musubi-tuner for 14B Fun control model
  - *From: JohnDopamine*

- **Video support added to ai-toolkit**
  - Recent commit added video dataset handling in UI, though implementation status unclear
  - *From: mamad8*

- **Fal.ai WAN trainer now available**
  - Charges around $5-7 for I2V 14B training, 1800 steps with 34 videos took 1.5 hours
  - *From: DevouredBeef*

- **VACE has only been out 24 hours**
  - Community discussing that VACE was very recently released
  - *From: CJ*

- **Qwen2.5-VL-Video-Captioning script updated**
  - Updated captioning scripts now support config toml files so you don't have to change python scripts. Also supports image captioning. Commented toml files in detail.
  - *From: Cseti*

- **VidTrainPrep tool released**
  - Python GUI tool for video dataset preparation featuring multi-range clipping & cropping, interactive range creation, AutoCaption with Gemini AI. Enhanced from HunyClip by Tr1dae.
  - *From: lovis.io*

- **Animated logo LoRA first version released**
  - First version of animated logo LoRA released on Civitai - result wasn't perfect but ready to start
  - *From: Alisson Pereira*

- **FramePack released by Fooocus author**
  - New tool for generating longer videos with same VRAM, uses 13B model with 6GB minimum requirement
  - *From: Ada*

- **FAL now supports WAN LoRA training for 14B model**
  - Can use Higgsfield dataset examples with prompts as captions
  - *From: NebSH*

- **SkyReels V2 training support added to diffusion-pipe**
  - Support implemented by tdrussel 2 days ago
  - *From: JohnDopamine*

- **SkyCaptioner V1 released for video captioning**
  - Qwen2.5-VL finetune by Skyreels team for video prompting
  - *From: TK_999*

- **NVIDIA Describe Anything models released**
  - New captioning models from NVIDIA
  - *From: mamad8*

- **MoviiGen trainer released**
  - ZulutionAI released MoviiGen trainer on GitHub, Kijai has merged safetensors files on HuggingFace
  - *From: JohnDopamine*

- **Anime-oriented Wan merge model released**
  - Created a t2v and i2v merge model that is more anime-oriented than base wan, includes tweaked versions
  - *From: 852話 (hakoniwa)*

- **RTX 6000 now available on RunPod**
  - RTX 6000 just arrived on runpod
  - *From: phant*

- **ComfyUI-JoyCaption V1.1.0 released**
  - Updated version that auto-captions and exports images with text files
  - *From: hicho*

- **Musubi Tuner LoRAs now work directly in ComfyUI**
  - No longer need conversion, can use LoRAs trained in Musubi Tuner directly in ComfyUI workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Masked training not currently available in Musubi Tuner**
  - Feature is not implemented in current version
  - *From: hablaba*

- **ContentV-8B model released**
  - ByteDance released 8B model based on Stable Diffusion 3.5 Large and Wan-VAE, achieves 85.14 on VBench, trained in 4 weeks with 256×64GB NPUs
  - *From: hicho*

- **ShotVL-7B VLM released for movie shots**
  - Fine tuned on Qwen, can understand various movie shot aspects, works with DeZoomer nodes
  - *From: yi*

- **DeZoomer nodes updated with SkyCaptioner and ShotVL-7B support**
  - New version available through ComfyUI manager or GitHub, includes video captioning options
  - *From: DeZoomer*

- **Wan I2V model training now available in ai-toolkit**
  - T2V was available and now I2V training is also supported
  - *From: Alisson Pereira*

- **Wan 2.2 training support added to Diffusion Pipe**
  - tdrussell implemented support for both high and low noise model training
  - *From: JohnDopamine*

- **Wan 2.2 will be 30fps instead of 16fps**
  - Time to redo all datasets for the new framerate
  - *From: Persoon*

- **Ostris working on 5B implementation, tdrussell on 14B**
  - AI-toolkit getting 5B support, diffusion-pipe getting 14B support
  - *From: seruva19*

- **Musubi Tuner has Wan2.2 development branch**
  - Kohya committed to feature-wan-2-2 branch 10 hours ago, functionality uncertain
  - *From: JohnDopamine*

- **LightX2V for Wan 2.2 not yet available**
  - Current LightX2V was made for 2.1 and requires high strength (like 3.0) to work properly on 2.2, people waiting for 2.2-specific version
  - *From: mamad8*

- **Diffusion-pipe updated with Wan 2.2 support**
  - Users can now update diffusion-pipe to train on Wan 2.2 models
  - *From: Kenk*

- **Comfy acknowledged 24fps was a mistake in default workflow**
  - The 24fps setting in ComfyUI default workflow was incorrect
  - *From: MilesCorban*

- **Anime aspect strengthened in Wan 2.2**
  - Situation vastly better than community build of Wan 2.1
  - *From: au*

- **News from Ostris mentioned**
  - No specific details provided in visible messages
  - *From: orabazes*

- **New LightX2V LoRAs released for WAN 2.2**
  - Use at weight 0.125 according to Kijai, but they reduce effectiveness of custom LoRAs
  - *From: _Djent_*

- **Musubi Trainer now supports proper WAN 2.2 training**
  - Latest version allows proper training of WAN 2.2 models
  - *From: Juampab12*

- **Diffusion-pipe updated with WAN 2.2 folder structure support**
  - No longer need to use old 2.1 folder structure workarounds
  - *From: mrassets*

- **Wan 2.2 support speculation**
  - Ostris mentioned working on formal Wan 2.2 support for AI-toolkit
  - *From: Fill*

- **Runpod template availability**
  - Pre-built runpod template for diffusion-pipe with Wan 2.2 support available
  - *From: CJ*

- **Ostris plans Accuracy Recovery Adapter LoRA for Wan2.2**
  - Will allow training at 3bit under 24GB VRAM, similar to existing QWen-Image 3-bit LoRA
  - *From: JohnDopamine*

- **Fal.ai offers Wan 2.2 training for $4.5-$5**
  - Cloud training option but results reported as poor, naming convention issues
  - *From: Orregon*

- **AI-Toolkit WAN 2.2 branch released**
  - Ostris added WAN 2.2 branch with Adapter LoRA (3-bit) support for training with 24GB VRAM cards
  - *From: JohnDopamine*

- **StableAvatar finetuning codes released**
  - Francis-Rings released finetuning and LoRA training codes for StableAvatar, supports infinite-length videos at various resolutions
  - *From: NebSH*

- **Qwen2.5-omni captioning tool released**
  - New video and image captioner using Qwen2.5-omni 7B-awq model
  - *From: Cseti*

- **Wan 2.2 T2V 14B released with high and low LoRAs**
  - Available alongside the previously released I2V version
  - *From: Janosch Simon*

- **Proper Wan 2.2 training implementation still in progress**
  - Diffusion Pipe hasn't fully implemented proper 2.2 training yet
  - *From: Dream Making*

- **Standard dual training becoming 2 output files trained simultaneously**
  - Major trainers implementing automatic timestep switchover during training
  - *From: CJ*

- **Potential 14x training speedup technique discovered**
  - New technique shows x14 speed up, model agnostic, currently being analyzed for implementation in WAN
  - *From: mamad8*

- **Wan 2.2 testing video released**
  - YouTube video showing 2.2 LoRA testing available
  - *From: crinklypaper*

- **Wan 2.2 launch stream available**
  - Launch stream contains presentation deck with technical details
  - *From: crinklypaper*

- **No public paper for Wan 2.2**
  - Unlike previous versions, no research paper has been published
  - *From: crinklypaper*

- **Official release of Wallace and Gromit style LoRA v1**
  - Community member released first version with documentation
  - *From: crinklypaper*

- **TREAD implementation available for Wan 2.2**
  - Fast training method implemented with 35% VRAM reduction
  - *From: Ada*

- **LightX team making new LoRAs**
  - Current LightX LoRA has issues, team working on replacements
  - *From: asd*

- **Apple released FastVLM and MobileCLIP2**
  - 85x faster and 3.4x smaller than previous work, enables real-time VLM applications and live video captioning locally in browser
  - *From: NebSH*

- **Wan 2.5 release confirmed for January 24th**
  - Release is stronger than a rumour according to community member
  - *From: ZeusZeus (RTX 4090)*

- **New Forge version released**
  - Announcement that there's a new version of Forge out and it's not dead
  - *From: Ruairi Robinson*

- **RamTorch as potential Deepspeed replacement**
  - New tool that could replace Deepspeed for training, recently went through bug fixes
  - *From: JohnDopamine*

- **Runpod now has model store for caching popular models**
  - Servers can cache models so you don't have to download or include in docker image
  - *From: Persoon*

- **New Wan 2.2 T2V Lightning LoRA released**
  - Week-old 4-step lightning lora available at lightx2v/Wan2.2-Lightning - noticeably better quality and text understanding
  - *From: WorldX*

- **RamTorch implementation in AI-Toolkit**
  - Lodestone implemented RamTorch in AI-Toolkit for handling larger models in RAM
  - *From: JohnDopamine*

- **Recent diffusers library changes causing compatibility issues**
  - Changes made to diffusers library 5 days ago regarding attention_dispatch function causing issues with diffusion-pipe
  - *From: Kytra*

- **Musubi Tuner GUI for Wan 2.2**
  - New GUI available at https://github.com/PGCRT/musubi-tuner_Wan2.2_GUI
  - *From: Tachyon*

- **AI Toolkit now has multi-training support**
  - Can train multiple models simultaneously
  - *From: Ryzen*

- **New all-in-one installer available for AI Toolkit on Windows**
  - Makes installation easier on GitHub
  - *From: Ryzen*

- **DimensionX datasets and code released on GitHub**
  - Could potentially work with Wan if trained appropriately, mentioned as potential project
  - *From: happy.j*

- **Oxen.ai offers managed service for Wan fine-tuning**
  - Fully managed dataset upload and fine-tuning with weight access
  - *From: Greg Schoeninger (Oxen.ai)*

- **AI Toolkit added RamTorch support**
  - Built-in feature added 2 weeks ago for better VRAM efficiency
  - *From: Ryzen*

- **Nvidia released 12B Nemotron VL model**
  - New model for video captioning, smaller than 30B Qwen variant
  - *From: Kiwv*

- **Job posting for WAN/VACE finetuning work**
  - Rishi Pandey hiring for video editing precision LoRAs, paying $2K+ per project
  - *From: Rishi Pandey*

- **AI toolkit implementing new loss handling feature**
  - Changes how loss is handled but VRAM stays the same. Decent feature that helps model learn new things
  - *From: Ryzen*

- **QWen 3-VL added to Ollama recently**
  - Now available through Ollama API
  - *From: DeZoomer*

- **ComfyUI-QwenVL project updated 4x recently**
  - Actively maintained project for QWen integration
  - *From: Guey.KhalaMari*

- **Pixel space training breakthrough**
  - New research shows diffusion models can be trained directly on pixels without VAE using clean output reparameterization
  - *From: spacepxl*

- **Crinklypaper released Scooby Doo style LoRA**
  - 27k steps on high, 17k on low, trained with Diffusion Pipe on 3090
  - *From: crinklypaper*

- **LightX released new T2V LoRAs**
  - New distill LoRAs available on HuggingFace
  - *From: crinklypaper*

- **LTX 2 expected early January**
  - Will have higher quality and audio support
  - *From: Kiwv*

- **HuMo dataset released**
  - Dataset available at modelscope.cn/datasets/leoniuschen/HuMoSet
  - *From: hudson223*

- **LTX 2 supports training on AI-toolkit with 5090 VRAM**
  - New model capability mentioned by ostris on X
  - *From: Kiwv*


## Workflows & Use Cases

- **Two-stage image+video training**
  - Use case: Better character LoRAs with preserved motion - train images for 15 epochs, then switch to videos
  - *From: Cseti*

- **Pretraining + finetuning for characters**
  - Use case: High-quality character LoRAs - pretrain on large dataset, then finetune on best 4 images
  - *From: mamad8*

- **Multi-character training with regularization**
  - Use case: Training multiple characters without bleeding - use heavy regularization data with high repeats
  - *From: mamad8*

- **Multi-resolution character training**
  - Use case: Training character LoRAs with multiple dataset configurations at 384, 512, 768, 1024 resolutions
  - *From: mamad8*

- **Photo then video training sequence**
  - Use case: Train photos first, then videos for movement, then photos again for quality
  - *From: mamad8*

- **I2V style transfer training workflow**
  - Use case: Train style changes that appear from frame 2 onwards. Extract first frame, convert to different style (using magnific ai), replace first frame in video with ffmpeg, then train
  - *From: mamad8*

- **Automated style conversion in ComfyUI**
  - Use case: Use model with controlnets to convert first frame to realistic, replace just first frame in otherwise stylized video, then save out for training
  - *From: spacepxl*

- **Low res video + high res image training strategy**
  - Use case: Getting motion from videos and quality from images - 19 videos at low res + 20 high res images for HD inference
  - *From: Juampab12*

- **I2V training with musubi**
  - Use case: Set one dataset for videos only, trainer automatically picks first frame as init image
  - *From: mamad8*

- **Multi-resolution training with same dataset**
  - Use case: Using different target_frames like [1,16,32,45] or [1,25,49] for different video lengths
  - *From: multiple users*

- **I2V transformation LoRA training**
  - Use case: Create 5-frame videos where frame 1 is 'before' image and frames 2-5 are identical 'after' images, then train I2V LoRA
  - *From: mamad8*

- **Aging timelapse I2V training**
  - Use case: Train LoRA on aging progression videos using frame repetition technique to avoid VAE compression artifacts
  - *From: Juampab12*

- **High-res video training with cropping**
  - Use case: Take 4k videos and divide them into 480x480 pieces for training to maintain quality
  - *From: Alisson Pereira*

- **Runpod training setup**
  - Use case: Cloud-based LoRA training with dataset upload via Jupyter notebook and screen for persistent training
  - *From: mamad8*

- **Video cropping for datasets**
  - Use case: Manual cropping to ensure videos crop where intended, not just center
  - *From: Juampab12*

- **Automated dataset generation using existing LoRAs**
  - Use case: Generate videos with existing LoRA, then train new LoRA for different model (e.g. Hunyuan to Wan)
  - *From: Alisson Pereira*

- **Batch video generation with automated prompts**
  - Use case: Create training datasets automatically rather than searching internet
  - *From: Alisson Pereira*

- **Using trigger phrase prepended to all captions**
  - Use case: 'steamboat Willie style' prepended before all captions for consistent style training
  - *From: Benjaminimal*

- **Combined video and image training**
  - Use case: Use small resolution videos for motion learning and high resolution images for detail
  - *From: Juampab12*

- **Style training without style descriptions**
  - Use case: Caption dataset without mentioning the style, let trigger word absorb the visual characteristics
  - *From: spacepxl*

- **Validation-based training monitoring**
  - Use case: Use separate validation set instead of training loss to judge model quality
  - *From: spacepxl*

- **Two-stage watermark removal training**
  - Use case: Train one model to detect watermarks with red rectangles, then another to process only those areas
  - *From: mamad8*

- **Multi-character control using color segmentation**
  - Use case: Use unique colors for each character in segmentation masks to prevent character bleed in multi-subject training
  - *From: spacepxl*

- **YouTube video dataset creation**
  - Use case: Use yt-dlp to download videos in mp4 format with best quality and no audio for training datasets
  - *From: mamad8*

- **Blender camera movement dataset creation**
  - Use case: Creating consistent camera movement LoRAs by rendering same camera path with different scenes/HDRIs
  - *From: ArtOfficial*

- **Gemini video captioning in ComfyUI**
  - Use case: Caption full videos up to 45 minutes using Fill Nodes gemini video node. Adjust frames_per_second (0-2) based on video speed - lower for fast moving content
  - *From: Kytra*

- **Multi-GPU training for faster iteration**
  - Use case: Use multiple GPUs to reduce training time from days to hours. 8x48GB cards for ~$10/hour or 10x3090s for $2.2/hour
  - *From: Kytra*

- **Module-specific training for camera movement**
  - Use case: Creating focused camera movement LoRAs that don't affect subject styling
  - *From: Amirsun(Papi)*

- **Mixed dataset with size buckets**
  - Use case: Training with both images and videos at different resolutions using size_buckets configuration
  - *From: Kytra*

- **Two-phase captioning system**
  - Use case: First pass generates tags, second pass creates natural language descriptions, concatenated for training
  - *From: Kytra*

- **Watermark removal with Wan + VACE + DiffSynth**
  - Use case: Removing watermarks from training datasets using fixed mask and 8-step inference
  - *From: Alisson Pereira*

- **Multi-frame captioning with Ollama**
  - Use case: Creating mosaics from 4-6 video frames and sending to Ollama with Gemma3 for fast batch captioning of 600+ videos
  - *From: Alisson Pereira*

- **Low-res motion + high-res stills training**
  - Use case: Training motion LoRAs using low resolution videos (244p) for motion capture combined with high resolution images (1024p) for quality
  - *From: Multiple users*

- **Resume training from checkpoints**
  - Use case: Continue training on fresh Runpod instance by saving global_step folders and latest file, then using --resume_from_checkpoint flag
  - *From: JohnDopamine*

- **Mixed image-video training for character LoRAs**
  - Use case: Use first frame of each training video as high-resolution image (1024) while training videos at lower resolution (244) for better quality
  - *From: Alisson Pereira*

- **Automated dataset creation using LLM + Flux + Gemma3**
  - Use case: Generate artificial training videos by creating random prompts, generating images with Flux, then creating video prompts with Gemma3
  - *From: Alisson Pereira*

- **Multi-resolution training with different target frames**
  - Use case: Training with [5, 45, 81] target frames using head configuration
  - *From: Benjimon*

- **Images + videos combined training for i2v**
  - Use case: Musubi-Tuner can train images and videos simultaneously for i2v models
  - *From: JohnDopamine*

- **Progressive training with iterative improvement**
  - Use case: Start with images, generate videos, add those to dataset, train more, repeat to build up quality
  - *From: Thom293*

- **Single video LoRA for consistent actions**
  - Use case: Train on one video to get same action every time in generations
  - *From: Kytra*

- **Video + image hybrid training**
  - Use case: Combine video training with high-quality still frames for better results
  - *From: Thom293*

- **Progressive training from images to video**
  - Use case: Start with images only, generate videos from results, then add video directory and continue training to maintain motion
  - *From: Thom293*

- **Anime style conversion workflow created**
  - Use case: Workflow and LoRA to convert videos to anime style on wan 2.1 locally, not yet shared publicly
  - *From: 852話 (hakoniwa)*

- **Opposing LoRA merger workflow**
  - Use case: Generate opposing LoRAs, merge with negative scaling, use SVD to extract merged tensors, downcast to float16
  - *From: Piblarg*

- **Merge LoRAs into base model for simplified inference**
  - Use case: Combine CausVid and custom LoRAs into single model to eliminate need for multiple LoRAs during generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use ComfyUI nodes for video preprocessing**
  - Use case: Load video, caption, and output captions with shortened clips all within ComfyUI
  - *From: Piblarg*

- **Character training progression**
  - Use case: 20 images minimum: 2x front, each side, 3/4, back, high/low angles, full body, sitting/reclining poses
  - *From: Thom293*

- **Video captioning with DeZoomer + SkyCaptioner**
  - Use case: Automated video captioning for training datasets using local models
  - *From: Thom293*

- **Mixed dataset training with images and videos**
  - Use case: Training LoRAs with both high-res images (1024) and videos (256-512) for character/style learning
  - *From: Alisson Pereira*

- **Progressive dataset training**
  - Use case: Start with images for quality, add videos for motion, remove videos at end to clean up - can add/subtract datasets to tune as you go
  - *From: Thom293*

- **Auto video dataset preparation**
  - Use case: Python program that slices videos by scene, crops watermarks, clips to predetermined frame chunks, converts fps
  - *From: CJ*

- **Universal model training**
  - Use case: Train I2V models in T2V to create universal model that works with VACE
  - *From: Alisson Pereira*

- **Face replacement pipeline for music videos**
  - Use case: Replace singer face using LoRA + SAM2 mask, then VACE + mask, then multitalk/liveportrait + mask
  - *From: happy.j*

- **Multi-pass enhancement pipeline**
  - Use case: V2V with character LoRA + SAM2 mask, then VACE 1.3B with points editor and SAM2, then light polishing at 0.1 denoise, then interpolate and upscale
  - *From: mdkb*

- **Style conversion using Kontext**
  - Use case: Run dataset through Kontext with different style prompts to create multiple LoRAs from same dataset (toon, realistic, CGI, etc.)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Skyreels image enhancement using low denoise I2I with ChatGPT vision for prompts**
  - Use case: Enhancing dataset images by running through WAN at 0.5 denoise with AI-generated prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Train at low res then switch to high res for final epochs**
  - Use case: Start training at 512 res, stop, edit config to 1024 for quality improvement
  - *From: MilesCorban*

- **Disposable style LoRA workflow**
  - Use case: Generate overnight img2img against prior generations, train on 15-20 favorites, use resulting LoRA for next generations
  - *From: JohnDopamine*

- **Modular T2V tester workflow for LORA testing**
  - Use case: Test LORAs with original prompts, generate new prompts with Qwen Omni/Instruct/Skycaptioner, includes audio generation capability
  - *From: Thom293*

- **Two-phase training approach**
  - Use case: Phase 1: multiple_overlapping on small dataset, Phase 2: single_middle with low repeats on larger dataset for generalization
  - *From: CJ*

- **Low model only training with full timestep**
  - Use case: Train single LoRA that works on both high and low models by using min_t=0, max_t=1 on low model
  - *From: Alisson Pereira*

- **Mixed image and video training dataset**
  - Use case: Use separate directories for images (1 frame) and videos (33 frames) with different resolutions and repeat counts
  - *From: chancelor*

- **Separate high/low noise LoRA training**
  - Use case: Train high noise for motion (timesteps 0.875-1.0) and low noise for details (timesteps 0-0.875), then use both during inference
  - *From: multiple users*

- **Low-only character LoRA training**
  - Use case: Train character LoRAs only on low noise model with full timestep range (0-1) for better identity capture
  - *From: Alisson Pereira*

- **Fast character LoRA training**
  - Use case: 30-minute training sessions for basic facial features, extend to 5+ hours for complex details like tattoos
  - *From: Kenk*

- **High and low LoRA training with separate configs**
  - Use case: Character and style training with optimal results
  - *From: mamad8*

- **Combined dataset training with videos and images**
  - Use case: 21 videos and 21 higher res first-frame grabs for balanced training
  - *From: MilesCorban*

- **Comprehensive video captioning pipeline in ComfyUI**
  - Use case: Uses skycaptioner for video, joycaption for first frame, LLM to merge captions, includes black bar removal and upscaling
  - *From: mrassets*

- **Video frame captioning with Qwen 2.5 VL**
  - Use case: Review frames in chunks, caption them, then provide unified caption for entire clip
  - *From: CJ*

- **Mixed resolution training strategy**
  - Use case: High model trained at low resolution overnight, then switch to normal resolution
  - *From: crinklypaper*

- **Progressive resolution training**
  - Use case: Train at lower res for majority of epochs, switch to higher res with blockswap for final 20%
  - *From: MilesCorban*

- **Separate high/low model training approach**
  - Use case: High noise: longer videos, lower res for motion/composition. Low noise: shorter videos, higher res for details
  - *From: Kenk*

- **Dual resolution training approach**
  - Use case: Train low resolution first, then bump to high resolution around 3.7k steps (epoch 35)
  - *From: crinklypaper*

- **Multi-resolution dataset setup**
  - Use case: Use same image directory with different resolutions (512, 768, 1024) and separate cache directories
  - *From: aipmaster*

- **High and low noise training separation**
  - Use case: High noise for composition/movement, low noise for details and refinement
  - *From: CJ*

- **High noise with videos + images, low noise with images only**
  - Use case: Character LoRA training for Wan 2.2 - reduces complexity while maintaining quality
  - *From: CJ, el marzocco*

- **Generate I2V videos from images, then select best ones for training**
  - Use case: Create training videos from static images - generate 33-frame videos, pick 15 best for movement, use rest as images
  - *From: el marzocco*

- **Train large datasets with single_beginning and short clips**
  - Use case: Handle 1800+ clips by using 1-second clips with single_beginning mode instead of multiple_overlapping
  - *From: Kenk*

- **Separate high/low noise training workflow**
  - Use case: Training character LoRAs by running separate scripts for high and low noise models using the same dataset
  - *From: screwfunk*

- **Progressive testing strategy for LoRA epochs**
  - Use case: Train 10 epochs high, test, then train 10 low, test combinations like 20/10, 30/20 to find optimal balance
  - *From: mrassets*

- **Automated captioning workflow using JoyCaption**
  - Use case: ComfyUI workflow that processes entire directories of images, generates captions, and creates matching txt files for training
  - *From: screwfunk*

- **Musubi dual-mode training**
  - Use case: Train single LoRA for both high and low noise models simultaneously
  - *From: artificial_fungi*

- **Mixed resolution training for low model**
  - Use case: Combine 640x360 base with few high res samples for better low model results
  - *From: flo1331*

- **JoyCaption ComfyUI workflow for dataset preparation**
  - Use case: Automated captioning of image datasets with customizable criteria and trigger word prepending
  - *From: screwfunk*

- **Dual training with separate high/low LoRA outputs**
  - Use case: Training both models simultaneously but keeping separate LoRA files for flexible inference
  - *From: artificial_fungi*

- **Character LoRA training with 20-30 images at 512x512**
  - Use case: Efficient character likeness training without overtraining
  - *From: MilesCorban*

- **Single LoRA for high/low noise training**
  - Use case: Train one LoRA that works for both high and low noise models, can still adjust strength independently
  - *From: screwfunk*

- **Extract first frame for captioning videos**
  - Use case: Pull first frame from training videos and use for captioning since motion doesn't need frame-by-frame description
  - *From: MilesCorban, screwfunk*

- **Train High model with lower epochs (2-5), then focus on Low model training with same dataset from start**
  - Use case: Style LoRA training for WAN 2.2
  - *From: screwfunk*

- **Use Musubi dual training to create single LoRA file for both high and low models**
  - Use case: Character likeness training with faster results
  - *From: screwfunk*

- **Use ChatGPT for detailed video captioning with specific photographer assistant prompt**
  - Use case: Creating detailed captions for LoRA training datasets
  - *From: flo1331*

- **Generate videos from images using I2V**
  - Use case: Create training videos by plugging images and prompts into Wan 2.2 I2V
  - *From: el marzocco*

- **Caption videos with AI then manually correct**
  - Use case: Use ChatGPT/Claude for initial captions, then manually fix inaccuracies. Limit AI captions to 5-10% of dataset
  - *From: flo1331*

- **Character LoRA training with videos**
  - Use case: Training character likeness with 14 videos, 33 frames each, GAS=2, separate high/low training
  - *From: flo1331*

- **Musubi dual training workflow**
  - Use case: Run cache latents, then text encode, then train. Both processes cached so only run once
  - *From: screwfunk*

- **Test LoRA training by disabling high model and using only low model**
  - Use case: Verify character fidelity is maintained by low model alone, then test different high model checkpoints
  - *From: mamad8*

- **Combine motion LoRA with style LoRA**
  - Use case: Use anime/motion LoRA trained on videos with style LoRA trained on images to get motion from first and style from second
  - *From: samurzl*

- **Auto sigma switching for LoRA training**
  - Use case: Automatically switch between high/low noise models at correct timestep
  - *From: CJ*

- **Manual sigma splitting**
  - Use case: Count sigma values in logs to manually set split points when auto doesn't work
  - *From: crinklypaper*

- **Character LoRA training pipeline**
  - Use case: Train consistent character representation using diverse dataset
  - *From: crinklypaper*

- **Combined image and video training**
  - Use case: Train LoRAs using both video data and higher resolution images
  - *From: MilesCorban*

- **Dual character LoRA training**
  - Use case: Training two separate characters in one LoRA to get both in same scene without blending
  - *From: screwfunk*

- **Single combined high/low LoRA training**
  - Use case: Training both high and low noise models together into single LoRA file using timestep boundary
  - *From: screwfunk*

- **Progressive resolution training**
  - Use case: Start with low res videos (256x144 81 frames), then add high res images for later epochs to improve style grasp
  - *From: Zlikwid*

- **Subgraph workflow for testing multiple LoRA epoch settings**
  - Use case: Testing high vs low epoch settings efficiently
  - *From: crinklypaper*

- **Training high on full resolution/frames, then low on high-res short clips**
  - Use case: Learning motion on high, details on low
  - *From: Ada*

- **Character LoRA training with separate image/video directories**
  - Use case: Training character LoRAs with different settings for images vs videos
  - *From: crinklypaper*

- **High and low noise model training sequence**
  - Use case: Train high noise model first (400-800 steps), then low noise model (800-3000 steps) for character LoRAs
  - *From: flo1331*

- **Multi-GPU training setup**
  - Use case: Run high noise training on one GPU and low noise training on another as separate jobs
  - *From: fearnworks, Zent*

- **Multi-character LoRA training**
  - Use case: Training single LoRA with multiple characters using separate triggers to avoid character bleeding
  - *From: screwfunk*

- **Dynamic dataset switching mid-training**
  - Use case: Change datasets during training to prevent overtraining of certain concepts while others are still learning
  - *From: mrassets*

- **Mixed resolution training approach**
  - Use case: Using 81 frame 16fps low res videos for motion paired with hi-res still images for character training
  - *From: Gentleman bunny*

- **Extensive high noise training**
  - Use case: Training high noise model for 117.5K+ steps to fix motion distortion and improve eye/hand quality
  - *From: crinklypaper*

- **High/Low separate training workflow**
  - Use case: Train High model on videos for motion, Low model on mix of images and videos for style and detail
  - *From: ingi // SYSTMS*

- **Vid2Vid with High/Low combination**
  - Use case: 2 steps with High model (starting from step 2) and 4-5 steps with Low model for better results
  - *From: ingi // SYSTMS*

- **ReActor face swapping workflow**
  - Use case: 512x512 different hairstyles with wildcards, then ReActor the face using celebrity Flux and SD models
  - *From: Kenk*

- **Character LoRA training with 18 images using specific musubi-tuner command**
  - Use case: Training character LoRAs for Wan 2.1 with good results
  - *From: Tachyon*

- **Video preparation for training: scale to target resolution, convert to 16fps using shotcut and ffmpeg**
  - Use case: Preparing video datasets for LoRA training
  - *From: flo1331*

- **FAL.ai for quick LoRA testing**
  - Use case: Fast $5, 30-minute character LoRA training for testing purposes (images only)
  - *From: shotgun messiah*

- **Train character LoRAs using 12 images from single photo shoot with different poses**
  - Use case: Better results than using 30 random images of same person
  - *From: el marzocco*

- **Train style LoRAs by captioning everything except the style**
  - Use case: Gets style baked into LoRA without describing it in captions
  - *From: crinklypaper*

- **ComfyUI workflow for captioning with Gemini**
  - Use case: Automated dataset captioning for LoRA training
  - *From: Muon*

- **Character + Style LoRA training approach**
  - Use case: Character consistency with style transfer
  - *From: Kytra*

- **Using Flux D LoRA for Wan training**
  - Use case: Train a LoRA for Flux D, generate images, then use those images to train Wan
  - *From: Ryzen*

- **Two-pass training for motion and likeness**
  - Use case: Run one training with sigmoid for likeness, another with shift for motion capture
  - *From: Tachyon*

- **Automated video dataset preparation**
  - Use case: Scripts for converting long-form video to captioned training data with keyframes
  - *From: Muon*

- **High model for complex motion, Low model for character details**
  - Use case: Training character LoRAs with motion capabilities
  - *From: Dream Making*

- **Train high model first, then focus on low model for character likeness**
  - Use case: Character LoRA training workflow
  - *From: crinklypaper*

- **Use JoyCaption in ComfyUI to generate captions from folder in 1 click**
  - Use case: Automated dataset captioning
  - *From: el marzocco*

- **Test high 2.2 with low 2.1 LoRA when training new 2.2**
  - Use case: Testing during 2.2 training process
  - *From: crinklypaper*

- **Train 5B model first as proof of concept, then move to larger model**
  - Use case: Experimenting with captions and reducing bleeding before full training
  - *From: Guey.KhalaMari*

- **Train individual character LoRAs, merge, then train with combined dataset**
  - Use case: Creating multi-character LoRAs while avoiding bleeding
  - *From: Guey.KhalaMari*

- **Use rotation LoRAs or Phantom to generate different angles for training data**
  - Use case: Augmenting limited dataset with varied perspectives
  - *From: Thom293*

- **I2V training workflow**
  - Use case: 52 5-second clips, hand captioned, took 400 steps to train
  - *From: Kiwv*

- **Character LoRA training with identical descriptions**
  - Use case: Training consistent character appearance with trigger word
  - *From: metaphysician*

- **Multi-dataset LoRA training with separate trigger words**
  - Use case: Training multiple concepts in one LoRA using different trigger words for each dataset
  - *From: Ryzen*

- **Train at 121 frames to extend Wan's frame capability**
  - Use case: Extending default 81 frame limit to enable longer 7.5 second videos, similar to how Holocine worked
  - *From: Kiwv*

- **Multi-step realistic character LoRA creation**
  - Use case: Creating high-quality person LoRAs: 1. Image-only LoRA 2. Generate videos with Phantom 3. Combined image+video LoRA 4. More videos 5. Final LoRA with new data
  - *From: Thom293*

- **WAN 2.2 image generation with LoRAs**
  - Use case: Use same LoRA in both high and low model slots, or high model without LoRA + low model with LoRA
  - *From: Dream Making*

- **Image + video mixed training**
  - Use case: Character LoRAs - prefer 20-30% videos unless motion focused. Videos harder to prepare than images
  - *From: crinklypaper*

- **Style LoRA training with 600 images + 120 videos**
  - Use case: Teen Titans style LoRA, 512x images 256x videos, trained to 47k total steps
  - *From: crinklypaper*

- **Hand captioning datasets instead of auto-captioning**
  - Use case: Ensuring high quality captions for LoRA training
  - *From: Kiwv*

- **Using Google API searches to auto-crop, caption and downscale images**
  - Use case: Automated dataset creation for character LoRAs using vibecode automation
  - *From: oskarkeo*

- **Training high and low noise models separately on 2 GPUs**
  - Use case: Parallel training to utilize multiple GPU setup
  - *From: HeadOfOliver*

- **Dual mode training with one LoRA file**
  - Use case: Train once to get file that works on both high and low noise models
  - *From: artificial_fungi*

- **Character + style training approach**
  - Use case: Minimum 150+ images for style LoRA with multiple characters to prevent character blending
  - *From: crinklypaper*

- **Video dataset preparation**
  - Use case: Split into 55 frame maximum clips at 16fps, manually pick scenes without cuts
  - *From: crinklypaper*

- **Context window multi-prompt generation**
  - Use case: Generate long videos with multiple scene transitions in single generation
  - *From: avataraim*

- **Progressive resolution training**
  - Use case: Start training at 256px, finish with high-res epochs for detail enhancement
  - *From: Thom293*

- **Living LoRA methodology**
  - Use case: Continuously adjust datasets during training for iterative improvement
  - *From: Thom293*

- **Put images in wan i2v and prompt a video to get both still and video**
  - Use case: Getting both image and video data for training
  - *From: Thom293*

- **Start with high LR, reach overfitting, go back steps and resume with lower LR**
  - Use case: Progressive learning rate training for better lora quality
  - *From: mrassets*

- **Test in-distribution and out-of-distribution prompts during training**
  - Use case: Monitoring generalization vs overfitting
  - *From: spacepxl*

- **Training multiple LoRAs simultaneously on same base model**
  - Use case: Can set weight for each adaptor to control which is active, minimal VRAM overhead unless using massive rank
  - *From: spacepxl*


## Recommended Settings

- **Learning rate**: 2e-5 for 14B, batch size 1
  - Works best after 50+ training runs, prevents overfitting
  - *From: mamad8*

- **LoRA rank**: 32 for 1.3B, 64-128 for complex concepts
  - 32 sufficient for 1.3B, higher ranks needed for complex character features
  - *From: samurzl*

- **Batch size scaling**: Scale LR with sqrt(batch size)
  - Maintains training dynamics when increasing batch size
  - *From: spacepxl*

- **Resolution for 1.3B**: 480p for best results
  - Model performs better with 480p training than higher resolutions
  - *From: comfy*

- **Optimizer**: adamw_optimi, lr=2e-5, betas=[0.9, 0.99], weight_decay=0.01
  - Default settings work well for most use cases
  - *From: Juampab12*

- **Learning rate**: 2e-5
  - Optimal for batch size 1 with alpha=rank
  - *From: mamad8*

- **Rank for character LoRA**: 32-64
  - 64 for single character, 128 overkill. Used 128 for 4 characters
  - *From: mamad8*

- **Video resolution for training**: 256x384, 384x256, or 384x384
  - Good balance for 24GB VRAM with 33-81 frames
  - *From: mamad8*

- **Batch size**: 1
  - Standard for LoRA training
  - *From: mamad8*

- **Alpha setting**: Equal to rank
  - Avoids musubi default alpha=1 which requires much higher learning rates
  - *From: mamad8*

- **LoRA rank for character training**: 64, batch size 1, LR 2e-5, multi-resolutions 384/512/768/1024, only images, 20-50 photos
  - Works well for character consistency training on 14B model
  - *From: mamad8*

- **Tile LoRA training parameters**: 5e-6 for 20k steps then 1e-5 for 12k steps, rank=128, alpha=128
  - Progress was slowing down so increased learning rate
  - *From: spacepxl*

- **I2V 14B learning rate**: 2e-5
  - Worked great in multiple use-cases, though requires 24 hours training on L40S
  - *From: mamad8*

- **24GB VRAM training config**: enable_ar_bucket=true, min_ar=0.5, max_ar=2.0, resolutions=[244,768], images at 768px/1 frame, videos at 244px/33 frames
  - Works on 24GB GPU
  - *From: chancelor*

- **General training parameters**: Batch size 1, makes it easy to do mixed resolution/frames
  - No quality benefit to higher batch sizes in image models, only hardware efficiency
  - *From: spacepxl*

- **LoRA rank recommendations**: 16 rank should be good enough for 99% of stuff, use 16 for known concepts, 32 for new data
  - Based on image model experience. 16 worked for camera movement, 32 for camera + new data
  - *From: Ada*

- **Resolution for movement training**: 384x256 for 14B model training
  - 14B does extremely well at this resolution for movement/action training
  - *From: mamad8*

- **Learning rate for I2V training**: 2e-4
  - Working well, will reduce to 5e-5 if too much
  - *From: Ada*

- **Target frames for cakify-style training**: [1,25,49]
  - Works with any frame length perfectly
  - *From: Juampab12*

- **Training epochs**: 16 epochs in 20 minutes
  - Sufficient for good results with WAN's fast learning
  - *From: Juampab12*

- **Learning rate for character training**: 7e-5
  - Used successfully for character LoRA training
  - *From: chancelor*

- **Frame rate for training videos**: 16 fps
  - Standard framerate for WAN training
  - *From: Juampab12*

- **Network alpha default**: 1 (default)
  - No difference when adjusted properly with learning rate
  - *From: spacepxl*

- **Learning rate for aging timelapse**: 7e-7 with 72 epochs
  - Successfully trained timelapse LoRA
  - *From: Juampab12*

- **Learning rate for transformation LoRA**: 2e-5 with rank 64, alpha 64
  - Used for furnish/empty room transformation with 250 videos, 6500 steps
  - *From: mamad8*

- **VAE finetuning learning rate**: 1e-6 * sqrt(batch_size)
  - Good starting point for VAE training
  - *From: spacepxl*

- **Learning rate adjustment for alpha**: multiply/divide by sqrt(alpha) when comparing different alphas
  - Rank is unrelated to learning rate unless alpha is set based on rank
  - *From: spacepxl*

- **Transformer dtype for 14B on 4090**: float8
  - Allows training on 4090 but is very slow
  - *From: Frojef*

- **Learning rate range**: 0.095 - 1.2
  - General working range
  - *From: Mngbg*

- **LoRA rank/alpha/LR combo**: 16 rank, 5e-5 lr, 1 alpha
  - Beginner-friendly settings
  - *From: Juampab12*

- **I2V frame buckets**: [25, 33]
  - Avoid frame bucket '1' and match video lengths
  - *From: mamad8*

- **Large model frame buckets**: [1, 33, 65, 81, 97, 113]
  - For training with multiple frame lengths on high VRAM systems
  - *From: Benjaminimal*

- **Resolution for large training**: [[832, 480]]
  - 832x480x113 frames = 45,240 tokens, manageable on 8xH100
  - *From: Benjaminimal*

- **VRAM token limits**: 1280x720x45 ≈ 43k tokens
  - 720p at 45 frames should fit on high-end hardware
  - *From: spacepxl*

- **Learning rate for styles**: 5e-5
  - Really stable for style training
  - *From: Mint*

- **Learning rate for depth control LoRA**: 2e-6
  - Converges faster and more stable than higher rates like 1e-5
  - *From: spacepxl*

- **Rank and alpha for depth control**: rank=128, alpha=128
  - Used in successful depth control LoRA training
  - *From: spacepxl*

- **Frame buckets for training**: 33, 49, 65, 81, 97, 113 frames
  - Used for varied length training at 480p
  - *From: Benjaminimal*

- **Learning rate for steamboat Willie style**: 1e-4
  - Worked well for ~80 clip dataset over 2500 steps
  - *From: Benjaminimal*

- **Block swap threshold**: 20+
  - Good starting point for 14B training, can go higher
  - *From: Alisson Pereira*

- **Learning rate for 14B I2V**: 5e-5
  - Used successfully with 149 videos, 64 frames, 48GB VRAM
  - *From: Alisson Pereira*

- **Rank for 14B training**: 64
  - Used with adamw8bit optimizer
  - *From: Alisson Pereira*

- **Training configuration for style LoRA**: target_frames = [1,25,69,81], resolution = [128,170], num_repeats = 2
  - Recommended for 24GB VRAM training
  - *From: Juampab12*

- **Network dimension**: 16
  - Used in successful training setup
  - *From: Juampab12*

- **Discrete flow shift**: 5.0
  - Standard setting for Wan training
  - *From: Juampab12*

- **Lego LoRA settings**: LR: 2e-5 then 8e-5, Rank: 128, 672x384 resolution
  - Used for 1500 video clip training with visible progress
  - *From: Cseti*

- **Block swapping**: 20 blocks
  - Enables 512x512x81f training on 24GB VRAM
  - *From: ArtOfficial*

- **Learning rate scaling with alpha**: lr @ alpha 1 = sqrt(128) * lr @ alpha 128
  - Alpha affects effective learning rate by square root relationship
  - *From: spacepxl*

- **Control LoRA latent noise**: 0.1 factor (random amount up to limit)
  - Helps with training regularization for low quality input videos
  - *From: spacepxl*

- **Timestep shift for depth control**: shift=5
  - Makes model pay attention to depth signal during training
  - *From: spacepxl*

- **Face LoRA training parameters**: 1.5e-5 LR, alpha=1, rank=64, flow=5
  - Conservative settings for multi-day training session
  - *From: Juampab12*

- **max_pixels parameter for VRAM optimization**: Lower values for 24GB VRAM
  - Defines max pixels per frame (width × height) to control VRAM usage
  - *From: Cseti*

- **Learning rate for quick style training**: 4e-4
  - Higher learning rate works well with Wan, can learn concepts quickly. Expects results within 10 epochs
  - *From: Kytra*

- **Character LoRA training settings**: LR 1.5e-5, rank 64, alpha 1
  - Used successfully for 65-hour training with 9k videos, trained for only 7 epochs total
  - *From: Juampab12*

- **Gemini frames_per_second for video captioning**: 0.8 to 1.0
  - Float between 0-2, lower means AI watches more closely. Use lower values for super fast moving videos
  - *From: Kytra*

- **Recommended video resolution for fal.ai training**: 416x240
  - Haven't seen much gain going higher resolution for character LoRAs
  - *From: Benjaminimal*

- **Target frames for character LoRA**: 81 frames at 16 fps
  - About 5 seconds total, works best with current Wan training
  - *From: Benjaminimal*

- **Training steps range**: ~1k to ~2k total steps
  - Depends on dataset size. On 8 GPUs this equals 125-250 steps due to step = one sample across all devices
  - *From: Benjaminimal*

- **Resolution for 14B model training**: [[1280,720]] for 720p content
  - Use double brackets for resolution specification in diffusion-pipe config
  - *From: ArtOfficial*

- **Learning rate for camera movement**: 5e-5
  - Works well for camera motion training when captions are good
  - *From: Amirsun(Papi)*

- **Rank for person training**: 32
  - Standard starting point for character LoRAs
  - *From: JohnDopamine*

- **Repeats calculation**: 3000steps/(videos×epochs)
  - Calculate repeats needed for desired total steps across dataset
  - *From: Amirsun(Papi)*

- **Checkpoint frequency**: save_every_n_epochs = 1
  - Ensures you get safetensors output after each epoch
  - *From: JohnDopamine*

- **Frame rate for training videos**: 16 fps
  - Recommended frame rate for WAN model training
  - *From: Alisson Pereira*

- **Learning rate**: 2e-5 to 3e-5
  - Wan really likes low learning rates, 2e-5 showed better loss than 3e-5
  - *From: Benjimon*

- **Network alpha**: 1 (default)
  - Default network alpha of 1 instead of matching rank
  - *From: Benjimon*

- **Learning rate for dim 32**: 5e-4
  - Good LR for network dimension of 32
  - *From: Benjimon*

- **Flow shift**: 1-3
  - Default flow shift too high at 6.0, should use 1-3
  - *From: Benjimon*

- **Loss target**: <0.10, ideally 0.06-0.095
  - Most good LoRAs achieved loss in this range
  - *From: Benjimon*

- **Training resolution**: 256x144 for 16:9, as low as 64x64 for motion
  - 512 is overkill, great success at 121 frames at 256p, motion LoRAs work at extremely low resolution
  - *From: CJ*

- **Training steps for simple motion**: At least 2000 steps (40 epochs)
  - Minimum recommended for motion LoRAs with ~50 video samples
  - *From: Alisson Pereira*

- **Training resolution and frames for 5090**: 244p resolution with 81 frames, or 256x384x81 with 5 blocks swapped
  - Balance between speed and VRAM usage
  - *From: Alisson Pereira*

- **Block swapping for 48GB GPU**: resolution = [480, 480] with 20 blocks swapped uses about 45-46GB
  - Fits within VRAM limits
  - *From: Benjimon*

- **Working resolutions for training**: resolution = [432, 768] target_frames = [24] OR resolution = [216, 384] max_frames = 64
  - Both work within VRAM settings
  - *From: Piblarg*

- **Gradient accumulation steps**: 1
  - Higher values can cause buckets to be dropped if batch_size becomes effectively higher than available samples
  - *From: Alisson Pereira*

- **Checkpoint frequency**: checkpoint_every_n_minutes = 7 to 20
  - More frequent checkpoints provide better flexibility for resuming training
  - *From: JohnDopamine*

- **Caption token limit**: Assumed 512 tokens
  - Standard limit though not thoroughly investigated
  - *From: Benjimon*

- **Learning rate for WAN training**: 2e-5 to 3e-5
  - Lower rates work better than higher ones that cause loss to go up
  - *From: Benjimon*

- **Block swap for 14B training**: 30-35 blocks
  - Allows higher resolution/frame training without speed impact
  - *From: Piblarg*

- **Target frames for training**: [5, 45, 81]
  - Progressive frame training approach
  - *From: Benjimon*

- **Resolution for 14B training with 48GB VRAM**: 480x480
  - Can do 20 blocks swapped without being too slow
  - *From: Benjimon*

- **Gradient accumulation for images**: 4
  - Helps stabilize training and reduces steps by factor of accumulation
  - *From: Thom293*

- **Learning rate for smaller datasets**: 2e-4
  - Higher rate works fine with smaller datasets and trains faster
  - *From: Piblarg*

- **Target loss range**: 0.04-0.1
  - Normal range for good training
  - *From: Benjimon*

- **Learning rate for character LoRAs**: 6e-5 to 1e-4
  - Good range for likeness training, depends on dataset size
  - *From: MatiaHeron*

- **Frame buckets for video training**: [1, 33, 65, 81]
  - Prevents videos from being chopped too much, accommodates different video lengths
  - *From: Thom293*

- **Resolution for motion training**: 160x240 or 512x512
  - Low res sufficient for motion capture, higher res for quality details
  - *From: Think*

- **Sampling parameters for Musubi**: --w 480 --h 480 --f 49 --s 20
  - Good default settings for sample generation during training
  - *From: JohnDopamine*

- **Video clip mode**: single_beginning or multiple_overlapping
  - single_beginning for pre-edited videos, multiple_overlapping for longer source videos
  - *From: Zlikwid*

- **Epochs for image training**: 15-20 epochs optimal
  - 10 epochs pretty good already, 20+ loses movement and looks rigid for style LoRAs
  - *From: Thom293*

- **Repeats for images**: 10 repeats for 1024x1024 images
  - Should get good results at default settings between 15-40 epochs
  - *From: Thom293*

- **Dataset size for character training**: 12-30 images for single human likeness
  - More often than not you'll just confuse it with too many images
  - *From: JohnDopamine*

- **Multiple resolutions frame_buckets**: [[768, 768], [768, 1024]] with frame_buckets = [1, 1]
  - Frame_buckets array must match number of resolution buckets defined
  - *From: crinklypaper*

- **4090 training settings**: Repeats 5, transformer dtype float8, save_dtype bfloat16, blocks_to_swap 8
  - Avoids OOM and produces good results for character LoRA training
  - *From: crinklypaper*

- **Blocks to swap for 4090**: 14-20 blocks
  - Went from 45-90s/it to 2.9s/it, allows larger datasets
  - *From: Think*

- **High-end training config**: fp16 model, fp8_base, fp8_scaled, block swap 20, flash_attn, split_attn, gradient checkpointing, dim 32, alpha 16, loraplus=4, lr 1e-5
  - Handles 213 video dataset at 11s/it with 23.5gb VRAM usage
  - *From: Persoon*

- **batch_size**: 2
  - Good balance for RTX 5090 with 1024x1024 images, prevents OOM while maintaining speed
  - *From: VRGameDevGirl84(RTX 5090)*

- **num_repeats**: 5
  - Default setting that works well for most datasets, can increase to 10 for larger VRAM
  - *From: Piblarg*

- **resolution**: [960, 544] or [1024, 1024]
  - Good balance between quality and training speed/VRAM usage
  - *From: Piblarg*

- **discrete_flow_shift**: 5.0 for Wan
  - Proper shift value for Wan models in Musubi Tuner
  - *From: Piblarg*

- **learning_rate**: 2e-4 for Musubi, 2e-5 for Diffusion Pipe
  - Default learning rates that work well for respective training tools
  - *From: Piblarg*

- **blocks_to_swap**: 5 for RTX 5090
  - Allows training without block swapping on high VRAM cards
  - *From: Piblarg*

- **max_train_epochs**: 25-35 for images, 50+ for complex styles
  - Image-only LoRAs typically converge faster than video training
  - *From: Thom293*

- **blocks_to_swap**: 20-30
  - Enables high resolution training (640-720p) on consumer GPUs
  - *From: Thom293*

- **Musubi Alpha**: 1 (default)
  - Unlike other trainers that use alpha=DIM/Rank, Musubi uses alpha=1, so learning rate should be set faster
  - *From: JohnDopamine*

- **discrete_flow_shift**: 3-7
  - Higher values allow more change in earlier timesteps, good for dynamic motion
  - *From: JohnDopamine*

- **sample_every_n_steps**: 250-500
  - Good balance for monitoring training progress without slowing down too much
  - *From: JohnDopamine*

- **eval_micro_batch_size_per_gpu**: 1
  - Prevents OOM issues during training
  - *From: crinklypaper*

- **Resolution bucketing**: [512] under video folder
  - Automatically resizes videos while allowing different resolution for images at top level
  - *From: Thom293*

- **Automagic optimizer**: lr = 1e-6, weight_decay = 0.00195, lr_bump = 5e-6
  - Converges much faster with per-parameter learning rates
  - *From: Alisson Pereira*

- **Video bitrate for quality training**: 20,000 (H264) or high value with ApplePro
  - Maintain high bitrate even at small resolution to preserve quality
  - *From: Alisson Pereira*

- **Character training dataset**: 10 images at 256x256, 1K epochs
  - Resolution not important part, gives model leeway for contextual differences
  - *From: mdkb*

- **CRF value for video resizing**: crf of 2
  - Smaller crf maintains closer to original quality, default crf causes compression
  - *From: Alisson Pereira*

- **Learning rate for large datasets**: 8e-5
  - LR 2e-5 was too slow for big dataset, 4e-4 fell apart quickly, 8e-5 worked well
  - *From: Cseti*

- **Gradient accumulation and batch size**: GAS 1 and Batch 1
  - Used for Wallace and Gromit 14B training with good results
  - *From: Cseti*

- **Training resolution for character LoRAs**: 1080p images
  - Much better results than 256x256 for character fidelity, especially for intricate details like tattoos
  - *From: hablaba*

- **LoRA strength for neutral face issue**: 0.8
  - Most common strength used when faces stuck in neutral expression due to lack of emotional training data
  - *From: mdkb*

- **Repeats for good results**: 10 repeats
  - Better results than 2 repeats, used with 150 images for style LoRA
  - *From: VRGameDevGirl84(RTX 5090)*

- **Training resolution**: 720x720
  - Resolution used for successful elven style LoRA training
  - *From: VRGameDevGirl84(RTX 5090)*

- **Training resolution**: 720x720 or 768x768
  - Good balance of quality and training time, 1024x1024 takes much longer
  - *From: VRGameDevGirl84(RTX 5090)*

- **Epochs for style LoRA**: Around 75 epochs
  - Default diffusion-pipe settings, 20 epochs often not enough
  - *From: Thom293*

- **Video clip length**: 5 seconds
  - Standard recommendation for training
  - *From: Thom293*

- **Training steps for 14B model**: 4000 steps
  - Successful 14B style LoRA with 60 training images
  - *From: Jas*

- **Repeats and gradient accumulation**: Repeats 1, Gradient accumulation 1
  - Allows higher resolution training locally
  - *From: Thom293*

- **Learning rate for dataset size**: 1e-4 for 50-100 images, 5e-5 for 200-500 images
  - Larger datasets need lower learning rates
  - *From: jikan*

- **High noise model timesteps**: min_timestep = 875, max_timestep = 1000
  - Corresponds to inference boundary of 0.875-1.0
  - *From: seruva19*

- **Low noise model timesteps**: min_timestep = 0, max_timestep = 875
  - Corresponds to inference boundary of 0-0.875
  - *From: seruva19*

- **Video training repeats**: 1 repeat only
  - Higher repeats not possible at 512+ resolution locally on 5090
  - *From: Thom293*

- **Recommended epochs/steps**: 5-10k steps minimum for video LORAs, 20-30k steps typical
  - Video LORAs need more training than image LORAs
  - *From: Thom293*

- **Automagic optimizer config**: lr=1e-6, weight_decay=0.00195, lr_bump=5e-6
  - Proven working configuration for Wan 2.2 training
  - *From: Alisson Pereira*

- **Low model timestep range**: min_t=0, max_t=1
  - Covers full timestep range so LoRA can be applied to both high and low models
  - *From: Alisson Pereira*

- **High model timestep range**: min_t=0.875, max_t=1
  - Official range for high noise model training
  - *From: mamad8*

- **Training parameters for character LoRA**: rank=64, batch_size=1, 16fps, 49 frames, 256p resolution, automagic optimizer
  - Working configuration for character training with 301 video samples
  - *From: Alisson Pereira*

- **Learning rate for automagic optimizer**: 1e-6 to 2e-5
  - Lower rates are more conservative, automagic adjusts per gradient
  - *From: Alisson Pereira*

- **Weight decay for automagic**: 0.01
  - Standard recommended value, can be as low as 0.0
  - *From: Alisson Pereira*

- **Batch size and gradient accumulation**: batch_size=2, gradient_accumulation_steps=2
  - Good balance for memory usage and training stability
  - *From: mamad8*

- **LoRA rank**: 32
  - Standard rank for character LoRAs
  - *From: multiple users*

- **High noise timestep range**: min_t=0.875, max_t=1.0
  - Specialized for high noise/motion training
  - *From: multiple users*

- **Low noise timestep range**: min_t=0, max_t=0.875 (or 0-1 for full range)
  - Specialized for details and character features
  - *From: multiple users*

- **High noise timestep range**: min_t = 0.875, max_t = 1
  - Targets high noise portion of diffusion process
  - *From: jikan*

- **Low noise timestep range**: min_t = 0, max_t = 0.875
  - Targets low noise portion for detail learning
  - *From: jikan*

- **Learning rate**: LR 4e-5
  - Part of working config for Wan 2.2
  - *From: mamad8*

- **Batch size and gradient accumulation**: batch size 2, gradient accumulation 2
  - Works well with Wan 2.2 default config
  - *From: mamad8*

- **High LoRA rank**: rank=16
  - To save disk space (results in ~160mb file)
  - *From: Kenk*

- **Low LoRA rank**: rank=32
  - Higher rank for detail capture
  - *From: Kenk*

- **Resolution for images**: 512
  - Good balance of quality and training speed
  - *From: Kenk*

- **Resolution for videos**: 226 or 265
  - Reduced from 512 for faster training
  - *From: Kenk*

- **lr_bump in Automagic**: 5e-6
  - Used for dynamic learning rate adjustment, increments/decrements individual gradient learning rates
  - *From: MilesCorban*

- **Training steps for character LoRA**: 500-750 steps
  - Probably sufficient, though original training went to 3000 steps
  - *From: orabazes*

- **Video dataset for character training**: 15 videos, 5 seconds each, 768x768
  - Effective dataset size for character LoRA training
  - *From: orabazes*

- **LightX2V weight for WAN 2.2**: 0.125
  - Recommended weight by Kijai for new Lightning LoRAs
  - *From: _Djent_*

- **Character dataset minimum**: 20 images at 512x512
  - Include face, upper body, full body, and back views for character training
  - *From: ybo678*

- **Automagic optimizer config**: lr=2e-5, weight_decay=0.00195, lr_bump=5e-6, eps=1e-8
  - Fast training with good results
  - *From: crinklypaper*

- **High model timesteps**: min_t=0.875, max_t=1.0
  - Required for high model training, different from low model
  - *From: aipmaster*

- **720p training settings**: frame_bucket=16, rank=16 or 32
  - Enables higher resolution training with manageable VRAM
  - *From: Kenk*

- **Video resolution for training**: 288x384 for videos, 576x768 for images
  - Balanced quality vs VRAM usage
  - *From: crinklypaper*

- **Blockswapping configuration**: 15 blocks for 720p training
  - Enables high resolution training on limited VRAM, ~1.1h per epoch
  - *From: Kenk*

- **Small dataset fast training**: 384x192 resolution, 8-10 videos
  - Very fast training in 2 hours for quick testing
  - *From: avataraim*

- **discrete_flow_shift**: 7 for high noise, 3 for low noise
  - 1.0 causes rough sketching, 3.0 for details, 7.0 for composition
  - *From: uff*

- **learning_rate**: 5e-5 and 4e-5 both work similarly
  - Both stabilize at same rate for high noise model
  - *From: tarn59*

- **min_t/max_t for high noise**: min_t = 0.875, max_t = 1.0
  - Correct timestep range for high noise expert
  - *From: Kytra*

- **min_t/max_t for low noise**: min_t = 0, max_t = 0.875
  - Correct timestep range for low noise expert
  - *From: Alisson Pereira*

- **batch_size**: 1-2 maximum
  - Higher batch sizes don't make sense unless large dataset
  - *From: Alisson Pereira*

- **network_dim**: 32
  - Used in successful character lora training
  - *From: aipmaster*

- **Loss target for low noise**: 0.08 to 0.07 range
  - Training to 0.043 comes out hazy, while 0.08-0.07 range looks better
  - *From: CJ*

- **Epochs for character LoRAs**: High: 70-100 epochs, Low: 10-20 epochs
  - Based on successful training with 15 images + 15 videos dataset
  - *From: el marzocco*

- **Min/max t values**: Low noise: min_t=0, max_t=0.875. High noise: min_t=0.875, max_t=1
  - Required settings for training respective noise models in Wan 2.2
  - *From: MatiaHeron*

- **Frame buckets for video training**: 16 frames for memory efficiency
  - Takes less VRAM while still capturing motion context
  - *From: Kenk*

- **Video resolution strategy**: Low noise: 768x video + 1024x images. High noise: 512x for efficiency
  - Balance between quality and VRAM usage
  - *From: CJ, Kenk*

- **Batch size for datasets over 100 steps**: 2 or 4
  - Helps prevent overfitting and training issues
  - *From: mrassets*

- **Low noise AdamW optimizer config**: lr=2e-5, betas=[0.9, 0.99], weight_decay=0.01, eps=1e-8, gradient_accumulation_steps=4
  - Works better than Automagic for low noise training
  - *From: screwfunk*

- **High noise timestep range with Lightning LoRAs**: timestep 1 to 0.875 across full 5 steps using DPM++/SDE scheduler
  - Follows simple sigma route for better quality with speed LoRAs
  - *From: CJ*

- **Character training dataset size**: 30-40 images with captions
  - Sufficient for character LoRA training
  - *From: screwfunk*

- **JoyCaption settings**: Custom settings shown in screenshot for detailed character descriptions
  - Produces high-quality captions for training
  - *From: screwfunk*

- **blockswap**: 36
  - Enables training on 16GB VRAM
  - *From: flo1331*

- **optimizer**: adamw_optimi for LOW model
  - Better results than automagic optimizer
  - *From: crinklypaper*

- **shift**: 5
  - Standard setting for 2.2, rarely needs adjustment
  - *From: crinklypaper*

- **timestep_boundary**: 875 for T2V
  - Default value for switching between high/low models in dual training
  - *From: JalenBrunson*

- **learning_rate**: 0.000025 for dual mode
  - Conservative rate for stable training
  - *From: artificial_fungi*

- **blocks_to_swap**: 15
  - For training 81 frames on 24GB VRAM
  - *From: chancelor*

- **Character LoRA training resolution**: 720x720 or 512x512
  - Mix of full body and face closeups turns out good results without needing high resolution
  - *From: el marzocco*

- **Timestep sampling**: sigmoid
  - Does better job on details like tattoos for character LoRAs
  - *From: hablaba*

- **LoRA weights for lightning setup**: 1.0 high, 0.8 low
  - Lightning 1.1 on high, LightX2V on low noise model
  - *From: CJ*

- **Maximum block swap**: 39 blocks
  - Maximum supported blocks for swapping in training
  - *From: 557733681767120896*

- **Shift parameter**: 1.5
  - Produces preferred generation results
  - *From: CJ*

- **rank**: 16
  - Faster training, focuses on essential details without learning unwanted elements like lighting
  - *From: Alisson Pereira*

- **resolution**: 512 or 256 (single dimension)
  - Let AR buckets handle aspect ratios automatically rather than fixing both dimensions
  - *From: Alisson Pereira, CJ*

- **dataset size for characters**: ~30 images, repeat 1, gas 3-4
  - K3NK's fast training approach, results in 10-13 steps per epoch
  - *From: CJ*

- **timestep for high noise training**: --min_timestep 875 --max_timestep 1000
  - For training high noise model with preserve_distribution_shape
  - *From: GOD_IS_A_LIE*

- **Learning rate**: 2e-5 (0.00002)
  - Lower LR prevents overfitting to training data outfits
  - *From: flo1331*

- **Weight decay**: 1e-2
  - Standard setting used in musubi
  - *From: flo1331*

- **Resolution settings**: resolutions = [512] instead of fixed aspect ratios
  - Improves training results significantly
  - *From: crinklypaper*

- **High model timesteps**: min_t = 0.875, max_t = 1
  - Standard recommended timesteps for high noise training
  - *From: crinklypaper*

- **Musubi timestep boundary**: --timestep_boundary 875
  - Defines when to switch from high to low during dual training
  - *From: screwfunk*

- **High noise LoRA strength**: 0.01
  - Reduces motion distortion while maintaining style
  - *From: crinklypaper*

- **Low noise LoRA strength**: 1.0
  - Standard strength for low noise component
  - *From: crinklypaper*

- **LightX2V settings**: High: 1.2, Low: 0.8
  - Recommended values for character LoRAs
  - *From: WorldX*

- **Character LoRA strength in ComfyUI**: High: 1.25, Low: 1.0
  - Balanced settings for character generation
  - *From: WorldX*

- **Euler sampler settings**: 20 steps, split at 10 (10/10)
  - Used for testing with lower resolution 832x480, 49 frames
  - *From: crinklypaper*

- **Learning rate for WAN**: 1e-6 or 2e-5
  - Only LR values that work well for WAN training
  - *From: CJ*

- **High noise timesteps**: min_t = 0.875, max_t = 1
  - Official example for high noise model training
  - *From: Fawks*

- **Low noise timesteps**: min_t = 0, max_t = 0.875
  - Complementary range to high noise for low noise training
  - *From: MilesCorban*

- **Flow shift values**: 3.0 for low, 7.0 for high
  - Used in successful training configuration
  - *From: flo1331*

- **Network dim and alpha**: 20 for both dim and alpha
  - Part of working configuration with CAME optimizer
  - *From: flo1331*

- **Gradient accumulation steps**: 2
  - Allows processing 2 videos per step, helps with memory efficiency
  - *From: flo1331*

- **Dataset size for style LoRA**: At least 300 images and 80+ videos
  - Sufficient for high model to work at epoch 1
  - *From: crinklypaper*

- **LoRA rank**: 16-20 for characters, 32 maximum
  - WAN works well with lower ranks, higher ranks take much longer to train
  - *From: flo1331*

- **Learning rate**: 2e-5
  - Good starting point that avoids overfitting
  - *From: multiple users*

- **Shift parameter**: 8
  - Reduces blur and distortion, especially with dmp++_sde scheduler
  - *From: crinklypaper*

- **Timestep range for WAN 2.2**: min_t = 0, max_t = 0.875
  - Standard range for training low model on WAN 2.2
  - *From: crinklypaper*

- **Training steps for WAN 2.2**: 200-400 steps
  - Good results achieved in this range, easier to overtrain than 2.1
  - *From: flo1331*

- **Training repeats**: 10
  - Used in successful character LoRA training
  - *From: el marzocco*

- **Shift parameter**: 8
  - Works well for style LoRAs, avoids distortion
  - *From: crinklypaper*

- **Split ratio**: 11/9 steps
  - Better motion results than 10/10 split
  - *From: crinklypaper*

- **DPM++_SDE steps**: 6 steps with beta shift 1.5
  - Works with lightning and lightx2v LoRAs
  - *From: CJ*

- **Split timing**: 2/4
  - Used with lightning LoRAs and short step counts
  - *From: CJ*

- **Sigma switch point**: 0.875
  - Approximation point for high/low noise model handoff
  - *From: CJ*

- **I2V sigma switch point**: 0.9
  - Different timestep target for image-to-video
  - *From: MilesCorban*

- **CFG for lightning**: 1
  - Lower CFG needed when using lightning LoRAs
  - *From: screwfunk*

- **Training resolution for high noise**: 224x224
  - Sufficient for high noise training, saves VRAM
  - *From: MilesCorban*

- **Training resolution for images**: 512x512
  - Higher resolution possible for single-frame images
  - *From: MilesCorban*

- **Batch size for 48GB VRAM**: 24 for images, 1 for videos
  - Memory optimization
  - *From: MilesCorban*

- **timestep_boundary**: 875
  - For splitting high/low noise training in combined LoRA
  - *From: screwfunk*

- **timestep_sampling**: sigmoid for low noise, shift for high noise
  - Sigmoid better for character details, shift better for motion/style
  - *From: flo1331*

- **shift values**: 8 for high noise, 6 for low noise
  - Avoids distortions while maintaining good movement and camera work
  - *From: crinklypaper*

- **learning rate**: 2e-5 (DP default) or 1e-4 (AI-Toolkit default)
  - Both work well, currently being tested for optimal results
  - *From: MilesCorban*

- **training resolution**: 512 for images, 256 max for videos
  - Good balance of quality vs VRAM usage on 24GB cards
  - *From: MilesCorban*

- **resolutions**: [512]
  - Standard bucket size for character training
  - *From: Kenk*

- **preserve_distribution_shape**: disabled
  - Found to produce worse results than default
  - *From: JalenBrunson*

- **Rank for Wan 2.2**: 16 or 20 maximum
  - Helps reduce movement impact compared to rank 32 used for 2.1
  - *From: flo1331*

- **High noise timesteps**: min_t = 0.875, max_t = 1
  - Standard for high noise model training
  - *From: crinklypaper*

- **Low noise timesteps**: min_t = 0, max_t = 0.875
  - Standard for low noise model training
  - *From: crinklypaper*

- **Learning rate for high/low training**: 2e-5
  - Standard learning rate being used successfully
  - *From: crinklypaper*

- **Minimum frames for effective training**: 27-33 frames
  - Better results than lowering resolution when VRAM constrained
  - *From: flo1331*

- **Wan 2.2 model configuration**: dtype = 'bfloat16', transformer_dtype = 'float8', timestep_sample_method = 'logit_normal', min_t = 0.875, max_t = 1
  - Working configuration for Wan 2.2 T2V training
  - *From: crinklypaper*

- **Video resolution for training**: 512 or lower, with 256 for memory-constrained setups
  - Videos mainly teach motion and don't need high resolution
  - *From: crinklypaper*

- **Frame buckets**: [48, 65, 81] without 121
  - 121 frames is too much for most setups and causes memory issues
  - *From: MilesCorban, crinklypaper*

- **Wan 2.2 5B generation**: CFG6, Shift 8, 30-50 steps, dpm++_sde scheduler
  - Best results observed for 5B model
  - *From: crinklypaper*

- **T2V timestep boundaries**: min_t = 0.875, max_t = 1.0 for T2V; min_t = 0.9 for I2V
  - Configured inference boundary timesteps
  - *From: crinklypaper*

- **Character training epochs**: High: 400-800 steps, Low: 800-3000 steps
  - High overtrains fast, low takes longer but handles fidelity
  - *From: flo1331*

- **LoRA+ ratio**: 4
  - Recommended value is 4 instead of standard 16 for better results
  - *From: flo1331*

- **gradient_accumulation_steps**: 4
  - Converges faster by adjusting optimizer after batches instead of individual samples
  - *From: flo1331*

- **Training steps for character LoRA**: 400-800 steps
  - Good results achieved in this range with proper config, can work earlier but 600 steps recommended
  - *From: flo1331*

- **timestep_boundary**: 875
  - For combined high/low training, splits high model training at timestep 875
  - *From: screwfunk*

- **Target frames for dataset**: 14-20
  - Optimal number for 33 frame video training
  - *From: flo1331*

- **discrete_flow_shift**: T2V=12, I2V=5
  - Correct flow shift values for different training types according to Kohya documentation
  - *From: Myrrah's kate*

- **High noise timesteps**: min_t = 0.875, max_t = 1
  - Correct timestep range for high noise model training
  - *From: crinklypaper*

- **Low noise timesteps**: min_t = 0, max_t = 0.875
  - Correct timestep range for low noise model training
  - *From: crinklypaper*

- **Learning rate for large datasets**: 2e-5
  - Default works well even for ~150 videos + 450 images dataset
  - *From: crinklypaper*

- **Discrete flow shift**: High: shift 8, Low: shift 6
  - Results in less motion distortion
  - *From: crinklypaper*

- **LoRA strength for overtrained models**: Low noise: 0.5-0.6
  - Fixes hand and face distortion issues
  - *From: Kierkegaard*

- **Video training specs**: 640x352x17 frames, batch size 1
  - Achievable on 12GB VRAM with ~26.20s/it speed
  - *From: CDS*

- **High/Low training ratio**: High steps = 1/2 Low steps
  - Rule of thumb for character training - high contributes motion, low contributes detail
  - *From: PineAmbassador*

- **timestep_sample_method**: uniform
  - Logit_normal favors middle timesteps which conflicts with High model's 0.85-1.0 range
  - *From: ingi // SYSTMS*

- **High model training epochs**: 15-25 epochs
  - Sufficient for motion and basic style capture
  - *From: Thom293, ingi // SYSTMS*

- **Low model training epochs**: 25-65 epochs
  - Needs more training for style and detail refinement
  - *From: Thom293, ingi // SYSTMS*

- **Character LoRA optimal epoch range**: 15-20 epochs
  - Pick epoch with lowest dip on tensorboard graph in this range
  - *From: el marzocco*

- **Learning rate**: 3e-4 (current) vs 2e-5 (recommended)
  - Lower learning rate with longer training for LoRAs that work at lower strengths
  - *From: flo1331*

- **Network dim/alpha**: 16/16 for characters, 32 for specific features, max 64 for motion
  - Higher ranks not needed for most use cases
  - *From: flo1331*

- **Gradient accumulation steps**: 4
  - Leads to better results by adjusting weights after multiple steps instead of after every image
  - *From: flo1331*

- **Discrete flow shift**: 1.0 for images, 5.0-12.0 for videos (testing needed)
  - Different values needed for different training types
  - *From: flo1331*

- **Resolution for training**: 640x360 for videos, higher res for images
  - Higher res not that important, can get good results on lower res
  - *From: flo1331*

- **Video FPS**: 16 fps
  - Standard for Wan training
  - *From: flo1331*

- **LoRA strength**: 1.0
  - 95% of the time, optimal strength. Speed LoRAs can make character LoRAs look worse
  - *From: Guey.KhalaMari*

- **Learning rate for character LoRAs**: 0.00002
  - 0.0003 commonly used rate can destroy training
  - *From: el marzocco*

- **Epochs for low noise training**: 15-20
  - Sweet spot for low noise, lower loses likeness, higher leads to poor motion and ugly people
  - *From: el marzocco*

- **Dataset repeats**: 10
  - Used in successful character LoRA training
  - *From: el marzocco*

- **High noise timesteps in AOS**: 1-0.85
  - Default range for high noise
  - *From: ArtOfficial*

- **Low noise timesteps in AOS**: 0.85-0
  - Default range for low noise
  - *From: ArtOfficial*

- **Image resolution for training**: 512x for images, 256x for videos
  - Good balance of quality and performance
  - *From: crinklypaper*

- **4-bit quantization**: Bit rate 4
  - For Accuracy Recovery Adapters
  - *From: JohnDopamine*

- **Learning rate for Wan 2.2**: High: 2e-5, Low: 5e-5
  - Recommended learning rates based on successful training results
  - *From: Thom293*

- **Rank for LoRA training**: Rank 32
  - Default setting that works well, rank 16 also fine for most cases
  - *From: crinklypaper*

- **Lightning LoRA steps**: 4 steps
  - 6 steps not good, only 4 steps works well with new lightning model
  - *From: WorldX*

- **Training resolution**: 512x, sometimes bump to 1024x
  - 512x for training with aspect ratio bucketing, can increase to 768x or 1024x if VRAM allows
  - *From: crinklypaper*

- **Block swap for 8GB VRAM**: 40 blocks
  - Recommended block swap setting for Musubi Tuner with 8GB VRAM and 64GB RAM
  - *From: xwsswww*

- **Learning rate for character/motion**: 5e-5 (0.00005)
  - Works for both character likeness and motion training
  - *From: Ryzen*

- **Training epochs for small dataset**: 165 epochs for 11 images (1800 steps total)
  - Aim for at least 1800 steps minimum
  - *From: Tachyon*

- **Video resolution**: 256x256 max
  - Higher resolutions cause VRAM issues and stalling
  - *From: Ryzen*

- **blocks_to_swap**: Lower than 35 for 8GB VRAM
  - 35 blocks is too high for 8GB VRAM, causes slowdown
  - *From: Tachyon*

- **Rank**: 32
  - Standard rank that works well, higher ranks are more intensive
  - *From: Tachyon*

- **Learning rate for Wan**: 2e-5 or 5e-5
  - Helps prevent overfitting as Wan trains too fast
  - *From: Ryzen*

- **Epochs for character training**: 70-120 epochs
  - Good range for convergence, can train longer for slight improvements
  - *From: flo1331*

- **Gas setting**: 4
  - Each step becomes 4 actual steps
  - *From: flo1331*

- **High model LoRA strength when testing**: 2-3.5
  - Apply to high at this strength with low at 1.0
  - *From: flo1331*

- **Character image resolution**: 1024x1024
  - Used for character LoRA training
  - *From: el marzocco*

- **Style LoRA resolution**: 1536x640
  - Approximately same megapixels as 1024x1024
  - *From: el marzocco*

- **Video timestep sampling**: shift
  - Good for motion capture in video data
  - *From: Ryzen*

- **Weight decay**: 0.1
  - Part of working training configuration
  - *From: Ryzen*

- **Learning rate**: 1e-4 maximum, 2e-5 if unstable
  - Higher rates can break training by going outside loss function
  - *From: Kiwv*

- **Batch size**: 2 minimum, ideally 10% of dataset
  - Improves training stability, can use gradient accumulation if VRAM limited
  - *From: Kiwv*

- **Caption dropout**: 0
  - Wan uses sentence-based prompts unlike SDXL tag-based
  - *From: Kiwv*

- **Gradient accumulation**: 2 or 4
  - Helps with low VRAM training, simulates larger batch size
  - *From: Tachyon*

- **Resolution for motion LoRAs**: 256x256
  - Sufficient for motion training, higher resolutions are overkill
  - *From: Kiwv*

- **Frame count**: 81 for complex motion, 41-61 for simple motion
  - More frames needed for complex movements
  - *From: Kiwv*

- **I2V LoRA training steps**: 400 steps
  - Sufficient for 52 5-second clips
  - *From: Kiwv*

- **Wan 2.2 inference settings**: 20 steps, cfg 2.5
  - Standard settings for 2.2 workflow
  - *From: Ryzen*

- **3090 training settings**: Gradient accumulation 2, batch size 1, train at 256, enable layer swapping
  - Optimized for 24GB VRAM limitations
  - *From: Kiwv*

- **Training speed on 3090**: 2k steps in 10 hours with block swapping
  - Achievable performance benchmark
  - *From: Kiwv*

- **5090 training speed**: 1 hour per 100 steps
  - Performance benchmark without block swapping
  - *From: Ryzen*

- **Learning rate**: 2e-5
  - More stable than 1e-4 and 5e-5, works reliably around 1500-2000 steps
  - *From: Ryzen*

- **Training steps for character LoRA**: 1500-2000 steps
  - Effective convergence point with 2e-5 learning rate
  - *From: Ryzen*

- **Batch size for 3090**: 1 batch size, 2 gradient accumulation
  - VRAM limitations
  - *From: Kiwv*

- **Caption dropout for multi-dataset**: 0.5
  - Required for trigger words to work in multi-dataset training
  - *From: Ryzen*

- **AI Toolkit test seed**: 42
  - All T2V samples generated by AI toolkit use seed 42 for consistency
  - *From: Kiwv*

- **CFG for 30 steps**: 4+
  - CFG 1-1.5 only meant for fast LoRAs
  - *From: Thom293*

- **Minimum dataset size for LoRAs**: 60 videos
  - Need this many to generalize properly, 20 videos insufficient
  - *From: Kiwv*

- **LoRA training steps**: 2000+ steps
  - Need this many for solid LoRA quality
  - *From: Kiwv*

- **Learning rate**: 5e-5
  - 2e-4 is much too high and causes issues
  - *From: Kiwv*

- **Video resolution**: 256x256, 33 frames minimum
  - Can go pretty low res depending on what you're training
  - *From: ingi // SYSTMS*

- **Video scaling**: 512x288 and 288x512 for landscape/portrait
  - Good balance for training
  - *From: ingi // SYSTMS*

- **Video length**: Standard Wan lengths + 1 frame (34, 50, 66, 82 frames)
  - Required for Diffusion Pipe
  - *From: ingi // SYSTMS*

- **Video frames for training**: 30-50 frames (~2 seconds at 16fps)
  - Can go longer but uses more resources
  - *From: crinklypaper*

- **Batch size**: Minimum 2
  - Batch size 1 is pretty much useless, need 2 minimum for generalization
  - *From: Kiwv*

- **Dataset size**: 50+ images minimum
  - Need enough data that model can't memorize dataset
  - *From: Kiwv*

- **VRAM usage**: 20GB for 512x resolution training
  - Allows training without OOM on 3090
  - *From: crinklypaper*

- **LoRA rank**: 32 for hand-captioned data, 64 for improved results
  - Higher rank provides better capture but uses more VRAM
  - *From: Kiwv*

- **Training steps for WAN 2.2 T2V**: 2500 steps with 18 images
  - Works for low-only training with ARA
  - *From: aipmaster*

- **Resolution for training**: 256x256
  - Sufficient quality with much faster training times
  - *From: oskarkeo*

- **Min/max noise for movement capture**: min_t = 0.8, max_t = 1
  - Speculation that mid-noise in high.toml helps with movement capture
  - *From: Kenk*

- **Speedrun baseline settings**: [256,256] on 25 images, batch 1, GAS 1, repeats 1, DIM/ALPHA 16/16, LR 0.0001, 35-40 epochs
  - Ensures functional LoRA as foundation
  - *From: artificial_fungi*

- **Standard training steps**: 1000-1500 steps for 10-20 videos, 500-1000 for 3-5 videos
  - Balanced training for different dataset sizes
  - *From: AshmoTV*

- **Learning rates by dataset size**: 1e-4 to 2e-4 for larger sets, 5e-5 to 8e-5 for smaller sets
  - Prevents over/underfitting based on data amount
  - *From: AshmoTV*

- **Rank recommendations**: Rank 32 is sufficient for most use cases
  - Higher ranks risk overfitting and slower training
  - *From: Kiwv*

- **Training resolution**: 512px for video, 768px or 1024px for fine details
  - Higher resolution captures finer details better
  - *From: AshmoTV*

- **Context window frames**: 81 frames * 9 segments = 729 frames
  - Generates 45 seconds in one generation
  - *From: avataraim*

- **LoRA training frames for resources**: 55 frames instead of 81
  - Faster training with lower VRAM usage
  - *From: crinklypaper*

- **Low model timestep range**: 0-1000 instead of 0-875
  - Covers gaps when using lightning LoRAs
  - *From: crinklypaper*

- **High model timestep range**: 875-1000
  - Standard high noise training range
  - *From: crinklypaper*

- **Learning rate**: 5e-05
  - Standard rate used with shift: 5
  - *From: avataraim*

- **Rank for LoRA training**: 32
  - Good balance of quality and efficiency
  - *From: crinklypaper*

- **Batch size 4, GAS 8**: Fits on 24GB VRAM
  - For training 2.2 5B lora
  - *From: crinklypaper*

- **Training resolution**: 256 for video, 512 for images
  - Good balance of quality and speed on 3090
  - *From: Ashtar*

- **Caption length**: Under 75 words
  - Keep captions concise
  - *From: Thom293*

- **Learning rate and epochs**: Main knobs for training
  - Primary parameters to control underfitting/overfitting
  - *From: spacepxl*

- **Training frames**: Up to 81 frames standard, 97 frames possible
  - 81 is built-in limit but higher tested by some users
  - *From: AshmoTV*

- **Training resolution and clip length**: 320p 1 second clips
  - For RTX 5090 with Wan 2.2 training
  - *From: Duckers McQuack*

- **Motion training parameters attempted**: 1e-4 learning rate, 80 reps, 40 epochs
  - Though this didn't work well for the user
  - *From: Duckers McQuack*

- **Training clips for motion**: Around 18 clips
  - Usually enough for motion training
  - *From: vuuw*


## Concepts Explained

- **Frame bucket mismatch**: When video frame count doesn't exactly match the specified bucket size, causing training failures
  - *From: DiXiao*

- **Two-stage training**: Training first on images for feature learning, then on videos for motion preservation
  - *From: Cseti*

- **Regularization data**: Generic images (man/woman) used to prevent overfitting and maintain model's general capabilities
  - *From: mamad8*

- **Alpha vs Rank in LoRA training**: Diffusion-pipe/DiffSynth default alpha=rank, musubi-tuner defaults alpha=1, significantly affecting training performance and required learning rates
  - *From: mamad8*

- **Block swapping**: CPU offloading technique to fit large models in limited VRAM, slower than quantization but avoids system memory bottlenecks
  - *From: spacepxl*

- **70/30 rule in LoRA training**: In LLM/multimodal training, typically want 70% target content, 30% non-target to prevent overfitting and maintain generalization. Similar to regularization images in dreambooth training
  - *From: fredbliss*

- **Alpha parameter in LoRA**: Alpha lessens the learning rate effect. Musubi may default alpha to equal rank, though documentation says 1 by default
  - *From: mamad8*

- **Repeat factor in dataset config**: Determines how many times each image is seen per epoch. Repeat=1 means 12 images randomized every 12 steps, repeat=2 means 24 steps before reordering. Mainly useful for balancing different datasets
  - *From: mamad8*

- **Frame bucketing**: System that handles different video lengths in training, spending more time on early frames
  - *From: DevouredBeef*

- **Alpha in LoRA training**: Parameter that affects learning rate - when alpha changes, learning rate should be adjusted by square root of the change to maintain same effective learning rate
  - *From: spacepxl*

- **Domain gap between images and videos**: There's a gap between training on images vs videos - they can transfer between each other but not perfectly
  - *From: spacepxl*

- **Causal VAE**: VAE where each frame depends on the last but not the next. First frame is special - gets 4x less compression because dimensions are same in latent space
  - *From: spacepxl*

- **Latent frame entanglement**: In each latent 'frame', the 4 pixel frames it represents are entangled and can't be split apart arbitrarily without training a model to interpret them
  - *From: spacepxl*

- **I2V slider LoRA technique**: Create videos with first frame as 'before' state and last 4 frames identical showing 'after' state to train transformation LoRAs
  - *From: mamad8*

- **Alpha parameter in LoRA**: Hyperparameter to control the power of LoRA weights, affects how alpha influences learning rate and weight influence on inference
  - *From: Alisson Pereira*

- **I2V conditioning**: I2V models are strongly conditioned on the first frame, making it difficult to learn character likeness since the model relies on the conditioning image
  - *From: mamad8*

- **video_clip_mode**: Setting that determines which frame is used as conditioning for I2V training, affects whether first frame or middle frame is selected
  - *From: mamad8*

- **Block swapping**: Feature that enables training larger models like 14B on local hardware by swapping model blocks
  - *From: JohnDopamine*

- **Frame buckets**: Different frame count configurations (33, 49, 65, etc.) used during training to handle varying video lengths
  - *From: Benjaminimal*

- **CFG distillation**: Process of teaching model to produce same result in half the activations by learning to focus on wanted parts and forget unwanted parts
  - *From: Benjaminimal*

- **Token budget calculation**: width/16 * height/16 * (1 + (frames - 1) / 4) = tokens. Accounts for VAE spatial compression and patch embedding
  - *From: spacepxl*

- **Style training methodology**: Caption as if style doesn't exist so trigger word absorbs visual characteristics not described in text
  - *From: spacepxl*

- **Training loss interpretation**: High loss (0.2+) = needs more training, Mid loss (0.05-0.1) = good learning, Very low loss (<0.02) = possible overfitting
  - *From: VRGameDevGirl84(RTX 5090)*

- **Image conditioning dominance**: In I2V models, encoded image conditioning latent is much stronger than CLIP vision, affecting training behavior
  - *From: Kijai*

- **Evaluation loss vs training loss**: Evaluation loss is calculated on separate validation data and is often a better indicator of model performance than training loss
  - *From: Payuyi*

- **Local minima in high dimensions**: In high-dimensional spaces used by neural networks, true local minima are basically impossible - there will always be gradients in some dimensions
  - *From: spacepxl*

- **Alpha parameter in LoRA**: Alpha affects the effective learning rate by a square root relationship - higher alpha requires lower learning rate for equivalent training
  - *From: spacepxl*

- **Control LoRA**: LoRA trained to respond to control inputs like depth maps or segmentation masks for guided generation
  - *From: spacepxl*

- **Gradient accumulation steps**: Setting that affects steps per epoch calculation. Default 2-4 in HYV, helps with memory efficiency
  - *From: Cseti*

- **Single beginning frame selection**: Training setting that cuts videos off at 81 frames, useful for future-proofing datasets with longer videos
  - *From: ArtOfficial*

- **Evaluation datasets**: Subset of training data (10%) used to evaluate actual training progress, more meaningful than training loss curves
  - *From: ArtOfficial*

- **Repeats in training**: For single concept datasets, repeats are just epochs in disguise. Only useful when balancing multiple concepts with different sample counts
  - *From: spacepxl*

- **Module-specific training**: Training only specific transformer modules (like self_attn, cross_attn) rather than full blocks to create more focused LoRAs
  - *From: Amirsun(Papi)*

- **Size buckets**: Configuration that allows mixing images (frame_count=1) and videos (frame_count>1) at different resolutions in same training run
  - *From: Kytra*

- **Evaluation dataset**: Separate dataset used to monitor validation loss and detect overfitting/underfitting without affecting training weights
  - *From: Alisson Pereira*

- **Alpha parameter in training**: Alpha makes a big difference with learning rate - Musubi uses alpha 1 by default, while most other trainers match rank
  - *From: JohnDopamine*

- **Video frame handling in trainers**: Trainer takes first frame as still and rest as video frames, so need one extra frame more than bucket setting
  - *From: ingi // SYSTMS*

- **Local minimum in training**: When loss stops decreasing, you may be caught in a local minimum - increasing LR or modifying dataset can help
  - *From: Amirsun(Papi)*

- **Effective batch size calculation**: batch_size = micro_batch_per_gpu * gradient_accumulation_steps - this affects which buckets get dropped during training
  - *From: Alisson Pereira*

- **Frame count requirements**: Videos need frame counts that are multiples of 16 +1. The first frame of each video clip is used as the conditioning image, and the model is trained to predict the rest of the video.
  - *From: Alisson Pereira*

- **Video clip modes**: single_beginning vs single_middle affects which part of video is used for training - important for movement LoRAs to capture the right frames
  - *From: Thom293*

- **AR bucket functionality**: enable_ar_bucket will calculate aspect ratio buckets by interpolating between min_ar and max_ar instead of specifying each bucket manually
  - *From: Alisson Pereira*

- **Gradient accumulation**: Accumulates N gradients before backpropagation, works like batch size but less expensive, helps stabilize training
  - *From: Alisson Pereira*

- **Block swap**: Optimization technique that allows higher resolution/frame training without significantly impacting speed
  - *From: Piblarg*

- **wan_cache_latents vs HV caching**: WAN requires specific caching commands, can't use HunyuanVideo caching commands
  - *From: Benjimon*

- **Alpha parameter in LoRA training**: Dim gets divided by alpha. If alpha=dim, no dampening (full strength, might overfit). If alpha=1 with dim=32, lots of dampening (more flexible, needs higher LR)
  - *From: Persoon*

- **Frame buckets**: System that sorts videos into different frame length categories. Videos go into highest bucket they meet or exceed
  - *From: Thom293*

- **Block swap**: Memory optimization technique that swaps model blocks to/from system RAM, enables larger model training on limited VRAM
  - *From: Piblarg*

- **Frame buckets**: Array that defines temporal buckets for training, must match the number of spatial resolution buckets defined
  - *From: crinklypaper*

- **Steps vs Epochs**: Epochs are relative - just how many times it goes through all training data. Steps are more important - one attempt of model to recreate dataset
  - *From: crinklypaper*

- **Loss smoothing in graphs**: Smoothing is just a graph tool for showing smoothed values, doesn't affect training. Better to select epochs at lowest actual loss values
  - *From: MatiaHeron*

- **Block swapping**: Memory optimization technique that allows training larger models/datasets by swapping blocks between VRAM and system RAM
  - *From: Piblarg*

- **Alpha vs Dim in optimizers**: Musubi uses alpha 1 vs diffusion pipe uses alpha = dim by default
  - *From: Piblarg*

- **Alpha parameter in LoRA training**: Scales the learning rate during training and inference, allows adjusting batch size without changing LR by adjusting alpha instead
  - *From: hablaba*

- **Multiple-overlapping training**: Feature in diffusion-pipe that creates multiple overlapping segments from longer video clips, e.g. frames 1-81 and 69-150 from 150-frame video
  - *From: MilesCorban*

- **Block swapping**: Memory optimization technique that swaps model blocks to/from disk to manage VRAM usage during training
  - *From: Piblarg*

- **Flow shift**: Higher flow shift allows more change to happen in earlier timesteps during training - useful for dynamic motion but may not significantly affect final output
  - *From: JohnDopamine*

- **Block swapping**: Technique to use system RAM to compensate for VRAM limitations, allows training larger models/higher resolutions
  - *From: Alisson Pereira*

- **Automagic optimizer tensorboard graphs**: 3D visualization showing distribution of weights/gradients/learning rates - X-axis is learning rate bins, Y-axis is value count, Z-axis is time/steps
  - *From: Alisson Pereira*

- **Block swapping**: Memory management technique to handle VRAM limitations during training
  - *From: Thom293*

- **LogC**: Flat camera source format that Arri cameras record in - HDR format leaving flexibility for color grading, most digital cameras record some form of Log
  - *From: Simonj*

- **Sigmoid timestep sampling**: Trains more on middle timesteps, equivalent to logit_normal in diffusion-pipe. More aggressive than shift but captures character details really well
  - *From: hablaba*

- **Shift values for timestep training**: Shift 1 similar to sigmoid, shift 7 or 3 for composition, values adjust focus to earlier/middle/later timesteps for composition vs fine details
  - *From: hablaba*

- **Masked training**: Uses alpha layers or separate B&W mask images to control which parts of image receive training focus, can be binary or gradient-based
  - *From: hablaba*

- **Blockswap**: Setting that affects VRAM usage during training, higher values slow down training significantly
  - *From: Jas*

- **Bucketing**: Feature that handles mixed resolutions in training datasets
  - *From: Guey.KhalaMari*

- **Network size**: Parameter that affects VRAM usage, should be tweaked differently for style vs character LoRAs
  - *From: Guey.KhalaMari*

- **High noise vs low noise training**: High noise learns big changes like shapes and styles affecting entire image. Low noise learns small details. High noise more important for style training, low noise for detail refinement
  - *From: Alisson Pereira*

- **Repeats vs Epochs difference**: Only matters with high batch sizes. With batch size 1, 10 images × 2 repeats × 5 epochs = 10 images × 1 repeat × 10 epochs. But repeats can cause same image in consecutive steps
  - *From: mamad8*

- **Multiple character training averaging**: Training LORA with multiple characters averages their faces together, doesn't work well for distinct characters
  - *From: Thom293*

- **lr_bump in automagic optimizer**: Controls adaptation speed - how quickly learning rate adjusts based on gradient direction consistency. Larger values = more aggressive, smaller = more conservative
  - *From: Alisson Pereira*

- **High vs Low noise model roles**: High model (0.875-1) handles heavy noise removal and large details, Low model (0-0.875) handles refinement and smaller details/textures
  - *From: Alisson Pereira*

- **Block swap**: Feature in diffusion-pipe that allows training with less VRAM by swapping model blocks, key advantage over other training tools
  - *From: Alisson Pereira*

- **High vs Low noise models in Wan 2.2 MoE**: High noise model (0.875-1.0 timesteps) handles motion and general shapes, Low noise model (0-0.875 timesteps) handles details and character features
  - *From: Alisson Pereira*

- **Regularization images**: Images of the same class (man/woman) as your character but not your specific character, prevents overfitting to always generate your character
  - *From: mamad8*

- **Automagic optimizer**: Optimizer that adjusts learning rate individually per gradient, more adaptive than standard optimizers
  - *From: Alisson Pereira*

- **Block swap**: Feature that transfers model blocks between CPU/RAM and GPU to manage memory, allows multitasking during training
  - *From: 2kpr*

- **High vs Low noise model roles**: High noise model handles composition and motion, low noise model handles details and quality
  - *From: mamad8*

- **lr_bump**: Learning rate bump parameter that can dramatically speed up convergence
  - *From: MilesCorban*

- **Automagic learning rate**: Uses thousands of individual learning rates, adjusts each gradient's learning rate separately using lr_bump for increments
  - *From: Alisson Pereira*

- **fp8_scaled format**: Bespoke format with same weights as regular fp8 but at different scales plus runtime scaling factors, won't work for training
  - *From: mrassets*

- **High vs Low noise model split**: High noise (0.857-1.0) handles conditioning and prompts, Low noise (0-0.857) handles fine details
  - *From: Alisson Pereira*

- **Concept bleeding effect**: LoRA limitation where trained concepts affect unrelated parts of the image, reason Regional Prompter was invented
  - *From: TekeshiX*

- **Blockswapping**: Method to train at higher resolutions on limited VRAM by swapping model blocks in/out of memory
  - *From: multiple users*

- **Multiple overlapping vs single beginning**: Multiple overlapping creates 2+ clips from longer videos, using more VRAM. Single beginning just takes first frames
  - *From: MilesCorban*

- **UMT5 token survival**: Custom trigger words must survive UMT5 tokenizer processing or become garbage, need to use vocabulary words
  - *From: mrassets*

- **Flow shift parameters**: Controls training behavior: 1.0 = rough sketching, 3.0 = sketching and details (low noise), 7.0 = composition and movement (high noise)
  - *From: uff*

- **High vs Low noise model roles**: High noise handles general shapes and movement, low noise handles all the details
  - *From: crinklypaper*

- **Timestep ranges**: High noise: 0.875-1.0, Low noise: 0-0.875, determines which part of diffusion process each expert handles
  - *From: Kytra, Alisson Pereira*

- **High vs Low noise model roles**: High noise handles motion and general structure, Low noise handles details and fine features. Can test high alone but need both for full quality
  - *From: el marzocco, MatiaHeron*

- **Automagic optimizer**: Optimizer that dynamically adjusts learning rate over time and is designed to avoid overfitting on specific dataset aspects
  - *From: MatiaHeron*

- **single_beginning vs multiple_overlapping**: single_beginning samples from start of clip, multiple_overlapping uses more VRAM but captures more temporal context
  - *From: Kenk*

- **High vs Low noise model training**: WAN 2.2 requires training separate LoRAs for high noise (handles shapes/dimensions) and low noise (handles details/clarity) models using different scripts but same dataset
  - *From: screwfunk*

- **Steps vs Epochs for training comparison**: Steps are more reliable than epochs for comparing training progress since epochs vary based on dataset size, batch size, and other configs
  - *From: screwfunk*

- **Motion blur overfitting**: LoRAs can overfit on motion blur effects in the training dataset, causing transparency or blur when characters move
  - *From: Persoon*

- **Dual-mode training**: Training both high and low noise models simultaneously with Musubi, producing single LoRA that works on both
  - *From: artificial_fungi*

- **MoE sampler**: Mixture of Experts sampler that switches between high/low models based on objective metrics like SNR
  - *From: artificial_fungi*

- **logsnr sampling**: Method used by Musubi to switch between high and low noise experts during dual training
  - *From: artificial_fungi*

- **Dual LoRA training**: Training method that creates LoRA adapters for both high and low noise models simultaneously, can output single or dual LoRA files
  - *From: artificial_fungi*

- **Contextual LoRAs**: LoRAs that can take a subject/object and put it in new context without needing anything else, similar to stand-in LoRA or Phantom/VACE but for I2V
  - *From: flo1331*

- **Timestep range 0 to 1**: Training low noise model across full timestep range instead of just 0 to 0.875, allows single model to work in both high and low contexts
  - *From: Alisson Pereira*

- **--preserve_distribution_shape**: Training parameter that constrains timestep sampling using rejection sampling to preserve original distribution shape instead of scaling
  - *From: JalenBrunson*

- **0.875 timestep threshold**: Marks the split between composition/movement focused processing (1 to 0.875) and detail/quality focused processing in high/low noise model workflow
  - *From: CJ*

- **Character concept vs character consistency**: K3NK trains ethnicity/general concepts rather than specific character consistency, using generated faces rather than consistent character identity
  - *From: Alisson Pereira, GOD_IS_A_LIE*

- **Learning Rate**: Higher learning rate means faster, more aggressive parameter adjustments with risk of overshooting. Lower LR means slower, more conservative adjustments. 2e-4 is bigger than 2e-5.
  - *From: flo1331*

- **WAN 2.2 High vs Low models**: High model creates base composition and motion but fuzzy. Low model takes that base and fills in all the details and clarity.
  - *From: screwfunk*

- **Musubi dual training**: Single training process that creates one LoRA file that works on both high and low models by switching at timestep boundary
  - *From: screwfunk*

- **Dual training**: Training both high and low noise LoRAs simultaneously, producing 2 separate output files
  - *From: Ryzen*

- **High vs Low noise models**: High noise handles motion, Low noise handles fine details and character likeness
  - *From: flo1331*

- **Unload TE**: Unloads text encoder/captions from GPU memory
  - *From: Ryzen*

- **Cache text embeddings**: Loads caption data to disk storage instead of keeping in GPU memory
  - *From: Ryzen*

- **Gradient Accumulation Steps**: GAS=1 updates weights after each batch, higher values accumulate gradients across multiple batches before updating. Higher values simulate larger batch sizes without more GPU memory
  - *From: screwfunk*

- **Flow shift**: Parameter that can be adjusted differently for high vs low noise training, affects training dynamics
  - *From: flo1331*

- **LoRA Plus**: Training technique that helps massively with results, considered a 'godsend' for training quality
  - *From: flo1331*

- **LoRAplus**: Musubi option that helps LoRAs converge faster, used at value 4
  - *From: flo1331*

- **Caption Dropout Rate**: Parameter that affects how captions are used during training (exact function not explained)
  - *From: Ryzen*

- **logsnr sampler**: Sampling method in Musubi specifically suited for style training
  - *From: flo1331*

- **Sigma scheduling**: Signal to noise ratio that determines when to switch between high and low noise models, commonly at 0.875 timestep
  - *From: CJ*

- **MoE (Mixture of Experts)**: Architecture in Wan 2.2 with High/Low noise expert split
  - *From: context*

- **Timestep boundary**: Point at which training switches between high and low noise, set to 875 in training configs
  - *From: MilesCorban*

- **Frame extraction chunking**: Method for extracting frames from videos during training, experimental feature
  - *From: MilesCorban*

- **logsnr timestep sampling**: Style-friendly sampler that's counterproductive for character LoRAs since it trains opposite of what's wanted for characters
  - *From: flo1331*

- **High vs Low noise model roles**: High noise sets stage/composition/motion and kicks things off, low noise fills in details. Like building house foundation vs finishing work
  - *From: screwfunk*

- **Image sequences for training**: Can feed image sequences into dataset instead of compressed videos, but requires rigorous quality control
  - *From: Guey.KhalaMari*

- **High vs Low noise model training**: Wan 2.2 requires training two separate LoRAs - high noise (motion/shape) and low noise (details)
  - *From: various*

- **TREAD**: Training technique that provides 35% VRAM reduction and faster convergence for Wan 2.2
  - *From: Ada*

- **High vs Low noise models in Wan 2.2**: High noise gets motion and general shape, low noise handles all the details. High can be overtrained easily affecting likeness
  - *From: crinklypaper*

- **Timestep sample method**: logit_normal method for sampling timesteps during training
  - *From: crinklypaper*

- **Frame buckets**: Different frame counts that videos are organized into during training, like [48, 65, 81, 121]
  - *From: crinklypaper*

- **Transformer_path vs ckpt_path**: For Wan 2.2 A14B, ckpt_path points to main checkpoint folder, transformer_path points to subfolder (high_noise_model or low_noise_model)
  - *From: crinklypaper*

- **I2V training concept**: I2V training teaches the model 'change' - what happens when going from point A to point B using video input as reference. Cannot train images on I2V model since images can't teach motion
  - *From: flo1331*

- **LoRA+**: Training technique that influences the B matrices of LoRA, speeds up convergence and improves results
  - *From: flo1331*

- **Gradient Accumulation Steps (GAS)**: Makes optimizer adjust after processing multiple samples instead of individual ones, leading to faster convergence
  - *From: flo1331*

- **Character LoRA bleeding**: When a character LoRA affects all people in generated content, not just the intended character. Can be caused by training only on single person without regularization data
  - *From: samurzl*

- **WAN 2.2 loss patterns**: High noise model shows smooth C-shaped loss curve, low noise model shows jagged staircase pattern. Focus on trend rather than absolute numbers
  - *From: crinklypaper*

- **Captioning logic for LoRAs**: Don't describe what you want permanent (gets baked in), do describe changeable elements. Caption background and unrelated elements you want to remain flexible
  - *From: mdkb*

- **High/Low noise expert split in Wan 2.2**: High model focuses on motion and general shapes/layout in pure noise stage. Low model handles style and detail refinement. High produces noise that Low model prefers.
  - *From: ingi // SYSTMS*

- **Timestep ranges and their effects**: Higher timesteps (lower blocks) handle general motion and shapes but mostly noise. Lower timesteps (high blocks) are more detail-oriented for generation.
  - *From: ingi // SYSTMS*

- **Gradient Accumulation Steps (GAS)**: Accumulates gradients over multiple steps before updating weights, leading to better results but slower training
  - *From: flo1331*

- **Block swapping**: Technique to use CPU RAM when GPU VRAM is insufficient, allowing training on lower VRAM cards
  - *From: flo1331*

- **Accuracy Recovery Adapters**: Novel method by Ostris allowing 4-bit training without quality loss, works alongside trainer during training
  - *From: JohnDopamine*

- **Timestep ranges for MoE training**: High model trains on 1-0.875 range, low model on 0.875-0 range (normalized), but low can train on full range 1-0
  - *From: Alisson Pereira*

- **Block swapping**: Can only swap the checkpoint (~16gb after fp8 quantization), active training still needs VRAM
  - *From: ArtOfficial*

- **High vs Low noise models in Wan 2.2**: High model responsible for randomness/creativity and motion, Low model for refinement and detail
  - *From: Tonon*

- **Dataset repeats impact**: Has large impact on output quality, affects total training steps calculation
  - *From: el marzocco*

- **WSL2**: Windows Subsystem for Linux 2
  - *From: LionsEagles*

- **Block swap**: Memory optimization technique that swaps model blocks between VRAM and RAM to enable training larger models on lower VRAM GPUs
  - *From: xwsswww*

- **Aspect ratio bucketing**: Training technique that groups images of different resolutions into buckets, allowing training on mixed resolutions
  - *From: JohnDopamine*

- **Caption dropout rate**: Training parameter that randomly drops captions during training, potentially useful for style LoRAs
  - *From: Muon*

- **Timestep sampling types**: Sigmoid focuses on character likeness, Shift focuses on video movement/motion
  - *From: Ryzen*

- **Frame buckets**: More frames create more frame buckets, and higher buckets use more resources causing OOM
  - *From: crinklypaper*

- **Network weights parameter**: Used to continue training from a previous LoRA checkpoint
  - *From: Tachyon*

- **Overtraining symptoms**: Loss stops going down for 10-20 epochs or starts going up, causes loss of flexibility, bad prompt following, and fucked eyes
  - *From: flo1331*

- **Loss convergence target**: Good results usually when loss goes down by 0.5, typically starts 0.9-1.3 and good at 0.75-0.55
  - *From: flo1331*

- **Triggerword side effects**: Can degrade text capabilities as model thinks triggerword is written text in training data
  - *From: flo1331*

- **High/Low model roles in 2.2**: High handles motion, camera, basic shapes; Low handles details like faces
  - *From: crinklypaper*

- **Steps vs Epochs**: Step is single batch computation, epochs depend on dataset size and batch size. 3000 steps can be different epoch counts
  - *From: Kiwv*

- **Effective batch size**: Real batch size multiplied by gradient accumulation steps, allows larger effective batches on limited VRAM
  - *From: Kiwv*

- **High vs Low noise expert roles in 2.2**: High handles shape, height, build, facial features, hair. Low handles details and corrections
  - *From: flo1331*

- **Learning rate function**: Controls how far you move along derivative line when minimizing loss function, too high goes outside function bounds
  - *From: Kiwv*

- **I2V vs T2V captioning**: I2V needs context for motion since first frame is provided. T2V needs full scene description. For I2V, human should be able to take image and create video from caption
  - *From: Kiwv*

- **Block swapping**: Technique to manage VRAM by swapping model blocks during training, needed for GPUs with limited VRAM
  - *From: Kiwv*

- **RamTorch**: Swaps layers of models rather than blocks, much more VRAM efficient than block swapping
  - *From: Kiwv*

- **Effective batch size**: Batch size multiplied by gradient accumulation - determines how much of dataset model sees per optimization step
  - *From: Kiwv*

- **Gradient accumulation**: Combines loss gradients over multiple steps, mathematically equivalent to larger batch size but uses same VRAM
  - *From: Kiwv*

- **Loss in LoRA training**: Difference between model's generated video and target video - training minimizes this difference
  - *From: Kiwv*

- **Trigger words in LoRA training**: Optional words that activate LoRA - can train without them using good captioning, or with them for more control
  - *From: Kiwv*

- **Dataset generalization**: More videos in dataset leads to better generalization, but training time stays same due to batch processing
  - *From: Kiwv*

- **Batch size effect**: Batch size 1 pushes model towards individual images each step. Batch size 2+ pushes towards common denominator in group. Models like Chroma trained with batch size 8192
  - *From: Kiwv*

- **True batch size**: batch size * gradient accumulation. Can set batch size to 1 and grad accumulate to 2 for same effect
  - *From: Kiwv*

- **Caption approach**: Caption what you don't want it to learn - describe everything except the aspect you want the trigger word to capture
  - *From: ingi // SYSTMS*

- **ARA (Advanced Rank Adaptation)**: Training technique used with WAN 2.2 T2V for improved results
  - *From: aipmaster*

- **Abliterated models**: Uncensored versions of models that need guidance to properly describe NSFW content
  - *From: Stef*

- **Layer offloading**: Technique to manage VRAM by swapping model layers, trades speed for memory efficiency
  - *From: oskarkeo*

- **Model swapping in dual training**: Training alternates between high and low noise models each step, requiring VRAM to hold both models
  - *From: oskarkeo*

- **Overfitting in LoRA training**: Model memorizes dataset instead of generalizing, fails on inputs outside training data
  - *From: Kiwv*

- **Regularization images**: Additional images (like 'a man'/'a woman') used to prevent LoRA from affecting all people in scenes
  - *From: oskarkeo*

- **Spectral autoregression**: Diffusion viewed as getting benefits of autoregressive modeling without scan order downsides
  - *From: spacepxl*

- **Living LoRAs**: LoRAs that are continuously updated by adding/removing dataset folders during training for iterative refinement
  - *From: Thom293*

- **Context windows**: Feature allowing multiple prompts separated by | to generate smooth transitions between different scenes
  - *From: avataraim*

- **High/Low model interaction**: High model lays foundation for style/composition, low model adds details and is dependent on high model training
  - *From: crinklypaper*

- **Validation loss**: Clean monitoring method that gives U curves like classical ML training, unlike noisy training loss
  - *From: spacepxl*

- **Dataset variety**: Not just number of data points but variety they represent - 1000 similar crops acts like 1 image vs 1000 different images
  - *From: spacepxl*

- **In-distribution vs out-of-distribution prompts**: Test prompts similar to training data vs different prompts to check generalization
  - *From: spacepxl*

- **Blend images/videos**: Content containing multiple concepts with multiple keywords to help model differentiate and tie concepts together
  - *From: Thom293*

- **QLora recipe**: Training approach used in NF4 quantization that maintains quality while reducing model size
  - *From: spacepxl*

- **Network dropout**: Training technique that can help with texture quality in LoRAs
  - *From: vuuw*


## Resources & Links

- **Diffusion-pipe WAN training guide** (repo)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: Kendo*

- **Arcane Jinx LoRA example** (model)
  - https://huggingface.co/Cseti/Wan-LoRA-Arcane-Jinx-v1
  - *From: Cseti*

- **DiffSynth I2V training PR** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/compare/main...qiwang1996:DiffSynth-Studio:main
  - *From: mamad8*

- **HunyClip dataset preparation tool** (tool)
  - https://github.com/Tr1dae/HunyClip
  - *From: Marco_vdm*

- **Musubi-tuner WAN branch** (repo)
  - https://github.com/kohya-ss/musubi-tuner/tree/wan2-1-inf
  - *From: 片ヨ亡亡丹片*

- **TagGUI for image captioning** (tool)
  - https://github.com/jhc13/taggui
  - *From: yi*

- **Florence-2 PromptGen** (model)
  - https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v2.0
  - *From: yi*

- **ToriiGate anime captioning** (model)
  - https://huggingface.co/Minthy/ToriiGate-v0.4-7B
  - *From: intervitens*

- **Huggingface diffusers branch for Wan** (repo)
  - https://github.com/huggingface/diffusers/pull/10943
  - *From: Arrow*

- **Ostris AI-Toolkit Wan configs** (config)
  - https://github.com/ostris/ai-toolkit/blob/main/config/examples/train_lora_wan21_14b_24gb.yaml
  - *From: happy.j*

- **Musubi-tuner Wan support** (repo)
  - https://github.com/kohya-ss/musubi-tuner
  - *From: zezo*

- **SVDQuant/Nunchaku speedup** (repo)
  - https://github.com/mit-han-lab/nunchaku
  - *From: Ada*

- **spacepxl Wan control LoRAs** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main
  - *From: spacepxl*

- **spacepxl Wan training code** (repo)
  - https://github.com/spacepxl/WanTraining
  - *From: spacepxl*

- **spacepxl LTX-Video VAE training** (repo)
  - https://github.com/spacepxl/LTX-Video
  - *From: spacepxl*

- **Video splitting script** (script)
  - https://discord.com/channels/1076117621407223829/1316871013384065126/1325599601113174017
  - *From: JohnDopamine*

- **Cakify LoRA settings on Civitai** (model)
  - https://civitai.com/models/1337473/cakify-cake-everything-wan-14b-i2v
  - *From: akatz*

- **Multi-aspect ratio training issue discussion** (repo)
  - https://github.com/kohya-ss/musubi-tuner/issues/75
  - *From: Juampab12*

- **Musubi tuner** (trainer)
  - https://github.com/kohya-ss/musubi-tuner
  - *From: Juampab12*

- **Multiple WAN trainers list** (trainers)
  - https://github.com/kohya-ss/musubi-tuner (Apache), https://github.com/a-r-r-o-w/finetrainers (Apache), https://github.com/Bria-AI/Zero-to-Wan (Apache), https://github.com/modelscope/DiffSynth-Studio (Apache), https://github.com/ostris/ai-toolkit (MIT), https://github.com/tdrussell/diffusion-pipe (MIT)
  - *From: Benjaminimal*

- **spacepxl's WAN training repo** (trainer)
  - https://github.com/spacepxl/WanTraining/
  - *From: spacepxl*

- **LoRA training guide with alpha explanation** (guide)
  - https://github.com/spacepxl/demystifying-sd-finetuning/?tab=readme-ov-file#lora
  - *From: spacepxl*

- **Flash attention wheels for Windows** (tool)
  - https://huggingface.co/lldacing/flash-attention-windows-wheel/tree/main
  - *From: HeadOfOliver*

- **First WAN I2V trained model** (model)
  - https://civitai.com/models/1264662
  - *From: Alisson Pereira*

- **Steamboat Willie LoRA** (model)
  - https://huggingface.co/benjamin-paine/wan-lora/resolve/main/steamboat-willie.bf16.safetensors
  - *From: Benjaminimal*

- **Causal Conv3D code** (repo)
  - https://github.com/Wan-Video/Wan2.1/blob/main/wan/modules/vae.py#L17
  - *From: spacepxl*

- **Video VAE inspiration paper** (paper)
  - https://arxiv.org/abs/2310.05737
  - *From: spacepxl*

- **Memory optimization commit** (repo)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: chancelor*

- **Trainer comparison matrix** (workflow)
  - https://discord.com/channels/1076117621407223829/1344309523187368046/1349578207585632390
  - *From: Benjaminimal*

- **spacepxl's SD finetuning guide** (repo)
  - https://github.com/spacepxl/demystifying-sd-finetuning/
  - *From: spacepxl*

- **Video cropping tool** (tool)
  - https://www.freeconvert.com/crop-video
  - *From: Juampab12*

- **Video dataset preprocessing scripts** (repo)
  - https://github.com/huggingface/video-dataset-scripts/tree/main
  - *From: Hashu*

- **Steamboat Willie LoRA** (model)
  - https://huggingface.co/benjamin-paine/wan-lora/resolve/main/steamboat-willie-14b.bf16.safetensors
  - *From: Benjaminimal*

- **Aging timelapse LoRA** (model)
  - https://civitai.com/models/1353985/aging-timelapse-wan21-i2v-lora?modelVersionId=1529405
  - *From: Alisson Pereira*

- **Runpod training tutorial** (tutorial)
  - https://www.youtube.com/watch?v=XYq89zuGGLA
  - *From: Alisson Pereira*

- **Civitai workflow for Wan** (workflow)
  - https://civitai.com/models/1309369?modelVersionId=1529049
  - *From: Alisson Pereira*

- **FFHQ dataset** (dataset)
  - https://github.com/NVlabs/ffhq-dataset
  - *From: BondoMan*

- **Zero-to-Wan captioning script** (script)
  - https://github.com/Bria-AI/Zero-to-Wan/blob/dev/data_prep/caption_video_dir.py
  - *From: Benjaminimal*

- **Diffusion-pipe commit with updated configs** (repo)
  - https://github.com/tdrussell/diffusion-pipe/commit/e33da3fbbd625c3af7c143df7c12c64a4c4db18d
  - *From: JohnDopamine*

- **Qwen2.5-VL Video Captioning script** (tool)
  - https://github.com/cseti007/Qwen2.5-VL-Video-Captioning
  - *From: Cseti*

- **Gemini video captioning script** (script)
  - *From: ArtOfficial*

- **Spiral Staircase LoRA** (lora)
  - https://civitai.com/models/1371822/kxsr-spiral-staircase-concept-wan-14b-t2v
  - *From: Kytra*

- **Replicate Wan LoRA trainer** (tool)
  - https://replicate.com/zsxkib/wan-lora-trainer/train
  - *From: pom*

- **Ostris Wan LoRA trainer on Replicate** (tool)
  - https://replicate.com/ostris/wan-lora-trainer/train
  - *From: BarleyFarmer*

- **Diffusion-pipe GitHub issue** (repo)
  - https://github.com/tdrussell/diffusion-pipe/issues/165
  - *From: Nathan Shipley*

- **Qwen2.5-VL simple captioning script** (script)
  - *From: chancelor*

- **VRGameDevGirl84's training process video** (tutorial)
  - https://youtu.be/OPQ46Z1nUZQ
  - *From: VRGameDevGirl84(RTX 5090)*

- **Updated diffusion-pipe UI** (tool)
  - https://github.com/alisson-anjos/diffusion-pipe-ui/tree/new-ui
  - *From: Alisson Pereira*

- **VACE paper** (research)
  - https://github.com/ali-vilab/VACE
  - *From: fredbliss*

- **VideoModelStudio with Wan support** (tool)
  - https://github.com/jbilcke-hf/VideoModelStudio
  - *From: LarpsAI*

- **Krea AI Wan training** (service)
  - https://www.krea.ai/account/compute-packs
  - *From: Nathan Shipley*

- **Fal Flux LoRA training** (service)
  - https://fal.ai/models/fal-ai/flux-lora-fast-training
  - *From: Nathan Shipley*

- **yt-dlp for video downloads** (tool)
  - https://github.com/yt-dlp/yt-dlp
  - *From: mamad8*

- **FluxFlow paper** (research)
  - https://haroldchen19.github.io/FluxFlow/
  - *From: mamad8*

- **Flux control LoRA training script** (code)
  - https://github.com/huggingface/diffusers/tree/main/examples/flux-control
  - *From: spacepxl*

- **Flux block pruning analysis** (research)
  - https://ostris.com/2024/09/07/skipping-flux-1-dev-blocks/
  - *From: spacepxl*

- **Flux Lite 8B pruned model** (model)
  - https://huggingface.co/Freepik/flux.1-lite-8B-alpha
  - *From: spacepxl*

- **Advanced Youtube Downloader** (tool)
  - https://github.com/adithya-s-sekhar/advanced-youtube-client-ayc
  - *From: JohnDopamine*

- **Qwen2.5-VL Video Captioning** (tool)
  - https://github.com/cseti007/Qwen2.5-VL-Video-Captioning
  - *From: burgstall*

- **Standalone AI Captioner GUI** (tool)
  - https://civitai.com/articles/12823/streamline-your-lora-training-with-the-standalone-ai-captioner-gui
  - *From: Amirsun(Papi)*

- **WSL Wan2.1 Training Setup Guide** (guide)
  - https://civitai.com/articles/12837/full-setup-guide-wan21-lora-training-on-wsl-with-diffusion-pipe
  - *From: Amirsun(Papi)*

- **Diffusion-pipe Gradio Configuration** (tool)
  - https://civitai.com/articles/12841
  - *From: H（4090）*

- **Turn to Ashes LoRA** (model)
  - https://civitai.com/models/1384085/turn-to-ashes?modelVersionId=1564022
  - *From: H（4090）*

- **Wan AI TimeLapse LoRA** (model)
  - https://civitai.com/models/1389992/time-lapse-wan21-t2v-14b-lora
  - *From: 852話 (hakoniwa)*

- **Everything Blossoms LoRA** (model)
  - https://civitai.com/models/1396847/everything-blossoms
  - *From: H（4090）*

- **DrawUndo LoRA** (model)
  - http://civitai.com/models/1397074/drawundo-wan21-i2v-720-lora?modelVersionId=1579140
  - *From: 852話 (hakoniwa)*

- **WanTraining by spacepxl** (repo)
  - https://github.com/spacepxl/WanTraining
  - *From: 852話 (hakoniwa)*

- **MeTube for video downloading** (tool)
  - https://github.com/alexta69/metube
  - *From: Semi*

- **Replicate WAN trainer** (training_service)
  - https://replicate.com/zsxkib/wan-lora-trainer/train
  - *From: pom*

- **Fal.ai WAN trainer** (training_service)
  - https://fal.ai/models/fal-ai/wan-trainer
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanVideo endframe workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_480p_I2V_endframe_example_01.json
  - *From: pom*

- **Fun Control training guide** (documentation)
  - https://github.com/aigc-apps/VideoX-Fun/blob/main/scripts/wan2.1_fun/README_TRAIN_LORA.md
  - *From: Alisson Pereira*

- **FFmpeg adjustment scripts** (tools)
  - https://github.com/alisson-anjos/useful-scripts
  - *From: Alisson Pereira*

- **PySceneDetect** (tool)
  - https://www.scenedetect.com/
  - *From: Alisson Pereira*

- **Amirsun's Studio Ghibli LoRA** (model)
  - https://civitai.com/models/1419443?modelVersionId=1607034
  - *From: Amirsun(Papi)*

- **Juampab12's Expression Changer LoRA** (model)
  - https://civitai.com/models/1421989
  - *From: Juampab12*

- **Fun LoRA conversion script** (tool)
  - https://github.com/maybleMyers/H1111/blob/main/funconvert_lora.py
  - *From: Benjimon*

- **Studio Ghibli Wan LoRA with detailed training guide** (model)
  - https://civitai.com/models/1404755/studio-ghibli-style-wan21-t2v-14b
  - *From: seruva19*

- **Demystifying SD Finetuning guide** (guide)
  - https://github.com/spacepxl/demystifying-sd-finetuning/
  - *From: Juampab12*

- **Wan 2.1 full finetuning script** (repo)
  - https://github.com/aigc-apps/VideoX-Fun/tree/main/scripts/wan2.1
  - *From: Benjimon*

- **JoyCaption Alpha Two GUI** (tool)
  - https://civitai.com/articles/7794/joycaption-alpha-two-gui-mod
  - *From: phant*

- **Pwnisher challenge datasets** (dataset)
  - https://huggingface.co/datasets/KXSR/pwnisher_challenges
  - *From: Kytra*

- **Gemma3 abliterated model for captioning** (model)
  - https://ollama.com/huihui_ai/gemma3-abliterated
  - *From: Alisson Pereira*

- **Useful video processing scripts** (repo)
  - https://github.com/alisson-anjos/useful-scripts
  - *From: Alisson Pereira*

- **Motion LoRA example with few clips** (model)
  - https://civitai.com/models/1331682?modelVersionId=1503530
  - *From: Benjimon*

- **Qwen2.5-VL-Video-Captioning** (repo)
  - https://github.com/cseti007/Qwen2.5-VL-Video-Captioning
  - *From: Cseti*

- **Studio Ghibli LoRA example** (model)
  - https://civitai.com/models/1404755?modelVersionId=1587891
  - *From: Alisson Pereira*

- **SingularUnity WAN2.1 MotionCraft LoRA** (model)
  - https://civitai.com/models/1403959/singularunity-wan21-motioncraft
  - *From: Amirsun(Papi)*

- **VidTrainPrep GUI tool** (tool)
  - https://github.com/lovisdotio/VidTrainPrep
  - *From: lovis.io*

- **Animated Logo LoRA** (model)
  - https://civitai.com/models/1468212?modelVersionId=1660567
  - *From: Alisson Pereira*

- **Higgsfield camera dataset** (dataset)
  - https://higgsfield.ai/
  - *From: NebSH*

- **FramePack** (tool)
  - https://github.com/lllyasviel/FramePack
  - *From: Ada*

- **FramePack demo page** (demo)
  - https://lllyasviel.github.io/frame_pack_gitpage/
  - *From: Ada*

- **Musubi Tuner WAN GUI** (gui)
  - https://github.com/Kvento/musubi-tuner-wan-gui
  - *From: realsammyt*

- **ComfyUI QwenVL for video captioning** (node)
  - https://github.com/alexcong/ComfyUI_QwenVL
  - *From: TK_999*

- **Qwen2.5-VL Video Captioning script** (tool)
  - https://github.com/cseti007/Qwen2.5-VL-Video-Captioning
  - *From: Cseti*

- **Studio Ghibli WAN training guide** (guide)
  - https://civitai.com/models/1404755/studio-ghibli-wan21-t2v-14b
  - *From: Piblarg*

- **Redline WAN training discussion** (guide)
  - https://civitai.com/models/1517145/redline-wan21-t2v-14b?modelVersionId=1716497
  - *From: Piblarg*

- **Prebuilt wheels list** (resource)
  - https://github.com/stars/realsammyt/lists/wheels
  - *From: realsammyt*

- **NVIDIA Describe Anything models** (models)
  - https://huggingface.co/collections/nvidia/describe-anything-680825bb8f5e41ff0785834c
  - *From: mamad8*

- **Eyecannndy motion dataset** (dataset)
  - https://eyecannndy.com/
  - *From: pom*

- **Diffusion Pipe RunPod tutorial** (tutorial)
  - https://learn2train.medium.com/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79
  - *From: TimHannan*

- **RunPod WAN LoRA training template** (workflow)
  - https://civitai.com/articles/12330/runpod-template-wan-lora-training-with-diffusion-pipe
  - *From: crinklypaper*

- **Musubi Tuner Simple GUI** (tool)
  - https://civitai.com/articles/12635/musubi-tuner-simple-gui
  - *From: ByArlooo*

- **MoviiGen trainer** (repo)
  - https://github.com/ZulutionAI/MoviiGen1.1
  - *From: JohnDopamine*

- **Kijai MoviiGen merged models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: JohnDopamine*

- **BIRME image resizer** (tool)
  - https://www.birme.net/?target_width=1024&target_height=1024
  - *From: JohnDopamine*

- **VideoX-Fun WAN training** (repo)
  - https://github.com/aigc-apps/VideoX-Fun/tree/main/scripts/wan2.1
  - *From: Benjimon*

- **WSL setup guide for Wan training** (tutorial)
  - https://civitai.com/articles/12837/full-setup-guide-wan21-lora-training-on-wsl-with-diffusion-pipe
  - *From: Thom293*

- **SkyCaptioner video captioning model** (model)
  - https://huggingface.co/Skywork/SkyCaptioner-V1
  - *From: Thom293*

- **Upscaler model database** (resource)
  - https://openmodeldb.info
  - *From: MatiaHeron*

- **Bowsette LoRA example** (model)
  - https://civitai.com/models/1615071/bowsette-lora-wan-21-14b-t2v-i2v?modelVersionId=1831542
  - *From: crinklypaper*

- **Boob size slider LoRA** (model)
  - https://civitai.com/models/1613190/wan-14b-boob-size-slider
  - *From: Piblarg*

- **Anime-oriented Wan merge model** (model)
  - https://civitai.com/models/1626197/aniwan2114bfp8e4m3fn
  - *From: 852話 (hakoniwa)*

- **DARE merge method** (repo)
  - https://github.com/yule-BUAA/MergeLM
  - *From: JohnDopamine*

- **LosslessCut** (tool)
  - https://github.com/mifi/lossless-cut
  - *From: MilesCorban*

- **Shutter Encoder** (tool)
  - https://www.shutterencoder.com/
  - *From: Jonathan*

- **ai-toolkit trainer** (tool)
  - https://discord.com/channels/1076117621407223829/1316871385909301459/1333867678082928792
  - *From: DeZoomer*

- **Video trimming script** (script)
  - https://discord.com/channels/1076117621407223829/1316871013384065126/1325599601113174017
  - *From: JohnDopamine*

- **ComfyUI-JoyCaption V1.1.0** (node)
  - *From: hicho*

- **DeZoomer ComfyUI Nodes** (node)
  - https://github.com/De-Zoomer/ComfyUI-DeZoomer-Nodes
  - *From: Thom293*

- **QwenVL ComfyUI Nodes** (node)
  - https://github.com/alexcong/ComfyUI_QwenVL
  - *From: TK_999*

- **Qwen2.5-VL Official Repo** (repo)
  - https://github.com/QwenLM/Qwen2.5-VL
  - *From: TK_999*

- **TagGUI for batch captioning** (tool)
  - https://github.com/jhc13/taggui
  - *From: scf*

- **Diffusion Pipe WSL Setup Tutorial** (tutorial)
  - https://civitai.com/articles/12837/full-setup-guide-wan21-lora-training-on-wsl-with-diffusion-pipe
  - *From: MatiaHeron*

- **Wan 14B Model** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-T2V-14B/tree/main
  - *From: Alisson Pereira*

- **Musubi Training Settings Discussion** (guide)
  - https://github.com/kohya-ss/musubi-tuner/discussions/182#discussioncomment-12655085
  - *From: JohnDopamine*

- **Ghibli LoRA Training Guide** (guide)
  - https://civitai.green/posts/14771927
  - *From: Piblarg*

- **FLF2V LoRA Example** (lora)
  - https://civitai.com/models/1598575/disguise-drop-wan21-14b-flf2v-720p
  - *From: seruva19*

- **Segment Anything Model** (tool)
  - https://segment-anything.com/
  - *From: Alisson Pereira*

- **LosslessCut for video splitting** (tool)
  - https://github.com/mifi/lossless-cut
  - *From: TK_999*

- **ContentV-8B Model** (model)
  - https://huggingface.co/ByteDance/ContentV-8B
  - *From: hicho*

- **Pazera Free MP4 Video Converter** (tool)
  - https://www.videohelp.com/software/Pazera-Free-MP4-Video-Converter
  - *From: JohnDopamine*

- **Shutter Encoder** (tool)
  - *From: Alisson Pereira*

- **ShotVL-7B** (model)
  - https://huggingface.co/Vchitect/ShotVL-7B
  - *From: yi*

- **DeZoomer ComfyUI Nodes** (repo)
  - https://github.com/De-Zoomer/ComfyUI-DeZoomer-Nodes
  - *From: DeZoomer*

- **Flash attention precompiled wheels** (repo)
  - https://huggingface.co/Kijai/PrecompiledWheels/tree/main
  - *From: Alisson Pereira*

- **Wan training guide** (workflow)
  - https://civitai.com/models/1517145/redline-wan21-t2v-14b
  - *From: notid*

- **BIRME image resizer** (tool)
  - https://www.birme.net/
  - *From: crinklypaper*

- **Art Official YouTube tutorials** (tutorial)
  - *From: mdkb*

- **Flash attention prebuilt wheel** (wheel)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.3.12/flash_attn-2.8.0+cu128torch2.7-cp311-cp311-linux_x86_64.whl
  - *From: Persoon*

- **Flash attention Windows wheel** (wheel)
  - https://huggingface.co/Panchovix/flash-attentionv2-blackwell2.0-nightly/blob/main/flash_attn-2.7.4.post1-cp312-cp312-win_amd64.whl
  - *From: Faust-SiN*

- **Qwen2.5-VL Video Captioning scripts** (repo)
  - https://github.com/cseti007/Qwen2.5-VL-Video-Captioning
  - *From: Cseti*

- **WAN training guide** (guide)
  - https://civitai.com/articles/11942/training-a-wan-or-hunyuan-lora-the-right-way
  - *From: mdkb*

- **VACE knowledge base** (knowledge base)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05
  - *From: mdkb*

- **AI-toolkit Discord server** (discord)
  - https://discord.gg/J4uj8MYD
  - *From: JohnDopamine*

- **Skyreels upscale/enhance workflow** (workflow)
  - https://civitai.com/models/1742500
  - *From: VRGameDevGirl84(RTX 5090)*

- **Flim.ai for movie scene datasets** (tool)
  - https://flim.ai/
  - *From: JohnDopamine*

- **ShotDeck for movie-based tag searching** (tool)
  - https://shotdeck.com
  - *From: JohnDopamine*

- **AllMovie database** (tool)
  - https://www.allmovie.com/
  - *From: samhodge*

- **TheMovieDB API** (tool)
  - https://developer.themoviedb.org/docs/getting-started
  - *From: samhodge*

- **High Speed Dynamic LoRA** (model)
  - https://civitai.com/models/1698719/high-speed-dynamic
  - *From: MaQue*

- **Diffusion Pipe Wan 2.2 documentation** (documentation)
  - https://github.com/tdrussell/diffusion-pipe/blob/main/docs/supported_models.md
  - *From: crinklypaper*

- **Wan 2.2 training guides on Civitai** (guide)
  - https://civitai.com/articles/14070/wan-21-video-lora-training-guide-based-on-414-official-stream-and-my-own-experience
  - *From: seruva19*

- **Motion training experience guide** (guide)
  - https://civitai.com/articles/16936/my-personally-training-experience-of-wanstarting-with-data
  - *From: seruva19*

- **Studio Ghibli style LORA guide** (model/guide)
  - https://civitai.com/models/1404755/studio-ghibli-style-wan21-t2v-14b
  - *From: pom*

- **fp16 Wan 2.2 checkpoints** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp16.safetensors
  - *From: seruva19*

- **Qwen VL nodes for ComfyUI** (nodes)
  - *From: Thom293*

- **Flash attention wheel for RTX 5090** (wheel)
  - https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.1/flash_attn-2.8.1+cu12torch2.7cxx11abiTRUE-cp311-cp311-linux_x86_64.whl
  - *From: mamad8*

- **Flash attention wheels collection** (wheel)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.3.12/flash_attn-2.8.0+cu128torch2.7-cp312-cp312-linux_x86_64.whl
  - *From: CJ*

- **Live Wallpaper Style LoRA** (model)
  - https://civitai.com/models/1264662/live-wallpaper-style?modelVersionId=2067386
  - *From: Alisson Pereira*

- **Musubi Tuner Wan2.2 branch** (repo)
  - https://github.com/kohya-ss/musubi-tuner/commits/feature-wan-2-2/
  - *From: JohnDopamine*

- **Pre-compiled flash attention for WSL** (wheel)
  - https://huggingface.co/orrzxz/flash-attention-linux-WSL-cu128-wheel
  - *From: Alisson Pereira*

- **Wan 2.2 fp16 model for training** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp16.safetensors
  - *From: MilesCorban*

- **Tensorboard command for monitoring training** (tool)
  - tensorboard --logdir=.
  - *From: Kenk*

- **TripleX captioning script** (tool)
  - https://github.com/NSFW-API/TripleX/tree/master
  - *From: Kenk*

- **Qwen2.5-VL Video Captioning** (repo)
  - https://github.com/cseti007/Qwen2.5-VL-Video-Captioning
  - *From: Cseti*

- **Na'vi LoRA example** (model)
  - https://civitai.com/models/1809771?modelVersionId=2048067
  - *From: Kenk*

- **WAN 2.2 T2V A14B model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B
  - *From: tarn59*

- **Diffusion-pipe training tutorial** (tutorial)
  - https://www.youtube.com/watch?v=9ATaQdin1sA
  - *From: orabazes*

- **Lightning LoRAs for WAN 2.2** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/3
  - *From: _Djent_*

- **Qinglong captions for video** (tool)
  - https://github.com/sdbds/qinglong-captions
  - *From: TekeshiX*

- **TagGUI for image tagging** (tool)
  - https://github.com/jhc13/taggui
  - *From: TekeshiX*

- **Diffusion-pipe UI** (tool)
  - https://github.com/alisson-anjos/diffusion-pipe-ui/tree/new-ui
  - *From: mrassets*

- **Musubi Trainer WAN 2.2 support** (news)
  - https://www.reddit.com/r/StableDiffusion/comments/1mh467h/musubitrainer_now_allows_for_proper_training_of/
  - *From: Juampab12*

- **BF16 converted I2V model** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Persoon*

- **Live wallpaper LoRA for 5B** (lora)
  - https://civitai.com/models/1264662?modelVersionId=2080103
  - *From: Alisson Pereira*

- **Diffusion-pipe repository** (repo)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: Kenk*

- **Musubi tuner for WAN 2.2** (tool)
  - https://github.com/kohya-ss/musubi-tuner
  - *From: avataraim*

- **Ext.to torrent site** (resource)
  - ext.to
  - *From: Kenk*

- **Differential output preservation discussion** (discussion)
  - https://github.com/tdrussell/diffusion-pipe/issues/332
  - *From: screwfunk*

- **Runpod template for Wan 2.2 training** (template)
  - https://console.runpod.io/explore/jn8k3c0b4t
  - *From: CJ*

- **Wan 14B RunPod template guide** (tutorial)
  - https://civitai.com/articles/11960/wan14b-in-1-click-with-workflows-included-runpod-template
  - *From: crinklypaper*

- **WAN/SDXL/Flux LoRA training template** (template)
  - https://civitai.com/articles/12330/wansdxlflux-all-in-one-lora-training-diffusion-pipe-with-auto-captioning
  - *From: crinklypaper*

- **MediaSyncer video testing tool** (tool)
  - https://whatdreamscost.github.io/MediaSyncer/
  - *From: JohnDopamine*

- **SageAttention acceleration library** (repo)
  - https://github.com/thu-ml/SageAttention
  - *From: TekeshiX*

- **Diffusion-pipe Wan 2.2 documentation** (documentation)
  - https://github.com/tdrussell/diffusion-pipe/blob/main/docs/supported_models.md#wan22
  - *From: Alisson Pereira*

- **First Wan 2.2 community LoRA** (model)
  - https://discord.com/channels/1076117621407223829/1402741644587175977
  - *From: Cseti*

- **Joy Caption for dataset preparation** (tool)
  - https://huggingface.co/spaces/fancyfeast/joy-caption-beta-one
  - *From: screwfunk*

- **Wan 2.2 full model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B
  - *From: MatiaHeron*

- **K3NK's Wan 2.2 ComfyUI workflow** (workflow)
  - https://civitai.com/models/1824027/wan-22-t2v-i2v-kijais-wrapper-workflow-k3nk
  - *From: Kenk*

- **Python frame counter script** (tool)
  - *From: MilesCorban*

- **Diffusion-Pipe RunPod template** (training template)
  - https://console.runpod.io/explore/jn8k3c0b4t
  - *From: screwfunk*

- **JoyCaption Beta One** (captioning tool)
  - https://huggingface.co/spaces/fancyfeast/joy-caption-beta-one
  - *From: screwfunk*

- **ComfyUI JoyCaption workflow for batch processing** (workflow)
  - *From: screwfunk*

- **PowerShell scripts for trigger word insertion** (script)
  - *From: screwfunk*

- **Musubi trainer settings for 2.9s iteration time** (training settings)
  - https://discord.com/channels/1076117621407223829/1344309523187368046/1377489799845253163
  - *From: seruva19*

- **CaptionFlow by bghira** (tool)
  - https://github.com/bghira/CaptionFlow
  - *From: Alisson Pereira*

- **Ostris Accuracy Recovery Adapters** (model)
  - https://huggingface.co/ostris/accuracy_recovery_adapters
  - *From: JohnDopamine*

- **Runpod template for Wan 2.2 training** (template)
  - https://console.runpod.io/explore/jn8k3c0b4t
  - *From: screwfunk*

- **Musubi Wan documentation** (documentation)
  - https://github.com/kohya-ss/musubi-tuner/blob/main/docs/wan.md
  - *From: JalenBrunson*

- **ComfyUI WanMoeKSampler** (node)
  - https://github.com/stduhpf/ComfyUI-WanMoeKSampler
  - *From: artificial_fungi*

- **Flash attention prebuilt wheels** (tool)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/
  - *From: Persoon*

- **Qwen2.5-omni captioning tool** (tool)
  - https://github.com/cseti007/qwen2.5-omni-captioning
  - *From: Cseti*

- **X-ray Alpha uncensored VLM** (model)
  - https://ollama.com/rosemarla/x-ray_alpha:latest
  - *From: Alisson Pereira*

- **JoyCaption Beta** (tool)
  - https://huggingface.co/spaces/fancyfeast/joy-caption-beta-one
  - *From: screwfunk*

- **Retro 90s Anime Style LoRA** (model)
  - https://civitai.com/models/1671285/retro-90s-anime-golden-boy-style-lora-wan-14b-t2v-i2v?modelVersionId=1891658
  - *From: crinklypaper*

- **RunPod WAN training tutorial** (tutorial)
  - https://civitai.com/articles/18081
  - *From: CJ*

- **StableAvatar** (repo)
  - https://github.com/Francis-Rings/StableAvatar
  - *From: NebSH*

- **AI-Toolkit WAN 2.2 branch** (repo)
  - https://github.com/ostris/ai-toolkit/tree/wan22_14b
  - *From: JohnDopamine*

- **WAN 2.2 LoRA training workflow guide** (tutorial)
  - https://civitai.com/articles/17740/my-wan22-lora-training-workflow-tldr
  - *From: flo1331*

- **K3NK's training examples** (training reference)
  - https://discord.com/channels/1076117621407223829/1344309523187368046/1403757590965649415
  - *From: Alisson Pereira*

- **Diffusion Pipe training tutorial** (tutorial)
  - https://civitai.com/articles/18081
  - *From: CJ*

- **K3NK's models on Civitai** (model collection)
  - https://civitai.com/user/K3NK/models
  - *From: Alisson Pereira*

- **JoyCaption for automated captioning** (tool)
  - https://huggingface.co/spaces/fancyfeast/joy-caption-beta-one
  - *From: screwfunk*

- **Wan 2.2 training scripts** (workflow)
  - *From: screwfunk*

- **ChatGPT captioning prompt for video training** (workflow)
  - *From: flo1331*

- **screwfunk's updated training scripts with save state** (workflow)
  - *From: screwfunk*

- **Civitai article on musubi setup** (guide)
  - *From: GOD_IS_A_LIE*

- **Wan 2.2 T2V/I2V Kijai's Wrapper Workflow** (workflow)
  - https://civitai.com/models/1824027/wan-22-t2v-i2v-kijais-wrapper-workflow-k3nk
  - *From: el marzocco*

- **Wan 2.2 LoRA Training Workflow Guide** (guide)
  - https://civitai.com/articles/17740/my-wan22-lora-training-workflow-tldr
  - *From: flo1331*

- **Wan 2.1 LoRA Training Workflow Guide** (guide)
  - https://civitai.com/articles/17385/my-wan21-lora-training-workflow-tldr
  - *From: flo1331*

- **Musubi Tuner Wan Documentation** (documentation)
  - https://github.com/kohya-ss/musubi-tuner/blob/main/docs/wan.md
  - *From: flo1331*

- **Musubi Tuner Official Repo** (repo)
  - https://github.com/kohya-ss/musubi-tuner
  - *From: xwsswww*

- **CAME optimizer** (tool)
  - https://github.com/yangluo7/CAME
  - *From: flo1331*

- **RTX 6000 Ada on Mercari Japan** (hardware)
  - https://jp.mercari.com/item/m41828148262
  - *From: screwfunk*

- **Qwen forum discussion link** (discussion)
  - https://discord.com/channels/1076117621407223829/1402003225061625888/1407307458921234432
  - *From: Guey.KhalaMari*

- **WAN 2.2 LoRA training workflow guide** (guide)
  - https://civitai.com/articles/17740/my-wan22-lora-training-workflow-tldr
  - *From: flo1331*

- **WAN 2.1 LoRA training workflow guide** (guide)
  - https://civitai.com/articles/17385/my-wan21-lora-training-workflow-tldr
  - *From: flo1331*

- **Musubi video dataset configuration** (documentation)
  - https://github.com/kohya-ss/musubi-tuner/blob/main/src/musubi_tuner/dataset/dataset_config.md#sample-for-video-dataset-with-control-images
  - *From: flo1331*

- **Musubi advanced config documentation** (documentation)
  - https://github.com/kohya-ss/musubi-tuner/blob/main/docs/advanced_config.md
  - *From: flo1331*

- **Golden Boy style LoRA** (model)
  - https://civitai.com/models/1671285?modelVersionId=2112013
  - *From: crinklypaper*

- **WAN 2.2 schedulers discussion** (discussion)
  - https://www.reddit.com/r/StableDiffusion/comments/1mkv9c6/wan22_schedulers_steps_shift_and_noise/
  - *From: Rego*

- **Wan 2.2 testing video** (tutorial)
  - https://www.youtube.com/watch?v=2d6A_l8c_x8
  - *From: crinklypaper*

- **Wan 2.2 launch stream** (presentation)
  - https://www.youtube.com/live/XaW_ZXC0Jv8?si=wh1AaSn7jycN1QRA
  - *From: crinklypaper*

- **RES4LYF node pack** (tool)
  - available via GitHub
  - *From: CJ*

- **Tiny VAE for preview** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: crinklypaper*

- **Kijai example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo2_2_I2V_A14B_example_WIP.json
  - *From: crinklypaper*

- **NotebookLM for Wan questions** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306?pli=1
  - *From: crinklypaper*

- **Hearmeman Musubi tutorial** (tutorial)
  - https://www.youtube.com/watch?v=kdfANZrJSp8
  - *From: WorldX*

- **Hearmeman's runpod script** (script)
  - https://github.com/Hearmeman24/runpod-diffusion_pipe/blob/master/wan2.2_lora_training/setup_and_train_musubi.sh
  - *From: Guey.KhalaMari*

- **Musubi advanced config documentation** (documentation)
  - https://github.com/kohya-ss/musubi-tuner/blob/main/docs/advanced_config.md#style-friendly-snr-sampler
  - *From: flo1331*

- **Scarlett Johansson test LoRA** (model)
  - https://www.dropbox.com/scl/fo/xs7zk07rwpzm261t9clv2/AJ948kA-Pi2mGGg0mPJqM3E?rlkey=fhrkx7uwrw4xh5yr4aprhn44w&st=4h111klm&dl=0
  - *From: JalenBrunson*

- **African Women T2V LoRA** (model)
  - https://civitai.com/models/1848135/african-women-t2v-wan-22-video-lora
  - *From: Kenk*

- **Hunyuan LoRA collection** (model)
  - https://civitai.com/collections/8755762
  - *From: Kenk*

- **TREAD implementation for Wan 2.2** (repo)
  - https://github.com/Ada123-a/diffusion-pipe-TREAD/blob/main/wan2.2_TREAD_example.toml
  - *From: Ada*

- **Wallace and Gromit style LoRA documentation** (documentation)
  - https://docs.google.com/document/d/1PQbAYn4_BdiGM6shq91HcyTLNZxrAGly3u3QaZJ9RqY/edit?usp=sharing
  - *From: crinklypaper*

- **Subgraph testing workflow** (workflow)
  - shared workflow file
  - *From: crinklypaper*

- **CuteCaption - AI captioning tool** (tool)
  - contact shotgun messiah via DM
  - *From: shotgun messiah*

- **Wan 2.2 training on RunPod guide** (tutorial)
  - https://civitai.com/articles/18081/training-wan-22-on-runpod-with-diffusion-pipe
  - *From: CJ*

- **Ada's captioning tool** (tool)
  - shared script file
  - *From: Ada*

- **Diffusion-pipe Wan 2.2 documentation** (documentation)
  - https://github.com/tdrussell/diffusion-pipe/blob/main/docs/supported_models.md
  - *From: crinklypaper*

- **Wan 2.2 bf16 models** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Persoon*

- **Wan 2.2 ComfyUI Repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: Guey.KhalaMari*

- **Qwen2.5-VL-7B-Captioner-Relaxed** (model)
  - https://huggingface.co/Ertugrul/Qwen2.5-VL-7B-Captioner-Relaxed
  - *From: MilesCorban*

- **Art datasets collection** (dataset)
  - https://github.com/georgeblck/art-datasets
  - *From: Persoon*

- **Wan 2.2 A14B Diffusers bf16** (model)
  - https://huggingface.co/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16
  - *From: mamad8*

- **Bowsette character LoRA** (lora)
  - https://civitai.com/models/1615071?modelVersionId=2166810
  - *From: crinklypaper*

- **5B style LoRA** (lora)
  - https://civitai.com/models/1897405?modelVersionId=2147817
  - *From: crinklypaper*

- **LoRA+ implementation** (repo)
  - https://github.com/nikhilgsh/loraplus
  - *From: DennisM*

- **Wan 2.2 I2V model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: Gentleman bunny*

- **Musubi dataset config documentation** (documentation)
  - https://github.com/kohya-ss/musubi-tuner/blob/main/src/musubi_tuner/dataset/dataset_config.md
  - *From: Kierkegaard*

- **WLSH nodes for ComfyUI** (tool)
  - https://github.com/wallish77/wlsh_nodes
  - *From: DennisM*

- **Musubi-tuner discussion thread** (repo)
  - https://github.com/kohya-ss/musubi-tuner/issues/59#issuecomment-2613708935
  - *From: flo1331*

- **WAN prompting guide** (research)
  - https://arxiv.org/pdf/2503.20314
  - *From: Kierkegaard*

- **Frame counting script for video datasets** (tool)
  - Script provided in message
  - *From: DennisM*

- **RunPod WAN 2.2 training guide** (guide)
  - https://civitai.com/articles/18081/training-wan-22-on-runpod-with-diffusion-pipe
  - *From: CJ*

- **Studio Ghibli LoRA training guide** (guide)
  - https://civitai.com/models/1404755/studio-ghibli-style-wan21-t2v-14b
  - *From: Kierkegaard*

- **Demystifying SD fine-tuning guide** (guide)
  - https://github.com/spacepxl/demystifying-sd-finetuning
  - *From: Kierkegaard*

- **WAN/Hunyuan LoRA training guide** (guide)
  - https://civitai.com/articles/11942/training-a-wan-or-hunyuan-lora-the-right-way
  - *From: mdkb*

- **WAN 2.1 fine-tuning guide** (guide)
  - https://learn2train.medium.com/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79
  - *From: mdkb*

- **Animated Logo Factory LoRA for Wan 2.1** (model)
  - https://civitai.com/models/1468212/animated-logo-factory
  - *From: Alisson Pereira*

- **Diffusion Pipe with Wan 2.2 fine tuning support** (repo)
  - https://github.com/tdrussell/diffusion-pipe/blob/main/docs/supported_models.md
  - *From: JohnDopamine*

- **Character LoRA training example on Civitai** (model)
  - https://civitai.com/models/1264662?modelVersionId=2080103
  - *From: Alisson Pereira*

- **K3NK Wan 2.2 workflow ver 1.92** (workflow)
  - CivitAI
  - *From: el marzocco*

- **RamTorch - potential Deepspeed replacement** (repo)
  - https://github.com/lodestone-rock/RamTorch
  - *From: JohnDopamine*

- **Wan 2.2 LoRA training workflow** (workflow)
  - https://civitai.com/articles/17740/my-wan22-lora-training-workflow-tldr
  - *From: flo1331*

- **Wan 2.1 LoRA training workflow** (workflow)
  - https://civitai.com/articles/17385/my-wan21-lora-training-workflow-tldr
  - *From: flo1331*

- **Beginner-friendly LoRA training tutorial** (tutorial)
  - https://youtu.be/oJdT5dzrNEY?si=d3SvYxw7hVpxiJlv
  - *From: Tachyon*

- **Accuracy Recovery Adapters** (model)
  - https://huggingface.co/ostris/accuracy_recovery_adapters
  - *From: JohnDopamine*

- **Portrait Master node for random styles and poses** (node)
  - https://github.com/florestefano1975/comfyui-portrait-master
  - *From: Tachyon*

- **JoyCaption standalone** (tool)
  - https://github.com/fpgaminer/joycaption
  - *From: shotgun messiah*

- **Kohya's Musubi Tuner GUI (abandoned)** (gui)
  - https://github.com/bmaltais/musubi-tuner-gui
  - *From: JohnDopamine*

- **AI-Toolkit Easy Install** (tool)
  - https://github.com/Tavris1/AI-Toolkit-Easy-Install
  - *From: xwsswww*

- **Kohya's GUI for image training** (gui)
  - https://github.com/bmaltais/kohya_ss
  - *From: xwsswww*

- **JoyCaption ComfyUI nodes** (tool)
  - https://github.com/1038lab/ComfyUI-JoyCaption
  - *From: el marzocco*

- **Accuracy Recovery Adapters** (tool)
  - https://huggingface.co/ostris/accuracy_recovery_adapters
  - *From: aipmaster*

- **Diffusion Pipe Docker** (tool)
  - wordbrew/diffusion-pipe-trainer:v3.3
  - *From: Alisson Pereira*

- **ComfyUI LoRA training custom node** (tool)
  - https://www.reddit.com/r/comfyui/comments/1nqd96f/i_have_created_a_custom_node_i_have_integrated/
  - *From: LionsEagles*

- **Wan training on Runpod guide** (workflow)
  - https://civitai.com/articles/18081/training-wan-22-on-runpod-with-diffusion-pipe
  - *From: Alisson Pereira*

- **New Wan 2.2 Lightning LoRA** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-250928
  - *From: WorldX*

- **Gurren Lagann Style LoRA** (model)
  - https://civitai.com/models/1897405/gurren-lagann-anime-style-wan-22-14b-lora?modelVersionId=2178677
  - *From: crinklypaper*

- **Wan 2.2 ComfyUI Workflow** (workflow)
  - https://civitai.com/models/1824027/wan-22-t2v-i2v-s2v-t2i-mmaudio4-6-stepsloop-video-extend-wanvideowrapper-workflowk3nk
  - *From: el marzocco*

- **Seruva's LoRA training guides** (tutorial)
  - https://civitai.com/user/seruva19
  - *From: crinklypaper*

- **Gemini captioning script** (tool)
  - https://gist.github.com/synap5e/357498ac59d019eac2ec53139c580d21
  - *From: Muon*

- **Google AI Studio for API keys** (tool)
  - https://aistudio.google.com/api-keys
  - *From: Muon*

- **Wan 2.2 training guide part 1** (guide)
  - https://docs.google.com/document/d/1DU6mV02vz9o39Uf4tAIlCQ9eTqEsY5W8V542N4EinZc/edit?usp=sharing
  - *From: crinklypaper*

- **Diffusion Pipe training issues** (repo)
  - https://github.com/tdrussell/diffusion-pipe/issues/416
  - *From: Dream Making*

- **High/Low noise training settings** (repo)
  - https://github.com/tdrussell/diffusion-pipe/issues/355#issuecomment-3170493704
  - *From: Dream Making*

- **JoyCaption Alpha Two** (tool)
  - https://huggingface.co/spaces/fancyfeast/joy-caption-alpha-two
  - *From: Tachyon*

- **Musubi Tuner step-by-step guide** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1lzilsv/stepbystep_instructions_to_train_your_own_t2v_wan/
  - *From: Tachyon*

- **Demystifying SD Fine-tuning** (guide)
  - https://github.com/spacepxl/demystifying-sd-finetuning
  - *From: Dream Making*

- **Wan 2.2 LoRA training workflow guide** (guide)
  - https://civitai.com/articles/17740/my-wan22-lora-training-workflow-tldr
  - *From: Tachyon*

- **Anime style training guide for Wan 2.2 part 1** (guide)
  - https://civitai.com/articles/20389
  - *From: crinklypaper*

- **ComfyUI JoyCaption node** (node)
  - https://github.com/1038lab/ComfyUI-JoyCaption
  - *From: el marzocco*

- **AI Toolkit Easy Install for Windows** (installer)
  - https://github.com/Tavris1/AI-Toolkit-Easy-Install
  - *From: Ryzen*

- **CAME optimizer for AI Toolkit** (optimizer)
  - https://github.com/yangluo7/CAME
  - *From: flo1331*

- **Random pose generator for character datasets** (tool)
  - *From: Tachyon*

- **220 effects & cameras dataset** (dataset)
  - *From: NebSH*

- **Wan 2.2 LoRA training workflow guide** (guide)
  - https://civitai.com/articles/17740/my-wan22-lora-training-workflow-tldr
  - *From: flo1331*

- **DimensionX GitHub repository** (repo)
  - https://github.com/wenqsun/DimensionX
  - *From: happy.j*

- **Gurren Lagann anime LoRA example** (model)
  - https://civitai.com/models/1897405?modelVersionId=2201875
  - *From: Tachyon*

- **Oxen.ai Wan fine-tuning service** (service)
  - https://docs.oxen.ai/examples/fine-tuning/video_generation
  - *From: Greg Schoeninger (Oxen.ai)*

- **Wan2.2-T2V-A14B-Diffusers-bf16** (model)
  - https://huggingface.co/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16/tree/main
  - *From: xwsswww*

- **Caption generation script** (tool)
  - Not provided
  - *From: Kiwv*

- **Lodestone Rock server** (community)
  - Not provided
  - *From: Kiwv*

- **send.vis.ee file sharing** (tool)
  - https://send.vis.ee/
  - *From: Kiwv*

- **Layer offloading technique** (technique)
  - https://x.com/tazmannner/status/1978071253542949056
  - *From: crinklypaper*

- **Detailed training settings guide** (guide)
  - https://civitai.com/articles/20389
  - *From: crinklypaper*

- **Gemini-powered captioning app for Wan** (tool)
  - *From: crinklypaper*

- **Qwen3-VL video captioning demo** (tool)
  - https://huggingface.co/spaces/baohuynhbk14/Qwen3-VL-Demo
  - *From: Kiwv*

- **Video clipping script** (tool)
  - *From: Kiwv*

- **Video annotation script** (tool)
  - *From: Kiwv*

- **OneTrainer** (tool)
  - *From: Kiwv*

- **Teen Titans style LoRA** (model)
  - https://civitai.com/models/2088410/teen-titans-2003-style-lora-wan-22-or-qwen
  - *From: crinklypaper*

- **Jujutsu Kaisen LoRA** (model)
  - https://civitai.com/models/2114480/jujutsu-kaisen-anime-lora-wan-video-22-t2v
  - *From: samurzl*

- **Qwen3-VL models for captioning** (model)
  - https://model.lmstudio.ai/download/lmstudio-community/Qwen3-VL-32B-Instruct-GGUF
  - *From: Kiwv*

- **Video clipper script** (tool)
  - *From: Kiwv*

- **Video annotater script** (tool)
  - *From: Kiwv*

- **ComfyUI-QwenVL node** (repo)
  - https://github.com/1038lab/ComfyUI-QwenVL
  - *From: Stef*

- **LoRA Captioner web app** (tool)
  - https://huggingface.co/spaces/comfyuiman/loracaptionertaz
  - *From: crinklypaper*

- **DagThomas ComfyUI nodes with QWen 3 support** (repo)
  - https://github.com/dagthomas/comfyui_dagthomas/commit/1709ad016109e1cd7769e592648dde927cffb3c8
  - *From: JohnDopamine*

- **Simple Captioner for local uncensored captioning** (tool)
  - https://github.com/o-l-l-i/simple-captioner
  - *From: BrainNXDomain*

- **Ostris AI Toolkit RunPod template** (tool)
  - https://console.runpod.io/deploy?template=0fqzfjy6f3&ref=h0y9jyr2
  - *From: crinklypaper*

- **WAN 2.2 T2V diffusers model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B-Diffusers/tree/main
  - *From: Guey.KhalaMari*

- **QWen 2.5 VL Video Captioning** (repo)
  - https://github.com/cseti007/Qwen2.5-VL-Video-Captioning
  - *From: DeZoomer*

- **Gemini AI Studio API** (tool)
  - aistudio.google.com
  - *From: Kiwv*

- **Musubi-tuner WAN training technique** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1oweppi/comment/novgpuc/
  - *From: oskarkeo*

- **Crinklypaper's LoRA Captioner v2** (tool)
  - https://huggingface.co/spaces/comfyuiman/loracaptionertaz_v2
  - *From: crinklypaper*

- **Scooby Doo Style LoRA** (model)
  - https://civitai.com/models/2167027/scooby-doo-mystery-incorporated-style-lora-qwen
  - *From: crinklypaper*

- **QwenVL ComfyUI Node** (node)
  - https://github.com/1038lab/ComfyUI-QwenVL
  - *From: Thom293*

- **Artificial_fungi training package** (workflow)
  - https://pixeldrain.com/u/qynM9PWq
  - *From: artificial_fungi*

- **JiT pixel space training paper** (repo)
  - https://github.com/LTH14/JiT/
  - *From: spacepxl*

- **Crinklypaper's training guide** (guide)
  - https://civitai.com/articles/20389/tazs-anime-style-lora-training-guide-for-wan-22-part-1-3
  - *From: crinklypaper*

- **ComfyUI Realtime LoRA** (tool)
  - https://github.com/shootthesound/comfyUI-Realtime-Lora/tree/main
  - *From: The Shadow (NYC)*

- **Wan2.2-Lightning model** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-250928-dyno
  - *From: crinklypaper*

- **New LightX distill LoRAs** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: crinklypaper*

- **ComfyUI DagThomas nodes** (node)
  - https://github.com/dagthomas/comfyui_dagthomas
  - *From: Thom293*

- **Anime style training guide part 2** (guide)
  - https://civitai.com/articles/23798
  - *From: crinklypaper*

- **Tensorboard patch for AI-Toolkit** (tool)
  - https://github.com/wallen0322/Tensorboard_patch_for_ai-toolkit
  - *From: JohnDopamine*

- **DiffSynth Studio Differential LoRA training** (method)
  - https://github.com/modelscope/DiffSynth-Studio/blob/main/docs/zh/Training/Differential_LoRA.md
  - *From: mrassets*

- **TagScribeR captioning tool** (tool)
  - https://github.com/ArchAngelAries/TagScribeR
  - *From: Thom293*

- **LoRA Caption Assistant (Windows compatible)** (tool)
  - https://github.com/zxtopower-tech/LoRA-Caption-Assistant
  - *From: Brooks*

- **Updated captioning tool v2** (tool)
  - https://huggingface.co/spaces/comfyuiman/loracaptionertaz_v2
  - *From: crinklypaper*

- **Captioning guide on Civitai** (guide)
  - https://civitai.com/articles/24082
  - *From: crinklypaper*

- **Training process guide** (guide)
  - https://civitai.com/articles/23798
  - *From: crinklypaper*

- **Anime style lora training guide** (guide)
  - https://civitai.com/articles/20389
  - *From: crinklypaper*

- **Demystifying SD finetuning guide** (guide)
  - https://github.com/spacepxl/demystifying-sd-finetuning/
  - *From: spacepxl*

- **5B lora release** (model)
  - https://civitai.com/models/1671285?modelVersionId=2560443
  - *From: crinklypaper*

- **Sampling shift write-up** (guide)
  - https://claude.ai/public/artifacts/3c79830d-d5f6-4770-b692-62383fd38a06
  - *From: shotgun messiah*

- **Seruva's Ghibli LoRA process documentation** (training guide)
  - *From: Piblarg*

- **Musibi tuner** (training tool)
  - *From: vuuw*


## Known Limitations

- **Character likeness poor in distant shots**
  - WAN has difficulty maintaining character features in wide/distant shots, unlike Hunyuan
  - *From: Cseti*

- **T2V LoRAs don't transfer well to I2V**
  - LoRAs trained on T2V model perform poorly when used with I2V model
  - *From: mamad8*

- **Higher ranks can cause overfitting**
  - While higher ranks learn faster, they quickly start overfitting with loss climbing
  - *From: samurzl*

- **Motion loss with image-only training at high epochs**
  - Training too long on images only can result in loss of camera motion
  - *From: makeitrad*

- **I2V LoRAs don't work across different model variants**
  - LoRAs trained on i2v-480P won't work on i2v-720P or t2v models
  - *From: codexq*

- **Wan VAE performs poorly with high inter-frame differences**
  - Struggles with timelapses where four frames of a latent have significant differences
  - *From: mamad8*

- **720P model doesn't handle LoRAs as well as 480P**
  - Loss of quality when using LoRAs trained on other models with 720P
  - *From: Cubey*

- **Character LoRAs can produce static results**
  - May need regularization videos or different training approach for proper movement
  - *From: mamad8*

- **Base Wan not good at outputting 4 frames**
  - Model struggles with very short 4-frame generations
  - *From: mamad8*

- **Single caption training creates inflexibility**
  - When training with only one caption per task, model goes crazy if using another prompt. Need to consolidate tasks and augment captions with GPT
  - *From: mamad8*

- **VAE encoding multiple different frames creates blur**
  - Tried encoding 4 completely different frames into one latent but everything becomes blurry
  - *From: mamad8*

- **Musubi trainer has issues with learning full motion**
  - Consistently only learns half the video motion, while other trainers like diffsynth work correctly with same dataset
  - *From: Juampab12*

- **DiffSynth doesn't support I2V training**
  - User wanted to switch but couldn't due to lack of I2V support
  - *From: Juampab12*

- **Training on pure images results in static video generations**
  - Images-only training causes motion problems in video generation
  - *From: Doctor Shotgun*

- **Very low resolution training concerns**
  - Training at 128x170 is extremely small - if base model doesn't know how to generate at this resolution, you'd have to train both resolution generation and your task
  - *From: mamad8*

- **1.3B model doesn't have I2V**
  - At least not yet, so can't take image input for high-res reference
  - *From: spacepxl*

- **Small datasets hurt motion quality**
  - With 50 images and 1-2 videos, motion will suffer a lot. 10 videos and 5 images might get good results
  - *From: Juampab12*

- **Image-only training damages motion capabilities**
  - Training only on images causes motion loss as it optimizes for images instead of both images and videos
  - *From: spacepxl*

- **Latent resizing artifacts**
  - If you resize latents you get lots of repeating artifacts - it only sort of works
  - *From: spacepxl*

- **VAE compression quality**
  - Compressed latents with different frames look like 140p compressed YouTube video from 2000
  - *From: mamad8*

- **720p training at 81 frames causes OOM**
  - Even on 8xH100 setup, full 720p at 81 frames runs out of memory
  - *From: Benjaminimal*

- **I2V cannot learn character likeness from images**
  - Training I2V model with only images will just strengthen first-frame reproduction ability rather than learning character features
  - *From: mamad8*

- **HUD elements don't train well at low resolution**
  - Video game HUD overlays failed to appear when training at low resolutions
  - *From: Mngbg*

- **VRAM size doesn't affect inference speed unless exceeded**
  - More VRAM won't make generation faster if you weren't hitting limits
  - *From: Screeb*

- **Higher learning rates can prevent effective learning**
  - Tries to learn too fast and becomes less effective than lower LRs
  - *From: spacepxl*

- **Training directly on I2V gives poor results**
  - User hasn't gotten good results training directly on I2V, considering T2V training instead
  - *From: ArtOfficial*

- **Wan celebrity/likeness training produces unrecognizable results**
  - Unlike HYV which works well for likenesses, Wan training results weren't recognizable
  - *From: JohnDopamine*

- **Camera movement training extremely difficult**
  - Hard to move focus off subject, possibly due to I2V clip_vision being heavily focused on subject
  - *From: ArtOfficial*

- **Multiple trigger words don't work well with insufficient data**
  - 10 images with second trigger word out of 150 total not enough
  - *From: ingi // SYSTMS*

- **Gemini API free tier very limited**
  - Only allows ~5 videos before hitting limitations
  - *From: Cseti*

- **Florence captioning produces errors**
  - Makes basic mistakes with hair color, length, person position, facing direction
  - *From: seitanism*

- **Block swapping validation bug**
  - Validation set doesn't work when block swapping is enabled in diffusion-pipe
  - *From: Payuyi*

- **Training loss unreliable without validation**
  - Raw training loss is random due to timestep sampling, needs validation set for meaningful metrics
  - *From: spacepxl*

- **Krea trained LoRAs cannot be downloaded**
  - Must use LoRAs within Krea platform only, cannot export for local use
  - *From: Nathan Shipley*

- **VideoUFO dataset quality issues**
  - Dataset contains garbage videos even when filtering with aesthetic score > 6.5
  - *From: mamad8*

- **Trigger words don't work well in Wan**
  - T5 encoder is too smart and prefers known concepts over custom trigger words
  - *From: Juampab12*

- **Control LoRA training needs large datasets**
  - Control LoRAs likely need significantly more training data than available for some character datasets
  - *From: mamad8*

- **Mixed camera movements don't train well**
  - Training with different pan directions results in stationary camera with objects moving instead of camera movement
  - *From: ArtOfficial*

- **Higher learning rates can damage model's anatomical knowledge**
  - Training with too high learning rate for too long can corrupt the model's understanding of anatomy and other base concepts
  - *From: samurzl*

- **Video captioning often misses temporal action**
  - Most video captioning tools only describe single frames rather than the action/movement happening in the video
  - *From: JmySff*

- **Tensorboard smoothing creates fake trends**
  - Don't trust tensorboard smoothing filter as it shows fake trends from moving average artifacts rather than real training progress
  - *From: spacepxl*

- **1.3B model poor for character training**
  - Struggles to maintain character likeness compared to 14B model, even with identical settings
  - *From: mamad8*

- **WAN generally poor for human likeness**
  - Not great at training human faces compared to other models like Hunyuan
  - *From: JohnDopamine*

- **Fun InP model quality issues**
  - Model performs poorly at T2V (doesn't know common concepts like red panda), I2V is mediocre
  - *From: Kijai*

- **Image-only training requires overfitting**
  - Training images only requires heavy overfitting to get good video likeness, degrading motion quality
  - *From: spacepxl*

- **Limited NSFW captioning capability**
  - JoyCaption struggles with extreme NSFW content recognition
  - *From: Kytra*

- **VACE control can break quality**
  - Sometimes VACE control seems to break quality, depth might be better than openpose
  - *From: Piblarg*

- **16fps output limitation for rapid movements**
  - Main limitation is hardcoded 16fps output for rapid movements
  - *From: Amirsun(Papi)*

- **Extending video instead of dropping frames messes up motion**
  - If you extend video duration instead of dropping frames, it will mess up the motion
  - *From: Benjimon*

- **Camera movement LoRAs extremely difficult to train**
  - Even with 20 videos of camera zoom, LoRA didn't work. Results are hard to distinguish from base model capabilities. Some concepts are harder to train because control is already built into the model.
  - *From: VRGameDevGirl84(RTX 5090)*

- **Training data collection is exhausting**
  - Collecting clips for motion LoRAs is time-consuming - 6+ hours to collect 100 clips with only 10 of the same motion, plus preparation/cropping/captioning work
  - *From: seitanism*

- **LoRA compatibility between model sizes**
  - LoRAs trained on 1.3B are not compatible with 14B and vice-versa. Also I2V trained LoRAs only work with I2V models, not T2V
  - *From: Kytra*

- **Training becomes very slow with higher resolutions**
  - Training at resolutions higher than 244p becomes supremely slow. 7.5 hours for 200 epochs with mixed resolution dataset
  - *From: seitanism*

- **WAN particle/artifact issues cannot be completely avoided**
  - Higher resolution and more steps help but don't eliminate the problem entirely
  - *From: TK_999*

- **14B LoRAs not compatible with 1.3B model**
  - Models have different architectures, LoRAs trained on one cannot be used on the other
  - *From: ZeusZeus (RTX 4090)*

- **Video LoRAs harder to evaluate for overtraining**
  - Very difficult to see where video LoRA might be overtrained or burnt compared to image LoRAs
  - *From: Piblarg*

- **Fun Control LoRA loading issues**
  - LoRA loading node was not working properly in Fun Control at time of testing
  - *From: ZeusZeus*

- **WAN LoRAs less effective on MoviiGen**
  - Previously trained WAN T2V LoRAs work on MoviiGen but with worse character likeness
  - *From: BondoMan*

- **14B model training challenges**
  - More difficult to train successfully compared to 1.3B, requires different approach and careful captioning
  - *From: JohnDopamine*

- **Training on images reduces video motion**
  - Beyond 20-40 epochs with images only, will start to lose motion in video output
  - *From: Thom293*

- **Wan has hard-trained motion blur**
  - Makes anything with animation difficult with high velocity things as it tries to blur
  - *From: Piblarg*

- **SkyCaptioner has high VRAM requirements**
  - Couldn't get it running locally without OOM on consumer hardware
  - *From: crinklypaper*

- **FAL training is images only**
  - When checked, FAL.ai only supported image training for Wan LoRAs
  - *From: Piblarg*

- **CivitAI training has 60 image limit**
  - CivitAI only lets you train 60 images max per session
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan models don't recognize certain actions in anime**
  - MiniCPM VQA cannot recognize character actions, requiring manual captioning of actions
  - *From: DreamWeebs*

- **Fp8 model incompatibility**
  - Wan2_1-T2V-14B_fp8_e4m3fn.safetensors has missing keys and doesn't load properly in Musubi Tuner
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sweet spot becomes smaller with very low quality training data**
  - Training with grainy GIFs works but creates smaller epoch range before artifacts appear
  - *From: Thom293*

- **Block swapping doesn't work in WSL2**
  - WSL2 on Windows has issues with block swapping functionality, works fine on native Windows/Linux
  - *From: MOV*

- **QwenVL doesn't read whole videos**
  - The ComfyUI QwenVL node doesn't process entire videos, only individual frames
  - *From: TK_999*

- **Video models limited by context tokens**
  - Gemma3 uses 256 tokens per image, so 40 frames needs 10,240 context length, may ignore frames if context too small
  - *From: Alisson Pereira*

- **Center cropping large videos results in very small sections**
  - Cropping 640 video from middle of 2160x3800 video is very small section - not ideal for video training
  - *From: Thom293*

- **Video compression artifacts hurt fine movement**
  - Compressed 4k videos still don't handle small fine movement like waves crashing without artifacting
  - *From: Thom293*

- **Some prompts don't respond to LoRA even with long training**
  - Certain scenes like studio scenes where base model is biased toward realistic over animated style
  - *From: Cseti*

- **Wan doesn't understand emotions or narrative states well**
  - Better results with more literal prompts rather than complex emotional/narrative descriptions
  - *From: crinklypaper*

- **Qwen VL captioning mistakes on claymation**
  - Hard for it to understand claymation style - didn't recognize genders correctly, thought hair was hat, many caption errors remained
  - *From: Cseti*

- **Image-only training reduces motion**
  - Training on images results in slower or less motion, but Dynamic speed LoRA can help counteract this
  - *From: VRGameDevGirl84(RTX 5090)*

- **RunPod community cloud reliability issues**
  - Almost all 4090s either python doesn't see GPU or machine won't start due to driver issues, support just suggests secure cloud
  - *From: Cseti*

- **Sigmoid training can affect backgrounds**
  - Sigmoid is stronger and easier to overtrain, can do weird stuff to backgrounds while learning character details well
  - *From: hablaba*

- **Multiple character LoRAs create merged twins**
  - Using 2 character LoRAs in same generation produces identical twins that merge both LoRAs rather than distinct characters
  - *From: el marzocco*

- **Training on styles WAN already handles well**
  - If base model + existing LoRAs already do a style well, training new LoRA may not add much value
  - *From: VRGameDevGirl84(RTX 5090)*

- **High resolution training catches imperfections**
  - Very high res datasets cause WAN to latch onto imperfections more than lower res training
  - *From: Persoon*

- **Training higher resolution than source degrades quality**
  - Training at higher resolutions than original 480p videos makes output worse unless upscaled first
  - *From: Thom293*

- **Multiple character LORAs don't work well**
  - Ends up averaging faces together instead of learning distinct characters
  - *From: Thom293*

- **Qwen Omni fp8 OOMs on 5090**
  - Works fine at fp4 though, fp8 causes out of memory errors
  - *From: Thom293*

- **DiffSynth produces weak LORAs on Wan 2.2**
  - Trained 20 epochs with 307 videos, LORA had almost no effect even at strength 10
  - *From: Alisson Pereira*

- **High model LoRA limited inference steps**
  - High noise model LoRA should only be used for 1/8 of inference steps due to narrow training timestep range (0.875-1)
  - *From: ArtOfficial*

- **LoKR causes OOM on 24GB VRAM with captions**
  - Training LoKR with captions causes out of memory on RTX 4090, works only with no captions or trigger words
  - *From: jikan*

- **Wan 2.1 LoRAs need high strength on 2.2**
  - Legacy 2.1 LoRAs require strength around 3.0 to work on 2.2, much higher than normal
  - *From: mamad8*

- **AI-toolkit doesn't support Wan 2.2 yet**
  - No Wan 2.2 support and lacks block swap for VRAM efficiency
  - *From: Alisson Pereira*

- **FP8 scaled models cannot be used for training**
  - Training fails with NaN values, must use fp16 models
  - *From: MilesCorban*

- **High noise model poor for character identity**
  - Character features not recognizable even at 8 steps when using high noise trained LoRA
  - *From: Kenk*

- **Model may be censored for adult content**
  - Generates fingers instead of male genitals, may need specific training to overcome
  - *From: Kenk*

- **Native ComfyUI mode produces worse results**
  - Same LoRA + model produces garbage in native mode but works well with Kijai wrapper
  - *From: Alisson Pereira*

- **Diffusion-pipe doesn't support video masking**
  - Only works with image masking, cannot mask watermarks or defects in video training
  - *From: MilesCorban*

- **Training only on images loses motion physics**
  - Particularly problematic for NSFW content where physics matter
  - *From: CJ*

- **5B model needs substantial training**
  - Requires more extensive training to reach expected performance given model size
  - *From: Fill*

- **WAN 2.2 14B heavily censored for NSFW content**
  - Testicles get deformed, model adds penises to females, struggles with male genitalia
  - *From: Kenk*

- **Character LoRAs affect all similar subjects in scene**
  - Cannot isolate effect to single character, affects every person or object of similar type
  - *From: Ruairi Robinson*

- **Lightning LoRAs reduce custom LoRA effectiveness**
  - New LightX2V LoRAs interfere with trained LoRAs, making them less effective
  - *From: _Djent_*

- **No LightX2V available for 5B model**
  - Speed improvements only available for 14B models, not 5B variant
  - *From: Alisson Pereira*

- **WAN heavily censored for NSFW content**
  - Converts penises to fingers, lacks NSFW training data unlike Hunyuan
  - *From: Kenk*

- **No metadata in WAN LoRA files**
  - Unlike image LoRAs, WAN video LoRAs don't store training metadata like epochs, learning rate in safetensors
  - *From: TekeshiX*

- **Training images mixed with videos not effective**
  - 768 resolution images in video training dataset don't show expected effects
  - *From: mrassets*

- **FP8 models don't work for training**
  - Must use FP16 models for training, FP8 scaled versions fail
  - *From: uff*

- **Wan 2.2 censorship**
  - Appears to be more censored than Hunyuan for NSFW content
  - *From: Kenk*

- **Loss graphs unreliable for diffusion models**
  - Diffusion-based model training should ignore loss graphs since it's lossy by nature
  - *From: MilesCorban*

- **Character bleeding in LoRAs**
  - Easy to train concepts that affect background, much harder to get it to affect just one character without bleeding
  - *From: Ruairi Robinson*

- **Automagic optimizer issues**
  - Multiple users report automagic optimizer wildly overtraining or not working properly
  - *From: MilesCorban, aipmaster*

- **Low noise training extremely slow convergence**
  - Loss gets stuck around 0.1xxx for extended periods, sometimes 18+ hours without improvement
  - *From: mrassets, crinklypaper*

- **Character LoRA transfer between T2V and I2V**
  - LoRAs trained on one mode may not work well on the other without very high strength settings causing artifacts
  - *From: screwfunk*

- **Radial attention resolution restrictions**
  - Only supports image sizes divisible by block size (128), gets error with non-conforming resolutions like 576x1024
  - *From: CJ*

- **Image-only training loses motion**
  - Training character LoRAs exclusively on static images results in no movement in generated videos
  - *From: crinklypaper*

- **Low noise model is very sensitive to overtraining**
  - Quality degrades significantly with higher epochs, making it hard to find the sweet spot
  - *From: flo1331*

- **WAN 2.2 training is much harder than 2.1**
  - Less reliable and consistent results compared to WAN 2.1, especially for character LoRAs
  - *From: aipmaster*

- **VRAM requirements are extremely high for video training**
  - Even 32GB can only fit 12 frames at 1280x720, making high-resolution video training impractical
  - *From: flo1331*

- **High resolution video training requires significant VRAM**
  - Training at 768p resolution is challenging even on high-end hardware
  - *From: Alisson Pereira*

- **Lightning LoRA incompatible with some character LoRAs**
  - Lightning completely breaks some LoRAs while LightX2V works but changes colors
  - *From: crinklypaper*

- **Cannot train on scaled fp8 model files**
  - Scaled versions cause state_dict loading errors, must use regular fp16
  - *From: flo1331*

- **Dual LoRA training VRAM limitations**
  - Cannot use block swap with dual training, making it very limited for higher resolution datasets even with 32GB VRAM
  - *From: 557733681767120896*

- **High noise model overtrains easily**
  - High noise model doesn't need as much training and easily overfits during dual training
  - *From: hablaba*

- **Image-only training harms motion**
  - Using only images for training results in slow-motion videos, videos needed to maintain motion quality
  - *From: MilesCorban*

- **LoRA merging not supported for WAN 2.1**
  - Post-hoc EMA merging of separately trained LoRAs not supported for WAN 2.1
  - *From: 557733681767120896*

- **High noise LoRA doesn't work well with Q4M quantization**
  - Works great on basic workflow with 14B 16fp when connected to both high and low, but fails with Q4M and especially with lightxv2
  - *From: GOD_IS_A_LIE*

- **Wan does poor job with swimming motion**
  - Custom motion training needed for swimming scenes
  - *From: Ryzen*

- **JoyCaption can produce inconsistent results**
  - Sometimes outputs unusual captions like 'except for black jacket' instead of proper descriptions
  - *From: Ryzen, screwfunk*

- **AI-toolkit may have issues with WAN training**
  - Success reported as failure compared to musubi, samples don't work on real generations
  - *From: GOD_IS_A_LIE*

- **Lightning models change style unpredictably**
  - Colors get oversaturated and style gets distorted, not reliable for testing trained models
  - *From: crinklypaper*

- **Loss graphs unreliable for WAN 2.2**
  - Cannot determine training quality from loss numbers, especially for high model
  - *From: screwfunk*

- **RTX 5090 can't handle 512 resolution for video training**
  - Must use 256 resolution instead due to VRAM constraints
  - *From: Ryzen*

- **Dual training requires significant VRAM**
  - Takes twice as much VRAM, GPUs under 32GB may struggle without block swap
  - *From: flo1331*

- **AI Toolkit missing key features**
  - No epochs support, no LR loss charts, limited feature set compared to other trainers
  - *From: Ryzen*

- **Can't train using Wan 2.2 GGUF models**
  - GGUF format not supported for training, need FP16 models
  - *From: flo1331*

- **Diffusion Pipe doesn't support dual training**
  - Cannot train high and low noise models simultaneously
  - *From: flo1331*

- **High model overfits very quickly**
  - High model overfits way too soon compared to low model, shouldn't train both at same time
  - *From: mamad8*

- **Traditional training metrics don't work for WAN 2.2**
  - Charts, steps, and loss metrics that were reliable for WAN 2.1 don't indicate quality for WAN 2.2
  - *From: screwfunk*

- **JoyCaption mentions tattoos despite instructions not to**
  - Even when explicitly instructed not to mention tattoos, JoyCaption still includes them in captions
  - *From: hablaba*

- **Lightning/LightX LoRAs broken with WAN 2.2 T2V**
  - Work fine for I2V but cause issues and distortions in T2V mode
  - *From: crinklypaper*

- **WAN 2.2 easier to overtrain than 2.1**
  - Model can show overtraining effects after just one epoch depending on dataset size and settings
  - *From: crinklypaper*

- **High model cannot work independently**
  - Unlike low model which can work alone, high model requires low model to function properly
  - *From: Alisson Pereira*

- **High noise LoRAs lose motion over training**
  - Becomes more apparent at higher epochs
  - *From: el marzocco*

- **High noise LoRAs can change character ethnicity**
  - Makes characters look Asian regardless of original ethnicity
  - *From: el marzocco*

- **Lightning LoRAs limited by step count**
  - Lower steps provide less room for hitting correct timestep switches
  - *From: CJ*

- **Training videos causes resolution issues**
  - Switching from images to videos in Musubi causes configuration errors
  - *From: WorldX*

- **Compressed video quality**
  - Video files are compressed, may not provide optimal training data compared to image sequences
  - *From: Guey.KhalaMari*

- **Multiple character LoRAs blend when used together**
  - Using separate character LoRAs in same video makes characters look like mix of both - model doesn't know to apply different LoRAs to different characters
  - *From: screwfunk*

- **Creating diverse faces with single LoRA**
  - Training multiple different faces in one LoRA still tends to produce same face, even with different trigger words per face
  - *From: Kenk*

- **Loss graphs unreliable for quality assessment in 2.2**
  - Unlike 2.1, loss values don't correlate with LoRA quality - manual testing required
  - *From: screwfunk*

- **Speed LoRAs cause quality tradeoffs**
  - Lightning and LightX both have issues - Lightning makes poor animation quality, LightX changes colors
  - *From: screwfunk*

- **Training with very short clips (7-13 frames) gives worse results**
  - Better to lower resolution than go below ~17 frames
  - *From: flo1331*

- **5B model VAE quality**
  - 5B model has VAE quality issues compared to 14B
  - *From: crinklypaper*

- **AI toolkit produces plastic-looking skin and anatomy issues**
  - Videos run at freakishly fast speed, anatomy becomes messy, compared to Diffusion-pipe which produces better results
  - *From: mrassets*

- **Training videos longer than 121 frames causes memory issues**
  - Even at 256 resolution, 121 frame buckets cause OOM errors
  - *From: MilesCorban*

- **Overtraining on static images reduces motion and emotions**
  - Character LoRAs become static and expressionless, can also cause foggy outputs at extremes
  - *From: MilesCorban*

- **Light X2V compatibility issues with trained LoRAs**
  - Results get messed up when using Light X2V with trained LoRAs, appears to be related to the Light X2V LoRA itself
  - *From: Kiwv*

- **Wan 2.2 LoRAs may not work perfectly in Wan 2.1**
  - Some compatibility but with limitations, particularly for low noise models
  - *From: Gentleman bunny*

- **I2V training cannot use image datasets**
  - I2V training crashes if you try to include images - must use video-only datasets
  - *From: DennisM*

- **Video training has detail limitations**
  - Cannot capture small details like tattoos due to low resolution and dim=16
  - *From: flo1331*

- **Trigger words damage text generation ability**
  - Using trigger words in captions destroys the model's ability to generate text in images
  - *From: flo1331*

- **Loss curves identical after 50 steps**
  - Loss curve looks exactly the same regardless of dataset after about 50 steps, making it unreliable for judging training progress
  - *From: flo1331*

- **Character LoRA cross-compatibility**
  - Character LoRAs trained on 2.2 T2V don't work well for I2V, while 2.1 LoRAs work better for 2.2 I2V than native 2.2 LoRAs
  - *From: scf*

- **Motion LoRA effectiveness on FLF2V**
  - WAN 2.2 I2V motion LoRAs seem to have little effect on FLF2V inference, unclear if it's LoRA quality or incompatibility
  - *From: jikan*

- **Training on images too long reduces motion**
  - If you train on just images for too long, it will reduce motion in video generation
  - *From: Thom293*

- **Character LoRA cross-contamination issue**
  - Character LoRAs at high strength (1.5) can make all males have the trained female face with a beard
  - *From: Tachyon*

- **Trained LoRAs weaker on control models**
  - LoRA trained on 5B model appears weaker when used on 5B control model
  - *From: Guey.KhalaMari*

- **Character bleeding into background characters unavoidable**
  - Common issue across all current models since Stable Diffusion 1.4/1.5, no way to completely avoid it
  - *From: JohnDopamine*

- **8GB VRAM insufficient for video training**
  - Videos barely fit with 16GB VRAM for 16-32 frames, with blockswap maximum 36 frames. 8GB probably only supports image training
  - *From: flo1331*

- **Image training degrades motion quality**
  - Training on images instead of videos reduces motion quality in generated videos
  - *From: flo1331*

- **Speed LoRAs can make character LoRAs look worse**
  - Using speed LoRAs alongside character LoRAs can degrade character resemblance
  - *From: Guey.KhalaMari*

- **Lip-sync models don't capture nuances well**
  - All lip-sync models including InfiniteTalk look pretty bad and don't capture performance nuances
  - *From: Guey.KhalaMari*

- **8GB VRAM insufficient for Wan training without block swapping**
  - Minimum 24GB required, block swapping can only reduce by ~8GB
  - *From: ArtOfficial*

- **Block swapping limited by checkpoint size**
  - Can only swap ~16GB (checkpoint), everything actively training must stay in VRAM
  - *From: ArtOfficial*

- **Low noise only LoRAs have minimal impact**
  - Especially for style effects, need high noise training to see significant results
  - *From: oumoumad*

- **Loss values in Wan 2.2 are unpredictable**
  - Loss doesn't drop consistently in Wan 2.2 low noise training, numerical value matters less than trending downward
  - *From: el marzocco*

- **High strength LoRAs create caricatures**
  - When using real people datasets, increasing LoRA strength above normal creates caricature with exaggerated features
  - *From: el marzocco*

- **Overtraining leads to unwanted feature persistence**
  - Around step 1800, LoRAs fall apart with issues like 'always has white hair' that are impossible to prompt away
  - *From: Kytra*

- **Missing training data affects style triggering**
  - If dataset had no nipples/hardcore nudity, the high model often wouldn't trigger the style for such content
  - *From: crinklypaper*

- **2.2 tensor graphs mostly useless**
  - Unlike 2.1, loss graphs in 2.2 don't provide reliable training indicators
  - *From: crinklypaper*

- **Hard cuts in videos not supported**
  - Videos with hard cuts should be split into separate videos as Wan doesn't handle them well
  - *From: crinklypaper*

- **Trigger words ineffective**
  - Trigger words don't really work in Wan training, better to describe actions directly
  - *From: Tachyon*

- **Wan 2.2 tensor graphs are not useful for monitoring training**
  - Can only observe patterns, graphs don't provide meaningful training metrics
  - *From: crinklypaper*

- **Training loss doesn't indicate overfitting**
  - Big model with small data will memorize everything and overfit forever
  - *From: spacepxl*

- **Triggerwords can degrade text generation capabilities**
  - Model thinks triggerword is written text, causing letter distortion
  - *From: flo1331*

- **8GB cards can't train videos effectively**
  - Video training requires more VRAM than available on 8GB cards
  - *From: flo1331*

- **8GB VRAM insufficient for Wan LoRA training**
  - Recovery adapters don't work, requires float8 which is extremely slow, minimum 5090 recommended
  - *From: Kiwv*

- **Can't train images with I2V mode**
  - Image training only works with T2V mode in training tools
  - *From: Kiwv*

- **Multi-character LoRAs prone to concept bleeding**
  - 5 character LoRA abandoned after 200 epochs due to excessive bleeding
  - *From: flo1331*

- **One Trainer doesn't support Wan 2.1 and won't be updated**
  - Developer has limited time, no plans to add Wan support
  - *From: metaphysician*

- **8GB VRAM insufficient for Wan training**
  - Need to offload 90% of model to CPU, essentially training on CPU which makes shared GPU memory usage slow training by 2x per GB
  - *From: Kiwv*

- **Training images on I2V wastes compute**
  - Model just outputs the input image for 1-frame generation, provides 0 loss
  - *From: Kiwv*

- **Plastic skin look with Wan 2.1/2.2**
  - Sometimes produces airbrushed/soft skin appearance even with high quality images
  - *From: humangirltotally*

- **Wan becomes repetitive beyond 81 frames**
  - 99% of training is on 81 frames, movement becomes repetitive at 161 frames
  - *From: Kiwv*

- **Multi-dataset LoRA training is problematic**
  - Model optimizes more prevalent concept first, making training less effective
  - *From: Kiwv*

- **3090 too slow for Wan training**
  - 40-50 hours for batch of 8-10 videos, 33 frames at 256px
  - *From: Kiwv*

- **WAN training on 8GB cards**
  - Requires minimum 24GB VRAM for fp8 training. 8GB forces CPU training taking 100+ hours
  - *From: Kiwv*

- **Small caption training only works for I2V**
  - T2V requires detailed scene descriptions, small captions cause memorization
  - *From: Kiwv*

- **Resolution mismatch causes distortion**
  - LoRAs trained on different resolutions will stretch output like SDXL
  - *From: Thom293*

- **AI toolkit can't train multiple frame counts simultaneously**
  - Feature is planned but not implemented
  - *From: Kiwv*

- **Image-only training can result in reduction in motion**
  - Better to add at least a few videos to dataset
  - *From: crinklypaper*

- **12 images insufficient for good LoRA**
  - Model will memorize exact images rather than learn concept. Need 50+ images minimum
  - *From: Kiwv*

- **WSL2 has speed drawbacks compared to native Linux**
  - Partitioned Ubuntu install works much better
  - *From: Kiwv*

- **Single person datasets create character LoRAs**
  - Training on single person data partly trains character features along with intended concept
  - *From: Kiwv*

- **Style LoRAs often bring unwanted objects**
  - Common objects from training data appear even when not wanted (e.g., Link appearing in Breath of Wild style)
  - *From: Kiwv*

- **Face cropping in adult LoRAs causes out-of-frame bias**
  - Training with faces cropped out makes LoRA bias toward putting faces out of frame
  - *From: crinklypaper*

- **Cannot train with WAN 2.2 fp8_scaled models**
  - fp8 scaled models incompatible with ai-toolkit training
  - *From: Guey.KhalaMari*

- **Wan 2.2 poor text generation**
  - Struggles with text in images, especially labels and logos, often produces distorted text
  - *From: crinklypaper*

- **Fast motion distortion in style LoRAs**
  - Fast motion causes mushy/distorted appearance, especially with anime style LoRAs, overfitting helps but doesn't fully resolve
  - *From: crinklypaper*

- **LoRA character bleed**
  - Character LoRAs tend to affect all people in scene, difficult to have distinct characters in crowds
  - *From: oskarkeo*

- **81 frames exponentially slower**
  - Training on full 81 frames gets exponentially slower, most effects achievable in 33 frames
  - *From: AshmoTV*

- **Wan2.2 produces slow motion by default**
  - Even with LightX2V LoRAs, getting proper real-time motion sequences is difficult
  - *From: dj47*

- **Character LoRAs can have bleeding between characters**
  - Characters may share features like headbands and lipstick across different characters
  - *From: dj47*

- **Training images-only for T2V gives unpredictable movement**
  - Movement can be erratic with legs kicking walls, requires video data for proper motion
  - *From: Ryzen*

- **Holocine model destroys LoRA compatibility**
  - LoRAs trained on standard models don't work with Holocine
  - *From: avataraim*

- **5B model has poor prompt adherence and quality**
  - Despite being native 720p 24fps, quality and prompt following is too terrible for practical use
  - *From: dj47*

- **Training poses is difficult**
  - User expressed frustration that pose training is particularly challenging
  - *From: Ryzen*

- **Dance sequence training is very hard**
  - Fixed sequence of moves like dance is very difficult to train effectively, even with 10-20 videos of 4s each
  - *From: Brooks*

- **9 different concepts in one lora is challenging**
  - Will need a lot of training steps, mixing concepts is harder
  - *From: spacepxl*

- **Naive unscaled fp8 quantization**
  - Produces trash quality for training or inference due to bad quality loss
  - *From: spacepxl*

- **Training secrets not widely shared**
  - Because there's serious money in training models, many techniques are kept as secrets
  - *From: Piblarg*


## Hardware Requirements

- **1.3B LoRA training**
  - 12.8GB VRAM for 38 images at 512x512 rank 32
  - *From: Kendo*

- **14B LoRA training**
  - 42.5GB VRAM for multi-resolution (384/512/768/1024), 4.2-25.8 steps/sec depending on resolution
  - *From: mamad8*

- **1.3B image training**
  - 6-7GB VRAM for 1024x576 resolution image-only training
  - *From: Cseti*

- **I2V 14B training**
  - 36GB VRAM for 256x384x5 frames at batch size 1
  - *From: mamad8*

- **4090 compatibility**
  - Can train 1.3B LoRAs, 14B uses full 24GB VRAM
  - *From: Cubey*

- **14B model training VRAM**
  - FP8 I2V training requires ~24GB+ VRAM, 400p x 13frames needs 24GB
  - *From: codexq*

- **1.3B model training**
  - Tight fit at 512x768x31 on 24GB, required rank 16
  - *From: 片ヨ亡亡丹片*

- **High resolution video training**
  - 1280x720@81 frames requires 135GB VRAM, takes 3 minutes per step
  - *From: mamad8*

- **Quantization memory savings**
  - NF4 quantization fits in <16GB even with VAE loaded for Hunyuan-sized models
  - *From: spacepxl*

- **Musubi 14B photo training**
  - ~26GB VRAM for 12 images at 512x512 to 512x704
  - *From: seitanism*

- **1.3B model VRAM usage**
  - 832x480 at 49 frames uses about half VRAM on 24GB GPU, much less restrictive than i2v 14B
  - *From: Juampab12*

- **Training time on consumer hardware**
  - 1 epoch with 15 videos, 5 repeats took 3 hours on 4090. 24 hours needed for good results at 2e-5 LR on L40S
  - *From: Juampab12*

- **14B model training on 24GB**
  - For 12GB, use resolution of 960x544, probably can do 1280x720 at least on 24GB, probably higher
  - *From: Juampab12*

- **Training speed**
  - About 30-20 minutes per epoch reported for diffsynth
  - *From: avataraim*

- **OOM limitations**
  - 128x170 resolution used because higher resolutions cause out of memory errors
  - *From: Juampab12*

- **14B model training on 4090**
  - Takes forever even at 768 resolution with transformer_dtype = float8. Barely fits 512x512x81 with fp8 transformer, AdamW8bitKahan optimizer, and blocks_to_swap=32
  - *From: Frojef*

- **1280x720x65 training**
  - Just barely fits in 80G H100 memory while training
  - *From: Benjaminimal*

- **1280x720x81 training**
  - OOMs on H100s - pipeline parallelism would theoretically fix this but not working yet
  - *From: Benjaminimal*

- **Multi-GPU utilization**
  - Diffusion-pipe achieves ~100% utilization of all 8 GPUs consistently
  - *From: Benjaminimal*

- **8xH100 for large frame training**
  - Needed for training with frame buckets up to 113 frames at 832x480 resolution
  - *From: Benjaminimal*

- **VRAM calculation for training**
  - 1280x720x81 = 75,600 tokens vs 832x480x113 = 45,240 tokens for planning training capacity
  - *From: spacepxl*

- **48GB VRAM for inference**
  - Video generation taking longer than expected even on 48GB VRAM GPU
  - *From: VRGameDevGirl84(RTX 5090)*

- **8xH100 for large-scale training**
  - Hardware used for successful steamboat Willie style LoRA training
  - *From: Benjaminimal*

- **4090 with 128GB RAM for 14B local training**
  - Sufficient for training 14B models with block swapping, likely doesn't use above 64GB
  - *From: JohnDopamine*

- **150GB storage allocation for runpod**
  - Recommended storage for training setup including models and packages
  - *From: Alisson Pereira*

- **Network Volume storage costs**
  - $10.50/month for 150GB at $0.07/GB
  - *From: DevouredBeef*

- **320x320 resolution training**
  - Can do 17 frames max on 24GB VRAM
  - *From: Juampab12*

- **Lego LoRA training**
  - 1500 videos with 672x384, 33/49/65 frames uses ~10GB VRAM on 4060ti
  - *From: Cseti*

- **14B I2V training**
  - 149 videos, 64 frames, requires 48GB L40S
  - *From: Alisson Pereira*

- **512x512x81f video training**
  - Possible on 24GB with block swapping enabled
  - *From: ArtOfficial*

- **Qwen2.5-VL captioning**
  - 7B model fits in 16GB VRAM with bnb, 24GB without quantization
  - *From: Cseti*

- **24GB VRAM for captioning**
  - RTX 4090 with 24GB can handle video captioning with max_pixels and fps parameter tuning
  - *From: Cseti*

- **H100 training costs**
  - 15000 step training session on 4090 costs approximately $8 on Runpod
  - *From: CJ*

- **Weekly Runpod spending**
  - $10-20 weekly depending on training frequency
  - *From: CJ*

- **H100 cluster training times**
  - Minimum 30 minute training times even with H100 cluster for proper quality without burning
  - *From: Kytra*

- ****
  - Training 512x512x81f on 14B maxes out 32GB VRAM (5090). Estimates 24GB (4090) could handle ~13f at 720p or 19f at 512p
  - *From: ArtOfficial*

- ****
  - 24GB 3090 handles LoRA training without issues, unless training checkpoints with millions of examples
  - *From: Amirsun(Papi)*

- ****
  - 8x H100s cost $12/hour on runpod. 8x 48GB cards ~$10/hour. 10x 3090s available for $2.2/hour for 1.3B model
  - *From: Kytra*

- ****
  - 3B: 735MB-5.75GB, 7B: 1.65GB-13.17GB, 72B: 16.64GB-133.11GB depending on precision (INT4 to FP32)
  - *From: Benjimon*

- ****
  - Using Qwen2.5 3B param on 24GB card achieves 5 fps on 2-second clips of 49 frames
  - *From: Amirsun(Papi)*

- **4090 VRAM for 1.3B training**
  - Can train 256x256x25f using 23.7GB VRAM without block swapping
  - *From: ArtOfficial*

- **A40 sufficient for training**
  - Successfully used on RunPod for training runs
  - *From: TimHannan*

- **H100 performance**
  - 1800 steps with 34 videos completed in ~1.5 hours on single H100
  - *From: DevouredBeef*

- **Training cost on RunPod**
  - High VRAM training can cost ~$50 and take 48 hours for 1000 steps with large datasets
  - *From: ArtOfficial*

- **Multiple GPU training doesn't linearly add VRAM**
  - To train on as large videos as one 48GB GPU you need 4x24GB GPUs with pipeline parallelism. The 4x24GB will be faster though if same generation
  - *From: Benjimon*

- **RTX 8000 performance vs 4090**
  - Wan training on RTX 8000 was about 50% slower than 48GB 4090, cheapest big GPU option
  - *From: Benjimon*

- **5090 training capabilities**
  - Can train videos at 244p with 81, 49, 33 frames using WSL with diffusion pipe, works with 32GB VRAM
  - *From: Alisson Pereira*

- **Gemma3 27B model VRAM usage**
  - Uses around 98% of 32GB VRAM on 5090, works fast for captioning
  - *From: Alisson Pereira*

- **VRAM for 14B training with block swapping**
  - 5090 with 32GB VRAM can train 14B at resolution [384, 288] with target_frames [45] and 10 blocks swapped, but may still OOM. Need to go lower resolution and more block swapping.
  - *From: const username = undefined;*

- **H100 training speed**
  - Even on H100, training takes 30 minutes per 2 epochs with high-resolution mixed dataset
  - *From: crinklypaper*

- **5090 training capabilities**
  - Can train 256x384x81 clips and 1920x1072 images with 5 blocks swapped, using 30GB VRAM
  - *From: seitanism*

- **Storage and transfer speeds**
  - Runpod network storage can have very slow download speeds (55kb/s) but AWS S3 transfer achieves 350 mb/s
  - *From: ingi // SYSTMS*

- **FramePack 13B model VRAM**
  - 6GB minimum for 1-minute video generation, works on laptop GPUs
  - *From: lovis.io*

- **WAN 14B training with 48GB VRAM**
  - Can do 480x480 resolution with 20 blocks swapped
  - *From: Benjimon*

- **WAN 14B training speed on RTX 8000**
  - 30 seconds per iteration
  - *From: Benjimon*

- **WAN 14B training speed on 4090 48GB**
  - 13 seconds per iteration
  - *From: Benjimon*

- **Character LoRA training on 1.3B**
  - 34 epochs took about 2 hours on RunPod A10
  - *From: TimHannan*

- **5090 training performance**
  - 52 images, epoch 50 in exactly 1 hour for 14B model
  - *From: seitanism*

- **Max frames with 5090**
  - 41 frames at 480x832 with 35 block swap
  - *From: Piblarg*

- **3090 24GB training specs**
  - Can handle WAN 1.3B training fine, 14B requires optimizations like block swap. hovering around 8s/it with 128GB RAM, AMD Threadripper CPU
  - *From: sneako1234*

- **5090 training capability**
  - Can train 512x81 frame videos on 14B model, reaches ~20GB VRAM usage
  - *From: Thom293*

- **4090 training specs**
  - Can train 512 res x 48 frames x1 repeat and 768 images x2 repeat with memory optimizations on HunyuanVideo, similar expected for WAN
  - *From: Thom293*

- **H100 vs consumer GPU**
  - H100 handles 14B T2V training at higher resolutions without issues, while 48GB consumer cards go OOM on same settings
  - *From: crinklypaper*

- **24GB VRAM training**
  - Can train with float8, blocks_to_swap 8, requires closing background apps. 4090 can handle 1024x1024 images at 10 repeats
  - *From: crinklypaper*

- **5090 training capabilities**
  - Can train 80 frames at 800x512 resolution, uses 20GB VRAM with block swap 32
  - *From: Thom293*

- **4090 optimization**
  - Blocks to swap 14-20, can achieve 2.9s/it, handles mixed image/video datasets on T2V model
  - *From: Think*

- **High-end training setup**
  - 4090 with 213 video dataset: 128x192@97 frames, 384x576@37 frames, 640x960@13 frames, 11s/it, 23.5GB VRAM
  - *From: Persoon*

- **Consumer hardware video limits**
  - Can't train 80 frames at high resolution on consumer hardware, 416x240 works fine at longer lengths
  - *From: Piblarg*

- **RTX 5090 training performance**
  - 7 minutes per epoch for 50 images at 1024x1024, batch size 2, can handle training without block swapping
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 4090 training capabilities**
  - Can handle images without block swapping, videos need 20-30 block swap for 81 frames, images+video can do batch 2 for images and 1 for videos
  - *From: Thom293*

- **RTX 3090 training speed**
  - 2.5 hours per epoch for 380 images at 576x768 resolution, using ~20GB VRAM
  - *From: crinklypaper*

- **Training VRAM usage comparison**
  - 14B model training on images uses surprisingly low VRAM compared to expected usage
  - *From: Piblarg*

- **RTX 5000 series compatibility**
  - Requires PyTorch >= 2.7.0 for Blackwell architecture (RTX 5090 etc)
  - *From: Alisson Pereira*

- **14B model training on RTX 5090**
  - Can train 450 images at 1024 resolution, 640p video training possible with block swap
  - *From: Thom293*

- **WSL2 memory allocation**
  - Need to configure .wslconfig file to allocate sufficient RAM (124GB) and swap (64GB) for block swapping
  - *From: MOV*

- **5090 training capacity**
  - Can train 640p x 81 frames, might hit 720p with memory fixes
  - *From: Thom293*

- **24GB VRAM limits**
  - Can only train 624x360 videos with 81 frames at most, block swap maxed out
  - *From: MaQue*

- **WSL2 memory configuration**
  - Need to increase WSL memory through .wslconfig file, recommend at least 32GB RAM for WSL
  - *From: Alisson Pereira*

- **Storage location importance**
  - Put everything inside WSL rather than mounted drives - reading outside WSL is much slower
  - *From: Alisson Pereira*

- **RTX 6000 Pro training**
  - Uses only 60GB VRAM for training to leave remaining for testing LoRAs
  - *From: notid*

- **Wallace and Gromit 14B LoRA training**
  - 70 hours on 4090, dataset of 87 videos at 570x405 resolution in [33,65,81] frames
  - *From: Cseti*

- **30 images WAN training**
  - About 4 hour training process on a 4090
  - *From: Faust-SiN*

- **1.3B WAN training on 12GB VRAM**
  - 4 hours for 10 images 256x256 with 32GB RAM using WSL2 ubuntu on windows 10
  - *From: mdkb*

- **14B training VRAM usage**
  - 20 out of 31 GB VRAM used, steady at 70°C, overnight training (9pm to 10:42am)
  - *From: VRGameDevGirl84(RTX 5090)*

- **8GB GPU WAN training possibility**
  - Should be able to train 1.3B T2V WAN with transformer dtype float8, save_dtype bfloat16 or block swapping
  - *From: crinklypaper*

- **GPU temperature during training**
  - 3090: 75°C with Flux, 5090 FE: 75°C core/85°C memory, A6000: 80°C, 4090: 69-80°C
  - *From: ˗ˏˋ⚡ˎˊ-*

- **3090 VRAM for 100 images**
  - Can fit 100 images at max 720p with some offloading
  - *From: Guey.KhalaMari*

- **5090 video training capability**
  - Can train 512p, 576p, 640p video, possibly 720p with tweaks, buckets 640p videos at 800x512
  - *From: Thom293*

- **4090 training time estimates**
  - 150 images: 2 nights (6-10 hours), 150 images + 75 videos: 4-5 nights (15-25 total hours)
  - *From: Thom293*

- **H100 96GB VRAM can handle 1280x720x81**
  - User only utilizing 29GB/96GB, could easily do full 720p training
  - *From: Thom293*

- **5090 32GB maxes at 640p with Diffusion Pipe**
  - Resizes videos to 800x512x81, but AI Toolkit can do 1280x768 with blockswap
  - *From: Thom293*

- **Model merging needs 89GB RAM**
  - Required for merging multiple Wan models together
  - *From: Thom293*

- **Wan 2.2 5B training VRAM usage**
  - 11GB VRAM for basic training, 19-21.5GB with batch size 4-5 and 4-5 repeats on 5090
  - *From: crinklypaper*

- **Wan 2.2 14B I2V training on 5090**
  - 256 resolution, 49 frames, rank 64, 301 videos, batch size 1 uses full VRAM without block swap
  - *From: Alisson Pereira*

- **RTX 5090 flash attention setup**
  - Requires torch 2.7.0+cu128, CUDA 12.8+, specific pre-compiled wheels due to compilation issues
  - *From: mamad8*

- **24GB VRAM training config**
  - Successfully trains with micro_batch_size=1, gradient_accumulation=4, 30 blocks swapped, or no block swap at 94% VRAM usage
  - *From: chancelor*

- **Low power consumption during training**
  - GPU power around 250W out of 450W potential, training runs quiet and cool with 90% VRAM usage at 0.2 samples/sec
  - *From: chancelor*

- **VRAM for 5B model training**
  - 1024p videos, 73 frames, batch size 2 with gradient accumulation doesn't use all VRAM on high-end GPU
  - *From: Alisson Pereira*

- **4090 training performance**
  - Can train character LoRAs in 30 minutes, supports block swap for multitasking, allows 512 resolution training
  - *From: Kenk*

- **Training speed difference**
  - Low noise model trains significantly faster than high noise model with same settings
  - *From: CJ*

- **12GB VRAM sufficient for Wan 2.1 14B training**
  - Training time: 1h25m with proper settings and block swapping
  - *From: Lodis*

- **Block swapping for VRAM management**
  - Enables training larger models with limited VRAM
  - *From: Kenk*

- **WAN 2.2 14B fp16 training VRAM**
  - 28GB for fp16, can use transformer_dtype='float8' to fit in 24GB
  - *From: MilesCorban*

- **Character LoRA training time on RTX 5090**
  - 6 hours for 3000 steps, could stop around 500-750 steps
  - *From: orabazes*

- **High/Low noise training time**
  - 3.5 hours each for high and low stages on capable hardware
  - *From: MilesCorban*

- **Multi-GPU support**
  - Diffusion-pipe supports model parallelism across multiple GPUs to pool VRAM
  - *From: mrassets*

- **WAN 2.2 14B training VRAM**
  - 24GB+ VRAM needed, blockswapping required for higher resolutions. 720p training uses ~1.1h per epoch
  - *From: Kenk*

- **Storage for RunPod template**
  - Needs ~200GB network volume for non-safetensor models (~100GB model files)
  - *From: CJ*

- **CUDA version requirement**
  - RunPod template requires CUDA 12.8, filter for this when deploying
  - *From: CJ*

- **4090 performance**
  - Can train WAN 2.2 5B in 4 batches, 4 repeats without OOM, no blockswap needed
  - *From: crinklypaper*

- **3090 local training**
  - Can train locally with diffusion-pipe, users successfully training on 3090
  - *From: crinklypaper*

- **CUDA version**
  - Must use CUDA 12.8 or greater for Wan 2.2 training template
  - *From: CJ*

- **GPU memory for video training**
  - L40S may work with block swap for 26 videos at 1280x720x81 frames, but H100 recommended
  - *From: flo1331, CJ*

- **Model storage space**
  - Wan 2.2 models take significant space, downloading 2.1 and 2.2 together uses about 150GB
  - *From: CJ*

- **Training hardware comparison**
  - H200: 4 hours, RTX Pro 6000: 4.5 hours for same training job, H200 costs 2x more
  - *From: Ruairi Robinson*

- **VRAM usage with frame buckets**
  - 16 frames uses less VRAM than higher frame counts. multiple_overlapping mode uses more VRAM than single_beginning
  - *From: Kenk*

- **Wan 2.2 model size**
  - Full model is approximately 125GB download, not the 25.6GB files some users initially got
  - *From: MatiaHeron*

- **4090 training capacity**
  - Can handle video training at 97% VRAM utilization with blockswap settings
  - *From: Kenk, MatiaHeron*

- **VRAM for video training**
  - 32GB VRAM can only handle 12 frames at 1280x720, 24GB barely enough for WAN 2.1 LoRA training
  - *From: flo1331*

- **Training speed on 5090**
  - High noise LoRA trains in 30-40 minutes on 5090 with 30-40 images
  - *From: screwfunk*

- **Training speed on 3090**
  - Video training with 56 videos at 120 frames takes ~20 minutes per epoch
  - *From: Kiwv*

- **Training speed on 4090**
  - 25 epochs (175 steps) takes about 1 hour for character training
  - *From: Critorio*

- **4080 16GB VRAM**
  - Can train 100 images at 512x512 consuming 15.4GB VRAM with blocks=16
  - *From: Luis Clement*

- **24GB VRAM**
  - Can train 81 frames at 240x416 resolution
  - *From: chancelor*

- **3060 12GB VRAM**
  - Can run dual-mode training with CPU offloading at 35s/it, 9 hours for 37 epochs with 25 images
  - *From: artificial_fungi*

- **WAN 2.2 dual training VRAM**
  - Takes significantly more VRAM than block swap training, 32GB may not be sufficient for video training
  - *From: flo1331*

- **24GB VRAM training support**
  - AI-Toolkit now supports WAN 2.2 training on 24GB cards using 3-bit Adapter LoRA
  - *From: JohnDopamine*

- **High resolution video training**
  - User successfully training 960x640 x 37 frames dataset on 48GB VRAM with 98% utilization using 32 block swap
  - *From: Persoon*

- **RTX 5090 compatibility**
  - Works fine with normal install and pytorch, xformers not required and can cause issues on Windows
  - *From: flo1331*

- **Character LoRA training on 3090**
  - 24 minutes for initial results, 1 hour 20 minutes for epoch 60 with good detail. Single LoRA approach uses 23.4GB VRAM
  - *From: screwfunk, crinklypaper*

- **4090 sufficient for ai-toolkit training**
  - Successfully trained character LoRA on first attempt without 3-bit adapter
  - *From: aipmaster*

- **Storage needs for training**
  - crinklypaper using 4TB NVMe getting full, MilesCorban recommends NAS with 30TB for experimentation
  - *From: crinklypaper*

- **Training time on RTX 3090**
  - High model: ~30 minutes, Low model: much longer. Single gen at 1284x720 takes ~20 minutes
  - *From: screwfunk*

- **Musubi dual training speed**
  - 24 minutes + 1 hour 20 minutes total on RTX 3090 for complete training
  - *From: screwfunk*

- **Minimum VRAM for character LoRA training**
  - 16GB sufficient, might work on 12GB. Dual training needs more
  - *From: flo1331*

- **RTX 5090 VRAM constraints**
  - 24GB VRAM but limited to 256 resolution for video training, adequate for image training
  - *From: Ryzen*

- **Musubi Tuner RTX 50 series support**
  - Official repo works with RTX 5090, contrary to some claims
  - *From: flo1331*

- **16GB VRAM training setup**
  - Can train with 27 frames max, needs blockswap, lower resolution, GAS=2 for memory efficiency
  - *From: flo1331*

- **24GB A5000 for Qwen training**
  - Can run Qwen with some offloading on 24GB A5000
  - *From: Guey.KhalaMari*

- **Training speed on RunPod**
  - Around $2/hour, if training takes 2 hours then $4 per LoRA is reasonable cost
  - *From: screwfunk*

- **Training time for character LoRA**
  - Both high and low sides trained in about 30 minutes each with proper settings
  - *From: CJ*

- **Training speed on A6000**
  - 0.625 samples/sec with batch size 24 at 512 resolution for image-only training. Speed varies 0.4-0.7 samples/sec depending on image/video size, frame length, LoRA dim/alpha, batch size
  - *From: MilesCorban*

- **CUDA 12.8 minimum for Blackwell cards**
  - RTX 50-series cards require CUDA 12.8 or higher
  - *From: Rego*

- **VRAM for AI Toolkit**
  - 48GB VRAM can train with batch size 24 for images, needs 128GB RAM for model loading
  - *From: MilesCorban*

- **VRAM for basic training**
  - 3090 (24GB) can train character LoRAs, 4090 should work fine
  - *From: crinklypaper*

- **RAM for Musubi**
  - Needs fast RAM and lots of it due to swapping into RAM
  - *From: MilesCorban*

- **AI Toolkit memory usage**
  - Gets full fp16 model and quantizes in memory, can crash with insufficient RAM
  - *From: MilesCorban*

- **24GB VRAM sufficient for training**
  - Can train all variants (AI-Toolkit, DP, Musubi) on 24GB VRAM with proper settings
  - *From: MilesCorban*

- **3090 training speeds**
  - 24 minutes per epoch for high noise, ~35.6 hours for 89 epochs. Around 30s/iteration for 314 videos at 256x144x81 frames
  - *From: crinklypaper*

- **H100 performance**
  - ~1.5 hours to reach 0.4 loss with fp16, batch size 40, multiple workers
  - *From: JalenBrunson*

- **4090 capabilities**
  - Can handle training up to 1500x1500 images, anything above causes hardware issues
  - *From: Gill Bastar*

- **768 res video at 33 frames**
  - Fits in 24GB with 1GB left over on 4090
  - *From: Ada*

- **1024 res at 17 frames**
  - Should work on 24GB VRAM
  - *From: Ada*

- **4 seconds of 768 resolution**
  - Barely doesn't fit on 24GB without block swap
  - *From: Ada*

- **5B model training**
  - Can run up to GAS 8 at 22GB VRAM, 10 mins per epoch at 70 steps
  - *From: crinklypaper*

- **256 res 81 frames with TREAD**
  - Takes almost exactly 20GB VRAM
  - *From: Ada*

- **VRAM for Wan 2.2 training**
  - Requires more than 44GB VRAM for training, even small datasets with 21 short videos need significant memory
  - *From: 835692458049404968*

- **Batch size limitations**
  - H200 with 141GB VRAM crashed with batch size 4, required batch size 1 for training
  - *From: TekeshiX, mamad8*

- **Training performance on 5090**
  - Around 12s/it with mixed video lengths (33-81 frames) and images at various resolutions (224px-1024px)
  - *From: mamad8*

- **Multi-GPU setup**
  - AI toolkit can run multiple jobs on different GPUs but not split single job across GPUs. Diffusion-pipe supports multi-GPU training
  - *From: fearnworks, MilesCorban*

- **VRAM for video training**
  - Need blockswap 36 for video training, would need 32-40GB VRAM for full 33-frame video training without blockswap
  - *From: flo1331*

- **Linux vs Windows performance**
  - Linux with proper Nvidia drivers (575 open) provides faster training and lower VRAM usage compared to Windows
  - *From: Kierkegaard*

- **14B model training on 12GB VRAM**
  - Possible with 640x352x17 frames, batch size 1, resulting in ~26.20s/it training speed
  - *From: CDS*

- **Full fine-tuning hardware needs**
  - RTX 3090 achieves about 15s/it for 720p images using bf16 checkpoint + fused backwards pass
  - *From: seruva19*

- **Local training VRAM requirements**
  - Never needed more than 24GB VRAM to train locally in Diffusion Pipe
  - *From: el marzocco*

- **Minimum VRAM for 14B training**
  - 24GB VRAM minimum, might be able to work with less
  - *From: Piblarg*

- **12GB VRAM sufficient for video LoRA training**
  - Can train video LoRAs on 12GB VRAM using Musubi since January
  - *From: artificial_fungi*

- **720p video training VRAM usage**
  - Batch of 30-40 720p videos uses 40-45% VRAM max, can run ComfyUI alongside
  - *From: ingi // SYSTMS*

- **RTX 6000 PRO advantages**
  - 48GB VRAM, costs £8,000, user struggles to go back to 32GB after using it
  - *From: ingi // SYSTMS*

- **VRAM for Wan 2.1 character LoRA training**
  - 18GB VRAM for 18 images at 960x960 resolution, 2-hour training time on RTX 5090
  - *From: Tachyon*

- **VRAM for Wan 2.2 training**
  - 16GB is enough for Wan 2.2 with blockswap, RTX 5090 should be plenty
  - *From: flo1331*

- **Video training VRAM needs**
  - Videos barely fit with 16GB VRAM for 16-32 frames, up to 36 frames with blockswap
  - *From: flo1331*

- **8GB VRAM limitations**
  - 8GB VRAM with 64GB CPU RAM can use blockswap for training, but probably limited to images only, not videos
  - *From: flo1331*

- **Training time estimates**
  - H200 or A6000: 1-2 hours, regular setup: 8-12 hours for character LoRA
  - *From: flo1331*

- **VRAM for Wan training without block swap**
  - 25GB VRAM for 1024x1024 images, 24GB minimum generally
  - *From: el marzocco*

- **Training time on 5090**
  - 2 hours for 12 images 1024x1024 at 20 epochs (low noise only)
  - *From: el marzocco*

- **VRAM with 8GB card**
  - Can probably train 512px images with block swapping and 64GB CPU RAM
  - *From: el marzocco*

- **Training without blockswap on 3090**
  - Can fit 512x images, bumping to 1024x for last 20% barely fits
  - *From: crinklypaper*

- **RAM usage for Wan 2.2 training**
  - 64GB RAM fills up and causes crashes with AI-toolkit, especially when using model switch every 10 steps
  - *From: const username = undefined;*

- **Training time on 5090**
  - 6 hours to train 5k steps, 20k steps would take about a day
  - *From: Ryzen*

- **3090 with 64GB RAM works for training**
  - Successfully trains with diffusion pipe on 512x resolution, sometimes 1024x
  - *From: crinklypaper*

- **GPU power consumption during training**
  - 262W usage observed during sample image processing
  - *From: Ryzen*

- **VRAM for video training**
  - 256x resolution max for videos to avoid OOM on GPUs like 5090. 512x causes stalling
  - *From: Ryzen*

- **Training speed on RTX 3090**
  - 40+ second iter times with 0.09-0.099 samples/sec for 2.2 training
  - *From: Dream Making*

- **System RAM**
  - 64GB RAM can cause OOM during training, 128GB recommended
  - *From: Charlie*

- **Video training VRAM**
  - 8GB cards insufficient for video training, images only should work
  - *From: flo1331*

- **Character training time**
  - 8-12 hours for videos with 20-25 images, 2-3 hours for images only
  - *From: flo1331*

- **High model convergence**
  - Takes less time than low model, converges around epoch 40-60
  - *From: flo1331*

- **Minimum GPU for training**
  - RTX 5090 minimum recommended, 24GB VRAM sufficient with diffusion-pipe
  - *From: Kiwv*

- **Training time with RTX 2080**
  - 4 hours for 164 epochs with small dataset
  - *From: xwsswww*

- **AI toolkit VRAM usage**
  - Requires float8 quantization for 8GB cards, very slow performance
  - *From: Kiwv*

- **Minimum 24GB VRAM for Wan training**
  - 8GB requires too much CPU offloading, shared GPU memory slows training significantly
  - *From: Kiwv*

- **5090 rental cost for LoRA training**
  - $2-3 per LoRA training session on RunPod
  - *From: Kiwv*

- **3090 training time**
  - 2+ day training runs, not 10-12 hours. Need block swapping which significantly increases time
  - *From: Kiwv*

- **5090 performance**
  - 3x faster than 3090, better energy efficiency, more VRAM
  - *From: Kiwv*

- **3090 Wan training performance**
  - 40-50 hours for 8-10 videos, 33 frames at 256px. Good for image training and inference but too slow for video training
  - *From: Kiwv*

- **5090 Wan training performance**
  - 90 minutes for 1.5k steps, 16 seconds per iteration dropping to 9-10 seconds. Uses 120GB RAM with GPU maxed out
  - *From: Ryzen*

- **3090 with 64GB system RAM**
  - Can train 100 videos and 300 images, 30-50 frames per video at 256x resolution, mostly without blockswap
  - *From: crinklypaper*

- **VRAM for batch size 2**
  - Requires unloading text encoder on some setups to fit batch size 2
  - *From: Ryzen*

- **WAN LoRA training VRAM**
  - Minimum 24GB VRAM for fp8 training. 8GB results in 45+ minutes per step
  - *From: Kiwv*

- **Qwen3-VL 8B video captioning**
  - Uses 19GB VRAM, very slow. 4B model uses 10.7GB but allocates ~50GB total
  - *From: Kiwv*

- **Training time on 5090**
  - 60 video dataset takes ~6-8 hours, 2-3x faster than 3090
  - *From: Kiwv*

- **GPU rental costs**
  - 5090 rental costs $0.50-0.90/hour, 2-3 hours needed for training
  - *From: Kiwv*

- **3090 training speed**
  - 1.5k steps per hour with 512x images, 256x videos, 38 frames. Speed varies by dataset
  - *From: crinklypaper*

- **5090 + 64GB RAM**
  - Diffusion Pipe uses 26GB VRAM with 1024x1024 images, under 24GB with 900x900 images
  - *From: el marzocco*

- **8GB GPU limitations**
  - Can train SD1.5 in 10 minutes, SDXL takes longer. Cannot train Wan 14B models, only 5B variants
  - *From: xwsswww*

- **RunPod RTX Pro 6000**
  - Used for massive LoRA training when local 3090 too slow
  - *From: Kiwv*

- ****
  - 96GB VRAM, 24k CUDA cores, best single GPU for WAN training
  - *From: Kiwv*

- ****
  - 200GB VRAM but only 16k CUDA cores, slower than 5090 but more memory
  - *From: Kiwv*

- ****
  - 32GB VRAM, 22k CUDA cores, good but VRAM limited for large training
  - *From: Kiwv*

- ****
  - Can train 256x256 LoRAs locally in half the time of higher resolution training
  - *From: oskarkeo*

- ****
  - 87GB VRAM usage for LoRA training, rarely goes above 30GB normally
  - *From: ingi // SYSTMS*

- ****
  - 87GB VRAM occupied when training 768x512x129 frame dataset
  - *From: Persoon*

- **Speedrun training times**
  - 3060 12gb: 1h 41min, 4060 ti 16gb: 56min, 3090: 36min, 5090: 14min, optimized 5090: under 10min
  - *From: artificial_fungi*

- **A100 training speed**
  - Around 20s/it on A100-80gb, 14s/it on H100 for 49 frames x 512px
  - *From: AshmoTV*

- **4090 Wan 2.1 14B training**
  - 15 secs/it on 4090, requires 64GB+ RAM and proper page file setup
  - *From: Juan Gea*

- **Windows page file**
  - Need 32GB page file instead of default 10GB to handle RAM requirements
  - *From: Juan Gea*

- **Model download storage**
  - Initial AI-toolkit setup downloads 65GB of model files
  - *From: b̶̈́͠o̶̗̅n̶̽̒k̵̽̿*

- **VRAM for 1024 square training**
  - Very heavy on VRAM, requires A100 or RTX 6000, RTX 6000 works with low VRAM mode
  - *From: dischordo*

- **Training at 512 resolution**
  - A100 or RTX 6000 works great for 512 video training
  - *From: AshmoTV*

- **High resolution training memory usage**
  - 1024 square clips bring detail but memory use is insane, may need H200 rental
  - *From: dischordo*

- **Video captioning performance**
  - 50k captions on 3090 took several days, 5090 is 2.3x faster
  - *From: spacepxl*

- **24GB VRAM for 2.2 5B lora training**
  - Can fit batch 4, GAS 8 on 24GB with 13 steps per epoch
  - *From: crinklypaper*

- **3090 sufficient for lora training**
  - Fine for starting lora training, can rent faster GPUs once you figure things out
  - *From: spacepxl*

- **Pro 6000 needed for larger batch sizes**
  - Uncensored lora needed Pro 6000 to fit proper batch size
  - *From: Kiwv*

- **4080 Super gets 3it/s on 256x256**
  - 16GB VRAM, training 256x256 images on musubi tuner
  - *From: oskarkeo*

- **480p x 81 frames doable on 4090**
  - Even 640p x 81 should work on 4090, user trains 640p x 81 on 5090
  - *From: Thom293*

- **PCIe x8 vs x4 makes big difference**
  - x8 significantly better for data transfer speed in/out of GPU
  - *From: Kiwv*

- **5090 sufficient for LTX 2 training**
  - Has enough VRAM for LTX 2 training with ai-toolkit
  - *From: Kiwv*

- **RTX 5090 training capacity**
  - Can handle 320p 1 second clips for Wan 2.2 training
  - *From: Duckers McQuack*

- **NF4 14b model size**
  - Only 7.3 GB storage requirement
  - *From: spacepxl*


## Community Creations

- **WAN LoRA conversion script** (tool)
  - Converts LoRA formats between Diffusers and ComfyUI compatibility
  - *From: mamad8*

- **Frame counting script** (tool)
  - Claude-generated script to batch inspect video frame counts for dataset preparation
  - *From: Cubey*

- **HunyClip** (tool)
  - App for preparing video dataset clips to exact frame range and size
  - *From: Marco_vdm*

- **FP8 I2V training adaptation** (script)
  - Adapted DiffSynth script to support FP8 training for I2V models
  - *From: codexq*

- **Wan control LoRAs** (lora)
  - Work-in-progress tile LoRAs for Wan 2.1 control
  - *From: spacepxl*

- **Wan training repository** (repo)
  - Training code for normal LoRA, CFG distillation, and control LoRA
  - *From: spacepxl*

- **Custom interface for zoom-out dataset creation** (tool)
  - Interface to select first input and configure speed of zoom-out for i2v training data creation, built with Claude in 4 hours
  - *From: mamad8*

- **Video comparison tool** (tool)
  - Tool for comparing video outputs, created with Claude
  - *From: Juampab12*

- **spacepxl's WAN trainer** (trainer)
  - Custom trainer for wacky experiments, owns code end to end but admits diffusion-pipe/musubi/finetrainers are much better in general
  - *From: spacepxl*

- **DiffSynth ComfyUI convert script** (script)
  - Script to convert DiffSynth output format to ComfyUI compatible format
  - *From: mamad8*

- **Steamboat Willie LoRA** (lora)
  - 1.3B LoRA trained on Steamboat Willie style, use prompt 'steamboat willie style'
  - *From: Benjaminimal*

- **Trainer Feature Comparison Matrix** (tool)
  - Comprehensive comparison of Wan training tools including features, difficulty, and performance metrics
  - *From: Benjaminimal*

- **LoRA merging script with Gradio UI** (tool)
  - Claude-generated script for merging Wan LoRAs with user interface
  - *From: JohnDopamine*

- **Gradio training interface** (tool)
  - UI for training Wan LoRAs with backend coding and downloads
  - *From: VRGameDevGirl84(RTX 5090)*

- **Blazor diffusion-pipe interface** (tool)
  - Dynamic interface for all models supported in diffusion-pipe
  - *From: Alisson Pereira*

- **Steamboat Willie style LoRA** (lora)
  - Golden era animation style trained on single public domain video
  - *From: Benjaminimal*

- **Aging timelapse LoRA** (lora)
  - Creates aging progression effects in videos
  - *From: Alisson Pereira*

- **Python app for dataset preparation** (tool)
  - Resizes images to 512x512, creates text files, uses AI for prompts, adds keywords
  - *From: VRGameDevGirl84(RTX 5090)*

- **Runpod automation scripts** (scripts)
  - Automates diffusion-pipe installation and creates basic config files
  - *From: VRGameDevGirl84(RTX 5090)*

- **Detailer/Enhancer LoRA** (lora)
  - Enhances and adds detail to people, trained on 200+ images
  - *From: VRGameDevGirl84(RTX 5090)*

- **Live wallpaper motion LoRA** (lora)
  - Creates motions similar to live wallpaper videos
  - *From: Alisson Pereira*

- **Spiral Staircase climbing LoRA** (lora)
  - 14B T2V LoRA for spiral staircase climbing concept
  - *From: Kytra*

- **90's CGI LoRA trained on ReBoot** (lora)
  - Recreates 90s computer graphics style
  - *From: Benjaminimal*

- **Lego movie LoRA** (lora)
  - Trained on ~1500 Lego movie clips, still in progress
  - *From: Cseti*

- **Diffusion-pipe interface for Wan** (tool)
  - Custom interface supporting Wan training, includes video captioning integration
  - *From: Alisson Pereira*

- **Save by steps modification for diffusion-pipe** (script)
  - Code modification to save models by step count instead of epochs
  - *From: Kytra*

- **Runpod setup scripts** (script)
  - Scripts for setting up diffusion-pipe and models on Runpod for 1.3B T2V training
  - *From: VRGameDevGirl84(RTX 5090)*

- **Updated Qwen2.5-vl-captioner** (script)
  - Updated captioning script with 24GB VRAM optimization and bug fixes
  - *From: Cseti*

- **Diffusion-pipe UI update** (interface)
  - New web interface for diffusion-pipe with model selection and improved functionality
  - *From: Alisson Pereira*

- **Fal Wan LoRA trainer** (service)
  - LoRA training service with downloadable results, passing review process
  - *From: Benjaminimal*

- **Qwen2.5 GUI Captioner** (tool)
  - All-in-one video and image batch captioner with GUI using Qwen2.5-VL, available as single exe
  - *From: Amirsun(Papi)*

- **Diffusion-pipe Gradio Configuration** (tool)
  - AI-generated Gradio page for configuring diffusion-pipe parameters, written by GROK
  - *From: H（4090）*

- **Claude After Effects automation script** (tool)
  - Custom script to automate video dataset preparation in After Effects for future-proofing
  - *From: Persoon*

- **Pan camera movement LoRA** (lora)
  - LoRA that can create 360 degree camera rotation, trained with Blender-generated consistent camera movements
  - *From: ArtOfficial*

- **Face emotion changing LoRA** (lora)
  - LoRA that changes camera angle and emotions (angry, surprised, sad, happy, neutral) from 9k 5-frame videos
  - *From: Juampab12*

- **Module-specific training modifications** (code_modification)
  - Modified diffusion-pipe scripts to train specific transformer modules rather than full blocks
  - *From: Amirsun(Papi)*

- **Fun model support for diffusion-pipe** (code_modification)
  - Added new model class and modifications to train Fun InP 1.3B model
  - *From: mamad8*

- **Video processing and scene detection tools** (scripts)
  - Tools for splitting videos, scene detection, and frame extraction for dataset preparation
  - *From: Amirsun(Papi)*

- **Two-phase captioning API** (tool)
  - Custom JoyCaption API with tag-based first pass and natural language second pass
  - *From: Kytra*

- **Resolution sorting script** (script)
  - Python script to split image datasets into resolution-based folders for better training control
  - *From: Fawks*

- **Studio Ghibli style LoRA** (lora)
  - 44MB LoRA trained on Studio Ghibli style, produces high-quality stylized animations
  - *From: Amirsun(Papi)*

- **Expression Changer LoRA** (lora)
  - LoRA for changing facial expressions using first frame as reference
  - *From: Juampab12*

- **Toon style LoRA** (lora)
  - Trained on 50 images for 1300 steps, creates cartoon-style video generations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Studio Ghibli style LoRA for 1.3B** (lora)
  - Community member made 1.3B version using shared dataset, undertrained but functional
  - *From: Piblarg*

- **Ollama Image Describer ComfyUI node** (node)
  - Custom ComfyUI node for captioning images using Ollama models
  - *From: Alisson Pereira*

- **Video processing scripts collection** (tool)
  - Collection of FFmpeg-based scripts for video dataset preparation
  - *From: Alisson Pereira*

- **VidTrainPrep** (tool)
  - Python GUI tool for video dataset preparation with multi-range clipping, cropping, and AutoCaption with Gemini AI
  - *From: lovis.io*

- **SingularUnity WAN2.1 MotionCraft** (lora)
  - Motion control LoRA trained on 5 videos initially, then 5 additional videos for more movements. Focused on cinematic motions and slow-mo
  - *From: Amirsun(Papi)*

- **Animated Logo LoRA** (lora)
  - First version LoRA for animated logos, results not perfect but functional starting point
  - *From: Alisson Pereira*

- **ComfyUI DeZoomer Nodes** (node)
  - First ComfyUI node by DeZoomer, includes video captioning functionality
  - *From: DeZoomer*

- **Garden of Words style LoRA** (lora)
  - 1.3B style LoRA trained on 'The Garden of Words' anime
  - *From: Cseti*

- **Snorrycam motion LoRA** (lora)
  - Third motion LoRA trained on Higgsfield dataset
  - *From: NebSH*

- **Redline style LoRA** (lora)
  - Motion-heavy anime style LoRA with detailed training writeup
  - *From: seruva19*

- **German Junkers Ju-87 airplane Stuka LoRA** (lora)
  - WAN 2.1 T2V 14B LoRA for German WWII dive bomber
  - *From: MisterMango*

- **Studio Ghibli style LoRA with detailed guide** (lora)
  - Includes detailed breakdown of dataset preparation and captioning methodology
  - *From: seruva19*

- **I2V morphing into plushtoy LoRA** (lora)
  - Trained on SkyReels I2V, works on base I2V also
  - *From: JohnDopamine*

- **LoRA merging Gradio app** (tool)
  - Python Gradio interface for merging LoRAs using DARE method with alpha normalization
  - *From: JohnDopamine*

- **Anime Wan merge model** (model)
  - T2V and I2V merge models that are more anime-oriented than base wan
  - *From: 852話 (hakoniwa)*

- **Cinematic detailer LoRA** (lora)
  - LoRA that enhances realism and cinematic quality, trained on 1024x1024 Flux-generated images without captions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Bowsette character LoRA** (lora)
  - Character LoRA with epoch 22 and 41 versions, includes full training breakdown
  - *From: crinklypaper*

- **Merged CausVid + enhancement LoRAs model** (model)
  - Combined CausVid v2 with face enhancement LoRAs at 0.4 strength for single-model inference
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sketch style LoRA** (lora)
  - Converts input videos to sketch style, trained using only images
  - *From: 852話 (hakoniwa)*

- **Graphic novel style LoRA** (lora)
  - 150 images, no captions, 25 epochs, successfully captures graphic novel aesthetic
  - *From: Thom293*

- **Modified DeZoomer nodes for SkyCaptioner** (node)
  - Modified py file to add SkyCaptioner support to DeZoomer video captioning nodes
  - *From: Thom293*

- **Sharpness LoRA** (lora)
  - Forces specific colors, brightness and visual effects
  - *From: Alisson Pereira*

- **Ollama ComfyUI Nodes** (node)
  - Nodes for accessing Ollama models through ComfyUI
  - *From: Alisson Pereira*

- **Video dataset preparation script** (tool)
  - Python program with ffmpeg for batch video processing - slices by scene, crops watermarks, clips to frame chunks, converts fps
  - *From: CJ*

- **Ultrawan LoRA conversion** (lora)
  - Converted from ckpt to safetensors format
  - *From: Alisson Pereira*

- **Disney 80s/90s animation LoRA** (lora)
  - Trained on 1500 screenshots and 150 videos from Beauty and the Beast, Aladdin, etc.
  - *From: notid*

- **Video cropping GUI tool** (tool)
  - Stand alone program for cropping any part of video through GUI interface
  - *From: CJ*

- **GPT batch captioning node** (node)
  - Does async calls, captions up to 20 images per request, can caption 100s of images in about 1 minute
  - *From: Fill*

- **AutoCropFaces node** (node)
  - Face-aware image cropping node in WAS Node Suite
  - *From: Faust-SiN*

- **Graphic Novel LoRA** (lora)
  - Experimental graphic novel style LoRA with training config shared
  - *From: Thom293*

- **Plushtoy Morph LoRA** (lora)
  - LoRA that morphs subjects into plush toys, trained on AnimateDiff interpolation clips
  - *From: JohnDopamine*

- **Disney character LoRA** (lora)
  - High-precision Disney character LoRA with MultiTalk compatibility, not shared due to legal concerns
  - *From: notid*

- **Vintage/Retro style LoRA** (lora)
  - 70s vintage style LoRA with LUT color grading, multiple training iterations testing captions vs trigger words
  - *From: VRGameDevGirl84(RTX 5090)*

- **Modular T2V tester workflow** (workflow)
  - Tests LORAs with original prompts, uses Qwen Omni/Instruct/Skycaptioner for new prompts, includes audio generation
  - *From: Thom293*

- **Automagic optimizer 3D graphs** (tool)
  - 3D visualization graphs showing learning rate adjustments over time for automagic optimizer
  - *From: CJ*

- **Character LoRA training configurations** (workflow)
  - TOML configuration files optimized for character training on low noise models
  - *From: multiple users*

- **Florence-based captioning script** (tool)
  - Script using Claude to create Florence-based video tagging for NSFW training
  - *From: Cubey*

- **Qwen 2.5 VL bulk captioning program** (tool)
  - Batches 16 frames at a time through clips, consolidates captions for movement capture
  - *From: CJ*

- **Live wallpaper LoRA for WAN 2.2 5B** (lora)
  - 24fps live wallpaper trained for 5000 steps at 1.3 strength
  - *From: Alisson Pereira*

- **Jinx character LoRA for WAN 2.2** (lora)
  - Arcane Jinx character LoRA with high and low noise versions
  - *From: Cseti*

- **Modified diffusion-pipe UI** (tool)
  - Added min_T, max_T and more features to diffusion-pipe UI, supports multi-GPU
  - *From: mrassets*

- **M4CROM4STI4 LoRA** (lora)
  - Highly regarded breast enhancement LoRA, though applies to all characters in frame
  - *From: Kenk*

- **Jinx character LoRA** (lora)
  - Character LoRA trained on both high and low models showing good likeness
  - *From: Cseti*

- **RunPod training template** (template)
  - Private RunPod template for WAN 2.2 training with diffusion-pipe, requires CUDA 12.8
  - *From: CJ*

- **Runpod diffusion-pipe template** (template)
  - Pre-configured environment with Python 3.12, Torch 2.7, CUDA 12.8, flash attention for Wan 2.2 training
  - *From: CJ*

- **Character LoRA testing workflow** (workflow)
  - ComfyUI workflow for auto-testing multiple combinations of high and low loras with labeled video outputs
  - *From: MilesCorban*

- **Frame counter script** (tool)
  - Python script to iterate through videos and count frames in each
  - *From: MilesCorban*

- **bash script for frame counting** (tool)
  - Uses ffprobe to count frames in video files with simple command line interface
  - *From: crinklypaper*

- **Diffusion-Pipe RunPod template** (training template)
  - Pre-configured RunPod template for WAN 2.2 LoRA training with GUI
  - *From: CJ*

- **JoyCaption batch processing workflow** (workflow)
  - ComfyUI workflow that processes directories of images and creates captions with matching txt files
  - *From: screwfunk*

- **PowerShell scripts for dataset preparation** (script)
  - Scripts to create txt files and insert trigger words at the beginning of captions
  - *From: screwfunk*

- **Golden boy style LoRA v2** (lora)
  - Improved character LoRA that works without other LoRAs, compatible with LightX2V
  - *From: crinklypaper*

- **Rocket cars dataset LoRA** (lora)
  - Motion LoRA trained on rocket car footage
  - *From: Fill*

- **Custom sigma switching nodes** (node)
  - ComfyUI nodes for automatically defining cutoff points between high/low models by observing sigma thresholds
  - *From: Alisson Pereira*

- **JoyCaption ComfyUI workflow** (workflow)
  - Automated image captioning workflow with trigger word prepending using PowerShell script
  - *From: screwfunk*

- **Qwen2.5-omni video captioner** (tool)
  - Video and image captioning tool using Qwen2.5-omni 7B-awq model
  - *From: Cseti*

- **Wan 2.2 T2V training scripts** (workflow)
  - Scripts for training single LoRA on images that works for both high and low noise models. Includes setup for latents, text encoding, and training
  - *From: screwfunk*

- **JoyCaption ComfyUI integration** (node)
  - Now split into 'JoyCaption' and 'JoyCaption Extra Options' nodes for batch image captioning
  - *From: Canin17*

- **Updated training scripts with save state** (workflow)
  - Includes --save_state, --save_state_on_train_end, --save_last_n_epochs_state 3 for resuming training
  - *From: screwfunk*

- **Anime style LoRA in progress** (lora)
  - Training to capture both visual style and animation movement of 2D anime in WAN
  - *From: crinklypaper*

- **CAME optimizer implementation** (tool)
  - More memory efficient optimizer that uses 1GB less VRAM than AdamW8bit
  - *From: flo1331*

- **Musubi training configs** (workflow)
  - Complete training configurations for video-based character training with flow shift parameters
  - *From: flo1331*

- **Auto sigma split workflow** (workflow)
  - Workflow that automatically switches sigma at 0.875 timestep
  - *From: CJ*

- **Improved workflow organization** (workflow)
  - Reorganized workflow with stacked LoRA loaders and RIFE VFI for 30fps interpolation
  - *From: screwfunk*

- **Musubi training configuration** (script)
  - Complete training script for combined image and video LoRA training
  - *From: MilesCorban*

- **High quality anime style LoRA V2** (lora)
  - Extensive training run showing progressive improvement over 89+ epochs, planned for weekend release with writeup article
  - *From: crinklypaper*

- **Ultimate deepthroat I2V LoRA** (lora)
  - NSFW LoRA trained at 211 resolution, earned 300k Civitai buzz
  - *From: Kenk*

- **Dual character experimental LoRA** (lora)
  - Attempting to train two separate characters in single LoRA to avoid blending issues
  - *From: screwfunk*

- **Wallace and Gromit style LoRA v1** (lora)
  - Anime-style motion LoRA trained on Wallace and Gromit data
  - *From: crinklypaper*

- **TREAD implementation for Wan 2.2** (tool)
  - Fast training method with 35% VRAM reduction
  - *From: Ada*

- **Video captioning and dataset preparation tool** (tool)
  - Tool with playback, cropping, splitting, auto-conversion and AI captioning
  - *From: Ada*

- **Multi-video generation subgraph workflow** (workflow)
  - ComfyUI subgraph for testing multiple LoRA settings simultaneously
  - *From: crinklypaper*

- **flo1331's character training config** (config)
  - Optimized config for character LoRA training with 33-frame videos, uses LoRA+, CAME optimizer, GAS=4
  - *From: flo1331*

- **Kinestasis stop motion LoRA** (lora)
  - LoRA trained for stop motion kinestasis effect, described as hard concept for model to learn
  - *From: Cseti*

- **Gurren Lagann anime style LoRA** (lora)
  - Extensively trained style LoRA with 117.5K+ steps on high model, detailed training process documentation
  - *From: crinklypaper*

- **Blade Runner cinematography LoRA** (lora)
  - Style LoRA for Blade Runner cinematography and themes
  - *From: Kierkegaard*

- **Frame counting script** (tool)
  - Python script to count frames in video datasets and identify problematic files
  - *From: DennisM*

- **Custom ChatGPT for NSFW captioning** (tool)
  - Custom GPT setup that can handle NSFW content for image/video captioning
  - *From: crinklypaper*

- **Animated Logo Factory LoRA** (lora)
  - LoRA for creating animated logos, creator plans to make version for Wan 2.2
  - *From: Alisson Pereira*

- **Diffusion Pipe interface improvements** (tool)
  - Plans to work on new interface using NextJS/VueJS/SvelteJS or ComfyUI nodes, with ai-toolkit style manual parameter editing and automatic captioning tools
  - *From: Alisson Pereira*

- **CuteCaption** (tool)
  - Dataset suite/caption editor with JoyCaption built in for captioning training data
  - *From: shotgun messiah*

- **RamTorch with block swap implementation** (tool)
  - Block swap implementation being developed for higher resolution training
  - *From: Alisson Pereira*

- **Goldenboy LoRA** (lora)
  - Retro 90s anime style LoRA for Wan 2.2
  - *From: crinklypaper*

- **Gurren Lagann LoRA** (lora)
  - Anime style LoRA with some motion issues
  - *From: crinklypaper*

- **Raven Teen Titans LoRA** (lora)
  - Character + style LoRA trained on only 87 images
  - *From: crinklypaper*

- **Art Official Studio Docker** (tool)
  - All-in-one Docker solution wrapping inference/training tools with auto-downloading
  - *From: ArtOfficial*

- **Gurren Lagann anime style LoRA** (lora)
  - Style LoRA that captures anime style with character Yoko easily promptable through characteristic descriptions
  - *From: crinklypaper*

- **Gemini-based captioning ComfyUI workflow** (workflow)
  - Automated workflow using Florence2 for cropping and Gemini 2.5 Pro for natural language captioning of training datasets
  - *From: Muon*

- **Wan 2.2 GUI** (tool)
  - GUI interface for Musubi Tuner Wan 2.2 training
  - *From: Tachyon*

- **Video dataset automation scripts** (workflow)
  - Scripts for converting long-form video to captioned training data
  - *From: Muon*

- **Top Gun style LoRAs** (lora)
  - Multiple style LoRAs for different Top Gun scenes (orange-tinted carrier, ground scenes, daytime combat)
  - *From: el marzocco*

- **Random pose generator for QWEN 2509** (tool)
  - Generates random poses for character LoRA datasets with predefined prompts
  - *From: Tachyon*

- **JoyCaption workflow for batch captioning** (workflow)
  - ComfyUI workflow to caption entire folders automatically
  - *From: el marzocco*

- **Motion dataset scraper** (tool)
  - Python script to scrape 220 effects & cameras from Higgsfield
  - *From: NebSH*

- **Gurren Lagann anime LoRA** (lora)
  - Multi-character anime style LoRA with detailed training methodology
  - *From: crinklypaper*

- **Caption generation script** (tool)
  - Python script for generating captions with video navigation using arrow keys
  - *From: Kiwv*

- **Gemini-powered captioning app** (tool)
  - Drop videos and images, uses Gemini Pro 2.5 to caption them, checks existing caption quality, exports as zip batch
  - *From: crinklypaper*

- **Video processing scripts** (tool)
  - Python scripts to clip videos to 7.5 seconds and annotate them for training
  - *From: Kiwv*

- **Caption editor** (tool)
  - In development to make captioning process easier
  - *From: shotgun messiah*

- **LoRA Captioner web app** (tool)
  - Web app using Gemini API for captioning images/videos with custom instructions, editing and download capabilities
  - *From: crinklypaper*

- **Modified ai-toolkit for FFLF training** (tool)
  - Modified ai-toolkit to handle First-Frame-Last-Frame dataset training
  - *From: mamad8*

- **Automated dataset creation script** (tool)
  - Google search scraper that auto-crops, captions with moondream, and prepares training data
  - *From: oskarkeo*

- **LoRA Captioner Tool** (tool)
  - Web app for captioning training images/videos with Gemini and Qwen support
  - *From: crinklypaper*

- **Scooby Doo Mystery Inc Style LoRA** (lora)
  - Style LoRA trained on 27k/17k steps for high/low, includes character recognition
  - *From: crinklypaper*

- **Training package with custom tools** (workflow)
  - Complete training setup for low VRAM/RAM with three LoRAs, configs and custom tools
  - *From: artificial_fungi*

- **Character LoRAs showcase** (lora)
  - Epic video compilation of multiple characters from Scooby-Doo universe
  - *From: avataraim*

- **WanVideoWrapper workflow examples** (workflow)
  - Context window workflows for multi-prompt generation
  - *From: avataraim*

- **Style comparison methodology** (workflow)
  - Visual comparison system for high/low model interaction effects
  - *From: crinklypaper*

- **Enhanced captioning tool with ComfyUI integration** (tool)
  - Extended captioner with ComfyUI integration to generate images from captions and verify they make sense for training
  - *From: Brooks*

- **Updated captioning tool with offline HF models** (tool)
  - Captioning tool that works with offline HuggingFace qwen models and multiple Gemini model selections
  - *From: crinklypaper*

- **Custom dataset prepper with vibecode** (tool)
  - Dataset preparation tool for character training with specific captioning methodology
  - *From: oskarkeo*

- **5B lora model** (lora)
  - Style lora trained on 2.2 5B model with maxed VRAM usage
  - *From: crinklypaper*

- **Seruva's Ghibli LoRA** (lora)
  - Creator documents training process for each LoRA made
  - *From: Piblarg*
