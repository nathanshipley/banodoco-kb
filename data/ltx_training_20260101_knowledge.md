# Ltx Training Knowledge Base
*Extracted from Discord discussions: 2026-01-01 to 2026-02-01*


## Technical Discoveries

- **LTX v1 LoRAs work with LTX-2**
  - Existing LTX v0.96/v1 LoRAs are compatible with LTX-2, visually anyway but audio doesn't get affected
  - *From: Fill*

- **LTX-2 training is significantly faster than other models**
  - What used to take over 20 hours on Wan2.2 now takes 1 hour on LTX-2. Training is lightning fast compared to previous video models
  - *From: oumoumad*

- **Training stalls after 1.5k steps with minor changes**
  - Character training progresses quickly up to 1.5k steps then progress becomes very minor, may need higher learning rate
  - *From: boorayjenkins*

- **5x-10x training speedup possible**
  - Reference to hydraulic press LoRA trained at home in 15 hours with significant speedup methods
  - *From: yi*

- **FP8 vs BF16 makes huge difference in quality**
  - Training on FP8 produces worse results, using BF16 for inference shows huge quality improvement
  - *From: NebSH*

- **Less character bleeding compared to Wan**
  - LTX-2 doesn't seem to overfit other characters like Wan does
  - *From: NebSH*

- **LTX-2 converges faster than LTX-1**
  - Model seems to converge in 1500 steps vs 2000 steps for LTX-1
  - *From: NebSH*

- **Multi-character training in single LoRA works**
  - Successfully trained 2 characters in one LoRA, though using them separately in generation causes mixing
  - *From: NebSH*

- **Sequential training approach works well**
  - 5000 steps on video data -> 2000 steps on image data -> 1400 steps on NSFW image data produces good results
  - *From: crinklypaper*

- **Audio-only training modifications improve LoRA**
  - Excluding cross attention keys between audio and video from trained LoRA improved results while keeping visual and audio concepts intact
  - *From: mamad8*

- **Model learns background music quickly**
  - After adding clips with same background music captioned as 'background music: ...', model learned the songs after just 2k steps
  - *From: dischordo*

- **Training order can be video first then images or images first then video - both work**
  - Images kick start style pickup much faster, but videos are better for voice training plus style
  - *From: crinklypaper*

- **Image-only training for animated styles is insufficient**
  - Gets the look somewhat but movement creates issues, probably because base model is missing that context
  - *From: crinklypaper*

- **Mixed video+image training produces best results**
  - Video + image training had best results compared to video only, image only, or image + video
  - *From: crinklypaper*

- **AI Toolkit supports mixed image+video training for LTX2**
  - Can have separate datasets - mark image datasets as 1f and it works fine. Bug that treated 1f datasets as i2v was fixed
  - *From: MOV*

- **LTX2 can learn character voices from small amounts of data**
  - At 1000 steps was already getting correct voice, even accidental 2-3 clips with audio taught Japanese accent
  - *From: Choowkee*

- **Scene splitter script in LTX trainer works better than pyscene**
  - Built-in scene splitter is quite nice for preparing datasets
  - *From: crinklypaper*

- **LTX2 is exceptionally good at learning audio/voices**
  - Multiple users report impressive voice cloning results, with one user saying their 1500 sample LoRA sounds exactly like their wife
  - *From: NC17z*

- **Increasing FPS can improve video generation quality**
  - User found that simply increasing fps made their generation work better
  - *From: crinklypaper*

- **LTX2 captures physical motion well**
  - User reports that LTX captures jiggling motion that WAN needed specific training for
  - *From: crinklypaper*

- **Simple 'Anime style' caption separates character from style effectively**
  - Just like with WAN, adding 'Anime style' to captions helps separate character learning from style learning
  - *From: Choowkee*

- **Training can be done on 4090 with good performance**
  - Successfully trained on RTX 4090 at 5.23 sec/iter with no layer offloading, cache text embeddings, low vram setting
  - *From: chancelor*

- **Large datasets require significant cache space**
  - When caching text embeddings, each dataset item creates 376mb files, leading to 300GB+ storage needs for large datasets
  - *From: avataraim*

- **768x768 training resolution shows better results than 512x512**
  - Training at 768 resolution produces clearer, more detailed motion learning compared to lower resolutions, though requires more VRAM
  - *From: dischordo*

- **Higher FPS training reduces motion artifacts**
  - Training at 32fps shows fewer hand distortions and motion artifacts compared to lower fps training, even when generating at 24fps
  - *From: MOV*

- **Custom cropping centered on motion area improves training**
  - Cropping training data to squares centered on the area of motion works better than letting the model resize whole clips
  - *From: dischordo*

- **Float8 with 4-bit text encoder uses 24-28GB VRAM**
  - Training configuration allowing LTX2 training on consumer cards with reasonable VRAM usage
  - *From: crinklypaper*

- **Audio normalize feature fixes pitch distortion**
  - Using audio normalize in AI Toolkit fixed high-pitched voice distortion that occurred from FPS mismatches
  - *From: crinklypaper*

- **IC LoRA can perform head swapping in videos**
  - Identity Consistent LoRA trained with 200+ paired video samples can swap heads across video sequences
  - *From: Alisson Pereira*

- **Musubi-Tuner has much smaller cache files than AI-Toolkit**
  - AI-Toolkit creates 360MB cache files per text encoder while Musubi-Tuner creates only 30MB cache files
  - *From: avataraim*

- **Recent Musubi-Tuner commits broke training**
  - Multiple users confirmed that newer commits fail to train properly, with bad loss curves and poor results
  - *From: Choowkee*

- **Older Musubi-Tuner commit works properly**
  - Commit 90e1559a7c73ff41ade497605e1f5b1850270711 produces proper loss curves and good results
  - *From: Choowkee*

- **Block swapping affects VRAM usage significantly**
  - 30 blockswap uses 18.6GB max VRAM, 26 blockswap uses 21.6GB, 24 blockswap uses 22.9GB for 512res 121f videos
  - *From: MOV*

- **High pitch voice issue can be fixed with audio preserve pitch setting**
  - Setting fps to match dataset and enabling audio preserve pitch fixed high pitch voices within 500 steps
  - *From: crinklypaper*

- **SDPA attention works better than Sage attention for training**
  - User switched from Sage attention to SDPA and got better training performance
  - *From: Choowkee*

- **LTX2 base resolution is 1280x720**
  - Model metadata shows modelspec.resolution: 1280x720 as base resolution
  - *From: Choowkee*

- **Musubi fork provides faster training than AI-toolkit**
  - User reported 2 it/s on 256x256x169 with Musubi vs 3 it/s with AI-toolkit, but Musubi is actually faster overall
  - *From: JonkoXL*

- **Audio-only training works with proper setup**
  - Successfully trained voice cloning using only audio files with 5 sec duration
  - *From: Gleb Tretyak*

- **Spatial outpainting possible with IC LoRA**
  - User trained IC LoRA by removing parts of videos (making them black) as reference and original videos as target
  - *From: oumoumad*

