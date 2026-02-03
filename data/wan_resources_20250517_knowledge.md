# Wan Resources Knowledge Base
*Extracted from Discord discussions: 2025-05-17 to 2026-02-03*


## Technical Discoveries

- **Removing reference input completely improves motion**
  - Completely removing the reference input from VACE increases the amount of motion in generated videos
  - *From: Ablejones*

- **Dummy reference frame technique works**
  - Using a 'dummy' reference frame for the first frame allows motion establishment before reference kicks in
  - *From: Ablejones*

- **Color matching brings back transition artifacts**
  - Attempting to use color matching to prevent degradation reintroduces scene changes at transitions
  - *From: Ablejones*

- **VACE strength parameter affects all control images**
  - The strength parameter in VACE applies to the entire set of control images, not just the reference image
  - *From: pom*

- **Two VACE nodes chained requires reference image on both**
  - When chaining two native VACE nodes (one for control, one for reference), the first node also needs the ref image to function
  - *From: TK_999*

- **Delaying VACE reference improves motion**
  - Running first 2 steps without reference input, then remaining 6 with reference provides better motion while maintaining accuracy
  - *From: Ablejones*

- **Pure text prompts work without images**
  - The workflow can generate videos using only text prompts without any input images
  - *From: Tango Adorbo*

- **Motion decreases in subsequent passes**
  - Each subsequent pass in the workflow seems to slow down motion overall
  - *From: The Shadow (NYC)*

- **FusionX works with native VACE integration**
  - FusionX model works well with native ComfyUI VACE integration for faster generation
  - *From: Ablejones*

- **VACE works better with inpainting and masking**
  - VACE really seems meant to be used for inpainting and iterates on itself at each sampler when not using masking, making transitions obvious and changing content
  - *From: the_darkwatarus_museum*

- **Reference image acts as embedding vector nudge**
  - Reference image doesn't have to be followed but if it matches conditioning it reinforces it - stays cute with monster ref but no monster prompt, gets monstrous with monster prompt but not as much without monster ref
  - *From: Ablejones*

- **LightX causes camera artifacts**
  - If you mention 'camera' in prompts with LightX, it literally puts a camera in the video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Kontext works well for start/end frame control**
  - First real test with Kontext to set start and end frames worked surprisingly well - took many attempts with Kontext to get frames right but one shot on Wan
  - *From: Ablejones*

- **VACE prompt format discovered**
  - Found what appears to be the dataset and prompt format for VACE in evaluation datasets, with VACE ranking at top
  - *From: fredbliss*

- **Can use depth and normals together as one input using an image blend node**
  - If you use an image blend node you can use depth/normal/etc as one input
  - *From: Faust-SiN*

- **Previous VACE embeds can be chained together**
  - Each VACE encode node has a previous VACE embeds input, just set up one like you would for pose and one like you would for normal and feed one into the next
  - *From: Tango Adorbo*

- **Normals need to be desaturated and blurred when used with VACE**
  - You'll want to desaturate the normal and blur it a little. Otherwise the normal completely drowns out everything. VACE wasn't trained to take normals as input, but you can trick it into using them as depth
  - *From: Faust-SiN*

- **Using end frames but throwing them away prevents unnatural transitions**
  - The trick with this WF is using the end frames to set the trajectory of the generation, but then throwing away the actual end frames for the next segment. This prevents the video from being unnatural during transitions
  - *From: Ablejones*

- **Split samplers prevent motion reduction when using start and reference frames**
  - With VACE if you send a starting frame and also a reference frame, the motion is severely reduced. Start sampling with no reference frame for 1 or 2 steps to get motion going, then recreate VACE conditioning with reference image
  - *From: Ablejones*

- **Low resolution base generation followed by upscaling works well**
  - 480x480 20 steps with teacache 0.200 for base, then upscale with 0.79 denoise. Can get base generation down to 45 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context options enable processing very long videos**
  - I have done 600 frame videos using context options set to 81
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pusa LoRA enables successful video extensions without VACE**
  - Can extend videos using pure Pusa (no VACE) with 81 frames per batch, 17 frame overlap, extended 7 times for 30 second results
  - *From: Hashu*

- **Detail LoRAs can cause face issues with VACE/I2V**
  - When doing VACE or image 2 video, detail LoRAs can add too much detail to faces
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pusa improves reference fidelity and reduces degradation**
  - Pusa LoRA at strength 1.0 maintains much better likeness of reference characters and reduces the degradation effect compared to VACE alone
  - *From: Ablejones*

- **Phantom performance varies dramatically with frame count**
  - Phantom works well at 121 frames but produces 'midgets' and clothing inconsistency at 49 frames, 81 frames also shows degradation
  - *From: mdkb*

- **Lowering LightX LoRA strength reduces cross-batch burning**
  - Using 0.5 LoRA strength instead of higher values significantly reduces cross-batch burning artifacts
  - *From: A.I.Warper*

- **WanVacePhantomSimpleV2 node can work with GGUF models**
  - If you can run the model in ComfyUI without that node then it will run with that node too
  - *From: Ablejones*

- **Phantom is very good at higher resolution even though it wasn't trained on it**
  - Works well at higher resolutions despite not being trained on them
  - *From: Ablejones*

- **Video captioning workflow available**
  - Reference to video captioning solution in different channel
  - *From: xwsswww*

- **FFLF phantom vace model works well for lower frame counts**
  - Best result was 832 x 480 x 121_24fps in 18mins, but worked better at 81 frames with FFLF avoiding usual Phantom problems at less than 121 frames
  - *From: mdkb*

- **Fun Control 2.2 is better than VACE for video continuation**
  - Especially for scenes that would normally have huge color changes, produces better results for video extensions
  - *From: Ablejones*

- **Impact Pack Detailer nodes work with video when warnings are bypassed**
  - The detailer nodes are already capable of running 5D tensors, only held back by 'does not allow image batches' warnings
  - *From: Ablejones*

- **Memory patcher improves generation times**
  - 1600x900x81 Wan22 t2v low denoise upscaler finished in 30 minutes where it used to take 50
  - *From: mdkb*

- **SEGSPreview now shows only first frame for each SEGS when it's a video**
  - This allows users to see how many SEGS it actually needs to run - if preview shows 9 segments, it will sample 9 full videos and stitch them together
  - *From: Ablejones*

- **New version of High 2.2 model fixes many issues**
  - Updated model available on Civitai that resolves various problems
  - *From: crinklypaper*

- **Detailer now uses a hook system instead of intrusive wrapper**
  - VACE now connects to detailer via a detailer hook in node pack instead of wrapper in impact pack, making detailer nodes function more like they normally do with images
  - *From: Ablejones*

- **Face detailing working with denoise 1.0**
  - Face was completely reconstructed by the model from reference and canny control
  - *From: Ablejones*

- **Different samplers show huge variation in results**
  - Unexpected large differences between samplers, some handle end frame transitions poorly while others promote more variation
  - *From: Ablejones*

- **Blockswap with 20 blocks helps with VRAM issues**
  - Using blockswap node with 20 blocks setting makes generation work on 24GB VRAM cards
  - *From: Slavrix*

- **V2 model fixes pose rig showing through in final render**
  - Switching from V1 to V2 model resolves issues with pose rig appearing in output
  - *From: Creature*

- **qin_zhang_2s sampler produces nice quality**
  - Higher order samplers often freeze the background but qin_zhang_2s looks quite nice
  - *From: TK_999*

- **VaceAdvancedModelPatch node can replace entire encoding node for model patching**
  - Instead of using a full WanVaceEncoder just to patch a model with LoRA, can use VaceAdvancedModelPatch node which is more efficient
  - *From: Ablejones*

- **Setting ETA to 0.0 eliminates fireflies/confetti noise artifacts**
  - When experiencing noise artifacts with fully_implicit_gauss-legendre_2s sampler, reducing eta to 0.0 cleans up the generation
  - *From: Ablejones*

- **Linear quadratic scheduler works better for low step counts than complex schedulers**
  - Beta and other complex schedulers lose their mathematical benefits at 4 steps, linear quadratic is more appropriate for 4-8 steps
  - *From: Ablejones*

- **Cseti's Kinestasis LoRA adds significant movement to animations**
  - Using Cseti's wan2.2-14B-Kinestasis_concept-lora at 0.45-0.8 strength on HN model adds much more movement than without, helps escape slow-mo effects
  - *From: The Shadow (NYC)*

- **Multiple WanVacePhantom nodes can be chained but phantom images must go in the last node**
  - When chaining multiple WanVacePhantom nodes, phantom and reference images should be added to the final node before the sampler to avoid latent size conflicts
  - *From: Ablejones*

- **Res4lyf 3s samplers do 3 model calls per step plus 1 extra at end**
  - lobatto_iiid_3s sampler makes 19 total model calls for 6 steps (3 per step + 1 final), significantly slower but higher quality than ddim
  - *From: Ablejones*

- **Sigma nodes override sampler step settings**
  - When using sigmas node it takes control over sampler step settings - if sigmas calls for 6 steps but sampler shows 4, the 6 from sigmas is what actually runs
  - *From: The Shadow (NYC)*

- **ClownsharkSampler uses base seed + 1 for noisy sampling**
  - When using ClownsharkSampler which doesn't expose seed setting, it uses the base seed + 1 for the noisy sampling when eta>0.0
  - *From: Ablejones*

- **HUMO works with 150+ frames**
  - HUMO can generate around 150 frames in one generation on 24GB VRAM at 1024x576, works at 121 frames at 1280x720, much longer than typical 3 second limit
  - *From: Juan Gea*

- **HUMO works with animals at strength 3**
  - HUMO audio-reactive model works effectively with animals (pets, fish) when using strength setting of 3
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **VACE strength works per latent frame**
  - VACE strength is applied per latent frame - first frame uses reference latent strength, remaining frames use control latent strengths
  - *From: Ablejones*

- **Ultimate Vocal Remover eliminates lip twitching in vid2vid**
  - Using Ultimate Vocal Remover for audio processing prevents lip twitching issues when doing vid2vid with Infinite Talking
  - *From: samhodge*

- **Race condition in Gemini API workflow**
  - Gemini response timing can cause prompts to not be ready when needed, causing repeated scenes
  - *From: samhodge*

- **Browser disconnection affects Gemini credentials**
  - If browser running frontend goes to sleep or disconnects, docker container continues but frontend doesn't pass ComfyUI credentials, resulting in null responses
  - *From: samhodge*

- **Path issues on Windows WSL causing index not to advance properly**
  - User reported index staying at 0 between runs due to file path configuration issues in WSL environment
  - *From: triquichoque*

- **Using same image for first frame and phantom reference causes problems**
  - Produces poor results with tears/distortion artifacts. Using diverse reference images instead produces much better results
  - *From: Gleb Tretyak*

- **Vace + Phantom merge workflow shows good character consistency**
  - User reports this combination works better than 2.2 workflows they tried, with proper character consistency when using diverse reference images
  - *From: Gleb Tretyak*

- **Audio scale setting affects mouth movement quality**
  - 2.0 audio scale can make characters look 'too shouty', 1.0 works better for some characters/styles
  - *From: samhodge*

- **New prompt creator node allows extensive customization**
  - Node includes fields for camera motion, character interactions, lighting, facial expressions, shots, outfit rules, and physical interactions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Auto-queue functionality working in new workflow version**
  - New node can automatically queue middle runs, only requiring manual intervention for final run if less than 16 groups
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face detailer LoRA can improve facial quality**
  - Adding face detailer LoRA at 2.0 strength makes faces look better in video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Frame count can be extended to 121 frames**
  - Can generate videos up to 5 seconds long (121 frames) instead of the previous 3.88 second limit, though first few frames may be funky
  - *From: VRGameDevGirl84(RTX 5090)*

- **Character description not needed in prompts**
  - Just using 'the woman' or 'the man' works fine - the model uses the reference image directly without needing detailed character descriptions
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX and FastWan LoRAs provide speed boost**
  - Using LightX with FastWan at 4 steps: 31.49 seconds vs LightX alone at 4 steps: 70.63 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fun 2.2 Vace better at following OpenPose**
  - Fun 2.2 Vace is very good at following openpose compared to regular Vace, using only openpose conditioning for motion
  - *From: Ablejones*

- **Context options enable longer upscales with limited VRAM**
  - At low denoise during upscaling, context switching is barely noticeable, enabling 1080p upscale on 16GB VRAM and longer videos on better cards
  - *From: Cseti*

- **Reference image ratio should match video ratio**
  - If generating 16:9 ratio video, reference image should be similar ratio for better results
  - *From: Santoshyandhe*

- **Krea1 images look better than Flux images**
  - When using Flux images it looks really fake. When using Krea1 images it looks much better
  - *From: VRGameDevGirl84(RTX 5090)*

- **Using 4 steps without FastWAN provides more cinematic results**
  - Removing FastWAN and using 4 steps gives more natural, cinematic results compared to using FastWAN accelerator
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face detailer LoRA improves face quality**
  - Custom face detailer LoRA helps make faces look better when using LightX2V, should be set to strength 1
  - *From: VRGameDevGirl84(RTX 5090)*

- **Slow motion occurs when using fast LoRAs with WAN 2.2**
  - FastWAN LoRAs cause slow motion effects with WAN 2.2, which is why people still use 2.1 in many cases
  - *From: kendrick*

- **Audio sync drift occurs across video segments**
  - Each video group gets slightly out of sync, becoming more noticeable by the end of long videos. Issue is caused by rounding/padding that adds frames of silence
  - *From: VRGameDevGirl84(RTX 5090)*

- **Random mouth movement can be controlled**
  - Mouth moves when there's noise in audio, mentions of singing/talking in prompts, or just HUMO behavior. Can be reduced by removing vocal references from prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context fields can be manually filled for consistent backgrounds**
  - Filling all 16 context fields with same background description (like 'a burning post-apocalyptic city') helps maintain more consistent backgrounds across scenes
  - *From: WackyWindsurfer*

- **Index node stays at 0 for 2-run videos but works for 3+ runs**
  - Workflow has bug where index doesn't update properly for videos requiring only 2 runs, but works fine for 3+ runs
  - *From: hudson223*

- **QwenEdit can be improved with 'clear skin' prompt**
  - Adding 'clear skin' to prompt removes unwanted skin details like moles and blemishes that QwenEdit AIO sometimes adds
  - *From: Tachyon*

- **Sage attention causes black screen issues with some models**
  - QwenEdit models can produce black outputs when using sage attention, disabling it resolves the issue
  - *From: Blink*

- **High Lightning LoRA strength too high in Mega v6**
  - Mega v6 has overly bright output due to high Lightning LoRA strength, and slower performance (128s vs expected 45s on 5090)
  - *From: Drommer-Kille*

- **VACE encoding can be done at lower strengths, but noise may be better**
  - Alternative approach to VAE encoding with VACE system
  - *From: pom*

- **Context options may cause specific issues**
  - Problems only occur when using context options, needs further testing
  - *From: Cseti*

- **RES4LYF samplers have unsampling/hybrid capabilities with sigma range controls**
  - AbNorsett helps with jittery trees in panning cameras but can lose face details. PEC is balanced across scheduler scale, cleans texture/color without killing detail. Lawson affects lighting/vibrance but is trickier
  - *From: vanhex*

- **Unsampler node can 'duck' noise above 0.6 during unsampling**
  - Keeps base structure of noise in frames. Can push up to 0.875 but becomes seed-dependent
  - *From: vanhex*

- **Switching schedulers from unsampling to resampling reduces noise without changing video structure**
  - Effective for removing 'dust' from videos using shift of 2-3 in Wan
  - *From: vanhex*

- **Impact Pack dependency causes auto-queue issues**
  - VRGameDevGirl84's workflow requires ComfyUI-Impact-Pack custom node for auto-queuing to work properly. Without it, workflows won't auto-advance between runs.
  - *From: VRGameDevGirl84(RTX 5090)*

- **5-second duration fixes sync issues**
  - Changing video generation from 4 seconds to 5 seconds (125 frames at 25 FPS) eliminates sync drift problems, while 4 seconds produces only 97 frames instead of expected 100.
  - *From: VRGameDevGirl84(RTX 5090)*

- **Language affects lip-sync quality**
  - French and Chinese languages produce better lip-sync results than English. Japanese, Korean, Italian, and Spanish are predicted to also work well based on phoneme similarity.
  - *From: Janosch Simon*

- **Individual video segments maintain sync better**
  - Individual generated segments (e.g., video_00003-audio.mp4) maintain almost perfect sync, but sync degrades during final video combination.
  - *From: WackyWindsurfer*

- **Shift value of 120 works for VACE extensions**
  - Using unusually high shift value of 120 (vs typical 4-6) helps with motion continuity in VACE video extensions without burning.
  - *From: Daviejg*

- **HuMo node requires frame counts that are 4n + 1 pattern**
  - Pattern is 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, etc. 100 frames gets rounded down to 97
  - *From: VRGameDevGirl84(RTX 5090)*

- **Claude AI is better than ChatGPT for code debugging**
  - Claude found a sync issue by analyzing a screenshot of workflow nodes, specifically identifying an audio crop node causing problems
  - *From: VRGameDevGirl84(RTX 5090)*

- **FP8_e4m3fn is better than FP8_e5m2 quantization**
  - Speed might be slightly better with e5m2 but quality difference doesn't make it worth it. Q8_0 was the only acceptable GGUF quantization
  - *From: patientx*

- **Resolution more effective than steps for quality**
  - 1280x720 at 4 steps gives better quality than higher steps at lower resolution, though takes longer (50 min vs 30 min)
  - *From: Chandler ✨ 🎈*

- **Fallback ffmpeg implementation works automatically**
  - Node uses imageio's built-in ffmpeg when system ffmpeg is not available: 'D:\AI\TEST\ComfyUI_windows_portable\python_embeded\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe'
  - *From: VRGameDevGirl84(RTX 5090)*

- **Can re-do specific scenes by muting unwanted groups**
  - Mute all groups except the one you want to re-do, then re-run the workflow to regenerate only specific scenes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Index -1 in select images node means end frame**
  - In VACE section, the second select images node with index -1 selects the last frame
  - *From: Cseti*

- **Can bypass LLM for consistent single-prompt videos**
  - For news anchor or single-scene consistency, bypass background remover nodes and Gemini LLM, use no prompts except same text in all Context nodes
  - *From: WackyWindsurfer*

- **CFG 1 required with LightX**
  - Negative prompts don't work as CFG must be set to 1 when using LightX
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context string has text limit**
  - The lyric string has a limit on how much text it can take, causing prompt truncation when using context strings
  - *From: VRGameDevGirl84(RTX 5090)*

- **Humo works for ref image to image**
  - Humo is competent for reference image to image generation, needs minimum 13 frames processing
  - *From: Chandler ✨ 🎈*

- **Prompt order affects character positioning**
  - Character being front and center the whole time might be related to prompt order
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo model babbles during instrumental sections due to needing lyrics for each scene**
  - The LLM needs a lyric for each scene or the prompts don't link up with the lyric. Pure silence for b-roll shots prevents blabber
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multiple reference images work better at 720p resolution**
  - If you give it a detailed face and also a full body reference it can use both of them at the same time on the same character. This works best at 720p resolutions
  - *From: Ablejones*

- **Frame count affects character consistency in Phantom**
  - When passing 3 ref characters to phantom: 49 frames produces 1 dwarf, 97 frames has wrong clothing on one person, 121 frames all look spot on
  - *From: mdkb*

- **81 frames with 14 frame overlap works well for elaborate transitions**
  - Found that 81 frames with a 14 frame overlap is pretty good too for more elaborate transitions
  - *From: happy.j*

- **Latent space upscaling causes ghosting issues**
  - Every single Latent Space Upscaler causes ghosting/doubling effect in one axis when upscaling from HN to LN model
  - *From: mdkb*

- **Don't let HN model denoise below 0.90 or 0.87**
  - The HN model isn't trained to remove noise below .90 or .87 so you are just wasting compute if you let it go to far
  - *From: jellybean5361*

- **Wan S2V (Speech-to-Video) produces poor quality results**
  - Multiple users tested Wan 2.2 S2V and found it looks like shit compared to HuMo
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE 2.2 requires different sampler than previous versions**
  - Dream Making found the culprit for issues was the sampler when using VACE 2.2
  - *From: Dream Making*

- **LightX LoRA causes unwanted lip movements**
  - Testing showed that LightX distill LoRAs are major culprit for lip movement when no audio is present
  - *From: Ablejones*

- **CFG and negative prompts can reduce unwanted lip movements**
  - Using CFG 3.0, 20 steps and negative prompts like 'talking, speaking, mouth movements, singing, yelling' reduces lip smacking better than LightX LoRA
  - *From: Ablejones*

- **No audio input better than empty audio for preventing lip movement**
  - Using no audio input was better than using empty audio clips for preventing unwanted lip movements
  - *From: Ablejones*

- **Resolution divisibility by 32 affects video quality**
  - Christian Sandor had square artifacts with 1280x720 (720 not divisible by 32), switching to 1024x576 solved all problems
  - *From: Christian Sandor*

- **Best combination of SVI Loras for clean continuations with Wan2.2 A14B I2V High Noise -> Wan HuMo 14B**
  - Workflow provides specific SVI lora settings for avoiding flash and maintaining consistency across extensions
  - *From: Ablejones*

- **Minimum block parameters found that suppress lipsync**
  - Frame cap seems to be 121 to avoid burn. Prompt needs to somehow indicate silence - 'standing' vs 'standing silently' makes a difference
  - *From: Chandler ✨ 🎈*

- **Audio attention layers hooking more successful than band editing in HuMo embeds**
  - Greater success now but caveat is frame limit reduced from 125 to avoid burn on first frames
  - *From: Chandler ✨ 🎈*

- **Color match node for video that prevents drift**
  - Normal color match nodes do matching on each frame individually to single reference causing drift when scene changes. Better to record color matching parameters from each video frame and apply to whole video
  - *From: Ablejones*

- **Using WanImageToVideoSVIPro on first sampler reduces color drift**
  - Made the first gen look somewhat same as the second which is good, though introduced some flash for a few start frames
  - *From: Gleb Tretyak*

- **Resolution significantly affects HuMo lipsync quality**
  - Moving from 512x512 to 1024x1024 resolution shows significant improvement in lipsync accuracy
  - *From: NC17z*

- **SageAttention-Triton doesn't negatively impact quality as feared**
  - Can be used at higher resolutions without major quality degradation
  - *From: Ablejones*

- **Audio padding improves lipsync**
  - Adding 0.2s of embedded silence to the start of audio helps with synchronization
  - *From: hudson223*

- **Prompting is crucial for HuMo performance**
  - Emotional direction and expression can get over-exaggerated, prompts mentioning talking/singing generate random mouth movements on first sample
  - *From: Mr_J*

- **Chain sampling mechanism explained**
  - Chain sampling runs first sampler for specified steps, then continues from that point with second sampler for remaining steps
  - *From: Ablejones*

- **Face size in pixels affects HuMo quality**
  - Resolution and size of the face in pixels is really important for HuMo performance
  - *From: Ablejones*

- **GGUF models work with end frames functionality**
  - GGUF models can be successfully used with end frame control nodes for better video generation control
  - *From: craftogrammer 🟢*

- **Audio encoding precision improvements**
  - Reworked audio scaling to only apply to first 2 frequency bands for more precise lip sync control
  - *From: hudson223*

- **Camera movement possible with lip sync**
  - Successfully achieved decent lip sync with camera movement using seed-sniping and proper prompting
  - *From: Ablejones*

- **VACE and HuMo can be combined in sampling schedule**
  - Can do HN sampling with VACE or VACE+Phantom, then switch to HuMo for LN sampling
  - *From: Ablejones*

- **Wan 2.1 performs nearly as well as Wan 2.2 with double sampling pass**
  - After much testing, Wan2.1 is 99.9% as good if not better than 2.2 if you do a second sampler pass
  - *From: Flipping Sigmas*

