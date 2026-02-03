# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-04-01 to 2025-05-01*


## Technical Discoveries

- **fp16_fast is significantly faster than bf16 for 4090**
  - 12.19/it vs 15.26/it - about 3 seconds per iteration faster
  - *From: ezMan*

- **SLG has minimal speed impact**
  - 10 steps with SLG: 12.51s/it vs without SLG: 12.18s/it - barely noticeable difference
  - *From: ezMan*

- **Teacache modulated time embeds doesn't work with dpmpp_sde**
  - Causes rainbows, but time embeds mode works albeit slowly
  - *From: ezMan*

- **VACE model released for Wan 1.3B**
  - Preview version available on HuggingFace, works with video control inputs like depth
  - *From: Kijai*

- **WhatsApp destroys video quality for vid2vid**
  - Transferring videos from phone to computer through WhatsApp significantly affects output quality compared to original files
  - *From: 3Dmindscaper2000*

- **Wan 1.3B can effectively improve old generations as second pass**
  - Using depth, highres and aesthetics loras with 1.3B at low step counts (6-8 steps) significantly improves motion coherence of old Hunyuan/Wan generations
  - *From: David Snow*

- **DepthCrafter vs Video Depth Anything comparison**
  - DepthCrafter appears better for static shots, VDA may be more temporally consistent but requires size reduction to avoid OOM
  - *From: David Snow*

- **VACE uses fp32 format**
  - The VACE model file is in fp32 format, making it larger than typical fp8 models
  - *From: Kijai*

- **Batched CFG causes flashy results with VACE**
  - Disabling batched CFG on sampler fixes bad and flashy VACE outputs
  - *From: TK_999*

- **VACE blocks are in bf16 while rest of model is fp32**
  - Mixed precision setup causing performance impact
  - *From: Kijai*

- **VACE adds 15 additional blocks that run every step**
  - This explains the significantly slower performance compared to standard Wan
  - *From: Kijai*

- **Reference images work best with white backgrounds**
  - Need to segment reference images and place on white background for proper likeness
  - *From: Kijai*

- **Video extension technique discovered**
  - Send empty frames as gray frames (0.5 works best) with video frames, mask where video frames are white and rest black
  - *From: Kijai*

- **VACE encode strength of 0.4 gives control with creativity**
  - Lower strength maintains control while allowing more creative freedom
  - *From: Cseti*

- **Padding reference images can make them work when they otherwise fail**
  - Image aspect ratio and canvas placement affects reference image functionality
  - *From: Kijai*

- **FP32 provides better quality than FP16 for VACE**
  - FP16 was described as 'trash', FP32 required for good results
  - *From: VK (5080 128gb)*

- **DensePosePreprocessor works well with VACE**
  - Works with good results at strength 1
  - *From: VK (5080 128gb)*

- **Reference images must have white background for VACE to work**
  - Model doesn't work at all if there aren't any white in the reference
  - *From: Kijai*

- **Multiple reference images are composited into single image**
  - Put multiple references into a single image rather than separate inputs
  - *From: Draken*

- **VACE puts reference image as first frame during processing**
  - Reference image is literally put into the first frame, trained to pick up likeness from it
  - *From: Draken*

- **Context windows can process longer videos in 81-frame chunks**
  - Context options split process to 81 frame windows with overlap, works much better for long videos
  - *From: Kijai*

- **Second pass at low denoise removes oversaturation**
  - 2nd pass at 6 steps works well to remove the oversaturated look
  - *From: NebSH*

- **Higher resolution helps reduce artifacts**
  - 1024x576 vs 720p shows improvement, though some artifacting remains
  - *From: Piblarg*

- **Force offload halves VRAM usage**
  - Enabling force offload halfed vram requirements
  - *From: VK (5080 128gb)*

- **VACE reference images need white background to work properly**
  - Reference images must be on white background, preferably with subject background removed. Position on canvas matters significantly for quality
  - *From: Kijai*

- **SLG parameters can help with image arrangement in VACE**
  - SLG 8, 0.1 start, 0.3 end noticed to help with image arrangement
  - *From: IllumiReptilien*

- **VACE works with existing 1.3B LoRAs**
  - LoRAs trained on original Wan weights work with VACE, making it better than fun-control
  - *From: Kytra*

- **Control inputs need specific formatting**
  - For lineart/canny, model wants black lines on white background
  - *From: Kijai*

- **Masking technique for VACE**
  - Use grey solid color composite where mask applies for better results. Prep reference image by removing background and compositing on grey layer
  - *From: IllumiReptilien*

- **CFG zero star and zero init helps with VACE**
  - Not SLG that helps, but CFG zero star and zero init settings
  - *From: IllumiReptilien*

- **VACE model needs separated subjects or padded images for reference**
  - Full reference images don't work well, need background removed or image padded
  - *From: Kijai*

- **VACE strength value really boosts the reference**
  - Using 1.5 strength now actually produces better results
  - *From: Kijai*

- **Gray areas represent missing video parts in VACE**
  - Values equal to 127 represent missing video part. White areas in mask represent parts to be generated, black areas represent parts to be retained
  - *From: AJO*

- **VACE works well with character LoRAs**
  - Standard 1.3B LoRAs work with VACE for character consistency
  - *From: Kytra*

- **VACE pose control produces excellent results**
  - Character lora + pose rig into VACE produces great results with consistency
  - *From: Kytra*

- **Hi-Res lora works with VACE**
  - Compatible with VACE model
  - *From: VK (5080 128gb)*

- **SemSegPrepprocessor and Coco Sem work well with VACE**
  - Both preprocessors produce surprisingly good results with VACE
  - *From: VK (5080 128gb)*

- **VACE can interpret mixed inputs automatically**
  - VACE understands first frame as reference and rest as control without explicit configuration - uses colored frames as-is and control inputs as motion guidance
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE supports creative inpainting with gray overlay**
  - Can do outfit swaps by compositing gray over masked areas in input frames - no explicit mask input needed
  - *From: Zuko*

- **Sapiens is SOTA for human preprocessing**
  - Meta's Sapiens models provide better temporal consistency than DWPose for pose, depth, segmentation, and normals
  - *From: Kijai*

- **DiffSynth models are full 1.3B models, not LoRAs**
  - The new DiffSynth releases are custom finetunes/distilled versions, not actual LoRAs despite the naming
  - *From: Kijai*

- **VACE 1.3B handles high resolution slightly better than standard 1.3B**
  - VACE version of 1.3B model shows improved high resolution performance
  - *From: DawnII*

- **VACE mask input controls where VACE can apply in both temporal and spatial terms**
  - The mask input defines the areas where VACE effects are applied across time and space
  - *From: Kijai*

- **VACE strength parameter affects different aspects depending on usage**
  - Affects control strength when using control only, and reference strength when using both control and reference
  - *From: Kijai*

- **Context windows work well with fewer frames than expected**
  - 720p generation with limited context frames still produces good results
  - *From: Kijai*

- **Reference images work better on white background, but gray can be better for predominantly white subjects**
  - White canvas is standard for reference, but gray background helps when subject is mostly white
  - *From: JmySff*

- **Multiple control images can be stacked by overlaying them**
  - You can combine multiple control inputs by overlaying the control images
  - *From: ameasure*

- **WAN 1.3B video quality is beyond typical 1.3B model expectations**
  - The quality output significantly exceeds what's normally expected from a 1.3B parameter model
  - *From: slmonker(5090D 32GB)*

- **VACE works with LoRAs**
  - LoRAs work perfectly with VACE, contrary to some expectations
  - *From: Kijai*

- **Main Wan 1.3B model was not even trained**
  - The original VACE model contained untrained 1.3B fp32 model, just the VACE blocks were trained
  - *From: Kijai*

- **VACE can be loaded separately**
  - Standalone VACE that can be loaded with any 1.3B model, saves 6GB disk space
  - *From: Kijai*

- **Resolution must be divisible by 16**
  - Both width and height need to be divisible by 16, not just 8, for proper operation
  - *From: Kijai*

- **DG models don't need white backgrounds**
  - DG models hold onto reference image position tighter and don't require white backgrounds
  - *From: Hashu*

- **VACE reference images are inserted at start of frame sequence**
  - If generating 33 frames with 1 ref image, it actually generates 29 frames as ref is first latent then dropped before decode
  - *From: Kijai*

- **Combining depth/normals/lineart improves video quality**
  - Using depth, lotus normals, and realistic lineart together provides more detail information to the model
  - *From: David Snow*

- **VACE model doesn't train any of the base layers**
  - Kijai extracted it and found VACE can be loaded separately from base models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DG models work much better at 4 steps 1 CFG**
  - Better at keeping style and reference image doesn't need white background
  - *From: Hashu*

- **prev_embeds allows different control and reference strength**
  - Only way to have different control strength and different ref input strength
  - *From: Hashu*

- **Early denoising steps are WAY stronger in prev_embeds**
  - Doing 50/50 split won't do much, early steps have much more influence
  - *From: Kijai*

- **Euler scheduler performs worse than UniPC for VACE**
  - Switching back to UniPC from Euler improved results significantly
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE supports inverted canny (black lines on white background)**
  - Works fine with black lines on white background, also tested lineart
  - *From: Kijai*

- **Bounding box control works but outlined circle does not**
  - Box moves the subject without drawing the box, circle starts drawing circle shapes
  - *From: Kijai*

- **VACE inpainting quality is exceptional**
  - Can replace complex compositing work that would take hours
  - *From: traxxas25*

- **VACE works similarly to Tora**
  - Uses start frame + trajectory with bbox + reference image
  - *From: Kijai*

- **Model can do extension without context**
  - The base model has extension capabilities, potentially reducing need for context windows
  - *From: Kijai*

- **LoRAs trained for base model work with VACE**
  - Base model unchanged so T2V LoRAs are compatible
  - *From: Kijai*

- **Reference image background removal improves consistency**
  - User couldn't get VACE to work until removing background from reference image
  - *From: ingi // SYSTMS*

- **Skyreels A2 model performs better I2V than base I2V model**
  - Initial tests show SkyreelsA2 gives different and potentially better results for normal I2V compared to base I2V model
  - *From: Kijai*

- **SkyreelsA2 can do multiple reference images**
  - Model supports 2-3 reference images, not just one
  - *From: Kijai*

- **SkyreelsA2 uses clip embeds unlike VACE**
  - Main difference from VACE is that SkyreelsA2 uses clip embeds since it's based on 14B I2V model, while VACE doesn't use clip embeds at all
  - *From: Kijai*

- **Reference image positioning affects final output significantly**
  - Composition and size of subjects in reference images is quite important for final output quality
  - *From: slmonker(5090D 32GB)*

- **TeaCache optimal threshold is around 30% skipped steps**
  - 30% skipped generally gives decent quality, more than 50% usually ends up bad, though I2V is far less sensitive than other tasks
  - *From: Kijai*

- **VACE works extremely well with image references and maintains subject consistency**
  - Multiple users demonstrated strong reference adherence in their generations
  - *From: slmonker(5090D 32GB)*

- **Blurred depth maps work better than clean Blender depth renders**
  - Sharp Blender depth maps don't work at all, but adding just 3 pixel blur makes them function properly
  - *From: Kijai*

- **VACE can do temporal inpainting with any number of input frames**
  - Black mask areas are kept, white areas are generated new. Can use for frame extension and morphing
  - *From: Kijai*

- **VACE context windows work for longer generations**
  - Successfully generated 960x480x221 frames using reference + control + context
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE sees bounding boxes as control - perfect boxes work, circular shapes make it draw circles**
  - Model interprets shape geometry in control inputs
  - *From: Kijai*

- **Lineart and canny need to be inverted for VACE**
  - Control inputs require color inversion to work properly
  - *From: Kijai*

- **Character replacement workflow using 2-step approach works very well**
  - First generate clean background, then generate character with proper lighting/environment prompting
  - *From: traxxas25*

- **VACE memory optimization breakthrough**
  - Kijai discovered memory optimizations that reduce VACE VRAM usage significantly: 832x480x81 frames now fits in ~12GB without offloading, and 1024x1024x81 fits in ~13GB VRAM
  - *From: Kijai*

- **VACE intermediate results can be moved to RAM**
  - Moving VACE intermediate results to RAM after each VACE block calculation reduces VRAM usage to almost nothing extra with only slight speed loss
  - *From: Kijai*

- **Depth and pose control blending technique**
  - Successfully blended depth and dwpose controls by using two separate VACE encode nodes with reduced strength (0.5 or less) or switching between them during generation steps
  - *From: yo9o*

- **Reward LoRAs released for Wan2.1-Fun models**
  - Wan2.1-Fun-14B-InP-HPS2.1.safetensors and Wan2.1-Fun-14B-InP-MPS.safetensors, 1.46 GB each, use Reward Backpropagation technique for better human preference alignment
  - *From: Lumi*

- **VACE supports outpainting functionality**
  - VACE can handle outpainting tasks, addressing a long-standing need
  - *From: Godhand*

- **Wan provides better camera movement handling than AnimatedDiff**
  - Wan doesn't create distorted backgrounds like AnimatedDiff when camera moves
  - *From: xwsswww*

- **Multi-frame control possible with VACE**
  - Can add frames in middle between start/end frames using white frames in video editor like CapCut
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE memory usage optimization**
  - Kijai halved the VACE memory usage and added offloading - 832x480x81 now uses only 6GB VRAM during sampling
  - *From: Kijai*

- **Reward LoRAs work with multiple models**
  - Reward LoRAs work with both Fun Control 1.3B and base 1.3B models, with recommended strengths of 0.5 for HPS and 0.7 for MPS
  - *From: DawnII*

- **Reference image requirements for VACE**
  - Reference images need to be on white background for best results - padding is simplest way, BG removal is better
  - *From: Kijai*

- **VACE works as single image generation**
  - VACE can work for single frame generation with control, though if using reference image, input needs to be 2 images
  - *From: Kijai*

- **VACE works with existing Wan 2.1 LoRAs without retraining**
  - VACE is additional module, original model weights not modified, so LoRAs work as well as they can
  - *From: Kijai*

- **DiffSynth converted LoRAs are 2x stronger than originals**
  - DiffSynth removed alpha keys from reward LoRAs, making them twice as powerful at 1.0 strength compared to originals
  - *From: Kijai*

- **VACE requires white canvas background for subject detection**
  - Subjects must be on white canvas for VACE to detect them properly, can have multiple subjects on same canvas
  - *From: Kijai*

- **Video-depth-anything uses less VRAM than DepthCrafter after xformers install**
  - Takes substantially less vram than depthcrafter after installing xformers
  - *From: David Snow*

- **VACE supports spatial and temporal inpainting/outpainting simultaneously**
  - Best part of VACE is that you can do all control, inpainting, outpainting at once
  - *From: Kijai*

- **VACE treats white areas as alpha/transparency**
  - The model is picky about too high quality depth maps being detected as grayscale input, and white areas are interpreted as transparent
  - *From: Kijai*

- **VACE has soft cap of 81 frames**
  - Artifacts appear around 129 frames, similar to other models trained at specific frame counts
  - *From: The Shadow (NYC)*

- **Riflex doesn't work well with Wan models**
  - Can mess up generated content compared to standard generation without riflex
  - *From: Pedro (@LatentSpacer)*

- **DG model loses character likeness but is faster**
  - Distilled model trades character consistency for speed improvements
  - *From: burgstall*

- **Combined VACE strength shouldn't exceed 1.0**
  - When using multiple VACE encodes, the combined strength should stay under 1.0 to avoid overly strong influence
  - *From: Kijai*

- **Feta_args value is set by frame count**
  - For 81 frames the default is 4.0, but can be lower for weaker effect. Using wrong values for frame count ruins output
  - *From: Kijai*

- **Multiple VACE encode nodes require much lower strength values**
  - When using more than 1 VACE node, the strength on both needs to be much lower, or better to schedule them step wise
  - *From: Kijai*

- **Reference images need white canvas padding**
  - Reference image needs to be on a white canvas for the model to use it, if you don't want to remove background you pad it instead. Reference image is NOT same thing as start image
  - *From: Kijai*

- **VACE automatically pads encoded video**
  - Made it automatically pad the encoded video to fix tensor errors when using reference images
  - *From: Kijai*

- **Multiple subjects can be used on reference canvas**
  - You can have multiple subjects on the reference canvas too
  - *From: Kijai*

- **VACE is not strictly just start/end frame**
  - It's not strictly just start/end frame, it's any number of frames and mask
  - *From: Kijai*

- **Multiple reference images can be composited**
  - You always could use more than one reference image, just composite them to same canvas
  - *From: Kijai*

- **VACE works with DWpose face only for character animation**
  - Using DWpose with face only enabled, reference image, and grey background masking produces good face animation with lip sync accuracy
  - *From: IllumiReptilien*

- **Grey background masking technique for VACE**
  - Using 50% grey with normal blend mode at 50% for masked areas in VACE inpainting workflows
  - *From: IllumiReptilien*

- **ReCamMaster model available for Wan**
  - New camera control model for Wan 2.1 1.3B that requires specific weights, produces noise without them
  - *From: Kijai*

- **IP Adapter announced for Wan 1.3b**
  - Ostris announced IP Adapter for Wan 1.3b with impressive adherence
  - *From: pom*

- **VACE can work without controlnet**
  - VACE can be used for lip sync and face animation without control inputs, just reference frames and bbox masks
  - *From: IllumiReptilien*

- **VACE can be used for straight I2V without needing input video**
  - You can use VACE with just a starting image and nothing else for image-to-video generation
  - *From: Hashu*

- **Multiple VACE controls can be chained together**
  - You can chain one VACE encode into another, just like controlnets, to use multiple controls simultaneously
  - *From: David Snow*

- **VACE supports temporal inpainting with flexible frame masking**
  - You can have any number of frames it keeps and any number of frames it tries to generate, not just start/end frames
  - *From: Kijai*

- **Two VACE embeds can be used for separate ref and control**
  - One embed with ref only and another with control can be used to separate reference image strength from control strength
  - *From: Kijai*

- **White or gray images can be used as neutral reference**
  - Using white or gray images as reference in VACE embed with control can help avoid reference image burn-in
  - *From: Kijai*

- **DG_Boost models work better with style LoRAs than base 1.3B**
  - DG_Boost Evol V3 can achieve closer style matches with LoRAs where base model cannot get close
  - *From: David Snow*

- **LoRA effect drops off dramatically after 2 steps**
  - First example style only works on 2 step videos, which are too low quality to be useful
  - *From: David Snow*

- **VACE works much better than vanilla WAN with LoRAs for style transfer**
  - Got essential style down in about an hour using VACE that couldn't be achieved in three days with vanilla WAN and LoRAs
  - *From: David Snow*

- **Reference images add 4 latent frames in VACE**
  - When plugging in a reference image to VACE, it adds 4 latent frames which can cause tensor mismatch errors
  - *From: DawnII*

- **Optimal Steps implementation works with WAN T2V native**
  - OptimalSteps from bebebe666 can reduce generation time - 20 optimal steps vs 20 regular steps shows quality improvement
  - *From: Vérole*

- **Context windows overlap affects frame calculation**
  - 2 context windows would be 81+81+16 = 169 frames total due to overlap, not just 162
  - *From: Kijai*

- **VACE allows flexible video generation combining control frames with or without source video encoding**
  - You can use control only, or control + source video. Control frames are generated from source video but you don't need to use the source video itself in diffusion process
  - *From: David Snow*

- **Lineart control works opposite with VACE compared to vanilla 1.3B**
  - On vanilla 1.3B, increasing lineart control skews towards lineart style, but with VACE it's the opposite - gets more shaded with higher lineart influence
  - *From: David Snow*

- **VACE with both reference image and control video at 1.0 creates noisy outputs**
  - Better results when separating control video from reference image with strength around 0.5 to 0.6 for cleaner outputs
  - *From: Johnjohn7855*

- **Higher resolution models seem to produce slower motion**
  - Higher resolution models need to focus more on increased pixels, so have less power to render motions/camera movements
  - *From: Johnjohn7855*

- **Context window changes style even when frame count matches**
  - Enabling context options can completely change the look even when testing at same frame number as context window due to overlap calculations
  - *From: David Snow*

- **ExVideo LoRA adds extra detail to normal 81-frame generations**
  - When ExVideo LoRA is left enabled on 81-frame generations, it acts as a detail enhancement LoRA, adding more visual detail beyond just frame extension
  - *From: David Snow*

- **Fun 1.3B model works with 220+ frames using extended length LoRA**
  - Fun 1.3B with extended length LoRA can generate 220 frames with good quality, taking only 2min 17sec on 4060 ti 16GB at 368x640 resolution
  - *From: Pol*

- **Fun models are significantly faster than VACE**
  - Fun 1.3B generates faster than VACE 1.3B and 14B models while using less VRAM
  - *From: Pol*

- **VACE uses 15 additional blocks that run on each step**
  - VACE model has 15 more blocks than base Fun model, explaining higher VRAM usage
  - *From: Kijai*

- **Wan models have issues with car motion direction**
  - Models tend to get car direction wrong, sending them backwards, sideways, or making them transform instead of moving forward
  - *From: David Snow*

- **Video-depth-anything and DepthCrafter are superior to regular depth anything**
  - These specialized video depth models provide better input quality which reflects in output quality
  - *From: David Snow*

- **TeaCache can work with Wan Fun Control 14B**
  - Use the '14B T2V' option in the TeaCache node model type dropdown for Wan Fun Control 14B
  - *From: MilesCorban*

- **SageAttention provides 100% speed increase with minimal quality impact**
  - About 1% quality drop for 100% speed increase, sometimes sage output is preferable
  - *From: Kijai*

- **VACE and Fun Control can give coherent output with single step**
  - Much more efficient than T2V which needs more steps
  - *From: Kijai*

- **TeaCache has heaviest quality hit but should be compared to actual step count**
  - 30% of steps skipped is acceptable quality tradeoff
  - *From: Kijai*

- **Training 1.3B models on synthetic data from 14B works better**
  - Using 14B model outputs as training data for 1.3B models produces better results than mixed video/image datasets
  - *From: Piblarg*

- **Wan2.1-FLF2V-14B-720P first-last frame model released**
  - Official first and last frame to video generation model, 720p resolution, works with old workflow but has new pos embed
  - *From: DawnII*

- **NormalCrafter produces stable video normals without motion disruption**
  - Video normal maps that maintain stability and don't mess up motion, works better than depth alone for control
  - *From: David Snow*

- **Combining depth and normals improves stability**
  - Lotus vs Normalcrafter comparison shows better stability with normals, prefer stability over fine details
  - *From: David Snow*

- **SynCamMaster places subjects at exact same position regardless of prompt**
  - Every generation puts subject at same position, background comes out correctly from expected camera angle but subject placement is wrong
  - *From: Kijai*

- **FLF2V model only has one new layer: img_emb.emb_pos**
  - Comparison shows 1303 common tensor keys with only img_emb.emb_pos being unique to FLF2V model
  - *From: Benjimon*

- **FLF2V model is significantly different from I2V model**
  - Average cosine similarity of 0.873389 with minimum of -0.377899, much less similar than Fun Control was to base model
  - *From: Benjimon*

- **Orbit camera generation node added but model struggles with over 90 degrees**
  - New node to generate orbit camera movements, but the model can't handle rotations greater than 90 degrees well
  - *From: Kijai*

- **FramePack generates backwards from end to beginning**
  - The model generates ending actions before starting actions due to inverted sampling, requires waiting for earlier frames
  - *From: JohnDopamine*

- **FramePack uses DiT patchify technique for temporal coherence**
  - For 3 frames predicting 4th: 3rd frame encoded normal, 2nd frame with fewer patches, 1st frame gets least patches. This technique isn't possible with UNet
  - *From: Fannovel16*

- **FramePack can generate 1-minute video with only 6GB VRAM**
  - Can generate 60 seconds at 30fps (1800 frames) using 13B model with minimal 6GB GPU memory, laptop GPUs work
  - *From: zelgo_*

- **FramePack processes video in 5-second chunks**
  - Generates approximately 5 seconds at a time, building up longer videos progressively
  - *From: JohnDopamine*

- **Wan FLF2V model primarily trained on Chinese text-video pairs**
  - Official repo now recommends using Chinese prompts for better FLF2V results
  - *From: DawnII*

- **FLF2V model exists and is available**
  - Wan 2.1 First Frame Last Frame model (FLF2V) is available with fp8 quantization, works with wrapper nodes
  - *From: DawnII*

- **VACE temporal masking system**
  - Black mask frames are keyframes (don't change), white mask frames are inpainted temporally. Can mix and match any number of frames
  - *From: Kijai*

- **VACE supports spatial masking in addition to temporal**
  - More advanced masking capabilities beyond just temporal control
  - *From: Kijai*

- **Fun InP model can do temporal masking like VACE**
  - Just not with control inputs
  - *From: Kijai*

- **Chinese prompts work better than English for FLF2V**
  - Recommended to use Chinese prompts for better results
  - *From: DawnII*

- **Resolution affects Fun Control performance significantly**
  - Anything below 576x1024 wouldn't follow lips and eye direction properly, need higher resolution on preprocessors too
  - *From: A.I.Warper*

- **VACE captures eye movement better than standard processing**
  - When using VACE with stylized Pixar character, eye movement tracking is noticeably improved
  - *From: A.I.Warper*

- **Mediapipe proves better than DWPose for realism-to-stylized workflows**
  - When using realistic source footage with stylized character reference, Mediapipe keeps the eyes big instead of conforming them to source video
  - *From: A.I.Warper*

- **VACE works with only 20 steps, could work with 8**
  - Quality results achieved with just 20 steps, potentially could get away with 8 steps
  - *From: A.I.Warper*

- **Using start frame instead of reference image produces better results**
  - Multiple users confirmed that using start frame approach works better than using separate reference image for VACE
  - *From: A.I.Warper*

- **CausVid has very fast inference time**
  - 12 seconds for 5 second 832x480 @ 16fps video, mainly limited by model loading time
  - *From: Cubey*

- **VACE has strong tendency to colorize and add warm tones**
  - Model consistently adds warm colorized tones to output videos
  - *From: DawnII*

- **VACE is trained to do grayscale to color conversion**
  - When using high quality depth maps or normal maps with VACE, it treats them as RGB grayscale inputs and goes into colorize mode
  - *From: Kijai*

- **Mediapipe face mesh captures extreme movements better than pose preprocessors**
  - Captures extreme mouth and eyebrow movements better than any pose preprocessors and pushes style further
  - *From: David Snow*

- **Fun-control can get eye movement at denoise 1.0 while VACE examples are at 0.7**
  - Control-fun can capture eye movements like eye crossing that VACE struggles with, even at higher denoise levels
  - *From: David Snow*

- **Using original video as control_images works like an insanely strong tileControlNet**
  - RGB images going in as control frames provide very strong control influence
  - *From: Draken*

- **Upscaling before making depth map or normal map helps quality loads**
  - Can use fast upscale methods like SD 1.5 TCD to improve depth/normal map quality
  - *From: deleted_user_2ca1923442ba*

- **PyTorch has been improving compile for GGUF weights**
  - They boosted the speed of GGUF weights compilation significantly
  - *From: deleted_user_2ca1923442ba*

- **FreSca is now available in the WanVideoWrapper**
  - New addition to the wrapper functionality
  - *From: Kijai*

- **UniAnimate works with Sapiens pose detection**
  - Can use Sapiens instead of just DWPose for pose guidance
  - *From: Kijai*

- **1.3B LoRAs work with Fun models and DG models**
  - Cross-compatibility between different model variants, though not as well as intended
  - *From: David Snow*

- **Fun LoRAs won't fully load on normal 1.3B model**
  - Missing image embed keys, so only partial functionality
  - *From: Kijai*

- **SkyReels version supports Wan LoRAs**
  - Benjimon's SkyReels version is very close to stock i2v model and supports Wan LoRAs
  - *From: Benjimon*

- **UniAnimate works with CFG 1.0**
  - UniAnimate works properly with CFG 1.0, but is bad when it has to add new stuff that's not in the reference
  - *From: Kijai*

- **UniAnimate purposely doesn't animate background**
  - The model is designed to focus on pose-driven animation without background animation
  - *From: Kijai*

- **UniAnimate works with multiple pose detection methods**
  - Trained with dwpose that has feet added, but works with sapiens/open pose just as well
  - *From: Kijai*

- **CFG distilled models don't work with low steps**
  - The DF model produces total garbage even at 8 steps, needs different approach than step distillation
  - *From: Kijai*

- **SageAttention and TeaCache performance boost is only 20% for some users**
  - User found that disabling both optimizations only slowed generation by 20%, much less than expected
  - *From: lostintranslation*

- **SageAttention speed increase scales dramatically with input size**
  - At higher resolution/longer videos it provides more than 100% increase, especially when attention is the bottleneck
  - *From: Kijai*

- **Hunyuan generation time is nearly 90% attention**
  - Attention dominates at higher resolutions according to thunderkittens STA paper
  - *From: deleted_user_2ca1923442ba*

- **UniAnimate works with reward LoRAs**
  - Only tested reward loras so far with UniAnimate, they did work
  - *From: Kijai*

- **UniAnimate gives everything slightly 3D look**
  - Observed effect when using UniAnimate for pose-driven animation
  - *From: Kijai*

- **UniAnimate has no speed overhead**
  - Same speed as 14B I2V, not seeing any overhead when using UniAnimate
  - *From: Kijai*

- **SkyReels 1.3B I2V model breaks in wrapper due to clip vision model**
  - Using penultimate hidden states instead of last from clip vision output fixes the issue
  - *From: Kijai*

- **SkyReels leaked weights are identical to official release**
  - Same upload dates, repo was just private temporarily
  - *From: Kijai*

- **SkyReels V2 I2V 1.3B has strong prompt following**
  - Prompt following is so strong it even ignores the image if it can't do it otherwise
  - *From: Kijai*

- **SkyReels DF model can be used asynchronously**
  - Diffusion Forcing architecture allows asynchronous usage
  - *From: Kijai*

- **VACE works with SkyReels DF models**
  - Successfully tested with 161 frames
  - *From: DawnII*

- **DF (Diffusion Forcing) models can continue from any number of frames**
  - Works better at frame continuation than VACE or Fun InP, can theoretically go forever by chaining nodes
  - *From: Kijai*

- **Only the 1.3B DF model has fps_embeds**
  - 14B DF model lacks fps embedding layers, so fps parameters won't work with it
  - *From: Kijai*

- **DF works with T2V concept using input latents**
  - Number of prefix_samples input will overwrite the noise for continuation
  - *From: Kijai*

- **addnoise_condition parameter in DF**
  - Seems to add noise and improve the new frames generated
  - *From: Kijai*

- **DF requires decode/encode between loops for quality**
  - Tried with latents directly and it degraded quality, need to decode/encode between windows
  - *From: Kijai*

- **VACE works with DF models**
  - Can combine VACE control with DF frame continuation, pushed fix to make it work properly
  - *From: Kijai*

- **Gray frames (0.5) work better than black frames for VACE**
  - Grey 127 is what the model recognizes for inpainting, use empty_frame_level 0.5 instead of 0
  - *From: DawnII*

- **1.3B LoRAs work on SkyReels models**
  - LoRAs trained on Wan base work great on SkyReelsV2-T2V-14B-720P
  - *From: mamad8*

- **SageAttention provides significant speed boost**
  - Twice as fast as SDPA with 99% quality retention
  - *From: Kijai*

- **TeaCache threshold works like step count**
  - Too high threshold skips too many steps and has huge quality hit
  - *From: Kijai*

- **Text encoder precision can be higher than model weights**
  - Can use text encoding at bf16 even with model at fp8, beneficial and separate model
  - *From: Kijai*

- **DG models are T2V only**
  - DG models are ~3GB T2V models without layers to handle clip embeds
  - *From: Kijai*

- **Native VACE is implemented as a model**
  - Can only use one VACE embed in native, not multiple like wrapper
  - *From: Kijai*

- **Wrapper torch compile works with LoRAs**
  - Compile works different with wrapper, will work with loras no problem
  - *From: Kijai*

- **VACE cannot be stacked/combined currently**
  - Each VACE includes ref, mask and control together making it difficult to mix multiple ones. Would require ~40 nodes to make it work properly
  - *From: Draken*

- **Phantom model puts reference latents at end instead of start**
  - Unlike VACE and A2 which put ref latents at start, Phantom appends them at the end
  - *From: Kijai*

- **14B DF model has massive time step embedding memory usage**
  - Time step embedding alone takes 7GB when using DF sampling. TeaCache clones timeembed for cache at ~4GB
  - *From: Kijai*

- **VACE is more sensitive to control input artifacts than base 1.3B**
  - VACE picks up on depth preprocessing artifacts like banding, making it worse for second passing when control inputs have issues
  - *From: David Snow*

- **Phantom needs 3 model predictions**
  - Based on the model structure, Phantom requires 3 separate model predictions during inference
  - *From: Kijai*

- **SkyReels V2 I2V prompting methodology focuses only on dynamics**
  - According to the paper, I2V prompts should only describe temporal action/expression/camera motion and eliminate static information like background/environment descriptions. The image provides static visual context, so prompts should focus purely on what changes over time.
  - *From: fredbliss*

- **Phantom model supports multiple reference images**
  - Phantom can take multiple reference images as input for consistent video generation, with a limit of 4 images. Images need to be encoded separately and then batched into different latents.
  - *From: Kijai*

- **CFG scheduling can replace two-pass workflows**
  - Instead of using two separate samplers, you can schedule CFG values per step in a single sampler using a list of floats (e.g., '6,6,6,6,6,1,1,1,1,1' for 10 steps)
  - *From: MilesCorban*

- **Phantom does 3 passes during sampling with 33% time overhead**
  - Phantom has no memory overhead but adds 33% sampling time due to doing 3 passes during generation
  - *From: Kijai*

- **SkyReels V2 uses structured caption fusion methodology**
  - The training uses structured captions fused specifically for I2V, focusing on action/expression/camera motion rather than detailed visual descriptions
  - *From: fredbliss*

- **Phantom works well with multiple viewpoints**
  - Tested with 4 different viewpoints as inputs to Phantom, helps a lot with fidelity of the person. Using 4 separate latents works better than feeding a grid of 2x3 images in one latent
  - *From: mamad8*

- **TeaCache skips all steps at very low thresholds**
  - At 0.13 threshold with 14B models, TeaCache skipped all conditional and unconditional steps and made generation 30% slower than baseline
  - *From: lostintranslation*

- **SLG improves hand motion but causes color burnout**
  - SLG prevents arm disappearance and improves motion, but causes snotty/burned appearance requiring lower CFG values
  - *From: lostintranslation*

- **fp16_fast provides significant speed boost**
  - Switching to pytorch nightly and using fp16_fast reduced generation time from 400s to 300s on 4080
  - *From: lostintranslation*

- **720p models work better for camera movement prompts**
  - 480p model failed to generate rotation with 'Camera slowly rotates to the right' prompt across 5 seeds, 720p model succeeded on first seed
  - *From: N0NSens*

- **Color matching fixes brightness drift in DF model**
  - DF model gets progressively brighter after first few frames when chaining videos together. Adding color match referencing initial image resolves this issue
  - *From: MilesCorban*

- **Torch compile provides speed improvement on 4090**
  - With compile: 2.94s/it, without: 4s/it on 4090 (640x480x33f)
  - *From: MilesCorban*

- **TeaCache memory usage varies dramatically by mode**
  - TeaCache mode 'e' uses 600MB while 'e0' uses 4000MB with 14B model
  - *From: Kijai*

- **Phantom works better than VACE for character consistency**
  - Phantom appears better at keeping character identity consistent compared to VACE
  - *From: NebSH*

- **VACE ending at 0.5 improves Phantom+VACE combination**
  - When combining Phantom and VACE, ending VACE at 0.5 produces better results
  - *From: Kijai*

- **SkyReels V2 supports up to 97 frames (possibly 121) at 24fps compared to base Wan's 16fps**
  - Model allows chaining infinite generations without visible seams
  - *From: seitanism*

- **fp8_fast works well with SkyReels V2 720p T2V model**
  - Provides 25% speed boost with crisp outputs, no quality degradation
  - *From: seitanism*

- **Second sampler in DF workflow uses more VRAM than first**
  - First sampler uses fewer frames in Kijai's workflow, second sampler is 17 frames more
  - *From: seitanism*

- **Teacache causes VRAM spike and memory that doesn't clear between samplers**
  - Turning off teacache prevents increased vram on subsequent samplers
  - *From: DawnII*

- **Skyreels models have oversaturated colors compared to base WAN**
  - Skyreels outputs have intensive, oversaturated colors. Adding 'natural color palette' or 'undersaturated colors' to prompts doesn't seem to change this. Base WAN has more natural coloring
  - *From: seitanism*

- **Skyreels does scene details much better than base WAN**
  - Despite color issues, Skyreels produces better details in scenes overall
  - *From: seitanism*

- **fp8_fast works with T2V but may ruin I2V quality**
  - fp8_fast gives 20-25% speed boost (4.5min to 3.5min) with T2V without noticeable quality loss, but totally destroys quality with I2V
  - *From: seitanism*

- **UniAnimate LoRA only works with 14B models, not 1.3B**
  - The UniAnimate LoRA from Kijai's HF is specifically for 14B models and doesn't work with 1.3B variants
  - *From: Kijai*

- **Skyreels V2 models are native 24fps**
  - New V2 models output native 24fps instead of 16fps, with 97 frames for 540p and 121 frames for 720p models
  - *From: Kijai*

- **fp8_fast quality degradation fix**
  - Kijai discovered that using same dtype for input and weight in fp8 scaled matmul now works, fixing the quality degradation with Wan that was caused by casting inputs to different fp8 precision
  - *From: Kijai*

- **30% speedup with fp8_fast fix**
  - The fp8_fast fix provides 30% speedup on 4000 series GPUs and up while maintaining better quality than before
  - *From: Kijai*

- **Hypercontrast style fix**
  - Adding 'natural colors. muted tones' to the end of prompts fixes the hyper-saturated, bright white highlights and pure black shadows style that Wan sometimes produces
  - *From: Screeb*

- **TeaCache frame count mismatch causes OOM**
  - Example workflow has higher frame count for subsequent samplers than first sampler, causing TeaCache to OOM - needs to be lowered to same count
  - *From: Cubey*

- **Fun 1.1 control model now includes reference image functionality similar to Animate Anyone**
  - The Control model can accept both a reference image and a control video as inputs for generation, providing effects similar to Animate Anyone while retaining original functionality
  - *From: DawnII*

- **Camera control model supports pan-and-tilt movements**
  - New camera control model supports left, right, up, down movements
  - *From: DawnII*

- **Sparge attention tuned parameters available for Wan 2.1 1.3B**
  - Sparge tuned wan 2.1 1.3b model available on HuggingFace, but tuned parameters are very model specific and limited to 1.3B T2V only
  - *From: yi*

- **Fun 1.1 control works better than 1.0 for following depth maps**
  - Fun 1.1 follows depth maps better and resolved previous issues with unwanted gesturing and talking
  - *From: boorayjenkins*

- **Reference image has limited effect when paired with start image**
  - When using both reference image and start image together, the reference image does not have much effect
  - *From: DawnII*

- **Adding noise_aug_strength of 0.03 helps motion following**
  - Adding noise_aug_strength of 0.03 back to WanVideo ImageToVideo Encode makes it follow motion correctly again
  - *From: boorayjenkins*

- **TeaCache optimization working in Phantom model**
  - TeaCache skipped 5 conditional, unconditional, and prediction_2 steps at steps [7, 9, 11, 13, 15]
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE native with auto masking system using segment anything**
  - Created workflow combining VACE native implementation with automatic masking using segment anything
  - *From: Vérole*

- **Loop_args parameter exists in WAN sampler**
  - Loop_args parameter found in sampler code but passes value as dict 'as is', samples show null values
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DG Fun model can do start/end frame morphing that VACE cannot**
  - DG model demonstrated capability for start/end frame transitions that VACE couldn't achieve
  - *From: N0NSens*

- **ComfyUI rope function fixes dtype errors**
  - Switching rope function from 'default' to 'comfy' resolves dtype mismatch errors in WAN sampler
  - *From: ˗ˏˋ⚡ˎˊ-*

- **HiDream base model outperforms Flux with no grid pattern and no 2nd pass needed**
  - Colin deleted all Flux models after trying HiDream base model
  - *From: Colin*

- **DF (1.3B 540 fp32) gives proper preview much sooner than base Wan**
  - Noticed during generation of 81 frames at 24fps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fun 1.1 models perform lot better than previous Fun models**
  - Also supports reference image now
  - *From: Kijai*

- **Fun_inp is way better than VACE for start/end images**
  - David Snow found it very impressive in testing
  - *From: David Snow*

- **CFG can be traded for very high shift values for 50% inference time reduction**
  - Setting CFG to 1 and shift to ridiculous value like 200 in vid2vid workflow with Wan 1.3 + VACE
  - *From: Pedro (@LatentSpacer)*

- **Shift values of 10-17 work well for Skyreels, especially for 14B model**
  - Good pointer for improved results
  - *From: Colin*

- **Fun models work even when feeding zeros to additional input channels**
  - They're trained to handle this gracefully
  - *From: Kijai*

- **FantasyTalking uses additional cross attention for audio conditioning**
  - Can adjust scale of attention and run extra pass with CFG control
  - *From: Kijai*

- **Fantasy Talking model has audio CFG bug fixed**
  - Missing brackets in audio CFG calculation caused sync issues, fixed as of 1h ago. Python didn't error from malformed calculation
  - *From: Kijai*

- **Fantasy Talking works beyond 81 frames**
  - Model can work with 121 frames but motion quality degrades. Uses 23fps output
  - *From: Kijai*

- **Empty audio causes Fantasy Talking sync issues**
  - Model doesn't know what to do with silence, may start lip sync from beginning despite silent audio causing offset
  - *From: Kijai*

- **Fantasy Talking effect weakens at higher resolutions**
  - Model becomes less effective at higher resolutions than its training resolution
  - *From: Kijai*

- **Fantasy Talking only supports mono audio**
  - If stereo input is provided, only first channel (left) is used
  - *From: Kijai*

- **Control LoRAs incompatible with VACE**
  - Control LoRAs modify model input channels making them incompatible with other techniques on same steps
  - *From: Kijai*

- **Multiple Fun Control inputs can be composited**
  - Instead of using multiple control nodes, composite control images on top of each other (depth + outlines + pose)
  - *From: Kijai*

- **Different seeds help prevent DirectFix overburning**
  - Using different seeds for each sampler helps prevent DF getting stuck in same output and overexposing
  - *From: Kijai*

- **Fun control models have different resolution training**
  - 1.3B models trained at 480p, 14B models trained at 720p
  - *From: Gavmakes*

- **Fun Control 1.1 models support reference images**
  - Can use either reference image or start frame, reference doesn't have to match control closely
  - *From: Kijai*

- **VACE can merge depth and normal pass controls**
  - Depth and normal merged work well, but keep other controls like lineart and pose separate
  - *From: David Snow*

- **Fantasy Talking has frame onset delay**
  - LoRA transformation always kicks in after 1 second, may be inherent to the model
  - *From: Stad*

- **720p model follows prompts better than 480p**
  - Same generation time but 720p has better prompt adherence, though can flicker at low resolutions
  - *From: N0NSens*

- **Camera control uses Google's RealEstate10K dataset**
  - Based on Google's dataset for 3D camera movements
  - *From: Kijai*

- **TeaCache disables native VACE node**
  - Both KJ nodes TeaCache and original disable VACE functionality
  - *From: Aaron Jason*

- **Using a fun ref image latent with an empty embed instead of feeding in the ref image prevents flash/blink at start**
  - Works well with no flash when using this approach
  - *From: Gavmakes*

- **14B control camera is significantly better than 1.3B**
  - Much improved camera control quality
  - *From: Kijai*

- **Empty frame level 0.5 is what the model is trained with**
  - Corresponds to 127, 127, 127 in RGB - mid gray
  - *From: Kijai*

- **Camera movements are fully customizable using Blender paths**
  - Can create custom camera trajectories in Blender and import them
  - *From: Kijai*

- **Wan I2V struggles to bring new elements into existence that aren't already in the image**
  - Works for simple additions like 'put on hat' but not for creating entirely new objects
  - *From: Draken*


## Troubleshooting & Solutions

- **Problem:** T5 TextEncoder crashing
  - **Solution:** T5 model file was corrupt - delete and redownload the file
  - *From: VK (5080 128gb)*

- **Problem:** Tiling causing black outputs
  - **Solution:** Turn off tiling - only needed for very large resolutions, VAE does 2 latents at once so length doesn't affect VRAM
  - *From: Kijai*

- **Problem:** Grey output when using Fun models with text only
  - **Solution:** Fun inpaint model is terrible at T2V, depends on control signal to infer color in some cases
  - *From: Kijai*

- **Problem:** Flash at video start with specific lora
  - **Solution:** Turning off flat color lora eliminates the flash at the start
  - *From: David Snow*

- **Problem:** First frame corruption with TeaCache
  - **Solution:** Set TeaCache start value to 10 or disable it, or use lower threshold values (0.2 works better with 20 steps)
  - *From: JohnDopamine*

- **Problem:** VAE taking forever with long sequences
  - **Solution:** Disable tiling - length doesn't affect VRAM use as VAE processes 2 latents at once
  - *From: Kijai*

- **Problem:** SageAttention error in CLIP vision encode
  - **Solution:** Probably using wrong clipvision model
  - *From: ameasure*

- **Problem:** VACE flashy/bad results
  - **Solution:** Turn off 'batched cfg' on the sampler
  - *From: TK_999*

- **Problem:** Expected all tensors to be on the same device error
  - **Solution:** Remove block swap node when using VACE
  - *From: Draken*

- **Problem:** Reference image not working properly
  - **Solution:** Pad the image and place on white background, remove first latent
  - *From: Kijai*

- **Problem:** Control depth not working with VACE
  - **Solution:** Disconnect control depth input to fix generation issues
  - *From: makeitrad*

- **Problem:** OOM on 24GB with 33 frames
  - **Solution:** Use quantization (fp8_e4m3fn) and proper precision settings
  - *From: CJ*

- **Problem:** VACE embeds widget disappeared from wrapper sampler
  - **Solution:** Updated to go into image_embeds input instead
  - *From: Hashu*

- **Problem:** Masking input video causes errors
  - **Solution:** Don't mask input video, mask the reference image instead. Model doesn't like alpha channels
  - *From: VK (5080 128gb)*

- **Problem:** Reference image resolution mismatch causes errors
  - **Solution:** Keep reference image resolution consistent, errors occur when changing to different resolutions like 480x832
  - *From: slmonker(5090D 32GB)*

- **Problem:** Style transfer not working with background
  - **Solution:** Remove background completely from reference image, model trained to look for refs separated by white background
  - *From: ingi // SYSTMS*

- **Problem:** Oversaturated and plastic-looking outputs
  - **Solution:** Turn off SLG or use specific SLG settings: block 8 with 0.1 start to 0.3-5 end
  - *From: IllumiReptilien*

- **Problem:** Flashing and color shifting on wider aspect ratios
  - **Solution:** Resize to 16:9 720p to stop flashing
  - *From: Faux*

- **Problem:** TeaCache not working great with VACE
  - **Solution:** Use threshold around 0.1 instead of normal 0.015
  - *From: Kijai*

- **Problem:** VACE reference not passed for context windows
  - **Solution:** Known limitation that ref image isn't passed for context windows
  - *From: Kijai*

- **Problem:** TeaCache memory issue with VACE
  - **Solution:** Fixed memory leak in TeaCache - reduced max reserved memory from 22.250 GB to 17.031 GB for 81 frames at 480x832
  - *From: Kijai*

- **Problem:** WanModel object has no attribute 'vace_blocks'
  - **Solution:** Need to update Wan nodes to latest version, not just ComfyUI
  - *From: Kijai*

- **Problem:** torch._scaled_mm error on RTX 3060
  - **Solution:** Don't use fp8_fast models on cards with compute capability < 9.0. Use regular fp8 models instead
  - *From: Faux*

- **Problem:** DPM++_SDE convergence changed after timestep fix
  - **Solution:** Switch to Euler scheduler which works properly after the fix
  - *From: DevouredBeef*

- **Problem:** OOM issues on 12GB VRAM with VACE
  - **Solution:** Use 27+ block swap, reduce resolution to 480x480 and frames to 33 initially, then scale up
  - *From: zelgo_*

- **Problem:** VACE outputs turning orange
  - **Solution:** Use proper masking with gray areas for missing parts
  - *From: amli*

- **Problem:** Getting weird VACE outputs
  - **Solution:** Need the TE bridge for proper setup
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** VACE outputting portrait instead of landscape
  - **Solution:** Disable 'swap dimensions' in CR SD1.5 Aspect Ratio node
  - *From: Ashtar*

- **Problem:** Workflow freezing when dragging
  - **Solution:** Update ComfyUI frontend to resolve compatibility issues
  - *From: seitanism*

- **Problem:** RuntimeError about tensors on different devices
  - **Solution:** One node may be on CPU when should be CUDA
  - *From: PirateWolf*

- **Problem:** VACE outputs video too bright
  - **Solution:** Try color match node hooking input vid to ref
  - *From: LarpsAI*

- **Problem:** Triton error on Windows
  - **Solution:** Clear Triton cache
  - *From: Kijai*

- **Problem:** Resolution not working with 856
  - **Solution:** Changed to 848 and it works, may need divisible by 16
  - *From: traxxas25*

- **Problem:** Sageattention bfloat/headdim errors
  - **Solution:** Remove TRELLIS and Hi3DGen nodes - they override global attention which should never be done
  - *From: Kijai*

- **Problem:** VACE OOMs and memory issues during inference
  - **Solution:** Use VACE block swap feature and ensure you're on latest commit with TeaCache memory bug fix
  - *From: Kijai*

- **Problem:** Wrong model error when switching between Wan models
  - **Solution:** Purge VRAM and reload models when changing between Fun 1.3B and 14B variants
  - *From: Seb*

- **Problem:** VACE always skipping step 0
  - **Solution:** Major bug fixed - start/end percent check was broken, now properly handles first step
  - *From: Kijai*

- **Problem:** Black video outputs with latest WanWrapper version
  - **Solution:** Use ComfyUI text encoding with the bridge instead of wrapper's built-in encoding
  - *From: Kijai*

- **Problem:** Tensor size mismatch error with VACE Encode
  - **Solution:** Check for Load Video node with select_every_nth parameter causing frame count discrepancy
  - *From: mamad8*

- **Problem:** Hot mess/noisy orange output with VACE workflow
  - **Solution:** Ensure pad node is connected and reference image is on white canvas
  - *From: Kijai*

- **Problem:** Gray halo around head when mask is too large
  - **Solution:** Reduce mask size to avoid artifacts
  - *From: Zuko*

- **Problem:** Skeleton/corrupted outputs with control
  - **Solution:** Check latent strength settings and image blend node clipping
  - *From: Kijai*

- **Problem:** FlowMatchEulerDiscreteScheduler error with use_beta_sigmas
  - **Solution:** Update nodes or use UniPC scheduler as alternative
  - *From: David Snow*

- **Problem:** Compile broken with teacache in latest wrapper
  - **Solution:** Only compile transformer blocks instead of full model
  - *From: Kijai*

- **Problem:** OOM with 81 frames on 12GB VRAM
  - **Solution:** Use vace block to swap=15 and normal block swap=30, or reduce frame count
  - *From: Ashtar*

- **Problem:** WanVideo BlockSwap error with VACE workflow
  - **Solution:** Set VACE blocks to more than 0 when using block swap, can be 1-15
  - *From: Kijai*

- **Problem:** Shape error with custom heights
  - **Solution:** Height and width must be divisible by 16, not just 8
  - *From: Kijai*

- **Problem:** Two different devices cuda:0 error
  - **Solution:** Add 1 VACE block to swap or disconnect swap blocks node
  - *From: JohnDopamine*

- **Problem:** Lotus model error
  - **Solution:** Wrong VAE - needs to use the 1.5 VAE, not other VAEs
  - *From: JmySff*

- **Problem:** Getting only 4 images in output
  - **Solution:** Check number of control images - output matches number of control images provided
  - *From: mamad8*

- **Problem:** Bone artifacts appearing in outputs
  - **Solution:** Use base model instead of DG, or reduce VACE strength
  - *From: IllumiReptilien*

- **Problem:** Memory allocation errors when canceling workflows
  - **Solution:** Use unload models button at the top, though it takes time
  - *From: David Snow*

- **Problem:** Orange tinted outputs in VACE
  - **Solution:** Use correct text encoder - fp8 scaled with upper group, bf16 from KJ with lower group
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Tensor error with negative dimension when doubling VACE embeds
  - **Solution:** Need reference image in both VACE nodes, can use blank grey image
  - *From: DawnII*

- **Problem:** Poor likeness with VACE inpainting
  - **Solution:** Remove background fully from reference, check resizing settings to avoid stretching
  - *From: Kijai*

- **Problem:** Pose dots appearing in final output
  - **Solution:** Issue occurs when overlaying DWPose on top of Depthmap in black
  - *From: burgstall*

- **Problem:** Black output with I2V and SageAttention on auto mode
  - **Solution:** Set SageAttention to disabled or manual mode instead of auto
  - *From: Kijai*

- **Problem:** Expected all tensors to be on the same device CUDA error with Grounding Dino
  - **Solution:** Replace the problematic node with the lower/alternative version
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Problem:** Tight shaped mask forcing unwanted shapes in output
  - **Solution:** Try using box mask instead of character cutout shapes
  - *From: Kijai*

- **Problem:** TeaCache causing mosaic/noisy output with low step counts
  - **Solution:** Use higher step counts (20+ steps) or lower threshold values, avoid with ancestral/SDE samplers
  - *From: Kijai*

- **Problem:** Ming nodes brightness/contrast not working with multiple frames
  - **Solution:** Use dzNodes brightness adjustment instead
  - *From: Vérole*

- **Problem:** Pose dots bleeding through in VACE output
  - **Solution:** Issue with overlayed controlnets - VACE doesn't play well with them
  - *From: traxxas25*

- **Problem:** Depth video showing outside mask area
  - **Solution:** Mask the depth map before feeding into VACE, or use original video with mask overlay
  - *From: traxxas25*

- **Problem:** ComfyUI loading wheel spinning indefinitely after update
  - **Solution:** Reinstall ComfyUI from scratch, then install custom nodes in small batches of 2 at a time through manager
  - *From: David Snow*

- **Problem:** Video-depth-anything preprocessor giving OOM after install
  - **Solution:** Switch to depthcrafter preprocessor, or ensure xformers is working properly as depth anything relies on it
  - *From: David Snow*

- **Problem:** Control networks destroying character consistency
  - **Solution:** Try lower control strength, or mask out faces from control maps if possible. Issue affects both face and clothing consistency
  - *From: wange1002*

- **Problem:** SkyreelsA2 VACE node error
  - **Solution:** Use normal I2V workflow instead of VACE nodes - SkyreelsA2 has nothing to do with VACE
  - *From: Kijai*

- **Problem:** VACE first/last frame not smooth interpolation
  - **Solution:** Try higher shift values (up to 35), interpolate more frames between start/end if too much difference, or create character LoRA for better likeness
  - *From: DawnII*

- **Problem:** Blender depth maps don't work with VACE
  - **Solution:** Add 3 pixel blur to the depth map - even minimal blur fixes the issue
  - *From: Kijai*

- **Problem:** CLIP images must be squares and center cropped by default
  - **Solution:** Make sure reference image fits the offset position when using bear offset
  - *From: Kijai*

- **Problem:** Lineart showing white lines in final render
  - **Solution:** Invert colors for lineart control input
  - *From: JmySff*

- **Problem:** Target width/height padding not working
  - **Solution:** Disconnect the target_width and height inputs completely, don't use 0 or -1
  - *From: Kijai*

- **Problem:** Context window transitions visible in background
  - **Solution:** Use control for background or accept that uncontrolled areas will change between windows
  - *From: Kijai*

- **Problem:** OOM errors with SAM2 nodes
  - **Solution:** No specific solution provided, user seeking help
  - *From: PirateWolf*

- **Problem:** Torch weights loading error with newer PyTorch versions
  - **Solution:** Set weights_only=False in torch.load or use safe_globals context manager
  - *From: Ashtar*

- **Problem:** VACE doesn't work well with blurred/faded masks
  - **Solution:** Use solid masks without blur for better results, blurred masks leave artifacts on edges
  - *From: A.I.Warper*

- **Problem:** Image dimensions causing broadcasting errors in i2v
  - **Solution:** Image dimensions need to be divisible by 16, round to nearest multiple of 16
  - *From: traxxas25*

- **Problem:** VACE inserting unwanted people in masked areas
  - **Solution:** Ensure bounding box completely covers subject, mask shadows/reflections, and tint mask color to match background
  - *From: traxxas25*

- **Problem:** TeaCache not showing status and running slower after ComfyUI update
  - **Solution:** Issue with automated memory management and patches, use --reserve-vram startup argument
  - *From: Scrap*

- **Problem:** Wireframe control not working well
  - **Solution:** Use line extraction instead of wireframe for better results
  - *From: Juan Gea*

- **Problem:** FP8_E5 compilation not working on 30-series
  - **Solution:** Works with torch 2.7 and triton 3.1.0, need to delete .triton cache
  - *From: Hashu*

- **Problem:** Getting fewer output frames than input control frames
  - **Solution:** Issue observed with VACE start/end frame - 24 frames in, 21 frames out
  - *From: notid*

- **Problem:** Flashing and artifacts in vid2vid refinement
  - **Solution:** Keep denoise above 0.5, control with latent strength, end percent and cfg. Low denoise causes weird flashing
  - *From: HeadOfOliver*

- **Problem:** Native T2V not working
  - **Solution:** Must provide start_image and clip vision for native T2V to work
  - *From: BondoMan*

- **Problem:** Last 3 frames always black in native I2V
  - **Solution:** Issue was using VAE decode (tiles) - using normal VAE decode solved it
  - *From: Kaïros*

- **Problem:** OOM on RTX 2080 with bf16
  - **Solution:** RTX 2080 doesn't fully support bf16 - switch to fp16 precision for VAE loader and model loader
  - *From: Kijai*

- **Problem:** T5 text encoder fp16 issues
  - **Solution:** Original T5 text encoder won't work in fp16 - use bf16 or native text encoding setup with fp8 scaled
  - *From: Kijai*

- **Problem:** Spotty results with weird contrast using WanSampler
  - **Solution:** Issue was text encoder precision - don't use T5 wrapper in fp16, use bf16 or comfy native loader
  - *From: Kijai*

- **Problem:** Fun Control workflow loading with wrong connections
  - **Solution:** Control Embeds connected to Extra Latents needs to be manually changed after loading example workflow
  - *From: The Shadow (NYC)*

- **Problem:** OOM errors on A4500 system
  - **Solution:** Kijai fixed something that resolved strange OOM error
  - *From: The Shadow (NYC)*

- **Problem:** Tiled encoding was broken in original code
  - **Solution:** Was being set in latent space then doing in pixel space, fixed to work properly
  - *From: Kijai*

- **Problem:** Video-depth-anything instant OOMs on fresh ComfyUI install
  - **Solution:** Install xformers to resolve the issue
  - *From: David Snow*

- **Problem:** VACE tensor shape mismatch with denoise less than 1
  - **Solution:** Need to pad input frames to match, duplicate first frame x4 and add to front
  - *From: Kijai*

- **Problem:** Triton recompile errors after model code changes
  - **Solution:** Clear Triton cache by deleting temp folder contents
  - *From: zelgo_*

- **Problem:** ComfyUI freezing when loading VACE workflow during generation
  - **Solution:** Only load workflows when not running generation
  - *From: DawnII*

- **Problem:** Missing WanVACEFaceSwap node
  - **Solution:** Reinstall WanVideo wrapper, using older version
  - *From: xwsswww*

- **Problem:** Block swap can't be set to 0
  - **Solution:** Set block swap to non-zero value
  - *From: Faust-SiN*

- **Problem:** Teacache skips all steps with conditioning combine nodes
  - **Solution:** Play with start and end settings of teacache to make it work
  - *From: JmySff*

- **Problem:** Key errors when using reward loras with 1.3B model
  - **Solution:** Expected behavior - normal 1.3B doesn't have img cross attention keys, only I2V models do. Everything else still loads and has effect
  - *From: Kijai*

- **Problem:** Freezing issues during generation
  - **Solution:** Update dependencies for custom nodes - exact cause unclear but dependency updates resolved the issue
  - *From: xwsswww*

- **Problem:** Core dumped crashes on Ubuntu with 5090
  - **Solution:** Check dmesg for GPU-related issues, verify correct clip model is being used
  - *From: MilesCorban*

- **Problem:** Tensor size mismatch error (16320 vs 57120)
  - **Solution:** Update to latest wrapper - Kijai fixed it to automatically pad the encoded video
  - *From: Kijai*

- **Problem:** Torch compile recompile errors
  - **Solution:** Fixed (hopefully) at least some of the torch compile recompile errors last night
  - *From: Kijai*

- **Problem:** Black frames in normal vid2vid when using context options
  - **Solution:** Known issue with context options on 14b model normal wrapper vid2vid
  - *From: Flipping Sigmas*

- **Problem:** Mask showing as fog in vid2vid with low denoise
  - **Solution:** Use proper control model like VACE or Fun Inpaint instead of latent masking with base t2v model. Apply gaussian noise to the mask
  - *From: DawnII*

- **Problem:** Tensor mismatch with pose estimator
  - **Solution:** Make sure pose estimator is set to correct resolution matching your video
  - *From: Roman_S*

- **Problem:** Reference image flashing at beginning of video
  - **Solution:** Caused by using saved latent node from ComfyUI core - use load video node instead
  - *From: Johnjohn7855*

- **Problem:** Xformers AttributeError after node updates
  - **Solution:** Disable quantization on the model - xformers not used by Wan nodes but triggered by diffusers
  - *From: Impactframes.*

- **Problem:** OOM issues with video depth
  - **Solution:** Had to reduce video depth to 512, potential memory leak in depth processing
  - *From: traxxas25*

- **Problem:** Control embeds not affecting results at 100% denoise
  - **Solution:** Control lora not strong enough for 1.0 denoise setting - reduce denoise or use stronger control
  - *From: David Snow*

- **Problem:** Color shift in VACE results
  - **Solution:** Better prompting - removed 'warm' from 'warm dimly lit hotel lobby' prompt
  - *From: traxxas25*

- **Problem:** Invalid WanVideo model selected error
  - **Solution:** VACE models need to be used in VACE nodes, not regular WAN nodes. Use the correct model type for each node
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Problem:** Need both VACE model and base WAN model
  - **Solution:** If using the basic VACE-only model, you need to use it WITH the original WAN model. The merged VACE models only need one file
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Problem:** VACE doesn't like input masks with holes
  - **Solution:** VACE has issues with masks that contain holes in them
  - *From: IllumiReptilien*

- **Problem:** Style drifting in vid2vid generations
  - **Solution:** More reference frames are needed, and reward/high res fix loras have bias towards realism so process without them first then add on second pass
  - *From: Hashu*

- **Problem:** First couple frames have reference image burned in
  - **Solution:** Try using neutral gray or white image as ref in embed with control, or pad the front of the video
  - *From: Kijai*

- **Problem:** Frame count mismatch in outputs
  - **Solution:** VHS has to round frame counts based on FPS settings. 81 frames at 16 FPS doesn't fit evenly into 5 seconds
  - *From: Kijai*

- **Problem:** Tensor size mismatch when using reference image in VACE
  - **Solution:** Update ComfyUI-WanVideoWrapper - reference images are now automatically padded
  - *From: Kijai*

- **Problem:** Blue bar on right side of video with Skip Layer Guidance
  - **Solution:** Reduce CFG by half (use CFG 3 instead of 6) and set SLG blocks to 8 or (8,9) instead of 10 for 14B models
  - *From: N0NSens*

- **Problem:** Model loading error when model name doesn't contain '720' or '480'
  - **Solution:** Model names must include numbers '720' or '480' to avoid 'model_variant referenced before assignment' error
  - *From: Kytra*

- **Problem:** TeaCache conflicts with certain step counts
  - **Solution:** If video output becomes noisy or strange with Tea Cache, try disabling it
  - *From: David Snow*

- **Problem:** Context windows don't work well with TeaCache
  - **Solution:** TeaCache too strong for context windows, reduce TeaCache strength or disable
  - *From: Kijai*

- **Problem:** Darkening in middle of video with Fun InP first-end frame workflow
  - **Solution:** Identified as style drift issue, happens consistently across different content types
  - *From: Blink*

- **Problem:** OptimalStepsSchedule produces black output
  - **Solution:** Doesn't work with unipc, only works with Euler and dpm samplers
  - *From: Kijai*

- **Problem:** Can't right click VideoHelperSuite video combine node to save video
  - **Solution:** Issue related to new UI update
  - *From: David Snow*

- **Problem:** ComfyUI won't restart after update with AIOHTTP error
  - **Solution:** Problem was caused by Jovimetrix custom node - removing it fixed the issue
  - *From: AJO*

- **Problem:** Tensor size mismatch when using mask with WanVideoEncode in VACE v2v
  - **Solution:** Remove mask from encode since mask is already provided in VACE encode
  - *From: hablaba*

- **Problem:** Context options changing style completely
  - **Solution:** Start frames won't be part of windows that aren't the first, but reference images work because they're added to each context manually and aren't positional
  - *From: Kijai*

- **Problem:** Black frame outputs
  - **Solution:** Update ComfyUI, frontend, Kijai nodes, and WanWrapper. Also refresh and try duplicating nodes then relinking
  - *From: Flipping Sigmas*

- **Problem:** Cannot use euler/beta scheduler
  - **Solution:** Need to update WanVideoWrapper to latest version
  - *From: Jas*

- **Problem:** Washed out colors at start of generation
  - **Solution:** Try switching off enhance-a-video node
  - *From: N0NSens*

- **Problem:** VACE producing distorted and dark first frames
  - **Solution:** Issue with VACE inpainting causing gradual color recovery
  - *From: PirateWolf*

- **Problem:** Results degrading until cache cleared
  - **Solution:** Use 'Free model and node cache' to prevent degradation
  - *From: Ro*

- **Problem:** SageAttention 2.0 installation issues on Windows
  - **Solution:** Windows dev environment weirdness with CUDA paths - need CUDA 12.8 but PATH may point to 11.8
  - *From: lostintranslation*

- **Problem:** CUDA 12.8 not being detected despite installation
  - **Solution:** Purge all old CUDA installations and reinstall with PATH configuration
  - *From: Kijai*

- **Problem:** Quality degrades after 1-2 generations with native + kjnodes
  - **Solution:** Manually clear VRAM after each generation - bug with patch nodes and ComfyUI lowvram mode
  - *From: Kijai*

- **Problem:** Blurry outputs in Wan generations
  - **Solution:** Increase steps to at least 20, adjust TeaCache start_step to 2 or 3
  - *From: MilesCorban*

- **Problem:** Fun Control breaks with end image
  - **Solution:** Both Fun Control models don't support end image, only VACE supports start/end images with controlnet
  - *From: DawnII*

- **Problem:** Color flash at loop reset
  - **Solution:** Set an end image and try color matching, though color matching isn't perfect
  - *From: DawnII*

- **Problem:** LoRAs don't work with torchcompile
  - **Solution:** Use ModelPatcher node as workaround - compile applies first, then loras (weight patch)
  - *From: Kijai*

- **Problem:** GGUF and LoRAs use more VRAM and slow down significantly
  - **Solution:** Use fp8 scaled models instead, or drop to Q5 GGUF. Every lora added slows GGUF down more
  - *From: Kijai*

- **Problem:** TeaCache bug with end steps causing generation failures
  - **Solution:** Fixed in latest update, was aware of bug but kept forgetting to fix it
  - *From: Kijai*

- **Problem:** Deep fried/corrupted images in later workflows
  - **Solution:** Something getting cached wrong affecting later workflows
  - *From: lostintranslation*

- **Problem:** Resolution error when changing from lowres to 832x480
  - **Solution:** Need to change other matching parameters besides just resolution
  - *From: N0NSens*

- **Problem:** VACE depth map results in black and white outputs
  - **Solution:** Reduce VACE strength significantly, but then it doesn't follow starting/ending frames as well
  - *From: Sway*

- **Problem:** 14B LoRAs don't work on 14B Fun model but 1.3B LoRAs work on 1.3B Fun
  - **Solution:** Fun models have more keys due to img cross attention, ComfyUI reports keys NOT applied but applies the rest
  - *From: Kijai*

- **Problem:** Quality degradation over multiple i2v generations in queue
  - **Solution:** Clear VRAM cache after each generation to prevent permanent degradation
  - *From: lostintranslation*

- **Problem:** Black frames output in multiple LoRA workflow
  - **Solution:** Related to optimizations like sageattn or torch.compile casting
  - *From: MilesCorban*

- **Problem:** FramePack showing black videos in Gradio
  - **Solution:** Gradio glitch - check output folder for correct saved video
  - *From: Benjimon*

- **Problem:** CLIP encode node error in new nodes
  - **Solution:** Need to concat (not average) the 2 image embeds in clip encode node
  - *From: Kijai*

- **Problem:** CUDA out of memory error
  - **Solution:** Check if it's actually RAM issue not VRAM - allocation error = VRAM, other errors often mean out of RAM
  - *From: Kijai*

- **Problem:** FLF2V model producing still results with same start/end image
  - **Solution:** Try higher CFG (7-10), full 1.0 motion lora, but higher CFG introduces artifacts
  - *From: Eclipse*

- **Problem:** VACE blur issues with depth control on anime style
  - **Solution:** Try lineart instead of depth control, depth maps being too flat can cause camera distance confusion
  - *From: Kijai*

- **Problem:** VACE not following reference image
  - **Solution:** Use first frame as encoded latent with proper temporal masking instead of just reference
  - *From: Kijai*

- **Problem:** Bad reference adherence in VACE
  - **Solution:** Bump shift to double digits like 20-30, counter to base models
  - *From: DawnII*

- **Problem:** Quality degradation when stitching multiple video runs together
  - **Solution:** Lower CFG and use color match node on the transition frame to maintain consistency
  - *From: A.I.Warper*

- **Problem:** Multiple VAE passes causing degradation
  - **Solution:** Every decode/encode cycle degrades quality - minimize the number of VAE passes
  - *From: DawnII*

- **Problem:** LoRA-induced degradation between batches
  - **Solution:** Clear VRAM between batches with different LoRAs using a dedicated clear VRAM workflow
  - *From: lostintranslation*

- **Problem:** VACE producing distorted results when control and reference don't align
  - **Solution:** Start image should be close to the control, reference image doesn't necessarily need to mimic control
  - *From: DawnII*

- **Problem:** FramePack generating fixed backgrounds without movement
  - **Solution:** Increase tile size for better quality, try higher resolution generation like 720x1280
  - *From: deleted_user_2ca1923442ba*

- **Problem:** 3090 fp8 compatibility issues with torch inductor
  - **Solution:** Use fp8_e5m2 weights with torch compile, or use SageAttention 2.0+ with direct cuda mode instead of Triton
  - *From: Kijai*

- **Problem:** Cannot import cached_download from huggingface_hub
  - **Solution:** Updated the module so imports are in the nodes, shouldn't try to import huggingface_hub anymore
  - *From: Kijai*

- **Problem:** Model variant error when loading merged I2V model
  - **Solution:** Rename the model to include 480 or 720 in filename, or update wrapper which defaults to 14B detection
  - *From: Kijai*

- **Problem:** ComfyUI freezing after producing output
  - **Solution:** Multiple users experiencing this after latest update, suggested solution is to reinstall from scratch
  - *From: lomerio*

- **Problem:** High quality depth maps not working with VACE
  - **Solution:** Blur the depth maps - VACE sees high quality depth as grayscale RGB and goes into colorize mode
  - *From: Kijai*

- **Problem:** Out of memory on VideoDepthAnythingProcess
  - **Solution:** Use DepthAnythingV2 which is less resource intensive, or lower input size
  - *From: David Snow*

- **Problem:** Out of memory on WanVideoDecode
  - **Solution:** Enable VAE tiling
  - *From: David Snow*

- **Problem:** UniAnimate tensor size mismatch error
  - **Solution:** Match all sizes - resolution and frame count between inputs
  - *From: Kijai*

- **Problem:** White particles appearing in generations
  - **Solution:** Lower the extra noise detail motion LoRA strength - too high causes this
  - *From: David Snow*

- **Problem:** ConnectionResetError at end of generation
  - **Solution:** Can be ignored unless something actually breaks
  - *From: David Snow*

- **Problem:** Fast motion and hands getting blurry
  - **Solution:** Turn off optimizations like SageAttention for better quality
  - *From: Benjimon*

- **Problem:** use_fresca toggle not working properly
  - **Solution:** Bug reported - toggle does nothing, always activates if scale is set
  - *From: Juampab12*

- **Problem:** OOM errors in depth preprocessing
  - **Solution:** Decrease input size and max res in the node, or use DepthAnything V2 which is less resource intensive
  - *From: David Snow*

- **Problem:** Reference images cause artifacts in VACE
  - **Solution:** Disabling reference image eliminates flashes at start and glitches - no known fix for using reference images
  - *From: David Snow*

- **Problem:** Video distortion with 1.3B model
  - **Solution:** Try 200 steps of DPM++ 2SA with eta=2.0 to eliminate temporal attention issues
  - *From: deleted_user_2ca1923442ba*

- **Problem:** Preprocessors pegging VRAM after update
  - **Solution:** Full restart resolved the issue
  - *From: David Snow*

- **Problem:** Oversharpened upscaling artifacts
  - **Solution:** Use RealESRGAN_x4plus_anime_6B instead of AnimeSharp for cleaner results
  - *From: gshawn*

- **Problem:** TeaCache node not properly disabling
  - **Solution:** Node uses global patch, won't disable unless it runs again. When set to disabled it restores default attention mode. Remove launch parameter and restart.
  - *From: Kijai*

- **Problem:** UniAnimate tensor size mismatch error
  - **Solution:** UniAnimate is for 14B only, won't work with other models or when combined with VACE
  - *From: Kijai*

- **Problem:** DWPose detection failures causing workflow crashes
  - **Solution:** DWPose is not perfect and will fail on some videos. Added workaround to handle failed detections.
  - *From: Kijai*

- **Problem:** VACE oversaturated outputs with tile control
  - **Solution:** Second pass processing, no combination of settings seems to eliminate it completely
  - *From: David Snow*

- **Problem:** Flash at start of vid2vid style transfer
  - **Solution:** Changing control embed start to 1 from 0 gets rid of flash but introduces more movement
  - *From: Gavmakes*

- **Problem:** Wan wrapper update breaking workflows
  - **Solution:** Update nodes after updating wrapper, issue was already fixed
  - *From: Kijai*

- **Problem:** SkyReels 1.3B I2V not working in wrapper
  - **Solution:** Use penultimate hidden states from clip vision instead of last, or use wrapper clip vision node instead of native loader
  - *From: Kijai*

- **Problem:** Torch update needed for new model
  - **Solution:** Update torch or use wrapper clip vision node
  - *From: Kijai*

- **Problem:** FLF jumping to last frame instead of morphing
  - **Solution:** Use camera movement prompts instead of scene details
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Second video in naive extension looks 'squished'
  - **Solution:** Requires color correction, use VACE or Fun inp instead
  - *From: Parker*

- **Problem:** WanVideoDiffusionForcingSampler error about latent preview module
  - **Solution:** Turn ON latent preview - error comes from having it off, fallback fails due to relative path issue
  - *From: Kijai*

- **Problem:** LoRA degradation issue with repeated generations
  - **Solution:** Clear VRAM between generations, issue may be related to rgthree power lora loader
  - *From: lostintranslation*

- **Problem:** VACE strength control confusion
  - **Solution:** Use two separate VACE encode nodes with different strength settings for different controls
  - *From: Hashu*

- **Problem:** VACE bad results in native
  - **Solution:** Should be fixed now (Python whitespace issue)
  - *From: comfy*

- **Problem:** System memory fallback causing slowdown
  - **Solution:** Activate 'prefer no system fallback' in Nvidia control panel
  - *From: zelgo_*

- **Problem:** Strong edge results with VACE + canny
  - **Solution:** Use black lines on white background, anyline is better choice than canny
  - *From: David Snow*

- **Problem:** Swimming noise on rock textures
  - **Solution:** Try lower CFG around 3.5-4.0 and shift around 4.0, avoid word 'wiggle' in prompt
  - *From: Kytra*

- **Problem:** Expected all tensors to be on same device error
  - **Solution:** Issue was VRAM management, fixed in latest update
  - *From: Dream Making*

- **Problem:** TeaCache console message when disabled
  - **Solution:** Generic console message when set to offload device
  - *From: David Snow*

- **Problem:** CUDA error with VACE when using first frame as ref_images
  - **Solution:** Try setting non-blocking to False when offloading blocks, or reboot system as error may be random
  - *From: Stad*

- **Problem:** Torch compile eating all memory with DF models
  - **Solution:** Issue with torch compile on DF models currently, avoid using compile with DF sampling
  - *From: Kijai*

- **Problem:** Video depth flipping in output
  - **Solution:** Re-encode the input video file to fix format issues
  - *From: David Snow*

- **Problem:** TeaCache not clearing between sampler nodes causing OOM
  - **Solution:** TeaCache doesn't clear cache between sampler nodes on 2nd sampler if first had entries
  - *From: jellybean5361*

- **Problem:** Missing workflow connections
  - **Solution:** Check all node connections as workflows can have many missing inputs
  - *From: David Snow*

- **Problem:** First frame corruption/artifacts in generated videos
  - **Solution:** Try toggling 'use_coefficients' on TeaCache or disconnect TeaCache completely. May be related to low step counts.
  - *From: JohnDopamine*

- **Problem:** MultiGPU setup causing OOM and device mismatch errors
  - **Solution:** Put model on 4090 and VAE+text on 3090. There's a known bug with MultiGPU nodes causing 'Expected all tensors to be on the same device' error.
  - *From: MilesCorban*

- **Problem:** Second pass in split workflows producing completely different slow motion video
  - **Solution:** Use lower denoise value (not 1.0) for second pass, as denoise 1.0 creates completely new video. Denoise is the ratio of new vs old content.
  - *From: Kijai*

- **Problem:** TAESD preview warning about missing models/vae_approx/None
  - **Solution:** Download taew2_1.safetensors and place in vae_approx folder. The warning can be ignored but proper file fixes preview functionality.
  - *From: David Snow*

- **Problem:** First frame corruption in I2V
  - **Solution:** Use longer videos (50+ frames), avoid very short clips like 1 second generations for testing
  - *From: TK_999*

- **Problem:** VACE line art issues
  - **Solution:** Making edge maps binary helps improve results
  - *From: Rishi Pandey*

- **Problem:** TeaCache causing slowdowns at low threshold
  - **Solution:** Use higher threshold like 0.25 for 14B models instead of 0.13, which is too low
  - *From: Kijai*

- **Problem:** DF model works poorly with torch compile
  - **Solution:** Disable torch compile when using DF model
  - *From: Kijai*

- **Problem:** Block swap causing OOM on 81 frames
  - **Solution:** Use 20 blocks for 81 frames on 16GB VRAM instead of 10
  - *From: lostintranslation*

- **Problem:** Burning/oversaturation with CFG
  - **Solution:** Left image burning indicates CFG too high or layer skipping issues
  - *From: Piblarg*

- **Problem:** Weird colored output in VACE workflow
  - **Solution:** Works with depth control but not with blend of depth and lineart
  - *From: TheSwoosh*

- **Problem:** mat1 and mat2 dtype error
  - **Solution:** Set base_precision to fp32, then use fp8 scaled clip
  - *From: Ablejones*

- **Problem:** CUDA out of memory on RTX 3090 with 14B model
  - **Solution:** Disable teacache or set mode to 'e' instead of 'e0', also try disabling compile
  - *From: Ablejones*

- **Problem:** Optimizations causing artifacts in chained videos
  - **Solution:** Disable teacache and switch from fp8e4m3_fast to fp8e4m3 to fix artifacts that compound over time
  - *From: MilesCorban*

- **Problem:** Character giving up on motion in extensions
  - **Solution:** Try bigger frame overlap and more specific prompts
  - *From: seitanism*

- **Problem:** First frame corruption
  - **Solution:** Likely caused by too few frames generated, doesn't happen when running 81 frames
  - *From: lostintranslation*

- **Problem:** VRAM leak when canceling workflow during sampling
  - **Solution:** Use clear models and clear cache buttons when canceling mid-way
  - *From: seitanism*

- **Problem:** OOM at second sampler in DF workflow
  - **Solution:** Turn off teacache to prevent memory buildup between samplers
  - *From: DawnII*

- **Problem:** Color brightness increase after multiple DF generations
  - **Solution:** Use color matching node to maintain consistent colors
  - *From: seitanism*

- **Problem:** Width and height are flipped causing generation issues
  - **Solution:** Check aspect ratios of images (height/width)
  - *From: DawnII*

- **Problem:** WanModel object has no attribute 'dwpose_embedding' error
  - **Solution:** This occurs when trying to use UniAnimate with 1.3B models - the LoRA only exists for 14B models
  - *From: Nokai*

- **Problem:** Input video length causing tensor size mismatch in DF
  - **Solution:** Can't input more frames than the generation frame count is set to. Need to extract last x frames from input, not the whole video
  - *From: TK_999*

- **Problem:** WAN forces frame counts to 4n+1 rule
  - **Solution:** Models require frame counts following 4n+1 pattern (65, 69, 81, etc). Can't generate 67 frames - will output 65 instead
  - *From: DeZoomer*

- **Problem:** OOM issues with DF models
  - **Solution:** Need to unload blocks - user reports needing to unload all 40 blocks for 1280x720x81 generation
  - *From: slmonker*

- **Problem:** torch.compile issues on 3000 series GPUs
  - **Solution:** Use e5m2 precision instead of e4 for 3000 series GPUs when wanting to use torch.compile
  - *From: Kijai*

- **Problem:** TeaCache OOM on second sampler
  - **Solution:** Lower frame count on subsequent samplers to match first sampler, or turn off teacache entirely
  - *From: Cubey*

- **Problem:** OOM at specific step with torch compile
  - **Solution:** Check dev branch of WanVideoWrapper repo for fix with torch compile and DF sampler
  - *From: Ablejones*

- **Problem:** IndexError with shift parameter
  - **Solution:** Don't use shift value of 50 in DF sampler node as it messes up the sigmas list
  - *From: Ablejones*

- **Problem:** Wrong text encoder format
  - **Solution:** Use text encoder from comfy org or kijai's huggingface, not other sources as they're in wrong format
  - *From: Piblarg*

- **Problem:** unianim_data referenced before assignment
  - **Solution:** Update the node
  - *From: Kijai*

- **Problem:** phantom_end_percent referenced before assignment error
  - **Solution:** Error occurs when using Fun models - Kijai fixed this issue
  - *From: DawnII*

- **Problem:** TypeError: convert_fp8_linear() got an unexpected keyword argument 'sd'
  - **Solution:** Switch back to main branch as this was an unfinished feature related to fp8_fast
  - *From: Kijai*

- **Problem:** Diffusion forcing sampler crashes with feta node not connected
  - **Solution:** Add disable_enhance() line to diffusion forcing sampler, as it was missing unlike the normal wanvideo wrapper
  - *From: seitanism*

- **Problem:** Model not fully offloading when cancelling mid-sampling causes OOM
  - **Solution:** Set model loader to offload_device instead of main_device, and use 'force model offload' option on text encoder
  - *From: Kijai*

- **Problem:** Fun Control 14b not following depth map, immediately starts gesturing
  - **Solution:** Use Fun 1.1 instead of 1.0, add noise_aug_strength of 0.03, and try different control embed settings
  - *From: boorayjenkins*

- **Problem:** Feta enhance broken on Fun 1.1
  - **Solution:** Issue occurs when using reference image as it adds +1 to length but feta is not set for this
  - *From: Kijai*

- **Problem:** UnicodeDecodeError after PC crash during WAN2.1 generation
  - **Solution:** Reinstalling torch fixed the issue
  - *From: Ashtar*

- **Problem:** AssertionError: Input tensors must be in dtype of torch.float16 or torch.bfloat16
  - **Solution:** Switch from sageattn to sdpa in attention settings
  - *From: shreyams.*

- **Problem:** Expected query, key, and value to have the same dtype error
  - **Solution:** Select fp8_e4 quantization to fix dtype mismatch
  - *From: David Snow*

- **Problem:** Dtype errors in WAN sampler
  - **Solution:** Change rope function from 'default' to 'comfy' in sampler settings
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Video preview disappearing when switching tabs
  - **Solution:** Issue affects both native and wrapper implementations, no solution provided
  - *From: lostintranslation*

- **Problem:** Video degradation with DF extension, especially with 1.3B version
  - **Solution:** Add colormatch node to each clip segment referring to initial frame, add refining stage with different model at denoise 0.6-0.7, or use unsampling/resampling
  - *From: Ablejones*

- **Problem:** FantasyTalking doesn't work with DF because DF isn't I2V model
  - **Solution:** DF doesn't use image cross attention at all, so audio conditioning won't work
  - *From: Kijai*

- **Problem:** Context window with FantasyTalking loses the image
  - **Solution:** Not fully resolved, but noted as limitation
  - *From: Kijai*

- **Problem:** T2V with FantasyTalking audio cfg gives poor results
  - **Solution:** Model is designed for I2V, T2V compatibility is limited
  - *From: Kijai*

- **Problem:** Fantasy Talking audio sync completely off
  - **Solution:** Update wrapper - audio CFG calculation was broken due to missing brackets
  - *From: Kijai*

- **Problem:** ComfyUI connection issues with new frontend
  - **Solution:** Hit Esc key to dismiss connection overlay
  - *From: MilesCorban*

- **Problem:** First frame corruption with incompatible settings
  - **Solution:** Use compatible model/latent size combinations
  - *From: Kijai*

- **Problem:** VACE start/end frame node error
  - **Solution:** Check rope setting is 'comfy' not 'default' on sampler node
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Fantasy Talking lip sync slightly off
  - **Solution:** Set audio CFG to 1.0, or shift audio 5 frames later if silence at start
  - *From: ingi // SYSTMS*

- **Problem:** TeaCache causing early skip issues
  - **Solution:** Set TeaCache start step to 6 or higher to avoid skipping too early
  - *From: Kijai*

- **Problem:** Tile LoRA producing noise output
  - **Solution:** Cannot use tile control LoRA with VACE - they're incompatible
  - *From: Kijai*

- **Problem:** 14B model OOM on 3090
  - **Solution:** Use block swapping and quantization for large resolutions with 14B models
  - *From: ingi // SYSTMS*

- **Problem:** VRAM issues with large models
  - **Solution:** Increase blocks to swap to 20, reduce clip vision precision to FP16 or BF16, use smaller resolution
  - *From: ingi // SYSTMS*

- **Problem:** torch._scaled_mm error on older GPUs
  - **Solution:** Change from bf16 to fp16 and base_precision to fp8_e4m3fn instead of fp8_fast
  - *From: J_Pyxal*

- **Problem:** Negative dimension tensor error
  - **Solution:** Check input frame dimensions and frame count - something off with input frames
  - *From: Kijai*

- **Problem:** Invalid WanVideo model selected for VACE
  - **Solution:** VACE module needs to be loaded alongside normal Wan 1.3B model, not as main model
  - *From: Kijai*

- **Problem:** SAM2 error on video input
  - **Solution:** Error occurs when mask indices aren't consistent across frames - if object not detected for 1 frame
  - *From: ArtOfficial*

- **Problem:** Wan video generations become progressively corrupted
  - **Solution:** Issue with Wan 2.1 reward LoRA - manually unload models and free cache
  - *From: gshawn*

- **Problem:** Black frames with context uniform looped
  - **Solution:** Use correct settings: 169 frames with context size 81 and 16 overlap
  - *From: Kijai*

- **Problem:** Reference image causes blink/flash at start of video
  - **Solution:** Use fun ref image latent with empty embed instead of feeding in the ref image directly
  - *From: Gavmakes*

- **Problem:** First frame corruption when using high step values
  - **Solution:** In wrapper TC node, values are exact steps not percentages - use actual step count (e.g., 20 for 20 steps)
  - *From: JohnDopamine*

- **Problem:** SystemError: PY_SSIZE_T_CLEAN macro error with RTX 5090 fresh install
  - **Solution:** Issue appears related to recent ComfyUI update with triton and sage installation
  - *From: Baku*


## Model Comparisons

- **1.3B vs 14B for vid2vid**
  - 1.3B model is better for vid2vid without a doubt - much faster and with depth, highres, aesthetics loras reaches new quality level
  - *From: David Snow*

- **Wrapper vs Native workflow**
  - Wrapper produces far more stable video outputs than native, native is a massive pain to use
  - *From: David Snow*

- **DepthCrafter vs Video Depth Anything**
  - DepthCrafter appears better for static shots, left (DepthCrafter) looks better by a decent bit
  - *From: Juampab12*

- **VACE vs InP model**
  - VACE already better than InP model - InP doesn't know what red panda is
  - *From: Kijai*

- **TeaCache performance between versions**
  - Old revision with both old RoPE & comfy RoPE worked better - newer version skips less steps for same thresholds
  - *From: DevouredBeef*

- **VACE vs Fun model**
  - VACE feels slower but better quality than Fun model
  - *From: Cseti*

- **VACE vs standard Wan speed**
  - VACE is approximately 2x slower - 3 minute generations become 7 minutes
  - *From: multiple users*

- **VACE vs FunInP model**
  - VACE makes FunInP model redundant due to superior capabilities
  - *From: Kijai*

- **LoRAs with VACE vs standard Wan**
  - LoRAs are kinda weird and not quite as good as standard Wan but some aspects work
  - *From: Kytra*

- **FP16 vs FP32 on VACE**
  - FP16 is 3 times faster but FP32 has much better quality
  - *From: VK (5080 128gb)*

- **With reference vs without reference on VACE**
  - Without reference image quality is 100 times better, almost photorealistic vs oversaturated colors and plastic skin with reference
  - *From: seitanism*

- **VACE vs Fun models**
  - VACE might make Fun models redundant
  - *From: Kijai*

- **10 steps vs 30 steps VACE**
  - 30 steps is a bit better quality but takes 3x longer (1 min vs 3 min for 41 frames)
  - *From: VK (5080 128gb)*

- **VACE vs Fun-Control**
  - VACE is almost objectively better - works with original Wan LoRAs and has more control options
  - *From: Kytra*

- **Euler vs DPM++_SDE after timestep fix**
  - Euler now produces same quality as UniPC after fix, while SDE variant has convergence issues
  - *From: Kijai*

- **VACE vs regular I2V**
  - VACE offers more control options but setup is more complex
  - *From: HeadOfOliver*

- **SkyReels A2 vs VACE**
  - SkyReels looks better but likely based on HYV so unfair comparison since VACE is 1.3B
  - *From: Juampab12*

- **Hunyuan vs SkyReels**
  - SkyReels was bigger and slower than hunyuan but a good bit better
  - *From: Benjimon*

- **Base Wan 1.3B vs DG_Wan models for V2V**
  - Base model better at following depth LoRA and closer to original video motion, DG_Wan models don't respond to LoRAs as well
  - *From: David Snow*

- **Sapiens vs DWPose for pose detection**
  - Sapiens provides better temporal consistency and more detailed human preprocessing
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Depth vs Pose control in VACE**
  - Pose gives better facial performance, depth provides different motion characteristics - can blend both for optimal results
  - *From: A.I.Warper*

- **WAN 1.3B vs other 1.4B models**
  - Faster than 14B, slower than other 1.4B models due to more blocks
  - *From: Zuko*

- **WAN 1.3B vs other similar sized image models**
  - Considerably better than other similar sized image models
  - *From: YatharthSharma*

- **WAN cost vs Kling**
  - Would cost over $100 on Kling for the same effect achievable with WAN
  - *From: slmonker(5090D 32GB)*

- **FP16 vs FP32 for WAN 1.3B**
  - FP32 is better quality but takes almost 2x time, marginal improvement not worth extra time
  - *From: David Snow*

- **UniPC vs Euler schedulers**
  - UniPC used to be best option until Kijai fixed Euler, now slightly worse than Euler
  - *From: David Snow*

- **DG model versions comparison**
  - Multiple DG variants available (High, Light, V3, V4) with different characteristics - High changes 2D/animation to realism
  - *From: Hashu*

- **4 steps vs 8 steps DG model**
  - 4 steps: 7 seconds generation time, 8 steps: longer but better quality
  - *From: Kijai*

- **VACE applied to different block counts**
  - Applying VACE to only 5 blocks or half the blocks works well, keeps part of bounding box in result
  - *From: Kijai*

- **DG models vs base Wan**
  - DG more creative but follows reference image much less, much faster (38sec vs 10min)
  - *From: IllumiReptilien*

- **VACE vs Fun Control models**
  - VACE is all fun and more since you can combine them plus use reference
  - *From: ˗ˏˋ⚡ˎˊ-*

- **5 steps base Wan vs 5 steps DG Wan**
  - DG significantly better at low step counts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DG at 60 steps vs base**
  - DG at 60 steps is actually pretty good, 2s/it for 960x608x61
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B vs 14B model quality**
  - 14B produces significantly better results than 1.3B preview model
  - *From: Kijai*

- **I2V vs T2V task difficulty**
  - Having actual starting frames (I2V) is not comparable to T2V generation - completely different tasks
  - *From: Kijai*

- **SkyreelsA2 vs VACE**
  - SkyreelsA2 uses 14B I2V model and clip embeds, better for I2V. VACE uses different approach trained on T2V model without clip embeds. SkyreelsA2 better for VRAM as no extra control inputs
  - *From: Kijai*

- **14B VACE vs current models**
  - 14B VACE will be tough to run, probably unusable even on 4090 due to double compute requirement
  - *From: Draken*

- **Fun models vs VACE/SkyreelsA2**
  - Fun models are mostly outclassed by VACE and SkyreelsA2, much worse than base 1.3B model
  - *From: DawnII*

- **VACE vs Fun Control for frame continuation**
  - Fun Control 14B works better for last latent/first latent technique
  - *From: JmySff*

- **Base Wan vs distilled models**
  - User feels like they prefer base Wan more, distilled models hard to tell apart
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Realistic lineart vs anyline**
  - Realistic lineart works better than anyline
  - *From: Kijai*

- **Inverted anyline vs depth**
  - Inverted anyline wins over depth for control
  - *From: Kijai*

- **VACE memory usage vs 14B Fun models**
  - VACE competes with nearly as much VRAM usage as 14B fun models
  - *From: DawnII*

- **14B vs 1.3B vid2vid quality**
  - 14B substantially better for vid2vid, though much slower
  - *From: David Snow*

- **Wan vs AnimatedDiff**
  - Wan is replacement for AnimatedDiff with better control and no background distortion on camera movement
  - *From: Kijai*

- **VACE vs Fun Control**
  - Fully different models, both serve similar control purposes
  - *From: Kijai*

- **Fun Control 14B vs VACE quality**
  - Fun Control 14B produces much better quality than VACE 1.3B, but loses reference subject/object feature
  - *From: JmySff*

- **1.3B skin detail capability**
  - 1.3B is terrible at skin detail
  - *From: David Snow*

- **Fun 1.3B vs VACE 1.3B**
  - Fun 1.3B feels terrible, so much worse in general compared to VACE
  - *From: Kijai*

- **Fun 14B vs VACE for pose control**
  - Fun 14B seems well trained for pose control, better than VACE
  - *From: Kijai*

- **VACE vs Fun Control versatility**
  - VACE is most versatile and supports old LoRAs and different models
  - *From: Kijai*

- **Original vs DiffSynth reward LoRAs**
  - DiffSynth converted version works much better, has bigger impact
  - *From: Pedro (@LatentSpacer)*

- **VACE vs Runway first frame style**
  - VACE with first frame and control works as good if not better than Runway first frame style for the task, though maybe not quality
  - *From: Draken*

- **CFG1 distilled lora vs non-distilled**
  - Distilled version actually slower despite lower CFG, not faster as expected
  - *From: CJ*

- **4o vs Gemini for image editing**
  - 4o better quality but changes faces when asked to change hair color. Gemini excellent at holding original image while changing it but lacks quality
  - *From: Fill*

- **5080 16GB vs older gen 24GB for Wan**
  - Pretty clear choice if you want to run 14B, you'll lose any speed benefit to offloading with 16GB
  - *From: Kijai*

- **GGUF vs swapping performance**
  - GGUF is just so slow compared to swapping
  - *From: Kijai*

- **Multiple VACE encodes vs single encode**
  - Splitting encodes made results much worse
  - *From: David Snow*

- **Base 1.3B vs Fun-Control**
  - Base 1.3B with control lora is much better than Fun-Control, which has glitches and artifacts. Fun-Control better for small details but worse overall
  - *From: David Snow*

- **DiffSynth LoRAs vs original**
  - DiffSynth converted LoRAs have double strength due to removed alpha keys - using at 0.5 equals original at 1.0
  - *From: Kijai*

- **Fun-Control vs Base with depth lora**
  - Fun-Control adds noise and artifacts, base with depth lora more stable
  - *From: David Snow*

- **VACE 1.3B vs regular 14B I2V**
  - VACE 1.3B gets results as good as classic I2V with 14B model
  - *From: Vérole*

- **Pika swap vs WAN VACE object replacement**
  - Pika kept the shape of original object (beer bottle) when swapping for banana, wasn't great
  - *From: Jas*

- **SAM2 vs referring expression segmentation**
  - Referring expression segmentation seems better but takes 15 minutes on 81 frames vs SAM2 being faster
  - *From: StableVibrations*

- **WAN vs Hunyuan Video overall**
  - WAN better for image quality, physics, prompt adherence, control options, and flexibility. Hunyuan better for speed and NSFW content
  - *From: Screeb*

- **WAN vs Hunyuan I2V**
  - WAN I2V much better - cleaner output without noise, camera stays still unless prompted vs Hunyuan's random camera movement
  - *From: Blink*

- **Hunyuan vs WAN for likeness LoRAs**
  - Hunyuan T2V better for training human likeness LoRAs, but WAN better for I2V
  - *From: JohnDopamine*

- **Fun Control vs VACE for combined controls**
  - Combined controls work relatively well with Fun Control but not with VACE - separate controlnets render much better with VACE
  - *From: JmySff*

- **DG_Boost models vs base 1.3B**
  - DG_Boost models better for character quality and certain details, especially interiors, but base closer to original rendering style
  - *From: David Snow*

- **Fun Control vs VACE Control with Reference**
  - VACE better for ease of use. Fun-Control is inconsistent - sometimes far better than base, sometimes far worse
  - *From: David Snow*

- **1.3B model vs optimal steps**
  - Even with Flux get better results using euler/beta than optimal steps
  - *From: Kijai*

- **480p model vs 720p model for motion**
  - 480p model seemed to produce better motion anyway, 480p gives better result than 720p model
  - *From: David Snow*

- **Q8 vs FP8 models**
  - Q8 model gives better quality than fp8. GGUF is slower than FP8 with optimizations but not by much
  - *From: Johnjohn7855*

- **VACE stability vs regular generation**
  - VACE is very, very stable
  - *From: David Snow*

- **Fun vs VACE speed**
  - Fun models are significantly faster than VACE for similar tasks
  - *From: Pol*

- **Fun 1.3B vs VACE for V2V**
  - Fun 1.3B respects reference images better than VACE for video-to-video
  - *From: Pol*

- **Lotus Depth vs Depth Anything**
  - Lotus depth gives more details in image generation, but causes flickering in video - not good for video use
  - *From: David Snow*

- **8 steps vs 60 steps with Fun model**
  - 8 steps produces remarkably good results, making it very efficient
  - *From: A.I.Warper*

- **Fun vs VACE VRAM usage**
  - Fun uses significantly less VRAM than VACE due to VACE's 15 additional blocks
  - *From: Kijai*

- **WSL vs dual boot for development**
  - Dual boot better for performance, WSL has more complex file system and memory management
  - *From: Kijai*

- **14B vs 1.3B model training**
  - 14B is much easier to train overall, 1.3B more challenging
  - *From: Piblarg*

- **Topaz vs other interpolators**
  - Topaz significantly better than 5 other tested interpolators
  - *From: Benjimon*

- **RTX 4090 vs 3090 vs RTX 8000 speed**
  - 1hr on 4090, 2hrs on 3090, 2.5-3hrs on RTX 8000 for same generation
  - *From: Benjimon*

- **BF16 vs FP16 conversion**
  - BF16 to FP16 conversion is lossy and produces worse quality than either format
  - *From: Kijai*

- **Kling 2 vs older Kling**
  - New Kling 2 looks very good and dynamic but heavily censored, rejected 19 of 26 prompts that worked in older model
  - *From: Fabricatedgirls*

- **FLF2V vs Fun 14B**
  - FLF2V probably better if comparing only first/last frame, but unsure if FLF2V can do more than 2 input frames like Fun can
  - *From: Kijai*

- **Q8 GGUF vs fp8**
  - GGUF about 20% slower than fp8 when fp8 fits in VRAM, Q8 uses more memory than fp8
  - *From: Kijai*

- **bf16 vs fp16 vs fp16 w/ sage on Fun Control 14B**
  - All produce cursed/body horror results in test case
  - *From: Benjimon*

- **480p vs 720p model performance**
  - 720p model may not be as good as 480p model, possibly trained on much less data
  - *From: MilesCorban*

- **Wan vs enhanced HYV in FramePack**
  - Enhanced HYV shows similar performance to Wan with better human anatomy and slightly faster speed
  - *From: Johnjohn7855*

- **Wan vs HYV prompt following**
  - Wan prompt following is 5x better literally, HYV never followed prompts great
  - *From: yi*

- **Using Wan vs going back to HYV**
  - Like going back to play Atari when you have Steam - can throw 3 paragraphs at Wan and it figures everything out
  - *From: crinklypaper*

- **HYV vs Wan for celebrity/human likeness training**
  - HYV is amazing for deepfake generations and celebrity likenesses, Wan trials didn't work out as well
  - *From: JohnDopamine*

- **VACE vs Fun Control**
  - VACE better for full character replacement, Fun significantly faster for style transfer iteration. Fun uses 1/3 memory and time of VACE
  - *From: A.I.Warper*

- **FLF2V vs regular Wan 14B I2V**
  - FLF2V has better source image adherence with loras than regular 14B 720 i2v model
  - *From: Eclipse*

- **FramePack vs 14B WAN quality**
  - FramePack is efficiency upgrade but at small cost to quality. Shows weird smoothing on textures
  - *From: Kytra*

- **Fun vs VACE for stylized first frame + control**
  - Fun is better for stylized 1st frame and control video ref scenario. VACE better for t2v prompting with control video ref
  - *From: N0NSens*

- **UniAnimate vs VACE**
  - UniAnimate will beat VACE because it's for the proper I2V model that's already really good, uses LoRA weights and pose embeds, only 1GB in fp16
  - *From: Kijai*

- **Fun-control vs VACE for eye movement**
  - Fun-control can capture eye movements better but doesn't look as good overall
  - *From: David Snow*

- **Inner's 1.3B model vs 14B model**
  - Inner's 1.3B model is better than 14B, uses synthetic data in addition to original dataset
  - *From: Flipping Sigmas*

- **DepthAnythingV2 vs original DepthAnything**
  - V2 is much faster and less resource intensive while maintaining quality
  - *From: David Snow*

- **SageAttention vs SDPA attention**
  - SDPA gives higher quality output, SageAttention hits hands badly but provides speed
  - *From: Benjimon*

- **1.3B model skin rendering**
  - Human skin is a weakness for 1.3B model compared to larger variants
  - *From: David Snow*

- **Benjimon's SkyReels vs stock i2v**
  - Very close to the stock i2v model based on full weight analysis
  - *From: Benjimon*

- **VACE vs traditional control methods**
  - VACE output is superior - essentially expands base model capability and looks better
  - *From: David Snow*

- **UniAnimate vs other pose methods**
  - UniAnimate produces better quality than VACE preview model at 25 steps
  - *From: Vérole*

- **SD 1.5 vs SDXL**
  - SD 1.5 has stronger controlnets and IP adapters, better T5/IC light support, but harder to use (300+ nodes vs simple workflow)
  - *From: deleted_user_2ca1923442ba*

- **Wan vs AnimateDiff for style transfer**
  - Wan much faster - 345 seconds on 4090 vs hours with AnimateDiff pipeline
  - *From: Gavmakes*

- **Different step counts for generation**
  - 20 steps vs 30 steps shows significant difference, 35 steps is sweet spot
  - *From: ezMan*

- **SkyReels 1.3B vs 14B speed**
  - 1.3B is four times faster than 14B
  - *From: ezMan*

- **Fun inp vs VACE for extension**
  - VACE 1.3b gives better results than Fun inp
  - *From: PirateWolf*

- **SkyReels 540p-i2v-14B vs regular Wan i2v 14B**
  - SkyReels 14B is closer to Wan i2v 14B than other variants based on weight analysis
  - *From: Benjimon*

- **4090 vs 4070Ti performance**
  - 4090 is 2x faster - 1008GB/s vs 505GB/s bandwidth plus >2x CUDA cores
  - *From: MilesCorban*

- **LTX 0.9.6 distilled vs Wan speed**
  - LTX much faster (almost SDXL speed) but Wan quality is much better - 'comparison is not even close'
  - *From: Colin*

- **Wan I2V vs Hunyuan motion**
  - Wan I2V is 'just on another level with the amount of motion it can do' even compared to Hunyuan
  - *From: Kijai*

- **VACE vs 14B models**
  - VACE is 'much better' and quicker than 14B models
  - *From: Colin*

- **1.3B vs 14B model differences**
  - Work about the same but 14B lacks fps embeds, 1.3B starts to lose quality in long generations
  - *From: Kijai*

- **MAGI-1 vs other models**
  - Claims to beat everything, but only wins by tiny bit in user preference benchmark
  - *From: Draken*

- **VACE vs DG models**
  - VACE is slower, DG very fast at 6 steps but not good for i2v
  - *From: N0NSens*

- **SageAttention vs SDPA**
  - SageAttention gets 99% quality while being twice as fast
  - *From: Kijai*

- **Two-pass upscaling vs regular upscaling**
  - Vastly prefer two-pass over regular upscaling
  - *From: Davidodave*

- **Wan vs SkyReels sampling behavior**
  - Wan determines result in first few steps, SkyReels starts with big motion and refines details throughout
  - *From: Zuko*

- **LatentSync vs LivePortrait**
  - Different uses - LivePortrait copies facial expressions, LatentSync generates lip motion from audio
  - *From: Zuko*

- **14B vs 1.3B Wan models**
  - 14B can handle 720p where 1.3B breaks down, but 14B is much slower (8 mins vs 30 secs per segment)
  - *From: Draken*

- **Base 1.3B vs VACE for second passing**
  - Base 1.3B better for second passing due to VACE being too sensitive to control input artifacts
  - *From: David Snow*

- **LTX vs other models for iteration speed**
  - LTX incredible for iteration speed - 20 seconds for 97 frames at 1280x720
  - *From: David Snow*

- **Cog 5B vs Wan 1.3B**
  - Wan 1.3B definitely better than Cog 5B despite smaller size
  - *From: Kijai*

- **Phantom vs VACE quality for facial fidelity**
  - 1.4b models (Phantom, 1.4b VACE) are too weak to capture true facial fidelity from reference pics. Gets elements down but doesn't achieve celebrity-level accuracy like Taylor Swift/RDJ.
  - *From: Zuko*

- **CFG scheduling vs TeaCache for speed optimization**
  - Quality hit from using CFG 1.0 is higher than just using more aggressive TeaCache
  - *From: Kijai*

- **SkyReels V2 vs other models prompting approach**
  - Other models haven't done dynamics-only prompting that SkyReels V2 paper recommends. Everything else is image conditioned, similar to how Google's Whisk animate works.
  - *From: fredbliss*

- **SkyReelV2-i2v-540p vs base Wan i2v**
  - SkyReelV2 is way better with improved movements, overall quality and subject fidelity
  - *From: mamad8*

- **Phantom vs SkyReels-A2**
  - Phantom seems better and has 1.3B version available
  - *From: Kijai*

- **DF vs framepack**
  - DF model is really miles ahead in quality and motion, allows prompt scheduling/travel
  - *From: seitanism*

- **Native vs wrapper VRAM usage**
  - Native has automatic offloading when VRAM gets full, wrapper needs manual block swap configuration
  - *From: Kijai*

- **Phantom vs VACE for character identity**
  - Phantom seems better at keeping character consistent
  - *From: NebSH*

- **Torch compile vs no compile on 4090**
  - Compile is faster: 2.94s/it vs 4s/it
  - *From: MilesCorban*

- **fp8e4m3_fast vs fp8e4m3 for chaining**
  - fp8e4m3 better for chaining as fp8e4m3_fast causes artifacts
  - *From: MilesCorban*

- **SkyReels V2 vs Wan 14b**
  - SkyReels quality is really great, even slightly better than wan 14b
  - *From: seitanism*

- **SkyReels DF vs framepack**
  - Much better than framepack
  - *From: boorayjenkins*

- **Wan vs Veo 2 color quality**
  - SkyReels looks more cinematic with mood, Veo looks documentary-like but has better natural colors
  - *From: seitanism*

- **Skyreels vs HYV (HunyuanVideo)**
  - HYV better for identity retention, facial behavior, fine hair, and cinematic look. Skyreels better for functionality and has ControlNet support. HYV is faster and native 24fps with correct motion blur
  - *From: Mads Hagbarth Damsbo*

- **Base WAN vs Skyreels V2**
  - Base model performed better in user tests - Skyreels V2 results described as 'not good' across several images tested
  - *From: N0NSens*

- **Skyreels V2 I2V vs base 480p speed**
  - V2 I2V 14B 540p faster than base 480p (2:50 vs 3:20) but result quality was bad
  - *From: N0NSens*

- **Base model vs Skyreels for anime/drawings**
  - Base model works way better for anime stuff and drawings
  - *From: Miku*

- **20 steps vs 30 steps**
  - 20 steps sometimes looks better for simple scenes, but 30+ steps needed for complex scenes with lots of details
  - *From: ezMan*

- **fp8_fast vs fp16_fast on 3090**
  - fp16_fast works on 3090, fp8_fast does not work on 3090
  - *From: Kijai*

- **Hunyuan vs Wan fp8 quality**
  - Hunyuan quality doesn't degrade from fp8_fast, but Wan has something special that breaks with fp8
  - *From: Kijai*

- **Fun 1.1 vs VACE**
  - Pretty similar to VACE but much faster
  - *From: Kijai*

- **Control 1.3B vs 14B**
  - 1.3B gives better results than 14B and is much faster
  - *From: Nokai*

- **Skyreels vs original base Wan**
  - Skyreels i2v and t2v are better than original base wan in quality and prompt following
  - *From: mamad8*

- **14B 480p vs VACE i2v**
  - 14B has better motion but takes 1753 seconds vs VACE's 443 seconds. VACE is sharper but has motion artifacts. Multiple VACE passes in same time as one 14B run could eliminate artifacts
  - *From: David Snow*

- **WAN base vs Skyreels V2**
  - V2 is better for videos with people, base WAN better for abstract ideas and anime/cartoon content
  - *From: MilesCorban*

- **Lower resolution (544x544) vs higher resolution (720x720+) with DF**
  - Lower resolution has less noticeable degradation when using DF to extend clips
  - *From: seitanism*

- **Diffusion Forcing vs Framepack**
  - Framepack is faster and does everything at once, DF is slower and more VRAM intensive but allows prompt scheduling like AnimateDiff
  - *From: MilesCorban*

- **HiDream vs Flux**
  - HiDream better - no grid pattern, no 2nd pass needed
  - *From: Colin*

- **Fun_inp vs VACE for start/end images**
  - Fun_inp way better according to testing
  - *From: David Snow*

- **VACE vs DG Fun for base Wan compatibility**
  - Base Wan DG doesn't work well with VACE, contradictory reports
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Skyreels V2 I2V vs base Wan2.1**
  - V2 I2V is much improved and current favorite
  - *From: Colin*

- **FantasyTalking vs Sonic**
  - FantasyTalking much better than Sonic, higher quality and listens to prompts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fantasy Talking vs LatentSync + Wan**
  - Comparable quality but Fantasy Talking offers more flexibility and works during transformations
  - *From: Stad*

- **DG models vs standard Fun_Inp**
  - DG models are stronger for inpainting tasks
  - *From: David Snow*

- **Skyreels vs Phantom for T2V**
  - Discussion initiated but no clear verdict provided
  - *From: N0NSens*

- **14B vs 1.3B SkyReels**
  - 14B is leagues better quality but much slower
  - *From: Colin*

- **Fantasy Talking vs Sonic vs Latent Sync**
  - Sonic more direct but less flexible, Latent Sync more convoluted but more possibilities, Fantasy Talking most flexible
  - *From: Stad*

- **Fun Camera Control vs ReCamMaster**
  - Fun is for T2V/I2V, ReCamMaster is for vid2vid
  - *From: Kijai*

- **14B vs 1.3B for control tasks**
  - 14B is much better but sometimes overkill, 1.3B can be underwhelming - a 3B model would be ideal
  - *From: Draken*

- **Text generation T2V vs I2V**
  - T2V works better for text generation than I2V due to low resolution vision encoder (326x326)
  - *From: pom*


## Tips & Best Practices

- **Use input file quality matters significantly**
  - Context: For vid2vid and style transfer, always use high quality source files and depthcrafter for depth inputs
  - *From: David Snow*

- **Try second-passing old generations with 1.3B**
  - Context: Can significantly improve thousands of 'almost good enough' videos using depth, highres and aesthetics loras
  - *From: David Snow*

- **Use context windows for longer v2v sequences**
  - Context: Especially with control, works great for longer video-to-video sequences
  - *From: Kijai*

- **Mix depth and realistic lineart as control embeds**
  - Context: For v2v to stay close to original while improving quality
  - *From: David Snow*

- **Avoid transferring videos through messaging apps**
  - Context: WhatsApp and similar apps compress and destroy video quality, affecting AI output
  - *From: 3Dmindscaper2000*

- **Regularly backup ComfyUI before updates**
  - Context: Zip portable ComfyUI before pressing update to avoid breaking workflows
  - *From: Lumi*

- **Use Docker with pinned commits for ComfyUI**
  - Context: Pin every custom node to specific commit for consistent installs across machines
  - *From: pixelperfecter*

- **Use max 77 frames with reference images**
  - Context: Because it ends up as 81 latents total
  - *From: Kijai*

- **Remove background from reference images**
  - Context: Place subject on white background for better likeness
  - *From: Kijai*

- **Use SLG and zero CFG for better results**
  - Context: When working with reference images
  - *From: Kijai*

- **Use fp16 or bf16 with fp8_e4m3fn quantization**
  - Context: For running VACE efficiently
  - *From: zelgo_*

- **Don't use block swapping with VACE**
  - Context: Won't help much and can cause errors
  - *From: Kijai*

- **Remove background completely from reference images**
  - Context: When using VACE style transfer
  - *From: ingi // SYSTMS*

- **Use compositor node to composite reference images**
  - Context: For better results when combining multiple references
  - *From: slmonker(5090D 32GB)*

- **Position reference face where face will be in video**
  - Context: When trying to transfer both face and clothing
  - *From: ingi // SYSTMS*

- **Use second pass for cleanup**
  - Context: Model is better at denoising its own outputs than straight vid2vid
  - *From: Piblarg*

- **Keep prompts simple**
  - Context: Complex prompts like adding rain can make output blurry
  - *From: PookieNumnums*

- **Disable block 1 and 2 on quality degradation LoRAs**
  - Context: Often improves quality by quite a margin without losing what lora was trying to achieve
  - *From: Juampab12*

- **Use 720p directly instead of upscaling from 480p**
  - Context: For quality generation
  - *From: Mint*

- **Second denoise pass cleans up results when using control**
  - Context: When control reduces coherence
  - *From: Piblarg*

- **Wan is super sensitive to style prompts**
  - Context: Include style specifications in prompts
  - *From: Mint*

- **Composite mask directly on input video works best**
  - Context: For VACE workflows
  - *From: Kijai*

- **Don't even use mask input for VACE**
  - Context: Mask input purpose unclear, works better without
  - *From: Kijai*

- **Zoom in on reference face for clearer likeness**
  - Context: When using reference images
  - *From: AJO*

- **Use mask as the key for better VACE results**
  - Context: When doing reference-based generation
  - *From: Kijai*

- **Try first with each control on their own to see they work**
  - Context: Before combining reference and control
  - *From: Kijai*

- **It's best to run new models with their repos first before introducing 20 layers of shlop**
  - Context: When testing new models
  - *From: Benjimon*

- **Best to manually pad reference images to match aspect ratio**
  - Context: When using reference images with VACE
  - *From: Kijai*

- **Set first frame 0, second frame 1 and last frame 1 for fade mask**
  - Context: When using create fade mask advanced node
  - *From: Kijai*

- **Use low CFG for DiffSynth models**
  - Context: CFG 1-3 prevents overbaked/overcooked output, light_v1 works best with character LoRAs
  - *From: BondoMan*

- **Structure prompts like training captions**
  - Context: Begin with video style, followed by content abstract, then detailed description for better prompt alignment
  - *From: fearnworks*

- **Use high shift values for DiffSynth models**
  - Context: Need shift 11+ for proper prompt following like hand waving motions
  - *From: BondoMan*

- **Combine reference frame with preprocessors**
  - Context: Put reference image as frame 0, preprocessor frames as rest for controlled starting point
  - *From: Hashu*

- **Fade control images to make them darker for lower control strength while maintaining reference strength**
  - Context: When you want general control rather than specific control
  - *From: Kijai*

- **Use Sapiens instead of OpenPose for face detection**
  - Context: OpenPose is barely usable for faces
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Align first frame exactly with first frame of control reference**
  - Context: For proper motion tracking when using control inputs
  - *From: Zuko*

- **Use start frame instead of reference when you don't want white background**
  - Context: When animating with depth control and specific backgrounds
  - *From: Kijai*

- **Set TinkerWAN Alpha lora to positive values with v1.0 version**
  - Context: New version works with positive instead of negative values
  - *From: David Snow*

- **Try drawing hands manually for better hand control**
  - Context: When pose control isn't giving good hand results
  - *From: Kijai*

- **Use hue shift on Sapiens bones for better results**
  - Context: To improve bone-based control quality
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use Image Composite Masked for video inpainting**
  - Context: When inpainting specific zones in video, use grey on input video and reference image
  - *From: mamad8*

- **Masks help maintain surrounding consistency**
  - Context: Without masks, areas around inpaint regions will change too
  - *From: Hashu*

- **Tab to Krita for complex compositing**
  - Context: For complex image composition tasks, external tools like Krita or Photopea are more efficient than ComfyUI nodes
  - *From: Kijai*

- **Use CFG 2.0 with DG models**
  - Context: DG models are essentially CFG distilled, CFG 1.0 kills quality
  - *From: Kijai*

- **Combine multiple depth estimation methods**
  - Context: Using depth, lotus normals, and realistic lineart together provides more detail for better video quality
  - *From: David Snow*

- **For better likeness: bigger reference on screen, use closeup of character face on white bg, higher res reference, describe character in prompt, can set reference strength higher than 1**
  - Context: When using VACE for character consistency
  - *From: Hashu*

- **Reference resolution and preprocessing doesn't have to match output video resolution**
  - Context: VACE reference images
  - *From: Hashu*

- **Cartoon/anime characters are much harder to get good likeness than realistic characters**
  - Context: VACE character consistency
  - *From: Hashu*

- **Do preprocessing beforehand so everything gets offloaded to avoid memory issues**
  - Context: Managing VRAM with VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use TeaCache with VACE for better performance**
  - Context: Optimizing VACE workflows
  - *From: JmySff*

- **Lower VACE embed strength for better results**
  - Context: User settled on slightly lower than 0.925 embed strength
  - *From: Kytra*

- **Convert input to 16fps for better lipsync**
  - Context: Though this didn't fully solve lipsync issues in testing
  - *From: burgstall*

- **Use Image Composite Masked node for transparency overlays**
  - Context: Create mask from grayscale image for proper compositing
  - *From: traxxas25*

- **Avoid --fast startup argument with certain precision settings**
  - Context: Can cause issues with float16 accumulate weights
  - *From: AJO*

- **Use box mask instead of tight character cutouts**
  - Context: Prevents shape forcing in VACE output
  - *From: Kijai*

- **Use solid background for better SkyreelsA2 reference results**
  - Context: When using SkyreelsA2 reference mode
  - *From: DawnII*

- **Create character LoRA for better likeness consistency**
  - Context: When having trouble with character consistency in VACE, use 10 images to train small LoRA
  - *From: notid*

- **Pad first frame image for SkyreelsA2**
  - Context: To match their training approach and get proper results
  - *From: Kijai*

- **Use individual clip embeds even when compositing images**
  - Context: For SkyreelsA2 workflows with multiple subjects
  - *From: Kijai*

- **Plan layout and size of person/subject/background when uploading reference images**
  - Context: For better VACE results
  - *From: slmonker(5090D 32GB)*

- **Describe reference properly to help with prompt-to-reference mapping**
  - Context: VACE uses prompt to reference matching
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use control with VACE reference or the reference overtakes the generation**
  - Context: When using VACE with reference images
  - *From: Kijai*

- **Include clothing details in prompts or reference to maintain consistency between context windows**
  - Context: When using VACE context windows
  - *From: Kijai*

- **Prompt for correct environment/lighting when generating characters**
  - Context: For character replacement workflows
  - *From: traxxas25*

- **Try mediapipe face instead of pose estimator for lip movements in closeups**
  - Context: When doing facial control with VACE
  - *From: Piblarg*

- **Use Hunyuan at low denoise as refiner for VACE outputs**
  - Context: To refine results without losing character traits
  - *From: traxxas25*

- **Gray works best for VACE masking**
  - Context: When doing subject removal or replacement
  - *From: traxxas25*

- **Tint mask color to background for better subject removal**
  - Context: When using VACE for removing subjects from video
  - *From: ArtOfficial*

- **Blur depth maps and make them darker when combining with pose**
  - Context: When blending depth and pose controls in VACE
  - *From: Kijai*

- **Use first steps with pose only for more character shape freedom**
  - Context: When combining multiple control inputs in VACE
  - *From: Kijai*

- **Use mask to composite back into original video**
  - Context: To avoid background artifacts when doing character transformations
  - *From: David Snow*

- **Don't use blurred masks**
  - Context: When working with segmentation masks for control
  - *From: Zuko*

- **Add 'rotating' in prompt for better rotation control**
  - Context: When trying to get objects to rotate properly
  - *From: Kijai*

- **Use reference images with VACE for better control**
  - Context: When trying to get specific character transformations
  - *From: Kijai*

- **Don't use depth LoRA for final upscale refinement**
  - Context: Better results without LoRA in refinement step
  - *From: Piblarg*

- **Use black images as ignored control frames**
  - Context: For Fun Control - send black image and it's ignored as control, allows multiple controls at different time steps without overlap
  - *From: Kijai*

- **Duplicate input 4 times for better frame preservation**
  - Context: When you want to keep specific frames intact in VACE, duplicating input 4 times may help reduce temporal leakage
  - *From: Kijai*

- **Use block swap for memory optimization**
  - Context: Use at least 1 VACE block swap for almost no VRAM usage with offloading
  - *From: Kijai*

- **Desaturate normal map outputs**
  - Context: When using depth/normal preprocessing, ensure no color remains - should be grayscale only
  - *From: David Snow*

- **Match reference image pose to first frame**
  - Context: For best VACE results, reference image should match the pose of the first frame
  - *From: HeadOfOliver*

- **Use 4 frames for single image generation**
  - Context: When doing single frame generation with Wan, generate 4 frames and extract the first to avoid noise
  - *From: Colin*

- **Use dark line preprocessor and multiply over top**
  - Context: Better approach for line art preprocessing
  - *From: David Snow*

- **Aesthetic LoRA obliterates motion**
  - Context: When using reward LoRAs for quality improvement
  - *From: David Snow*

- **Use full white for full effect in VACE outpainting**
  - Context: For outpainting masks, though gray might work better for inpainting
  - *From: Kijai*

- **DiffSynth LoRAs should be used at 0.5 strength instead of 1.0**
  - Context: Since they're 2x stronger than originals without alpha keys
  - *From: Kijai*

- **Use reward LoRAs at CFG 1 for quality improvement**
  - Context: Even at CFG 1 it improves quality
  - *From: Pedro (@LatentSpacer)*

- **Lower strength when doing frame extension with first frame as reference**
  - Context: When using VACE for frame extension with reference frame to help fidelity
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use standard 1.3B with aesthetics lora instead of DG if using loras**
  - Context: When wanting to use loras, standard model works better than distilled
  - *From: DawnII*

- **Be detailed with prompts when doing character replacement**
  - Context: When using VACE for character replacement with reference images
  - *From: traxxas25*

- **Use animated diff masks for advanced control**
  - Context: For more sophisticated video manipulation workflows
  - *From: David Snow*

- **LoRAs help with likeness consistency on unseen angles**
  - Context: For I2V when character needs to turn head or bow, T2V lora applied to I2V model improves results
  - *From: Faux*

- **Use lower shift values for more motion**
  - Context: Lower values = more motion, 5 is more stable value, try 3 and 7 shift
  - *From: Benjimon*

- **Start prompts with action description**
  - Context: Start prompt with something like 'A mid shot action video sequence' for better motion
  - *From: Benjimon*

- **Use frame generation for quick testing**
  - Context: Set number of frames to 1 to generate images from Wan for quick testing, then use 'run (instant)' to iterate settings
  - *From: Jas*

- **Use AI for prompt generation**
  - Context: Use Claude, ChatGPT or Gemini to create prompts, then use node to incrementally go through them
  - *From: Jas*

- **Add 'mute' or 'mouth closed' to prevent lip movement**
  - Context: For animations without lip movement
  - *From: Cubey*

- **Pad reference images with white background**
  - Context: When using VACE reference images, pad with white background for better results
  - *From: A.I.Warper*

- **Use higher frame rate from source video for better motion**
  - Context: Big motion causes issues even with pose preprocessor
  - *From: notid*

- **Skip every second frame degrades motion significantly**
  - Context: When doing v2v, maintain full frame rate
  - *From: David Snow*

- **Depth is more stable input than pose**
  - Context: Pose preprocessors available are not great
  - *From: David Snow*

- **Use bbox mask for better VACE results**
  - Context: When doing face-only animation with VACE
  - *From: IllumiReptilien*

- **Lower control lora strength for reward loras**
  - Context: Reward loras should be used at 0.5-0.7 strength and introduce fireflies at higher strengths
  - *From: Kijai*

- **Use multiple controls by chaining VACE encodes**
  - Context: When you want to combine canny and depth or other controls
  - *From: David Snow*

- **Invert your lineart for better results**
  - Context: When using lineart controls in VACE
  - *From: David Snow*

- **Black areas in mask preserve original, white areas generate new content**
  - Context: When using input masks in VACE - black = original video, white = new generation
  - *From: Hashu*

- **Process without reward/high res loras first, add on second pass**
  - Context: When doing style transfer to avoid bias towards realism
  - *From: Hashu*

- **Use 2D, flat colour, cel-shading prompts to maintain style**
  - Context: When trying to prevent 2D to 3D style drift
  - *From: StableVibrations*

- **Increase overlap to reduce context window switching artifacts**
  - Context: When generating long videos with context windows
  - *From: David Snow*

- **Use CFG 2 with DG_Boost models**
  - Context: For better results with the new boosted models
  - *From: David Snow*

- **Use 50px padding for VACE reference images**
  - Context: Works fine, don't need the 256px shown in examples
  - *From: A.I.Warper*

- **Don't blur edges for VACE masks**
  - Context: Keep mask edges sharp for better results
  - *From: Kijai*

- **Use 'arms cropped, hands cropped out of view' to avoid drawing hands**
  - Context: When you don't want hands visible in the generation
  - *From: Kytra*

- **Tweak control blending percentages when combining multiple controls**
  - Context: 100% often gives bad results, 60% worked better for anime style
  - *From: Johnjohn7855*

- **Separate reference image and input frames with different strengths in VACE**
  - Context: Reference at 100% strength, input frames at 60% gave cleaner results
  - *From: Johnjohn7855*

- **For distant character details, crop out character and do stylization, then paste back to video**
  - Context: When character loses important details like robotic parts when far away
  - *From: Johnjohn7855*

- **Lower resolution to get more motion, use video to get control video, resize and run with VACE**
  - Context: When motion is required
  - *From: Johnjohn7855*

- **Too many controls tend to leave noise behind, increasing steps don't help**
  - Context: When combining multiple control methods
  - *From: Johnjohn7855*

- **Just stylize the first frame rather than using separate reference image**
  - Context: When using stylized first frame + ref-image seems redundant
  - *From: David Snow*

- **Use 20 blocks instead of 10 for block swap with 720 model**
  - Context: When dealing with VRAM issues on hefty 720 model
  - *From: David Snow*

- **Use last frame from previous generation as first frame + reference for continuity**
  - Context: For creating longer continuous videos by chaining generations
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Disable context windows for style preservation**
  - Context: When you want to maintain consistent style across generation
  - *From: David Snow*

- **Add contrast node to normal output for mouth movements**
  - Context: Helps model pick up on small facial movements and mouth details
  - *From: David Snow*

- **Use control video strength of 0.5-0.6 with reference at 1.0**
  - Context: Good balance for clean results while maintaining reference image influence
  - *From: Johnjohn7855*

- **Use simple car prompts like 'Car speeds over a snowy landscape'**
  - Context: Complex motion prompts don't help with car direction issues
  - *From: Verevolf*

- **Use end image to prevent color shifting in loops**
  - Context: When creating seamless video loops
  - *From: DawnII*

- **Start TeaCache at step 2 or 3 for better quality**
  - Context: When using TeaCache optimization
  - *From: MilesCorban*

- **Use last frame to start new video for extension**
  - Context: When extending Wan 14B videos with LoRAs
  - *From: Benjimon*

- **Train on videos only instead of mixed video/image datasets**
  - Context: When training 1.3B models using synthetic 14B data
  - *From: Piblarg*

- **Use SDPA attention for older GPUs like RTX 8000**
  - Context: RTX 8000 and similar older cards don't support BF16
  - *From: Benjimon*

- **Use pose control for butter smooth motion**
  - Context: Simple test with just pose input produces very smooth results
  - *From: David Snow*

- **Crank up LoRA strength to 2.0 for non-Fun LoRAs on Fun models**
  - Context: With 1.3B models, need higher strength to have any effect
  - *From: Kijai*

- **Use defaults for shift and cfg with Wan**
  - Context: Defaults work best, more important than with other models like HunyuanVideo
  - *From: Draken*

- **Try empty prompt or minimal prompts with FLF2V**
  - Context: Even empty prompt seems better sometimes, or model hallucinates too much between frames
  - *From: Kijai*

- **Disable force_offload for multiple consecutive runs**
  - Context: Will speed up subsequent runs on same workflow
  - *From: Kijai*

- **Use 768x768 or higher for 720p model**
  - Context: 720p model works better at 720x720 and up, closer to 1 megapixel
  - *From: Draken*

- **Use low denoise 0.38 with distilled 1.3B model**
  - Context: For fast rendering with good quality - 1.11 minutes for 161 frames
  - *From: Flipping Sigmas*

- **Set clipvision strength around 0.3 for more dynamic i2v**
  - Context: To make i2v less static, combine with specific motion prompting
  - *From: DevouredBeef*

- **Use Chinese prompts for FLF2V**
  - Context: Model was primarily trained on Chinese text-video pairs for better results
  - *From: DawnII*

- **Crank up shift a lot in HYV to get motion**
  - Context: HYV requires high shift values for dynamic movement
  - *From: Benjimon*

- **Use Chinese prompts for better FLF2V results**
  - Context: When using the new first frame last frame model
  - *From: DawnII*

- **Increase resolution for lip and eye direction following**
  - Context: When using Fun Control, use 576x1024 or higher
  - *From: A.I.Warper*

- **Use shift values of 20-30 for better VACE reference adherence**
  - Context: Counter to base models but improves style adherence
  - *From: DawnII*

- **Use lineart instead of depth for anime style content**
  - Context: When getting blur issues with VACE depth control
  - *From: Kijai*

- **Mix 3 control nets for better face control**
  - Context: Use depth (overall composition) + pose + line (face mimics)
  - *From: N0NSens*

- **Upscale original footage for vid2vid workflows**
  - *From: chrisd0073*

- **Overdo AI upscaling for toonish style conversion**
  - *From: David Snow*

- **Use smaller frame ranges for more stability**
  - *From: Hashu*

- **Force 16fps in video loader for better motion handling**
  - *From: Flipping Sigmas*

- **Consider tile size as quality control in FramePack**
  - *From: deleted_user_2ca1923442ba*

- **Use threshold to force consistency with mediapipe landmarks**
  - Context: When working with eye detection and control
  - *From: David Snow*

- **Use timestep scheduling instead of stacking VACE encodes**
  - Context: When wanting different strengths for different controls
  - *From: Kijai*

- **Blur depth maps for VACE compatibility**
  - Context: When VACE treats high quality depth maps as RGB grayscale inputs
  - *From: Kijai*

- **Always copy entire ComfyUI folder as backup before updating**
  - Context: To avoid reinstalling from scratch when updates break
  - *From: Thom293*

- **Use symlinked models folder with multiple ComfyUI installs**
  - Context: Allows sharing models across different ComfyUI versions while maintaining compatibility
  - *From: Nathan Shipley*

- **Force rate 24 instead of 16 for WAN helps with getting correct previews**
  - Context: When using VHS loader for output
  - *From: Flipping Sigmas*

- **Never install requirements.txt files**
  - Context: They're often full of unnecessary dependencies
  - *From: Kijai*

- **Enable animated previews during generation**
  - Context: Saves hours by allowing you to cancel bad runs early
  - *From: David Snow*

- **Check ComfyUI input folder regularly**
  - Context: It keeps copies of every media file loaded and can cause launch failures
  - *From: JohnDopamine*

- **Use specific camera movement prompts for better motion**
  - Context: Prompting 'tracking shot' gives more lively character outputs
  - *From: Jas*

- **For fast motion scenes, turn off all optimizations**
  - Context: Better quality for action sequences at cost of speed
  - *From: Benjimon*

- **Use shift up to 17 for SkyReels**
  - Context: When running SkyReels models
  - *From: Benjimon*

- **Run source footage through Topaz first for better results**
  - Context: When doing v2v processing - garbage in, garbage out principle
  - *From: David Snow*

- **Use Florence2 box detection instead of referring expression segmentation**
  - Context: For better mask tracking results
  - *From: Kijai*

- **Adding 'anime' to prompt improves overall quality**
  - Context: When using UniAnimate for anime-style content
  - *From: Kijai*

- **Use CFG of 2.0 with VACE**
  - Context: High CFG causes artifacts with VACE
  - *From: David Snow*

- **Use DPM++ or DEIS samplers to avoid blocky glitches**
  - Context: UniPC sampler causes weird issues, Euler with same settings won't
  - *From: David Snow*

- **Make all resolutions/frame lengths match for UniAnimate**
  - Context: Node will cut if too long and pad with last pose if too short
  - *From: Kijai*

- **Ignore ref pose for easiest UniAnimate setup**
  - Context: Load lora, use default I2V workflow, add pose inputs
  - *From: Kijai*

- **Style lora would probably help a lot with UniAnimate**
  - Context: When working with pose-driven animation
  - *From: Kijai*

- **Try different seeds to fix blocky artifacts**
  - Context: Wan models have similar blocky glitches that depend on seed, prompt, and CFG
  - *From: Screeb*

- **Lower CFG generally makes blocky artifacts better or go away**
  - Context: All Wan models can have blocky glitches
  - *From: Screeb*

- **Use camera movement prompts for FLF instead of scene details**
  - Context: When using First-Last-Frame morphing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Try UniPC FlowMatch scheduler for better results**
  - Context: When getting broken outputs
  - *From: yi*

- **Use fp32 for better quality but slower speed**
  - Context: When quality is more important than speed
  - *From: Kijai*

- **Update nodes before using new workflows**
  - Context: When using SkyReels workflows
  - *From: Kijai*

- **Enable animated preview to save time**
  - Context: Will save days worth of wasted generations in the long run - it's a gamechanger
  - *From: David Snow*

- **Use different prompts for each DF window**
  - Context: DF allows using different prompts etc. for each continuation window
  - *From: Kijai*

- **Use LoRAs instead of reference images for style transfer**
  - Context: Reference images cause flash at start and glitches, LoRAs work better despite limited availability
  - *From: David Snow*

- **Use VACE start/end frame node for automation**
  - Context: Auto fills grey frames and masks for you instead of manual setup
  - *From: Hashu*

- **Add SLG later rather than from the getgo**
  - Context: When optimizing workflow
  - *From: Kijai*

- **Use separate VACE encodes for multiple controls**
  - Context: Better than combining into one for reference image + line art
  - *From: David Snow*

- **Use anyline instead of canny for VACE**
  - Context: Much better choice for line art control
  - *From: David Snow*

- **Half-body pictures produce better faces**
  - Context: Larger face proportion in frame leads to better generated faces
  - *From: wange1002*

- **Never use precision higher than model weights**
  - Context: No point in using higher precision than what weights are stored at
  - *From: Kijai*

- **Use as much RAM as possible for speed**
  - Context: If you have 128GB RAM, use it all for faster performance
  - *From: lostintranslation*

- **Use empty frame (black or gray) for missing VACE components**
  - Context: When trying to separate VACE controls
  - *From: Kijai*

- **Combine depth, normal and line controls with image blend**
  - Context: Can encode multiple controls into single embed for both VACE and base 1.3B
  - *From: David Snow*

- **Use TeaCache 'e' mode for less memory usage**
  - Context: E mode uses ~600MB instead of ~4GB for cache
  - *From: Kijai*

- **VACE works best with cleanup and reruns**
  - Context: Can get amazing results with additional passes
  - *From: Draken*

- **Better preprocessors needed for VACE**
  - Context: VACE sensitivity to artifacts means preprocessing quality is crucial
  - *From: David Snow*

- **For I2V, only prompt the dynamics and let the image provide static context**
  - Context: When using SkyReels V2 I2V models, focus prompts on action/expression/camera motion rather than describing visual elements already in the image
  - *From: fredbliss*

- **Adjust TeaCache threshold to balance speed vs quality**
  - Context: TeaCache can degrade hands at higher settings, so find the right threshold balance. You can see how many steps it skips after sampling.
  - *From: Kijai*

- **Use spline editor for smooth CFG scheduling transitions**
  - Context: Instead of abrupt CFG changes, spline editor allows smooth transitions between CFG values across steps
  - *From: Kijai*

- **Clear VRAM and cache between runs to avoid OOM**
  - Context: Especially important when canceling runs midway to prevent memory issues
  - *From: MilesCorban*

- **Push start percent up from 1 to 10-30 for TeaCache**
  - Context: When experiencing first frame corruption
  - *From: JohnDopamine*

- **Use Resize To Closest node for better stride**
  - Context: Better at ensuring image has right stride leading to better videos
  - *From: jellybean5361*

- **Test at 33 frames minimum for quality assessment**
  - Context: Anything less than 33 frames doesn't work well for testing enhancements and settings
  - *From: Kijai*

- **Always keep cfgzerostar and Fresca enabled**
  - Context: Safe to always keep on, generally better output
  - *From: Kijai*

- **Use separate VACE embed for each sampler node**
  - Context: When combining VACE with DF model
  - *From: DawnII*

- **Use color match to fix brightness drift in extended videos**
  - Context: When chaining DF model videos together
  - *From: MilesCorban*

- **Check outputs and do seed hunting with each sampler for infinite generation**
  - Context: When creating long video sequences
  - *From: seitanism*

- **Adjust SLG start to 0.3 and end to 0.8 for better results**
  - Context: When experiencing discoloration or artifacts with default SLG settings
  - *From: zelgo_*

- **Don't go under 33 frames or over 97 frames**
  - Context: When using DF models, too low frame count needs different settings
  - *From: MilesCorban*

- **Use bigger frame overlap for better motion consistency**
  - Context: When character motion degrades in video extensions
  - *From: seitanism*

- **Use 27 frame overlap instead of default 17 for better extension quality**
  - Context: When doing video extension with DF
  - *From: boorayjenkins*

- **Use simpler images/scenes for better DF results**
  - Context: Complex scenes with lots of detail cause more degradation
  - *From: seitanism*

- **Color matching helps but be careful with scene changes**
  - Context: Can cause weird colors if scene changes too much
  - *From: Ablejones*

- **Use ID preprocessing for better identity retention with HYV**
  - Context: When doing identity-focused generation
  - *From: Mads Hagbarth Damsbo*

- **Stabilize content for V2V then matchmove back after generation**
  - Context: When dealing with temporal downsampling issues in HYV
  - *From: Mads Hagbarth Damsbo*

- **Try different overlap values for DF stitching**
  - Context: Default is 17 but 9 also works, can experiment with lower values for smaller inferences
  - *From: Kijai*

- **Avoid using same seed on all DF samplers**
  - Context: Sometimes causes repetition in diffusion forcing workflows
  - *From: Kijai*

- **Use WinDirStat to manage storage**
  - Context: For Windows users to understand which folders use most storage, especially cache folders that grow to absurd sizes
  - *From: mamad8*

- **Use cfg scheduling for speed**
  - Context: 1/3rd of steps with cfg 1 increases speed
  - *From: seitanism*

- **Prompt input frames carefully**
  - Context: Input frames are very strong and often override prompts - need to hold the model's hand and only write prompts for next sampler after being happy with previous output
  - *From: seitanism*

- **Use Keep Proportion for ultrawides**
  - Context: For ultrawide videos, use 1600x1600 with Keep Proportion in Image Resize node
  - *From: ezMan*

- **20 steps for testing, 50+ for quality**
  - Context: General guideline for step counts
  - *From: MilesCorban*

- **Start control embeds at 0.0 and end early rather than the other way around**
  - Context: When using control embeds, often start at 0.0 and end at 0.5
  - *From: David Snow*

- **Use blur on depth maps to allow more natural interpretation**
  - Context: Add blur node to depth map and turn down latent strength to let model interpret motion more naturally
  - *From: David Snow*

- **Use main_device only for cloud GPUs with 80GB+ VRAM**
  - Context: main_device should only be used for high VRAM setups or when using 1.3B models
  - *From: Kijai*

- **Mix depth with line/canny/pose to fix faces**
  - Context: Using multiple control types can improve face quality
  - *From: N0NSens*

- **For long vid2vid with VACE, feed it 5-6 frames from previous rendered piece**
  - Context: Don't do masking until after those frames, keep segments close to same length for consistent look
  - *From: TimHannan*

- **Use first frame instead of just reference image for better VACE results**
  - Context: First frame gets incorporated into actual frames, while ref image gets turned into data and fed to model
  - *From: Draken*

- **Can combine both first frame and reference image in VACE**
  - Context: Useful when first frame is close-up but you want model to know details that are off-screen
  - *From: Draken*

- **Don't update ComfyUI unless you have to**
  - Context: Only update when new model needs it or required node needs it to avoid breaking things
  - *From: Draken*

- **Use ComfyUI rope function instead of default**
  - Context: Comfy's rope is more efficient and avoids dtype errors
  - *From: Kijai*

- **Choose LOW versions for many steps rendering, HIGH models for few steps (6-8)**
  - Context: DG models usage, modify CFG to avoid over-saturated colors
  - *From: JmySff*

- **Padding beginning and end with first/last frame helps with degradation**
  - Context: DF extension workflows
  - *From: TimHannan*

- **Use same prompt that generated initial t2v/i2v clip in DF stage**
  - Context: When using t2v/i2v fed into DF approach
  - *From: anever*

- **Match 1.3B/14B LoRAs with right model when using DF**
  - Context: LoRA compatibility across model sizes
  - *From: anever*

- **For FantasyTalking, adjust audio scale - 0.5 works well for t2v**
  - Context: Audio conditioning strength
  - *From: Kijai*

- **With Wan LoRAs on Skyreels, consider using 16fps as LoRAs may be trained at that fps**
  - Context: Frame rate optimization
  - *From: hablaba*

- **Use CFG balance for Fantasy Talking**
  - Context: Finding balance between audio CFG and sampler CFG is key to good results
  - *From: Stad*

- **Use variable CFG scheduling**
  - Context: First 3 steps with audio CFG 5.0, rest at 1.0 for better quality
  - *From: Kijai*

- **Clip silence from audio**
  - Context: Remove empty audio at beginning to avoid sync issues with Fantasy Talking
  - *From: andrewrasmussen.*

- **Use swap memory for larger models**
  - Context: Can run 14B with only 8GB VRAM using SSD as additional RAM (slower but works)
  - *From: Stad*

- **Fantasy Talking works better with shorter prompts**
  - Context: Long prompts cause model to stop moving lips
  - *From: ingi // SYSTMS*

- **Use frame numbers that are multiples of 16+1**
  - Context: Model likes these frame counts - try 81 instead of 77
  - *From: ingi // SYSTMS*

- **Give VACE model room with single control**
  - Context: Often 1 control is enough, model needs space to work
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use vocal separation for Fantasy Talking**
  - Context: Clear speech works better, remove music backing for better results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Add duplicate frames at video start for LoRA flash issue**
  - Context: Cut them off in post to handle flash artifacts from LoRAs
  - *From: Gavmakes*

- **Use points editor workflow for masking**
  - Context: Send single frame first to add points, then full animation
  - *From: David Snow*

- **Keep empty frame level at 0.5**
  - Context: This is the default the model was trained with
  - *From: Kijai*

- **Save first frame and drag it over inputs when working with video segmentation**
  - Context: When node doesn't load first frame automatically
  - *From: ArtOfficial*

- **Use birme.net for quick batch image resizing**
  - Context: Free tool for preparing training datasets
  - *From: JohnDopamine*


## News & Updates

- **VACE model released**
  - Ali-vilab released VACE-Wan2.1-1.3B-Preview on HuggingFace - video control system with subject reference capabilities
  - *From: Kijai*

- **VACE also released for LTX**
  - VACE is available for both Wan and LTX models
  - *From: DawnII*

- **MuseTalk 1.5 released**
  - New version of MuseTalk released but requirements are problematic for ComfyUI integration
  - *From: burgstall*

- **FastVideo Wan support in development**
  - New support being prepared for Wan version in FastVideo project
  - *From: JohnDopamine*

- **VACE preview model released**
  - Video control system with style transfer, inpainting, subject-driven capabilities
  - *From: community*

- **Native ComfyUI support coming for VACE**
  - Official developer confirmed implementation in progress from China
  - *From: comfy*

- **Kijai added start/end percent controls to VACE**
  - Can end at halfway through steps for faster processing
  - *From: Kijai*

- **59 new Wan effects LoRAs released**
  - Collection includes T2V and I2V LoRAs for 14B model at 480p
  - *From: ⚡*

- **VACE planned for 14B model**
  - VACE people are intending on putting it on the 14B
  - *From: Piblarg*

- **VACE support added to Kijai's WanVideoWrapper**
  - New VACE Encode node available for comprehensive control similar to ACE++ for video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache memory optimization**
  - Fixed memory leak that was more apparent with VACE due to larger tensor sizes
  - *From: Kijai*

- **Wan Fun models released**
  - Wan fun (inpaint and control) models available a few days ago
  - *From: ˗ˏˋ⚡ˎˊ-*

- **New SkyReels A2 model released**
  - New model from Skywork AI team
  - *From: Juampab12*

- **VACE-14B model expected to drop**
  - Larger variant of VACE model coming
  - *From: Benjimon*

- **SkyReels-A2 released by SkyworkAI**
  - New model but lacks control features, diffusers format only, less interesting than VACE according to community
  - *From: Kijai*

- **12 new DiffSynth Wan 2.1 model variants**
  - Different levels of distilled + hires + refined editions, experimental versions supporting 4-10+ steps
  - *From: Kijai*

- **VACE compilation improvements**
  - Now compiles VACE blocks when compile transformer blocks selected, ~15% speed increase
  - *From: Kijai*

- **New Start to End Frame node available**
  - Kijai released helper node for managing start and end frames in VACE
  - *From: Kijai*

- **TinkerWAN Alpha lora updated to v1.0**
  - New version uses positive instead of negative values
  - *From: David Snow*

- **New example workflow with start/end frame and control with reference**
  - Kijai provided updated workflow examples in single file
  - *From: Kijai*

- **WanVideoWrapper nodes updated with error detection**
  - Added proper error messages to prevent common configuration mistakes
  - *From: Kijai*

- **New Test Pattern node added**
  - Helper node for creating test patterns and adding empties between frames
  - *From: Kijai*

- **Standalone VACE model released**
  - Separate VACE loader available, saves 6GB disk space and works with any 1.3B model
  - *From: Kijai*

- **VACE model select node pushed**
  - New node for loading standalone VACE models
  - *From: Kijai*

- **Multiple DG model variants available**
  - Various DG models (High, Light, V3, V4) available on HuggingFace
  - *From: Hashu*

- **New prev_embeds parameter added to VACE**
  - Allows multiple control inputs with different strengths and timestep ranges
  - *From: Kijai*

- **VACE context input made optional**
  - Fixed workflow compatibility issue
  - *From: Kijai*

- **New DG distilled models available**
  - Multiple variants (light/medium/high, v1-v4) for faster inference
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kosinkadink working on native ADE context implementation for Wan**
  - Will make ADE contexts treat any tensor dimension as batch, not just first dimension
  - *From: Kosinkadink*

- **Kosinkadink back from China conference but recovering from illness**
  - Development may be slower while recovering
  - *From: Kosinkadink*

- **New custom node released for text extraction**
  - ComfyUI-BS-Textchop for extracting multiple text segments
  - *From: burgstall*

- **SkyreelsA2 model released**
  - 14B model that does same as VACE with reference and start frame, better for I2V using 14B I2V model
  - *From: Kijai*

- **ComfyUI getting more unstable with recent updates**
  - Users reporting more frequent issues with custom nodes and loading after updates
  - *From: David Snow*

- **VACE native ComfyUI support coming soon**
  - Comfy will look into native VACE support once available
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SkyReels v2 paper released**
  - User excited about potential dataset release
  - *From: fredbliss*

- **New tiny autoencoder available**
  - Mentioned in passing, no details provided
  - *From: fredbliss*

- **Distilled Wan model available in pinned messages**
  - Community member points to pinned messages for distilled version
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Triton now easily installable on Windows**
  - Can now just pip install triton-windows, works with Python 3.12/CUDA 12 on Windows 11
  - *From: Lumi*

- **Dream Making released Frutiger Lora for 14B model**
  - Available on HuggingFace: dreamer8/FrutigerLora14B_Wan with sample generations
  - *From: Dream Making*

- **Major VACE memory optimization update pushed**
  - Significant VRAM reduction with minimal speed loss, removes redundant tensor conversions
  - *From: Kijai*

- **Reward LoRAs released**
  - HuggingFace repo alibaba-pai/Wan2.1-Fun-Reward-LoRAs now available with HPS2.1 and MPS variants
  - *From: Lumi*

- **VACE 14B final version in development**
  - VACE author confirmed they are working on final 14B version and seeking developer feedback
  - *From: HJ*

- **Native ComfyUI support for reward LoRAs**
  - ComfyUI added native support that converts the released reward LoRAs
  - *From: Screeb*

- **Tiled VACE encode added**
  - Kijai added tiled encoding option for VACE (2x2 tile) to handle higher resolutions
  - *From: Kijai*

- **VACE 14B model coming soon**
  - Kijai confirmed it looks like 14B VACE should be out pretty soon
  - *From: Kijai*

- **New reward LoRAs from DiffSynth-Studio released**
  - Different files with different transformer structure, works better than originals
  - *From: Pedro (@LatentSpacer)*

- **Kijai updated WanVideoWrapper with fixes**
  - Fixed tiled encoding and other improvements
  - *From: Kijai*

- **14B VACE model development mentioned**
  - Developers said 14B VACE is coming but not yet uploaded
  - *From: ameasure*

- **CFG distilled LoRA uploaded**
  - Distilled model LoRA now available for faster inference
  - *From: mkt*

- **Fixed batched CFG support**
  - Kijai added batched CFG support in recent update
  - *From: Kijai*

- **New aesthetic and highres LoRAs uploaded**
  - New HPS and MPS LoRAs uploaded yesterday, different file sizes from previous ones
  - *From: David Snow*

- **Pytorch starting to have nvfp4 support**
  - Would give further edge to the 5000 series GPUs
  - *From: Kijai*

- **IP Adapter for Wan 1.3b announced**
  - Ostris announced IP Adapter with impressive adherence, early stages but promising
  - *From: pom*

- **ReCamMaster model available**
  - Camera control model for Wan 2.1, available in branch but not merged to main
  - *From: Kijai*

- **New detail enhancement LoRA released**
  - dg_wan2_1_v1_3b_lora_extra_noise_detail_motion.safetensors - adds significant detail, max recommended 0.35
  - *From: David Snow*

- **Multiple new boost LoRAs released**
  - Boost ares, Boost evol, Boost stock, Boost train - 20 different variants available
  - *From: DawnII*

- **SkyReels-A2 model released**
  - New model that needs its own workflow, has example with wrapper
  - *From: AI_Fan*

- **WanWrapper updated with simple nodes**
  - Kijai merged simple version nodes to main branch
  - *From: Kijai*

- **New DG_Boost model variants released**
  - Multiple versions including Evol V3, configured for 5-6 steps, compatible with Diffusion Pipe training tool, final version from creator
  - *From: David Snow*

- **Kijai added mask padding to VACE**
  - Fixed issue where mask edges become obvious by automatically padding masks
  - *From: Kijai*

- **New schedulers added to WanVideoWrapper**
  - DEIS, DPM, UniPC, Beta schedulers added - DEIS seemed somewhat sharper, UniPC/Beta showed promise
  - *From: Kijai*

- **OptimalSteps implemented for WAN native**
  - GitHub repo bebebe666/OptimalSteps provides custom sigmas for potentially faster generation
  - *From: crinklypaper*

- **Pusa-VidGen has Wan2.1 on roadmap**
  - GitHub project planning Wan2.1 integration
  - *From: yi*

- **SynCamMaster-Wan2.1 released**
  - New camera control system for Wan 2.1 available on HuggingFace
  - *From: yi*

- **First animated logo LoRA released**
  - First version available on Civitai, result not perfect but ready to start
  - *From: Alisson Pereira*

- **Wan 2.1 Knowledge Base ported to Notion**
  - Complete channel summary with videos and workflows now publicly accessible
  - *From: Nathan Shipley*

- **SkipLayerGuidanceDiT node available in ComfyUI**
  - Same as SLG args for skipping layers in diffusion models
  - *From: yi*

- **CausVid released for faster Wan inference**
  - Alternative sampling method that runs model differently instead of sampling all frames together
  - *From: Cubey*

- **Wan2.1-FLF2V-14B-720P model released**
  - First-last frame to video generation model, 720p only, available on HuggingFace with fp16 and fp8 versions
  - *From: JohnDopamine*

- **CublasOps in ComfyUI speeds up fp16 inference by ~20%**
  - New commit in ComfyUI for faster fp16 inference, works well with SDXL
  - *From: yi*

- **TheDirector workflow published**
  - Custom node for 2-24 scene Wan generation in one go with consistent characters using Gemini
  - *From: AJO*

- **FramePack I2V released by lllyasviel**
  - New system for generating long duration videos (up to 1 minute) with minimal VRAM. HYV weights available on HuggingFace
  - *From: JohnDopamine*

- **Wan FLF2V 14B 720P officially released**
  - Now available on official Wan-AI repo with Chinese prompt recommendation
  - *From: DawnII*

- **Kijai working on FramePack ComfyUI implementation**
  - Very early mockup version running with native models except transformer
  - *From: Kijai*

- **Union Pro 2.0 Flux ControlNets released**
  - New insane Flux control nets just dropped
  - *From: Draken*

- **Wan FLF2V (First Frame Last Frame) model released**
  - 14B model for 720P with fp8 quantization available
  - *From: 🦙rishappi*

- **FramePack model released**
  - Currently only for Hunyuan, allows low VRAM video generation and longer videos
  - *From: BondoMan*

- **UniAnimate-DiT released**
  - New model from ali-vilab
  - *From: yo9o*

- **FLUX.1-dev-ControlNet-Union-Pro-2.0 released**
  - New ControlNet model from Shakker-Labs
  - *From: PolygenNoa*

- **SkyReels V2 models released**
  - Multiple variants: I2V 14B at 540P and 720P, T2V 14B at 540P and 720P, DF 1.3B at 540P - all based on Wan 2.1 and finetuned on 10M clips
  - *From: yi*

- **UniAnimate-DiT repository available**
  - New repository for UniAnimate-DiT, ComfyUI implementation expected soon
  - *From: amli*

- **Wan developer AMA on Twitter**
  - Lead developer shared that they have faster models but don't have OK to open source yet, expects VACE for 14B to perform much better than 1.3B
  - *From: JohnDopamine*

- **FLF2V GGUFs uploaded**
  - city96 uploaded GGUF versions of Wan2.1-FLF2V-14B-720P
  - *From: gshawn*

- **SkyReels models made private/deleted from HuggingFace**
  - All SkyReels V2 model weights were removed, possibly uploaded early by mistake before code release
  - *From: Screeb*

- **UniAnimate-DiT released**
  - Pose controlnet for 14B I2V models with LoRA weights and pose embeds, includes improved dwpose detector with feet
  - *From: Kijai*

- **I2V model and new scheduler need new inference code**
  - Current I2V runs but results are broken, no code released yet
  - *From: Kijai*

- **FreSca integration added to WanVideoWrapper**
  - Now available through the wrapper interface
  - *From: Kijai*

- **SkyReels Wan version was released then taken down**
  - Released today but quickly removed, will be rereleased later
  - *From: Piblarg*

- **Skycaptioner will be released after a week**
  - Was accidentally made public before intended release
  - *From: yi*

- **DMD (step distillation) coming to SkyReels v2**
  - Will reduce step count from 50 to 5 steps for faster generation
  - *From: yi*

- **SeedVR upscaler potentially releasing in August**
  - Developer commented on issues saying hopefully they can get approval to release open by August
  - *From: JohnDopamine*

- **SkyReels V2 models released**
  - All models now available on HuggingFace including Diffusion Forcing version for infinite length videos
  - *From: yi*

- **SkyReels V2 code released**
  - GitHub repository now available with implementation
  - *From: yi*

- **SkyCaptioner V1 released**
  - Video captioning model now available on HuggingFace
  - *From: Persoon*

- **SkyReels V2 models released**
  - 1.3B and 14B I2V models at 540P, plus Diffusion Forcing variants
  - *From: multiple users*

- **5B SkyReels model spotted**
  - Larger variant appears to be in development
  - *From: Draken*

- **VACE compatibility with SkyReels DF confirmed**
  - Successfully tested with 161 frames
  - *From: DawnII*

- **MAGI-1 24B model released**
  - Fully autoregressive with V2V and I2V, 1440p VAE, 4.5B variant coming soon
  - *From: yi*

- **SkyReels V2 DF models available**
  - 1.3B and 14B variants with Diffusion Forcing, only 1.3B has fps embeds
  - *From: Kijai*

- **Chipmunk embedding caching tool**
  - New tool for embed caching to improve performance
  - *From: yi*

- **Native VACE bad results fixed**
  - Python whitespace issue resolved
  - *From: comfy*

- **VRAM management issue fixed**
  - Expected tensors device error resolved in latest WanWrapper
  - *From: Kijai*

- **Sigmas input added to WanSampler**
  - New feature in latest wrapper version for experimenting with OptimalSteps scheduler
  - *From: Kijai*

- **Phantom model released**
  - Phantom-Wan 1.3B available, appears to be module to add to base Wan similar to VACE
  - *From: DawnII*

- **New quantization method for video models**
  - Paper on SOTA diffusion model quantization that works on video models
  - *From: deleted_user_2ca1923442ba*

- **SkyReels V2 structured prompting revealed**
  - Paper shows detailed JSON schema for structured video prompting with subjects, camera, environment
  - *From: fredbliss*

- **Phantom model now available with ComfyUI support**
  - Phantom code pushed to dev branch for testing. It's a 1.3B parameter model that uses 10.6GB VRAM for 1280x768x81 generation.
  - *From: Kijai*

- **SkyReels V2 models and methodology released**
  - New approach focusing on dynamics-only prompting for I2V, with structured caption fusion methodology
  - *From: fredbliss*

- **New SkyReels V2 models released**
  - T2V and I2V variants with improved quality for humans
  - *From: mamad8*

- **DF (endless generation) model available**
  - Allows extending videos by taking last 17 frames and generating new 97-frame clips
  - *From: seitanism*

- **Phantom model now available**
  - 1.3B model for subject reference, works like SkyReels A2 but smaller
  - *From: DawnII*

- **VACE + DF combination working**
  - Can now use VACE with DF model for better continuation
  - *From: mamad8*

- **Phantom model available in wrapper dev branch**
  - New character consistency model now integrated into WanVideoWrapper
  - *From: Kijai*

- **TeaCache support added to Skyworks models**
  - Default values added for Skyworks models in teacache
  - *From: jellybean5361*

- **Fix pushed for clip model compatibility**
  - Fixed compatibility issues with different clip model formats
  - *From: Kijai*

- **SkyReels teases Camera Director model**
  - Coming Soon on their HuggingFace
  - *From: seitanism*

- **SkyReels released 6 models recently**
  - Multiple new models in recent days
  - *From: seitanism*

- **Diffusion Pipe now supports SkyReels training**
  - Added support for training likenesses on SkyReels models
  - *From: JohnDopamine*

- **Skyreels V2 models released with 720p support**
  - New 720p I2V and DF models uploaded to HuggingFace, native 24fps output
  - *From: jellybean5361*

- **WAN going commercial**
  - Wan announced commercialization, suggesting potential changes to open source availability
  - *From: JohnDopamine*

- **RealisDance-DiT and Uni3C coming**
  - Two new WAN 2.1 utilities for controlling humans in videos, weights releasing same day
  - *From: yi*

- **New Fun Control Camera model released**
  - Wan2.1-Fun-V1.1-1.3B-Control-Camera available on HuggingFace
  - *From: DawnII*

- **Sparge attention model available**
  - There is now a sparge attention model for wan2.1 1.3B variant for memory optimization
  - *From: yi*

- **Wan team promises low VRAM version**
  - Someone from Wan team said they'd add 'low VRAM version' with their optimizations mentioned in the paper
  - *From: Kijai*

- **Fun 1.1 models released with improved inpaint and control capabilities**
  - Inpaint model trained with larger batch size for more stable performance, Control model includes reference image functionality
  - *From: DawnII*

- **14B models are now available**
  - 14B versions of the models are being released
  - *From: DawnII*

- **Kijai merged dev to main branch**
  - Most things seem to work so dev branch was merged to main
  - *From: Kijai*

- **Step1X-Edit model released with MIT license**
  - New editing model that seems good for editing first frame of video then using Wan to modify whole video
  - *From: mamad8*

- **ComfyUI frontend 1.17.11 reported as glitchy**
  - Users experiencing issues with latest frontend version, recommendation to wait before updating
  - *From: David Snow*

- **Kijai updated node to fix frontend compatibility issues**
  - Old node made no sense with frontend update and caused errors between workflows saved with different frontend versions
  - *From: Kijai*

- **Fix pushed for default rope dtype issues**
  - Kijai fixed default rope option but recommends using comfy rope as it's more efficient
  - *From: Kijai*

- **Fun 1.1 models released with better performance**
  - Includes reference image support
  - *From: Kijai*

- **FantasyTalking model released - Wan-based lip sync**
  - Audio + image to video, 81 frames, uses 720p model as base
  - *From: Kijai*

- **CausVid model published - 4-step distillation from 50-step model**
  - T2V model for faster inference, extends DMD to videos
  - *From: multiple users*

- **TransPixeler added Wan support**
  - Available in branch on GitHub
  - *From: JohnDopamine*

- **Fantasy Talking model released**
  - New lip sync model from Alibaba using 14B I2V, outputs 23fps, English only
  - *From: Multiple users*

- **Multiple character LoRAs released on Civitai**
  - Large batch of anime character models for Wan T2V just released
  - *From: Kytra*

- **Wan2.1-Fun-V1.1-1.3B-Control-Camera model released**
  - New camera control model for Wan, usage unclear
  - *From: N0NSens*

- **Fantasy Talking ComfyUI implementation available**
  - Kijai implemented ComfyUI nodes within hours of model release
  - *From: Multiple users*

- **Fun Camera Control released**
  - Compatible with AnimateDiff camera control poses, supports pan movements
  - *From: Kijai*

- **New camera control for 3D movements**
  - Based on Google's RealEstate10K dataset, supports controllable camera paths
  - *From: Kijai*


## Workflows & Use Cases

- **Second-pass enhancement with 1.3B**
  - Use case: Improving old Hunyuan/Wan generations using v2v with depth, highres, aesthetics loras at 6-8 steps
  - *From: David Snow*

- **Long video extension with InP model**
  - Use case: Creating longer videos by extending with the InP model, though context windows better for long vid2vid
  - *From: Kijai*

- **VACE with depth video input**
  - Use case: Using depth video as control signal for VACE model, works better than InP for subject consistency
  - *From: Kijai*

- **Video extension using VACE**
  - Use case: Extending videos by masking empty gray frames with video content
  - *From: Kijai*

- **Reference image + depth control**
  - Use case: Character consistency with pose control
  - *From: multiple users*

- **Outpainting with VACE**
  - Use case: Expanding video canvas dimensions
  - *From: Kijai*

- **VACE style transfer with pose control**
  - Use case: Consistent style transfer with pose guidance using DWPose preprocessor
  - *From: ingi // SYSTMS*

- **Double passing old Wan output with 1.3B**
  - Use case: Improving quality of previous generations
  - *From: David Snow*

- **Context window processing for long videos**
  - Use case: Processing videos longer than 81 frames by splitting into overlapping windows
  - *From: Kijai*

- **480p generation then V2V upscale to 720p**
  - Use case: Quick upscaling - V2V upscale only needs 8-10 steps
  - *From: zelgo_*

- **Reference image face swapping with VACE**
  - Use case: Subject replacement in videos using reference image and video input
  - *From: Kijai*

- **Loop generation for lofi girl style videos**
  - Use case: Seamless looping videos with consistent style using custom LoRAs
  - *From: Mint*

- **Character lora + pose rig into VACE**
  - Use case: Character consistency with controlled poses using text2video
  - *From: Kytra*

- **Reference image with proper masking for VACE**
  - Use case: Placing subjects with background removed or padded images
  - *From: Kijai*

- **VACE with depth control for motion transfer**
  - Use case: Applying motion from driving video to static images
  - *From: seitanism*

- **Mixed frame input for VACE**
  - Use case: First frame as reference image, remaining frames as control input for motion guidance
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Outfit swap with gray masking**
  - Use case: Composite gray over clothing areas in input frames, use reference image to guide replacement
  - *From: Zuko*

- **Blended depth and pose control**
  - Use case: Overlay pose on top of depth maps for combined facial performance and body motion
  - *From: A.I.Warper*

- **Start to End Frame with VACE masking**
  - Use case: Creating controlled animations between specific start and end frames while preserving facial identity
  - *From: slmonker(5090D 32GB)*

- **Multi-frame keyframe workflow**
  - Use case: Creating smooth transitions through multiple keyframes (1st-mid-end frames)
  - *From: slmonker(5090D 32GB)*

- **Combined depth and pose control**
  - Use case: Using both depth maps and pose detection for enhanced motion control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context window long video generation**
  - Use case: Generating very long videos (1300+ frames) using context windows
  - *From: Kijai*

- **Loop video creation**
  - Use case: Creating seamless loop videos by using first frame as last frame
  - *From: slmonker(5090D 32GB)*

- **VACE with reference and prompt**
  - Use case: Character consistency in video generation using reference image with text prompts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Bounding box control for T2V/I2V**
  - Use case: Controlling specific regions in video generation, works better with I2V than T2V
  - *From: Kijai*

- **Combined depth/normals/lineart preprocessing**
  - Use case: Enhanced detail in video generation by combining multiple depth estimation methods
  - *From: David Snow*

- **Multiple control inputs using prev_embeds**
  - Use case: Use pose for half the steps, depth for the rest, or both at same time with reduced strength
  - *From: Kijai*

- **Separate VACE module loading**
  - Use case: Load base 1.3B and VACE separately for more flexibility, works with DG models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Depth + reference with prev_embeds**
  - Use case: First encode 0-0.2 with depth map and ref, second encode 0.2-1 with only ref image
  - *From: zelgo_*

- **First frame extraction and restyling pipeline**
  - Use case: Grab first frame, restyle with Stable Diffusion, use as reference for video restyling - similar to Runway restyle
  - *From: VRGameDevGirl84(RTX 5090)*

- **3D model animation to ComfyUI pipeline**
  - Use case: Animate 3D model with .anims in Unity, export video on black background, import to ComfyUI for processing
  - *From: Kytra*

- **VACE inpainting with start frame + trajectory + bbox + reference**
  - Use case: Character replacement and object manipulation in videos
  - *From: Kijai*

- **SkyreelsA2 reference workflow**
  - Use case: Using reference images with 14B model for better I2V results
  - *From: Kijai*

- **Bbox inpainting with yo9o method**
  - Use case: Custom inpainting workflow developed for targeted object modification
  - *From: yo9o*

- **3D cube to video generation**
  - Use case: Converting 3D animated shapes to realistic video using reference images
  - *From: ingi // SYSTMS*

- **Two-step character replacement**
  - Use case: Generate clean background first, then character with proper lighting, composite together
  - *From: traxxas25*

- **VACE temporal inpainting for frame extension**
  - Use case: Keep certain frames with black mask, generate new frames in white mask areas
  - *From: Kijai*

- **Context windows for long video generation**
  - Use case: Generate longer videos by splitting into overlapping chunks
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Automated subject removal with Gemini and segmentation**
  - Use case: Remove subjects and objects automatically for clean plates
  - *From: yo9o*

- **VACE video extension with 4-frame overlap**
  - Use case: Creating longer videos by extending 33-frame chunks with 4-frame overlap, allows new prompts and control adjustments per segment
  - *From: Hashu*

- **Depth and pose control blending**
  - Use case: Using separate VACE encode nodes for depth and pose with reduced strength or step switching
  - *From: yo9o*

- **Subject removal with VACE**
  - Use case: Removing people/objects from video using proper masking techniques
  - *From: ArtOfficial*

- **Two-step refinement: 1.3B initial generation then 14B refinement**
  - Use case: Getting quality while managing speed - generate with 1.3B then refine with 14B at low denoise
  - *From: Piblarg*

- **Character mask workflow for clean backgrounds**
  - Use case: Generate character transformation then composite back to avoid background artifacts
  - *From: David Snow*

- **Multi-frame VACE with intermediate frames**
  - Use case: Create video in editor with white frames between keyframes for more control points
  - *From: VRGameDevGirl84(RTX 5090)*

- **Infinite video generation with VACE**
  - Use case: Create long videos by keeping last 4 frames of each render as beginning frames of next batch
  - *From: JmySff*

- **VACE inpainting for watermark removal**
  - Use case: Remove watermarks by compositing mask to input and using reference image
  - *From: Alisson Pereira*

- **VACE outpainting**
  - Use case: Expand video frames in any direction - very simple setup
  - *From: Kijai*

- **Triple preprocessor setup for control**
  - Use case: Using video-depth-anything, lotus normals, anyline lineart for comprehensive control
  - *From: David Snow*

- **VACE with dual encode nodes for different strengths**
  - Use case: Using 2 different VACE encode nodes with prev_embeds for blending lineart and depth
  - *From: Hashu*

- **5-extension workflow for long videos**
  - Use case: 81 frame chunks extended 5 times, 30 minutes total generation time
  - *From: Hashu*

- **Upscale/refine workflow with reward LoRAs**
  - Use case: Using 1.3b-control with reward LoRAs for upscaling
  - *From: HeadOfOliver*

- **VACE infinite loop using frame extension and Flux**
  - Use case: Mix frame extension with i2i of last frame through Flux to use as ref in VACE in a loop
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Character replacement with VACE**
  - Use case: White padding on reference, openpose for movement, comp background with mask, optional vid2vid with low denoise
  - *From: traxxas25*

- **Using conditioning combine nodes for better results**
  - Use case: Runs multiple predictions and combines them, takes longer but better results than simply mixing controlnet images
  - *From: JmySff*

- **VACE subject removal**
  - Use case: Remove any subject (cars, birds, people) from videos using BBOX detection
  - *From: ArtOfficial*

- **Multi-pass refinement**
  - Use case: First pass VACE generation, then vanilla 1.3B with enhancement LoRAs for 8 steps to improve quality
  - *From: David Snow*

- **V2V with VACE start frame and control**
  - Use case: Video-to-video with around 0.8 denoise, start image, depth and lineart control
  - *From: David Snow*

- **VACE with DWpose face only**
  - Use case: Character animation with lip sync using reference image and grey background masking
  - *From: IllumiReptilien*

- **Two-pass VACE workflow**
  - Use case: 60 steps VACE with pose + ref frame, then 8 steps second pass
  - *From: A.I.Warper*

- **Crop and paste back workflow**
  - Use case: Cropping character at full resolution, processing through VACE, then pasting back in place
  - *From: A.I.Warper*

- **Context window looping**
  - Use case: 169 frames, uniform looped context for better loops but slower processing
  - *From: Kijai*

- **Multiple VACE controls**
  - Use case: Using canny and depth simultaneously by chaining VACE encodes
  - *From: StableVibrations*

- **Object replacement with masking**
  - Use case: Replacing objects in videos using input masks - black preserves original, white generates new
  - *From: IllumiReptilien*

- **Two-pass style processing**
  - Use case: First pass without enhancement loras, second pass adds them to avoid realism bias
  - *From: Hashu*

- **Looping with AnimateDiff upscaler**
  - Use case: Running flashing loops through AnimateDiff upscaler to make more seamless and increase color contrast
  - *From: Jas*

- **VACE with reference image for style transfer**
  - Use case: Getting specific art styles that are difficult to achieve with LoRAs alone
  - *From: David Snow*

- **Two-stage VACE generation**
  - Use case: Save latents in first stage, decode in second stage to avoid reference image being merged into first frames
  - *From: Johnjohn7855*

- **Multi-pass generation for camera movement**
  - Use case: Generate video in first pass, then use Recam in second pass for single image input
  - *From: David Snow*

- **VACE with start/end frames and control preprocessor**
  - Use case: Direct i2v with control frames for stylization while maintaining control
  - *From: David Snow*

- **Crop and paste system for distant characters**
  - Use case: Running distant character at full resolution by cropping subject with masking then pasting back to source video location
  - *From: A.I.Warper*

- **Fun control for vid2vid**
  - Use case: Works well for video to video generation
  - *From: boorayjenkins*

- **Mixing depth input with sporadic lineart frames**
  - Use case: Give helper frames on ones model doesn't read well - works better than putting actual reference frames
  - *From: TimHannan*

- **Looping video generation with last frame continuation**
  - Use case: Creating extended video sequences by feeding last frame of previous generation as input to next
  - *From: AJO*

- **Reference + control for first gen, then last frame + reference + control for subsequent**
  - Use case: Maintaining consistency across multiple video generations
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Triple control setup with depth, normal, and reference**
  - Use case: Maximum temporal consistency and detail preservation
  - *From: David Snow*

- **3x RIFE interpolation then drop every other frame**
  - Use case: Converting 16fps Wan output to 24fps for film
  - *From: Kijai*

- **Multiple clip generation with frame dropping**
  - Use case: Create 3-5 clips in one workflow, drop duplicate frames, interpolate 3x with RIFE
  - *From: seitanism*

- **Seamless loop creation**
  - Use case: Best system for creating seamless video loops with color matching
  - *From: gshawn*

- **TheDirector custom node**
  - Use case: Create 2-24 scene wan generation in one go with consistent character images
  - *From: AJO*

- **First-last frame generation with FLF2V model**
  - Use case: Generate video between two specific frames with better coherence
  - *From: Kijai*

- **Combining depth and normals for control**
  - Use case: Better stability in controlled video generation
  - *From: David Snow*

- **Multiple LoRA mixing with distilled 1.3B**
  - Use case: Fast rendering: Ghibli LoRA + ex LoRA + depth control, 8 steps, CFG 1.5, 161 frames in 1.11 minutes
  - *From: Flipping Sigmas*

- **VACE arbitrary frame interpolation**
  - Use case: True interpolation by placing input frames on every other frame, having VACE interpolate missing ones
  - *From: Screeb*

- **Perspective change with VACE + DWPose**
  - Use case: Use Blender to move camera with dwpose, then img2vid with dwpose control for perspective changes
  - *From: hablaba*

- **VACE temporal masking with first frame**
  - Use case: Using stylized first frame as keyframe with control frames for rest of sequence
  - *From: Kijai*

- **Daisy chaining VACE runs for long sequences**
  - Use case: Extract last frame from first run, use as start for next run with shifted control video
  - *From: A.I.Warper*

- **Fun Control with multiple control nets**
  - Use case: Combining depth + pose + lineart for better face control
  - *From: A.I.Warper*

- **Two-pass VACE processing with stitching**
  - Use case: Creating longer videos while maintaining character consistency
  - *From: A.I.Warper*

- **VACE with first pass and FUN cleanup**
  - Use case: Faster processing while maintaining quality
  - *From: A.I.Warper*

- **Flux i2i + LoRAs + Redux for first frame restyling**
  - Use case: Preparing stylized starting frames
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use original video as latents with mask for selective face preservation**
  - Use case: Keep face from start image while using original video for the rest
  - *From: DeZoomer*

- **Style transfer using V2V low denoise with DG models plus ExVideo LoRA**
  - Use case: Simple style transfer for long videos, used for 1000 frame generations
  - *From: Flipping Sigmas*

- **Redux for image restyling with 0.6-0.8 denoise + LoRA**
  - Use case: Image-to-image style transfer and character modification
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 1.3B upscaling with controlnets**
  - Use case: Video upscaling while preserving structure using depth and lineart guidance
  - *From: David Snow*

- **VACE ref2vid for restyling**
  - Use case: Style transfer on videos with depth and line art controls
  - *From: sneako1234*

- **VACE v2v with 5 LoRAs and prompting**
  - Use case: High-quality video transformation at 1280x544 ultrawide resolution with denoise at 0.8
  - *From: David Snow*

- **Generate at 480p then upscale to 720p**
  - Use case: Using 14B for animation then upscaling with ultrasharp
  - *From: PirateWolf*

- **Using UniAnimate for pose-driven animation**
  - Use case: 1GB LoRA weights with pose embeds, works with both 14B and 720p models
  - *From: Kijai*

- **UniAnimate with basic 14B I2V**
  - Use case: Pose-driven animation using dwpose detection
  - *From: Kijai*

- **VACE with background removal**
  - Use case: Style transfer while preserving green screen background
  - *From: David Snow*

- **Context window for video extension**
  - Use case: Extending video length with Wan 14B
  - *From: hablaba*

- **Second pass enhancement**
  - Use case: Improving VACE oversaturated outputs
  - *From: Gavmakes*

- **FLF morphing with camera movement prompts**
  - Use case: Creating smooth transitions between different frames
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video extension with Fun inp for 14B**
  - Use case: Extending videos when VACE not available for 14B
  - *From: Kijai*

- **VACE with SkyReels DF for long generation**
  - Use case: 161 frame generation with control
  - *From: DawnII*

- **LTX + 1.3B cleanup pass**
  - Use case: Use LTX for initial generation, then cleanup with 1.3B using depth/normal/line controls and Florence2 prompts
  - *From: David Snow*

- **DF + VACE combination**
  - Use case: Combine Diffusion Forcing with VACE controls for extended video generation with style control
  - *From: Kijai*

- **Chained DF nodes for infinite video**
  - Use case: Chain DF sampler nodes with decode/encode between each to continue video indefinitely
  - *From: Kijai*

- **Two-pass video generation**
  - Use case: Higher quality output by feeding sampler output into another sampler
  - *From: lostintranslation*

- **Face restoration workflow**
  - Use case: Crop, inpaint and stitch workflow targeting faces using CropAndStitch nodes
  - *From: David Snow*

- **VACE upscaling workflow**
  - Use case: Using VACE for upscaling instead of traditional methods
  - *From: Cseti*

- **Multi-stage sampling with sigma split**
  - Use case: Better quality and faster generation by splitting steps into two parts with different CFG
  - *From: lostintranslation*

- **VACE upscale workflow**
  - Use case: Upscaling videos using VACE with reference images
  - *From: Cseti*

- **480p to 720p upscaling**
  - Use case: Video resolution upscaling workflow
  - *From: Cseti*

- **SkyReels V2 I2V with dynamics-only prompting**
  - Use case: Generate videos from images using only motion/action descriptions, letting the image provide static visual context
  - *From: fredbliss*

- **Multi-reference Phantom workflow**
  - Use case: Generate videos with multiple reference images (up to 4) for consistent character/object generation
  - *From: Kijai*

- **CFG scheduling in single sampler**
  - Use case: Replace two-pass workflows with single sampler using scheduled CFG values per step for speed optimization
  - *From: TK_999*

- **Multi-viewpoint Phantom generation**
  - Use case: Improving character fidelity by using 4 different viewpoints as separate latents
  - *From: mamad8*

- **DF endless generation**
  - Use case: Take last 17 frames of clip, extend to 97 frames, stitch together removing first 17 frames of new clip for smooth transitions
  - *From: seitanism*

- **VACE + DF combination**
  - Use case: Using VACE with DF for temporal inpainting and better video continuation
  - *From: mamad8*

- **Infinite video generation with multiple samplers**
  - Use case: Creating long seamless video sequences by chaining 4-second clips with context overlap
  - *From: seitanism*

- **iClone animation to SDXL to Wan Fun with depth**
  - Use case: Using 3D animation as base for AI video generation with depth control
  - *From: boorayjenkins*

- **Color correction for extended videos**
  - Use case: Maintaining consistent brightness across chained video segments
  - *From: MilesCorban*

- **DF extension with overlap frames**
  - Use case: Creating long videos (30 seconds to 2+ minutes) without visible seams, allows prompt traveling and different LoRAs per section
  - *From: seitanism*

- **81 frame gen with -27 frame reference for 97 frame extension**
  - Use case: Each loop generates 70 new frames (97 max - 27 overlap)
  - *From: boorayjenkins*

- **Unsample/resample degraded segments**
  - Use case: Improving quality of individual clips when degradation occurs
  - *From: Ablejones*

- **Dreambooth training with Skyreels T2V**
  - Use case: Human likeness training with simple token/class captions like 'ohwx man' - works well with just 16 images in about an hour at 1e-4
  - *From: JohnDopamine*

- **Diffusion Forcing for video extension**
  - Use case: Autoregressive model that can continue videos endlessly from any number of frames, even just 1 frame
  - *From: Kijai*

- **VACE native ComfyUI workflow**
  - Use case: Simple workflow for VACE controlnet using native nodes, adapted from wan fun workflow
  - *From: Vérole*

- **FramePacking for 4n+1 frames**
  - Use case: Getting proper frame ranges for Wan by padding image batch to X number of images by duplicating last frame
  - *From: Rishi Pandey*

- **Edit first frame then use Wan for whole video**
  - Use case: Use Step1X-Edit to modify first frame of video, then use Wan to apply changes to entire video
  - *From: mamad8*

- **First and last frame modification with FLF2V**
  - Use case: Modify both first and last frame of video using in-context technique, then use FLF2V
  - *From: mamad8*

- **Fun Control with reference image only**
  - Use case: Using Fun 1.1 control model with reference image input for VACE-like functionality
  - *From: Kijai*

- **VACE native with auto masking using segment anything**
  - Use case: Automated masking for VACE operations
  - *From: Vérole*

- **Florence2 + Groq LLM for i2v prompting**
  - Use case: Florence2 for basic image details, fed into Groq for descriptive video prompts
  - *From: David Snow*

- **Multi-stage DF workflow for long videos**
  - Use case: Takes image/video input, guides 33-frame clip, feeds last 4-17 frames back for next stage
  - *From: MilesCorban*

- **Using DG Fun models for i2v with custom nodes**
  - Use case: Start/end image workflows using native nodes
  - *From: David Snow*

- **T2V/I2V fed into DF for extension**
  - Use case: Generate short video then extend with DF, works well with LoRAs
  - *From: anever*

- **I2V + DF extension with last frame as first frame of FLF2V**
  - Use case: Looping video creation
  - *From: daking999*

- **Fantasy Talking lip sync**
  - Use case: Adding realistic lip sync to static images with audio input
  - *From: Multiple users*

- **Two-stage Fantasy Talking refinement**
  - Use case: Use Fantasy Talking as base, then run through Wan again with pose processor for better quality
  - *From: ingi // SYSTMS*

- **VACE with composited controls**
  - Use case: Combine multiple control inputs (depth, pose, outlines) by compositing images rather than using multiple nodes
  - *From: Kijai*

- **VACE multi-control setup**
  - Use case: Use two VACE nodes connected via prev_vace_embeds for multiple controls
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fantasy Talking with variable CFG**
  - Use case: Audio CFG 5, sampler CFG 5, works only in English, 81 frames max
  - *From: Stad*

- **Points editor for video masking**
  - Use case: Select mask points on single frame, then process full video
  - *From: David Snow*

- **Batch I2V generation with multiple variants per image**
  - Use case: Generate three videos per image overnight by duplicating custom sampler three times instead of using batch size
  - *From: David Snow*

- **Custom camera control using Blender paths**
  - Use case: Creating complex camera movements by designing paths in Blender and importing to Wan
  - *From: Kijai*


## Recommended Settings

- **SLG blocks**: 9 or 10
  - Other blocks performed worse in tests
  - *From: ezMan*

- **SLG range**: 0.2/0.8
  - Recommended start and end values
  - *From: ezMan*

- **CFG for SLG**: 4
  - Avoids weird rainbow prismatic color weirdness, 3 is not enough
  - *From: ezMan*

- **TeaCache threshold**: 0.2
  - Works better with 20 steps, skips 6 conditional steps vs 8 with higher threshold
  - *From: Kijai*

- **CFG for v2v enhancement**: 2
  - Used with euler/beta scheduler for second-pass improvements
  - *From: David Snow*

- **Denoise strength**: 0.8
  - For second-pass v2v to retain more detail from original
  - *From: David Snow*

- **Steps for second-pass**: 6-8
  - Low step count effective for improving old generations
  - *From: David Snow*

- **Zero_init for I2V**: not recommended
  - Zero_init not recommended for I2V according to community consensus
  - *From: ameasure*

- **VACE Encode strength**: 0.4
  - Maintains control while allowing creativity
  - *From: Cseti*

- **Base precision**: fp16 or bf16
  - Optimal performance
  - *From: zelgo_*

- **Quantization**: fp8_e4m3fn
  - Memory efficiency
  - *From: zelgo_*

- **Gray frame value for extension**: 0.5
  - Works best for empty frames in video extension
  - *From: Kijai*

- **TeaCache threshold for VACE**: 0.1
  - Standard 0.015 doesn't work well with VACE
  - *From: Kijai*

- **Steps for VACE**: 10 steps
  - Good balance of speed vs quality
  - *From: VK (5080 128gb)*

- **SLG for VACE**: Block 8, start 0.1, end 0.3-0.5
  - Prevents oversaturation issues
  - *From: IllumiReptilien*

- **DensePose strength**: 1
  - Works well at full strength
  - *From: VK (5080 128gb)*

- **Frame limit**: 81 frames
  - Model can only do up to 81 frames properly by default
  - *From: Kijai*

- **Block swap for 12GB VRAM**: 27+ for VACE workflows
  - Prevents OOM errors
  - *From: Ashtar*

- **V2V upscale steps**: 8-10 steps
  - Sufficient for upscaling and quite quick
  - *From: zelgo_*

- **SLG parameters for VACE**: SLG 8, 0.1 start, 0.3 end
  - Helps with image arrangement
  - *From: IllumiReptilien*

- **Frame limit for default Wan**: 81 frames maximum
  - Beyond 81 frames it loops
  - *From: zelgo_*

- **VACE strength**: 1.5
  - Really boosts the reference for better results
  - *From: Kijai*

- **TeaCache with VACE**: e with 0.1 threshold
  - Skips about 30% of the steps
  - *From: Kijai*

- **Model precision for 1.3B VACE**: fp32 base with VACE blocks in bf16
  - 1.3B model is in fp32 but VACE blocks are bf16, using fp16 is a bit lossy
  - *From: Kijai*

- **Frame count for VACE**: 81 frames
  - More than 81 frames adds artifacts, at 81 it's crystal clear
  - *From: seitanism*

- **Context frames and overlap**: context_frames 81 & default context_overlap 16
  - Default recommended settings
  - *From: Kijai*

- **CFG for DiffSynth models**: 1-3
  - Prevents overbaked output, light_v1 variant works best
  - *From: BondoMan*

- **SLG parameters**: 8/0.2/0.8
  - Works fine with WanLoraBlock8 set to false
  - *From: BondoMan*

- **Shift value for DiffSynth**: 11+
  - Required for proper prompt following with complex motions
  - *From: BondoMan*

- **Context size for testing**: 81 frames with 16 overlap
  - Recommended starting point for context window testing
  - *From: Kijai*

- **VACE block to swap**: 15
  - Helps manage VRAM usage on 12GB cards
  - *From: Ashtar*

- **Normal block swap**: 30
  - Additional VRAM management for larger frame counts
  - *From: Kijai*

- **TinkerWAN Alpha lora strength**: Positive values (v1.0)
  - Negative values obliterate videos with new version
  - *From: David Snow*

- **Overlap parameter**: 5 or higher
  - Even small overlap of 5 doesn't significantly affect speed, so higher overlap can be used
  - *From: A.I.Warper*

- **VACE blocks**: 1-15 (more than 0)
  - Required when using block swap to avoid errors
  - *From: Kijai*

- **Context options**: 81/16/32
  - Sweet spot settings mentioned by experienced user
  - *From: David Snow*

- **CFG for DG models**: 2.0
  - DG models are CFG distilled, lower values kill quality
  - *From: Kijai*

- **Hi-res LoRA strength**: 1.0
  - Recommended strength when using hi-res LoRA with higher resolutions
  - *From: VK (5080 128gb)*

- **DG models**: 4 steps, 1 CFG
  - Works much better at low step counts
  - *From: Hashu*

- **VACE depth control**: 0.5 strength, 0.75 end percent
  - Good balance for depth control
  - *From: Hashu*

- **Reference strength**: Can use values higher than 1.0
  - Sometimes helps with likeness
  - *From: Hashu*

- **Prev_embeds early steps**: Use lower percentages like 0.0-0.2
  - Early steps are much stronger, 50/50 split won't do much
  - *From: Kijai*

- **DG V4 High CFG**: 1.0
  - Recommended setting for DG V4 High model
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SLG blocks and strength**: 8 blocks, 0.10 to 0.30
  - User's VACE settings though results were disappointing
  - *From: PirateWolf*

- **TeaCache threshold**: 0.1-0.25
  - Lower values needed for low step counts, 0.25 works with 22 samples
  - *From: zelgo_*

- **VACE embed strength**: slightly lower than 0.925
  - Better results than default 0.925
  - *From: Kytra*

- **TeaCache threshold**: 30% skipped steps
  - Good balance of quality and speed, more than 50% usually bad quality
  - *From: Kijai*

- **VACE shift values**: Double digit values, up to 35
  - Better interpolation results for first/last frame workflows
  - *From: DawnII*

- **Control network strength**: Lower values
  - To preserve character consistency when using controls
  - *From: Draken*

- **Resolution for VACE**: 960x480x81 or less frames, 848x480 also works
  - Recommended by experienced users
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Aspect ratio for Wan**: 856x480
  - Best results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Depth map preprocessing**: Add 3 pixel blur to Blender depth maps
  - Sharp depth maps don't work with VACE
  - *From: Kijai*

- **VACE depth strength**: 0.4
  - 0.3 is too loose, 0.4 works better for depth control
  - *From: Kijai*

- **Combined control strength**: 0.5 or less on each
  - Full strength on multiple controls won't work, need to reduce strength when combining
  - *From: Kijai*

- **Image dimensions**: Divisible by 16
  - Required to avoid broadcasting errors
  - *From: traxxas25*

- **Denoise for vid2vid refinement**: Above 0.5
  - Prevents flashing and artifacts
  - *From: HeadOfOliver*

- **Vid2vid denoise range**: 0.4-0.7
  - Depends on resolution and video length
  - *From: Piblarg*

- **VACE strength**: 0.5
  - Controls both control and reference strength
  - *From: Kijai*

- **Training learning rate**: 5e-5 for dim 128, 5e-4 for dim 32
  - Optimal learning rates for different network dimensions
  - *From: Benjimon*

- **Training batch size**: 1
  - Unless using multi-GPU setup
  - *From: Benjimon*

- **HPS LoRA strength**: 0.5
  - Recommended by benchmark tests
  - *From: DawnII*

- **MPS LoRA strength**: 0.7
  - Recommended by benchmark tests
  - *From: DawnII*

- **VACE frame formula**: (4*x)+1
  - VAE encodes 4 frames to one latent except for the first
  - *From: Piblarg*

- **Maximum stable frames for I2V**: 81
  - Standard limit for stable generation
  - *From: DawnII*

- **CFG**: 1
  - Works well with VACE medium V2 and reward LoRAs
  - *From: Hashu*

- **Steps**: 10
  - Sufficient for VACE with reward LoRAs
  - *From: Hashu*

- **DiffSynth reward LoRA strength**: 0.4-0.5
  - Sweet spot, above 0.5 causes artifacts even at CFG 1
  - *From: Pedro (@LatentSpacer)*

- **14B model settings**: Steps 25, CFG 6, shift 11, denoise 0.65, LoRA 1.12
  - Good results with Ghibli LoRA
  - *From: Flipping Sigmas*

- **Tiled encoding**: Enable for 8GB VRAM or less
  - Encoding seems heavier than decoding
  - *From: Kijai*

- **VACE strength for frame extension**: Lower than default
  - Prevents stutter when using first frame as reference
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG for distilled model**: 1.0
  - Required setting when using CFG distilled LoRA
  - *From: crinklypaper*

- **LoRA strength for distilled model**: 1.0
  - Standard strength for CFG distilled LoRA
  - *From: crinklypaper*

- **Riflex default value**: 6
  - Allows for new frames to be generated after without looping
  - *From: Pedro (@LatentSpacer)*

- **Shift parameter**: 3 or 7
  - Lower values provide more motion, 5 is more stable
  - *From: Benjimon*

- **Denoise for v2v**: 0.8
  - Standard denoise level for video-to-video workflows
  - *From: Kijai*

- **Steps for second pass refinement**: 8 steps
  - Sufficient for refinement pass with enhancement LoRAs
  - *From: David Snow*

- **Empty frame level with LoRA stack**: 1.0
  - 1 = white seems to work best in testing
  - *From: The Shadow (NYC)*

- **VACE steps for quality**: 20+ steps
  - Higher steps might help with ghosting artifacts
  - *From: ArtOfficial*

- **Control lora strength**: 1.0 (not 0.55)
  - Workflow accidentally had wrong setting
  - *From: David Snow*

- **VACE grey background**: 50% grey with normal blend mode at 50%
  - For masking in VACE workflows
  - *From: IllumiReptilien*

- **Reward lora strength**: 0.5-0.7
  - Higher strengths introduce fireflies
  - *From: Kijai*

- **Shift skip for looping**: 12 for 81 frames
  - Should be half of the latents
  - *From: Kijai*

- **Loop generation**: 77 frames with slight jump
  - Current method has issues, context window method better but slower
  - *From: Jas*

- **Extra noise detail LoRA**: 0.2 recommended, max 0.35
  - Higher values just add noise without benefit
  - *From: David Snow*

- **Depth strength for 2D style**: 0.55 with end at 0.4
  - Prevents too much 3D drift in 2D styles
  - *From: StableVibrations*

- **Pose/ref combo strength**: 0.9 strength full blast
  - For maintaining character consistency
  - *From: StableVibrations*

- **New boost LoRAs**: 4-6 steps
  - More aggressive models that require fewer steps
  - *From: David Snow*

- **CFG**: 2
  - Works well with DG_Boost models
  - *From: David Snow*

- **CFG with Skip Layer Guidance**: 3
  - Reduce CFG by half when using SLG to avoid blue bar artifact
  - *From: N0NSens*

- **Skip Layer Guidance blocks**: 8 or (8,9)
  - Avoid setting blocks to 10 on 14B models to prevent blue bar
  - *From: JmySff*

- **Depth LoRA strength**: 0.05
  - Very low strength still works effectively
  - *From: David Snow*

- **DG_Boost models steps**: 5 or 6
  - Models configured for these step counts by default
  - *From: David Snow*

- **Control blending percentage**: 60%
  - 100% gave bad results, 60% worked better for combined controls
  - *From: Johnjohn7855*

- **VACE control video + reference image strength**: 0.5 to 0.6
  - Cleaner outputs compared to 1.0 which creates noise
  - *From: Johnjohn7855*

- **CFG and shift with cfg distilled lora**: cfg=1 and shift=10
  - Used with cfg distilled lora + aesthetic lora
  - *From: Johnjohn7855*

- **CFG and shift for general use**: cfg=4.5 and shift=7
  - Previous recommended settings
  - *From: Johnjohn7855*

- **Block swap for 720 model**: 20 blocks
  - Better VRAM management for hefty 720 model
  - *From: David Snow*

- **Context window size**: 81 frames
  - Model performs best at 81 frames, should be best context window size
  - *From: Kijai*

- **Steps for Fun model**: 8 steps
  - Produces remarkably good results with much faster generation
  - *From: A.I.Warper*

- **Framerate for Wan models**: 16fps
  - Fixed framerate that motion is supposed to look good at
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Control merge strength**: 0.6
  - Good balance - 1.0 is too rigid for reference image application
  - *From: Johnjohn7855*

- **RIFE interpolation for 24fps**: RIFE x3 then take every 2nd frame
  - Converts from 16fps to 24fps (16x3/2=24)
  - *From: AJO*

- **Resolution for extended frames**: 368x640 or 368x680
  - Allows 220+ frames without OOM on 4060 ti 16GB
  - *From: Pol*

- **Steps**: At least 20
  - Prevents blurry outputs
  - *From: MilesCorban*

- **TeaCache start_step**: 2 or 3
  - Better quality before TeaCache kicks in
  - *From: MilesCorban*

- **TeaCache skip percentage**: 30% of steps
  - Acceptable quality tradeoff
  - *From: Kijai*

- **Resolution for quality testing**: 960x720
  - Good balance for testing outputs
  - *From: Sway*

- **TeaCache**: 0.13 cutoff
  - Cutoff for major quality degradation
  - *From: lostintranslation*

- **LoRA strength on Fun models**: 2.0
  - Need higher strength for non-Fun LoRAs to have any effect
  - *From: Kijai*

- **CFG and shift for Wan**: Use defaults
  - Defaults work best, more critical than with other models
  - *From: Draken*

- **Shift for FLF2V**: 7 vs 16
  - Some users get better results with shift 7 instead of default 16
  - *From: seitanism*

- **Steps for FLF2V**: 24 steps vs 6
  - 24 steps much better quality but slower (6 steps: 1min, 24 steps: 3:50)
  - *From: N0NSens*

- **Denoise**: 0.38
  - Works well with distilled 1.3B model for quality/speed balance
  - *From: Flipping Sigmas*

- **CFG**: 1.5
  - Used with distilled model and multiple LoRAs
  - *From: Flipping Sigmas*

- **Steps**: 8
  - Sufficient for distilled model with LoRAs
  - *From: Flipping Sigmas*

- **Clipvision strength**: 0.3
  - Reduces static behavior in i2v generations
  - *From: DevouredBeef*

- **blocks_to_swap for 12GB VRAM**: 37-40
  - Allows generation above 480p with 81 frames on FLF2V
  - *From: DawnII*

- **CFG for FLF2V with same start/end image**: 7-10 with 1.0 motion lora
  - Needed to get motion, but higher values introduce artifacts
  - *From: Eclipse*

- **VACE shift for better reference adherence**: 20-30
  - Double digits improve style adherence, counter to base models
  - *From: DawnII*

- **gpu_memory_preservation for 4090-5090**: 3-6
  - ChatGPT suggestion for these GPU ranges
  - *From: slmonker(5090D 32GB)*

- **VACE steps with DG model and extend lora**: 8 steps
  - Allows longer generation but produces realistic results
  - *From: Rishi Pandey*

- **CFG**: Lower values
  - Reduces overcooking/artifacts and maintains better character consistency across runs
  - *From: A.I.Warper*

- **VACE steps**: 20 steps (potentially 8)
  - Provides good quality results efficiently
  - *From: A.I.Warper*

- **Frame batch size**: 33 frames
  - Provides more stability and allows finer text prompting control
  - *From: Hashu*

- **Video loader fps**: 16 fps
  - Helps with motion handling, can interpolate to higher fps later
  - *From: Flipping Sigmas*

- **Shift parameter for SkyReels 540p model**: 17
  - To get good movement
  - *From: Benjimon*

- **Depth control timestep scheduling**: 0.0 - 0.1 or 0.2 of the steps
  - To control depth frame influence while maintaining other controls
  - *From: Kijai*

- **Context window settings for long videos**: Specific context options shown in screenshot
  - For generating 1000+ frame videos without breaking
  - *From: Flipping Sigmas*

- **Extra noise detail motion LoRA strength**: 0.1-0.2 maximum
  - Higher values cause white particles
  - *From: David Snow*

- **MPS/HPS LoRA strength**: 0.3 maximum
  - Higher values change face appearance too much, diffsynth converts are 2x stronger
  - *From: gshawn*

- **Denoise for upscaling**: 0.3-0.7 range
  - 0.7 gives detail reset, 0.3 minimal change, find sweet spot
  - *From: lostintranslation*

- **FreSca scale_high**: 1.50
  - Provides small but significant quality improvement
  - *From: David Snow*

- **UniAnimate CFG**: Higher than 1.5
  - Demo uses 1.5 for weird reason, higher CFG with SLG gives better results
  - *From: Kijai*

- **Steps for Wan**: 50 steps
  - Preferred setting for quality
  - *From: Benjimon*

- **SLG block settings**: block 8, 0.10-1.00
  - For VACE processing
  - *From: David Snow*

- **UniAnimate CFG**: 1.0
  - Works properly at this setting
  - *From: Kijai*

- **VACE denoise**: 0.8
  - Very little of original remains, relies on preprocessor influence
  - *From: David Snow*

- **UniAnimate steps with teacache**: 50 steps with 22 skipped
  - Maintains quality while using teacache acceleration
  - *From: Kijai*

- **CFG**: 2.0
  - Prevents artifacts with VACE
  - *From: David Snow*

- **Steps**: 35
  - Sweet spot for generation quality
  - *From: Johnjohn7855*

- **Control embed start**: 1 instead of 0
  - Gets rid of flash at start but introduces more movement
  - *From: Gavmakes*

- **Reference threshold**: 0.3 (default)
  - For DWPose detection in UniAnimate
  - *From: wange1002*

- **FPS output**: 24fps
  - Default for SkyReels but may appear too fast
  - *From: Kijai*

- **Resolution for 1.3B**: 544x960
  - Standard resolution for the model
  - *From: Kijai*

- **Steps for DF**: 50 steps recommended
  - Better quality with Diffusion Forcing models
  - *From: Vérole*

- **CFG for DF testing**: 6
  - Good balance for testing
  - *From: Vérole*

- **prefix_samples in DF**: 17 frames commonly used
  - For 97 frame generation with 17 input frames, generates 80 new frames
  - *From: Kijai*

- **empty_frame_level in VACE**: 0.5
  - Creates grey frames (127) that model recognizes for inpainting instead of black frames
  - *From: Hashu*

- **CFG for DF**: CFG 1 not great
  - Low CFG values don't work well but content carries through generations
  - *From: DawnII*

- **Base precision**: Bf16
  - Recommended for better performance
  - *From: David Snow*

- **SLG block**: 8
  - Good choice for 1.3B model
  - *From: Kijai*

- **SLG parameters for 14B 480p**: 8, 9, 10 with CFG 3-4
  - Reduce CFG to compensate for SLG boost
  - *From: Piblarg*

- **SLG start/end percent**: 0.2, 0.8
  - Weaker but less likely to burn, safer than 0,1
  - *From: Piblarg*

- **CFG for Uni-PC sampler**: 3.5 to 4.0
  - Good range with shift around 4.0 and 50 steps
  - *From: Kytra*

- **TeaCache for 1.3B**: Use retention/e0 mode
  - Old settings work okay with alternative mode
  - *From: Kijai*

- **TeaCache mode**: e mode instead of e0
  - Uses ~600MB instead of ~4GB memory
  - *From: Kijai*

- **14B DF sampling steps**: 69 frames max on first gen
  - Memory limitations on RTX 5090
  - *From: jellybean5361*

- **LTX generation**: 97 frames at 1280x720
  - 20 second generation time
  - *From: David Snow*

- **Wan 14B generation time**: ~3-5 minutes for 832x480
  - With TeaCache and SAGE attention
  - *From: jellybean5361*

- **SkyReels V2 default resolution**: 1280x768
  - Official default resolution used in examples
  - *From: Kijai*

- **TeaCache threshold for hands preservation**: 0.13
  - Seems to not degrade hands too much while providing speed benefit
  - *From: lostintranslation*

- **CFG scheduling example**: 6,6,6,6,6,1,1,1,1,1 for 10 steps
  - Replaces two-pass workflow with single sampler using higher CFG for first half, CFG 1 for second half
  - *From: MilesCorban*

- **Denoise for second pass**: Less than 1.0
  - Denoise 1.0 creates completely new video, lower values blend new with old content
  - *From: Kijai*

- **TeaCache threshold for 14B models**: 0.25
  - 0.13 is too low and causes performance issues
  - *From: Kijai*

- **TeaCache start step with e0**: 6
  - When using e0 coefficient setting
  - *From: Kijai*

- **Block swap for 16GB VRAM**: 20
  - Prevents OOM on 81 frames, 10 blocks insufficient
  - *From: lostintranslation*

- **SLG settings for quality**: blocks: 10, start: 0.2, end: 0.8, cfg: 3.5
  - Good balance for hand quality while using TeaCache
  - *From: Kytra*

- **Minimum frame count for testing**: 33-50 frames
  - Model tuned for 81 frames, shorter clips need different settings and don't test well
  - *From: Kijai*

- **CFG for longer clips**: Higher CFG
  - With longer clips you can and should use higher CFG
  - *From: Kijai*

- **Enhance value for full frame count**: 4
  - Value of 4 on enhance is meant for full 81 frame count
  - *From: Kijai*

- **CFG for DF model**: 7
  - Higher CFG of 7 with shift of 4 produces better previews
  - *From: boorayjenkins*

- **Samplers for quality**: 40
  - Increased from 25 to 40 for better results
  - *From: boorayjenkins*

- **Frame overlap**: 27 frames
  - Bigger overlap helps maintain motion consistency in extensions
  - *From: boorayjenkins*

- **SLG guidance**: start 0.3, end 0.8
  - Better than defaults which can cause discoloration
  - *From: zelgo_*

- **TeaCache mode**: e
  - Uses only 600MB vs 4000MB with e0 mode
  - *From: Kijai*

- **Overlap frames**: 27 frames (vs default 17)
  - Better extension quality, lose 10 more frames but improves results
  - *From: boorayjenkins*

- **VRAM usage for DF 14b**: 30GB at 544x544x97 with 15 block swap
  - High VRAM requirements for diffusion forcing
  - *From: seitanism*

- **VRAM usage for 1.3b**: 8GB at 1280x768
  - More manageable requirements
  - *From: DawnII*

- **Block swapping for VRAM management**: 30 blocks for 720x720x81 frames (overkill), user reports needing all 40 blocks for 1280x720x81
  - Memory optimization for large generations
  - *From: Kijai*

- **Phantom model resolution**: Max 1280x768
  - Takes more VRAM than 1.3B usually, can be lowered
  - *From: Kijai*

- **TeaCache with DF models**: TeaCache e0 uses more memory than e
  - Memory optimization consideration
  - *From: jellybean5361*

- **TeaCache weight and start**: 0.15 weight, start at step 5
  - Works well for memory optimization
  - *From: mamad8*

- **Blockswap for 720p I2V**: 10 blockswap
  - Allows 81 frames at 480x480 on 3090 24GB VRAM
  - *From: mamad8*

- **Steps for different use cases**: 20 steps for testing, 50+ for quality
  - Balance between speed and quality
  - *From: MilesCorban*

- **noise_aug_strength**: 0.03
  - Helps with motion following in WanVideo ImageToVideo Encode
  - *From: boorayjenkins*

- **control_embed_strength**: start 0.0, end 0.5
  - Better control embed performance
  - *From: David Snow*

- **model_device**: offload_device
  - Prevents OOM issues when changing LoRA settings, main_device only for 80GB+ VRAM
  - *From: Kijai*

- **Steps for Phantom model**: 20 steps
  - Good balance of quality and speed for 14B 720p model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Resolution for Phantom**: 1024x576
  - 89 frames at this resolution with 20 steps completed in ~180 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Minimum steps for quality**: 20 steps minimum
  - Below 20 steps everything starts to change/fall apart
  - *From: MilesCorban*

- **Skyreels i2v quantization for 4090**: fp8
  - Fits almost all on VRAM with minimal system RAM offload
  - *From: MilesCorban*

- **Rope function**: comfy
  - More efficient than default and avoids dtype errors
  - *From: Kijai*

- **CFG**: 1
  - Can trade with very high shift (200) for 50% faster inference
  - *From: Pedro (@LatentSpacer)*

- **Shift**: 10-17
  - Works well for Skyreels, especially 14B model
  - *From: Colin*

- **Audio scale**: 0.5
  - Good balance for FantasyTalking with t2v
  - *From: Kijai*

- **Denoise**: 0.6-0.7
  - For refining stage in DF extension to combat degradation
  - *From: Ablejones*

- **Fantasy Talking audio CFG**: 1.0
  - Higher values can cause sync issues and quality degradation
  - *From: Multiple users*

- **Fantasy Talking FPS**: 23
  - Model is trained for 23fps output, other frame rates cause sync issues
  - *From: Kijai*

- **TeaCache start step**: 6
  - Prevents early skipping that degrades quality
  - *From: Kijai*

- **Variable audio CFG**: 5.0 for first 3 steps, then 1.0
  - Balances quality and sync accuracy
  - *From: Kijai*

- **DF different seeds**: Use different seed for each sampler
  - Prevents overburning and overexposure
  - *From: Kijai*

- **blocks_to_swap**: 20
  - Reduces VRAM usage if you have decent RAM
  - *From: ingi // SYSTMS*

- **clip_vision_precision**: FP16 or BF16
  - Reduces VRAM usage
  - *From: ingi // SYSTMS*

- **base_precision**: fp8_e4m3fn
  - Use e5 in quant for older GPU compatibility
  - *From: Jemmo*

- **addnoise_condition**: 10
  - Prevents flickering, paper suggests 20 for 14B model
  - *From: N0NSens*

- **CFG settings**: cfg3/shift5/addnoise10
  - No flickering configuration
  - *From: N0NSens*

- **camera_control_strength**: 0.2
  - Lower strength to prevent over-constraining
  - *From: Kijai*

- **fantasy_talking_fps**: 23
  - Only works at 23 frames per second
  - *From: Stad*

- **Empty frame level**: 0.5
  - Model is trained with this value (127,127,127 RGB)
  - *From: Kijai*

- **TC node start/end values in wrapper**: Use exact steps not percentages
  - Wrapper uses steps while native node uses percentages
  - *From: Kijai*


## Concepts Explained

- **SLG (Skip Layer Guidance)**: Node that works on uncond blocks at set inference range, very good at low step count
  - *From: ezMan*

- **VACE**: Video control system from Alibaba with style transfer, inpainting, subject-driven, and outpainting capabilities
  - *From: Kijai*

- **Second-pass enhancement**: Running existing video generations through another model to improve quality and motion coherence
  - *From: David Snow*

- **TeaCache modulated time embeds**: Optimization technique that doesn't work with dpmpp_sde scheduler, causes rainbow artifacts
  - *From: ezMan*

- **Context windows**: Method for processing longer video sequences by breaking them into overlapping segments
  - *From: Kijai*

- **VACE blocks**: 15 additional processing blocks that run every sampling step, causing slower performance
  - *From: Kijai*

- **Mixed precision in VACE**: VACE blocks use bf16 while rest of model uses fp32
  - *From: Kijai*

- **Context windows**: Splits long video processing into 81-frame chunks with overlap, allowing processing of longer videos without memory issues
  - *From: Kijai*

- **Reference compositing**: Multiple reference images are combined into a single image rather than processed separately
  - *From: Draken*

- **First frame injection**: VACE puts reference image as the first frame and is trained to pick up likeness from it
  - *From: Draken*

- **VACE**: All-encompassing control model for video generation, similar to ACE++ but for video. Works with reference images, masks, and various control inputs
  - *From: Kytra*

- **TeaCache**: Memory caching system that had a bug causing memory leaks, especially noticeable with VACE's larger tensors
  - *From: Kijai*

- **VACE task interpretation**: Model interprets tasks automatically rather than requiring explicit task specification like in Python API
  - *From: DawnII*

- **VACE reference vs I2V reference**: The reference image is not like you'd use with I2V model - needs specific preprocessing
  - *From: Kijai*

- **VACE masking system**: Gray areas (127 values) represent missing video parts, white areas in mask represent parts to be generated, black areas represent parts to be retained
  - *From: AJO*

- **Prompt alignment/extension**: LLM-based system that rewrites user prompts to match training caption distribution - adds details, motion attributes, and proper structure
  - *From: fearnworks*

- **VACE input frame interpretation**: Model automatically distinguishes between reference frames (colored) and control frames (preprocessed) without explicit labeling
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache memory bug**: Memory usage incorrectly scaling with steps in VACE, now fixed in latest commits
  - *From: Kijai*

- **Reference vs Start Frame in VACE**: Reference means reference object/subject (needs white background), start frame is for matching first frame of sequence
  - *From: Kijai*

- **VACE mask input**: Controls where VACE effects are applied in both spatial (image areas) and temporal (time) dimensions
  - *From: Kijai*

- **Context windows**: Method for generating long videos by processing in overlapping segments
  - *From: Kijai*

- **VACE blocks**: 15 blocks that can be selectively applied, controls which parts of the model use VACE functionality
  - *From: Kijai*

- **Context Embedder and Context Blocks**: In VACE training, DiT parameters are frozen and only Context Embedder and Context Blocks are trainable
  - *From: mamad8*

- **Block swap**: Memory optimization technique that requires VACE blocks > 0 to function properly
  - *From: Kijai*

- **DG models**: Distilled Guidance models - CFG distilled variants that work at lower CFG values
  - *From: DawnII*

- **prev_embeds**: Allows multiple VACE control inputs with different strengths and timestep ranges, like multiple ControlNets
  - *From: Kijai*

- **DG models**: Distilled Wan models for faster inference, available in light/medium/high variants
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE module separation**: VACE can be loaded separately from base model since it doesn't train base layers
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache step skipping behavior**: TeaCache skips 'useless steps' to speed up generation, but can cause issues with low step counts or certain samplers
  - *From: TimHannan*

- **SageAttention auto mode issue**: Auto mode can cause NaN (black output) with I2V, manual mode works fine
  - *From: Kijai*

- **VACE mask input vs reference masking**: Mask input is for the video, not the reference image - controls what parts of video get replaced
  - *From: traxxas25*

- **SkyreelsA2 reference padding**: Model adds padding to first frame image and uses clip embeds for multiple reference images, different approach from VACE
  - *From: Kijai*

- **VACE block swap**: VACE can be run separately and results used one by one on blocks for better memory efficiency
  - *From: Kijai*

- **TeaCache skip reporting**: TeaCache reports how many steps were actually skipped after generation, helps optimize threshold settings
  - *From: Kijai*

- **VACE temporal inpainting**: Black mask areas are kept from input, white areas are generated new. Can use any number of input frames
  - *From: Kijai*

- **Context windows**: Splits model prediction on each step, does chunks with overlap and combines them. Very slow but enables longer generations
  - *From: Kijai*

- **Prompt to reference matching**: VACE uses prompt description to map to reference image features
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE prev embeds**: Feature for chaining multiple VACE encode nodes, feeding output of one as input to another for complex control combinations
  - *From: yo9o*

- **VACE block swap**: Memory management technique that automatically enables when even 1 VACE block is swapped, moves intermediate results to RAM
  - *From: Kijai*

- **VACE strength**: Controls both the control image and reference image strength - it's the overall strength of VACE itself
  - *From: Kijai*

- **Reward Backpropagation**: Technique used to optimize generated videos for better alignment with human preferences
  - *From: Lumi*

- **Network dim in LoRA training**: Higher dim = more parameters trained. Keep low for simple/single concepts, higher for complex training
  - *From: Benjimon*

- **Temporal leakage**: When keeping 1 frame in VACE, it gets packed in a latent with 3 other frames causing some influence from adjacent frames, but this also enables smooth operation
  - *From: Kijai*

- **Inactive vs reactive frames**: VACE refers to frames as inactive (preserved) and reactive (generated) - frames marked with mask are considered part of desired output, rest is inpainted
  - *From: Kijai*

- **VACE**: Video control system with style transfer, inpainting, subject-driven, outpainting capabilities. Additional module that doesn't modify original model weights
  - *From: Kijai*

- **prev_embeds**: Input for combining multiple control types in VACE, allows blending different preprocessors
  - *From: Hashu*

- **Alpha keys in LoRAs**: Original LoRAs had alpha=64 with rank=128, DiffSynth removed alpha making them 2x stronger
  - *From: Kijai*

- **White canvas requirement**: VACE is trained to detect subjects on white canvas background, can have multiple subjects
  - *From: Kijai*

- **Empty_frame_level**: Setting in VACE that creates white, black or grey masks/frames that it will generate content in
  - *From: BondoMan*

- **RIFLEX**: Frequency index that allows for new frames to be generated after without looping, disabled when set to 0
  - *From: Pedro (@LatentSpacer)*

- **Temporal mask**: Input for controlling which parts of video are affected over time
  - *From: Dream Making*

- **VACE**: Only an extra module used with the original model, they just included the original model in the initial file they shared
  - *From: Kijai*

- **Reference image vs start image**: Reference image is different from start image - reference needs white canvas, start image is for exact first frame creation
  - *From: Kijai*

- **Temporal masking**: The mask from the start/end frame node is temporal masking, it helps preserve your stylized first frame
  - *From: DawnII*

- **DiffSynth LoRA conversion**: Removes alpha keys, effectively doubling strength - 0.5 strength equals original at 1.0
  - *From: Kijai*

- **VACE keyframes**: Black mask areas are keyframes with strong influence, white areas are generated
  - *From: Kijai*

- **Grey background masking**: Using grey color in masked areas instead of black to avoid filtering issues
  - *From: IllumiReptilien*

- **VACE model types**: Two types: basic VACE-only model (needs original WAN model too) and merged model (standalone)
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Temporal inpainting**: VACE's method of selectively preserving some frames while generating others, not limited to just start/end frames
  - *From: Kijai*

- **Latent warm up**: 1 latent = 4 frames, identified as potential cause of flashing in loops
  - *From: The Shadow (NYC)*

- **Reference image positioning**: Position matters in VACE reference images as they affect the whole generation regardless of temporal information
  - *From: Kijai*

- **Fun InP**: WAN inpainting model for temporal inpainting only, while VACE can do both temporal and spatial inpainting
  - *From: Kijai*

- **Differential Diffusion in VACE**: Built into WanVideo encode node via mask input, blends masked areas but can affect style consistency
  - *From: David Snow*

- **Reference image padding**: Reference images automatically add 4 latent frames in VACE, now handled automatically
  - *From: Kijai*

- **OptimalSteps**: Custom sigmas implementation similar to 'align your steps' but with different values for potentially faster generation
  - *From: Kijai*

- **VACE flexibility**: Can use control only, or control + source video. Control frames generated from source video but source video itself doesn't need to be used in diffusion
  - *From: David Snow*

- **Context window overlap calculation**: Context frames + overlap determines total frames rendered. 81 context + 24 overlap + 81 frames = 169 total for example
  - *From: Kijai*

- **Reference images vs start frames in context**: Start frames won't be part of windows that aren't first, but reference images work because added to each context manually and aren't positional
  - *From: Kijai*

- **ExVideo LoRA**: LoRA that doubles video length from 81 to 161 frames and can also act as detail enhancement
  - *From: David Snow*

- **Context windows**: Feature for longer generations but can cause style shifting - disable for style preservation
  - *From: David Snow*

- **SageAttention dtype selection**: Different precision modes (auto, fp16_cuda) for different GPUs - auto works for most, fp16_cuda needed for 4090 with I2V
  - *From: Kijai*

- **SLG (Skip Layer Guidance)**: Same as SkipLayerGuidanceDiT node for skipping diffusion layers
  - *From: Colin*

- **BF16 to FP16 conversion**: Lossy conversion that can't recover missing precision data, results in worse quality than either format
  - *From: Kijai*

- **FPS conditioning**: Model conditioning based on frame rate - Wan doesn't seem to have this feature
  - *From: Kijai*

- **pos_embed in FLF2V**: New positional embedding that affects how clip image embeds are applied, seems to make first frame influence stay longer
  - *From: Kijai*

- **Block swap**: Memory management technique that can improve generation speed by 60% on both 41 and 81 frame generations
  - *From: lostintranslation*

- **SLG/cfg zero star**: Technique that works with FLF2V model, though optimal prompting strategy still unclear
  - *From: Kijai*

- **DiT patchify for temporal coherence**: Technique where recent frames get more patches than distant frames - 3rd frame normal patches, 2nd fewer patches, 1st least patches. Not possible with UNet architecture
  - *From: Fannovel16*

- **Inverted sampling in FramePack**: Model generates from end to beginning, so ending actions appear before starting actions during generation
  - *From: JohnDopamine*

- **FramePack architecture**: Uses HunyuanVideoTransformer3DModelPacked class name, different from standard HYV architecture
  - *From: JohnDopamine*

- **Temporal masking in VACE**: Black mask frames are keyframes that don't change, white mask frames are inpainted temporally. Allows mixing keyframes with generated content
  - *From: Kijai*

- **First frame vs reference in VACE**: First frame as encoded latent maintains better coherence than sending stylized frame as reference
  - *From: DawnII*

- **FramePack resolution limitation**: Gradio demo fixed at 600x600 resolution which impacts quality, not a fault of Gradio but intentional limitation
  - *From: BNP4535353*

- **Multiple VAE passes degradation**: Every time an image is decoded and then re-encoded through a VAE, it loses quality - this compounds with each additional pass
  - *From: DawnII*

- **DF in model name**: Likely stands for Diffusion-Forcing, a training technique, though exact meaning unclear
  - *From: Screeb*

- **Diffusion Forcing (DF)**: A different category of model entirely, like 1 frame T2V that is fed as a reference
  - *From: deleted_user_2ca1923442ba*

- **VACE**: A controlnet module that allows T2V models to use images, enables controls or reference passing
  - *From: Kijai*

- **TeaCache mode**: Detection method used to differentiate between 480p and 720p models that are identical in keys
  - *From: Kijai*

- **Image embeds in Fun LoRAs**: Special keys that normal 1.3B model lacks, causing incomplete LoRA loading
  - *From: Kijai*

- **VAE tiling**: Memory optimization technique for video decoding to prevent OOM errors
  - *From: David Snow*

- **VACE blocks**: Numbers that represent which blocks VACE is applied to, affects processing quality
  - *From: David Snow*

- **DMD vs CFG distillation**: DMD is step distilled (reduces step count from 50 to 5), CFG distilled is different and doesn't work well with low steps
  - *From: yi*

- **UniAnimate architecture**: 1GB LoRA weights and pose embeds that work as control model for normal 14B I2V
  - *From: Kijai*

- **LoRA compatibility**: LoRAs = change weights decomposed to two matrices A and B. Can add change weights to original model always - software issue rather than math issue when not possible
  - *From: deleted_user_2ca1923442ba*

- **Block swap bottleneck**: When using block swap, those become more of a bottleneck and you won't feel attention speed up as much
  - *From: Kijai*

- **Diffusion Forcing**: Method for generating infinite-length videos, supports both T2V and I2V with synchronous and asynchronous inference modes
  - *From: Colin*

- **Diffusion Forcing (DF)**: New architecture requiring whole new sampling process, allows asynchronous usage
  - *From: Kijai*

- **Penultimate hidden states**: Second-to-last layer outputs from clip vision, fixes compatibility issues
  - *From: Kijai*

- **Block swap**: Memory management technique needed for larger models on limited VRAM
  - *From: Juampab12*

- **Diffusion Forcing (DF)**: Method that can continue from any number of frames, works like T2V with input latents where prefix_samples overwrite noise
  - *From: Kijai*

- **fps_embeds**: FPS embedding layers only available in 1.3B DF model, missing from 14B version
  - *From: Kijai*

- **addnoise_condition**: Hyperparameter in DF that adds noise and improves new frame generation
  - *From: Kijai*

- **SLG**: Like a big boost to CFG but works better than just raising CFG, provides more detail and motion without artifacts
  - *From: Kijai*

- **Block swap**: More blocks swapped = higher VRAM savings, trial and error system specific setting
  - *From: David Snow*

- **VACE**: More like ControlNet, was released bundled with normal 1.3B model
  - *From: Kijai*

- **Diffusion Forcing**: Uses different scheduling, creates new scheduler for each latent with per-token denoising
  - *From: Kijai*

- **TeaCache threshold**: Works like step count consideration - too high skips too many steps with quality hit
  - *From: Kijai*

- **VACE**: Almost like a single controlnet that can do multiple functions (ref, mask, control) but everything is bundled together
  - *From: Draken*

- **DF (Diffusion Forcing)**: Sampling method that requires massive VRAM due to time step embedding size
  - *From: Kijai*

- **TeaCache**: Caching system that clones timeembed, uses 4GB for cache in standard mode, 600MB in 'e' mode
  - *From: Kijai*

- **SkyReels structured prompting**: JSON schema with subjects, shot_type, camera_motion, environment, lighting fields for better video generation
  - *From: fredbliss*

- **Dynamics-only prompting**: SkyReels V2 methodology where I2V prompts only describe temporal changes (action/expression/camera motion) while the input image provides static visual context
  - *From: fredbliss*

- **Model parameters (14b vs 1.3b)**: Refers to number of parameters in models - 14 billion vs 1.3 billion, basically the brain cells. 14b gives better quality but takes more time and memory to run.
  - *From: Zuko*

- **Denoise ratio**: The ratio of new vs old content in diffusion sampling. 1.0 means completely new, lower values blend new generation with existing content.
  - *From: Kijai*

- **TeaCache**: Speed optimization technique that can skip diffusion steps, but may degrade quality especially for hands at higher threshold settings
  - *From: Kijai*

- **FLF2V**: First-Last-Frame to Video, only allows start and end frame input
  - *From: Kijai*

- **DF model**: Endless generation model that extends videos by using previous frames as input for new generations
  - *From: seitanism*

- **fp8_e4m3fn vs e5m2**: Different precision formats - GPUs prior to 4000 series don't work with e4m3fn and need e5m2, e4m3 has less precision than e4m8
  - *From: Kijai*

- **Block swap**: Manual VRAM management in wrapper vs automatic offloading in native implementation
  - *From: Kijai*

- **Phantom model**: Uses images as suggestion rather than straight i2v, not like ipadapter, good for subject reference
  - *From: TK_999*

- **Diffusion Forcing (DF)**: New technique/architecture used in Skyreels V2 models
  - *From: seitanism*

- **VACE ending**: Ability to end VACE conditioning at specific point (like 0.5) when combining with other techniques
  - *From: Kijai*

- **TeaCache modes**: Different memory usage modes - 'e' uses 600MB, 'e0' uses 4000MB for time embeddings
  - *From: Kijai*

- **Diffusion Forcing (DF)**: Technique for extending videos by using overlap frames from previous generation to guide next generation seamlessly
  - *From: seitanism*

- **Overlap frames**: Frames from end of previous video used as reference for next generation - default 17, can use 27 for better quality
  - *From: boorayjenkins*

- **Diffusion Forcing (DF)**: Autoregressive video model that can continue videos endlessly with proper motion continuation, works by extending from any number of input frames
  - *From: Kijai*

- **4n+1 frame rule**: WAN models require frame counts following pattern of 4x+1 (like 65, 69, 81) because each unit the model generates is 4 frames plus 1 start frame
  - *From: jellybean5361*

- **Token/class captions**: Dreambooth style training using simple 2-word captions like 'ohwx man' or 'joesmith person' instead of full descriptions
  - *From: JohnDopamine*

- **fp8_fast quality degradation**: Previously fp8_fast cast inputs to different precision (fp8_e5m2) when weights were fp8_e4m3fn, causing quality loss. Now same dtype works without degradation
  - *From: Kijai*

- **TeaCache step activation**: TeaCache activates at step 6, which is the 15% point when using default settings
  - *From: Cubey*

- **fp8_e4m3fn_fast_no_ffn**: Skips the FFN layers which cause quality degradation, but is then not much faster than regular fp8_fast
  - *From: Kijai*

- **addnoise_condition**: Parameter that supposedly improves consistency, though user noted minimal difference between settings
  - *From: seitanism*

- **Control embeds**: Better term for ControlNet when used with these models
  - *From: David Snow*

- **TeaCache**: Optimization technique that skips certain steps during generation - shown skipping steps 7, 9, 11, 13, 15 for conditional, unconditional, and prediction_2 passes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap**: Technique for memory management, but current implementations may not work properly or run blocks on CPU
  - *From: Kijai*

- **Flow shift**: Controls amount of change/movement throughout video - low shift = less change/movement, high shift = more change/movement
  - *From: Ro*

- **Hidream**: Feature that generates very similar images at different seeds, can be used with prompts like 'close-up' to generate same picture with different angle/zoom for start/end frames
  - *From: N0NSens*

- **Image cross attention**: Image conditioning or 'image prompting' - how models use image input for conditioning
  - *From: Kijai*

- **DF (Diffusion Forcing)**: Model that can continue from any amount of frames, even just one, but doesn't use image cross attention
  - *From: Kijai*

- **DG models**: Distilled models with LOW versions for many steps, HIGH versions for few steps
  - *From: JmySff*

- **Audio conditioning**: Additional cross attention mechanism in FantasyTalking for audio-to-video sync
  - *From: Kijai*

- **Audio CFG**: Classifier-free guidance specifically for audio conditioning in Fantasy Talking model
  - *From: Kijai*

- **Swap memory**: Using SSD space as additional RAM when system RAM is insufficient for large models
  - *From: Stad*

- **Control LoRA input channel modification**: Control LoRAs modify model input channels making them incompatible with other techniques like VACE
  - *From: Kijai*

- **Composited control inputs**: Combining multiple control types by overlaying control images rather than using separate control nodes
  - *From: Kijai*

- **VACE**: Video control system that works as modules alongside base models, like controlnet for video
  - *From: Kijai*

- **Fun Control reference vs start frame**: Reference image doesn't need to match control closely, more flexible than start frame
  - *From: Kijai*

- **Camera control dataset**: Uses Google's RealEstate10K dataset for 3D camera movement training
  - *From: Kijai*

- **Empty frame level**: Controls what to replace blank frames with - 0 is black, 1 is white, 0.5 is mid gray (127,127,127 RGB)
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fun ref image latent with empty embed**: Method to use reference images without causing flash/blink artifacts at video start
  - *From: Gavmakes*


## Resources & Links

- **VACE-Wan2.1-1.3B-Preview** (model)
  - https://huggingface.co/ali-vilab/VACE-Wan2.1-1.3B-Preview/tree/main
  - *From: Kijai*

- **DiffSynth-Studio-Lora-Wan2.1-ComfyUI** (lora)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: DawnII*

- **VACE GitHub Repository** (repo)
  - https://github.com/ali-vilab/VACE
  - *From: DawnII*

- **Wan2.1 end frame workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_480p_I2V_endframe_example_01.json
  - *From: Faux*

- **Video Depth Anything** (tool)
  - https://videodepthanything.github.io/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Recognize Anything Model (RAM)** (tool)
  - https://github.com/xinyu1205/recognize-anything
  - *From: TK_999*

- **MuseTalk 1.5** (repo)
  - https://github.com/TMElyralab/MuseTalk
  - *From: burgstall*

- **Wan prompt extend system prompts** (repo)
  - https://github.com/Wan-Video/Wan2.1/blob/main/wan/utils/prompt_extend.py
  - *From: Kagi*

- **VACE GitHub repository** (repo)
  - https://github.com/ali-vilab/VACE
  - *From: zelgo_*

- **VACE project page with examples** (documentation)
  - https://ali-vilab.github.io/VACE-Page/
  - *From: makeitrad*

- **Arcane Jinx LoRA for VACE testing** (model)
  - https://huggingface.co/Cseti/Wan-LoRA-Arcane-v1/blob/main/664463-csetiarcane-Nfj1nx-e15-e7-s5070-ipv.safetensors
  - *From: Cseti*

- **VACE annotators** (model)
  - https://huggingface.co/ali-vilab/VACE-Annotators/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE-Wan2.1-1.3B-Preview model** (model)
  - https://huggingface.co/ali-vilab/VACE-Wan2.1-1.3B-Preview/tree/main
  - *From: VK*

- **VACE workflow tutorial video** (tutorial)
  - https://youtu.be/r3mDwPROC1k?si=aCo9BWShbL4uBPYJ
  - *From: Impactframes.*

- **VACE official page** (documentation)
  - https://ali-vilab.github.io/VACE-Page/
  - *From: Siraj*

- **ComfyUI-enricos-nodes** (repo)
  - https://github.com/erosDiffusion/ComfyUI-enricos-nodes
  - *From: slmonker(5090D 32GB)*

- **TinkerWan stability LoRA** (lora)
  - https://civitai.com/models/1425406/tinkerwan-wan-13b-stability-and-quality-enhancement-lora?modelVersionId=1611139
  - *From: Juampab12*

- **DiffSynth-Studio LoRA** (lora)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: IllumiReptilien*

- **Wan2.1 14B T2V LoRAs collection** (lora collection)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-t2v-loras-67dc73d82f66cfac2b4eb253
  - *From: ⚡*

- **Wan2.1 14B I2V LoRAs collection** (lora collection)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b
  - *From: ⚡*

- **Alvdansen LoRAs** (lora collection)
  - https://civitai.com/user/alvdansen
  - *From: Mint*

- **VACE model weights** (model)
  - https://huggingface.co/ali-vilab/VACE-Wan2.1-1.3B-Preview/tree/main
  - *From: Kytra*

- **VACE workflow examples** (workflow)
  - https://github.com/if-ai/ComfyUI-IF_VideoPrompts/tree/main/WF
  - *From: Impactframes.*

- **WanFunControlToVideo node update** (node)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1354606222833353005
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Mediapipe face preprocessor** (tool)
  - https://github.com/kijai/ComfyUI-FollowYourEmojiWrapper
  - *From: Kijai*

- **VACE Annotators** (model)
  - https://huggingface.co/ali-vilab/VACE-Annotators
  - *From: DawnII*

- **VACE UserGuide** (documentation)
  - https://github.com/ali-vilab/VACE/blob/main/UserGuide.md#32-single-tasks
  - *From: AJO*

- **Hi-Res LoRA for Wan2.1** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: VK (5080 128gb)*

- **SkyReels A2 model** (model)
  - https://huggingface.co/Skywork/SkyReels-A2
  - *From: Juampab12*

- **Sapiens models** (model)
  - https://huggingface.co/facebook/sapiens-pose-1b-torchscript
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SkyReels-A2 code** (repo)
  - https://github.com/SkyworkAI/SkyReels-A2
  - *From: Kijai*

- **DiffSynth Wan models** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: BondoMan*

- **Wan prompt extension code** (repo)
  - https://github.com/Wan-Video/Wan2.1/blob/679ccc6c68eee39ac9af0618dff904bf2c708283/wan/utils/prompt_extend.py
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TinkerWAN Alpha lora v1.0** (lora)
  - https://civitai.com/models/1425406?modelVersionId=1614659
  - *From: David Snow*

- **Sapiens ComfyUI nodes** (nodes)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: ArtOfficial*

- **DreamyVibes model** (model)
  - https://huggingface.co/CCP6/dreamyvibes/tree/main
  - *From: JohnDopamine*

- **Multiple control stacking example** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1357385562256048369
  - *From: ameasure*

- **Standalone VACE model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VACE_1_3B_preview_bf16.safetensors
  - *From: Kijai*

- **DG model collection** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: Kijai*

- **SkyReels A2 model** (model)
  - https://huggingface.co/Skywork/SkyReels-A2
  - *From: s2k*

- **VACE official code** (repo)
  - https://github.com/ali-vilab/VACE
  - *From: yo9o*

- **ComfyUI TexturePacker** (tool)
  - https://github.com/kijai/ComfyUI-TexturePacker
  - *From: Kijai*

- **Enricos compositor nodes** (tool)
  - https://github.com/erosDiffusion/ComfyUI-enricos-nodes/tree/master
  - *From: IllumiReptilien*

- **Triton for Windows** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: David Snow*

- **PyTorch 2.8 installation guide** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1jdfs6e/automatic_installation_of_pytorch_28_nightly/
  - *From: DeZoomer*

- **Video Depth Anything ComfyUI node** (node)
  - https://github.com/yuvraj108c/ComfyUI-Video-Depth-Anything
  - *From: David Snow*

- **VACE module** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VACE_1_3B_preview_bf16.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DG distilled models** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: JmySff*

- **TAEW preview file** (tool)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: Zuko*

- **Wan 1.3B LoRA search** (search)
  - https://huggingface.co/models?other=base_model:adapter:Wan-AI/Wan2.1-T2V-1.3B
  - *From: seruva19*

- **SOTS Art Wan LoRA** (model)
  - https://huggingface.co/AlekseyCalvin/SOTS_Art_Wan1.3B_LoRA_rank256_bySilverAgePoets
  - *From: David Snow*

- **MMAudio safetensors** (model)
  - https://huggingface.co/Kijai/MMAudio_safetensors/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **AudioX model** (model)
  - https://huggingface.co/HKUSTAudio/AudioX
  - *From: YatharthSharma*

- **ComfyUI-BS-Textchop** (node)
  - https://github.com/Burgstall-labs/ComfyUI-BS-Textchop
  - *From: burgstall*

- **Civitai Green (SFW version)** (model repository)
  - https://civitai.green/search/models?sortBy=models_v9&query=wan%20lora
  - *From: AJO*

- **3D character rig resource** (tool)
  - https://toyxyz.gumroad.com/l/ciojz
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SkyreelsA2 fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_SkyreelsA2_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **VACE native ComfyUI discussion** (discussion)
  - https://ptb.discord.com/channels/1076117621407223829/1342763350815277067/1356778493983330525
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SkyreelsA2 example workflow** (workflow)
  - Included with node update
  - *From: Kijai*

- **A2-Bench dataset** (dataset)
  - https://huggingface.co/datasets/Skywork/A2-Bench
  - *From: fredbliss*

- **Triton for Windows** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Lumi*

- **RTX 5090 Triton setup guide** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1jle4re/how_to_run_a_rtx_5090_50xx_with_triton_and_sage/
  - *From: ChronoKnight*

- **MatAnyone ComfyUI implementation** (repo)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra
  - *From: JohnDopamine*

- **Frutiger Lora 14B** (lora)
  - https://huggingface.co/dreamer8/FrutigerLora14B_Wan
  - *From: Dream Making*

- **Complete list of Civitai WAN loras** (resource)
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Motion segmentation research** (research)
  - https://motion-seg.github.io/
  - *From: yo9o*

- **Higgsfield AI using WAN loras** (service)
  - https://higgsfield.ai
  - *From: Draken*

- **Ghibli LoRA for 1.3B** (lora)
  - *From: Piblarg*

- **Ghibli LoRA for 14B** (lora)
  - https://civitai.com/models/1404755/studio-ghibli-style-wan21-t2v-14b
  - *From: Piblarg*

- **Reward LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs
  - *From: Lumi*

- **RTX 5090 ComfyUI setup guide** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1jk2tcm/step_by_step_from_fresh_windows_11_install_how_to/
  - *From: Piblarg*

- **Musubi trainer frontend** (tool)
  - https://github.com/maybleMyers/H1111
  - *From: Benjimon*

- **Upscale workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1358558275733553345
  - *From: HeadOfOliver*

- **Converted Reward LoRAs for ComfyUI** (model)
  - https://huggingface.co/Kijai/Wan2.1-Fun-Reward-LoRAs-comfy/tree/main
  - *From: Kijai*

- **Fun Control 1.3B model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-Control
  - *From: DawnII*

- **ComfyUI repackaged text encoders** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/text_encoders
  - *From: Kijai*

- **Higres and Aesthetics LoRAs** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: David Snow*

- **WanTraining control LoRA trainer** (tool)
  - https://github.com/spacepxl/WanTraining
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE feedback and issues** (repo)
  - https://github.com/ali-vilab/VACE/issues/27
  - *From: Kijai*

- **Audio reactive spline example** (workflow)
  - https://youtu.be/_ioElEFP8TY
  - *From: Kijai*

- **MatAnyone ComfyUI node** (node)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra
  - *From: JohnDopamine*

- **MatAnyone main repo** (repo)
  - https://github.com/pq-yang/MatAnyone
  - *From: JohnDopamine*

- **DiffSynth reward LoRAs** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: Flipping Sigmas*

- **VACE preview model** (model)
  - https://huggingface.co/ali-vilab/VACE-Wan2.1-1.3B-Preview/tree/main
  - *From: xwsswww*

- **Video batch loading node** (node)
  - https://github.com/alt-key-project/comfyui-dream-video-batches
  - *From: Mikkle*

- **VACE GitHub issue about inpainting** (repo)
  - https://github.com/ali-vilab/VACE/issues/30
  - *From: Kijai*

- **Wan ecosystem summary document** (workflow)
  - *From: Adrien Toupet*

- **Native ComfyUI T2V workflow** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/text_to_video_wan.json
  - *From: MilesCorban*

- **WanWeightedControlToVideo node** (tool)
  - https://github.com/wordbrew/comfyui-wan-control-nodes
  - *From: CJ*

- **Face swap with VACE example** (workflow)
  - https://www.reddit.com/r/comfyui/comments/1jugop6/a_more_rigorous_vace_faceswap_vaceswap_example/?sort=new
  - *From: xwsswww*

- **FL_gemini nodes for prompt generation** (tool)
  - http://github.com/filliptm/ComfyUI_Fill-Nodes
  - *From: Flipping Sigmas*

- **Loop Sequential Integer node for testing** (tool)
  - https://github.com/justUmen/Bjornulf_custom_nodes?tab=readme-ov-file#56----loop-sequential-integer
  - *From: AJO*

- **Perfect loop LoRA** (model)
  - https://civitai.com/models/1264662?modelVersionId=1528511
  - *From: The Shadow (NYC)*

- **ExVideo LoRA** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: David Snow*

- **Depth LoRA** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/depth
  - *From: David Snow*

- **Speed Control LoRA** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/blob/main/Wan2.1-1.3b-lora-speedcontrol-v1_new.safetensors
  - *From: Johnjohn7855*

- **ReCamMaster-Wan2.1** (model)
  - https://huggingface.co/KwaiVGI/ReCamMaster-Wan2.1
  - *From: DawnII*

- **AutoCrop Faces ComfyUI node** (tool)
  - https://github.com/liusida/ComfyUI-AutoCropFaces
  - *From: xwsswww*

- **DG_Wan variants** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: David Snow*

- **ReCamMaster model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_kwai_recammaster_1_3B_step20000_bf16.safetensors
  - *From: Kijai*

- **ReCamMaster branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/recammaster
  - *From: Kijai*

- **14B CFG distilled model** (model)
  - https://huggingface.co/mktn/Wan2.1-14B-cfgdistill_test/tree/main
  - *From: CJ*

- **Pusa V0.5 model** (model)
  - https://huggingface.co/RaphaelLiu/Pusa-V0.5
  - *From: const username = undefined;*

- **AutoCropFaces node** (node)
  - https://github.com/liusida/ComfyUI-AutoCropFaces
  - *From: MilesCorban*

- **Yolo Cropper node** (node)
  - https://github.com/tooldigital/ComfyUI-Yolo-Cropper
  - *From: MilesCorban*

- **Extra noise detail LoRA** (lora)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/blob/main/dg_wan2_1_v1_3b_lora_extra_noise_detail_motion.safetensors
  - *From: David Snow*

- **Kijai WanVideo models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: harryB*

- **LatentPop style LoRA for Flux** (lora)
  - https://huggingface.co/jakedahn/flux-latentpop
  - *From: David Snow*

- **Multiple new boost LoRAs** (lora)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/commit/3fec64897d603a9a0a4c1f656a818079ceec095b
  - *From: DawnII*

- **SkyReels-A2 model** (model)
  - https://github.com/SkyworkAI/SkyReels-A2
  - *From: AI_Fan*

- **Flat color LoRA** (lora)
  - https://civitai.com/models/1132089?modelVersionId=1525407
  - *From: David Snow*

- **DG_Boost Evol V3 model** (model)
  - *From: David Snow*

- **OptimalSteps implementation** (tool)
  - https://github.com/bebebe666/OptimalSteps
  - *From: crinklypaper*

- **Co-tracker for mask tracking** (tool)
  - https://github.com/facebookresearch/co-tracker
  - *From: mamad8*

- **ComfyUI-BETA-Helpernodes with crop and stitch nodes** (node)
  - https://github.com/Burgstall-labs/ComfyUI-BETA-Helpernodes
  - *From: burgstall*

- **MatAnyone Kytra custom nodes** (node)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra
  - *From: Kytra*

- **Sameface fix Flux LoRA** (lora)
  - https://civitai.com/models/766608/sameface-fix-flux-lora
  - *From: David Snow*

- **DG_Model_Wan2_1_v1_3b_t2v_Boost_Final** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Model_Wan2_1_v1_3b_t2v_Boost_Final
  - *From: David Snow*

- **Pusa-VidGen with Wan2.1 roadmap** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen
  - *From: yi*

- **ComfyUI-GGUF** (repo)
  - https://github.com/city96/ComfyUI-GGUF
  - *From: MilesCorban*

- **Wan2.1-T2V-14B-gguf models** (model)
  - https://huggingface.co/city96/Wan2.1-T2V-14B-gguf
  - *From: MilesCorban*

- **ComfyUI face parsing** (repo)
  - https://github.com/Ryuukeisyou/comfyui_face_parsing
  - *From: Johnjohn7855*

- **ComfyUI-RMBG** (repo)
  - https://github.com/1038lab/ComfyUI-RMBG
  - *From: Johnjohn7855*

- **Eyes detection ADetailer** (model)
  - https://civitai.com/models/150925/eyes-detection-adetailer
  - *From: xwsswww*

- **ComfyUI-AIR-Nodes** (repo)
  - https://github.com/jonnydolake/ComfyUI-AIR-Nodes
  - *From: A.I.Warper*

- **ComfyUI-Inpaint-CropAndStitch** (repo)
  - https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch
  - *From: David Snow*

- **ExVideo LoRA** (lora)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: David Snow*

- **SynCamMaster-Wan2.1** (model)
  - https://huggingface.co/KwaiVGI/SynCamMaster-Wan2.1
  - *From: yi*

- **SynCamMaster main repo** (repo)
  - https://github.com/KwaiVGI/SynCamMaster
  - *From: JohnDopamine*

- **Animated Logo LoRA** (lora)
  - https://civitai.com/models/1468212?modelVersionId=1660567
  - *From: Alisson Pereira*

- **Fun 14B FP16 conversion** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Benjimon*

- **Lotus Depth models** (model)
  - https://huggingface.co/Kijai/lotus-comfyui/tree/main
  - *From: David Snow*

- **Wan 2.1 Knowledge Base** (knowledge base)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: Nathan Shipley*

- **Ghibli Wan 1.3B LoRA** (model)
  - https://civitai.com/models/1474964/ghibli-wan-13b?modelVersionId=1668351
  - *From: Piblarg*

- **Seamless Loop Workflow** (workflow)
  - https://civitai.com/models/1426572/wan-21-seamless-loop-test-workflow
  - *From: gshawn*

- **CausVid** (repo)
  - https://github.com/tianweiy/CausVid?tab=readme-ov-file
  - *From: Cubey*

- **Eyes In Camera LoRA** (model)
  - https://drive.google.com/file/d/18Po5RJR_3x1jaUDK4_nksK41QtVNV3be/view?usp=sharing
  - *From: NebSH*

- **Wan2.1-FLF2V-14B-720P** (model)
  - https://huggingface.co/ypyp/Wan2.1-FLF2V-14B-720P
  - *From: DawnII*

- **NormalCrafter** (tool)
  - https://huggingface.co/spaces/Yanrui95/NormalCrafter
  - *From: DawnII*

- **Kijai fp8 version of FLF2V** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-FLF2V-14B-720P_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **FLF2V inference code** (repo)
  - https://github.com/yupeng1111/Wan2.1/tree/first_last_frame_transformation
  - *From: DawnII*

- **TheDirector workflow** (workflow)
  - https://civitai.com/models/1476469?modelVersionId=1670194
  - *From: AJO*

- **FramePack I2V HY weights** (model)
  - https://huggingface.co/lllyasviel/FramePackI2V_HY/tree/main
  - *From: JulienDoku*

- **FramePack repository** (repo)
  - https://github.com/lllyasviel/FramePack
  - *From: JohnDopamine*

- **CausVid alternative approach** (repo)
  - https://github.com/tianweiy/CausVid
  - *From: yi*

- **Wan FLF2V 14B official** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P
  - *From: DawnII*

- **VACE user experience improvement thread** (repo)
  - https://github.com/ali-vilab/VACE/issues/27
  - *From: JohnDopamine*

- **WanVideo FLF2V fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-FLF2V-14B-720P_fp8_e4m3fn.safetensors
  - *From: DawnII*

- **FramePackWrapper ComfyUI node** (repo)
  - https://github.com/kijai/ComfyUI-FramePackWrapper
  - *From: zelgo_*

- **WanVideo FLF2V example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_FLF2V_720P_example_01.json
  - *From: mamad8*

- **HunyuanVideo repackaged model** (model)
  - https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files
  - *From: Kijai*

- **UniAnimate-DiT** (repo)
  - https://github.com/ali-vilab/UniAnimate-DiT
  - *From: yo9o*

- **Discord chat analysis with NotebookLM** (tool)
  - https://youtu.be/kG81Kkal5XM
  - *From: Nathan Shipley*

- **Chat data files for NotebookLM** (tool)
  - https://www.dropbox.com/scl/fo/r4t10eeok40qqapnhnzc3/ALncPlceSgiPB3ZKTILazg4?rlkey=62o9du85uk9fumd1hmc33rj7g&dl=0
  - *From: Nathan Shipley*

- **Fal.ai coupon for $20 credit** (tool)
  - https://fal.ai/dashboard?coupon=YEAROFVIDEO
  - *From: NebSH*

- **SkyReels V2 I2V 14B 540P** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-14B-540P
  - *From: yi*

- **SkyReels V2 T2V 14B 720P** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-T2V-14B-720P
  - *From: yi*

- **UniAnimate-DiT repository** (repo)
  - https://github.com/ali-vilab/UniAnimate-DiT
  - *From: amli*

- **Wan2.1-FLF2V-14B-720P GGUFs** (model)
  - https://huggingface.co/city96/Wan2.1-FLF2V-14B-720P-gguf
  - *From: gshawn*

- **FramePack Gradio demo** (repo)
  - https://github.com/lllyasviel/FramePack
  - *From: Benjimon*

- **ComfyUI-WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: DawnII*

- **Wan developer Twitter AMA** (resource)
  - https://x.com/StevenZhang66/with_replies
  - *From: JohnDopamine*

- **SkyReels V2 fp8 conversion** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-SkyReels-V2-I2V-14B-540P_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **UniAnimate-DiT** (repo)
  - https://github.com/ali-vilab/UniAnimate-DiT
  - *From: Kijai*

- **ComfyUI-FollowYourEmojiWrapper** (repo)
  - https://github.com/kijai/ComfyUI-FollowYourEmojiWrapper
  - *From: Kijai*

- **UniAnimate LoRA weights** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/UniAnimate-Wan2.1-14B-Lora-12000-fp16.safetensors
  - *From: Kijai*

- **SkyReels V2 I2V 540p model backup** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Benjimon*

- **FLUX Redux style shaping workflow** (workflow)
  - https://gist.github.com/nathanshipley/7a9ac1901adde76feebe58d558026f68
  - *From: Nathan Shipley*

- **FLUX Redux HuggingFace Space** (tool)
  - https://huggingface.co/spaces/multimodalart/flux-style-shaping
  - *From: Nathan Shipley*

- **Extra noise detail motion LoRA** (lora)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/blob/main/dg_wan2_1_v1_3b_lora_extra_noise_detail_motion.safetensors
  - *From: David Snow*

- **Fun Reward LoRAs** (lora)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs/tree/main
  - *From: David Snow*

- **DepthAnythingV2 models** (model)
  - https://huggingface.co/Kijai/DepthAnythingV2-safetensors/tree/main
  - *From: lostintranslation*

- **ComfyUI-DepthAnythingV2 node** (node)
  - https://github.com/kijai/ComfyUI-DepthAnythingV2
  - *From: David Snow*

- **FreSca implementation** (repo)
  - https://github.com/WikiChao/FreSca
  - *From: Kijai*

- **Benjimon's Wan files** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Benjimon*

- **DepthAnything V2** (repo)
  - https://github.com/kijai/ComfyUI-DepthAnythingV2
  - *From: David Snow*

- **SeedVR upscaler** (tool)
  - https://iceclear.github.io/projects/seedvr/
  - *From: JohnDopamine*

- **STAR upscaler (CogvideoX based)** (repo)
  - https://github.com/NJU-PCALab/STAR
  - *From: JohnDopamine*

- **CFG distilled Wan model** (model)
  - https://huggingface.co/mktn/Wan2.1-14B-cfgdistill_test/tree/main
  - *From: DawnII*

- **ComfyUI-Sapiens** (repo)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: Kijai*

- **UniAnimate-W for ComfyUI** (repo)
  - https://github.com/Isi-dev/ComfyUI-UniAnimate-W
  - *From: N0NSens*

- **Perturbed attention guidance** (repo)
  - https://github.com/pamparamm/sd-perturbed-attention
  - *From: deleted_user_2ca1923442ba*

- **Characteristic guidance** (repo)
  - https://github.com/redhottensors/ComfyUI-Prediction
  - *From: deleted_user_2ca1923442ba*

- **SkyReels V2 models** (model)
  - https://huggingface.co/collections/Skywork/skyreels-v2-6801b1b93df627d441d0d0d9
  - *From: yi*

- **SkyReels V2 code** (repo)
  - https://github.com/SkyworkAI/SkyReels-V2
  - *From: yi*

- **BiRefNet background removal** (tool)
  - https://github.com/lldacing/ComfyUI_BiRefNet_ll
  - *From: David Snow*

- **Inspyrenet-Rembg** (tool)
  - https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg
  - *From: David Snow*

- **MTB nodes** (tool)
  - https://github.com/melMass/comfy_mtb
  - *From: David Snow*

- **SkyCaptioner V1** (model)
  - https://huggingface.co/Skywork/SkyCaptioner-V1
  - *From: Persoon*

- **SkyReels V2 I2V 1.3B** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P/blob/main/model.safetensors
  - *From: Kijai*

- **SkyReels collection** (model collection)
  - https://huggingface.co/collections/Skywork/skyreels-v2-6801b1b93df627d441d0d0d9
  - *From: Seb*

- **Weight comparison script** (tool)
  - https://github.com/maybleMyers/H1111/blob/main/compare_safetensors_weights.py
  - *From: Benjimon*

- **TorchInfo for model analysis** (tool)
  - https://github.com/TylerYep/torchinfo
  - *From: Kytra*

- **SkyReels 14B fp16** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Benjimon*

- **Groq ComfyUI node** (node)
  - https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node
  - *From: Colin*

- **SkyReels models on HuggingFace** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Skyreels
  - *From: Kijai*

- **MAGI-1 repository** (repo)
  - https://github.com/SandAI-org/MAGI-1
  - *From: Kijai*

- **WanVideoWrapper DF testing commit** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/commit/65f5505fca115c23f3eb60689a2cf793d11b90df
  - *From: Kijai*

- **Chipmunk embedding caching** (tool)
  - https://github.com/sandyresearch/chipmunk
  - *From: yi*

- **Kijai GitHub sponsorship** (repo)
  - https://github.com/kijai
  - *From: Zuko*

- **DG models for ComfyUI** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: N0NSens*

- **In-Context LoRA** (repo)
  - https://github.com/ali-vilab/In-Context-LoRA
  - *From: N0NSens*

- **CropAndStitch nodes** (tool)
  - https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch
  - *From: David Snow*

- **BETA Helper nodes** (tool)
  - https://github.com/Burgstall-labs/ComfyUI-BETA-Helpernodes
  - *From: David Snow*

- **SkyReels DF example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_skyreels_diffusion_forcing_extension_example_01.json
  - *From: aiacsp*

- **MAGI-1 model** (model)
  - https://huggingface.co/sand-ai/MAGI-1
  - *From: ˗ˏˋ⚡ˎˊ-*

- **I2V simple workflow** (workflow)
  - https://civitai.com/models/1309369/img-to-video-simple-workflow-wan21-or-gguf-or-lora-or-upscale-or-teacache
  - *From: lostintranslation*

- **MediaPipe for FollowYourEmoji** (tool)
  - https://github.com/kijai/ComfyUI-FollowYourEmojiWrapper
  - *From: Kijai*

- **Phantom-Wan models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Phantom-Wan-1_3B_fp16.safetensors
  - *From: Kijai*

- **File Converter tool** (tool)
  - https://github.com/Tichau/FileConverter/releases
  - *From: David Snow*

- **Phantom research** (repo)
  - https://github.com/Phantom-video/Phantom
  - *From: DawnII*

- **SkyReels V2 model** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P/tree/main
  - *From: CDS*

- **Quantization research paper** (research)
  - https://arxiv.org/html/2503.06564v1
  - *From: deleted_user_2ca1923442ba*

- **SkyCaptioner V1 model** (model)
  - https://huggingface.co/Skywork/SkyCaptioner-V1
  - *From: fredbliss*

- **A2-Bench dataset** (dataset)
  - https://huggingface.co/datasets/Skywork/A2-Bench/blob/main/sample_v1.json
  - *From: fredbliss*

- **Phantom model** (model)
  - https://huggingface.co/bytedance-research/Phantom
  - *From: JohnDopamine*

- **TAEW2_1 VAE file** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: David Snow*

- **SkyReels V2 repository** (repo)
  - https://github.com/SkyworkAI/SkyReels-V2/tree/main/skycaptioner_v1
  - *From: fredbliss*

- **ComfyUI QwenVL PR for SkyCaptioner** (tool)
  - https://github.com/alexcong/ComfyUI_QwenVL/pull/18
  - *From: TK_999*

- **WanVideo A2 example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_skyreels_a2_example_01.json
  - *From: Zuko*

- **VACE project page** (documentation)
  - https://ali-vilab.github.io/VACE-Page/
  - *From: Zuko*

- **SkyReelV2-i2v-540p** (model)
  - *From: mamad8*

- **Resize To Closest node** (node)
  - *From: jellybean5361*

- **WanVideoWrapper DF sampler** (node)
  - *From: seitanism*

- **PyTorch nightly** (tool)
  - *From: lostintranslation*

- **Wan2_1-SkyReels-V2-DF-14B-540P_fp8_e4m3fn.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Skyreels/Wan2_1-SkyReels-V2-DF-14B-540P_fp8_e4m3fn.safetensors
  - *From: seitanism*

- **Phantom model** (model)
  - https://huggingface.co/bytedance-research/Phantom
  - *From: NebSH*

- **Wan2_1-SkyReels-V2-DF-1_3B-540P_fp32.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Skyreels/Wan2_1-SkyReels-V2-DF-1_3B-540P_fp32.safetensors
  - *From: Jemmo*

- **RealisDance-DiT** (research)
  - https://thefoxofsky.github.io/project_pages/RealisDance-DiT/index
  - *From: yi*

- **ComfyUI-FreeMemory** (tool)
  - *From: Mngbg*

- **SkyReels V2 Project** (repo)
  - https://github.com/SkyworkAI/SkyReels-V2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai SkyReels Models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Skyreels
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Example DF workflow on Kijai's git** (workflow)
  - *From: boorayjenkins*

- **Diffusion Pipe SkyReels support** (repo)
  - https://github.com/tdrussell/diffusion-pipe/commit/ed947867f363b7fa39596561ed2054b919cff2f6
  - *From: JohnDopamine*

- **Skyreels V2 720p models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Skyreels
  - *From: ezMan*

- **RealisDance-DiT** (model)
  - https://thefoxofsky.github.io/project_pages/RealisDance-DiT/index
  - *From: yi*

- **Uni3C** (model)
  - https://ewrfcas.github.io/Uni3C/
  - *From: yi*

- **WAN VACE native workflow** (workflow)
  - https://civitai.com/articles/13951/wan-video-vace-native-comfyui
  - *From: Vérole*

- **WinDirStat storage management** (tool)
  - *From: mamad8*

- **ComfyUI-FramePacking** (tool)
  - https://github.com/rishipandey125/ComfyUI-FramePacking
  - *From: Rishi Pandey*

- **Wan2.1-Fun-V1.1-1.3B-Control-Camera** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-1.3B-Control-Camera
  - *From: DawnII*

- **Sparge attention model for wan2.1** (model)
  - https://huggingface.co/Xiang-cd/sparge-attention-model-zoo/tree/main/want2v-1.3B
  - *From: yi*

- **SpargeAttn repository** (repo)
  - https://github.com/thu-ml/SpargeAttn
  - *From: yi*

- **Fun 1.1 14B Control model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-1.3B-Control/blob/main/diffusion_pytorch_model.safetensors
  - *From: Kijai*

- **Quantized 14B model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Fun-V1_1-14B-Control_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **VideoX-Fun update commit** (repo)
  - https://github.com/aigc-apps/VideoX-Fun/commit/fa953a04e95edbd357d43128bec0eb03cf9372f8
  - *From: DawnII*

- **Sparge attention model** (model)
  - https://huggingface.co/Xiang-cd/sparge-attention-model-zoo/tree/main/want2v-1.3B
  - *From: yi*

- **Step1X-Edit model** (repo)
  - https://github.com/stepfun-ai/Step1X-Edit
  - *From: mamad8*

- **Wan 2.1 Knowledge Base** (tool)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f?pvs=74
  - *From: Nathan Shipley*

- **NotebookLM chat scraping demo** (tool)
  - https://www.youtube.com/watch?v=kG81Kkal5XM&feature=youtu.be
  - *From: Nathan Shipley*

- **ComfyUIMini** (tool)
  - https://github.com/ImDarkTom/ComfyUIMini
  - *From: boorayjenkins*

- **Comfy Portal iOS app** (tool)
  - https://apps.apple.com/us/app/comfy-portal/id6741044736
  - *From: boorayjenkins*

- **WAN VACE native workflow** (workflow)
  - https://civitai.com/models/1508309/wan-vace-native-workflow
  - *From: Vérole*

- **Civitai SFW version** (tool)
  - https://civitai.green/
  - *From: yi*

- **Phantom 1.3B model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Phantom-Wan-1_3B_fp32.safetensors
  - *From: VRGameDevGirl84(RTX 5090)*

- **SkyReels V2 DF model** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-DF-1.3B-540P
  - *From: Nokai*

- **SkyReels V2 I2V model** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P
  - *From: Nokai*

- **ComfyUI-wanBlockswap** (node)
  - https://github.com/orssorbit/ComfyUI-wanBlockswap
  - *From: Draken*

- **ViewComfy** (tool)
  - https://github.com/ViewComfy/ViewComfy
  - *From: A.I.Warper*

- **DiffSynth Studio LoRA** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: N0NSens*

- **DG Wan Fun models** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Wan2_1_V1.3b_Fun_Inp
  - *From: David Snow*

- **DG Custom Nodes** (tool)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Wan2_1_V1.3b_Fun_Inp/DG_Custom_Node_For_Wan2_1_I2V_Double_Prompts
  - *From: David Snow*

- **Skyreels V2 I2V** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-14B-720P
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FantasyTalking** (repo)
  - https://github.com/Fantasy-AMAP/fantasy-talking
  - *From: Bingo*

- **CausVid model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-CausVid
  - *From: mkt*

- **TransPixeler Wan support** (repo)
  - https://github.com/wileewang/TransPixeler/tree/wan
  - *From: JohnDopamine*

- **Throwaway 1.3 LoRAs** (model)
  - https://huggingface.co/CCP6/throwaway-1.3-lora-for-kicks/tree/main
  - *From: JohnDopamine*

- **Latentpop Flux LoRA** (model)
  - https://huggingface.co/jakedahn/flux-latentpop
  - *From: David Snow*

- **DG Wan2.1 Fun_Inp models** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Wan2_1_V1.3b_Fun_Inp
  - *From: David Snow*

- **Wan2.1 Fun collection** (model)
  - https://huggingface.co/collections/alibaba-pai/wan21-fun-v11-680f514c89fe7b4df9d44f17
  - *From: 片ヨ亡亡丹片*

- **Tile control LoRA** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/blob/main/1.3b/tile/wan2.1-1.3b-control-lora-tile-v1.0_comfy.safetensors
  - *From: Kijai*

- **Wan 2.1 base model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_t2v_1.3B_fp16.safetensors
  - *From: Kijai*

- **SkyReels 1.3B I2V** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P
  - *From: Colin*

- **Fun Camera Control 14B** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-14B-Control-Camera
  - *From: Zuko*

- **Google RealEstate10K dataset** (dataset)
  - https://google.github.io/realestate10k/download.html
  - *From: Kijai*

- **Blender camera control addon** (tool)
  - https://toyxyz.gumroad.com/l/ciojz
  - *From: toyxyz*

- **ComfyUI segment anything 2 video example** (workflow)
  - https://github.com/kijai/ComfyUI-segment-anything-2/blob/main/example_workflows/points_segment_video_example.json
  - *From: ˗ˏˋ⚡ˎˊ-*

- **AudioX repository** (repo)
  - https://github.com/ZeyueT/AudioX
  - *From: Jemmo*

- **RTX 5090 setup guide** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1jle4re/how_to_run_a_rtx_5090_50xx_with_triton_and_sage/
  - *From: Baku*

- **BIRME image resizer** (tool)
  - https://www.birme.net/?target_width=1024&target_height=1024
  - *From: JohnDopamine*


## Known Limitations

- **Fun inpaint model terrible at T2V**
  - Produces grey outputs and poor results when used for text-to-video generation
  - *From: Kijai*

- **Control model issues with out-of-frame objects**
  - When character gets up from sofa, reveals gaping hole where they sat - unfun I2V was more consistent
  - *From: miko*

- **Enhanced-a-video too slow with native**
  - Too big of a speed hit with native workflow, wrapper doesn't support fp8 scaled
  - *From: Doctor Shotgun*

- **Finger generation still poor**
  - Even with improved 1.3B setup at 8 steps, still can't do fingers properly
  - *From: David Snow*

- **VACE only works with video input currently**
  - Reference image functionality not yet implemented, only input frames work as control signal
  - *From: Kijai*

- **Inpaint model changes unmasked areas**
  - When using fun inpaint model, unmasked areas also change during inpainting process
  - *From: wayward_18*

- **Video Depth Anything OOM issues**
  - Need to reduce input size to avoid out of memory, can OOM quickly with longer sequences
  - *From: David Snow*

- **VACE is significantly slower than standard models**
  - Approximately 2x slower due to 15 additional blocks running every step
  - *From: multiple users*

- **High VRAM consumption**
  - 832x480x45 frames takes 19GB VRAM, can use up to 31GB
  - *From: Kijai*

- **Reference image likeness inconsistent**
  - Doesn't always maintain close likeness without proper preprocessing
  - *From: Ro*

- **LoRA compatibility issues**
  - LoRAs work but not as well as with standard Wan models
  - *From: Kytra*

- **Block swapping ineffective**
  - Won't help much with VRAM usage and can cause errors
  - *From: Kijai*

- **VACE much heavier than base 1.3B model**
  - Surprisingly heavy despite being based on 1.3B, requires block swap on 4090 to avoid OOM
  - *From: ingi // SYSTMS*

- **Model limited to 81 frames by default**
  - Can be forced to do more with control but doesn't work properly
  - *From: Kijai*

- **Reference images don't work with context windows**
  - Ref image isn't passed for context windows processing
  - *From: Kijai*

- **Poor quality with reference + control video combination**
  - May work better using either reference OR control, not both
  - *From: seitanism*

- **Start/end frame feature is flawed with I2V model**
  - Hacky way to force it, never worked perfectly as model not trained for it
  - *From: Kijai*

- **VACE reference image flexibility**
  - Extremely locked into reference image angle and position, not very flexible for pose changes
  - *From: AJO*

- **fp8_fast model compatibility**
  - fp8_fast models not supported on cards with compute capability < 9.0 (RTX 3060 and lower)
  - *From: Faux*

- **Control reduces coherence**
  - Anytime you give control input, you lose some coherence in the output
  - *From: Piblarg*

- **VACE mask input unclear**
  - Purpose of mask input in VACE not well understood, works better without it
  - *From: Kijai*

- **VACE doesn't work with Fun models**
  - Not compatible with Fun Control system
  - *From: Kijai*

- **VACE has issues with full reference images**
  - Model doesn't work well with full reference like that, needs separated subjects or background removed
  - *From: Kijai*

- **Frame count limitation**
  - More than 81 frames adds artifacts, works best at 81 frames
  - *From: seitanism*

- **Limited character consistency scenarios**
  - Can't use reference image like PuLID for face override at any angle
  - *From: AJO*

- **Sapiens normals single resolution support**
  - Only supports single input resolution, doesn't work well in landscape orientations
  - *From: Kijai*

- **SkyReels-A2 lacks control features**
  - No control capabilities compared to VACE, making it less useful for creative workflows
  - *From: Kijai*

- **DG_Wan models poor LoRA compatibility**
  - Don't respond to LoRAs as well as base models, affecting V2V quality
  - *From: David Snow*

- **VACE is memory intensive**
  - Requires significant VRAM, 12GB cards struggle with 81 frames even with block swapping
  - *From: Ashtar*

- **Blurred masks don't work well with VACE**
  - Blurred mask inputs appear to not be functioning properly
  - *From: Zuko*

- **No spline control for varying control strength over time**
  - Cannot reduce control strength over time while keeping reference at full strength
  - *From: Hashu*

- **Mediapipe face detection inconsistent**
  - Fails to detect obvious faces in about half of frames
  - *From: David Snow*

- **Model generates different animation initially**
  - First few seconds show different animation in preview before matching prompt and introducing reference
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Bounding box control randomness in T2V**
  - Often doesn't create anything in bounding box on first frame with T2V, more useful with I2V
  - *From: Kijai*

- **VACE blocks memory usage**
  - Blocks themselves are tiny, but huge input size uses lots of memory
  - *From: Kijai*

- **TexturePacker canvas size limitation**
  - Limited to 512 squares for canvas, meant for texture packing (e.g., 1024x512)
  - *From: Kijai*

- **No frame-range LoRA application**
  - Cannot apply LoRA effects to specific frame ranges only
  - *From: Kijai*

- **ComfyUI animation system**
  - Lacks proper animation system and keyframe settings options
  - *From: David Snow*

- **VACE inpainting barely preserves likeness in reference image**
  - Using pose or no input_frames preserves likeness fine, but inpainting struggles
  - *From: Zuko*

- **5 steps is very poor quality in base Wan**
  - Need higher step counts for decent results with base model
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Can't use reference on one VACE and not another when chaining**
  - Using reference adds latent, so all chained VACE nodes need reference (can use blank grey)
  - *From: Kijai*

- **Text gets distorted in Wan**
  - Never successfully preserved text shape
  - *From: David Snow*

- **High motion is problematic**
  - Vid2vid works great for static shots but struggles with movement-heavy content
  - *From: 3Dmindscaper2000*

- **VACE doesn't play well with overlayed controlnets**
  - Causes artifacts like pose dots bleeding through in output
  - *From: traxxas25*

- **TeaCache incompatible with ancestral/SDE samplers**
  - Samplers that do substeps and add noise don't work with TeaCache
  - *From: Kijai*

- **TeaCache pointless with low step counts**
  - Causes mosaic/noisy outputs when used with few steps
  - *From: Kijai*

- **Start/end images don't work with context options**
  - Some windows won't have start/end frames in context mode
  - *From: Kijai*

- **SageAttention auto mode causes black output with I2V**
  - Suspected issue with cross attention in fp8 models
  - *From: Kijai*

- **LoRAs may not work perfectly with SkyreelsA2**
  - Base model weights are changed so existing LoRAs won't be perfect
  - *From: Kijai*

- **14B VACE will be very heavy to run**
  - Even on 4090 will likely be unusable due to double compute requirement
  - *From: Draken*

- **Fun models lack basic concepts**
  - Missing things like 'red panda' from training, much worse than base 1.3B
  - *From: Kijai*

- **Control networks destroy character consistency**
  - Adding any control network inevitably breaks consistency in faces and clothing
  - *From: wange1002*

- **VACE human subjects get generalized**
  - Tend to look similar within categories (asian woman, blonde woman, etc.)
  - *From: ArtOfficial*

- **Can't search Discord by file attachment extension**
  - User frustrated about search limitations
  - *From: fredbliss*

- **SkyReels v2 can't do video-to-video**
  - No way to input video frames for v2v
  - *From: JmySff*

- **VACE doesn't understand normal maps well**
  - Requires desaturating or other processing to work
  - *From: Kijai*

- **Context windows show transitions in backgrounds**
  - Uncontrolled background areas change between windows
  - *From: JmySff*

- **Native ComfyUI Wan can't use more than 1 clip embed for SkyReels**
  - Fails to keep images besides the first one
  - *From: Kijai*

- **VACE only works with 1.3B models**
  - Cannot use VACE module with 14B models currently
  - *From: Kijai*

- **VACE struggles with blurred masks**
  - Faded/blurred masks leave artifacts on edges, solid masks work better
  - *From: A.I.Warper*

- **Combined controls require reduced strength**
  - Using multiple control inputs at full strength doesn't work, need to reduce to 0.5 or less
  - *From: Kijai*

- **14B models not compatible with preprocessors**
  - Cannot use tiled diffusion or similar preprocessing with 14B variants
  - *From: David Snow*

- **1.3B quality issues**
  - 1.3B can look awful without proper LoRAs, especially for stylized content
  - *From: froyo*

- **Complex pose handling**
  - Model struggles with characters doing weird/complex poses like Roger Rabbit
  - *From: David Snow*

- **Reward LoRAs compatibility**
  - Reward LoRAs likely don't work with regular models, only with Fun variants
  - *From: Lumi*

- **VACE 8GB VRAM limit**
  - VACE runs out of memory on 8GB RTX 2080 for 640x360x10 frames without optimizations
  - *From: xwsswww*

- **Reference images don't work with DG models**
  - Reference image functionality is not available when using distilled guidance models
  - *From: JmySff*

- **Fun Control lacks VACE flexibility**
  - Fun Control can't do overlapping controls like VACE, and no way to set inpaint mask strength in native nodes
  - *From: JmySff*

- **14B model extremely slow on 8GB**
  - 14B model takes 3 hours for 17 frames on laptop 4070, making it impractical
  - *From: froyo*

- **Tiled VACE encoding very slow**
  - Tiled encoding works but is incredibly slow compared to normal encoding
  - *From: Kijai*

- **Fun 1.3B quality is poor**
  - Much worse than VACE 1.3B in general quality
  - *From: Kijai*

- **VACE has inference time overhead**
  - Overhead on inference time compared to base models
  - *From: Kijai*

- **Multiple Fun Control models multiply inference time**
  - Would mean running 2nd full model alongside, multiplying inference time
  - *From: Kijai*

- **Fun Control chaining doesn't work**
  - Only last control node in chain applies, others are ignored
  - *From: Kijai*

- **Reward LoRAs reduce motion**
  - LoRAs for quality improvement tend to kill movement/motion
  - *From: Jas*

- **VACE reference and inpainting are all part of same context**
  - Makes it difficult to use multiple VACE encodes effectively as they interfere with each other
  - *From: Kijai*

- **Text prompt does nearly nothing at full VACE strength**
  - When using control + reference frames, text prompts have minimal influence
  - *From: Draken*

- **Gemini API outputs images one at a time**
  - Even when requesting multiple images, they come back individually without context to each other
  - *From: Fill*

- **Character likeness drift on longer videos**
  - 81 frame videos show likeness drift, especially noticeable between reference/first frames and later generated frames
  - *From: Pedro (@LatentSpacer)*

- **Slow motion tendency in outputs**
  - 90% of outputs have slow motion with very little character movement
  - *From: Jas*

- **Wan doesn't work well over 81 frames**
  - Performance and quality issues beyond 81 frames
  - *From: Draken*

- **1.3B struggles with small details**
  - Small things like hands and distant eyes turn into blobs, close-up faces have decent eyes but far shots they become blobs
  - *From: Draken*

- **VACE tends to drift from start image**
  - Vace tends to drift from the start image after a few frames, which is why many use additional reference frames
  - *From: David Snow*

- **Native ComfyUI lacks VACE support**
  - Native ComfyUI doesn't have VACE support yet, would take effort to implement properly
  - *From: Kijai*

- **Fun-Control model quality**
  - Prone to heinous render artifacts, glitches and artifacts galore
  - *From: David Snow*

- **Control lora strength at high denoise**
  - Control lora not strong enough to deal with 1.0 denoise setting
  - *From: David Snow*

- **Reward loras introduce fireflies**
  - Consistently introduce fireflies, need to disable when using Fun-Control
  - *From: David Snow*

- **LoRA incompatibility with Fun models**
  - LoRAs made with standard models don't work well on Fun models, VACE won't work with Fun models
  - *From: Kijai*

- **ReCamMaster struggles against video motion**
  - Works better when camera motion aligns with existing video motion
  - *From: Kijai*

- **Camera paths only work for max 81 frames**
  - Camera control paths have a limitation of 81 frames maximum
  - *From: Kijai*

- **VACE doesn't like masks with holes**
  - Input masks with holes in them cause issues with VACE
  - *From: IllumiReptilien*

- **Style drift over frames**
  - Tendency to move away from input image style and shift from 2D to 3D over 10+ frames
  - *From: David Snow*

- **Camera movement limitations**
  - 360 degree camera movements don't work, even 180 degrees may not work - turns back after 90 degrees
  - *From: Kijai*

- **Reference image burn-in**
  - First couple frames can have reference image burned into them when using VACE
  - *From: A.I.Warper*

- **Base weights may not work with VACE**
  - Camera embeds definitely don't work with other weights
  - *From: Kijai*

- **2-step generation quality too low**
  - While LoRA effects work best at 2 steps, quality is insufficient for practical use
  - *From: David Snow*

- **Multiple VACE encodes cause issues**
  - Using multiple VACE encodes for different controls can cause tensor mismatch errors and raging inferno results
  - *From: David Snow*

- **VACE not good with certain art styles**
  - VACE struggles with stylized content like flat color/cartoon styles
  - *From: Kijai*

- **Recam requires existing video**
  - Cannot use Recam with single image input - needs video generation first or duplicate single image
  - *From: David Snow*

- **TeaCache conflicts with context windows**
  - TeaCache doesn't work well with context windows, causes issues
  - *From: Kijai*

- **OptimalSteps only works well with 14B models**
  - For 1.3B models, OptimalSteps gives worse results each time
  - *From: Kijai*

- **OptimalStepsSchedule is situational and not useful**
  - Way too situational to be useful, doesn't work with unipc sampler
  - *From: Kijai*

- **1.3B model struggles with complex prompts**
  - 1.3B kinda struggles with prompts anyway, not suitable for complex descriptions
  - *From: Kijai*

- **14B LoRAs not compatible with 1.3B models**
  - LoRAs trained for 14B models won't work with 1.3B models
  - *From: David Snow*

- **WAN has heavy bias towards certain face types**
  - Very heavy bias towards certain type of face, nearly identical to default 'flux face'
  - *From: David Snow*

- **WAN doesn't do much camera motion**
  - Model limitation for camera movement effects
  - *From: Johnjohn7855*

- **VACE doesn't work with native ComfyUI nodes currently**
  - Need Kijai's wrapper, not compatible with regular ComfyUI nodes at this time
  - *From: Kijai*

- **Car motion direction issues**
  - Models frequently get car direction wrong, sending them backwards, sideways, or making them transform
  - *From: David Snow*

- **VACE doesn't work well with reference images for V2V**
  - VACE model doesn't respect reference image input for video-to-video tasks
  - *From: Pol*

- **Lotus depth causes video flickering**
  - While good for images, lotus depth creates flickering artifacts in video generation
  - *From: David Snow*

- **BF16 to FP16 conversion loses quality**
  - Converting from BF16 to FP16 results in loss of both range and precision
  - *From: Kijai*

- **1.3B and 14B LoRAs not compatible**
  - LoRAs trained for different model sizes are completely incompatible
  - *From: Kijai*

- **Fun Control doesn't support end images**
  - Both Fun Control models break when using end image, only VACE supports start/end images
  - *From: DawnII*

- **Color matching isn't perfect for loops**
  - Still has issues with color shifting despite color matching attempts
  - *From: Cubey*

- **Wan fixed at 16fps**
  - No fps conditioning available, requires interpolation for other frame rates
  - *From: Kijai*

- **RTX 8000 very slow for inference**
  - 2.5-3 hours for generations that take 1 hour on 4090
  - *From: Benjimon*

- **FLF2V does 'middle step' transitions often**
  - Often creates intermediate steps between start and end frames rather than direct transitions
  - *From: Kijai*

- **720p model may be inferior to 480p**
  - Observations suggest 720p model not as good as 480p, possibly due to training on less data
  - *From: MilesCorban*

- **VACE doesn't understand plan changes in video unlike Fun**
  - VACE has trouble with dynamic changes compared to Fun model
  - *From: N0NSens*

- **SynCamMaster subject positioning is broken**
  - Places subjects at exact same position regardless of prompt, though background angles work correctly
  - *From: Kijai*

- **Orbit camera can't handle over 90 degrees**
  - Model struggles with camera rotations greater than 90 degrees
  - *From: Kijai*

- **FramePack limited prompt complexity**
  - Works well for simple prompts like dancing, but not complex scenarios like 1-minute Tom & Jerry episodes
  - *From: JohnDopamine*

- **Motion still context-windowy in FramePack**
  - Despite generating longer videos, motion characteristics still resemble HYV's context window limitations
  - *From: Cubey*

- **Early gens more brave, later stuff stiffens**
  - In FramePack generation, earlier chunks show more dynamic motion while later parts become more static
  - *From: Cubey*

- **Quality degradation in consecutive i2v generations**
  - Running multiple different images through i2v in queue causes permanent quality degradation until cache cleared
  - *From: lostintranslation*

- **FLF2V requires precise prompting**
  - Model seems to need very specific prompt formulation to work well
  - *From: Kijai*

- **FramePack has texture smoothing issues**
  - Demo videos show weird smoothing on textures, gives pause about texture quality
  - *From: Kytra*

- **Eye movement is particularly hard across all models**
  - Capturing eye movement is challenging for VACE, Fun, and vanilla 1.3B
  - *From: David Snow*

- **VACE memory requirements limit long sequences**
  - Extra 15 blocks for VACE make longer sequences difficult due to VRAM constraints
  - *From: A.I.Warper*

- **Fun Control too rigid for illustrative content**
  - Controlnet adherence too strong for artistic/illustrative use cases
  - *From: Rishi Pandey*

- **FramePack generates fixed backgrounds**
  - Backgrounds don't move and appear static, making videos look unnatural
  - *From: wange1002*

- **Fast motion handling issues**
  - VACE struggles with fast motion, step count doesn't help much
  - *From: N0NSens*

- **Quality degradation on longer generations**
  - Longer video generations show increasing quality degradation
  - *From: N0NSens*

- **VACE adds unwanted warm colorization**
  - Model consistently adds warm tones that may not match intended output
  - *From: xwsswww*

- **Models rarely trained on people smiling**
  - AI video models seem to have limited training on smiling subjects
  - *From: A.I.Warper*

- **WAN can't simply generate more frames with weights alone**
  - Needs new inference code and scheduler for longer generation
  - *From: Kijai*

- **VACE struggles with extreme eye movements**
  - Cannot pick up rapid eye crossing movements that Fun-control can handle
  - *From: David Snow*

- **SD1.5 era pose preprocessors are really bad**
  - Poor quality compared to newer methods like mediapipe
  - *From: David Snow*

- **Characters won't shut up with certain LoRAs**
  - Mouths constantly in motion unless heavily constrained
  - *From: David Snow*

- **UniAnimate won't work with 8GB cards**
  - Memory requirements too high for 8GB VRAM
  - *From: xwsswww*

- **1.3B model poor skin rendering**
  - Human skin always seems to degrade, becomes airbrushed looking
  - *From: David Snow*

- **Fast motion handling**
  - Model doesn't handle fast motion well in general, especially hands
  - *From: David Snow*

- **VACE style consistency with new surfaces**
  - Restyling breaks when new unseen surfaces appear in rolling objects
  - *From: sneako1234*

- **Reference images cause artifacts in VACE**
  - Causes flashes at start and glitches throughout video with no known workaround
  - *From: David Snow*

- **CFG distilled models don't work with low steps**
  - Produces total garbage even at 8 steps, needs different sampler or approach
  - *From: Kijai*

- **UniAnimate doesn't do face pose**
  - Doesn't support OpenPose face detection, only body pose
  - *From: Kijai*

- **Sapiens has single resolution limitation**
  - Annoying limitation that restricts flexibility
  - *From: Kijai*

- **1.3B model has distortion issues**
  - Temporal attention problems causing weird distortions, doesn't happen with 14B I2V
  - *From: PirateWolf*

- **Wan models limited to 720p and 480p resolutions**
  - Native resolution limitations
  - *From: N0NSens*

- **UniAnimate doesn't accept face input**
  - Cannot be used for lip sync applications
  - *From: PolygenNoa*

- **DWPose detection failures**
  - Not perfect and sometimes can't detect pose, will fail on some videos
  - *From: Kijai*

- **VACE draws unwanted nipples on smooth surfaces**
  - Cannot be negative prompted out, sees breast shapes and draws nipples
  - *From: David Snow*

- **UniAnimate won't work with VACE currently**
  - May be possible when 14B VACE comes out
  - *From: Kijai*

- **SkyReels struggles with abstract content**
  - Human-centric model has trouble with non-human subjects
  - *From: Kijai*

- **Color consistency issues**
  - Struggles to keep colors on some input images
  - *From: Kijai*

- **Diffusion Forcing not fully implemented**
  - Requires new sampling process, not yet supported in wrapper
  - *From: Kijai*

- **Control LoRAs don't work with VACE on same step**
  - Control LoRA changes input channels, VACE only handles 16 channels
  - *From: Kijai*

- **Wan LoRAs limited compatibility**
  - 1.3B style LoRAs work somewhat but not well, 14B motion LoRAs don't work with 1.3B
  - *From: Jas*

- **Limited style LoRAs for 1.3B model**
  - Less than five good style loras available, most are 'basically just tits and weird kink shit'
  - *From: David Snow*

- **1.3B DF quality degradation in long generations**
  - 1.3B model starts to lose quality in extended generations, works better with videos it generates itself
  - *From: Kijai*

- **Reference images cause artifacts in VACE**
  - Using reference images tends to cause flash at start of animation and glitches
  - *From: David Snow*

- **VACE currently only works with 1.3B variants**
  - VACE is only an addon module for 1.3B wan variants, not compatible with 14B models yet
  - *From: DawnII*

- **OptimalSteps scheduler limitations**
  - Only works for 14B T2V and won't work with lots of other optimizations
  - *From: Kijai*

- **Native VACE can only use one embed**
  - Unlike wrapper which can use multiple VACE embeds, native implementation limited to single embed
  - *From: Kijai*

- **DG models don't handle I2V well**
  - Very fast at 6 steps but not good for image-to-video tasks
  - *From: N0NSens*

- **Pose matching requirement for UniAnimate with DF**
  - Pose has to match the init frame, works somewhat with 14B DF model
  - *From: Kijai*

- **Prompt following issues when extending**
  - Sometimes ignores prompt, sometimes 'jumps' during video extension
  - *From: Kijai*

- **Swimming noise on fine textures**
  - Wan has issues with fine details like rocks, may be due to lack of training material
  - *From: andrewrasmussen.*

- **VACE only works with 1.3B T2V model**
  - Cannot use VACE with I2V models currently
  - *From: Draken*

- **Cannot merge VACE with I2V models**
  - Shape mismatch errors occur when trying to merge VACE with I2V models
  - *From: Kijai*

- **14B model requires 54GB VRAM officially**
  - Inference takes incredible VRAM due to DF sampling method
  - *From: Kijai*

- **Phantom incompatible with other reference methods**
  - Needs reference in latents making it incompatible with other approaches
  - *From: Kijai*

- **Video quantization challenges**
  - 4-bit quantization may harm temporal attention too much for video models
  - *From: deleted_user_2ca1923442ba*

- **1.3B models insufficient for detailed facial fidelity**
  - Phantom and 1.4b VACE are too weak to capture true facial fidelity from reference pics, especially for celebrity-like accuracy
  - *From: Zuko*

- **TeaCache degrades hand quality**
  - Higher TeaCache threshold settings tend to make hands look messy/degraded
  - *From: lostintranslation*

- **Phantom has sampling time overhead**
  - 33% additional sampling time due to doing 3 passes during generation
  - *From: Kijai*

- **MultiGPU wrapper has device compatibility issues**
  - Known bug causing 'Expected all tensors to be on the same device' errors when splitting models across GPUs
  - *From: MilesCorban*

- **Short video generation unreliable**
  - Videos under 33 frames don't work well for quality testing, model tuned for 81 frames
  - *From: Kijai*

- **DF model incompatible with torch compile**
  - Quality and performance suffer when using torch compile with DF model
  - *From: Kijai*

- **Blurry hands issue unsolved**
  - No good solution found for blurry hands problem
  - *From: Piblarg*

- **SLG causes color burnout**
  - SLG improves motion but creates snotty/burned appearance requiring CFG adjustment
  - *From: lostintranslation*

- **Phantom grid input doesn't work well**
  - Feeding 2x3 grid of character images in one latent distorts results compared to separate latents
  - *From: mamad8*

- **Phantom and VACE combination works badly**
  - Phantom image takes over everything, and ending Phantom early loses all reference
  - *From: Kijai*

- **fp8_fast always been really bad for Wan**
  - Should not be used with Wan models
  - *From: Kijai*

- **Torch compile slow and eats extra memory**
  - Uses about 4GB more VRAM
  - *From: Kijai*

- **Character LoRAs not working perfectly with DF models**
  - Wan14b T2V LoRAs working only to some degree
  - *From: seitanism*

- **UniAnimate does not work on SkyReels V2 DF models**
  - Compatibility issue with newer DF architecture
  - *From: DawnII*

- **DF quality degrades with complex scenes**
  - Lots of detail in scenes causes more degradation over extensions
  - *From: seitanism*

- **Cannot resample middle clips in DF chain**
  - Resampling breaks continuity with other clips, only works for single clips or last clip before continuing
  - *From: seitanism*

- **Video generators are 8-bit with no dynamic range**
  - Cannot recover clipped highlights in post-processing
  - *From: Fabricatedgirls*

- **Skyreels may have cheap video look baked in**
  - Clipped highlights and oversaturated colors that are harder to fix
  - *From: Fabricatedgirls*

- **UniAnimate only works with 14B models**
  - No 1.3B version exists, limiting accessibility for users with less VRAM
  - *From: Kijai*

- **fp8_fast ruins I2V quality**
  - While it works fine for T2V with speed benefits, it completely destroys quality in I2V mode
  - *From: Kijai*

- **DF input frame restrictions**
  - Cannot input more frames than the generation frame count setting, requires preprocessing to extract correct number of frames
  - *From: Kijai*

- **Skyreels has baked-in oversaturation**
  - Color palette appears oversaturated and difficult to control via prompting
  - *From: seitanism*

- **Wan fp8 quality degradation**
  - Even with fix, doing FFN layers on fp8 still has huge quality hit especially with I2V. Excluding FFN layers fixes quality but then it's rarely any faster
  - *From: Kijai*

- **SkyReels I2V 720P memory requirements**
  - 500GB of memory still consistently runs out of memory, model loading takes tens of minutes
  - *From: Soutlkf*

- **Input frame override**
  - Input frames are very strong and often override the prompt, making it difficult to control generation
  - *From: seitanism*

- **Camera control only supports panning movements**
  - No zoom functionality, only pan-and-tilt movements (left, right, up, down)
  - *From: Kijai*

- **Sparge attention parameters very model specific**
  - Limited to 1.3B T2V only and possibly limited to other generation parameters as well
  - *From: Kijai*

- **Multiple control models require extra passes**
  - Each additional control model adds 33% more to inference time
  - *From: Kijai*

- **Fun models have quality issues**
  - Quality is not as great as other models, less than ideal results
  - *From: Hashu*

- **Step1X-Edit requires 46GB VRAM**
  - Very high VRAM requirement for 768x768 generation
  - *From: mamad8*

- **Loop_args don't work with 14B model**
  - According to Kijai, loop_args parameter doesn't like the 14B model, works better with 1.3B
  - *From: David Snow*

- **VACE start image feature loses style after about a second**
  - Start image feature doesn't properly capture reference image style and what it does capture phases out quickly
  - *From: David Snow*

- **Same start/end image produces non-moving video**
  - Setting start and end image to the same thing results in expensive static image rather than loop
  - *From: ameasure*

- **Quality degradation with DF model extending different resolution clips**
  - DF 540p model doesn't understand input from 720p model well, quality degrades fast when extending
  - *From: seitanism*

- **Block swap implementations may not work properly**
  - Current block swap code either doesn't do anything or runs blocks on CPU, may interfere with ComfyUI's normal offloading
  - *From: Kijai*

- **FantasyTalking only 81 frames**
  - Limited length output, though can be extended with loops
  - *From: Kijai*

- **FantasyTalking doesn't work with DF**
  - DF isn't I2V model, doesn't use image cross attention
  - *From: Kijai*

- **FantasyTalking designed for 720p model but runs at 512p**
  - Using 480p gives artifacts but works
  - *From: Kijai*

- **Video degradation with DF extension**
  - Especially obvious with 1.3B version when scene content doesn't change much
  - *From: Ablejones*

- **Base Wan DG models don't work well with VACE**
  - Contradictory reports, but generally poor compatibility
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fantasy Talking English only**
  - Model only supports English audio, Chinese and other languages don't work
  - *From: Kijai*

- **Fantasy Talking mono audio only**
  - Only supports mono audio input, stereo gets converted by using left channel
  - *From: Kijai*

- **Motion degradation beyond 81 frames**
  - While model can generate 121+ frames, motion quality decreases significantly
  - *From: Kijai*

- **Control LoRA VACE incompatibility**
  - Cannot use control LoRAs with VACE due to input channel modifications
  - *From: Kijai*

- **LoRA model size compatibility**
  - LoRAs trained for 1.3B cannot be used with 14B models and vice versa
  - *From: Fill*

- **Fantasy Talking resolution sensitivity**
  - Effect becomes weaker at higher resolutions than training resolution
  - *From: Kijai*

- **Fantasy Talking frame limit**
  - Limited to 81 frames maximum, more than that kills LoRA functionality
  - *From: Stad*

- **Fantasy Talking language support**
  - Only works in English
  - *From: Stad*

- **VACE doesn't work with Fun models**
  - Only works with normal 1.3B base models
  - *From: Kijai*

- **Camera control doesn't understand roll**
  - Model may not comprehend roll movements in camera control
  - *From: Kijai*

- **LoRA flash artifacts**
  - EX Video LoRA causes 5+ frame flash at video start
  - *From: Gavmakes*

- **DF brightening over time**
  - Sliding models build up brightness over time from context passing
  - *From: Draken*

- **I2V cannot generate new objects not present in source image**
  - Works for simple modifications like adding hats but fails to create entirely new elements
  - *From: Draken*

- **Text generation worse in I2V than T2V**
  - Due to low resolution vision encoder (326x326) used under the hood
  - *From: pom*

- **Vision encoder resolution too small**
  - Old siglip 326x326 resolution causes issues with text generation and fine details
  - *From: pom*


## Hardware Requirements

- **4090 performance**
  - fp16_fast: 12.19s/it, bf16: 15.26s/it for 81 frames 40 steps at 480x832
  - *From: ezMan*

- **A6000 limitations**
  - Using A6000 for fp16 model takes over an hour with jet engine noise levels
  - *From: Doctor Shotgun*

- **VRAM for VACE**
  - VACE model is double the size of fp8 wan1.3b but still manageable for 1.3B, extra compute required
  - *From: Kijai*

- **VRAM usage**
  - 832x480x45 frames: 19GB, can spike to 31GB for 480p generations
  - *From: multiple users*

- **16GB VRAM support**
  - Can run on 16GB VRAM around 12GB usage
  - *From: zelgo_*

- **Model size**
  - Only ~3.5GB in fp16, so offloading doesn't save much
  - *From: Kijai*

- **VRAM for long generations**
  - 333 frames at 480x768 used 14GB VRAM, took 2hr10m
  - *From: PookieNumnums*

- **16GB VRAM performance**
  - 41 frames in one minute at 10 steps FP16, 3 minutes at 30 steps
  - *From: VK (5080 128gb)*

- **Context windows memory usage**
  - Doesn't use more memory than 81 frames would, slower but more efficient
  - *From: Kijai*

- **12GB VRAM VACE settings**
  - Need 27+ block swap, start with 480x480 resolution and 33 frames, then scale up gradually
  - *From: Ashtar*

- **VACE memory usage**
  - With 81 frames at 480x832, uses ~2GB less memory after TeaCache fix (down to 17.031 GB max reserved)
  - *From: Kijai*

- **Torch 2.7+ required**
  - torch.backends.cuda.matmul.allow_fp16_accumulation requires torch 2.7.0.dev2025 minimum
  - *From: Ashtar*

- **GPU compute capability**
  - RTX 3060 has insufficient compute capability for fp8_fast models, need 9.0 or 8.9+
  - *From: Faux*

- **Memory savings with fp8_scaled**
  - Using fp8_scaled over bf16 saves 11GB VRAM
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Speed comparison fp16 vs fp32**
  - Setting base precision fp16 with no quants is much faster than fp32 with fp8 quant
  - *From: seitanism*

- **VACE memory usage**
  - 960x960 at 60 steps works on 3090 with 128GB RAM using block swap, large resolutions need memory management
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Performance benchmark**
  - 61 frames at 1280x544 V2V takes 139 seconds on undervolted 4090 at 50% power without optimizations
  - *From: David Snow*

- **Long video generation RAM usage**
  - VAE works on few frames at a time, main limitation is RAM not VRAM for length. 1300+ frames possible
  - *From: Kijai*

- **VACE VRAM requirements**
  - 12GB VRAM struggles with 81 frames, needs aggressive block swapping. Works with 27 frames.
  - *From: Ashtar*

- **720p context generation**
  - Very slow process, approximately 35.28s per iteration
  - *From: A.I.Warper*

- **4090 performance**
  - A.I.Warper and Kytra both using 4090, prompt execution around 1500-2115 seconds for 41 frames 1280x720
  - *From: A.I.Warper*

- **3060 12GB capability**
  - RTX3060 12GB can handle 81 frames at height=960 with block swap after git pull update
  - *From: Ashtar*

- **5090 setup**
  - Users reporting successful setup with PyTorch nightly cu128
  - *From: Piblarg*

- **DG model speed**
  - 4 steps with DG model, cfg 1.0, generates in 7 seconds
  - *From: Kijai*

- **VACE with DG inference time**
  - DG High V4 + VACE (5 steps) generates in 50 seconds
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MMAudio VRAM**
  - Takes about 8GB VRAM
  - *From: Benjimon*

- **DG model performance**
  - Very fast, 38 seconds vs 10 minutes for normal Wan, 2s/it for 960x608x61
  - *From: burgstall*

- **SkyreelsA2 VRAM usage**
  - Same as 14B model, no extra inputs required
  - *From: Kijai*

- **Wan latents memory usage**
  - Takes much VRAM due to huge input with many frames, calculations not done in quantized precision even with 16GB quantized model
  - *From: Kijai*

- **VRAM usage for VACE**
  - Nearly as much VRAM as 14B Fun models, heavier than expected for 1.3B
  - *From: DawnII*

- **Triton compatibility**
  - Works with Python 3.12/CUDA 12 on Windows 11, can install in ComfyUI embedded Python
  - *From: Lumi*

- **VACE VRAM usage optimized**
  - 832x480x81 frames: ~12GB VRAM without offloading, 1024x1024x81: ~13GB VRAM, significant reduction from previous versions
  - *From: Kijai*

- **Highest resolution tested**
  - 720x960 with 720p model using GGUF on limited GPU
  - *From: traxxas25*

- **VRAM for 14B inference**
  - 173 frames at 848x480 takes 15 mins on 4070 Ti (12GB VRAM) with sage attention and block swap
  - *From: traxxas25*

- **8GB VRAM capability**
  - Possible to run 14B T2V on laptop 4070 8GB taking 3 hours for 17 frames
  - *From: froyo*

- **Training VRAM needs**
  - 7GB VRAM for training with fp8 model, 8GB training is possible
  - *From: Piblarg*

- **14B speed benchmarks**
  - 81 frames at 768x768, 8 steps: 631 seconds on undervolted 4090 (50% power)
  - *From: David Snow*

- **VACE VRAM usage**
  - Takes 3-5 minutes on 96GB VRAM runpod instance
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE memory optimized**
  - 832x480x81 frames now uses only 6GB VRAM during sampling with optimizations
  - *From: Kijai*

- **RTX 2080 bf16 limitation**
  - RTX 2080 doesn't fully support bf16 - must use fp16 for models and VAE
  - *From: Kijai*

- **14B VRAM with offloading**
  - 14B can work with 8GB through offloading but will be extremely slow
  - *From: Kijai*

- **VRAM for tiled encoding**
  - Tiled encoding recommended for 8GB VRAM or less, encoding heavier than decoding
  - *From: Kijai*

- **A6000 compatibility**
  - Works on A6000 with proper quantization settings
  - *From: Gateway {Dreaming Computers}*

- **HD video processing time**
  - 1920x1080, 45 frames took 3+ hours with white padding reference image
  - *From: xwsswww*

- **14B model inference time**
  - 14B model took half hour for generation
  - *From: Flipping Sigmas*

- **RTX 4090 block swapping**
  - Question about block swapping needed for Fun Control 14B on RTX4090
  - *From: JmySff*

- **VRAM for 1920x1080 81f generation**
  - Possible on 4090 with tiled VAE bf16, took about 30 minutes
  - *From: Pedro (@LatentSpacer)*

- **Render time for 1280x720**
  - 20 minutes on RTX 3090
  - *From: burgstall*

- **Speed improvement with DG model**
  - First test inference went from 7:12 to 3:42
  - *From: DawnII*

- **14B model needs 24GB VRAM**
  - Can run 14B at 81 frames decent resolution without swap if you don't use monitor or use GGUF q6, but 16GB will lose speed benefits to offloading
  - *From: Kijai*

- **VRAM for video depth**
  - Had to reduce to 512 due to OOM issues, potential memory leak
  - *From: traxxas25*

- **Generation times**
  - 20 min on 480x832 with 81 frames on some setups, 90 seconds after flux inpaint on others, 5 mins on 3090
  - *From: claygraffix*

- **4090 performance**
  - User with 4090 can run wan 1.3b in both bf16 and fp32 with quantized peripheral models
  - *From: notid*

- **WAN 14B on 24GB VRAM**
  - 14B model works on 24GB VRAM GPUs
  - *From: Guillaume*

- **Training time on 4090**
  - Style LoRA training takes about 1 hour on RTX 4090
  - *From: Jas*

- **I2V inference on 3090**
  - 14B I2V takes long time even on RTX 3090
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Generation time with high-end GPU**
  - RTX 4060Ti 16GB: 165 frames at 848x480, 25 steps took 55.75s/it for 10 seconds of video
  - *From: Vérole*

- **VACE generation performance**
  - 245 frames at 848x480 with 8 steps took 11:31 total (86.41s/it) on 4060Ti 16GB
  - *From: Vérole*

- **Cloud system timing**
  - GGUF 8 at 8 steps: 81 frames in 2 mins 45 seconds. 25 steps: 347 seconds per scene
  - *From: AJO*

- **81 frames vs 49 frames performance difference**
  - 4090 with 128GB RAM: 49 frames under 6 minutes, 81 frames hangs at 12% and stops progressing
  - *From: boorayjenkins*

- **VACE performance improvement**
  - Got 720p for 81 frames in 4 mins with VACE workflow on 4090
  - *From: boorayjenkins*

- **720 model VRAM usage**
  - VRAM goes to 100% usage, 720 model is hefty beast, recommend 20 blocks for block swap
  - *From: David Snow*

- **Multi-GPU support**
  - Wan supports multi GPU, can use CUDA_VISIBLE_DEVICES=1 in Linux or custom nodes for multiple GPUs
  - *From: Benjimon*

- **4060 ti 16GB performance**
  - 220 frames at 368x640 in 2min 17sec using 6.5GB VRAM with Fun 1.3B + ExVideo LoRA
  - *From: Pol*

- **720p VRAM usage**
  - 81 frames at 720p uses only 9GB VRAM with Fun model, much less than VACE
  - *From: A.I.Warper*

- **SageAttention 2.0 speed improvement**
  - More than 2x faster with larger input sizes, requires CUDA 12.8
  - *From: Kijai*

- **4070ti performance comparison**
  - 225 frames at 848x480 took 8 hours with VACE model, much slower than Fun
  - *From: traxxas25*

- **RTX 8000 compatibility**
  - Works with FP16 and SDPA attention, no BF16 support, very slow inference
  - *From: Benjimon*

- **VRAM for TeaCache**
  - Can use main_device for faster performance if spare VRAM available, otherwise offload_device
  - *From: DawnII*

- **RIFE interpolation**
  - Low VRAM usage for frame interpolation
  - *From: seitanism*

- **Multi-GPU usage**
  - Can run separate Wan sessions on each GPU, NVLink not beneficial
  - *From: Benjimon*

- **FLF2V VRAM usage**
  - 81 frames at 768x768 with 30 steps: Max allocated 15.175 GB, Max reserved 16.812 GB with TeaCache
  - *From: Kijai*

- **H100 80GB doesn't need offloading**
  - Depending on resolution, H100 with 80GB may not need model offloading
  - *From: Kijai*

- **16GB VRAM with fp8 scaled**
  - Workable with offloading for 81 frames of 720x480, but struggles with LoRAs on Q8 GGUF
  - *From: lostintranslation*

- **FramePack VRAM**
  - Minimal 6GB for 1-minute video at 30fps with 13B model, laptop GPUs okay
  - *From: zelgo_*

- **FramePack generation speed**
  - 4090: 9.6 minutes for 5 second clip without optimizations, under 2 minutes per batch with teacache/sage/flash/xformers
  - *From: TK_999*

- **Long video generation time**
  - About 1 hour estimated for 30 second video on consumer hardware
  - *From: Cubey*

- **FLF2V on 12GB VRAM**
  - Can generate above 480p resolution with 81 frames using 37-40 blocks_to_swap and fp8 model
  - *From: DawnII*

- **FLF2V on 24GB VRAM**
  - Can generate 640x640, 33 frames with 40 blocks_to_swap. OOM issues can be RAM related, not VRAM
  - *From: mamad8*

- **VACE memory usage**
  - Uses extra 15 blocks compared to regular inference, limiting long sequence generation
  - *From: A.I.Warper*

- **VRAM for high resolution VACE**
  - 720x1280 resolution may be challenging on 16GB GPUs like 4060ti
  - *From: deleted_user_2ca1923442ba*

- **Cloud GPU pricing**
  - H100s available for $0.50/hour, eight 24GB GPUs for under $0.20/hour on vast.ai
  - *From: deleted_user_2ca1923442ba*

- **3090 fp8 support**
  - Can use fp8_e5m2 weights with torch compile, SageAttention 2.0+ works with direct cuda mode
  - *From: Kijai*

- **UniAnimate VRAM requirements**
  - Will not work with 8GB cards
  - *From: xwsswww*

- **Long video generation hardware**
  - 720p 1000 frame generation possible, requires significant compute power
  - *From: Flipping Sigmas*

- **Memory for depth processing**
  - VideoDepthAnything can cause OOM at 720x480x41 frames on 16GB VRAM
  - *From: lostintranslation*

- **Processing time for upscaling workflow**
  - 320 seconds for full upscaling workflow on test hardware
  - *From: lostintranslation*

- **UniAnimate speed on 4090**
  - Around 3 minutes with every optimization for same performance as 14B I2V
  - *From: Kijai*

- **Storage needs for video models**
  - Multiple users reporting 1TB+ of video diffusion models, requiring 4-8TB storage drives
  - *From: CJ*

- **720p generation on 24GB VRAM**
  - Need to split into 41 frame runs on 24GB VRAM
  - *From: A.I.Warper*

- **4090 performance**
  - 345 seconds for style transfer generation
  - *From: Gavmakes*

- **VRAM for 1.3B at 544x960**
  - Around 8GB at fp16
  - *From: Kijai*

- **VRAM for full resolution 97 frames**
  - Under 9GB for 960x544
  - *From: zelgo_*

- **14B requirements**
  - Same as regular Wan (fits in 24GB)
  - *From: Benjimon*

- **Generation time on H100**
  - 128 seconds for 1.3B model
  - *From: VRGameDevGirl84(RTX 5090)*

- **4070Ti performance**
  - 97 frames 544x960 30 steps in ~7.21s/it with optimizations
  - *From: Corneilious Pickleberry*

- **MAGI-1 VRAM needs**
  - 24B model needs 8x4090 recommended, 4.5B variant will run on 1x4090, FP8 27GB, Q4 should be runnable on 16GB VRAM
  - *From: yi*

- **SkyReels DF on 12GB card**
  - Got 14B DF model working on 12GB card at 480x480 passing 33 frames between samplers
  - *From: Davidodave*

- **14B models performance**
  - 14B models take about 20 minutes per generation, too slow for some users
  - *From: Colin*

- **MAGI-1 VRAM**
  - Requires 8x4090 GPUs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Block swap optimization**
  - Trial and error, reduce blocks until OOM then add 1-2 back
  - *From: zelgo_*

- **System fallback setting**
  - Disable 'prefer no system fallback' in Nvidia control panel to prevent slowdown from VRAM spilling to system RAM
  - *From: zelgo_*

- **14B 480p VRAM usage**
  - Around 83% VRAM usage with 16GB, fails without system fallback
  - *From: lostintranslation*

- **14B DF model VRAM**
  - Officially needs 54GB, practically uses ~30GB during sampling on RTX 5090
  - *From: Kijai*

- **TeaCache memory usage**
  - Standard mode: ~4GB, 'e' mode: ~600MB
  - *From: Kijai*

- **Time step embedding**
  - Takes 7GB alone when using DF sampling
  - *From: Kijai*

- **RTX 5090 limits**
  - Max 69 frames on first gen with 14B DF model before OOM
  - *From: jellybean5361*

- **Phantom VRAM usage**
  - Uses 10.6GB VRAM for 1280x768x81 generation, around 9GB base usage
  - *From: TK_999*

- **SkyCaptioner memory usage**
  - Loads in 16.7GB RAM with no quantization
  - *From: TK_999*

- **MultiGPU setup recommendation**
  - Put model on 4090, VAE+text on 3090 for optimal memory distribution
  - *From: MilesCorban*

- **Minimum VRAM trend**
  - 16GB is becoming minimum requirement as developers move away from 8GB GPU support
  - *From: deleted_user_2ca1923442ba*

- **ComfyUI-LatentSyncWrapper VRAM**
  - Requires 20GB VRAM for lipsyncing, causes OOM on lower VRAM
  - *From: xwsswww*

- **4080 generation speed**
  - ~470s to generate 81 frames at 512x768 with teacache 0.25, improved to 300s with fp16_fast
  - *From: lostintranslation*

- **4090 vs 3090 torch compile compatibility**
  - 4090 can use e4m3fn with ~30% speed boost, 3090 needs e5m2 format
  - *From: Kijai*

- **Multi-GPU performance**
  - 35 second generations for Phantom on 8 GPUs at 832x480, 50 steps
  - *From: Kytra*

- **Generation time comparison**
  - 480p model: 6min, 720p model: 7min for same resolution output
  - *From: N0NSens*

- **RTX 3090 compatibility with 14B model**
  - 24GB VRAM works for DF 14B model
  - *From: MilesCorban*

- **Resolution recommendations for DF model**
  - 640x480 works fine for testing, can play with aspect ratios
  - *From: MilesCorban*

- **RAM requirements causing slowdowns**
  - 32GB RAM can cause 5+ minute delays when changing prompts due to swapping
  - *From: mamad8*

- **A6000 torch compile support**
  - Torch compile now works on A6000, speed improvement from 14.22s/it to 12.22s/it
  - *From: MilesCorban*

- **RTX 4090 VRAM limits**
  - At 640x480 max around 40-50 frames, overflow to RAM without block swap
  - *From: MilesCorban*

- **Long generation times on RTX 5090**
  - 832x528 with 20 steps taking hours, much longer than expected
  - *From: VRGameDevGirl84(RTX 5090)*

- **A6000 for testing**
  - Switched to A6000 for VRAM capacity, taking speed hit for testing
  - *From: MilesCorban*

- **DF 720p model VRAM**
  - 720x720x81 frames used 10.253GB max allocated, 12.406GB max reserved with 30 blocks swapped on 4090
  - *From: Kijai*

- **Phantom model VRAM**
  - Takes about 10GB VRAM, can be lowered to 8GB
  - *From: slmonker*

- **DF generation time**
  - ~20 minutes for DF generation on 4090
  - *From: TK_999*

- **Skyreels speed improvement**
  - fp8_fast gives 20-25% speed boost, reducing generation from 4.5min to 3.5min
  - *From: seitanism*

- **fp8_fast GPU compatibility**
  - fp8_fast only works on 4000 series GPUs and up, provides 30% speedup. fp16_fast works on 3090 but fp8_fast does not
  - *From: Kijai*

- **3090 I2V performance**
  - 3090 24GB VRAM can run Wan2_1-SkyReels-V2-I2V-14B-720P at 81 frames, 480x480, 10 blockswap in 14 minutes with teacache
  - *From: mamad8*

- **4090 performance comparison**
  - 4090 generates 77 frames at 1280x720 faster than 5090 at 30 steps vs 20 steps
  - *From: ezMan*

- **VRAM usage for Step1X-Edit**
  - 46GB VRAM required for 768x768 generation
  - *From: mamad8*

- **H100 performance**
  - 77 frames at 1024x560 with 20 steps completed in 483 seconds, max memory 52.4GB
  - *From: VRGameDevGirl84(RTX 5090)*

- **4090 limitations**
  - Skyreels DF 720 at 640px for 121 frames works on 4090, but OOM at higher resolutions
  - *From: boorayjenkins*

- **850W PSU adequacy**
  - 850W PSU should be adequate for 3090 unless powering high-end CPU at full load
  - *From: seitanism*

- **RTX 5090 VRAM usage**
  - Max allocated 16.100 GB, max reserved 16.969 GB for 89 frames at 1024x576 with Phantom
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 4090 with fp8 quantization**
  - 640x480 clips fit mostly in VRAM with minimal system RAM offload
  - *From: MilesCorban*

- **RTX 4090 with fp16 models**
  - fp16 works but requires significant offloading to system RAM
  - *From: MilesCorban*

- **14B model VRAM usage**
  - Pegs VRAM at 97% usage during generation
  - *From: David Snow*

- **RTX 5090 pricing**
  - Card cost $2900 with protection plan, MSRP around $2000
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRAM for HiDream**
  - Colin runs full on 16GB VRAM, can do fp16 but takes longer
  - *From: Colin*

- **FantasyTalking VRAM**
  - Claims 5GB VRAM support despite using 720p model
  - *From: Stad*

- **Fantasy Talking VRAM**
  - 5GB VRAM possible with num_persistent_param_in_dit=0, but quality tradeoffs exist
  - *From: Faux*

- **Swap memory for 14B**
  - User needed 60GB RAM but had 32GB, used 28GB SSD as swap memory to run 14B model on 4060
  - *From: Stad*

- **RTX 5090 performance**
  - 1024x576, 89 frames, 30 steps completed in 3:07 (198 seconds total), 16.1GB max VRAM
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fun_Inp model size**
  - 1.3B Fun model is 3GB weight, potentially usable on 8GB GPUs
  - *From: Blink*

- **Fantasy Talking on RTX 5090**
  - 2 minutes 44 seconds for 81 frames at 512x512 with 20 steps, max 19.3GB VRAM
  - *From: VRGameDevGirl84(RTX 5090)*

- **Compute capability for torch._scaled_mm**
  - Requires CUDA compute capability >= 9.0 or 8.9, or ROCm MI300+
  - *From: J_Pyxal*

- **DF 14B 720p on RTX 3090**
  - No OOM but won't progress past first step, too heavy
  - *From: PirateWolf*

- **Wan I2V 14B VRAM usage**
  - Max allocated 19.738 GB, Max reserved 21.781 GB for 720x544, 81 frames, 25 steps - took 249.73 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 5090 setup issues**
  - Fresh install with triton and sage causing SystemError with recent ComfyUI update
  - *From: Baku*


## Community Creations

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models by Kijai, more stable than native
  - *From: Kijai*

- **VACE integration** (node)
  - Kijai added VACE model support to ComfyUI wrapper for video control and inpainting
  - *From: Kijai*

- **VACE workflow examples** (workflow)
  - Multiple users sharing working VACE workflows with different control types
  - *From: Hashu*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models by Kijai
  - *From: mentioned in context*

- **VACE embed node** (node)
  - Node that connects to sampler for VACE functionality
  - *From: Draken*

- **WanVideoWrapper VACE support** (node)
  - Added VACE Encode node to Kijai's wrapper for comprehensive video control
  - *From: Kijai*

- **Control LoRA for upscaling** (lora)
  - spacepixel made control LoRA for 1.3B model tiling upscale
  - *From: Piblarg*

- **Lofi girl style LoRA** (lora)
  - Custom LoRA for creating seamless lofi girl style videos with specific art style
  - *From: Mint*

- **pad image batch interleaved** (node)
  - Node to make gray frame creation simpler, can also pad single image and add empty frames between images for interpolation
  - *From: Kijai*

- **Auto segmenter** (tool)
  - Grabs the person or head or whatever automatically
  - *From: AJO*

- **VACE helper node for start/end frames** (node)
  - New helper node for easier setup of start and end frame batching in VACE workflows
  - *From: Kijai*

- **WanVideoWrapper** (wrapper)
  - ComfyUI implementation wrapper for WAN models with VACE support
  - *From: Kijai*

- **Start To End Frame node** (node)
  - Helper node for managing start and end frame workflows in VACE
  - *From: Kijai*

- **Test Pattern node** (node)
  - Creates test patterns and adds empty frames between keyframes
  - *From: Kijai*

- **ImagePad node** (node)
  - Simplifies padding images with white background for VACE reference requirements
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan video models
  - *From: Kijai*

- **Standalone VACE loader** (node)
  - New node for loading VACE separately from main model
  - *From: Kijai*

- **Lotus ComfyUI implementation** (node)
  - Kijai's implementation of Lotus depth/normal map generation
  - *From: Kijai*

- **Spline editor for bounding boxes** (workflow)
  - Method for creating animated bounding boxes for VACE control
  - *From: Hashu*

- **TAEW preview for Wan** (tool)
  - Enables low-pass preview during sampling for Wan models
  - *From: Zuko*

- **ComfyUI-BS-Textchop** (node)
  - Custom node for extracting multiple text segments using start/end markers, supports up to 15 outputs
  - *From: burgstall*

- **SkyreelsA2 ComfyUI implementation** (node)
  - ComfyUI wrapper node for SkyreelsA2 with example workflows
  - *From: Kijai*

- **Custom bbox inpainting workflow** (workflow)
  - Custom workflow developed with yo9o for targeted inpainting
  - *From: yo9o*

- **CivChan Wan LoRA** (lora)
  - LoRA for CivChan character
  - *From: Piblarg*

- **Claydoh model** (model)
  - Claymation/Play-Doh style Wan 14B model using custom Blender sculpts dataset
  - *From: Hot Hams, the God of Meats*

- **Frutiger Lora 14B** (lora)
  - Vaporwave/00s aesthetic style lora for WAN 14B model
  - *From: Dream Making*

- **LLM Polymath node** (node)
  - Custom node for LLM integration with Gemini API support
  - *From: yo9o*

- **VACE depth+pose blending workflow** (workflow)
  - Technique for combining depth and pose controls without showing rig artifacts
  - *From: yo9o*

- **Ghibli LoRA 1.3B** (lora)
  - Studio Ghibli style LoRA trained for 1.3B model, undertrained but functional
  - *From: Piblarg*

- **Ghibli LoRA 14B** (lora)
  - Studio Ghibli style LoRA trained overnight for 14B model
  - *From: Piblarg*

- **Depth map upscale workflow** (workflow)
  - Standalone workflow using better depth maps with soft light blend mode
  - *From: Flipping Sigmas*

- **Musubi trainer frontend** (tool)
  - H1111 - frontend built on top of musubi inference scripts
  - *From: Benjimon*

- **WireframeDesigner** (tool)
  - Lightweight alternative to Blender for creating wireframe control videos for VACE
  - *From: burgstall*

- **Mask expansion node** (node)
  - Node that can expand a mask in any direction, useful for bounding boxes with shadows or reflections
  - *From: traxxas25*

- **Tiled WanVideo VACE Encode** (node)
  - 2x2 tiled encoding option for handling higher resolution videos in VACE
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - Comprehensive wrapper for Wan models with VACE support
  - *From: Kijai*

- **VACE face swap workflow** (workflow)
  - Face swapping using VACE capabilities
  - *From: xwsswww*

- **Upscale/refine workflow with reward LoRAs** (workflow)
  - High resolution workflow using multiple reward LoRAs
  - *From: HeadOfOliver*

- **WanWeightedControlToVideo** (node)
  - Node for controlling weight and timeline application of weight for native WanFunControl node
  - *From: CJ*

- **FL_gemini nodes** (node)
  - Nodes for integrating Gemini AI for prompt generation in ComfyUI
  - *From: Fill*

- **VACE subject removal workflow** (workflow)
  - Uses BBOX from Florence2 to remove any subjects from videos, allows mask dilation
  - *From: ArtOfficial*

- **Multi-pass refinement workflow** (workflow)
  - Combines VACE first pass with vanilla 1.3B refinement using enhancement LoRAs
  - *From: David Snow*

- **ReCamMaster workflow** (workflow)
  - Basic workflow to turn single image into 81 frame video with camera controls
  - *From: Kytra*

- **Face crop and stitch workflow** (workflow)
  - Padded face crop and stitch with video workflow
  - *From: burgstall*

- **WanVideoWrapper nodes** (node)
  - Kijai's wrapper implementation with simple nodes merged to main
  - *From: Kijai*

- **Sequence feature for API** (tool)
  - Added feature sequence with delay parameter to reduce API failure chances
  - *From: Impactframes.*

- **Camera path workflow** (workflow)
  - Workflow for camera movement control in WAN
  - *From: Kijai*

- **WAN IPA implementation** (tool)
  - IPA (presumably IP-Adapter) implementation for WAN, works better as mix with i2v LoRA
  - *From: pom*

- **Custom sigmas for OptimalSteps** (tool)
  - Custom implementation of OptimalSteps scheduling for WAN native
  - *From: Vérole*

- **ComfyUI-AIR-Nodes target crop** (node)
  - Node pack with target crop functionality for cropping and processing video regions
  - *From: A.I.Warper*

- **Custom node for crop_data + mask** (node)
  - Written to accept crop_data plus new mask on generated output
  - *From: A.I.Warper*

- **Mask input for context window** (node)
  - Added mask input to context window node
  - *From: Kijai*

- **Wan looper workflow** (workflow)
  - Automatically grabs last frame and loops generation process multiple times
  - *From: AJO*

- **Animated Logo LoRA** (lora)
  - First version of LoRA for creating animated logos
  - *From: Alisson Pereira*

- **Fun 14B FP16 conversion** (model)
  - Converted 14B Fun model to FP16 for Turing GPU training compatibility
  - *From: Benjimon*

- **Ghibli 1.3B LoRA** (lora)
  - High quality Ghibli style trained on synthetic 14B data
  - *From: Piblarg*

- **Eyes In Camera LoRA** (lora)
  - Trained on Higgsfield dataset for camera-directed eye contact
  - *From: NebSH*

- **Custom interpolation node** (node)
  - Internal logic for framerate interpolation using GIMM_VFI
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TheDirector** (node)
  - Custom node for multi-scene wan generation with consistent characters
  - *From: AJO*

- **Orbit camera generation node** (node)
  - Node to generate orbit camera movements, limited to under 90 degrees
  - *From: Kijai*

- **ModelPatcher node** (node)
  - Workaround for using LoRAs with torchcompile
  - *From: Kijai*

- **Kijai FramePack ComfyUI implementation** (node)
  - Very early mockup version that runs FramePack in ComfyUI with native models except transformer
  - *From: Kijai*

- **Orbit creation node** (node)
  - Node to create camera orbits for RecamMaster
  - *From: Kijai*

- **VACE temporal mask generation node** (node)
  - Generates temporal masks automatically based on inputs for VACE keyframe system
  - *From: Kijai*

- **Probably Lora-Induced Degradation Fixer** (workflow)
  - Custom workflow to clear VRAM between batches to prevent LoRA-induced quality degradation
  - *From: lostintranslation*

- **Mediapipe face control tool** (tool)
  - Custom mediapipe JS API implementation for face landmark detection with filtering options
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ExVideo LoRA** (lora)
  - LoRA for video extension and style transfer, works well for long video generation
  - *From: Flipping Sigmas*

- **DG models depth control LoRA** (lora)
  - Depth control LoRA used in combination with style transfer workflows
  - *From: Flipping Sigmas*

- **Image batch manipulation nodes** (node)
  - Nodes for inserting keyframes and splitting image batches
  - *From: Kijai*

- **UniAnimate DWPose alignment node** (node)
  - Node for aligning DWPose to reference images
  - *From: Kijai*

- **SkyReels Wan version** (model)
  - Close to stock i2v model that supports Wan LoRAs
  - *From: Benjimon*

- **FramePackWrapper with keyframe support** (node)
  - Fork with added keyframe support for better control
  - *From: Ashtar*

- **Custom Sapiens pose node** (node)
  - Lite version for pose detection with part selection capability
  - *From: Kijai*

- **Modified pose detector** (tool)
  - Built modified detector for testing UniAnimate pose inputs
  - *From: Kijai*

- **DWPose failure workaround** (tool)
  - Added workaround to handle failed pose detections
  - *From: Kijai*

- **One-time Runpod installation script** (tool)
  - Automatically downloads everything for FLF workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **First working DF extension test** (workflow)
  - Initial implementation of Diffusion Forcing support
  - *From: Kijai*

- **WanVideoWrapper DF support** (node)
  - Added Diffusion Forcing sampler support with VACE compatibility
  - *From: Kijai*

- **VACE start/end frame automation node** (node)
  - Automatically generates grey frames and masks for VACE workflows
  - *From: Kijai*

- **Style LoRA training success** (lora)
  - 1.3B style LoRA trained using ostris ai-toolkit, working well on recent video generations
  - *From: Jas*

- **Character LoRA in progress** (lora)
  - Training character LoRA on 14B model using 1000 epochs with 104 images per epoch
  - *From: AJO*

- **Likeness LoRA improvement** (lora)
  - Likeness LoRA trained on Wan 14B works better on SkyReels
  - *From: Zuko*

- **VACE upscale workflow** (workflow)
  - Multi-stage upscaling workflow using VACE with reference images
  - *From: Cseti*

- **Structured prompting automation** (tool)
  - Automating SkyReels V2 structured prompting format
  - *From: fredbliss*

- **Multi-stage sampling workflow** (workflow)
  - Sigma split workflow for better quality and speed
  - *From: lostintranslation*

- **Phantom ComfyUI implementation** (node)
  - ComfyUI support for Phantom model with multi-reference image capability
  - *From: Kijai*

- **SkyReels prompter based on paper methodology** (tool)
  - Tool that generates dynamics-only prompts for SkyReels V2 I2V following the paper's guidelines
  - *From: fredbliss*

- **Character LoRAs for Wan** (lora)
  - Human likeness LoRAs working well with close expressions, trained on same pics across SDXL, HunYuan, and Wan
  - *From: boorayjenkins*

- **Jennifer Connelly LoRA** (lora)
  - Trained on Wan for celebrity likeness
  - *From: Fabricatedgirls*

- **ComfyUI-FramePacking** (node)
  - Node that rounds image sequences to nearest 4n+1 by padding last frame, plus trimming node
  - *From: Rishi Pandey*

- **ComfyUI-FramePacking** (tool)
  - Node that pads image batch to 4n+1 frames for Wan by duplicating last frame
  - *From: Rishi Pandey*

- **WAN VACE native workflow with auto masking** (workflow)
  - Combines VACE native implementation with segment anything for automatic masking
  - *From: Vérole*

- **ComfyUI-wanBlockswap** (node)
  - Node for block swap functionality, though effectiveness questioned
  - *From: orssorbit*

- **Florence2 + Groq i2v workflow** (workflow)
  - Uses Florence2 for image analysis and Groq LLM for video prompt generation
  - *From: David Snow*

- **Pepe meme LoRA** (lora)
  - LoRA for Pepe memes
  - *From: Piblarg*

- **Throwaway 1.3B LoRAs** (lora)
  - vpunk filmstyle, smbnes gamestyle, mjspooky filmstyle
  - *From: JohnDopamine*

- **Fantasy Talking ComfyUI nodes** (node)
  - ComfyUI implementation of Fantasy Talking lip sync model with audio CFG controls
  - *From: Kijai*

- **Variable CFG scheduling** (workflow)
  - Method to vary audio CFG over generation steps for better quality/sync balance
  - *From: Kijai*

- **Blender camera control script** (tool)
  - Converts Blender camera movements to Wan camera control format
  - *From: Kijai*

- **Camera control Blender addon** (tool)
  - Blender addon for camera control integration
  - *From: toyxyz*