- **Audio LoRA training successful with very small dataset**
  - Successfully trained with only 20 audio files, each 5 seconds long with simple phrases
  - *From: Gleb Tretyak*

- **YouTube shorts effective for training data**
  - YouTube shorts are great for cropping out everything but the person, creates better focus for training
  - *From: Jonathan Scott Schneberg*


## Troubleshooting & Solutions

- **Problem:** Fal trainer showing internal server error but training actually succeeds
  - **Solution:** Check logs for lora_file: url= line to download the trained LoRA, training didn't actually fail
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** Audio causes OOM during preprocessing
  - **Solution:** Need to cleanup text encoder in preprocess script before moving to latent caching
  - *From: fearnworks*

- **Problem:** Triton dependency prevents Windows training
  - **Solution:** Can use triton-windows manually installed, though official trainer requires Linux
  - *From: AshmoTV*

- **Problem:** Slow motion effect when generating longer videos than training dataset
  - **Solution:** Include variation in dataset with same effect at different speeds and durations, use prompts mentioning timing like 'quick burst'
  - *From: oumoumad*

- **Problem:** OOM on dataset preprocessing with 24GB VRAM
  - **Solution:** Need higher VRAM cards or use CPU preprocessing (very slow - 6 minutes for 3 second clip)
  - *From: crinklypaper*

- **Problem:** Quantization error with fp8 model
  - **Solution:** Set quantization to 'null' if using fp8 model since it's already fp8
  - *From: crinklypaper*

- **Problem:** Empty conditions folder during preprocessing
  - **Solution:** Change output_file = output_path / output_rel_path to output_file = output_path /'dataset'/ output_rel_path.name - issue with pathlib handling relative paths when folder named 'dataset'
  - *From: iGoon*

- **Problem:** Out of memory on longer frame training
  - **Solution:** Train on 5-6 seconds instead of 20 seconds, even on H100. 500 frames causes OOM
  - *From: NebSH*

- **Problem:** T2V produces floating heads and weird anatomy while I2V works fine
  - **Solution:** Consider adding high quality images to training data to improve T2V performance
  - *From: daring_ls*

- **Problem:** Audio captioning for engine sounds mixed with speech
  - **Solution:** Avoid putting descriptive text like 'There is a reving engine' as character will often say it literally
  - *From: vanhex*

- **Problem:** Black screen LoRA from training without samples
  - **Solution:** Take at least one sample at 250 steps to make sure it's not broken
  - *From: dischordo*

- **Problem:** Audio error 'Invalid argument: avcodec_send_frame() NaN/+-Inf' after ~6000 steps
  - **Solution:** Error goes away when removing audio but video becomes black. Doesn't happen at 5600 steps checkpoint
  - *From: Lumori*

- **Problem:** Multiple character voices combining into one
  - **Solution:** Need to tag each character specifically in SPEECH prompts and separate them properly in dataset
  - *From: Lumori*

- **Problem:** Slow training speed with full offloading
  - **Solution:** Reduce transformer offloading - went from 9s/it to 5s/it by offloading only 20% instead of 100%
  - *From: Critorio*

- **Problem:** AI Toolkit convergence issues with newer versions
  - **Solution:** Roll back to first release that supported LTX2 (Jan 13) for normal convergence
  - *From: Choowkee*

- **Problem:** Training on videos longer than expected frames
  - **Solution:** AI toolkit takes first 121f (or specified amount) and doesn't require exact length
  - *From: MOV*

- **Problem:** CUDA 13.0 compatibility issues with libnvrtc-builtins
  - **Solution:** Update cuda-toolkit from 12.8 to match the requirements
  - *From: burgstall*

- **Problem:** Poor training results even after 2000+ steps
  - **Solution:** Ensure source videos are proper aspect ratios (divisible by 32) to avoid cropping important content
  - *From: BrainNXDomain*

- **Problem:** Cache latent or additional resolution checkboxes causing issues
  - **Solution:** Disabling these checkboxes resolved training problems
  - *From: Mazrael.Shib*

- **Problem:** High loss starting above 1.0 and not dropping quickly
  - **Solution:** This indicates potential dataset or settings issues - healthy runs should start lower and drop gradually
  - *From: Choowkee*

- **Problem:** Running out of disk space with text embedding cache
  - **Solution:** Either get larger drive, split training into multiple sessions, or use unload text encoder method
  - *From: chancelor*

- **Problem:** High-pitched audio in generated videos
  - **Solution:** Set correct FPS in dataset settings and enable audio normalize feature, or use Audio Preserve Pitch option
  - *From: MOV*

- **Problem:** Poor I2V results when only training T2V
  - **Solution:** Add the same dataset twice, with I2V enabled on one copy to train both modes simultaneously
  - *From: MOV*

- **Problem:** Cache not updating after changing I2V settings
  - **Solution:** Delete _latent_cache and _t_e_cache folders in dataset directory to force recaching
  - *From: MOV*

- **Problem:** OOM errors on 5090 with 64GB RAM
  - **Solution:** Quantize transformers to float8 and set offload to 100%
  - *From: Jonathan Scott Schneberg*

- **Problem:** WSL2 Docker memory limitations on Win11 Home
  - **Solution:** Update WSL2 to break 100GB vxhd limitation, avoid Docker if possible and use direct WSL2 installation
  - *From: metaphysician*

- **Problem:** High pitch voices in generated audio
  - **Solution:** Set fps to same as dataset and enable audio preserve pitch
  - *From: crinklypaper*

- **Problem:** Training freezes when VRAM exceeds capacity
  - **Solution:** Some samples go up to 24GB and freeze, adjust block swap settings
  - *From: avataraim*

- **Problem:** Bad training results with newer Musubi-Tuner versions
  - **Solution:** Roll back to commit 90e1559a7c73ff41ade497605e1f5b1850270711
  - *From: Choowkee*

- **Problem:** OOM errors during training
  - **Solution:** Set blocks_to_swap to 5 and test what works for your setup
  - *From: avataraim*

- **Problem:** Sage attention causing training issues
  - **Solution:** Do not use sage attention during training, use SDPA instead
  - *From: Benjimon*

- **Problem:** Training results very poor with unstable repository versions
  - **Solution:** Use specific stable commit: 2b77b23defc40bea39ee21680fa3ab73765ab3bf
  - *From: avataraim*

- **Problem:** High VRAM usage when training with audio+video
  - **Solution:** Train video-only first to test, audio training requires more VRAM management
  - *From: avataraim*

- **Problem:** Poor voice cloning results
  - **Solution:** Need 20-30+ videos minimum for good voice cloning, not just 10 videos
  - *From: JonkoXL*

- **Problem:** Chrome occupying VRAM during training
  - **Solution:** Disable GPU acceleration in Chrome to free up VRAM
  - *From: scf*

- **Problem:** AdamW optimizer causing issues
  - **Solution:** User fixed training by not using AdamW optimizer
  - *From: Jimi*