- **Original VACE 2.1 better at inpainting than Fun VACE 2.2**
  - Fun VACE 2.2 models forgot some things like inpainting, they are not as good as original VACE for that. When switched to original VACE with same WF it worked beautifully for first-last-frame control
  - *From: Ablejones*

- **Different sampler/scheduler combinations affect LoRA behavior**
  - ddim/beta + ddim/ddim_uniform will get you closer to reference image if changing likeness too much. er_sde/bong tangent and res_2s/beta57 make the inflation more extreme with nice detail
  - *From: ingi // SYSTMS*

- **Doubling up control frames improves frame preservation**
  - If you double up the frames, it does a better job of preserving the frames in VACE workflows
  - *From: brbbbq*

- **Native Wan prompt scheduling works differently than frame-specific systems**
  - Uses Context Window system with pipe (|) separator method - splits prompts across context windows rather than specific frame numbers
  - *From: Flipping Sigmas*


## Troubleshooting & Solutions

- **Problem:** Color and quality shift after several segments
  - **Solution:** Still being investigated - color matching attempts bring back transition issues
  - *From: Ablejones*

- **Problem:** Expected tensors to be on same device error with control inputs
  - **Solution:** Plug the control video into the Start to End Frame node
  - *From: pom*

- **Problem:** Motion becoming too static with control frame and reference
  - **Solution:** Delay the reference input by a few steps (e.g., 2 steps without reference, then 6 with reference)
  - *From: Ablejones*

- **Problem:** Long generation times on 4060Ti 16GB
  - **Solution:** Enable block swap (suggested 30-40 blocks), reduce resolution, ensure source images aren't too large
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** VACE Module error with checkpoints
  - **Solution:** VACE Module only works with wrapper, not native, and is meant for using VACE with other checkpoints - it's not a checkpoint itself
  - *From: Faust-SiN*

- **Problem:** Control masks not connected in workflow
  - **Solution:** Connect control masks to take advantage of masking that prevents continuation frames from changing
  - *From: Ablejones*

- **Problem:** Poor quality with LightX2V LoRA
  - **Solution:** Use more steps in first group (20 steps) before applying speed optimizations in subsequent groups
  - *From: The Shadow (NYC)*

- **Problem:** First frame not matching perfectly
  - **Solution:** Check GGUF loaders, NAG settings, and CFG values - disable NAG and set CFG back to 1 if needed
  - *From: The Shadow (NYC)*

- **Problem:** Native compile setup throwing error vs wrapper
  - **Solution:** Use wrapper with block swap at 40 as workaround
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Dark video output with color changes
  - **Solution:** Changed color match to 0, color changes depend on the image - some don't need correction
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Can't do 4 steps without LightX LoRA
  - **Solution:** Put LightX LoRA back and set to 1.00 when using 4 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Tensor error at 1920x1080
  - **Solution:** Use 1920x1072 instead to solve the error
  - *From: Koba*

- **Problem:** Character and setting drift in chained generations
  - **Solution:** Keep same reference image throughout to maintain consistency
  - *From: Ablejones*

- **Problem:** Workflow freezing due to too many nodes
  - **Solution:** Step away from overly complex workflows, use simpler approaches
  - *From: the_darkwatarus_museum*

- **Problem:** Kijai's wrapper MultiTalk branch crashes with VACE
  - **Solution:** Had to use a hacked up version of kijai's wrapper. Made VACE ignore the extra layers from multitalking cause it chokes on them
  - *From: Tango Adorbo*

- **Problem:** Normal node broke with ComfyUI update
  - **Solution:** Switched to NormalCrafter which works now and is much cleaner
  - *From: Faust-SiN*

- **Problem:** 1920x1080 resolution not working
  - **Solution:** Either update the divisible by to 16 or change it to 1920x1072
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** OOM issues with large video upscaling
  - **Solution:** Use context options set to 81 for default settings
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Group nodes causing workflow issues when sharing
  - **Solution:** Group nodes can be buggy when sharing workflows. Split out the nodes from the group
  - *From: Ablejones*

- **Problem:** High CPU usage from VideoHelperSuite nodes
  - **Solution:** Swapped in preview animation node and CPU usage went down to nothing
  - *From: garbus*

- **Problem:** Dimensions error with GGUF models
  - **Solution:** Dimensions need to be divisible by 16 for proper operation
  - *From: xwsswww*

- **Problem:** GGUF models not detected by diffusion model node
  - **Solution:** Cannot use GGUF models with VACE module in native - need merged model or different workflow approach
  - *From: mdkb*

- **Problem:** Triton error on 4070 12GB VRAM
  - **Solution:** Issue appears to be Triton-related memory problem
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Color shift issues with VACE
  - **Solution:** VACE encode node may be causing color shifts - prompting matters a lot, may need prompt tweaking for each batch
  - *From: Hashu*

- **Problem:** Subgraph workflow corruption
  - **Solution:** Select everything in workflow, copy it, make new empty workflow, then paste to fix corruption
  - *From: phazei*

- **Problem:** bf16 VACE module incompatibility
  - **Solution:** bf16 VACE module doesn't work properly with Phantom fp8_e5m2 - causes issues even when VACE not in workflow
  - *From: mdkb*

- **Problem:** OOM error with 16GB VRAM on aggressive workflow
  - **Solution:** Check frame count - workflow may be using entire length of input video by default which causes issues
  - *From: Ablejones*

- **Problem:** PC freezes during generation
  - **Solution:** Likely spilling into shared VRAM - use memory management techniques
  - *From: Ablejones*

- **Problem:** Unicode error installing janky_memory_patch.py
  - **Solution:** Download file correctly by clicking normally on GitHub then clicking raw download button, not right-click save as
  - *From: Ablejones*

- **Problem:** WanVacePhantomSimpleV2 error 'only integer tensors of a single element can be converted to an index'
  - **Solution:** Need images plugged into the phantom image input. VACE references can be empty. Don't plug videos into phantom image input as it causes OOM
  - *From: mdkb*

- **Problem:** Total steps and split step configuration error
  - **Solution:** If total steps is 10 and split step is 10, low noise starts at step 10 but total is 10 - need to adjust steps proportionally
  - *From: thaakeno*

- **Problem:** VACE module producing black outputs
  - **Solution:** Looks like when you use an I2V model without a start image - check image inputs
  - *From: Ablejones*

- **Problem:** Segs Detailer doesn't work with Wan/VACE/Phantom
  - **Solution:** Use modified Impact Pack fork that bypasses image batch warnings
  - *From: Ablejones*

- **Problem:** SEGS preview node getting stuck on video
  - **Solution:** Disable the node or use ImageFromBatch+ with decompose segs to display only one frame
  - *From: Ablejones*

- **Problem:** Tensor size mismatch with crop factor less than 1.5
  - **Solution:** Use crop factor between 1.2-1.5, lower values cause size alignment issues
  - *From: Ablejones*

- **Problem:** OOM with Tiled SEGS
  - **Solution:** Reduce crop factor to 1.20-1.50 instead of 3.0, and reduce bbox_size to decrease sampling dimensions
  - *From: Ablejones*

- **Problem:** Fun Control creating bright flashes during scene changes
  - **Solution:** Model doesn't want to be used for continuation, tends to hide scene changes with bright flashes
  - *From: Ablejones*

- **Problem:** Tensor size mismatch error in DetailerForEach
  - **Solution:** Use dimensions divisible by 16, even though VAE encodes to be divisible by 8
  - *From: Ablejones*

- **Problem:** upsample_trilinear3d_out_frame not implemented for 'Byte'
  - **Solution:** Update to latest version of forked impact-pack, issue fixed in SAM2 Video Detector node
  - *From: Ablejones*

- **Problem:** Pose rig showing through in final render
  - **Solution:** Try random seed, or adjust VACE strength up or down
  - *From: Piblarg*

- **Problem:** MASK to SEGS for Video node not working with detailer
  - **Solution:** Connect mask to segs nodes to Tile segs then to Detailer node, use SEGSDetailer For Video (SEGS/pipe) node
  - *From: xwsswww*

- **Problem:** Janky Memory Patcher node missing model input
  - **Solution:** Connect a model to the model input of the node
  - *From: Ablejones*

- **Problem:** OOM issues after ComfyUI update
  - **Solution:** Try increasing buffer GB to 1.0 or 2.0, free up more drive space
  - *From: Ablejones*

- **Problem:** Seed must be between 0 and 2**32 - 1
  - **Solution:** Change seed value, user fixed by entering 20000
  - *From: xwsswww*

- **Problem:** Audio crop error with start/end time
  - **Solution:** Use mp3 instead of wav, use melbandroformer_fp32 instead of fp16, reset index to 0
  - *From: smithyIAN - 4080ti Super 16gig*

- **Problem:** Whisper model loader breaking with symlinked folders
  - **Solution:** Create audio_encoders folder in models directory
  - *From: Slavrix*

- **Problem:** Out of memory errors on low RAM systems
  - **Solution:** Increase Windows paging file size to 80-96GB instead of default ~25GB. Most OOM issues are due to insufficient swap space, not actual RAM limitations
  - *From: Ablejones*

- **Problem:** RuntimeError about mismatched tensor sizes in WanVacePhantom
  - **Solution:** When using multiple WanVacePhantom nodes, put phantom/reference images only in the last node before sampler to avoid latent size conflicts
  - *From: Ablejones*

- **Problem:** HN and LN models flipped causing poor video quality
  - **Solution:** Double-check that High Noise and Low Noise models are correctly assigned in workflow - easy mistake that degrades results significantly
  - *From: Ablejones*

- **Problem:** Fireflies/confetti noise with gauss-legendre samplers
  - **Solution:** Set eta to 0.0, try different schedules/shifts, avoid steps that are too large
  - *From: Ablejones*

- **Problem:** Mouth movement during silent audio sections
  - **Solution:** Use better audio separation (Suno stems work better than open source), check for noise in vocal track during preview
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Dancing fireflies artifacts
  - **Solution:** Set ETA to ZERO or increase from 0.25 to fix dancing fireflies issue
  - *From: The Shadow (NYC)*

- **Problem:** Large steps causing artifacts
  - **Solution:** Decreasing shift may help, or increasing number of steps when using only a few steps
  - *From: Ablejones*

- **Problem:** Audio crop error with start/end time
  - **Solution:** Ensure start time is less than end time and within audio length bounds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** ComfyUI workflow loop dependency
  - **Solution:** Fixed duration approach (3.88s) avoids loop dependency between Transcribe node and TimecodeFromIndex node
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Mouth movement during silence
  - **Solution:** Audio noise can cause unwanted mouth movement - use songs with continuous vocals or reduce background noise
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Empty response from Gemini model
  - **Solution:** Pass API key into docker container as well as frontend, turn off screen saver, keep browser connected with credentials available
  - *From: samhodge*

- **Problem:** Lyrics not concatenated with LLM instructions
  - **Solution:** Use concat node to combine lyrics with system prompt instructions before sending to Gemini
  - *From: kendrick*

- **Problem:** Race condition in workflow execution
  - **Solution:** Connect string from Gemini node into negative prompt of first text encoder to prevent timing issues and ensure proper execution order
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Index reset required when stopping before first video completes
  - **Solution:** Reset index to 0 if you stop the workflow before the first video is done
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** AudioCrop error with start/end time
  - **Solution:** Set index to 0, error usually occurs when index is too high
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Missing PromptSplitter node after update
  - **Solution:** Delete current custom node folder and re-install via manager, node was moved to correct py file
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Index not advancing between runs on Windows WSL
  - **Solution:** Use absolute path format like A:\COMFY_UI\ComfyUI_windows_portable_nvidia\ComfyUI_windows_portable\ComfyUI\output\candyskiesV2
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Memory leak detected with WAN21_Vace model
  - **Solution:** Restart ComfyUI. Issue seems related to erroring during encode/sample then fixing workflow and continuing
  - *From: Gleb Tretyak*

- **Problem:** Poor results with phantom reference
  - **Solution:** Don't use same image for first frame and phantom reference. Use diverse reference images instead
  - *From: Gleb Tretyak*

- **Problem:** Workflow conflicts in manager showing old version
  - **Solution:** Manager installs latest nodes via git pull but doesn't update version display. Try update still works
  - *From: kendrick*

- **Problem:** Audio sync issues in longer videos
  - **Solution:** VRGameDevGirl84 identified timing issue between runs and is fixing it
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Transcription accuracy issues with non-English songs
  - **Solution:** Use context string feature to manually input correct lyrics for each run
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Audio sync issues in later parts of video
  - **Solution:** 
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Gray banner at top and bottom of video
  - **Solution:** 
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Character not matching reference image
  - **Solution:** 
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Video flashing at start
  - **Solution:** 
  - *From: Cseti*

- **Problem:** Character degradation in VACE extend process
  - **Solution:** 
  - *From: Ablejones*

- **Problem:** Motion and color degradation in extended videos
  - **Solution:** 
  - *From: garbus*

- **Problem:** No video output despite completion
  - **Solution:** 
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Index node not updating/staying at 0
  - **Solution:** Check file path format - use standard Windows path format without double escaping. Ensure output folder exists and is empty
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Audio sync restarting on each chunk
  - **Solution:** Usually user error with index node or file path configuration. Ensure no existing videos in folder when starting
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Black screen output with QwenEdit
  - **Solution:** Disable sage attention when using QwenEdit models, or check denoise is set to 1.0
  - *From: Trentino*

- **Problem:** Random pillar/letter boxing appearing
  - **Solution:** Appears randomly due to HUMO, no specific fix identified
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Unwanted mouth movement during non-vocal sections
  - **Solution:** Remove vocal/singing references from prompts, check for audio noise, or disconnect audio from HUMO for silent sections
  - *From: triquichoque*

- **Problem:** Inconsistent backgrounds across scenes
  - **Solution:** Fill context fields manually with consistent background descriptions, or use reference image with desired background
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Start index out of range error
  - **Solution:** Disconnect math expression node if connected, issue may resolve itself
  - *From: stas*

- **Problem:** LLM sending wrong number of prompts
  - **Solution:** Sometimes LLM sends 12 instead of 16 prompts, causing end segments to use only reference image
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Vace needs a base model to run but workflow errors
  - **Solution:** Original Vace model was released as full standalone (Wan 2.1 base + Vace blocks). Kijai separated Vace blocks requiring base model. Use full Vace model file for standalone operation
  - *From: Ablejones*

- **Problem:** Characters look more plastic in Wan output videos
  - **Solution:** May be caused by NSFW LORAs. Check if same issue happens with non-NSFW version. Can use reality LORAs or lower shift + Smartphone Snapshot Photo Reality STYLE lora
  - *From: Rusch Meyer/Phr00t*

- **Problem:** Audio sync issues in long videos
  - **Solution:** Different audio files have different samples causing sync issues. Need audio cleaning node. Some files work, some don't. Recording with Windows recorder works better
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Face detailer misalignment
  - **Solution:** Adjust mask with 'grow mask with blur' options or 'crop_size_mult' values when seeing edge of box
  - *From: Cseti*

- **Problem:** OOM on RAM with face detailer upscaling nodes
  - **Solution:** Bypass face detailer image upscale nodes or try different model. Issue is models not offloading
  - *From: Cseti*

- **Problem:** Auto-queue not working in V7
  - **Solution:** Only fails if files already in folder. Forward slashes on Windows cause issues - use regular file path copy/paste
  - *From: VRGameDevGirl84(RTX 5090)/hudson223*