- **Problem:** Musubi-tuner crashes with OOM on validation sampling
  - **Solution:** User gave up and switched to Simpletuner on Linux
  - *From: Gleb Tretyak*

- **Problem:** Simpletuner config path errors
  - **Solution:** Fix paths in config JSON - replace system-specific paths like '/home/gleb/.simpletuner/config/lycoris_config.json' with your own system paths
  - *From: Gleb Tretyak*

- **Problem:** LoRA trained for 4000 steps has basically 0 effect at 256 resolution
  - **Solution:** No solution provided - user asking if LTX2 can't be trained on 256 res, previously worked at 512 res
  - *From: protector131090*


## Model Comparisons

- **LTX-2 vs Wan2.2 training speed**
  - LTX-2 is dramatically faster - 1 hour vs 20+ hours for similar datasets
  - *From: oumoumad*

- **Character likeness LTX-2 vs Wan2.2**
  - Character likeness is less good than Wan 2.2, may need more steps or different precision
  - *From: NebSH*

- **128 rank vs 32 rank LoRAs**
  - 128 rank (ltx-trainer) yields nicer results without AI-ish chrome/metal particles, 32 rank less biased to texture changes
  - *From: oumoumad*

- **LTX-2 vs LTX-1 training speed**
  - LTX-2 is approximately 10x faster to train than WAN, but more sensitive
  - *From: crinklypaper*

- **FP16 vs FP8 generation quality**
  - FP16 always produces better results - smoother movement, higher quality, more details. Difference is like Veo3.1 vs Veo3.1 fast
  - *From: Tonon*

- **Dataset size impact**
  - Smaller datasets (108 videos) seem to converge faster than larger ones (830+ videos). Larger datasets may be too restrictive and slow down learning
  - *From: NebSH*

- **Official LTX trainer vs AI Toolkit**
  - Official trainer is better but annoying to use, AI Toolkit easier but came out recently so may have bugs
  - *From: Kiwv*

- **Musubi tuner vs AI Toolkit for LTX2**
  - Musubi faster (2it/s vs slower), 1.3it/s for pure video training
  - *From: Choowkee*

- **WAN 2.2 vs LTX2 training**
  - WAN seemed simpler (crop, keyword, train, ship), LTX2 more complex but can learn and generalize intelligently
  - *From: Kiwv*

- **Distilled vs base LTX2 model**
  - Distilled is fried with amalgamation and prompt deviation, base model has no issues
  - *From: Kiwv*

- **LTX2 vs WAN for audio learning**
  - LTX2 is significantly better at learning voices and audio
  - *From: Choowkee*

- **Different FPS settings for 2D content**
  - 24fps performed better than 48fps-60fps for 2D content in testing
  - *From: protector131090*

- **AI-toolkit vs Musubi tuner fork**
  - Musubi tuner provides more control over parameters and is faster for LTX2 training
  - *From: Choowkee*

- **Video+image datasets vs image-only**
  - Video datasets produce much more realistic results than image-only, especially for realism
  - *From: ZeusZeus (RTX 4090)*

- **Musubi tuner vs AI Toolkit speed**
  - Musubi tuner achieves 2.9s/iter with 10% offload vs slower performance in AI Toolkit
  - *From: scf*

- **Cache sizes: Musubi vs AI Toolkit**
  - Musubi produces cache files ~30MB vs AI Toolkit's 300+MB, 10x smaller
  - *From: avataraim*

- **Musubi-Tuner vs AI-Toolkit cache size**
  - Musubi-Tuner cache is 12x smaller (30MB vs 360MB per file)
  - *From: avataraim*

- **Musubi-Tuner vs AI-Toolkit speed**
  - Musubi-Tuner is faster: 11s/it vs 15s/it on same dataset
  - *From: MOV*

- **Musubi-Tuner vs AI-Toolkit for specific dataset**
  - Musubi-Tuner at 800 steps wins in both quality and audio for this test dataset
  - *From: avataraim*

- **Training samples vs ComfyUI results**
  - Samples during training are MUCH worse than actual LoRA performance in ComfyUI
  - *From: NebSH*

- **Musubi vs AI-toolkit for voice training**
  - Musubi produces better voice cloning results - good results in 800 steps vs poor results in AI-toolkit at 2K steps
  - *From: avataraim*

- **LTX2 vs WAN for eye generalization**
  - WAN 2.1 handles anime eye styles better than LTX2 on same dataset
  - *From: Choowkee*


## Tips & Best Practices

- **Use varied dataset for motion effects to avoid slow-mo bias**
  - Context: When training effect LoRAs, include same effect at different speeds and durations
  - *From: oumoumad*

- **Avoid mixing closeups and wide shots in single dataset**
  - Context: Models can get confused seeing closeups and wide views as separate subjects
  - *From: oumoumad*

- **Use first_frame_conditioning_p: 1.0 for product training**
  - Context: Key parameter for training LoRAs on objects like cars, specify only one frame for bucket preprocessing
  - *From: oumoumad*

- **2000 steps can cause overfitting with small datasets**
  - Context: Better results between 1000-1500 steps unless dataset has 24+ varied examples
  - *From: oumoumad*

- **Negative prompts are very important in LTX-2**
  - Context: Every word has impact, good for fixing issues and minimizing bias, unlike previous LTXV where negative prompts felt ineffective
  - *From: oumoumad*

- **Use BF16 instead of FP8 for better quality**
  - Context: FP8 training produces worse character likeness, BF16 inference shows huge quality difference
  - *From: NebSH*

- **Use detailed captions with shot-by-shot breakdown for longer videos**
  - Context: For videos 8-13 seconds with multiple actions or cuts, include overall description, then shot-by-shot breakdowns with audio description
  - *From: fearnworks*

- **Test captioning concept without LoRA first**
  - Context: Find prompts that get in vague ballpark to help identify right captioning approach
  - *From: fearnworks*

- **Use custom sigmas and specific sampler settings for I2V**
  - Context: Use undistilled model with distill LoRA at 0.5-0.6 strength, DPM SDE sampler, custom sigmas, 1.0 denoise strength, sometimes reduce precompression
  - *From: dischordo*

- **Checkpoint often and test locally instead of sampling during training**
  - Context: Sampling during training never looks right
  - *From: crinklypaper*

- **Tag music uniquely with actual song names rather than generic 'background music'**
  - Context: Generic tags cause different songs to mix together, especially bad if in different keys
  - *From: dischordo*

- **Normalize audio levels to around -7db**
  - Context: Model picks up full audio range, good level for training
  - *From: dischordo*

- **Include dialogue in Japanese as romaji in captions**
  - Context: Don't translate to English, write as 'sou desu ne' etc. and specify language
  - *From: crinklypaper*

- **Use diverse clips for concept training**
  - Context: Too few or similar clips cause model to learn unintended specifics like faces, expressions, colors
  - *From: SmaX*

- **Start with 512 res and 65 frames or 256 res and 121 frames for video**
  - Context: Good starting points for LTX2 video training
  - *From: MOV*

- **Don't overtrain - less steps can be better**
  - Context: User found 1500 step LoRA performed better than 6000 step version, suggesting overtraining can hurt results
  - *From: NC17z*

- **Use detailed captions for LTX2**
  - Context: LTX2 may need more detailed captions compared to other models due to DiT-based architecture
  - *From: Mazrael.Shib*

- **Mix images and videos for best results**
  - Context: 500 images + 100 videos combination works well for learning both style and character
  - *From: avataraim*

- **Consider rank size relative to dataset size**
  - Context: For 20 videos, rank 32 might be too much and could cause overfitting instead of generalization
  - *From: Kiwv*

- **Use keyframes for smoother motion**
  - Context: Multiple close keyframes with sufficient frames between them produces smoother results
  - *From: JUSTSWEATERS*

- **Train both T2V and I2V modes for best results**
  - Context: When planning to use LoRA for both text-to-video and image-to-video generation
  - *From: MOV*

- **Match training FPS to your dataset FPS**
  - Context: Prevents audio pitch distortion and timing issues during generation
  - *From: MOV*

- **Use rank 32 for most character LoRAs**
  - Context: Balance between learning capacity and overfitting for identity/character training
  - *From: MOV*

- **Pad frames minimally to fit bucket sizes**
  - Context: When preparing video datasets, pad maximum 2-3 frames to fit bucket requirements
  - *From: crinklypaper*

- **Generate lipsynced I2V for character training instead of interpolating stills**
  - Context: Preserves natural lipsync when training with audio clips
  - *From: MOV*

- **Use lower rank for character training with images**
  - Context: To avoid diminished movement and talking ability, try rank 4-8 instead of higher values
  - *From: Guey.KhalaMari*

- **Train character with multiple people in final stage**
  - Context: To counter the issue where LoRA makes everyone look like the trained character
  - *From: Guey.KhalaMari*

- **Don't rely on training samples for quality assessment**
  - Context: Samples are much worse than actual LoRA performance in ComfyUI
  - *From: NebSH*

- **Use 3 second clips around 73 frames for good results**
  - Context: For training with audio, this duration works well
  - *From: crinklypaper*

- **Use natural language captions, not keyword-based ones**
  - Context: For LTX2 training with LLM-based text encoders
  - *From: Kiwv*

- **Caption as if describing for the original LTX2 dataset**
  - Context: Better results than artificial keyword-style captions
  - *From: Kiwv*

- **Use consistent keywords throughout dataset**
  - Context: Don't mix 'car', 'automobile', 'racer' - pick one term and stick with it
  - *From: LTX Lux*

- **Audio clips should be 24fps to avoid audio issues**
  - Context: When preparing video datasets with audio
  - *From: crinklypaper*

- **Caption audio naturally at end of video captions**
  - Context: Use format like 'character says "dialogue"' and describe background sounds
  - *From: crinklypaper*

- **Aim for overtraining rather than undertraining**
  - Context: Model learns extremely slowly, need 150+ repeats per data point on average
  - *From: dischordo*

- **Use GUI for Simpletuner on Linux**
  - Context: When using Simpletuner
  - *From: Kiwv*

- **Sometimes editing config file directly is easier than using complex UI**
  - Context: When dealing with complex training interfaces
  - *From: scf*

- **Use YouTube shorts for training datasets**
  - Context: For character training - allows cropping out everything but the person for better focus
  - *From: Jonathan Scott Schneberg*


## News & Updates

- **LTX-2 trainer supports multiple training modes**
  - Standard LoRA Training (Video-Only), Audio-Video LoRA Training, Full Model Fine-tuning, In-Context LoRA (IC-LoRA) Training
  - *From: NebSH*

- **Fal.ai LTX-2 trainer available but image-only**
  - Fal trainer currently only supports images, not video training
  - *From: NebSH*

- **Audio training toggle available but needs tweaking**
  - Audio training option exists but default settings need adjustment, being worked on
  - *From: Dragonyte*

- **AI Toolkit now officially supports LTX-2 LoRA training**
  - Ostris announced official support and trained Carl Sagan LoRA on RTX 5090
  - *From: Arts Bro*

- **AI Toolkit added I2V training support**
  - Ostris pushed I2V training capabilities to AI Toolkit
  - *From: fearnworks*

- **VRAM usage reduction in AI Toolkit**
  - Recent commit allows proper caching of latents, drastically reducing VRAM usage during training
  - *From: MOV*

- **LTX2 training tutorial coming soon**
  - Finishing touches on tutorial, hope to have live in a day or so
  - *From: LTX Lux*

- **Official LTX2 training tutorial released**
  - Training Custom LoRAs with LTX-2 (Full Workflow) on YouTube
  - *From: LTX Lux*

- **Planned AI Toolkit improvements**
  - PRs coming for audio-only training, video+image training together, prodigyscheduler_free optimizer, multiple dataset folders with balancing, tensorboard logging
  - *From: mamad8*

- **Musubi tuner fork fixed audio-only datasets**
  - Audio-only training with dummy video was broken but has been fixed
  - *From: Gleb Tretyak*

- **LTX model had git commit pulled back causing re-downloads**
  - Recent git commit in LTX repo was reverted, causing users to see updates and re-download all files
  - *From: BrainNXDomain*

- **Musubi-Tuner LTX-2 fork available**
  - Fork by AkaneTendo25 supports LTX Video 2 training
  - *From: avataraim*

- **Recent Musubi-Tuner updates broke training**
  - Updates from last few days caused training failures, author working on fixes
  - *From: Choowkee*

- **Koyha working on official LTX training support**
  - Official support for LTX training coming to Musubi-Tuner soon
  - *From: JonkoXL*


## Workflows & Use Cases

- **Music video generation using camera control LoRAs**
  - Use case: Generate start images then run with LTXV 0.97 distilled 13B using randomly assigned camera control LoRAs
  - *From: burgstall*

- **Character dataset creation from interviews**
  - Use case: Use pyscene to extract clips from interviews - 10 min video becomes ~177 training clips
  - *From: NebSH*

- **Video-first then image training**
  - Use case: Train 5000 steps on videos first to get motion/sound, then continue with images to improve style accuracy
  - *From: crinklypaper*

- **Sequential dataset training**
  - Use case: 5000 steps video -> 2000 steps images -> 1400 steps specific content images for comprehensive character/style learning
  - *From: crinklypaper*

- **AMV-style video-to-video training**
  - Use case: Extract keyframes from AMV, repeat first frame until scene changes to create reference video for transition training
  - *From: Alisson Pereira*

- **Multi-stage training approach**
  - Use case: Train on videos first then switch to images, or vice versa, by stopping and resuming from checkpoint
  - *From: crinklypaper*

- **Character + environment training**
  - Use case: Train room separately with token, then person in room with both tokens, crop different shots for variety
  - *From: MOV*

- **Gemini captioning workflow**
  - Use case: Use Gemini with custom tool to caption video datasets including Japanese dialogue
  - *From: crinklypaper*

- **Image + Video dataset combination**
  - Use case: Training both style and character simultaneously using 500 images + 100 videos with audio
  - *From: avataraim*