- **Problem:** Auto-queue not working in fresh ComfyUI install
  - **Solution:** Install ComfyUI-Impact-Pack custom node from manager or GitHub (https://github.com/ltdrdata/ComfyUI-Impact-Pack)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** HuMoEmbeds tensor device mismatch error
  - **Solution:** Update both wan wrapper and VRGameDevGirl's custom nodes, use latest workflow version (V7.1)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Frame count mismatch - getting 97 frames instead of 100
  - **Solution:** Use 5-second duration instead of 4 seconds, or try 4.2 seconds (105 frames) to avoid rounding issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Workflow stopping mid-run with connection error
  - **Solution:** ConnectionResetError is usually just a blip and shouldn't stop runs. Check if too many videos in folder are causing confusion.
  - *From: hudson223*

- **Problem:** Torch compile error on last loop iteration
  - **Solution:** Change dimensions to multiples of 32 instead of 16 to fix RoPe function compile errors
  - *From: HeadOfOliver*

- **Problem:** Sync issue in workflow
  - **Solution:** Remove/fix audio crop node at the end of workflow that was causing timing problems
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Face changes too much during upscaling
  - **Solution:** Change start step to 5 instead of default 4 to denoise less, or use LoRA training on the face
  - *From: HeadOfOliver*

- **Problem:** RuntimeError with face detailer batch crop
  - **Solution:** Happens when no face detected in some frames, related to pagefile/CPU RAM issues
  - *From: NebSH*

- **Problem:** Rebooting PC results in faster generation
  - **Solution:** Something to do with ComfyUI rather than the workflow - restart helps
  - *From: smithyIAN - 4080ti Super 16gig*

- **Problem:** Video duration 3.88 seconds instead of 4
  - **Solution:** HuMo requires 4n+1 frames, so 100 frames gets rounded to 97. New system auto-adjusts UP to 101 frames = 4.04 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Torchaudio.save failing with permissions
  - **Solution:** Switch from torchaudio.save to soundfile.write
  - *From: triquichoque*

- **Problem:** FileNotFoundError when ffmpeg not installed
  - **Solution:** Updated node now has fallback that uses imageio's built-in ffmpeg automatically
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Triton cache path too long on Windows
  - **Solution:** Create shorter torch cache ENV PATH or delete cache content
  - *From: BestWind*

- **Problem:** Nodes cannot be moved in workflow
  - **Solution:** Right click and unpin - red pin was added to prevent users from breaking workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Background removal making face bad
  - **Solution:** Bypass the background remover nodes if reference image already has desired background
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** OOM on second pass with 5090
  - **Solution:** Use block swapping if you have enough system RAM, or reduce frame count
  - *From: Flipping Sigmas*

- **Problem:** OOM errors after adding ComfyUI-WanAnimatePreprocess
  - **Solution:** Remove the custom node that was recently added
  - *From: Maartificial_4090_24G*

- **Problem:** NoneType object has no attribute 'add_callback' error
  - **Solution:** Try disabling sage_attention and enable_fp16_accumulation
  - *From: Ablejones*

- **Problem:** Model and module confusion in workflow
  - **Solution:** Module goes into diffusion model selector, the model goes into model loader. Diffusion Model Loader needs full base model, not just extracted VACE blocks
  - *From: Ablejones*

- **Problem:** Random objects (planes, buildings) appearing in second pass
  - **Solution:** Turn down LoRA strength to 0.7, or turn off 'add noise to sampling' on low noise pass
  - *From: Flipping Sigmas*

- **Problem:** PyTorch 2.8.0 causing issues with 5090 on RunPod
  - **Solution:** Roll back to pytorch version 2.7.1+cu128
  - *From: Mazrael.Shib*

- **Problem:** Excessive tears in generation
  - **Solution:** Add 'NOTE: No tears, no crying!' under emotion setting in prompt creator node
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Time jump 11 frames before end of output
  - **Solution:** Happens when images are too similar. Try using different images or adjusting parameters
  - *From: happy.j*

- **Problem:** Second pass produces random weird characters
  - **Solution:** Use WanVacePhantomDualV2 node instead of regular dual node for better compatibility
  - *From: Ablejones*

- **Problem:** DWPose leaking into generation when combined with Depth
  - **Solution:** Send each control input as its own Vace input instead of using image blend screen at .5
  - *From: Ablejones*

- **Problem:** Character loses consistency in first 71 frames
  - **Solution:** Lower the SHIFT parameter on both Samplers to help retain likeness, experiment with higher total steps and start step
  - *From: thaakeno*

- **Problem:** OOM errors on longer generations
  - **Solution:** Enable the Block Swap node and set block swap to 30 for 24GB cards
  - *From: thaakeno*

- **Problem:** Outfit doesn't change despite multiple outfit values
  - **Solution:** Remove outfit from continuity instruction or add note in character input to override
  - *From: triquichoque*

- **Problem:** ImageResize node invalid data error in V9
  - **Solution:** Replace the invalid value with '1' for the per_batch input
  - *From: triquichoque*

- **Problem:** Latent upscaling ghosting
  - **Solution:** Use multiple smaller upscaling steps instead of x2 in one go, though this can cause tiling and blur
  - *From: mdkb*

- **Problem:** Model adds human faces to non-human characters like robots
  - **Solution:** Experiment with SHIFT parameter, higher steps, and create custom LoRAs for specific character types
  - *From: thaakeno*

- **Problem:** Square artifacts in half of video output
  - **Solution:** Switch resolution to dimensions divisible by 32 (like 1024x576 instead of 1280x720)
  - *From: Christian Sandor*

- **Problem:** OOM errors on newer ComfyUI versions
  - **Solution:** Issue identified as ComfyUI problem, not model-specific. Try using GGUFs or adjusting block swap settings
  - *From: patientx*

- **Problem:** Flash attention error with SeedVR2 on version 2.8.3
  - **Solution:** Revert to SDPA attention or use SeedVR2 v2.5.17 which should work without flash attention
  - *From: Adrien Toupet*

- **Problem:** ComfyUI crashing with 'Reconnecting' message
  - **Solution:** Try simpler native Wan workflows first, check if using correct ComfyUI version (not portable), reduce frame count and dimensions for testing
  - *From: brbbbq*

- **Problem:** VACE overshooting rotation in transitions
  - **Solution:** Issue occurs when start and end frames are identical - change end and start frames so they don't match to give VACE different points to interpolate between
  - *From: Bernie 'Hot Dog' Madoff*

- **Problem:** Lip movement when not wanting it
  - **Solution:** Don't use audio input or use empty audio input, don't use LightX lora or use at low strength, use CFG with negative prompt describing talking/lip movement for at least few steps, apply Lip Sync Suppressor node
  - *From: Ablejones*

- **Problem:** OOM errors with sequential generation workflow
  - **Solution:** Each segment runs independently so if you can run first segment you can run 500th. Often can just run WF again and it will pick up where left off since allocation error usually dumps VRAM
  - *From: Ablejones*

- **Problem:** Static images in extensions after fine initial generation
  - **Solution:** Issue was using wrong SVI model - switching back to correct model fixed it. Using 2.2 lora on model based on 2.1 (HuMo) caused problems
  - *From: aiacsp*

- **Problem:** Batches not matching at cut points when upscaling long sequences
  - **Solution:** Noise levels don't match between end of previous batch and start of next batch. No clear solution found yet
  - *From: Bernie 'Hot Dog' Madoff*

- **Problem:** VAE not found error in workflow
  - **Solution:** VAE wasn't named same and in same directory as workflow expected. Had to go in subgraph to change it or rename VAE file to match
  - *From: NebSH*

- **Problem:** Audio drift over time
  - **Solution:** Audio length needs to be exact multiple of frame count. VRGameDevGirl's HUMO workflow pads tiny amount of silence to make things land perfectly on frame boundaries
  - *From: hudson223*

- **Problem:** ComfyUI crashes during long generations
  - **Solution:** Use --no-cache argument or remove video preview nodes from workflow to prevent RAM issues
  - *From: Ablejones*

- **Problem:** Audio overlap causing lipsync issues
  - **Solution:** Audio encoder should be padded with silence and not have repeated audio, unlike video overlap
  - *From: hudson223*

- **Problem:** Wrong LoRA causing red/weird outputs
  - **Solution:** Use specific SVI LoRA from the workflow notes, not SVIv2 LoRA for low noise sampler
  - *From: Ablejones*

- **Problem:** Device mismatch error
  - **Solution:** Route 'denoised' output instead of 'output' from ClownsharkChainsampler
  - *From: Ablejones*

- **Problem:** ComfyUI Essentials compatibility
  - **Solution:** Switch to 'nightly' version in ComfyUI manager to fix math node issues
  - *From: Ablejones*

- **Problem:** WanImageToVideoSVIPro not working
  - **Solution:** Remove all kjnodes and reinstall them
  - *From: Henque*

- **Problem:** SimpleMath node error 'unexpected keyword argument c'
  - **Solution:** Switch ComfyUI_essentials to nightly version or replace with Math Expression node from ComfyUI Custom Scripts
  - *From: Ablejones*

- **Problem:** ComfyUI_essentials causing various node failures
  - **Solution:** Remove ComfyUI_essentials package entirely and replace nodes with alternatives from other packages
  - *From: mdkb*

- **Problem:** TextLineCounter node missing from WAS Node Suite
  - **Solution:** Delete WAS folder and manually git clone, or switch to nightly version
  - *From: Ivoxx*

- **Problem:** Video flashing/fading transitions with end frames
  - **Solution:** Use 2 frames instead of 1 for middle/first/last frames when they don't catch up properly
  - *From: Blink*

- **Problem:** Aggressive transition to last frame with Wan 2.2
  - **Solution:** Enable t2v lighting lora and adjust both lighting loras strength in high and low pass until finding sweetspot
  - *From: SL3ND3R*

- **Problem:** VAE is invalid error
  - **Solution:** Use Wan2_1_VAE_bf16.safetensors or wan_2.1_vae.safetensors from official repos
  - *From: Ablejones*

- **Problem:** Duration math node attached to batch instead of frame count
  - **Solution:** Rewire the duration math node to connect to frame count rather than batch
  - *From: hudson223*

- **Problem:** Sage attention tensor type errors with GGUF
  - **Solution:** Disable sage attention or ensure using sage attention 2++ with proper CUDA/PyTorch versions
  - *From: craftogrammer 🟢*

- **Problem:** Last frame not working in VACE workflows
  - **Solution:** Issue is with Fun VACE 2.2 models - switch to original Wan 2.1 VACE for better inpainting/frame control
  - *From: Ablejones*

- **Problem:** Static degraded animation after first generation
  - **Solution:** Was using wrong LoRA - needed to use correct SVI LoRA instead of SVI 2.0 Pro lora for humo-low noise
  - *From: Stef*

- **Problem:** Quality degrading in longer extensions
  - **Solution:** HuMo has harder time when subject moves farther away or is smaller in frame. Try increasing resolution of generation
  - *From: Ablejones*

- **Problem:** OOM issues on 12GB card with certain workflows
  - **Solution:** Use Wan 2.1 instead of 2.2, or put LoRA inline into standard KSampler with proper HI/LO conditioning manipulation
  - *From: atom.p*


## Model Comparisons

- **Current VACE vs SkyReels DF model**
  - VACE shows huge improvement - can fix both color shift AND quality degradation that SkyReels DF couldn't handle
  - *From: Ablejones*

- **res_2m vs res_2s sampler**
  - res_2m has similar to normal sampler time, res_2s is slower but potentially better quality
  - *From: Ablejones*

- **RIFE vs other interpolation**
  - RIFE is faster for frame interpolation
  - *From: Rishi Pandey*

- **TensorRT vs standard processing**
  - TensorRT interpolates 300 frame video in 2 seconds, significantly faster
  - *From: Ablejones*

- **Hunyuan Vid vs WAN training data**
  - Hunyuan Vid's training dataset seemed more cinematic (possibly torrented movies), does random but accurate cuts/scene changes
  - *From: JohnDopamine*

- **VACE vs VEO on volcano/family scenes**
  - VEO volcano effect worse than VACE, but VEO better for family on bench scene
  - *From: fredbliss*

- **FusionX upscaling vs Topaz**
  - Results just as good as Topaz for upscaling 480p to 1920x1080
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX vs 30 steps base**
  - LightX gives less real look, nuked prompt adherence compared to 30 steps
  - *From: pom*

- **Native vs Wrapper performance**
  - Native node workflow runs twice as fast as Kijai's Wrapper
  - *From: Dakhari*

- **LCM/DDIM_uniform vs uni_pc/simple**
  - Got better results using LCM/DDIM_uniform combo, but could have been tweaking the lora strength/VACE embed
  - *From: Faust-SiN*

- **NormalCrafter vs Lotus for normals**
  - NormalCrafter has less flickering than Lotus
  - *From: Gateway {Dreaming Computers}*

- **Preview Animation vs VideoHelperSuite nodes**
  - Preview Animation nodes are lighter and reduce CPU usage significantly
  - *From: garbus*

- **UniPC vs LCM with Phantom**
  - UniPC produces amazing results with FusionX Phantom model, while LCM usually worked better with just Phantom + LightX
  - *From: trax*

- **Pusa vs regular VACE for extensions**
  - Pusa kills motion when combined with LightXv2 but adding reward, motion boost, movie gen LoRAs brings motion back
  - *From: Hashu*

- **res_2s vs Euler sampling**
  - res_2s provides dramatic quality jump over Euler, should only be 2x slower, so 5 steps res_2s takes about same time as 10 steps Euler
  - *From: Ablejones*

- **Vace + Phantom vs adding Wan2.2**
  - Vace + Phantom using Wan2.1 work perfectly together. Adding Wan2.2 is much more difficult because we don't have proper models for that yet
  - *From: Ablejones*

- **Janky Memory Patcher vs Block Swapper**
  - It's not like block swapper, it's not better, it's just another tool with different mechanism
  - *From: Ablejones*

- **Multi samplers with VACE vs Wan2.2 i2v for chaining**
  - Wan2.2 i2v can handle chaining samplers with flawless transitions, while VACE has noticeable changes in first frame when chaining
  - *From: the_darkwatarus_museum*

- **Fun Control 2.2 vs VACE for extensions**
  - Fun Control 2.2 is definitely better, especially for scenes with huge color changes
  - *From: Ablejones*

- **CausVid vs LightX2V**
  - CausVid has better likeness but weaker overall quality, LightX2V hurts likeness but better aesthetic
  - *From: MarkDalias*

- **Euler vs other samplers**
  - Euler leaves graininess, uni_pc or res_multistep are same speed and much sharper
  - *From: Ablejones*

- **V1 vs V2 model for pose control**
  - V2 model fixes pose rig showing through, V1 has this issue more often
  - *From: Piblarg*

- **Various samplers performance**
  - gauss_legendre_2s works well for extensions, res_2s and other 2s samplers may work well too but faster, qin_zhang_2s slower but nice quality
  - *From: Ablejones*

- **HuMo vs Infinite talk**
  - HuMo results are quite impressive, at least as good as Infinitetalk, but context windows don't work with HuMo
  - *From: JmySff*

- **lobatto_iiid_3s vs ddim sampler quality**
  - Significant quality improvement with 3s sampler but much slower (3 model calls per step vs 1)
  - *From: Ablejones*

- **Linear quadratic vs beta scheduler for low steps**
  - Linear quadratic more appropriate for 4-8 steps, complex schedulers lose benefits at low step counts
  - *From: Ablejones*

- **Suno stems vs open source audio separation**
  - Suno stems provide better quality separation and help reduce mouth movement during silent sections
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN 2.2 v10 vs Mega versions for I2V**
  - v10 has dedicated I2V model that's better at keeping features from original image, while Mega versions based on VACE T2V are more capable and flexible but Mega has less I2V noise
  - *From: Phr00t*

- **HUMO vs InfiniteTalk**
  - HUMO produces better results than InfiniteTalk for lip sync, especially with WAN 2.2, though limited to shorter durations typically
  - *From: Juan Gea*

- **Q6 GGUF vs checkpoint quality**
  - Q6 GGUF should be almost same as checkpoint quality, low quality may be due to other settings
  - *From: Trentino*

- **Phantom reference vs Vace reference**
  - Phantom reference is much better at reference than Vace reference
  - *From: Ablejones*

- **2.2 5b vs 14b HN/LN models**
  - Community doesn't think 5b is significant compared to 14b HN/LN, 5b doesn't have similar controls for endless travel
  - *From: The Shadow (NYC)*

- **Audio scale 2.0 vs 1.0**
  - 1.0 works better for less 'shouty' characters, 2.0 can make heads look like they'll 'flip open'
  - *From: samhodge*

- **Vace + Phantom merge vs 2.2 workflows**
  - Vace + Phantom merge works better for character consistency, though prompt adherence may be weaker than 2.2
  - *From: Gleb Tretyak*

- **New V6 workflow vs V5**
  - V6 has better clarity with pusa lora removed, more customizable with new prompt creator
  - *From: kendrick*

- **Fun 2.2 Vace vs regular Vace**
  - Fun 2.2 Vace much better at following OpenPose conditioning
  - *From: Ablejones*

- **Krea1 vs Flux images as reference**
  - Krea1 images produce more realistic results than Flux images which look fake
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.1 vs Wan 2.2 face consistency**
  - Wan 2.1 face changes completely, Wan 2.2 retains face better but is very slow
  - *From: Santoshyandhe*

- **LightX alone vs LightX + FastWan**
  - LightX + FastWan is 2.2x faster (31.49s vs 70.63s) at 4 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **4 steps without FastWAN vs with FastWAN**
  - Without FastWAN gives more cinematic, natural results but takes longer
  - *From: VRGameDevGirl84(RTX 5090)*

- **QwenEdit AIO vs regular Qwen 2509**
  - AIO looks better overall but sometimes adds unwanted skin details, regular model is blurrier but cleaner
  - *From: Tachyon*

- **WAN 2.1 vs WAN 2.2 with fast LoRAs**
  - 2.1 still preferred in many cases due to slow motion issues with fast LoRAs on 2.2
  - *From: kendrick*

- **Individual run segments vs final combined video**
  - Individual segments like video_00003-audio.mp4 maintain sync almost perfectly, while final combined video has sync issues
  - *From: WackyWindsurfer*

- **WAN vs closed models (Ray3, Veo3)**
  - Closed models have less temporal flickering/popping in details like hair and textures compared to WAN
  - *From: HeadOfOliver*

- **Different languages for lip-sync**
  - Chinese and French produce more natural lip-sync results than English, likely due to phoneme training data
  - *From: Janosch Simon*

- **Claude vs ChatGPT for coding**
  - Claude is much better at solving code problems that ChatGPT fumbles around
  - *From: Scruffy*

- **New lightx2v lora vs standard**
  - New lora has better quality at 4 steps but is slower, sometimes loads sometimes not
  - *From: Chandler ✨ 🎈*

- **1024x576 vs 1280x720**
  - Takes same amount of time as 1280x720, so 1024x576 not worth doing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Q4_K_M vs larger models**
  - Q4_K_M works well for 16GB VRAM, but if you have more VRAM use bigger models for better results
  - *From: Cseti*

- **WAN 2.2 vs Phantom for character consistency**
  - WAN 2.2 basically breaks phantom, could not see a benefit
  - *From: Piblarg*

- **Phantom vs VACE for product replication**
  - Phantom is amazingly good at accurately replicating products from references
  - *From: Ablejones*

- **Gemini 2.5 vs other models for video understanding**
  - Gemini 2.5 overall has the best video understanding from any model currently (besides GPT 5 which has video analysis turned off)
  - *From: thaakeno*

- **HuMo vs Wan 2.2 S2V**
  - HuMo works much better for lip sync, Wan S2V produces poor quality results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.1 vs 2.2**
  - Wan 2.2 is definitely better quality than 2.1
  - *From: xwsswww*

- **Phr00t's AIO vs full Wan 2.2**
  - AIO cuts out high model for speed/simplicity which degrades motion, but sits between Wan 2.1 and full 2.2 in quality
  - *From: Phr00t*

- **LightX LoRA vs standard settings for lip movement**
  - LightX LoRA causes almost unavoidable lip movements, standard CFG settings with negative prompts work better for preventing unwanted speech
  - *From: Ablejones*

- **Wan 2.2 A14B I2V Low Noise vs Wan 2.1 I2V models**
  - 2.2 I2V LN model is not same or similar to 2.1 I2V-480p or 720p models. The 2.2 I2V LN model cannot generate video by itself, needs HN stage
  - *From: Ablejones*

- **RTX 5090 performance with Wan models**
  - Takes 85sec to gen 81 frames at 720x720 with 5090
  - *From: burgstall*

- **Wan 2.1 1.3B vs 14B**
  - 1.3B version is pretty bad compared with 14B, but works on 12GB cards
  - *From: ingi // SYSTMS*

- **This workflow vs other lipsync solutions**
  - Haven't found anything that comes close to this workflow in regards to flexibility and creative direction
  - *From: Mr_J*

- **GGUF vs FP8 performance**
  - GGUF: 10:44 execution time, 14.2GB VRAM avg. FP8: 12:28 execution time, 15.5GB VRAM avg. GGUF uses less VRAM but slightly faster
  - *From: craftogrammer 🟢*

- **Kijai wrapper vs default ComfyUI nodes for VACE**
  - Default ComfyUI nodes recommended for VACE - better memory usage and performance, Kijai has worse performance and requires manual blockswap
  - *From: Blink*

- **Wan 2.1 vs 2.2 for end frame transitions**
  - Wan 2.2 known for aggressive transitions to last frame, may need lora adjustments
  - *From: SL3ND3R*

- **Wan 2.1 vs Wan 2.2**
  - Wan2.1 is 99.9% as good if not better than 2.2 if you do a second sampler pass, and uses less VRAM
  - *From: Flipping Sigmas*

- **Fun VACE 2.2 vs Original VACE 2.1**
  - Fun VACE 2.2 better at pose control and high noise compatibility, but original VACE better at inpainting tasks
  - *From: Ablejones*

- **WanVaceAdvanced nodes vs Native nodes**
  - Same output when settings are equal, but Advanced nodes provide more control over reference frame strength and easier setup
  - *From: Ablejones*


## Tips & Best Practices

- **Use lower VACE strength for more motion in subsequent passes**
  - Context: Set VACE strength to 0.8-0.9 on additional segments (not first) to allow more motion
  - *From: Kaïros*

- **Use minimal phrasing for segments**
  - Context: Since this mode retains visual information, use simple action descriptions like 'The man turns left and opens the door'
  - *From: TK_999*

- **Direction-type prompts work best**
  - Context: Focus on directional/action prompts rather than complex scene descriptions when using continuation
  - *From: JohnDopamine*

- **Fix aspect ratio before processing**
  - Context: Use resize node or manual adjustment to fix aspect ratio issues
  - *From: JohnDopamine*

- **Use context of 20 for smoother transitions**
  - Context: Dial up context to 20 frames instead of default 10 for better transitions between segments
  - *From: pom*

- **Vary seeds only for terminal tracking**
  - Context: Varying seeds between generations helps track progress in terminal but doesn't affect generation quality
  - *From: Ablejones*

- **Add more prompts to each segment for better results**
  - Context: When doing long form i2v with multiple segments
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use ChatGPT to create sequential prompts**
  - Context: Give it the start image and have it create continuation prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Hook up control_masks inputs**
  - Context: Unless leaving them out for specific reason - prevents continuation frames from changing too much
  - *From: Ablejones*

- **Start simple and save workflows before adding complexity**
  - Context: When experimenting with new techniques
  - *From: Gateway {Dreaming Computers}*

- **Remove 'fixes' that may be making things worse**
  - Context: Sometimes original simple approach works better
  - *From: Ablejones*

- **Use low denoise (0.6) for upscaling**
  - Context: When wanting to preserve logo/text details
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use image2image on first frame of control video to style transfer**
  - Context: When using inputs that are very different from desired output style
  - *From: Faust-SiN*

- **Start with very low resolution and high teacache for fast base generation**
  - Context: When wanting to speed up workflow with upscaling approach
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use select_every_nth frame instead of speed changes in external editor**
  - Context: When wanting to effectively use every other frame for processing
  - *From: TransformerMan*

- **Use NAG for negative prompting since normal method doesn't work with CFG zero**
  - Context: When CFG is set to zero in Wan workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Allow video model freedom to use only frames it generates to continue**
  - Context: For more natural motion in long video generation
  - *From: Ablejones*

- **Don't use FusionX for upscaling**
  - Context: When doing upscaling workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Keep seed and shift consistent throughout generations**
  - Context: For successful video extensions with Pusa
  - *From: Hashu*

- **Use collage images for multiple characters in Phantom**
  - Context: Phantom limited to 4 images but can use collages of multiple characters per image slot
  - *From: Ablejones*

- **Reduce VACE strength at later steps for better results**
  - Context: When experiencing darkness or inpainting weirdness
  - *From: Piblarg*

- **Don't cast fp8_e4 to fp8_e5**
  - Context: You lose precision on model weights for no benefit
  - *From: Ablejones*

- **Try 12 steps minimum with Euler sampler**
  - Context: For better quality when using Euler instead of res_2s
  - *From: Ablejones*

- **For I2V with Vace, send starting image as first frame without mask, then grey values to other frames with masks**
  - Context: When doing image-to-video with VACE
  - *From: Ablejones*

- **Use openpose without Face points to help with character likeness**
  - Context: When control inputs affect character resemblance
  - *From: Ablejones*

- **Try running Lightx2v/lightning loras at strength=0.5 and CFG=2.0 if CFG=1.0 worsens Phantom resemblance**
  - Context: When using speed loras with VACE+Phantom
  - *From: Ablejones*

- **Send same image multiple times for Phantom subject to potentially improve resemblance**
  - Context: When trying to enhance character likeness
  - *From: Ablejones*

- **Use ImageAndMaskPreview node with opacity 0.4 and red color to visualize mask outputs**
  - Context: For debugging mask positioning
  - *From: Ablejones*

- **Crop characters images similar to the pose you want - do closeup if you have closeup**
  - Context: When creating reference collages for VACE
  - *From: Piblarg*

- **Good prompting and getting trigger phrase for character is important**
  - Context: For better character consistency
  - *From: Piblarg*

- **Use loras more as steps go up**
  - Context: When working with character loras on phantom base
  - *From: Piblarg*

- **Blur background more in post to hide distant face issues**
  - Context: When faces at distance break during camera zoom at 16fps
  - *From: mdkb*

- **Use higher strengths for openpose with HN model**
  - Context: Openpose needs higher strengths to work with HN model and VACE
  - *From: Ablejones*

- **Start with causvid for first few steps and lightx for the last bit**
  - Context: Get best of both worlds for speed and quality
  - *From: Piblarg*

- **Increase CFG, resolution, and steps for better face consistency**
  - Context: When losing face resemblance with speed optimizations
  - *From: Ablejones*

- **Use manual face masking in Blender with grease pencil**
  - Context: For better control than AI segmentation, can interpolate between frames
  - *From: xwsswww*

- **Use 'combined' setting when you only have one mask - it won't make a difference**
  - Context: When working with MASK to SEGS nodes
  - *From: Ablejones*

- **Replace 'For Video' with 'For AnimateDiff' in your head**
  - Context: The 'For Video' naming is confusing, sometimes you want to use it most of the time you don't
  - *From: Ablejones*

- **Don't have to pass model and conditioning each time unless changing it**
  - Context: When using ChainSampler nodes
  - *From: Ablejones*

- **Phantom prefers simple but real background, VACE reference likes white background**
  - Context: When preparing reference images
  - *From: Ablejones*

- **Send Phantom references as two images in a batch separately instead of concatenated**
  - Context: Better approach than making one concatenated image
  - *From: Ablejones*

- **Prompt is really important for extension workflows**
  - Context: Model is kicked in specific direction, conflicting prompts cause weird results
  - *From: Ablejones*

- **Use spline lines instead of straight lines for easier workflow visualization**
  - Context: Makes it easier to see what's connected in complex workflows
  - *From: Ablejones*

- **Use --cache-none mode for very long workflows**
  - Context: When running complex workflows that use many techniques and might fail due to memory issues
  - *From: Ablejones*

- **Bypass FastWAN LoRA when using 4 steps**
  - Context: For 4-step generation workflows, removing the speed LoRA can improve results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use native ComfyUI LoRA scheduling with Set/Get nodes**
  - Context: Create 'before LoRA' and 'after LoRA' model states using Set nodes, then use Get nodes to apply different LoRA strengths to different samplers
  - *From: JalenBrunson*

- **Change background throughout generation to reduce degradation**
  - Context: Varying the scene during video generation helps prevent progressive control degradation, though doesn't eliminate it completely
  - *From: Ablejones*

- **Use Banostasis with specific prompt format**
  - Context: Start prompt with 'Banostasis concept,' and use 0.45-1.0 strength depending on what looks good with sampler
  - *From: The Shadow (NYC)*

- **Separate HN and LN passes for better control**
  - Context: Allow early HN steps without distill loras and with CFG 3-3.5 for more stylized aesthetics before applying speed optimizations
  - *From: The Shadow (NYC)*

- **Use pad instead of crop for image resize**
  - Context: When starting with square or portrait reference photos to avoid cutting off top of head
  - *From: kendrick*

- **Pre-generate prompts instead of using LLM nodes**
  - Context: Create prompts with GPT/Gemini beforehand separated with | symbol to avoid randomness in long generations
  - *From: Vérole*

- **Use default 1.0 strength values for Vace**
  - Context: When starting with the Phantom merge
  - *From: Ablejones*

- **Don't add Vace reference unless you have specific reason**
  - Context: When using Phantom merge, use Phantom references like normal
  - *From: Ablejones*

- **Test Phantom example workflows first before adding Vace**
  - Context: Before combining Phantom and Vace functionality
  - *From: Ablejones*

- **Set Vace strength of Phantom frames to 0.0**
  - Context: When using Vace merge, Phantom frames need Vace strength but it's automatically set to 0.0 in background
  - *From: Ablejones*

- **Ensure only one video in result folder**
  - Context: Important for workflow to function properly
  - *From: Janosch Simon*

- **Reset index to 0 and clear output folder for new composition**
  - Context: When starting a new song/composition
  - *From: kendrick*

- **Read all the notes before running the workflow**
  - Context: Multiple users missed important configuration details
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use diverse reference images for phantom merge**
  - Context: When using vace + phantom merge for character consistency
  - *From: Gleb Tretyak*

- **Add 'multiple people' to negative prompt**
  - Context: When using phantom merge to improve character consistency
  - *From: Gleb Tretyak*

- **Don't change control after generation setting**
  - Context: Users should leave it on fixed to avoid issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use tile sizes that don't evenly divide latent size**
  - Context: For upscaling to avoid bad seams - want overlap at edges
  - *From: Clownshark Batwing*

- **Queue runs right away, don't wait for completion**
  - Context: You can queue all runs immediately for automated processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use headshot or upper body shot for reference images**
  - Context: Full body shots where head is very small don't work well as reference
  - *From: VRGameDevGirl84(RTX 5090)*

- **Longer overlaps improve video quality**
  - Context: Making overlaps longer gives the model more to work with for better results
  - *From: ingi // SYSTMS*

- **Use JSON format for LLM prompts**
  - Context: JSON format helps LLMs maintain consistency and structure, especially for lesser models
  - *From: Scruffy*

- **Keep prompts simple for character descriptions**
  - Context: Just use 'the woman' or 'the man' instead of detailed descriptions - let reference image handle character details
  - *From: VRGameDevGirl84(RTX 5090)*

- **Check output folder if video doesn't display**
  - Context: Sometimes nodes don't show the video preview but the file is created in the output folder
  - *From: VRGameDevGirl84(RTX 5090)*

- **Match reference image aspect ratio to video**
  - Context: Similar aspect ratios between reference and output produce better results
  - *From: Santoshyandhe*

- **Start with empty folder and only add image and song to workflow**
  - Context: When troubleshooting workflow issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Queue all runs at once instead of waiting between runs**
  - Context: For multi-run videos, queue all runs immediately after seeing the run count
  - *From: VRGameDevGirl84(RTX 5090)*

- **Keep face detailer LoRA strength at 1**
  - Context: Higher values will look strange
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use 2-3 sentences for prompting**
  - Context: For QwenEdit models, doesn't need to be fancy
  - *From: Phr00t*

- **Remove example references from instruction prompts**
  - Context: LLM tends to overuse any examples provided in instructions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use context options node to fit larger upscales in 16GB VRAM**
  - Context: When doing upscaling passes
  - *From: Cseti*

- **Use headshot only in reference image for HuMo**
  - Context: HuMo tends to follow reference image strongly, full body nude references will override clothing prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt explicitly to avoid unwanted hallucination**
  - Context: When experiencing unwanted artifacts or changes
  - *From: Cseti*

- **Resolution has higher impact than steps**
  - Context: For video generation quality vs speed tradeoffs
  - *From: hudson223*

- **480p gets crunchy textures that don't filter out easily**
  - Context: 1280 or 1024 resolution handles upscaling better
  - *From: hudson223*

- **Add film grain lightly to HN results**
  - Context: Helps LN model grip and polish better in dual model workflows
  - *From: mdkb*

- **Try 1600x900 resolution for fixing faces at distance**
  - Context: 900p fixes faces where 720p doesn't always work
  - *From: mdkb*

- **Use headshot reference images for better character consistency**
  - Context: Face can get lost with full body shots, headshots maintain character better in HuMo workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **Keep character descriptions minimal**
  - Context: Too much detail in character description makes result look less like reference image
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fix seeds for audio generation to prevent changes between passes**
  - Context: When generating audio in same workflow, fixed seeds prevent audio regeneration that could break sync
  - *From: Chandler ✨ 🎈*

- **Use higher shift values for better motion freedom**
  - Context: Shift of 9+ gives model more freedom for complex scenes like dynamic motion
  - *From: ingi // SYSTMS*

- **1024x576 is sweet spot resolution**
  - Context: Good balance of quality and performance for video generation
  - *From: hudson223*

- **Use headshot photo for best character consistency**
  - Context: When using reference images, headshots work better than full body shots
  - *From: VRGameDevGirl84(RTX 5090)*

- **Don't describe character details in prompt for consistency**
  - Context: Just say 'the woman' or 'the man' to maintain same person throughout video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Test default workflow before making changes**
  - Context: Workflow is complex and changes can break functionality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use context strings to inject LoRA keywords**
  - Context: Works for adding specific styling or effects
  - *From: Chandler ✨ 🎈*

- **Go as high as possible with batch size for consistency**
  - Context: All frames within batch will be temporally consistent
  - *From: Adrien Toupet*

- **Clear folder before starting fresh run**
  - Context: Prevents merging videos from previous runs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use different camera angles between scenes to make cuts less noticeable**
  - Context: Since each generation starts with reference image, vary camera zoom/angle in prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Add extra notes to prevent unwanted elements**
  - Context: In prompt creator last string, hit enter then add 'Extra Notes: No tears, no crying' etc.
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use simpler character descriptions with reference images**
  - Context: Less detail pulls less away from reference image, let the ref image do the work
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use strict cycle for scene consistency**
  - Context: For news anchor or consistent scenes, change list handling to use strict instead of free interpretation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use block swap 20 and 8 steps for high resolution**
  - Context: When using 1280x720 or higher resolutions on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **Avoid negative prompting in positive prompts**
  - Context: Good chance it will add the things you tell it not to add
  - *From: VRGameDevGirl84(RTX 5090)*

- **Keep outfit descriptions simple**
  - Context: Each group is only 4 seconds, too much detail leaves no room for other elements
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use context string for custom prompts**
  - Context: Set 'Use context only' to true and connect lyric string to prompt splitter, can turn LLM off
  - *From: VRGameDevGirl84(RTX 5090)*

- **Set Extra Trim to 0 for exact end frame landing**
  - Context: When trying to loop videos, bypass 'Remove End Frame' subgraph node
  - *From: Ablejones*

- **Use 'the woman' instead of detailed character descriptions for better consistency**
  - Context: When prompting for character consistency across scenes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use two reference images - one full body with outfit, one close up**
  - Context: For better character and clothing consistency
  - *From: VRGameDevGirl84(RTX 5090)*

- **Delete last frame from inputs to second sampler for better motion**
  - Context: So the second sampler runs without the last frame guiding it, just continues the trajectory set from the first sampler
  - *From: Ablejones*

- **Try gens without a prompt at all for unexpected results**
  - Context: For more creative and abstract transitions
  - *From: ingi // SYSTMS*

- **Match pose resolution carefully - sometimes you want thicker skeletons**
  - Context: When using DWPose with different video resolutions
  - *From: Ablejones*

- **Add pure silence for b-roll shots to prevent blabbering**
  - Context: When creating music videos with instrumental sections
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use Google AI Studio to create better studio-style headshots and full body shots**
  - Context: For improving reference image quality before generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use 'first to last frame' or control video inputs for lots of motion**
  - Context: When you want specific motion that you're looking for
  - *From: Phr00t*

- **Describe background in every prompt for better backgrounds**
  - Context: When backgrounds look too basic or simple
  - *From: VRGameDevGirl84(RTX 5090)*

- **Add 'rapping' to HuMo prompts for more realism**
  - Context: When creating rap or music videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **Describing the position helps with OpenPose**
  - Context: When OpenPose isn't picking up smaller figures in frame
  - *From: Piblarg*

- **Try bumping shift value on low noise sampler up for artifacts**
  - Context: When getting square artifacts in video output
  - *From: Flipping Sigmas*

- **Use dimensions 1024x576 for best results**
  - Context: Standard resolution that works well across workflows
  - *From: Charlie*

- **For prompts that need to indicate silence, use 'standing silently' vs just 'standing'**
  - Context: When suppressing lip sync - 'standing' prompt still had lip movement while 'standing silently' did not with node active
  - *From: Chandler ✨ 🎈*

- **Remove any mention of speaking from prompt when using HuMo**
  - Context: Let HuMo add it itself when it needs to, helps with long silences
  - *From: Ablejones*

- **Don't connect conditioning or model inputs to ChainSampler nodes unless changing them**
  - Context: LATENT output line carries information from previous node
  - *From: Ablejones*

- **Set cond_retain_index_list to 0 for I2V with context windows**
  - Context: Keeps the reference for I2V going through context windows
  - *From: Ablejones*

- **Use cache none for long workflows**
  - Context: Otherwise they won't work without gigantic amounts of RAM
  - *From: Gleb Tretyak*

- **Try reducing prompt complexity for difficult subjects**
  - Context: For subjects like Shrek with large mouth movements, change prompt to 'mumbling' instead of 'speaking' and reduce HN steps from 3 to 2
  - *From: Ablejones*

- **Drop a step on the 1st sampler to improve movement and lip movement**
  - Context: Especially effective for non-realistic images
  - *From: Mr_J*

- **Change ETA levels to affect movement**
  - Context: Can help control motion dynamics
  - *From: Mr_J*

- **Prompt better and prompt for motion to improve dynamics**
  - Context: Try different seeds if specific segment doesn't have good lip sync
  - *From: Ablejones*

- **Use original image looking directly into lens**
  - Context: Important for preventing odd eye movements during generation
  - *From: NC17z*

- **Add audio delay at output for better sync**
  - Context: Default 0.2s delay can be adjusted as necessary
  - *From: Ablejones*

- **Save video and reload to continue extensions**
  - Context: When making very long videos beyond hardware limits
  - *From: Ablejones*

- **Use at least 5 frame overlap for smooth transitions**
  - Context: Otherwise Vace doesn't know how to handle video pacing
  - *From: ingi // SYSTMS*

- **Use show anything node to debug math node values**
  - Context: When troubleshooting math node connections and values
  - *From: hudson223*

- **Check each segment for lip sync quality before proceeding**
  - Context: HuMo's lip sync performance is very seed-dependent, requires iteration on prompt and seed
  - *From: Ablejones*

- **Use empty audio and concat audio nodes for audio padding**
  - Context: When needing to add silence at start of audio clips
  - *From: Gleb Tretyak*

- **Switch ComfyUI node packages to nightly to avoid version issues**
  - Context: Manager silently downgrades packages causing node compatibility issues
  - *From: Ablejones*

- **Post-process extensions to smooth transitions**
  - Context: A little VFX work helps smooth out extension artifacts between segments
  - *From: hudson223*

- **Use different LoRA types for different model sections**
  - Context: Use High Noise Wan 2.2 Lora for HN sections, Wan2.1 lora for LN section (HuMo)
  - *From: Ablejones*

- **Calculate video segments using division**
  - Context: If each segment is 3.8 seconds, divide total audio duration by 3.8 to get number of segments needed
  - *From: Ablejones*

- **Trim final segment silence using frame manipulation**
  - Context: Use 'Frames Slice' node and set stop frame as audio duration / frame rate to remove silence
  - *From: Ablejones*

- **Move Set Output_Video node to control workflow end point**
  - Context: Move node to where you want video to end and mute remaining groups
  - *From: Ablejones*


## News & Updates

- **Kijai working on tiled wan sampler**
  - Patch available for tiled wan sampler with VRAM saving benefits, tested on 4K+ upscale
  - *From: .tarkan*

- **Updated LLM nodes released**
  - Pushing update to LLM nodes for orchestrating scene/director prompts
  - *From: fredbliss*

- **Experimental Args and SLG nodes are not working**
  - Made comparison in AE in Difference overlay and confirmed they can be safely deleted
  - *From: N0NSens*

- **VACE Native implementation working**
  - Native VACE support now available in ComfyUI
  - *From: The Shadow (NYC)*

- **New Wan2.2 low steps model with CausVid merge**
  - CausVid v2 merged at 1.0 strength for better performance
  - *From: Piblarg*

- **Test version of 2.2 high model released**
  - Available on Civitai for testing
  - *From: crinklypaper*

- **Wan 2.2 5B version released**
  - Available on Civitai
  - *From: crinklypaper*

- **Kinestasis stop motion LoRA released for Wan 2.2**
  - Trained for stop motion effects, only use on high noise sampler, sensitive to prompt structure
  - *From: Cseti*

- **Modified Impact Pack fork available for video detailing**
  - Enables SEGS detailer functionality with Wan video models
  - *From: Ablejones*

- **New version of High 2.2 model released**
  - Available on Civitai, fixes many issues with the previous version
  - *From: crinklypaper*

- **Kijai has Infinite talk working in native**
  - Hard time using with VACE but confirmed working, will be implemented in native eventually
  - *From: Piblarg*

- **Phr00t released WAN 2.2 Mega Rapid AIO v3 with NSFW merge**
  - Updated NSFW LoRA set and strengths, recommends euler_a/beta instead of ipndm/beta
  - *From: Phr00t*

- **Ablejones submitted PR for ComfyUI i2v improvements**
  - Modified Humo model code for proper i2v support, submitted as GitHub PR #10034
  - *From: Ablejones*

- **Bytedance Lynx model released**
  - New model from same company as Phantom but different team, claims to beat Phantom and MagRef in face preservation
  - *From: MarkDalias*

- **Phr00t's AllInOne model list**
  - Posted comprehensive list of models and LoRAs included in WAN2.2-14B-Rapid-AllInOne
  - *From: Phr00t*

- **VRGameDevGirl nodes updated to version 3.0.0**
  - Major update with new workflow, old workflows will no longer work, includes automatic index detection based on existing videos in folder
  - *From: VRGameDevGirl84(RTX 5090)*

- **New workflow makes index management automatic**
  - Workflow now automatically knows what index should be based on how many videos already created in folder path
  - *From: VRGameDevGirl84(RTX 5090)*

- **V6.2 workflow released with auto-queue functionality**
  - New node automatically queues middle runs, reducing manual intervention
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt creator node in development**
  - Highly customizable node for camera motion, lighting, character interactions, and more
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN 2.2 'Mega' Rapid AIO v5 released**
  - Plus NSFW merge version available
  - *From: Phr00t*

- **Pins working for important messages**
  - Pom helped get pinning functionality working for the channel
  - *From: VRGameDevGirl84(RTX 5090)*

- **Extended frame support discovered**
  - Frame count can now go up to 121 frames (5 seconds) instead of previous 3.88 second limit
  - *From: VRGameDevGirl84(RTX 5090)*

- **New prompt creator nodes in development**
  - New nodes being developed to automate prompt creation, making workflow more user-friendly
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio sync fixes implemented**
  - Found and fixed audio sync issues that occurred in later parts of videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN 2.2 Mega Rapid AIO v6 uploaded**
  - New version of the all-in-one model available
  - *From: Phr00t*

- **No VACE 2.2 planned according to KJ**
  - Only extracted VACE module will be available, no full 2.2 version
  - *From: Lumifel*

- **New auto-queue nodes in development**
  - VRGameDevGirl84 working on nodes that auto-queue middle runs, only requiring 1-2 manual runs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio sync issues being fixed**
  - Active work on resolving audio drift across video segments
  - *From: VRGameDevGirl84(RTX 5090)*

- **DC-AI team might release DC Videogen Wan2.1 version for faster processing**
  - No Wan2.2 version in sight
  - *From: yi*

- **KWAI team released UniMMVSR paper with similar method**
  - Timing coincidence with community development
  - *From: yi*

- **VRGameDevGirl84 published new V7 workflow with updated nodes**
  - Old workflow should still work but V7 recommended
  - *From: VRGameDevGirl84(RTX 5090)*

- **V7.1 workflow released with sync improvements**
  - Updated workflow with improved lip-sync (though not fully fixed) and updated node annotations available at GitHub
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phr00t WAN 2.2 Mega Rapid AIO v7 uploaded**
  - Both NSFW and SFW mega versions v7 are now available
  - *From: Phr00t*

- **Sync issue 100% fixed in upcoming workflow**
  - Audio crop node was causing timing problems, now resolved
  - *From: VRGameDevGirl84(RTX 5090)*

- **New lightx2v LoRA released**
  - Available at huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/tree/main/loras
  - *From: Chandler ✨ 🎈*

- **SeedVR2 updated with noise options in nightly**
  - New noise controls to reduce artifacts, will be deployed to main soon
  - *From: Adrien Toupet*

- **Chinese expert optimizing HuMo model**
  - Top expert in China working on improved model with better character consistency
  - *From: dashixiong*

- **Node updated with ffmpeg fallback**
  - Fixed FileNotFoundError by adding automatic fallback to imageio's built-in ffmpeg
  - *From: VRGameDevGirl84(RTX 5090)*

- **New workflow v8 released**
  - Improved consistency and performance over previous versions
  - *From: Cseti*

- **Added volume intensity feature**
  - Working on appending intensity level to lyric segments to help LLM understand audio dynamics
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN 2.2 Mega Rapid AIO v8 posted**
  - Both SFW and NSFW versions available
  - *From: Phr00t*

- **WAN 2.2 Mega Rapid AIO v9 released**
  - Updated SFW + NSFW variants
  - *From: Phr00t*

- **New story mode added to prompt creator**
  - Makes flow better and less random, follows lyrics more closely
  - *From: VRGameDevGirl84(RTX 5090)*

- **Motion breakthrough in development**
  - Working on big motion breakthrough for next mega release
  - *From: Phr00t*

- **WAN 2.2 Mega Rapid AIO v12 released**
  - Big update to improve motion and quality, for both SFW/NSFW merges
  - *From: Phr00t*

- **New Prompter V2 released**
  - Now with chat history, full prompt library system with share feature, and template referencing
  - *From: thaakeno*

- **ComfyUI updated offload logic**
  - Now can use nodes even with 1280x720x121, before couldn't go beyond 33 frames at 960x544
  - *From: Dream Making*

- **V9 workflow released**
  - New workflow version with additional functionality, faster generation, and better automation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fat JD Vance LoRAs released**
  - LoRAs for Wan2.1 and Qwen Image available on HuggingFace
  - *From: huwhitememes ✦ MKS*

- **SVI LoRAs now available for Wan 2.2**
  - Version 2.0 SVI LoRAs released for Wan 2.2 compatibility
  - *From: PATATAJEC*

- **New unlimited length Wan 2.2 i2v method available**
  - ComfyUI-PainterLongVideo is the latest method for unlimited length Wan 2.2 i2v videos, works really good
  - *From: Dream Making*

- **Comprehensive Wan models list compiled**
  - Koba created comprehensive spreadsheet listing most Wan models, LoRAs and modules with CFG, steps, sampler info
  - *From: Koba*

- **New workflow combining Wan 2.2 (FMML) as high-noise model and Humo as low-noise model**
  - Enables first → middle → middle → last frame generation with fully automated image generation pipeline using LLM for prompt creation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Updated HuMo audio-motion node set**
  - Update made at https://github.com/ckinpdx/comfyui-humo-audio-motion with improved audio attention layers hooking
  - *From: Chandler ✨ 🎈*

- **ComfyUI Essentials nodes version issue**
  - SimpleMathDual node missing from stable 1.1.0, need to switch to nightly version or wait for pyproject.toml version bump
  - *From: Ablejones*

- **Workflow v4 released with more motion options**
  - Added options for increasing motion, changed first generation to HuMo only, changed steps to 6/2 from 7/3
  - *From: Ablejones*

- **Workflow v5 released**
  - Removed I2V augmentation, removed CFG step on HuMo, added LightX2V CFG step on High Noise sampler
  - *From: Ablejones*

- **Workflow v6 released with easier extension**
  - Uses new ComfyUI Switch node, can extend videos indefinitely by loading previous video, added Cut End Frames subgraph nodes
  - *From: Ablejones*

- **ComfyUI 0.8.0 release supports native SwitchNode**
  - V6 workflow now works with native SwitchNode in latest ComfyUI release
  - *From: triquichoque*

- **New workflow versions released without ComfyUI_essentials**
  - V5.1c and V6.1d released to remove dependency on problematic ComfyUI_essentials package
  - *From: Ablejones*

- **SYSTMS released INFL8 LoRA for Qwen Image Edit**
  - First LoRA release for inflating objects, with Wan 2.2 LoRAs coming in next day or so
  - *From: ingi // SYSTMS*

- **New InfiniteTalk native workflow released**
  - Clean and Easy Native Workflow for InfiniteTalk with Custom Audio File or TTS with Vibe Voice for Infinite Extensions
  - *From: Elvaxorn*

- **New version of style LoRA released**
  - Made to stick to whatever style better, proper i2v lora instead of T2V style, with new flow including local llm for prompting
  - *From: Flipping Sigmas*

- **Wan Prompt Scheduling node released**
  - Custom node that supports multiple prompts separated by pipe character with evenly distributed prompt weights across time
  - *From: atom.p*


## Workflows & Use Cases

- **Endless Travel with native VACE nodes**
  - Use case: Creating long video sequences by chaining multiple generations with frame overlap
  - *From: pom*

- **Music video creation with ChatGPT integration**
  - Use case: Using ChatGPT to create 7 text prompts, generating images with Flux, then using WAN prompts for transitions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pure text-to-video without images**
  - Use case: Generating videos using only text prompts for each segment without any reference images
  - *From: Tango Adorbo*

- **Reference input delay technique**
  - Use case: Running initial steps without reference, then applying reference for remaining steps to balance motion and accuracy
  - *From: Ablejones*

- **Control input integration with depth/pose**
  - Use case: Adding depth and pose control from driving video to guide generation
  - *From: Faust-SiN*

- **Long form i2v with sequential prompts**
  - Use case: Creating longer videos by chaining segments with evolving prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE with control video for depth/normal maps**
  - Use case: Using control video to extract depth/normal maps for better motion control
  - *From: Faust-SiN*

- **Crop and stitch upscaling**
  - Use case: Crop face, upscale at 1280x720, then stitch back to original
  - *From: Grimm1111*

- **Text to image/image upscale using WAN**
  - Use case: General purpose text to image or image enhancement
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE + MultiTalk lip sync**
  - Use case: Combining VACE with lip sync using face masks for second pass
  - *From: Tango Adorbo*

- **Split control video into 71 frame chunks and sequentially feed into Video Continuation Generator**
  - Use case: Long video generation with depth control
  - *From: Faust-SiN*

- **Low resolution base generation followed by upscaling**
  - Use case: Fast video creation - 45 seconds for base, then upscale with 0.79 denoise
  - *From: VRGameDevGirl84(RTX 5090)*

- **Key frame guided generation with end frame trajectory**
  - Use case: Long video with character consistency using Kontext-generated key frames
  - *From: Ablejones*

- **For loop workflow for smooth travel between arbitrary number of images**
  - Use case: Given a directory of images (n>2), generate smooth transitions
  - *From: seb bae*

- **ClownRegionalConditioning for prompt travel with WAN**
  - Use case: Form of prompt travel using regional conditioning
  - *From: DrJKL*

- **Text to image + ControlNet analysis for video continuation**
  - Use case: Automatically grab last frame, analyze with ChatGPT Vision, create prompt, generate image for next video segment
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pure Pusa video extension without VACE**
  - Use case: 81 frames per batch, 17 frame overlap, can extend 7 times for 30+ second videos
  - *From: Hashu*

- **Advanced KSampler step splitting for VACE**
  - Use case: Higher VACE strength for first few steps, then lower strength for later steps
  - *From: Piblarg*

- **Florence 2 character masking with VACE**
  - Use case: Automatically mask characters for targeted editing, requires manual fixing
  - *From: Piblarg*

- **Using 2.2 HN model for few steps to get depth map, then use for Phantom+Vace generation**
  - Use case: Hacking Wan2.2 with Phantom using Vace control
  - *From: Ablejones*

- **Long looping videos with Wan + Qwen Image Edit**
  - Use case: Generate long looping videos using primary image prompt and 3 edit prompts for timestep actions
  - *From: chancelor*

- **Image travel through arbitrary number of images**
  - Use case: Creating smooth transitions between multiple images
  - *From: seb bae*

- **FFLF (First-Frame-Last-Frame) with controlnet and VACE+Phantom**
  - Use case: 832x480x81 frames at 24fps in 15 minutes on 3060
  - *From: mdkb*

- **FFLF to VACE character swap to Wan22 upscaler**
  - Use case: Complete video processing pipeline from generation to upscaling with face consistency
  - *From: mdkb*

- **Crop/refine/replace for distant faces**
  - Use case: Automatically upscale video frame, fix faces, scale back for narrative films
  - *From: Ablejones*

- **Multi-image travel with VACE**
  - Use case: Process multiple image inputs without Nilor nodes, supports global prompt
  - *From: seb bae*

- **SEGS detailer for video enhancement**
  - Use case: Detail specific parts of video based on segmentation, works with VACE
  - *From: Ablejones*

- **VACE and Phantom for total face replacement**
  - Use case: Complete face reconstruction using reference and canny control
  - *From: Ablejones*

- **Tiled video upscaling with selective denoising**
  - Use case: Upscale videos while applying different denoise values to characters vs background
  - *From: Ablejones*

- **Chain sampling with High/Low noise models**
  - Use case: Split generation between high and low noise models with different conditioning
  - *From: The Shadow (NYC)*

- **HuMo audio-reactive video generation**
  - Use case: Text to video with reference image and audio synchronization
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom prompt list processing for music videos**
  - Use case: Process pipe-separated prompts for full song generation, 16 prompts at a time
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGameDevGirl84's music video workflow with ChatGPT integration**
  - Use case: Alternative to Gemini API using ChatGPT custom GPT for prompt generation, requires manual process for each run
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom and VACE reference control for character consistency**
  - Use case: Long video generation maintaining character appearance using phantom images and VACE references with careful strength scheduling
  - *From: Ablejones*

- **Video extension using res2 sampler with purgeVram**
  - Use case: Keep adding video segments with VRAM purging between segments for longer sequences
  - *From: dullheavenTM*

- **T2I style transfer workflow**
  - Use case: Style transfer for images, though doesn't translate as well for video
  - *From: Zuko*

- **Chain sampler setup for CFG injection**
  - Use case: Separate first 2 HN steps to get CFG in, then run remaining on distill model
  - *From: The Shadow (NYC)*

- **HUMO long-form generation**
  - Use case: Generate up to 150 frames with HUMO using wrapper nodes, fp16 model, 40 blocks swapped
  - *From: Juan Gea*

- **Music video generation with audio sync**
  - Use case: Automated music video creation with lip sync using transcribed lyrics and LLM prompt generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Endless Vace/Phantom merge workflow**
  - Use case: Creating continuous video sequences with scene variations using both Phantom and Vace controls
  - *From: The Shadow (NYC)*

- **Music video generation with automatic scene progression**
  - Use case: Generate cinematic music videos with automatic scene changes based on lyrics using LLM prompt generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Transition workflow for blending videos**
  - Use case: Creating smooth transitions between unrelated video clips using common elements
  - *From: ingi // SYSTMS*

- **Music video workflow V6.2 with auto-queue**
  - Use case: Automated music video generation with minimal manual intervention
  - *From: VRGameDevGirl84(RTX 5090)*

- **Vace + Phantom merge for character consistency**
  - Use case: Maintaining character appearance across video segments
  - *From: Gleb Tretyak*

- **Face detailing using Phantom**
  - Use case: Enhancing facial details in generated videos
  - *From: Ablejones*

- **Multi-language content creation**
  - Use case: Creating movie reviews and documentaries in Hindi and other languages
  - *From: Santoshyandhe*

- **Music video generation with automatic lip sync**
  - Use case: Creating full music videos from audio files and reference images with automated prompt generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE start to end node for conditioning**
  - Use case: Proper conditioning formatting for video generation
  - *From: Piblarg*

- **Multi-pass upscaling workflow**
  - Use case: 81 frames 480p to 1080p upscaling on 16GB VRAM using 3-pass upscale with face detailing
  - *From: Cseti*

- **Frame interpolation using VACE**
  - Use case: Taking 6 frames spaced over 49 frames with gray gaps and masks for interpolation
  - *From: ingi // SYSTMS*

- **Travel video generation using reference images**
  - Use case: Using travel images as reference inputs for Vace instead of frames, with Fun 2.2 Vace, Dyno for High Noise, Phantom for Low Noise
  - *From: Ablejones*

- **Music video generation with lip sync**
  - Use case: Creating full music videos with automatic lip sync to vocals
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sequential upscaling with context options**
  - Use case: Upscaling video from 480p to 720p using 0.3 denoise passes with face detailing
  - *From: Cseti*

- **First-frame-last-frame extension**
  - Use case: Creating longer videos (10+ seconds) using VACE with frame morphing
  - *From: Phr00t*

- **Manual context filling for consistent backgrounds**
  - Use case: Maintaining consistent backgrounds across all video segments
  - *From: hudson223*

- **V2V repaints using RES4LYF samplers without ControlNet or VACE**
  - Use case: Post-production style workflow for stability, relighting, and refining details
  - *From: vanhex*

- **Upscale workflow using loop nodes from easy-use node pack**
  - Use case: Set variable to define number of upscale iterations
  - *From: Cseti*

- **HuMo V7 long-form music video generation**
  - Use case: Synchronized lip-sync music videos with auto-queuing
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE video extension with dynamic scene introduction**
  - Use case: Adding new elements like vehicles to existing scenes during video extension, split into separate iterations for better control
  - *From: Daviejg*

- **AI influencer content creation with inline TTS and BGM**
  - Use case: Automated shorts creator for Instagram/TikTok using LLM script generation, VibeVoice TTS, and background music
  - *From: VRGameDevGirl84(RTX 5090)*

- **V7.1 workflow with multi-pass upscaling**
  - Use case: Creating high quality music videos with automatic audio sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Using Vace Ref frames for creative control**
  - Use case: Control how creative vs original the output should be
  - *From: Hashu*

- **I2V with dual LoRA sampling method**
  - Use case: Uses new lightx2v lora at high and old 2.1 lightx2v at low
  - *From: FL13*

- **Ollama proxy for ChatGPT integration**
  - Use case: Use ChatGPT API through local ollama node setup
  - *From: triquichoque*

- **Scene-specific re-generation**
  - Use case: Fix bad hands, faces, or specific scenes by muting unwanted groups and re-running
  - *From: VRGameDevGirl84(RTX 5090)*

- **News anchor/talking head setup**
  - Use case: Bypass background remover and LLM, use reference image with background, same context in all nodes
  - *From: WackyWindsurfer*

- **Manual prompt control**
  - Use case: Turn off auto Q, use context string only option, populate audio previews then manually write prompts for each segment
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multiple songs in one set**
  - Use case: Combine all audio into one song, then cut up after generation for efficiency
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context string for manual prompts**
  - Use case: Use context string boxes with 'Use context only' true for custom prompts per group
  - *From: VRGameDevGirl84(RTX 5090)*

- **Seamless looping integration**
  - Use case: Manually assemble control frames, stitch render on both ends, trim for smooth transitions
  - *From: brbbbq*

- **High-res dynamic video outpainting**
  - Use case: Adjust aspect ratios on the fly while keeping visual flow consistent using WAN 2.2 VACE + Qwen Image Edit 2509
  - *From: yo9o*

- **Dual model workflow with HN/LN split**
  - Use case: Running HN at lower resolution (360p) then upscaling for LN at 720p in 16 minutes on 3060 RTX
  - *From: mdkb*

- **Multiple character music video workflow**
  - Use case: Creating music videos with multiple consistent characters using batch reference images
  - *From: WackyWindsurfer*

- **VACE with Phantom depth map method**
  - Use case: Use WAN 2.2 HN output as depth map input for fresh Phantom generation
  - *From: Ablejones*

- **Automated music video workflow**
  - Use case: Only needs character image and song, rest is automatic using Gemini API for prompt generation
  - *From: burgstall*

- **Story mode with manual GPT prompts**
  - Use case: Using GPTs instead of LLM node for more control over story generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGDG v9 workflow for commercial-style videos**
  - Use case: Creating quick commercial/advertisement style content with headshots
  - *From: Scruffy*

- **Endless workflow with Wan 2.2 upscaling**
  - Use case: 30 second generations that continue seamlessly, can stitch together for longer videos
  - *From: Zlikwid*

- **F2LF sequences with VACE transitions**
  - Use case: Multiple First-Frame-Last-Frame sequences connected with VACE 2.2 transitions for complex motions
  - *From: Bernie 'Hot Dog' Madoff*

- **Loop transition removal workflow**
  - Use case: Removes pauses in AnimateDiff workflow specifically for looped videos using A B A pattern
  - *From: lostless.visuals*

- **Wan2.2 A14B I2V High Noise -> Wan HuMo 14B continuation**
  - Use case: Clean audio-synced video extensions with SVI loras to avoid flash and maintain consistency
  - *From: Ablejones*

- **3-pass clownshark sampling process**
  - Use case: Uses no distill cfg 3.0 for one step on high with standard sampler, then two steps high with distill lora on resample (with NAG), then remainder on low pass with distill lora
  - *From: BarleyFarmer*

- **First → middle → middle → last frame generation**
  - Use case: Automated pipeline using Wan 2.2 (FMML) + Humo with LLM-generated prompts for each segment
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo + SVI infinite extension workflow**
  - Use case: Creating long-form audio-synced videos with continuous extension capability
  - *From: Ablejones*

- **Low-end hardware version using Wan 2.1 1.3B**
  - Use case: Running on 12GB cards with 49 frames @360x480 resolution
  - *From: atom.p*

- **Separate initial and extension workflows**
  - Use case: Keep initial video generation and extension processes separate for easier management
  - *From: craftogrammer 🟢*

- **V5.1c - Simplified extension workflow**
  - Use case: Basic workflow, just add more extension blocks to make longer videos
  - *From: Ablejones*

- **V6.1d - Continuation workflow**
  - Use case: Generate initial video then switch mode to continue generating from last video
  - *From: Ablejones*

- **SVI Pro loop workflow with automatic batching**
  - Use case: Using prompt list for automatic batching instead of manual copy/paste
  - *From: Ivoxx*

- **VACE+Phantom then HuMo refinement**
  - Use case: Generate scene with VACE+Phantom for movement, then v2v pass with HuMo for lip sync
  - *From: Ablejones*

- **InfiniteTalk Extension Workflow**
  - Use case: Generate and preview each 5 second chunk separately and attach together, allowing faster generations, more VRAM saving, and flexibility compared to context window workflows
  - *From: Elvaxorn*

- **Segmented upscaling with VACE**
  - Use case: Upscale every 16th frame then use as first/last frame for VACE at 17 frames per gen, with color matching and 1 frame overlap stitching
  - *From: ingi // SYSTMS*

- **Manual audio sync workflow**
  - Use case: Manually combining sections after generation failure, requires calculating length and muting certain groups when audio runs out
  - *From: AJO*


## Recommended Settings

- **Block swap for 4060Ti**: 30-40 blocks, 5 for VACE
  - Helps with VRAM limitations on lower-end hardware
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE strength for subsequent passes**: 0.8-0.9
  - Allows more motion while maintaining quality in continuation segments
  - *From: Kaïros*

- **Steps for FusionX VACE**: 8 steps total (2 without reference, 6 with reference)
  - Balances speed and quality while maintaining reference accuracy
  - *From: Ablejones*

- **Steps for LightX2V LoRA**: 20 steps first group, then 4-8 steps subsequent
  - Ensures quality with speed LoRA - insufficient initial steps cause quality loss
  - *From: The Shadow (NYC)*

- **Context frames**: 20 frames
  - Provides smoother transitions between segments
  - *From: pom*

- **Frame count per segment**: 81 frames
  - Provides better results than shorter segments
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sampler for LightX2V**: LCM/Simple
  - Works well with LightX2V LoRA for faster generation
  - *From: Gateway {Dreaming Computers}*

- **Denoise**: 0.79 for general use, 0.5-0.7 for upscaling
  - Balance between quality and preserving details
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE strength**: 0.8
  - Prevents depth/normal information from influencing too much
  - *From: Ablejones*

- **Block swap**: 40
  - For better memory management
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps**: 4 with LightX, 8 without
  - LightX allows for significant speed boost
  - *From: VRGameDevGirl84(RTX 5090)*

- **Resolution divisibility**: 16
  - Required for proper processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **MPS in FusionX**: 0.5
  - Default setting in the merge
  - *From: VRGameDevGirl84(RTX 5090)*

- **Ghibli LoRA strength**: 0.3
  - Used in successful long video generation
  - *From: Faust-SiN*

- **VACE embed strength**: 0.7
  - Used in successful long video generation
  - *From: Faust-SiN*

- **Steps for base generation**: 20-25
  - With teacache cranked up to 0.8 for fast base generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoise for upscaling**: 0.79
  - Tipping point - above that it changes everything, below it is less adaptive
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG**: 7
  - Standard setting used in workflows
  - *From: pom*

- **Shift**: 4
  - Standard setting used in workflows
  - *From: pom*

- **Context frames**: 81
  - Default setting for context options
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps with LightX2V**: 5
  - LightX2V lets it run fast with CFG 1, shift 1
  - *From: mdkb*

- **Pusa LoRA strength**: 1.0
  - Maintains better reference fidelity and reduces degradation
  - *From: Ablejones*

- **LightX LoRA strength**: 0.5
  - Reduces cross-batch burning artifacts
  - *From: A.I.Warper*

- **Video extension overlap**: 17 frames
  - Works well with 81 frame batches for smooth transitions
  - *From: Hashu*

- **Euler steps**: 12 minimum
  - Better quality than lower step counts
  - *From: Ablejones*

- **res_2s steps**: 5-6 steps
  - Dramatic quality improvement with manageable speed trade-off
  - *From: Ablejones*

- **CausVid merge strength**: 1.0
  - Full strength works well for low steps model
  - *From: Piblarg*

- **Frame count**: 81 or 121 frames
  - Phantom trained on 121, Vace/Wan2.1 on 81. Can try middle-ground like 97 frames
  - *From: Ablejones*

- **CFG with speed loras**: CFG=2.0 instead of 1.0
  - CFG=1.0 makes Phantom resemblance worse when using Lightx2v/lightning
  - *From: Ablejones*

- **Lightx2v lora strength**: 2-3 strength
  - Works best at this range, can go higher. At 1.0 feels too weak
  - *From: thaakeno*

- **Lightning lora strength**: 1.0
  - Should stay at 1.0 unlike Lightx2v
  - *From: thaakeno*

- **Vace control strength**: 0.5 for depth and canny each
  - Used for 4/12 steps in experimental workflow
  - *From: Ablejones*

- **CausVid LoRA strength**: 0.5
  - Lower strength with CFG 2.0-2.5 for reasonable resemblance
  - *From: Ablejones*

- **Minimum steps for resemblance**: 8
  - Less steps lose likeness, more steps better but slower
  - *From: Ablejones*

- **Crop factor for Tiled SEGS**: 1.20 to 1.50
  - 3.0 is too large and causes OOM issues
  - *From: Ablejones*

- **Memory patcher settings**: min_weight_memory_ratio: 0.00, model_threshold_gb: 10.00, buffer_gb: 2.00
  - Prevents OOM while maintaining performance
  - *From: Ablejones*

- **VACE reference strength for likeness**: Increase CFG, decrease distill lora strength
  - When losing face consistency with speed optimizations
  - *From: Ablejones*

- **Denoise for face detailing**: 1.0
  - Allows complete face reconstruction from reference and canny
  - *From: Ablejones*

- **Phantom strength in VACE**: 0.0
  - Best strength for latent frames associated with Phantom images
  - *From: Ablejones*

- **ControlVid strength with Phantom**: 2.0
  - Higher strength needed to make character follow control video instead of reference pose
  - *From: Gleb Tretyak*

- **Buffer GB for Janky Memory Patcher**: 1.0 or 2.0
  - Helps resolve OOM issues after ComfyUI updates
  - *From: Ablejones*

- **Blockswap blocks**: 20
  - Makes generation work on 24GB VRAM cards
  - *From: Slavrix*

- **Tile dimensions**: Divisible by 16
  - Important even though VAE encodes to be divisible by 8, prevents tensor errors
  - *From: Ablejones*

- **ETA**: 0.0
  - Eliminates fireflies/noise artifacts in fully_implicit_gauss-legendre_2s sampler
  - *From: Ablejones*

- **CFG on HN first step**: 3.5
  - When not using distill LoRA on first HN sampler step
  - *From: The Shadow (NYC)*

- **Cseti Kinestasis LoRA strength**: 0.45-0.8
  - Adds significant movement to animations without being too strong
  - *From: The Shadow (NYC)*

- **Windows paging file**: 80-96GB
  - Prevents OOM errors when working with large models, most important setting for low RAM systems
  - *From: Ablejones*

- **Linear quadratic threshold_noise at inflection 0.5**: 0.2
  - Drops by 0.2 noise level by 50% of steps, more intuitive control than complex schedulers
  - *From: Ablejones*

- **Banostasis LoRA strength**: 0.45-1.0
  - Depending on what looks good with sampler, example used Res 2s stable + 0.45 strength
  - *From: The Shadow (NYC)*

- **ETA parameter**: 0
  - To avoid dancing fireflies artifacts
  - *From: The Shadow (NYC)*

- **HUMO strength for animals**: 3
  - Works effectively with animal subjects
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **CFG for early HN steps**: 3-3.5
  - Better for stylized aesthetics before applying distill optimizations
  - *From: The Shadow (NYC)*

- **HUMO CFG first step**: 3.5
  - Used in successful long-form generation setup
  - *From: Juan Gea*

- **Frames for Phantom merge**: 97 frames
  - Half-way between Phantom's 121 frames and Vace's 81 frames
  - *From: Ablejones*

- **Frame rates**: Phantom: 24fps with 121 frames, Vace: 16fps with 81 frames
  - Training specifications for each model
  - *From: Ablejones*

- **Vace strength for Phantom frames**: 0.0
  - Phantom frames in Vace merge should have no Vace strength influence
  - *From: Ablejones*

- **Audio scale**: 1.0 instead of 2.0
  - Reduces overly exaggerated mouth movements
  - *From: samhodge*

- **Shift parameter for transitions**: 8
  - Sweet spot for transition quality, lower values can help force transitions
  - *From: ingi // SYSTMS*

- **Denoise for upscaling**: 0.4
  - Used for successful 6-tile upscaling at 640x640 each
  - *From: Ablejones*

- **Tile size for upscaling**: 480x480 for 640x640 latents
  - Creates overlap at edges to avoid seams
  - *From: Clownshark Batwing*

- **Lyrics transcription**: true
  - Required for LLM to have lyrics context for prompt generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX + FastWan LoRA steps**: 4 steps
  - Provides good quality with significant speed improvement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face detailer LoRA strength**: 2.0
  - Improves facial quality in generated videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio scale for mouth movement**: 2 (normal), 1 (less movement)
  - Controls how much the mouth moves - scale of 1 results in minimal mouth movement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video resolution**: 720p
  - Good balance of quality and generation speed
  - *From: samhodge*

- **Qwen AIO sampler/scheduler**: ipndm/simple at 4 steps
  - Recommended settings for Qwen AIO v2, more steps are better
  - *From: Phr00t*

- **Frame count for extended videos**: 121 frames (5 seconds)
  - Maximum working frame count, though first few frames may be funky
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps**: 4
  - For cinematic results without FastWAN
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face detailer LoRA strength**: 1
  - Higher values look strange
  - *From: VRGameDevGirl84(RTX 5090)*

- **Frames**: 97
  - Hardcoded workflow requirement, changing breaks workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **FPS**: 25
  - Hardcoded workflow requirement, changing breaks workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoise for upscaling**: 0.3
  - For sequential upscaling passes
  - *From: Cseti*

- **QwenEdit steps**: 4-8
  - No significant improvement over 8 steps
  - *From: Phr00t*

- **CFG for QwenEdit**: 1
  - Standard setting for QwenEdit models
  - *From: Tachyon*

- **Frames per second**: 25
  - Other values will cause sync issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Unsampler noise ducking**: 0.6
  - Keeps base noise structure, can push to 0.875 but becomes seed-dependent
  - *From: vanhex*

- **Denoise for LN model in detailer approach**: 0.79
  - Effective for polishing without changing structure
  - *From: mdkb*

- **Qwen LoRA strengths**: 8-step: 0.7, 4-step: 0.3, NSFW loras: 0.3 each
  - NSFW loras normalized to 1.5 total
  - *From: Phr00t*

- **Steps for HuMo**: 8 steps
  - 10 steps somehow decreased quality in testing
  - *From: Chandler ✨ 🎈*

- **VACE strength**: 0.70-0.75
  - Balance between motion and stability for video extensions
  - *From: Daviejg*

- **Shift value for VACE**: 120
  - Helps with motion continuity without burning, despite being much higher than typical 4-6
  - *From: Daviejg*

- **Resolution**: 1024x576
  - Sweet spot for quality vs performance balance
  - *From: hudson223*

- **Video duration**: 5 seconds
  - Eliminates sync drift issues, produces proper 125 frames at 25 FPS
  - *From: VRGameDevGirl84(RTX 5090)*

- **Scene duration for HuMo**: 4.04 seconds (101 frames)
  - Must follow 4n+1 pattern, auto-adjusts from 4.0 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Generation time RTX 5090**: 15-16 mins per 1 min video, 30 min for 4 min with 2 steps
  - Default settings vs FastWan optimization
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lyric overlap**: 0 for no overlap
  - Prevents doubling up lyrics in transcription
  - *From: J_Pyxal*

- **SeedVR2 noise values**: Start with input noise 0.01-0.05, latent noise for softness
  - Only use if artifacts present, very sensitive
  - *From: Adrien Toupet*

- **Upscaling resolution vs steps**: 1280x720 at 4 steps
  - Better quality than higher steps at lower resolution
  - *From: Chandler ✨ 🎈*

- **Florence2 coordinates index**: Set to face number you want upscaled
  - bbox detects multiple faces as face 0, face 1 etc
  - *From: Cseti*

- **Color match strength**: 0.5 or bypass node
  - Default setting can make videos too dark
  - *From: Flipping Sigmas*

- **Audio scale**: 1.2-1.3
  - Better results for certain music types
  - *From: Mazrael.Shib*

- **High noise LoRA settings**: Can be bumped up
  - May improve results when using fp8 scaled models
  - *From: Flipping Sigmas*

- **Resolution**: 1280x720
  - Best results for quality vs performance
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps**: 8
  - Optimal with LightX for high resolution
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap**: 20
  - Recommended for high resolution on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **Base model length**: 81
  - Can push to 109 depending on VRAM, longer lengths cause exponential slowdown
  - *From: Phr00t*

- **Shift**: 8.00
  - Increased for better results with ClownShark nodes
  - *From: brbbbq*

- **AnimateDiff LoRA strength**: 0.50-0.65
  - Good range for motion enhancement
  - *From: brbbbq*

- **Frame overlap**: 14 frames with 81 total frames
  - Good for elaborate transitions
  - *From: happy.j*

- **SHIFT parameter**: Lower values
  - Helps retain character likeness and consistency
  - *From: thaakeno*

- **HN denoise**: 1.0
  - Standard setting, don't touch
  - *From: mdkb*

- **LN denoise**: 0.25
  - For image space upscaling workflow
  - *From: mdkb*

- **Block swap**: 30
  - For 24GB VRAM cards to prevent OOM
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps**: 4 steps HN, 8 steps LN
  - Balance between quality and speed
  - *From: mdkb*

- **LightX2V strength**: 3 for HN, 4 for LN
  - Optimal performance in dual model workflow
  - *From: mdkb*

- **UniPC sampler**: 6 steps
  - Alternative fast sampling method
  - *From: hudson223*

- **CFG**: 3.0 with 20 steps
  - Better for preventing unwanted lip movements compared to LightX LoRA
  - *From: Ablejones*

- **CFG with LightX**: 1.0 with 8 steps
  - When using LightX LoRA for faster inference
  - *From: Ablejones*

- **Resolution**: 1024x576
  - Both dimensions divisible by 32, prevents artifacts, good quality
  - *From: Charlie*

- **Frames for HuMo**: Maximum ~5 seconds
  - Anything over 5 seconds causes bad first few frames and degrades video quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap**: Disable for RTX 5090
  - Default settings work without block swap on high-end GPUs
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX lora strength**: 0.5
  - Lower strength helps avoid unwanted lip movement
  - *From: Ablejones*

- **CFG schedule**: CFG 3.0 for 2 steps out of 8, then CFG 1.0
  - Helps control lip movement in early steps
  - *From: Ablejones*

- **Frame limit for HuMo with audio attention layers**: 121 frames maximum
  - To avoid burn on first frames
  - *From: Chandler ✨ 🎈*

- **Block swap for memory optimization**: 40 block swaps mentioned
  - For running on lower VRAM cards like RTX 3090
  - *From: dj47*

- **Resolution for Wan generation**: 720x720
  - Standard test resolution, takes 85sec on RTX 5090 for 81 frames
  - *From: burgstall*

- **LLM response word limit**: 80-100 words
  - Cap found in Wan2.1/wan/utils/prompt_extend.py notes
  - *From: JohnnyLongBalls*

- **Steps configuration**: 6/2 instead of 7/3
  - Allows more HuMo motion in latest workflow versions
  - *From: Ablejones*

- **Audio delay**: 0.2s default
  - Helps synchronize audio with video generation
  - *From: Ablejones*

- **Frame overlap**: 5-6 frames minimum
  - Needed for smooth video transitions
  - *From: ingi // SYSTMS*

- **Resolution**: 1024x1024 vs 512x512
  - Higher resolution significantly improves lipsync quality
  - *From: NC17z*

- **Block swapping**: 30 blocks aggressively
  - For managing VRAM with large models
  - *From: ingi // SYSTMS*

- **Sage attention**: sage attention 2++
  - Some nodes install sage attention 1, need to ensure 2++ version
  - *From: craftogrammer 🟢*

- **Audio scale value**: Variable control
  - Rewired HuMo node to include audio scale to increase/decrease mouth movement
  - *From: hudson223*

- **Frame count for transitions**: 2 frames instead of 1
  - Prevents flashing transitions when middle/end frames don't catch up properly
  - *From: Blink*

- **PyTorch version**: 2.9.1+cu130
  - Cutting edge setup that avoids sage attention errors
  - *From: craftogrammer 🟢*

- **Segment length calculation**: 97 frames max per section, 97/25 = 3.88 seconds
  - Standard segment timing for workflows
  - *From: AJO*

- **VACE steps**: 2 steps
  - Running VACE at different steps for comparison testing
  - *From: pom*

- **Video generation steps**: 20 steps
  - Better quality than default, though still not as good as WanVaceAdvanced nodes at 4 steps
  - *From: brbbbq*


## Concepts Explained

- **Context options**: Allows for unlimited number of frames, just takes longer to process
  - *From: VRGameDevGirl84(RTX 5090)*

- **Control masks**: Inputs that prevent continuation frames from changing too much in VACE workflows
  - *From: Ablejones*

- **Character drift**: Tendency for characters and settings to change over chained generations
  - *From: Ablejones*

- **Residual self-attention**: Continuation frames leave attention patterns that are hard to overcome with prompt changes
  - *From: Ablejones*

- **TeaCache**: A caching mechanism that can be cranked up to speed up generation, used with low resolution base generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Split Sigmas/Samplers**: Method to separate sampling into stages - first sampler without reference frame to get motion going, second sampler with VACE conditioning for control
  - *From: Ablejones*

- **NAG**: New way to do negative prompting since CFG is zero and normal negative prompting doesn't work
  - *From: VRGameDevGirl84(RTX 5090)*

- **Cross-batch burning**: Artifacts that appear when extending videos across multiple generation batches
  - *From: A.I.Warper*

- **Block swapping**: Memory optimization technique where parts of model are loaded/unloaded from VRAM as needed to manage memory usage
  - *From: Ablejones*

- **Step splitting**: Using different settings (like VACE strength) for different steps within the same generation
  - *From: Piblarg*

- **Janky Memory Patcher**: Tells ComfyUI to pretend you have less VRAM than you actually do, giving header room for VRAM usage spikes
  - *From: Ablejones*

- **Dynamic paging file**: Operating system feature where hard drive space supplements RAM dynamically - it's normal for disk space to change
  - *From: Ablejones*

- **res_2s sampler**: Takes twice as long because it takes 2 substeps per full step, res_3s takes 3 substeps etc
  - *From: Ablejones*

- **FFLF (First-Frame-Last-Frame)**: Morphing technique that avoids usual Phantom problems at less than 121 frames
  - *From: mdkb*

- **Faces at distance issue**: AI models break distant faces during camera zoom, unlike digital cameras, common in narrative films
  - *From: mdkb*

- **SEGS**: Segmentation system used for detailing specific parts of images/video
  - *From: Ablejones*

- **Tiled SEGS**: Splits video into segments for detailed processing without OOM, each segment sampled at crop region dimensions
  - *From: Ablejones*

- **SEGS preview functionality**: Shows first frame of each segment to indicate how many full videos will be sampled and stitched
  - *From: Ablejones*

- **Detailer hook system**: New way VACE connects to detailer via hook instead of intrusive wrapper, makes nodes function more normally
  - *From: Ablejones*

- **Chain sampling**: Latent carries conditionings, model, sigmas, current step, raw latent - don't need other inputs unless changing them
  - *From: Ablejones*

- **Sampler model call counts**: *m samplers = 1 call per step, *s samplers = number before 's' calls per step (e.g. res_2s = 2x slower)
  - *From: Ablejones*

- **ETA in samplers**: Controls how much noise is added and removed per step, similar to 'ancestral' or 'sde' in base ComfyUI. Higher eta allows more change per step, makes generation more flexible
  - *From: Ablejones*

- **Phantom images**: Used to maintain character consistency throughout video generation by providing reference frames that prevent character degradation
  - *From: Ablejones*

- **VACE references**: Single frame references for style/appearance control, multiple references pile on top of each other, better to combine into single reference image
  - *From: Ablejones*

- **Sigma nodes control**: Sigma nodes take priority over sampler step settings when connected
  - *From: The Shadow (NYC)*

- **VACE strength per frame**: Strength values are applied per latent frame, with first frame using reference strength and subsequent frames using control strengths
  - *From: Ablejones*

- **Loop dependency in ComfyUI**: Occurs when nodes wait on each other creating circular dependency that breaks workflow execution
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom reference vs Vace reference**: Phantom works by adding latent frames to existing frames and uses prompts internally for strength, while Vace reference is a separate control mechanism
  - *From: Ablejones*

- **Race condition in workflow**: Timing issue where components execute out of order, causing dependencies to not be available when needed
  - *From: samhodge*

- **Memory leak with WAN21_Vace**: Occurs when workflow errors during encode/sample phase, then user fixes workflow and continues - model stays referenced somewhere
  - *From: Gleb Tretyak*

- **Phantom reference diversity**: Using different images as phantom reference vs first frame produces better character consistency than using same image
  - *From: Gleb Tretyak*

- **Tile overlap for upscaling**: Tile size should not evenly divide latent resolution to create overlap at edges and prevent seams
  - *From: Clownshark Batwing*

- **VACE extend process**: Video extension process that has intrinsic character degradation issues, more apparent on darker videos
  - *From: Ablejones*

- **Context switching in upscaling**: At low denoise during upscaling, context switching is barely noticeable, allowing longer videos on limited VRAM
  - *From: Cseti*

- **FastAPI wrapper approach**: Wrapping ComfyUI workflow in FastAPI container for automated processing via cURL commands
  - *From: samhodge*

- **Fast group muter**: Node that allows disabling specific video groups/segments in the workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **Index node**: Tracks which video segment is being processed, should increment for each run
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context fields**: 16 optional prompt fields that can be filled for specific segments, get populated by LLM or manually
  - *From: kendrick*

- **Audio sync drift**: Gradual timing offset between audio and video that accumulates across segments
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap**: Using different model configurations for each upscaling pass
  - *From: Cseti*

- **Gen lock**: Production technique to sync all audio/video sources on multi-cam sets, prevents drift between sources
  - *From: hudson223*

- **Context options**: Settings that can cause specific issues with Wan processing
  - *From: Cseti*

- **List cycling in prompt generation**: When multiple options provided for categories (Outfit, Environment, etc.), system cycles through items in order without repetition until all used, then restarts cycle
  - *From: VRGameDevGirl84(RTX 5090)*

- **Temporal noise shifting/popping**: Visual artifact in WAN where small details like hair, textures drift or morph between frames, creating flickering effect. More noticeable than in closed source models.
  - *From: HeadOfOliver*

- **Audio drift in video generation**: Timing mismatch where audio gradually becomes out of sync with video over duration, typically audio being ~1 second longer than video
  - *From: hudson223*

- **4n+1 frame pattern**: HuMo requires specific frame counts following mathematical pattern where n is integer
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lyric overlap**: Provides context to LLM for prompt generation but doesn't affect actual audio sync
  - *From: Chandler ✨ 🎈*

- **Context strings**: Alternative to lyrics for providing scene context, can be used for LoRA keywords
  - *From: VRGameDevGirl84(RTX 5090)*

- **List handling options**: Strict Cycle uses each item once then repeats, Reference Guide uses everything as guide, Random Selection grabs randomly, Free Interpretation allows LLM to ignore/combine
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context string vs lyrics**: Context string can be used alone or combined with lyrics, requires 'enable lyrics' to be on for context to work
  - *From: VRGameDevGirl84(RTX 5090)*

- **Extra Trim**: Cuts off latent frames from end of video generation (2 latent = 8 real frames) because end frames can get weird as model converges to target
  - *From: Ablejones*

- **Context string limit**: Lyric string has text limit to prevent issues with people screaming like 'ahhhhhhhhh' being too long for LLM context
  - *From: VRGameDevGirl84(RTX 5090)*

- **HN/LN dual model workflow**: High Noise model runs first pass at lower resolution, Low Noise model does second pass at higher resolution
  - *From: jellybean5361*

- **Motion blocks in diffusion**: Earlier blocks focus more on motion, used for training transition LoRAs
  - *From: ingi // SYSTMS*

- **Latent space upscaling**: Upscaling in latent space between HN and LN passes to save VRAM and time, but can cause ghosting
  - *From: mdkb*

- **Context Options**: Allows generation past 81 frames but with very long generation times
  - *From: thaakeno*

- **Block swap**: Memory management technique that happens automatically in native ComfyUI without additional nodes
  - *From: Blink*

- **VACE overshooting**: When VACE continues motion past target frames then rotates back to align - occurs when start and end frames are identical
  - *From: Bernie 'Hot Dog' Madoff*

- **All-in-One (AIO) model**: Simplified model that cuts out high noise model for speed but sits between Wan 2.1 and full 2.2 in quality
  - *From: Phr00t*

- **SVI loras**: Specific video interpolation loras that need precise input preparation and often aren't compatible with each other
  - *From: Ablejones*

- **Color drift**: Issue where video colors gradually shift away from source when using frame-by-frame color matching instead of consistent video-wide matching
  - *From: Ablejones*

- **Audio attention layers hooking**: Method for integrating audio input into video generation by modifying attention mechanisms, more effective than band editing for HuMo
  - *From: Chandler ✨ 🎈*

- **Frame burn**: Artifact where first frames get overexposed or corrupted, happens when exceeding certain frame limits in generation
  - *From: Chandler ✨ 🎈*

- **Chain sampling**: Runs first sampler for specified steps, then continues from that point with second sampler for remaining steps
  - *From: Ablejones*

- **Frame overlap**: Video generations need overlap to blend smoothly, but audio should be padded with silence instead of repeated
  - *From: hudson223*

- **SVI hack**: Combining SVI 2 Pro lora with SVI v2 lora for 2.1, using latter with HuMo instead of base Wan2.1
  - *From: Ablejones*

- **Extension blocks**: Segments that continue video generation from previous segments using specific timing and audio synchronization
  - *From: Ablejones*

- **HN/LN sampling split**: High Noise and Low Noise sampling phases that can use different models - VACE for HN, HuMo for LN
  - *From: Ablejones*

- **Seed-sniping**: Technique of adjusting seeds to achieve specific performance results, especially important for lip sync quality
  - *From: Ablejones*

- **Unsampling and resampling**: Method to refine output with different model by reversing then resampling, slowest but potentially most accurate method
  - *From: Ablejones*

- **Prompt Scheduling in Wan**: Uses Context Window system with pipe (|) separator to assign different prompts to different context windows (segments) rather than specific frame numbers. Windows are typically 81 frames with 16-frame overlap
  - *From: Flipping Sigmas*

- **HI/LO conditioning**: High noise starts strong and fades to 0.0, low noise starts at 0.0 and finishes strong, with mid strength set to 0.5 and combined with opposing weights
  - *From: atom.p*


## Resources & Links

- **Electric Alien LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1344057524935983125/1386258901934280715
  - *From: JohnDopamine*

- **Morphing into Plushtoy LoRA** (lora)
  - https://civitai.com/models/1525175/wan-i2v-skyreels-i2v-morphing-into-plushtoy-trained-on-sr-v2-i2v?modelVersionId=1725658
  - *From: JohnDopamine*

- **FusionX VACE GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.1_T2V_14B_FusionX_VACE-GGUF/tree/main
  - *From: VRGameDevGirl84(RTX 5090)*

- **FusionX VACE** (model)
  - https://huggingface.co/QuantStack/Wan2.1_T2V_14B_FusionX_VACE/tree/main
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steerable Motion repository** (repo)
  - https://github.com/banodoco/steerable-motion
  - *From: The Shadow (NYC)*

- **Quick Connections ComfyUI extension** (tool)
  - https://github.com/niknah/quick-connections
  - *From: BarleyFarmer*

- **Ablejones latest workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1387913773335183360
  - *From: Ablejones*

- **FusionX ingredients workflow** (workflow)
  - https://civitai.com/models/1690979
  - *From: VRGameDevGirl84(RTX 5090)*

- **Live wallpaper LoRA** (lora)
  - https://civitai.com/models/1264662/live-wallpaper-style
  - *From: The Shadow (NYC)*

- **ComfyUI LLM nodes** (node)
  - https://github.com/dagthomas/comfyui_dagthomas
  - *From: JohnDopamine*

- **MTB nodes for frame extraction** (node)
  - https://github.com/melMass/comfy_mtb
  - *From: JohnDopamine*

- **VACE evaluation dataset** (dataset)
  - https://huggingface.co/datasets/BestWishYsh/OpenS2V-Eval
  - *From: fredbliss*

- **Execution inversion nodes for loops** (node)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui
  - *From: fredbliss*

- **ControlFlow Utils nodes** (node)
  - https://github.com/VykosX/ControlFlowUtils
  - *From: drmbt*

- **Shrug Prompter LLM nodes** (node)
  - https://github.com/fblissjr/shrug-prompter
  - *From: fredbliss*

- **Dreambait nodes with frame blend** (node)
  - https://github.com/drmbt/comfyui-dreambait-nodes
  - *From: drmbt*

- **ClownRegionalConditioning nodes** (node pack)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui
  - *From: DrJKL*

- **Flux chin removal model** (model)
  - https://civitai.com/models/1742500
  - *From: VRGameDevGirl84(RTX 5090)*

- **NAG node pack** (node pack)
  - https://github.com/ChenDarYen/ComfyUI-NAG
  - *From: trax*

- **Puppet style LoRA for 1.3B** (lora)
  - *From: Flipping Sigmas*

- **City96 Wan GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-T2V-14B-gguf/tree/main
  - *From: xwsswww*

- **FusionX Lightning ingredients/workflows** (workflow)
  - https://civitai.com/models/1736052/fusionxlightning-ingredientsworkflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan2.2 A14B LoRA extract** (model)
  - https://huggingface.co/drozbay/Wan2.2_A14B_lora_extract/tree/main
  - *From: Ablejones*

- **Pusa LoRA by Kijai** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Pusa
  - *From: pom*

- **LightX2V newer versions** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Shawneau 🍁 [CA]*

- **WAN prompt generator tool** (tool)
  - https://prompter.on.websim.com/
  - *From: thaakeno*

- **Phantom VACE GGUF merged model** (model)
  - https://huggingface.co/orabazes/wan-14B_vace_phantom_v2_GGUF/tree/main
  - *From: mdkb*

- **Janky Memory Patcher installation** (tool)
  - https://github.com/drozbay/janky_memory_patcher
  - *From: Ablejones*

- **ComfyUI-WanVaceAdvanced with updated docs and workflow example** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: Ablejones*

- **Wan2_1-VACE_module_14B_fp8_e4m3fn.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_fp8_e4m3fn.safetensors
  - *From: Ablejones*

- **FakeVace merge for continuation/extension** (model)
  - https://discord.com/channels/1076117621407223829/1402796376932220998
  - *From: JohnDopamine*

- **ComfyUI-MultiGPU** (tool)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: xwsswww*

- **Video upscaling workflow tutorial** (tutorial)
  - https://www.youtube.com/watch?v=CmAGOcbU1T4
  - *From: mdkb*

- **Wan 2.2 5B version** (model)
  - https://civitai.com/models/1897405?modelVersionId=2147817
  - *From: crinklypaper*

- **Video captioning solution** (workflow)
  - https://discord.com/channels/1076117621407223829/1145677539738665020/1411716362858135602
  - *From: xwsswww*

- **CausVid v2 LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors
  - *From: Ablejones*

- **Kinestasis stop motion LoRA** (lora)
  - https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1
  - *From: Cseti*

- **Modified Impact Pack fork** (repo)
  - https://github.com/drozbay/ComfyUI-Impact-Pack
  - *From: Ablejones*

- **WanBlockswap for native ComfyUI** (repo)
  - https://github.com/orssorbit/ComfyUI-wanBlockswap
  - *From: xwsswww*

- **ComfyUI Essentials package** (custom_nodes)
  - *From: seb bae*

- **Radial attention calculation node** (repo)
  - https://github.com/comfy-deploy/comfyui-llm-toolkit
  - *From: Impactframes.*

- **ComfyUI-WanVaceAdvanced** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: Ablejones*

- **High 2.2 model updated** (model)
  - https://civitai.com/models/1897405
  - *From: crinklypaper*

- **SAM2.1 model** (model)
  - https://huggingface.co/facebook/sam2.1-hiera-base-plus/blob/main/sam2.1_hiera_base_plus.pt
  - *From: xwsswww*

- **VACE workflow example** (workflow)
  - https://docs.comfy.org/tutorials/video/wan/vace#1-workflow-download-3
  - *From: Ablejones*

- **LoRA scheduling blog post** (tutorial)
  - https://blog.comfy.org/p/masking-and-scheduling-lora-and-model-weights
  - *From: The Shadow (NYC)*

- **Cseti's Kinestasis concept LoRA** (lora)
  - https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1
  - *From: The Shadow (NYC)*

- **ChatGPT custom GPT for WAN music videos** (tool)
  - https://chatgpt.com/g/g-68d0a5a9f7b4819189bdb15c826c789c-wan-2-1-humo-text-to-music-video-prompt-helper
  - *From: VRGameDevGirl84(RTX 5090)*

- **Clownshark's scheduler explanation video** (educational)
  - https://www.youtube.com/watch?v=egn5dKPdlCk&t=4s
  - *From: Ablejones*

- **ComfyUI PR for i2v improvements** (code)
  - https://github.com/comfyanonymous/ComfyUI/pull/10034
  - *From: Ablejones*

- **Phr00t's model discussion list** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/discussions/109#68d5f7599abc92c5d6ae8105
  - *From: Phr00t*

- **Anal missionary LoRA** (lora)
  - https://civitai.com/models/1434685/anal-missionary-wan-22
  - *From: Tachyon*

- **Mega v4 model** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/tree/main/Mega-v4
  - *From: ezMan*

- **Rapid AIO Mega workflow** (workflow)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/blob/main/Mega-v3/Rapid-AIO-Mega.json
  - *From: ezMan*

- **Audio separation nodes** (repo)
  - https://github.com/christian-byrne/audio-separation-nodes-comfyui
  - *From: VRGameDevGirl84(RTX 5090)*

- **Bytedance Lynx paper** (research)
  - https://arxiv.org/abs/2509.15496
  - *From: MarkDalias*

- **Dockerized ComfyUI** (tool)
  - https://github.com/mmartial/ComfyUI-Nvidia-Docker
  - *From: triquichoque*

- **Suno music playlist** (resource)
  - https://suno.com/playlist/32bbcd3b-c2dd-46a6-acfb-0548294e76d7
  - *From: kendrick*

- **VRGameDevGirl Custom Nodes v3.0.0** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl
  - *From: VRGameDevGirl84(RTX 5090)*

- **New workflow tutorial video** (tutorial)
  - https://youtu.be/bagfoMTzlO8
  - *From: VRGameDevGirl84(RTX 5090)*

- **Gemini node tutorial** (tutorial)
  - https://discord.com/channels/1076117621407223829/1417710283945672764/1419476712374403082
  - *From: Janosch Simon*

- **Ollama Docker setup** (tool)
  - https://github.com/mythrantic/ollama-docker
  - *From: triquichoque*

- **ComfyUI-Logic nodes hash** (node)
  - *From: samhodge*

- **ComfyUI-LogicUtils v1.7.2** (repo)
  - https://github.com/aria1th/ComfyUI-LogicUtils
  - *From: triquichoque*

- **WAN22.XX_Palingenesis base model** (model)
  - https://huggingface.co/eddy1111111/WAN22.XX_Palingenesis
  - *From: Phr00t*

- **ComfyUI-Impact-Pack fork for WAN workflows** (repo)
  - https://github.com/drozbay/ComfyUI-Impact-Pack
  - *From: Ablejones*

- **Transition workflow** (workflow)
  - *From: ingi // SYSTMS*

- **V6.2 Music video workflow** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows
  - *From: WackyWindsurfer*

- **VACE start to end node** (node)
  - *From: Piblarg*

- **Groq API for LLM** (api)
  - https://console.groq.com/home
  - *From: JohnDopamine*

- **Qwen Rapid AIO model** (model)
  - https://huggingface.co/Phr00t/Qwen-Rapid-AIO
  - *From: Phr00t*

- **DeJPG upscaler model** (model)
  - *From: Cseti*

- **4xclearreality upscaler** (model)
  - *From: Cseti*

- **SunoAI API options** (api)
  - https://sunoapi.com/en/pricing
  - *From: Scruffy*

- **Suno official API** (repo)
  - https://github.com/suno-ai/hackmit-starter-app
  - *From: Scruffy*

- **VRGameDevGirl's workflows repository** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lan8mark's WAN 2.2 tuning guide** (guide)
  - *From: Lan8mark*

- **Lan8mark's latent upscale guide** (guide)
  - *From: Lan8mark*

- **ControlFlowUtils for branching logic** (repo)
  - https://github.com/VykosX/ControlFlowUtils
  - *From: Scruffy*

- **Ostris training guide** (guide)
  - https://www.youtube.com/watch?v=d_b3GFFaui0
  - *From: pom*

- **Face detailer LoRA** (lora)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Qwen 4 Play LoRA** (lora)
  - https://civitai.com/models/2004155/qwen-4-play
  - *From: Phr00t*

- **VRGameDevGirl V7 Workflow** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **UniMMVSR research paper** (research)
  - https://shiandu.github.io/UniMMVSR-website/
  - *From: yi*

- **ComfyUI-Impact-Pack** (custom node)
  - https://github.com/ltdrdata/ComfyUI-Impact-Pack
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGameDevGirl workflows V7.1** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **VibeVoice TTS** (tool)
  - *From: Chandler ✨ 🎈*

- **Charlie's WAN 2.1 14B LoRA - Punk Style** (lora)
  - https://huggingface.co/Charlietooth/wan2.1-14B-lora-punk-style
  - *From: Charlie*

- **Sonauto AI music generator** (tool)
  - *From: smithyIAN - 4080ti Super 16gig*

- **MelBandRoFormer models** (model)
  - https://huggingface.co/Kijai/MelBandRoFormer_comfy/tree/main
  - *From: Mazrael.Shib*

- **VRGameDevGirl Workflow V7.1** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **New LightX2V LoRA** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/tree/main/loras
  - *From: Chandler ✨ 🎈*

- **Claude Desktop with Code access** (tool)
  - https://docs.claude.com/en/docs/claude-code/setup
  - *From: Janosch Simon*

- **SeedVR2 Video Upscaler** (repo)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler
  - *From: pom*

- **Ollama API Proxy** (tool)
  - https://github.com/xrip/ollama-api-proxy
  - *From: triquichoque*

- **WAN2.2-14B-Rapid-AllInOne-GGUF** (model)
  - https://huggingface.co/patientxtr/WAN2.2-14B-Rapid-AllInOne-GGUF/tree/main
  - *From: patientx*

- **ComfyUI-Whisper for subtitles** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Whisper
  - *From: Scruffy*

- **Wan 2.1 Knowledge Base** (resource)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481cd852cde21e16a7206
  - *From: brbbbq*

- **NotebookLM Banodoco Wan KB** (resource)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: brbbbq*

- **Workflow v8 embedded** (workflow)
  - *From: Cseti*

- **ComfyUI-Upscaler-Tensorrt** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt
  - *From: Tachyon*

- **Music Video Prompt Crafter GPT** (tool)
  - https://chatgpt.com/g/g-68eee927f1988191988c9250fa7bd5e1-music-video-prompt-crafter
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo model by eddy1111111** (model)
  - https://huggingface.co/eddy1111111/humo/tree/main
  - *From: dashixiong*

- **WAN2.2 Mega Rapid AIO** (workflow)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: Phr00t*

- **Looping node discussion** (tool)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/discussions/100
  - *From: Phr00t*

- **VRGameDevGirl84 Discord server** (community)
  - https://discord.gg/FJ9VvCDXw3
  - *From: VRGameDevGirl84(RTX 5090)*

- **Training data for LoRA** (dataset)
  - https://drive.google.com/file/d/1TX4BRvJGDjdQ3CswXq9r60jkRoGYHHNw/view?usp=sharing
  - *From: Flipping Sigmas*

- **Prompter V2** (tool)
  - https://prompter-v2.vercel.app/
  - *From: thaakeno*

- **ComfyUI-BS-Textchop node** (node)
  - https://github.com/Burgstall-labs/ComfyUI-BS-Textchop
  - *From: burgstall*

- **ComfyUI-Gemini_Flash_2.0_Exp node** (node)
  - https://github.com/Burgstall-labs/ComfyUI-Gemini_Flash_2.0_Exp
  - *From: burgstall*

- **WAN 2.2 GGUF workflow for 24GB** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/WAN2.2_GGUF_UPSCALER_14B.json
  - *From: thaakeno*

- **Fat JD Vance LoRA for Wan2.1** (lora)
  - https://huggingface.co/huwhitememes/fatjdvance_v1-wan2.1
  - *From: huwhitememes ✦ MKS*

- **Fat JD Vance LoRA for Qwen** (lora)
  - https://huggingface.co/huwhitememes/fatjdvance_v1-qwen_image
  - *From: huwhitememes ✦ MKS*

- **HuMo workflow support discord** (community)
  - https://discord.gg/FJ9VvCDXw3
  - *From: VRGameDevGirl84(RTX 5090)*

- **Comprehensive Wan models spreadsheet** (reference)
  - https://docs.google.com/spreadsheets/d/1HvJ5_ZAzx0Dmw_mifdj1sx2nyIIXoUmqUYj30sMlJpI/edit?usp=sharing
  - *From: Koba*

- **SVI LoRAs for Wan 2.2** (lora)
  - https://huggingface.co/vita-video-gen/svi-model/tree/main/version-2.0
  - *From: PATATAJEC*

- **ComfyUI-PainterLongVideo** (node)
  - https://github.com/princepainter/ComfyUI-PainterLongVideo
  - *From: Dream Making*

- **Wan2.2-I2V-A14B-GGUF Q6** (model)
  - https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/tree/main
  - *From: Flipping Sigmas*

- **ComfyUI-Humo_Lipsync_Suppress** (node)
  - https://github.com/ckinpdx/ComfyUI-Humo_Lipsync_Suppress
  - *From: Chandler ✨ 🎈*

- **Water Morphing Wan LoRA** (lora)
  - https://huggingface.co/Ashmotv/water_morping_wan
  - *From: AshmoTV*

- **Wan2.2 AnimateDiff LoRA** (lora)
  - https://civitai.com/models/2207829/wan22-animatediff-lora
  - *From: ReDiff*

- **ImageSorter tool** (tool)
  - https://github.com/filliptm/ImageSorter
  - *From: Scruffy*

- **HuMo audio-motion ComfyUI nodes** (repo)
  - https://github.com/ckinpdx/comfyui-humo-audio-motion
  - *From: Chandler ✨ 🎈*

- **WanExperiments nodes** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **Infi-var-L LoRA** (model)
  - https://civitai.com/models/1811141?modelVersionId=2098713
  - *From: Flipping Sigmas*

- **Ollama tutorial by Pixaroma** (tutorial)
  - https://www.youtube.com/watch?v=eK6MXm7q37c
  - *From: JohnnyLongBalls*

- **LightX2V Wan2.2 LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/tree/main/loras
  - *From: aiacsp*

- **Curated AnimatedDiff dataset** (dataset)
  - https://drive.google.com/drive/folders/1WPvl-UjENJQ_Kf-5BXm8fbta9RQgI636
  - *From: pom*

- **VRGameDevGirl84 Discord server** (community)
  - https://discord.gg/B3yp9wste
  - *From: VRGameDevGirl84(RTX 5090)*

- **Paint smear LoRA** (lora)
  - https://huggingface.co/Ashmotv/paint_smear
  - *From: AshmoTV*

- **OmniAvatar LoRA for lipsync** (lora)
  - https://huggingface.co/OmniAvatar/OmniAvatar-14B
  - *From: Elvaxorn*

- **WanExperiments nodes** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Elliryk*

- **Chain sampling explanation video** (tutorial)
  - https://youtu.be/A6CXfW4XaKs?t=109
  - *From: Ablejones*

- **V5.1c workflow** (workflow)
  - *From: Ablejones*

- **V6.1d workflow** (workflow)
  - *From: Ablejones*

- **Wan2_1_VAE_bf16.safetensors** (model)
  - *From: Ablejones*

- **wan_2.1_vae.safetensors** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/vae/wan_2.1_vae.safetensors
  - *From: Ablejones*

- **SYSTMS INFL8 LoRA** (lora)
  - https://huggingface.co/systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511
  - *From: ingi // SYSTMS*

- **Voice samples collection** (resource)
  - https://rentry.org/Voice-Samples
  - *From: drbaph*

- **Knitting effect LoRA** (lora)
  - https://huggingface.co/Ashmotv/knitting_effect
  - *From: AshmoTV*

- **Wan Prompt Scheduling node** (node)
  - https://github.com/AtomicPerception/ap_Nodes/blob/main/ap_wan_scheduled_conditioning.py
  - *From: atom.p*

- **TTM (Time2Move) workflow** (workflow)
  - https://github.com/rik-python/AI-Time2Move-Comfyui
  - *From: AshmoTV*

- **SYSTMS INFL8 LoRA** (model)
  - https://huggingface.co/systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511/tree/main
  - *From: ingi // SYSTMS*

- **Motion LoRAs collection** (model)
  - https://huggingface.co/peteromallet/ad_motion_loras/tree/main
  - *From: atom.p*


## Known Limitations

- **Progressive quality degradation**
  - Multiple generations cause gradual color shift and quality loss like copying VHS tapes
  - *From: Ablejones*

- **Scene consistency test challenges**
  - Static scenes like windmills are torture tests that reveal coherence and color issues more easily
  - *From: Ablejones*

- **Motion reduction in subsequent passes**
  - Each continuation pass tends to reduce overall motion in the generated video
  - *From: The Shadow (NYC)*

- **LLM complex prompt handling**
  - MMAudio doesn't handle complex prompts well, just does 'stuff' instead of following detailed instructions
  - *From: Tango Adorbo*

- **TensorRT compatibility**
  - TensorRT nodes not working on RTX 5090 yet, despite excellent performance on older cards
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE iterates on itself without masking**
  - When not using masking, VACE adds more detail at each sampler making transitions obvious
  - *From: the_darkwatarus_museum*

- **Prompt changes have limited effect in continuation**
  - Residual self-attention makes dramatic prompt changes only slightly vary the result
  - *From: Ablejones*

- **LightX affects prompt adherence**
  - Reduces realism and can cause unwanted camera artifacts when 'camera' mentioned
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk has no optimizations**
  - Pretty big memory usage, needed 65 frame chunks
  - *From: Tango Adorbo*

- **ComfyUI poor at looping**
  - Visual coding tools always struggle with loop implementations
  - *From: fredbliss*

- **LoRAs tend to distort outputs more with each successive 5 second clip**
  - Original problem trying to solve with depth control as sanity check
  - *From: Faust-SiN*

- **Lotus has quite the flicker factor**
  - Unless doing something wrong, Lotus produces flickering
  - *From: Faust-SiN*

- **VACE wasn't trained to take normals as input**
  - Can trick it into using them as depth but needs processing
  - *From: Faust-SiN*

- **Control video sometimes gets ignored with certain strength settings**
  - At VACE encode strength 0.5, control video may be ignored
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt adherence issues in long generations**
  - Video gets stuck at first prompt, doesn't change like prompts specify character changes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pusa kills motion when combined with LightXv2**
  - Requires additional LoRAs like reward, motion boost, movie gen to restore motion
  - *From: Hashu*

- **Phantom limited to 4 reference images**
  - Can work around by using collages of multiple characters per image slot
  - *From: Ablejones*

- **GGUF models incompatible with VACE module in native**
  - Need to use merged models or wrapper workflows instead
  - *From: mdkb*

- **WAN better for realistic content than creative/stylized**
  - Struggles with creative or highly stylized prompts compared to realistic content
  - *From: N0NSens*

- **Pusa mostly trained on live action**
  - Probably won't help much with 2D or stylized content
  - *From: Tango Adorbo*

- **VACE and Phantom cannot work with i2v models**
  - Not possible to make them work together with i2v models
  - *From: Ablejones*

- **Color changes from video to video in extensions**
  - Everyone still having issues with colors changing from video to video when extending
  - *From: Ablejones*

- **Wan 2.2 still limited to 5s videos**
  - Only 81 frames at 16fps work smoothly, going past requires Context Window Options which takes much longer
  - *From: thaakeno*

- **Control inputs can affect character likeness**
  - Openpose, canny, depth can affect character likeness by forcing landmarks that may not match the character
  - *From: Ablejones*

- **VACE has issues with chaining samplers**
  - Noticeable change in first frame when taking last frame of one sampler as first frame of next, unlike Wan2.2 i2v which handles this flawlessly
  - *From: the_darkwatarus_museum*

- **Fun Control model doesn't work well for continuation**
  - Creates bright flashes to hide scene changes, model resists this usage
  - *From: Ablejones*

- **FaceDetailer doesn't work with videos**
  - Only works with images, not compatible with Phantom or VACE models currently
  - *From: xwsswww*

- **Impact Pack treats video frames as separate images**
  - Detailer for Video nodes encode each frame separately like AnimateDiff instead of treating as 5D tensor
  - *From: Ablejones*

- **LoRAs need retraining for Phantom base**
  - Need to retrain with Phantom as base model for best effect
  - *From: Piblarg*

- **VACE integration with detailer is fragile**
  - Very fragile, doesn't work well yet, lots of size errors
  - *From: Ablejones*

- **VACE causes over-contrast issues**
  - Tends to create contrast problems in output
  - *From: Ablejones*

- **Open pose control is weak on VACE model**
  - Needs extra strength, not surprising given the model architecture
  - *From: Ablejones*

- **Some samplers don't handle end frame transitions well**
  - They sort of fade into the next frame instead of clean transitions
  - *From: Ablejones*

- **Context windows don't work with HuMo**
  - Only drawback compared to Infinite talk
  - *From: JmySff*

- **Color drift with VACE extensions is intrinsic**
  - Will happen and depends heavily on the specific video being processed
  - *From: Ablejones*

- **Phantom resemblance depends on source similarity**
  - Gets much worse if resolution of subject decreases (far from camera)
  - *From: Ablejones*

- **No magic workflow for perfect character upscaling**
  - Each video requires parameter tweaking, no universal settings that work perfectly for all content
  - *From: Ablejones*

- **Progressive degradation in long videos**
  - Even with careful controls, video quality and character consistency degrade over time, though 2.2 is better than 2.1
  - *From: Ablejones*

- **Res4lyf samplers not optimized for 4 steps**
  - These samplers were designed for higher step counts, may need adjustments for 4-step sampling
  - *From: Ablejones*

- **Native ancestral samplers fail with WAN models at low steps**
  - Many built-in sde/ancestral samplers completely fail with WAN models, especially at low step counts
  - *From: Ablejones*

- **HUMO 3 second limit**
  - HUMO typically limited to 3 seconds though some users report success with longer generations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Style transfer doesn't work well for video**
  - T2I style transfer workflow doesn't translate as well when applied to video generation
  - *From: Ablejones*

- **VACE I2V consistency**
  - Mega versions might have VACE limitation for I2V consistency compared to dedicated I2V models
  - *From: Phr00t*

- **Fixed duration requirement**
  - Workflow requires hardcoded 3.88s duration per scene to avoid loop dependency issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **End frame ignored in Mega v4**
  - Mega v4 seems to ignore end frame parameter and only uses start frame
  - *From: Blink*

- **Style transfer at low steps**
  - Cannot effectively inject style transfer at low steps (<6), switches to I2V mode using style reference instead of intended input reference
  - *From: The Shadow (NYC)*

- **Mouth movement during silence**
  - Sometimes lip sync shows mouth movement during silent parts of audio, inconsistent behavior
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multi-voice and harmony handling**
  - Songs with multiple voices and harmonies are more challenging to process properly
  - *From: samhodge*

- **Audio sync issues in longer videos**
  - Next run doesn't start exactly where last one left off, causing sync drift
  - *From: VRGameDevGirl84(RTX 5090)*

- **Whisper transcription accuracy**
  - Not perfect, especially for non-English songs - produces phonetic approximations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Can't auto-disable groups in ComfyUI**
  - No way found to programmatically disable workflow groups, requires manual intervention
  - *From: VRGameDevGirl84(RTX 5090)*

- **Transitions don't always work**
  - Struggle with completely unrelated content, need common elements like similar person/color/shape
  - *From: ingi // SYSTMS*

- **ComfyUI audio file picker doesn't work with subfolders**
  - JS limitations prevent subfolder organization of audio files
  - *From: VRGameDevGirl84(RTX 5090)*

- **Character degradation in extended videos**
  - VACE extend process has intrinsic character degradation, more visible on darker videos
  - *From: Ablejones*

- **Motion and color degradation over time**
  - Pure T2V with repeated prompts shows color and motion degradation coinciding
  - *From: garbus*

- **First few frames issues with longer videos**
  - Can do longer than 3.88 seconds but first few frames are funky
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio sync degradation over time**
  - Later parts of video show mouth not fully in sync with audio
  - *From: VRGameDevGirl84(RTX 5090)*

- **Complex instructions for local LLMs**
  - Instructions might be too complex for open source local LLMs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Upscaling removes lip sync**
  - Upscaling workflows typically remove the lip sync functionality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio sync drift in long videos**
  - Gradual desync between audio and video that becomes noticeable in videos over ~3 minutes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Slow motion with fast LoRAs on WAN 2.2**
  - Using speed LoRAs with WAN 2.2 causes slow motion effects
  - *From: kendrick*

- **Random mouth movement during silence**
  - HUMO can cause mouth movement even during non-vocal sections, hard to completely control
  - *From: VRGameDevGirl84(RTX 5090)*

- **Inconsistent backgrounds across scenes**
  - Even with same prompts, backgrounds can vary between video segments
  - *From: WackyWindsurfer*

- **Index node bug with 2-run videos**
  - Workflow doesn't properly track index for videos requiring only 2 runs
  - *From: hudson223*

- **LLM prompt count inconsistency**
  - LLM sometimes sends 12 instead of 16 prompts, causing incomplete video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI flow control limitations**
  - Cannot branch execution during runtime, cannot programmatically control node groups
  - *From: triquichoque*

- **Sage attention compatibility**
  - Some models like QwenEdit produce black outputs when sage attention is enabled
  - *From: Trentino*

- **HuMo strongly follows reference image**
  - Full body nude references override clothing prompts, better to use headshots only
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio sync issues get progressively worse in longer videos**
  - Sync problems compound over time, noticeable after 1:30, very apparent by end of long videos
  - *From: hudson223/WackyWindsurfer*

- **RES4LYF samplers take significant time to run**
  - Warning that these samplers are time-intensive but provide lots of control
  - *From: vanhex*

- **4-second duration produces incorrect frame count**
  - Generates 97 frames instead of expected 100 frames (4 seconds * 25 FPS), cause unknown
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lip-sync degrades during final video combination**
  - Individual segments maintain good sync but final combined video loses synchronization
  - *From: WackyWindsurfer*

- **English language lip-sync quality**
  - English produces less natural lip-sync compared to Chinese, French, and other languages
  - *From: Janosch Simon*

- **Face burning in VACE extensions**
  - Faces become 'baked potatoes' after 3-5 iterations in video extension workflows
  - *From: lostintranslation*

- **Small detail flickering in WAN**
  - Model struggles with small details causing temporal inconsistency in hair, textures, and fine elements
  - *From: HeadOfOliver*

- **Local LLMs struggle with complex prompt generation**
  - Models like Meta Llama can't handle the complexity needed for proper prompt creation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face consistency issues during upscaling**
  - Original face changes too much during upscaling passes
  - *From: D-EFFECTS*

- **Whisper transcription errors with rap/complex lyrics**
  - Difficult to understand lyrics get transcribed incorrectly
  - *From: J_Pyxal*

- **SeedVR upscaling creates artifacts without proper noise settings**
  - Need to add noise before upscaling to prevent artifacts
  - *From: ingi // SYSTMS*

- **Cannot queue multiple songs**
  - Can only do one song at a time, no way to queue different songs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Small cuts between scenes unavoidable**
  - Each generation starts with reference image causing small jumps back to character at rest
  - *From: Chandler ✨ 🎈*

- **Local LLMs don't understand complex instructions well**
  - Instructions are very complex and local models don't work as well as external APIs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Color space shifts to olive green/grey**
  - Model tends to change color space, color match only works to certain degree
  - *From: Mandulis - Max - 2/2*

- **VACE 2.2 context handling issues**
  - Context handling and 21:9 support still break, feels rough around edges
  - *From: yo9o*

- **I2V not picking up reference images**
  - When trying to use as I2V, it isn't 'picking' up the image and just doing T2V instead
  - *From: cocktailprawn1212*

- **Humo resolution limit**
  - Things get weird over 720x1280, features start changing at 720x1.3, body stretches at 720x1.5
  - *From: Chandler ✨ 🎈*

- **Model can't use everything in prompt**
  - If there's too much detail going on, model can't process all prompt elements
  - *From: VRGameDevGirl84(RTX 5090)*

- **Can't preserve exact elements in transitions**
  - Takes a lot of creative liberties in transitions and can quickly move away from your inputs
  - *From: brbbbq*

- **Context Options too slow for practical use**
  - Works past 81 frames but generation times are way too long to be useful
  - *From: thaakeno*

- **WAN 2.2 breaks Phantom compatibility**
  - 2.2 basically breaks phantom, could not see a benefit when used together
  - *From: Piblarg*

- **Multiple references not well supported**
  - Probably wasn't trained to use more than 1 reference per character
  - *From: Ablejones*

- **Latent space upscaling causes artifacts**
  - All latent space upscalers cause ghosting/doubling effects
  - *From: mdkb*

- **6 seconds can cause frame burning**
  - 6 seconds can cause the first few frames to be burnt
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo doesn't work well with longer than 4 seconds**
  - Anything over ~4 seconds produces poor quality results
  - *From: burgstall*

- **Phr00t's AIO not designed for fast motions**
  - Model is designed for ease of use and speed, but fast motion is one of the downsides
  - *From: Phr00t*

- **LightX LoRA causes unavoidable lip movements**
  - Almost no way to make characters stop lip movements when LightX LoRA is involved
  - *From: Ablejones*

- **Wan S2V produces poor quality**
  - Multiple users report Wan 2.2 S2V looks like shit compared to alternatives
  - *From: Mazrael.Shib*

- **HuMo cannot replace large mouth movements**
  - After first stage with Wan 2.2 HN, HuMo second stage not able to replace large movements like Shrek's mouth
  - *From: Ablejones*

- **Wan 2.2 models don't have clipvision layers**
  - Clipvision input literally doesn't do anything with Wan 2.2 models
  - *From: Ablejones*

- **Most SVI models need specific input preparation**
  - Often aren't compatible with each other due to specific requirements
  - *From: Ablejones*

- **GGUF models produce blocky look**
  - User reports blocky appearance that can't be eliminated with GGUF versions
  - *From: Stanley*

- **Batch processing creates noise level mismatches**
  - When upscaling long sequences in batches, start of each batch appears much noisier than end of previous batch
  - *From: Bernie 'Hot Dog' Madoff*

- **I2V augmentation doesn't work with SVI**
  - Motion scale does very little for SVI Pro because of how image channels are set up, breaks video at high strength
  - *From: Ablejones*

- **SVI extensions not very dynamic**
  - SVI stages need aggressive prompting to get movement beyond their anchor image
  - *From: Ablejones*

- **Workflow is seed sensitive**
  - May need to try different seeds if specific segment doesn't look right or have good lip sync
  - *From: Ablejones*

- **Quality degradation over long extensions**
  - Videos start degrading noticeably after 20+ seconds, may need face swapping
  - *From: craftogrammer 🟢*

- **ComfyUI_essentials package causing widespread issues**
  - Package in maintenance mode for 9 months, causing node failures and compatibility problems
  - *From: mdkb*

- **HuMo lip sync very seed-dependent**
  - Performance quality varies significantly with different seeds, requires manual checking and iteration
  - *From: Ablejones*

- **Wan 2.2 aggressive end frame transitions**
  - Model tends to make harsh transitions to final frames, requires lora strength adjustment
  - *From: SL3ND3R*

- **VACE and HuMo fundamentally incompatible**
  - Cannot use VACE+HuMo simultaneously in same sampling, must split or do separate passes
  - *From: Ablejones*

- **FP8 fast model artifacts**
  - Removing parts of model can get unique results but creates artifacts and suffers lip sync quality
  - *From: hudson223*

- **Fun VACE 2.2 struggles with inpainting tasks**
  - Not as good as original VACE for inpainting, forgot some capabilities while gaining others like better pose control
  - *From: Ablejones*

- **HuMo quality degrades with distance and size**
  - Has harder time when subject moves farther away or is smaller in frame, leading to quality degradation in longer extensions
  - *From: Ablejones*

- **No frame-perfect scheduling in Wan**
  - Cannot easily assign specific prompts to exact frame numbers like AnimateDiff - limited to granularity of context windows (blocks of ~81 frames)
  - *From: Flipping Sigmas*


## Hardware Requirements

- **4060Ti 16GB performance**
  - Takes very long time for generation, requires block swap and lower resolution
  - *From: victor*

- **RTX 5090 TensorRT compatibility**
  - TensorRT nodes not working yet on RTX 5090, was working on previous hardware
  - *From: VRGameDevGirl84(RTX 5090)*

- **TensorRT interpolation speed**
  - 2 seconds to interpolate a 300 frame video on RTX 4080
  - *From: Ablejones*

- **Generation time for 36 second video**
  - 1093.91 seconds (18+ minutes) for processing on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRAM for upscaling**
  - Can do 48 frames before OOM on 3090ti 24GB VRAM/96GB RAM, over 600 frames possible with context options at 0.5 denoise
  - *From: drmbt*

- **4K+ upscaling**
  - Confirmed working on patched tiled sampler with VRAM optimizations
  - *From: .tarkan*

- **1920x1080 generation**
  - Possible with divisible by 16 and block swapping to 40
  - *From: VRGameDevGirl84(RTX 5090)*

- **Performance timing**
  - 129 frames at 1024x576 with 3 steps took 393 seconds on 3090
  - *From: burgstall*

- **VRAM for 81 frames**
  - Doable but packs up RAM and VRAM close to limits
  - *From: Tango Adorbo*

- **597 frames at 576x1024**
  - Took 13 minutes with 3 steps, max allocated 12.874 GB VRAM
  - *From: craftogrammer*

- **High VRAM setup still has limits**
  - 96GB GPU with 100GB RAM couldn't upscale 1920x1080 150 frames without context options
  - *From: AmirKerr*

- **Single GPU development limitations**
  - Need 8x5090 rack for proper development workflow with model loading times
  - *From: Clownshark Batwing*

- **33 frames video memory usage**
  - Takes up ~196MB RAM in ComfyUI due to 33*960*540*4*3 bytes calculation
  - *From: Elriel*

- **16GB VRAM sufficient for most workflows**
  - Can run almost any of these models unless doing 720p at 121 frames
  - *From: Ablejones*

- **Shared VRAM performance impact**
  - Generation time goes up 20x when using shared VRAM
  - *From: Ablejones*

- **24GB VRAM can still get OOM**
  - Native workflows can cause OOM even on RTX 4090 24GB due to memory estimation issues
  - *From: avataraim*

- **VRAM for frame count**
  - 16GB VRAM can get OOM with aggressive workflows, especially with high frame counts
  - *From: Ablejones*

- **RTX 3060 capabilities**
  - Can run 832x480x121 frames at 24fps in 15 minutes with VACE+Phantom merge, but struggles above 480p in some workflows
  - *From: mdkb*

- **RTX 5070 limitations**
  - OOMs above 81 frames
  - *From: MarkDalias*

- **RTX 5090 performance**
  - Q4_K_M model takes ~105s per sampler at default resolution without blockswap on 24GB VRAM
  - *From: thaakeno*

- **Block swap settings for low VRAM**
  - Specific torch and block swap configurations help with low VRAM management
  - *From: mdkb*

- **3060 RTX performance**
  - 832x480x121 frames at 24fps in 18 minutes, 1600x900x81 upscaler in 30 minutes
  - *From: mdkb*

- **16GB VRAM settings**
  - Use buffer_gb: 2.00, model_threshold_gb: 10.00 for stable operation
  - *From: Ablejones*

- **Paging file size for RAM management**
  - Need adequate paging file size when RAM doesn't offload properly after ksampler
  - *From: Ablejones*

- **VRAM for generation**
  - 24GB A5000 can run with blockswap, may need memory management tricks
  - *From: Slavrix*

- **RAM for blockswap**
  - 124GB RAM available for blockswap operations on test machine
  - *From: Slavrix*

- **Memory management**
  - Can use blockswap node instead of clearing cache if you have enough RAM
  - *From: thaakeno*

- **VRAM usage with chained workflows**
  - Complex workflows with multiple controls can push even high-end cards to their limits, sometimes requiring runpod even for high-end hardware
  - *From: JalenBrunson*

- **Low-end system performance**
  - A4500 with 24GB VRAM and 28GB system RAM can handle 81 frames at 832x480, takes ~24 minutes but works
  - *From: The Shadow (NYC)*

- **System RAM importance**
  - 28GB system RAM is limiting factor, modern OS handles swapping well but insufficient swap file causes failures
  - *From: The Shadow (NYC)*

- **Sampling speed with res4lyf**
  - lobatto_iiid_3s at 389s/iteration for 81 frames, 3 model calls per step makes it very slow but high quality
  - *From: pom*

- **3090 performance**
  - 720x720 49 frames in just over 2 minutes, 81 frames in 189 seconds when warm
  - *From: burgstall*

- **24GB VRAM for HUMO long-form**
  - 150 frames at 1024x576 works on 24GB, 1280x720 doesn't fit but would work on 5090
  - *From: Juan Gea*

- **48GB VRAM availability**
  - User reports having 48GB VRAM available for testing
  - *From: samhodge*

- **48GB VRAM for local LLM**
  - Can easily run gemma2.5-VL in ollama locally with 48GB VRAM
  - *From: triquichoque*

- **4090 GPU performance**
  - Pretty advanced workflow runs on 4090
  - *From: Janosch Simon*

- **RAM usage for transitions**
  - Up to 80%+ of 96GB RAM at max model strength
  - *From: ingi // SYSTMS*

- **Processing time on RTX 5090**
  - 565 seconds for first run, 503 seconds for second run
  - *From: Simon*

- **RAM upgrade recommendation**
  - 64GB not enough, need 128GB for complex workflows
  - *From: Charlie*

- **RAM usage for upscaling workflow**
  - Uses around 100GB RAM - can be lowered by using fewer passes or bypassing image upscales
  - *From: Cseti*

- **16GB VRAM upscaling capability**
  - Workflow optimized for 16GB VRAM - can upscale 81 frames to 1080p, better cards can do more frames or higher resolution
  - *From: Cseti*

- **Generation time on RTX 5090**
  - 10-15 seconds or faster for Qwen AIO
  - *From: Phr00t*

- **Generation time on mobile 4080**
  - 30 seconds or less for Qwen AIO on 12GB mobile 4080
  - *From: Phr00t*

- **Upscaling time**
  - 5 minutes for 100 frames using wan2.2 upscale workflow
  - *From: Santoshyandhe*

- **5090 performance**
  - 1 hour for 5 minute video at 720x480, 768x768 taking 128s vs expected 45s
  - *From: VRGameDevGirl84(RTX 5090)*

- **16GB VRAM for upscaling**
  - Need context options node to fit upscaling workflow in 16GB VRAM
  - *From: Cseti*

- **4K output file sizes**
  - 4K output was 21GB, considered overkill
  - *From: hudson223*

- **10sec upscale from 480p to 720p**
  - 16GB VRAM without face detailer
  - *From: Cseti*

- **128GB RAM sometimes insufficient**
  - OOMing on 1/3 of generations with face detailer upscaling nodes even with 128GB RAM
  - *From: ingi // SYSTMS/Cseti*

- **2-minute 50-second video generation**
  - Single pass using RTX 4090
  - *From: huangkun1985*

- **1x upscale + 2x interpolation**
  - Doubles generation time, most added time is in RIFE interpolation
  - *From: Chandler*

- **Audio generation cost**
  - $5 lasts weeks of daily testing with VibeVoice/similar services
  - *From: VRGameDevGirl84(RTX 5090)*

- **High VRAM optimization**
  - With 96GB VRAM, load main model on main device, use BF16 for WAN 2.2, FP32 for VAE/text encoder
  - *From: ingi // SYSTMS*

- **VRAM usage for SeedVR upscaling**
  - 832x480 video 161 frames: ~38GB first run, 64GB second run
  - *From: Dever*

- **High resolution generation VRAM**
  - 1280x720 topped at 96% VRAM usage on RTX 5090
  - *From: Chandler ✨ 🎈*

- **CPU RAM for concatenation**
  - Video concatenation can use all 96GB RAM available
  - *From: Chandler ✨ 🎈*

- **GPU thermal issues above 23GB**
  - RTX 3090 doesn't reach 60°C when using >23GB VRAM, fans don't spin properly
  - *From: Ashtar*

- **4090 performance**
  - 4 hours for full music video generation
  - *From: Hueman Instrument*

- **5090 optimal settings**
  - 81 frames, 2 passes, longest side 960px with teacache + sageattention at VRAM limit
  - *From: Mandulis - Max - 2/2*

- **5090 generation time**
  - 30 minutes for 3-4 minute videos, 4-5 minutes per 41 frames when optimized
  - *From: Mazrael.Shib*

- **3090 compatibility**
  - Can run with gguf models and 64GB RAM, fp8 models don't work
  - *From: BestWind*

- **LLM VRAM usage**
  - LLMs use VRAM equal to file size - 14GB model needs >14GB VRAM to load
  - *From: Chandler ✨ 🎈*

- **VRAM scaling**
  - 64GB RAM enough for 1280x720, 8 steps with block swapping on RTX 5090
  - *From: WackyWindsurfer*

- **Performance benchmark**
  - RTX 5090: 45 minutes for 16 segments at 1280x720 with LightX 8 steps (produces 1m04s clip)
  - *From: WackyWindsurfer*

- **Cloud pricing**
  - 48GB L40S for 40 cents/hour, can generate 720p song for under $5, 50c per minute of 720p footage
  - *From: samhodge*

- **Length vs VRAM**
  - Longer than 81 frames causes exponential slowdown due to VRAM limits or RAM swapping
  - *From: cocktailprawn1212*

- **Driver compatibility**
  - RTX 5060ti 16GB works with v570 drivers on Ubuntu, v580 drivers still not working properly
  - *From: Scruffy*

- **RTX 3060 performance**
  - 720p in 16 minutes using dual model workflow with 360p HN pass and 4 steps each
  - *From: mdkb*

- **RTX 5090 performance**
  - Around 60s per sampling step, 30s for preprocessing/decoding at 720p
  - *From: jellybean5361*

- **24GB VRAM settings**
  - Use block swap set to 30, can run Q4_K_M model workflow
  - *From: thaakeno*

- **16GB VRAM (4060ti)**
  - 4 hours per 4 second video without swap, need sage/triton fixes for decent speed
  - *From: cimetsys*

- **4080 Super performance**
  - 750 seconds for 1 minute generation, working more efficiently than previous versions
  - *From: AJO*

- **VRAM for Flipping Sigmas V2 workflow**
  - Even RTX 5090 users getting OOM errors, may need to run upscale as separate flow
  - *From: Henque*

- **RTX 5090 settings**
  - Default settings work, disable block swap, can use fp8 models
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap needed for fp16 models on RTX 5090**
  - Block swap required when using fp16 versions even on high-end hardware
  - *From: hudson223*

- **96GB RAM limitation**
  - 96GB DDR5 may not be enough for 720p combine stage, crashed during video combination
  - *From: burgstall*

- **RTX 5090 performance**
  - 85 seconds to generate 81 frames at 720x720
  - *From: burgstall*

- **RTX 4090 with Wan2.2 14B models**
  - Gets OOM with 28GB full model, needs to use GGUF version
  - *From: Stanley*

- **RTX 3090 limitations**
  - Can't get past 2nd upscaler due to OOM even with 40 block swaps, needs lighter models or GGUF
  - *From: dj47*

- **L40S specifications**
  - 48GB VRAM, 64GB RAM - handles complex workflows without memory issues
  - *From: BarleyFarmer*

- **Low VRAM compatibility**
  - Workflow can handle really low frame count (40 frames each extension) and low VRAM
  - *From: Mr_J*

- **VRAM usage scales with frames and resolution**
  - 3090 24GB can handle 13 second video at 25fps 480p. 5090 with 128GB RAM should handle 40+ seconds
  - *From: TimHannan, NebSH*

- **12GB cards can run Wan 2.1 1.3B version**
  - Can generate 49-97 frames at 360x480 resolution with reduced quality
  - *From: atom.p*

- **RAM management critical for long videos**
  - ComfyUI caches node outputs, eventually runs out of memory. Use --no-cache or remove preview nodes
  - *From: Ablejones*

- **Generation speed with Sage Attention**
  - Speed improved from 22 seconds to 14-15 seconds per iteration
  - *From: craftogrammer 🟢*

- **VRAM usage comparison**
  - GGUF Q5KM: avg 14.2GB VRAM, FP8_scaled: avg 15.5GB VRAM with sage attention
  - *From: craftogrammer 🟢*

- **System setup for stability**
  - Windows 11 WSL2 (Ubuntu) gets fewer weird issues than native Windows, no speed penalties
  - *From: craftogrammer 🟢*

- **CUDA and PyTorch versions**
  - CUDA 13, PyTorch 2.9.1+cu130, Python 3.12.3 for cutting edge stability
  - *From: craftogrammer 🟢*

- **3060 RTX limitations**
  - Older hardware with sage attention 1 and torch 2.7 may have compatibility issues with essentials
  - *From: mdkb*

- **12GB VRAM insufficient for certain workflows**
  - Gets OOM every time with some advanced workflows, need to use Wan 2.1 instead of 2.2 or simplified approaches
  - *From: atom.p*

- **RTX 5090 and RTX PRO 6000 WS potential multi-GPU setup**
  - Could potentially work together for nice performance boost
  - *From: HeadOfOliver*


## Community Creations

- **Start to End Frame node** (node)
  - Node that helps with frame extraction and continuation workflows
  - *From: pom*

- **FusionX VACE model** (model)
  - Distilled merge that provides excellent quality with faster generation times
  - *From: VRGameDevGirl84(RTX 5090)*

- **Native VACE workflow variants** (workflow)
  - KSampler and RES4LYF variants of the endless travel workflow
  - *From: Ablejones*

- **Workflow with individual prompts per sampler** (workflow)
  - Modified workflow allowing different text prompts for each generation segment
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multi-prompt travel system** (workflow)
  - Workflow adaptation allowing prompt and frame length changes at each section
  - *From: Kaïros*

- **Janky Memory Patcher** (node)
  - Fixes ComfyUI native Wan memory bottleneck issues
  - *From: Ablejones*

- **FusionX merge model** (model)
  - Merge model with exposed LoRAs for tweaking, includes MPS, realism, LightX2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE + control video workflow** (workflow)
  - Uses control video for depth/normal maps with VACE for better motion control
  - *From: Faust-SiN*

- **Prompts per section workflow** (workflow)
  - Workflow with different prompts and reference images for each video section
  - *From: BarleyFarmer*

- **Tiled wan sampler patch** (patch)
  - Adds VRAM saving benefits to tiled wan sampler
  - *From: .tarkan*

- **Text to image/upscale workflow** (workflow)
  - WAN workflow for text to image and image upscaling
  - *From: VRGameDevGirl84(RTX 5090)*

- **Modified workflow with for loop** (workflow)
  - Generate smooth travel for arbitrary number of images using directory input
  - *From: seb bae*

- **Puppet style LoRA** (lora)
  - Based on Wizard's Thunderbirds Flux LoRA, trigger is 'puppet style'
  - *From: Flipping Sigmas*

- **ClownRegionalConditioning workflow** (workflow)
  - Simple workflow using ClownRegionalConditioning for prompt travel with WAN
  - *From: DrJKL*

- **Janky Memory Patcher** (node)
  - Solves memory issues by replacing core ComfyUI function, enables better memory management for large models
  - *From: Ablejones*

- **FusionX Phantom merged model** (model)
  - Produces stellar character reference results, works well with UniPC sampler
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN prompt generator with JSON mode** (tool)
  - Expanded system instructions with prompt examples from WAN 2.2 guide, includes usage counter
  - *From: thaakeno*

- **WanVacePhantomSimpleV2** (node)
  - Node for running VACE+Phantom together with various control inputs
  - *From: Ablejones*

- **Janky Memory Patcher** (tool)
  - Memory management tool to prevent OOM by limiting perceived VRAM
  - *From: Ablejones*

- **Long looping video workflow** (workflow)
  - Uses Wan + Qwen Image Edit with primary prompt and 3 edit prompts for timestep actions
  - *From: chancelor*

- **Image travel workflow** (workflow)
  - Creates smooth transitions through arbitrary number of images
  - *From: seb bae*

- **Kinestasis stop motion LoRA** (lora)
  - Creates stop motion effects for Wan 2.2, sensitive to specific prompt structures
  - *From: Cseti*

- **Modified Impact Pack** (custom_nodes)
  - Enables SEGS detailer functionality with Wan video models by bypassing image batch warnings
  - *From: Ablejones*

- **Multi-image travel workflow** (workflow)
  - Supports multiple image inputs without Nilor nodes, global prompt support
  - *From: seb bae*

- **Radial attention calculator** (node)
  - Calculates correct size for radial attention in long video generation
  - *From: Impactframes.*

- **WanVaceAdvanced nodes** (custom nodes)
  - Advanced VACE implementation with improved detailer integration and tiling support
  - *From: Ablejones*

- **Updated HuMo workflow** (workflow)
  - Audio-reactive video generation with custom prompt processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom Gemini integration** (node modification)
  - Tweaked Gemini code for LLM-based prompt generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Qwen2.5-VL workflow with Ollama** (workflow)
  - Local alternative to Gemini API using Qwen vision model through Ollama for prompt generation
  - *From: smithyIAN - 4080ti Super 16gig*

- **WAN 2.2 Mega Rapid AIO v3** (workflow)
  - Updated all-in-one workflow with modified NSFW LoRAs and recommended scheduler changes
  - *From: Phr00t*

- **VACEextend workflow** (workflow)
  - Fully T2V workflow without subgraphs, uses high-res fix architecture between high and low models
  - *From: Daviejg*

- **VRGameDevGirl84 music video workflow** (workflow)
  - Automated music video generation with audio transcription, LLM prompt generation, and lip sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Modified Gemini node** (node)
  - Tweaked Gemini API node to accept string input for lyrics integration
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom audio processing nodes** (node)
  - Nodes for audio cropping, scaling, and segmentation with lyric overlap and fallback features
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGameDevGirl Music Video Workflow v3.0** (workflow)
  - Automated music video generation with LLM-driven scene progression, automatic index management, and improved prompt generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom-Vace merge** (model)
  - Combination of Phantom model with Vace blocks for enhanced control capabilities
  - *From: Ablejones*

- **Auto-queue node** (node)
  - Automatically queues middle runs in music video workflow, with toggle to turn on/off
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt Creator node** (node)
  - Highly customizable node for generating detailed prompts with camera motion, lighting, character interactions
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanVaceAdvanced node** (node)
  - Advanced Vace processing node for improved consistency
  - *From: Ablejones*

- **Clownoptions tile node** (node)
  - Tiling options for upscaling workflows
  - *From: Clownshark Batwing*

- **Music video workflow with automated prompt generation** (workflow)
  - Complete workflow for generating music videos with lip sync, automatic prompt creation from lyrics, and video concatenation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt creator subgraph** (node)
  - Automated prompt creation system that takes lyrics and reference photo to create themed prompts with camera directions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multi-pass upscaling workflow** (workflow)
  - 81 frame 480p to 1080p upscaling workflow optimized for 16GB VRAM with face detailing
  - *From: Cseti*

- **Qwen Rapid AIO** (model)
  - NSFW-capable image editing model for creating start and end frames
  - *From: Phr00t*

- **Face detailer LoRA** (lora)
  - Custom LoRA that improves face quality when using LightX2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **Auto-queue nodes** (node)
  - Nodes that automatically queue middle runs, reducing manual intervention
  - *From: VRGameDevGirl84(RTX 5090)*

- **Reminder node** (node)
  - Node that pops up message if file path isn't updated from default
  - *From: VRGameDevGirl84(RTX 5090)*

- **QwenEdit upscaler LoRA (planned)** (lora)
  - Training LoRA for QwenEdit to upscale every X frames while maintaining consistency
  - *From: pom*

- **Spine editor integration** (workflow)
  - Control resolution distribution across upscale iterations
  - *From: Cseti*

- **Audio cleaning node** (node)
  - Standardizes audio files to prevent sync issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Loop-based upscale workflow** (workflow)
  - Automated upscale iterations using easy-use node pack loops
  - *From: Cseti*

- **VRGDG_ConditionalLoadVideos** (custom node)
  - Loads videos ending with -audio.mp4 for processing, ignores other files in folder
  - *From: VRGameDevGirl84(RTX 5090)*

- **Punk Style LoRA for WAN 2.1 14B** (lora)
  - 33 video training dataset produces high-quality punk aesthetic for WAN generations
  - *From: Charlie*

- **Enhanced Audio Split Node V2** (node)
  - Auto-versioning, smart project detection, simplified folder input
  - *From: VRGameDevGirl84(RTX 5090)*

- **Dual sampling I2V workflow** (workflow)
  - Uses new lightx2v at high and old 2.1 lightx2v at low with proper sigma splitting
  - *From: FL13*

- **Local LLM integration** (workflow)
  - Modified workflow to use Gemma3 27B instead of Gemini API
  - *From: NoHuman*

- **Ollama ChatGPT proxy setup** (tool)
  - Container setup to use paid ChatGPT through ollama node
  - *From: triquichoque*

- **Infinite variation LoRA** (lora)
  - Helps with variation in generated content
  - *From: Flipping Sigmas*

- **GPT for lyric processing** (tool)
  - Custom GPT that takes lyrics and crafts lists for prompt creator based on song
  - *From: VRGameDevGirl84(RTX 5090)*

- **TensorRT upscaler nodes** (node)
  - Fast upscaling nodes used in workflow
  - *From: Cseti*

- **Seamless loop workflow integration** (workflow)
  - Integrates looping functionality into existing workflows with manual control frame assembly
  - *From: brbbbq*

- **720p to 1080p upscale pipeline** (workflow)
  - Full pipeline optimized for 720p generation and upscaling to 1080p without VRAM issues, 12 minutes for 2 passes at 81 frames on 5090
  - *From: Mandulis - Max - 2/2*

- **High-res dynamic outpainting workflow** (workflow)
  - Uses subgraph + dynamic widget setup for cleaner, more modular workflow with aspect ratio adjustment
  - *From: yo9o*

- **Containerised version for SaaS** (tool)
  - Docker containerised version for easy deployment and potential SaaS offering
  - *From: samhodge*

- **Face reconstruction node** (node)
  - Handles missing face masks without errors, faster than original method
  - *From: ingi // SYSTMS*

- **Transition LoRA** (lora)
  - Helps force transitions in clips without obvious transition points, trained on motion blocks
  - *From: ingi // SYSTMS*

- **Steerable Motion workflow additions** (workflow)
  - Added looping groups and frame stitching functions to existing workflow
  - *From: brbbbq*

- **Automated music video workflow** (workflow)
  - Uses Gemini API for automated prompt generation, only needs character image and song
  - *From: burgstall*

- **Pixel art trajectory workflow** (workflow)
  - FL Pixel art node for trajectory-based video generation
  - *From: Fill*

- **Flipping Sigmas LoRA V2** (lora)
  - Updated psychedelic/liquid art LoRA trained with help from community, more potent than V1
  - *From: Flipping Sigmas*

- **Water Morphing Wan LoRA** (lora)
  - LoRA trained on just 3 videos for water morphing effects
  - *From: AshmoTV*

- **Wan2.2 AnimateDiff LoRA** (lora)
  - AnimateDiff LoRA for Wan 2.2, experimental with limited testing
  - *From: ReDiff*

- **Loop transition removal workflow** (workflow)
  - Removes pauses in AnimateDiff workflow for seamless looped videos
  - *From: lostless.visuals*

- **Humo Lipsync Suppress with autoswitch** (node)
  - Forked version that adds autoswitch based on empty vocals input for automation
  - *From: burgstall*

- **Image batch labeler** (node)
  - Labels each image in a batch, useful for debugging and tracking overlap frame workflows
  - *From: Ablejones*

- **Audio delay node** (node)
  - Adds silence to front of audio clip to fix sync problems where audio comes before video
  - *From: JohnDopamine*

- **SORA watermark node** (node)
  - Adds SORA-style watermark to any video to make it look like it was generated on SORA
  - *From: JohnDopamine*

- **Video color match node** (node)
  - Prevents color drift by recording color matching parameters from each video frame and applying to whole video instead of frame-by-frame matching
  - *From: Ablejones*

- **Lip Sync Suppressor node** (node)
  - Suppresses unwanted lip movement when using empty audio input
  - *From: Ablejones*

- **Modified Ollama prompt generation workflow** (workflow)
  - Make-It-Flipping-Rad-V2 with basic Ollama prompt generation as alternative to Google API
  - *From: JohnnyLongBalls*

- **Custom consistency LoRA** (lora)
  - Private LoRA trained to help maintain consistency across generations
  - *From: yo9o*

- **Updated FMML-HuMo workflow** (workflow)
  - Combines Wan 2.2 (FMML) as high-noise and Humo as low-noise with automated LLM prompt generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Paint smear LoRA** (lora)
  - Artistic style LoRA for paint smear effects
  - *From: AshmoTV*

- **Audio padding modification** (workflow)
  - Modified audio encoder to add silence padding instead of overlap for better lipsync
  - *From: hudson223*

- **Low-end hardware workflow variant** (workflow)
  - Downgraded version using Wan 2.1 1.3B for 12GB cards
  - *From: atom.p*

- **Audio scale modification for HuMo** (node modification)
  - Rewired HuMo node to include variable audio scale control for mouth movement intensity
  - *From: hudson223*

- **VACE preparation node set** (workflow)
  - Node set that prepares video for VACE encode, works with any VACE workflow
  - *From: Blink*

- **Exploded effect v2 LoRA** (lora)
  - LoRA for creating exploded/deconstructed visual effects that would traditionally require Houdini
  - *From: AshmoTV*

- **Wan Prompt Scheduling node** (node)
  - Supports multiple prompts separated by pipe character with evenly distributed weights across time
  - *From: atom.p*

- **Updated style LoRA** (lora)
  - New version that sticks to styles better, proper i2v lora instead of T2V style
  - *From: Flipping Sigmas*

- **InfiniteTalk Native Workflow** (workflow)
  - Clean workflow for infinite extensions with custom audio or TTS, generates 5-second chunks separately
  - *From: Elvaxorn*