- **Head swap IC LoRA training**
  - Use case: Training for face swapping by using head-swapped first frames with Humo processing at 0.7 denoise
  - *From: Alisson Pereira*

- **Multi-keyframe generation**
  - Use case: Using 4 keyframes with 25fps processing and 121 frames for smooth character motion
  - *From: JUSTSWEATERS*

- **Whisper + Qwen-VL captioning workflow**
  - Use case: Automated video captioning for training with speech transcription and visual description
  - *From: MOV*

- **IC LoRA head swap training**
  - Use case: Train identity-consistent LoRA for video head swapping using paired video samples
  - *From: Alisson Pereira*

- **Mixed dataset training**
  - Use case: Training with both videos (512x512, 73 frames) and images (768x768) for character LoRAs
  - *From: avataraim*

- **Character training with diverse dataset**
  - Use case: Using 94 images and 59 videos with audio for character LoRA, achieved good results at 3.5k-5k steps
  - *From: crinklypaper*

- **Audio-only training with Simpletuner**
  - Use case: Voice cloning using only audio files
  - *From: Gleb Tretyak*

- **Spatial outpainting with IC LoRA**
  - Use case: Remove parts of videos (make black) as reference, use originals as target for outpainting training
  - *From: oumoumad*

- **Audio 2 Audio with voice LoRA**
  - Use case: Provide audio source of intended performance and apply voice LoRA on top, using Kijai's node with audio trained on black frames and Video/Audio LoRA
  - *From: Guey.KhalaMari*

- **Repurposing character LoRAs for voice only**
  - Use case: Using existing character LoRAs but only extracting their voice component with Kijai's node
  - *From: Guey.KhalaMari*


## Recommended Settings

- **Learning rate**: 0.0002
  - Used successfully for tear effect LoRA training
  - *From: oumoumad*

- **Steps**: 1000-1500
  - Better results than 2000 steps unless dataset is very varied (24+ examples)
  - *From: oumoumad*

- **Resolution**: 512x different buckets
  - Used successfully for 121 frame video training in ~1 hour
  - *From: KevenG*

- **Frames**: 121 frames
  - Good balance of quality and training speed for video LoRAs
  - *From: KevenG*

- **Quantization**: null
  - Set to null if using fp8 model since it's already fp8, otherwise will error
  - *From: crinklypaper*

- **Rank**: 64-128
  - 128 rank produces better quality than 32 rank, but 32 rank less texture biased
  - *From: oumoumad*

- **learning_rate**: 1e-4 (default), 2e-5 for stability
  - 4e-4 is too high, 2e-5 recommended by Kiwv
  - *From: Kiwv*

- **rank and alpha**: 32
  - Standard setting used by multiple successful trainers
  - *From: NebSH*

- **first_frame_conditioning_p**: 0.5 for both T2V/I2V, 1.0 for I2V only, 0.0 for T2V only
  - 0.5 works for both modes, adjust based on desired capabilities
  - *From: mamad8*

- **training steps**: 1500 steps typical, sweet spot 7k-9k for style
  - LTX-2 converges faster than LTX-1, style accuracy peaks around 7k-9k steps
  - *From: NebSH*

- **resolution buckets**: 960x544x41 through 960x544x137
  - Standard resolution buckets used by successful trainers
  - *From: Cseti*

- **Frame count**: 121 frames at 25fps
  - Standard for LTX2, avoids slow motion/sped up issues
  - *From: SmaX*

- **Audio normalization**: -7db
  - Good level that model picks up well
  - *From: dischordo*

- **Transformer offloading**: 20% instead of 100%
  - Better speed (9s/it to 5s/it) without full VRAM usage
  - *From: Critorio*

- **Training resolution**: 5 second clips at 25fps for video
  - Recommended by AI-toolkit author, should match intended generation length
  - *From: SmaX*

- **Clip length variety**: 2-8 seconds acceptable
  - Won't completely mess up training, just affects learning
  - *From: amli*

- **Video resolution**: 768x512 (preferred), 512x512, 768x768, 1024x768
  - Must be divisible by 32 due to VAE spatial compression factor
  - *From: BrainNXDomain*

- **Training steps for small datasets**: 5000 steps
  - General recommendation, but stop when results look good
  - *From: Kiwv*

- **Frame count and resolution**: 512 resolution with 49 frames, or 256 resolution with 79 frames
  - Works well on 4090 with 18GB VRAM usage
  - *From: avataraim*

- **Rank for IC LoRA**: 128
  - Higher rank helped significantly for IC LoRA training compared to typical 64
  - *From: Alisson Pereira*

- **Video duration**: 2 seconds
  - Works well for cartoon/animated content training
  - *From: avataraim*

- **Resolution for consumer cards**: 512x512 at 121 frames
  - Fits in 24GB VRAM with slight headroom
  - *From: MOV*

- **768 bucket at 121 frames**: Works on A6000 without offloading
  - Provides better motion learning for unique concepts
  - *From: dischordo*

- **Audio scale**: Tested values: 0.75, 0.8, 0.85, 1.0, 1.5
  - Different values for lipsync intensity testing
  - *From: Mazrael.Shib*

- **Offload percentage**: 75% works, 100% recommended for 24GB cards
  - VRAM management for consumer hardware
  - *From: avataraim*

- **Rank**: 16-32 for identity LoRAs, 64+ for complex concepts
  - Balance learning capacity with overfitting prevention
  - *From: MOV*

- **rank**: 4-8 for character training
  - Higher ranks can cause diminished movement and talking ability
  - *From: Guey.KhalaMari*

- **learning_rate**: 1e-4 default
  - Standard rate, but may need adjustment for small datasets
  - *From: CJ*

- **blocks_to_swap**: 5-10 for 4090
  - Balance between VRAM usage and speed
  - *From: avataraim*

- **training steps**: 3k-8k steps
  - Sufficient for good results without overtraining
  - *From: Guey.KhalaMari*

- **blocks_to_swap**: 0 for RTX 5090, 5 for RTX 4090, 20+ for lower VRAM
  - VRAM optimization
  - *From: avataraim*

- **network_dim/network_alpha**: 32/32 recommended over 32/16
  - 32/16 gives horrible results in LTX2 unlike other models
  - *From: Choowkee*

- **learning_rate**: 1.5e-4
  - Used in working training configuration
  - *From: Jimi*

- **max_train_steps**: 400-800 steps for good results
  - Sufficient for character training with proper dataset
  - *From: avataraim*

- **audio duration**: 5 seconds for audio clips
  - Works well for voice cloning
  - *From: Gleb Tretyak*

- **video count for voice training**: 20-30+ videos minimum
  - 10 videos insufficient for good voice cloning
  - *From: crinklypaper*

- **Audio training dataset**: 20 audio files, 5 seconds each
  - Sufficient for basic audio LoRA training
  - *From: Gleb Tretyak*

- **Character LoRA training dataset**: 25 photos of a person with captions in txt
  - Standard dataset size for character training
  - *From: protector131090*


## Concepts Explained

- **In-Context LoRA (IC-LoRA)**: Training mode supported by LTX-2 for vid2vid pairs
  - *From: Persoon*

- **Bucket preprocessing**: Maximum bucket size limited by shortest video in dataset - if shortest video has 41 frames, that's the max bucket size even if other videos are longer
  - *From: oumoumad*

- **Multi frame conditioning**: LTX-2 feature that can help bias generation to desired outcomes
  - *From: oumoumad*

- **first_frame_conditioning_p**: Probability of using first frame as conditioning (0.0-1.0). Controls I2V vs T2V capability retention during training
  - *From: mamad8*

- **Frame bucket number**: Number after resolution (e.g. 89, 113) refers to frame count the model was trained on, not resolution bucket
  - *From: NebSH*

- **Cross attention keys exclusion**: Technique to exclude cross attention keys between audio and video modalities from trained LoRA, potentially improving results
  - *From: mamad8*

- **Frame count buckets**: System for organizing training data by frame counts, one of the training pitfalls to manage
  - *From: dischordo*

- **Audio normalization**: Process to standardize audio levels across training clips to avoid volume inconsistencies
  - *From: dischordo*

- **Resolution buckets**: 1920x1080 goes into 1536 bucket (1920+1080=3000, so ~1536x1536 square format)
  - *From: MOV*

- **Layer offloading**: Moving model layers between GPU and CPU RAM to save VRAM, affects training speed
  - *From: MOV*

- **DiT-based architecture**: LTX2 uses DiT (Diffusion Transformer) which may require different captioning approaches compared to non-DiT models like WAN
  - *From: Mazrael.Shib*

- **VAE spatial compression factor**: LTX2 uses compression factor of 32, requiring input dimensions to be divisible by 32
  - *From: BrainNXDomain*

- **IC LoRA**: Image Conditioning LoRA - trains with control and target video datasets to transform one type of video into another
  - *From: Alisson Pereira*

- **Text embedding cache**: Creates large cache files (376MB per dataset item) to avoid recomputing text encodings, but requires significant storage
  - *From: chancelor*

- **IC LoRA**: Identity Consistent LoRA - specialized training approach for maintaining character identity across video generations
  - *From: Alisson Pereira*

- **Bucket size**: Training resolution dimensions, not the same as final output resolution
  - *From: dischordo*

- **Rank**: Controls how many model weights the LoRA affects - higher rank = more layers affected = more VRAM but potentially more learning
  - *From: MOV*

- **LTX2 i2v mode**: Forces first frame to be input image but still generates based on text prompt, not trained as dedicated i2v
  - *From: Kiwv*

- **Mixed datasets in LTX2**: May prioritize videos over images during training
  - *From: Choowkee*


## Resources & Links

- **LTX-2 Trainer GitHub** (repo)
  - https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer
  - *From: NebSH*

- **Training modes documentation** (documentation)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/docs/training-modes.md
  - *From: NebSH*

- **Fal.ai LTX-2 trainer** (platform)
  - https://fal.ai/models/fal-ai/ltx2-video-trainer
  - *From: NebSH*

- **Tear effect LoRA** (model)
  - https://huggingface.co/oumoumad/LTX-2-19b-LoRA-TEAR
  - *From: oumoumad*

- **Gemma-3-12b Abliterated for LTX2** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/tree/main
  - *From: crinklypaper*

- **LTX-2 training paper** (paper)
  - https://arxiv.org/pdf/2601.03233
  - *From: fearnworks*

- **Hydraulic press LoRA with speedup tips** (model)
  - https://huggingface.co/kabachuha/ltx2-hydraulic-press#ltx-2-hydraulic-press-trained-at-home-in-just-15-hours
  - *From: yi*

- **Sprout LoRA for LTX-2** (model)
  - https://huggingface.co/oumoumad/LTX-2-19b-LoRA-SPROUT
  - *From: oumoumad*

- **IceKiub's LTX-2 Docker template** (tool)
  - docker pull icekiub/icyltx2:latest
  - *From: Alisson Pereira*

- **IceKiub template tutorial** (tutorial)
  - https://youtu.be/JlfQIyjxx2k?t=178
  - *From: Alisson Pereira*

- **Scooby Doo style LoRA** (model)
  - https://civitai.com/models/2308294?modelVersionId=2597100
  - *From: crinklypaper*

- **LTX-2 official trainer repository** (repo)
  - https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer
  - *From: NebSH*

- **TartanAir dataset for IC LoRA** (dataset)
  - https://tartanair.org/
  - *From: Cseti*

- **LoRA Captioner Tool** (tool)
  - https://huggingface.co/spaces/comfyuiman/loracaptionertaz
  - *From: crinklypaper*

- **Deep Zoom LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1461346143161028702/1461346143161028702
  - *From: oumoumad*

- **Ostris LTX2 settings** (settings)
  - https://x.com/ostrisai/status/2011070979066450171
  - *From: Choowkee*

- **Cakeify Dataset** (dataset)
  - https://huggingface.co/datasets/Lightricks/Cakeify-Dataset
  - *From: matanby*

- **AI Toolkit Easy Install** (tool)
  - https://github.com/Tavris1/AI-Toolkit-Easy-Install
  - *From: MOV*

- **Archive.org music videos** (dataset)
  - https://archive.org/details/artsandmusicvideos
  - *From: NebSH*

- **Archive.org cartoons** (dataset)
  - https://archive.org/details/vintage_cartoons
  - *From: NebSH*

- **LTX trainer quickstart** (documentation)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/docs/quick-start.md
  - *From: ColinUrbs*

- **Scooby Doo Style LoRA** (lora)
  - https://civitai.com/models/2308294/scooby-doo-style-lora-ltx2?modelVersionId=2597100
  - *From: crinklypaper*

- **Official LTX2 captioning prompts** (prompt)
  - provided in message
  - *From: BrainNXDomain*

- **Musubi tuner fork** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner
  - *From: Gleb Tretyak*

- **LTX-2 dataset preparation docs** (documentation)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/docs/dataset-preparation.md
  - *From: Choowkee*

- **Head swap LoRA for Flux** (model)
  - https://civitai.com/models/2027766
  - *From: Alisson Pereira*

- **Qwen2.5-Omni-7B** (model)
  - mentioned
  - *From: BrainNXDomain*

- **Musubi Tuner LTX-2 fork** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner/tree/ltx-2
  - *From: avataraim*

- **LTX2 Training Docker image** (tool)
  - https://www.reddit.com/r/StableDiffusion/comments/1q8nknf/ltx2_lora_training_docker_imagerunpod/
  - *From: metaphysician*

- **Video captioning tool** (tool)
  - https://huggingface.co/spaces/comfyuiman/loracaptionertaz_v2
  - *From: crinklypaper*

- **Captioning guide** (workflow)
  - https://civitai.com/articles/24082/tazs-ultimate-imagevideo-easy-captioning-tool-gemini-qwen-vl
  - *From: crinklypaper*

- **Golden Boy LoRA** (model)
  - https://civitai.com/models/2334302?modelVersionId=2625818
  - *From: crinklypaper*

- **BFS Head Swap LoRA** (model)
  - https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video
  - *From: Alisson Pereira*

- **Oxen.ai training livestream** (resource)
  - https://www.youtube.com/watch?v=QMRuOZ_JVXg
  - *From: LTX Lux*

- **SD Finetuning guide** (resource)
  - https://github.com/spacepxl/demystifying-sd-finetuning/
  - *From: JUSTSWEATERS*

- **Musubi-Tuner LTX-2 fork** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner.git
  - *From: avataraim*

- **Working Musubi-Tuner commit** (repo)
  - https://github.com/kohya-ss/musubi-tuner/tree/90e1559a7c73ff41ade497605e1f5b1850270711
  - *From: Choowkee*

- **ComfyUI API helper** (tool)
  - https://github.com/deimos-deimos/comfy_api_simplified
  - *From: Guey.KhalaMari*

- **Gemma model for training** (model)
  - https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized
  - *From: avataraim*

- **Musubi LTX2 fork - stable version** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner/tree/2b77b23defc40bea39ee21680fa3ab73765ab3bf
  - *From: avataraim*

- **Flash Attention prebuilt wheels** (tool)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.11/flash_attn-2.8.3+cu128torch2.8-cp312-cp312-win_amd64.whl
  - *From: crinklypaper*

- **Flash Attention packages documentation** (repo)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/blob/main/doc/packages.md
  - *From: crinklypaper*

- **Older branch of Musubi Tuner for audio** (tool)
  - not provided
  - *From: Guey.KhalaMari*

- **Simpletuner installation** (tool)
  - git clone repo, then pip install '.[cuda13-stable]'
  - *From: Gleb Tretyak*

- **Simpletuner UI command** (tool)
  - simpletuner server --ssl --port 8080
  - *From: avataraim*


## Known Limitations

- **Dataset must be homogeneous**
  - Either all videos or all images, mixing is not supported in training
  - *From: crinklypaper*

- **Fal trainer reliability issues**
  - Multiple users reporting failures and inconsistent results with fal trainer
  - *From: multiple users*

- **Windows compatibility requires manual setup**
  - Official trainer requires Linux, Windows needs manual triton installation
  - *From: boorayjenkins*

- **Effect duration tied to training data length**
  - Training on 3sec clips tends to produce slow motion when generating longer videos
  - *From: oumoumad*

- **I2V is fussy and does its own thing**
  - I2V mode often ignores input and generates unexpected content, sometimes just shows initial frame then goes off on its own
  - *From: fearnworks*

- **Multiple characters in one generation bleed together**
  - When trying to use 2-character LoRA for generating different characters separately, they get mixed like in WAN
  - *From: NebSH*

- **Long music training doesn't work well**
  - Training on 40-90 second music samples performed poorly, likely because base model only trained on 5-10s max
  - *From: mamad8*

- **Pronunciation issues in non-English languages**
  - French words often mispronounced with silent letters spoken or wrong sounds, text encoder doesn't reliably encode pronunciation
  - *From: NebSH*

- **Real movement causes distortion**
  - Even at 9k steps on image + 12k steps on video, any real movement gets distortion
  - *From: crinklypaper*

- **Videos without audio tracks cause issues**
  - Having videos with no audio in dataset may cause inference errors
  - *From: Lumori*

- **Character voice separation difficulty**
  - Multiple characters in dataset tend to combine voices into one unless properly separated
  - *From: Lumori*

- **WAN training parameters don't translate to LTX2**
  - Training approaches that worked for WAN don't work as well for LTX2
  - *From: Choowkee*

- **Audio quality cannot be improved through LoRA**
  - Audio limitations are inherent to LTX2 model itself and cannot be fixed with LoRAs
  - *From: Kiwv*

- **Logos are difficult to train**
  - Multiple attempts to train logos failed even after 9000+ steps, suggesting logos may be a pain point for the model
  - *From: Mazrael.Shib*

- **Small datasets don't work well**
  - 5 videos won't learn anything meaningful, need at least 40 videos for proper training
  - *From: Kiwv*

- **Character bleed between subjects**
  - Some character attributes can bleed between different characters in the dataset
  - *From: crinklypaper*

- **IC LoRA doesn't support audio conditioning during training**
  - Audio must be added as adaptation to IC LoRA workflow, not trained directly
  - *From: Alisson Pereira*

- **Image-only training produces poor motion results**
  - Training with only images gives poor results for video generation compared to video training
  - *From: Mazrael.Shib*

- **Low FPS training causes motion artifacts**
  - Training at low FPS creates hand distortions and artifacts during fast movements
  - *From: MOV*

- **Dataset limited to landscape causes poor vertical video results**
  - Training primarily on landscape videos results in poor performance on vertical videos with full body visible
  - *From: Alisson Pereira*

- **Overtraining character LoRAs with images**
  - Can cause diminished movement and inability for character to talk, even at 250 steps
  - *From: CJ*

- **Training samples are poor quality indicators**
  - Samples during training look much worse than actual LoRA performance
  - *From: NebSH*

- **Recent Musubi-Tuner versions broken**
  - Latest commits fail to train properly with bad loss curves
  - *From: Choowkee*

- **Eyes generalization issues**
  - Model fails to generalize anime eye styles correctly even at 6k steps
  - *From: Choowkee*

- **Audio generation inconsistency**
  - Works only 30% of the time and is prompt-dependent
  - *From: Jonathan Scott Schneberg*

- **8GB VRAM insufficient for training**
  - Barely possible on 24GB, definitely not feasible on 8GB cards
  - *From: Kiwv*

- **Outpainting seam issues**
  - IC LoRA outpainting works but slightly alters original content creating visible seams
  - *From: oumoumad*

- **LTX2 isn't like a one-shot voice cloner**
  - Mileage that audio LoRA can give seems limited
  - *From: Guey.KhalaMari*

- **Simpletuner validation during training doesn't work yet**
  - Plus need to convert LoRAs to ComfyUI format
  - *From: Gleb Tretyak*

- **Possible resolution limitation for training**
  - LoRA trained at 256 resolution had no effect, while 512 resolution previously worked
  - *From: protector131090*


## Hardware Requirements

- **VRAM for training**
  - RTX 6000 Pro uses ~48GB VRAM for training at 992x544x185 without audio, 37-44GB with fp8 model
  - *From: fearnworks*

- **Full model fine-tuning**
  - Requires significant resources, likely multiple H100s
  - *From: burgstall*

- **Minimum VRAM estimate**
  - Looking like 44GB VRAM minimum for training, though AI Studio might enable 24GB
  - *From: Kiwv*

- **System RAM usage**
  - Uses tons of RAM, 64GB recommended for smooth operation
  - *From: crinklypaper*

- **Text encoder size**
  - Gemma text encoder is 23.5GB
  - *From: crinklypaper*

- **H100 training stats**
  - Peak GPU memory: 45.45 GB, 0.30 steps/second, 111.9 minutes total time
  - *From: NebSH*

- **H100 VRAM usage with specific buckets**
  - 60-70GB VRAM usage with resolution buckets 960x544x41 through 960x544x137
  - *From: Cseti*

- **RTX 3090/4090 training possible**
  - Sub-24GB training possible but slow, image-only training works on 24GB
  - *From: ZeusZeus*

- **RTX 3090 training requirements**
  - Need 128GB+ RAM, float8 model, 4-bit text encoder, 256 resolution, 72 frames (3 seconds) might work
  - *From: Kiwv*

- **24GB VRAM training setup**
  - Possible with 128GB RAM, float8 model and text encoder, 100% offload, 512 resolution 5s videos, 30s/it speed
  - *From: MOV*

- **Minimum GPU for training**
  - Tested on 5090+, 4090 might work for images with heavy quantization and offloading but will be slow with poor quality
  - *From: LTX Lux*

- **5090 VRAM usage**
  - 14GB VRAM utilization during training with offloading enabled
  - *From: Choowkee*

- **3090 capability**
  - Can train locally with 100% offload, good for 512res videos and 1024res images
  - *From: MOV*

- **24GB VRAM limitation**
  - Too little for proper LTX training, can only do images with heavy quantization and offloading
  - *From: Kiwv*

- **H100 speed**
  - <1s/it on H100 with LTX trainer, ~7.9s/it on H100 with AI Toolkit
  - *From: scf*

- **VRAM for video training**
  - 100 videos at 512 resolution with 49 frames uses 18GB VRAM on 4090, with 7.30 sec/iter speed
  - *From: avataraim*

- **Storage for text embedding cache**
  - Large datasets require 300GB+ storage space for cached embeddings
  - *From: avataraim*

- **RTX 4090 performance**
  - 5.23 sec/iter for image training, 6-7 sec/iter for video training with audio
  - *From: chancelor*

- **Memory usage during training**
  - Training shows 74.8% memory usage (17.9GB/24GB) on RTX 4090
  - *From: avataraim*

- **24GB VRAM minimum for video training**
  - 512x512x121 frames with rank 32 and audio training uses 22.5-23GB VRAM in AI Toolkit
  - *From: MOV*

- **768x768 training needs A6000 class**
  - 768 resolution at 121 frames requires high-end professional cards without offloading
  - *From: dischordo*

- **Consumer 24GB cards work with optimization**
  - RTX 4090/3090 can train with float8, 4-bit text encoder, and full offloading
  - *From: avataraim*

- **Cache storage needs**
  - 400 videos + 400 images = ~300GB cache files in AI Toolkit, 30MB in Musubi
  - *From: avataraim*

- **VRAM usage with block swapping**
  - 512res 121f videos: 30 swap=18.6GB, 26 swap=21.6GB, 24 swap=22.9GB max VRAM
  - *From: MOV*

- **Training speed on 4090**
  - 5-6 it/sec for 512 video + 768 images, 10 it/sec for video only
  - *From: avataraim*

- **Training speed on 5090**
  - Around 3.30s/it for 512x512 video with images
  - *From: JonkoXL*

- **Cache storage requirements**
  - TE cache for 720 image dataset is 265GB, can quickly fill SSD
  - *From: izashin*

- **RTX 4090 VRAM usage**
  - Can run with blocks_to_swap=5, but may freeze with audio+video training
  - *From: avataraim*

- **RTX 5090 VRAM usage**
  - Can run with blocks_to_swap=0, training speed 3.62 iter/sec
  - *From: avataraim*

- **A6000 performance**
  - Works well for training, used when 4090 had issues
  - *From: avataraim*

- **Minimum VRAM for training**
  - 24GB barely sufficient, 8GB not feasible for quality training
  - *From: Kiwv*

- **VRAM for musubi-tuner**
  - 16 VRAM, still got OOM on validation sampling at 512x512x49
  - *From: Gleb Tretyak*


## Community Creations

- **Tear effect LoRA** (lora)
  - Trained tear/ripping effect, available in 32 and 128 rank versions
  - *From: oumoumad*

- **Sprout LoRA** (lora)
  - Plant sprouting effect retrained for LTX-2 with fine detail improvements
  - *From: oumoumad*

- **Character LoRAs** (lora)
  - Various character LoRAs trained on interview footage using pyscene extraction
  - *From: NebSH*

- **Camera control LoRAs** (lora)
  - 20 camera control LoRAs trained for LTXV 0.97 distilled
  - *From: NebSH*

- **NSFW LoRAs** (lora)
  - Handjob and other adult content LoRAs trained successfully
  - *From: KevenG*

- **IceKiub's LTX-2 Docker template** (tool)
  - Free template with interface for LTX-2 training, available on Runpod or local Docker
  - *From: Alisson Pereira*

- **Audio-only training modifications** (tool)
  - Modified LTX-2 trainer for audio-only training, significantly reduces memory usage
  - *From: mamad8*

- **Scooby Doo style LoRA** (lora)
  - Character and style LoRA trained on Scooby Doo content with voice capabilities
  - *From: crinklypaper*

- **South Park LoRA** (lora)
  - Style LoRA trained on 4 episodes, 889 videos, produces authentic South Park style
  - *From: NebSH*

- **Video segmentation script** (tool)
  - Bash script for bulk segmenting videos into 5s 24fps files
  - *From: ZeusZeus*

- **IC Light LoRA for LTX-2** (lora)
  - Useful for audio react workflows, reference input can be basic white on black audio react map to drive luminance
  - *From: oumoumad*

- **Lum Particles LoRA** (lora)
  - Use any basic white on black video to drive luminance, handy for audio react workflows
  - *From: oumoumad*

- **Musubi tuner fork for LTX2** (tool)
  - Community fork adding LTX2 support to Kohya's training tools, faster than AI Toolkit
  - *From: Choowkee*

- **Custom checkpoint selector node** (node)
  - ComfyUI node to easily select training checkpoints by index from a directory path
  - *From: avataraim*

- **Dataset loader node** (node)
  - ComfyUI node that loads videos and captions from dataset path, supports JSON or separate files
  - *From: avataraim*

- **Multi-run generation node** (node)
  - Allows running 50+ video generations with single click for easy checkpoint comparison
  - *From: avataraim*

- **Whisper ComfyUI node** (node)
  - Custom node for running Whisper speech recognition in ComfyUI workflows
  - *From: MOV*

- **Gradio interface for LTX Musubi** (tool)
  - Easy interface to create datasets, generate toml files, cache, and train with live terminal view
  - *From: avataraim*

- **Firefox extension for Twitch clips** (tool)
  - Scrape and download multiple clips from Twitch as mp4 for dataset creation
  - *From: crinklypaper*

- **Batch setup files for Musubi-Tuner** (workflow)
  - Easy .bat setup for Windows users with install, cache, and train scripts
  - *From: avataraim*

- **Kijai's node for voice LoRA** (node)
  - Works for repurposing character LoRAs for voice only and audio-trained LoRAs
  - *From: Guey.KhalaMari*
