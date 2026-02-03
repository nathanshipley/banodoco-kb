# Wan Ecosystem - External Sources Content

*Fetched: February 3, 2026*

This document contains technical details extracted from external sources for the Wan knowledge base. Use this alongside the Discord extraction data when building the static KB.

---

## Official Wan 2.1

**Source:** https://github.com/Wan-Video/Wan2.1

### Available Models
- Wan2.1-T2V-14B (480P & 720P)
- Wan2.1-T2V-1.3B (480P)
- Wan2.1-I2V-14B-720P
- Wan2.1-I2V-14B-480P
- Wan2.1-FLF2V-14B-720P (First-Last-Frame-to-Video)
- Wan2.1-VACE-1.3B & VACE-14B (video creation/editing)

### Framework Integrations
- **Diffusers**: Integrated T2V and I2V pipelines
- **ComfyUI**: Native integration available
- **DiffSynth-Studio**: Enhanced support with quantization and LoRA training

### Community Projects Built on Wan2.1
Video-As-Prompt, LightX2V, DriVerse, UniAnimate-DiT, Wan-Move, EchoShot

### Related Tools
- **xDiT**: Distributed inference framework (v0.4.1+)
- **TeaCache**: Acceleration achieving ~2x speedup
- **Qwen Models**: Used for prompt extension

---

## Official Wan 2.2

**Source:** https://github.com/Wan-Video/Wan2.2

### Available Models

| Model | Purpose |
|-------|---------|
| T2V-A14B | Text-to-Video (480P/720P) with MoE architecture |
| I2V-A14B | Image-to-Video (480P/720P) |
| TI2V-5B | Text/Image-to-Video (720P@24fps, consumer GPU compatible) |
| S2V-14B | Speech-to-Video with audio-driven generation |
| Animate-14B | Character animation and replacement |

### Key Features
- Mixture-of-Experts (MoE) architecture
- Cinematic-level aesthetic generation with detailed control
- 16×16×4 compression ratio VAE
- Multi-GPU inference via FSDP + DeepSpeed Ulysses
- CosyVoice text-to-speech integration for S2V tasks

### Community Projects
LightX2V, HuMo, FastVideo, Cache-dit, ComfyUI-WanVideoWrapper, DiffSynth-Studio

---

## VACE (Video Creation & Editing)

**Source:** https://github.com/ali-vilab/VACE

### Capabilities
- **Tasks**: Reference-to-Video (R2V), Video-to-Video (V2V), Masked Video-to-Video (MV2V)
- **Features**: Move-Anything, Swap-Anything, Reference-Anything, Expand-Anything, Animate-Anything

### Models Available
- VACE-Wan2.1-1.3B-Preview
- VACE-Wan2.1-14B
- VACE-LTX-Video-0.9
- VACE-Annotators (preprocessors)
- VACE-Benchmark (evaluation dataset)

### Requirements
- Python 3.10+
- PyTorch 2.5.1+
- CUDA 12.4

---

## Kijai's ComfyUI-WanVideoWrapper

**Source:** https://github.com/kijai/ComfyUI-WanVideoWrapper

### Supported Models (20+)

**Primary Models:**
- WanVideo (main T2V/I2V)
- WanVideoFun
- SkyReels

**Video Enhancement:**
- ReCamMaster, VACE, Phantom, ATI, Uni3C, MiniMaxRemover, MAGREF, LongCat-Video

**Character & Face Animation:**
- FantasyTalking, FantasyPortrait, MultiTalk, HuMo, EchoShot, Stand-In, WanAnimate

**Motion & Camera Control:**
- Lynx, MoCha, UniLumos, BindWeave, TimeToMove, SteadyDancer, One-to-all-Animation, SCAIL

### Key Features
- Block swapping for VRAM optimization
- FP8 quantization support
- Context window handling for long sequences
- LoRA weight support
- GGUF model loading
- Torch.compile optimization

---

## Phantom (Subject Consistency)

**Source:** https://github.com/Phantom-video/Phantom

### Models
- **Phantom-Wan-1.3B**: 480P and 720P
- **Phantom-Wan-14B**: 480P and 720P (trained on 480P, less stable at higher res)

### Requirements
- PyTorch >= 2.4.0
- Base model: Wan2.1-T2V-1.3B or 14B

### Features
- Single and multi-subject reference (up to 4 images)
- Text-to-video with reference consistency
- Multi-GPU via FSDP + xDiT USP
- 16fps and 24fps generation

### Usage Parameters
- `--ref_image`: Comma-separated paths (max 4)
- `--prompt`: Text description
- `--base_seed`: Reproducibility control
- `--size`: Resolution (e.g., 832*480)
- `--frame_num`: Frame count

### Tips
- Describe reference images accurately in prompts
- Use horizontal orientations for stability
- Modify seed iteratively for quality

---

## MAGREF (Multi-Reference)

**Source:** https://github.com/MAGREF-Video/MAGREF

### Purpose
Generate videos from multiple reference images with subject disentanglement

### Requirements
- **VRAM**: ~70GB recommended (80GB GPU like H100)
- **Multi-GPU**: Supports FSDP and Ulysses parallelism (8 GPUs)
- PyTorch 2.5.1, CUDA 12.1/12.4

### Features
- Any-reference video generation
- Text-to-video with reference guidance
- FP8 quantization variant available
- ComfyUI integration (community)

---

## EchoShot (Multi-Shot Consistency)

**Source:** https://github.com/JoHnneyWang/EchoShot

### Purpose
Generate multiple video shots of the same person with consistent identity

### Model
- Built on Wan2.1-T2V-1.3B
- EchoShot-1.3B-preview weights

### Features
- Text-to-multishot portrait video
- Maintains identity across different scenes
- LLM-based prompt extension (Qwen)

---

## HuMo (Human-Centric Multimodal)

**Source:** https://github.com/Phantom-video/HuMo

### Models
- **HuMo-17B**: 480P & 720P
- **HuMo-1.7B**: Lightweight, runs on 32GB GPU
- **HuMo-Longer**: Coming soon

### VRAM
- HuMo-1.7B: 480P in 8 minutes on 32GB GPU
- HuMo-17B: Runs on 3090 via ComfyUI
- Supports multi-GPU (FSDP + Sequence Parallel)

### Features
- Text + Audio (TA mode)
- Text + Image + Audio (TIA mode)
- Strong text prompt following
- Consistent subject preservation
- Synchronized audio-driven motion

### Audio Processing
- Whisper-large-v3 encoder
- Optional background noise removal (Kim_Vocal_2)

### Parameters
- `scale_a`: Audio guidance strength
- `scale_t`: Text guidance strength
- `diffusion.timesteps.sampling.steps`: 50 default (30-40 for faster)

### Dataset
HuMoSet: 670K video samples with diverse references and audio-visual sync

---

## MultiTalk (Multi-Person Conversations)

**Source:** https://github.com/MeiGen-AI/MultiTalk

### Base Model
Wan2.1-I2V-14B-480P

### VRAM
- Standard: RTX 4090 level
- Low VRAM: 8GB with `--num_persistent_param_in_dit 0`
- Multi-GPU: FSDP supported

### Features
- Single and multi-person video
- Cartoon characters and singing
- Up to 15 seconds (201 frames max, 81 optimal)
- 480p and 720p at arbitrary aspect ratios
- TTS audio integration
- TeaCache acceleration (2-3x speedup)

### Parameters
- `--mode streaming`: Long video
- `--use_teacache`: Enable acceleration
- `--sample_steps`: 40 recommended (10 for faster)
- `--teacache_thresh`: 0.2-0.5 optimal

### Limitations
- 480P single-GPU only in current code
- 720P requires multiple GPUs
- Trained on 81-frame videos at 25 FPS

---

## InfiniteTalk (Unlimited Length)

**Source:** https://github.com/MeiGen-AI/InfiniteTalk

### Base Model
Wan2.1-I2V-14B-480P with InfiniteTalk LoRA

### Improvements over MultiTalk
- Reduces hand/body distortions
- Superior lip synchronization
- Sparse-frame dubbing (lips, head, body, expressions)
- Unlimited duration via streaming

### Features
- Image-to-video and video-to-video modes
- TeaCache acceleration
- Multi-GPU inference
- Gradio and ComfyUI integration

### Limitations
- I2V beyond 1 minute: Color shifts become pronounced
- V2V camera: Not identical to original
- FusionX LoRA: Exacerbates color shift, reduces ID preservation

---

## FantasyTalking (Portrait Animation)

**Source:** https://github.com/Fantasy-AMAP/fantasy-talking

### Requirements
- PyTorch >= 2.0.0
- Wan2.1-I2V-14B-720P base model
- Wav2Vec2-base-960h audio encoder

### VRAM Configurations

| Config | Speed | VRAM |
|--------|-------|------|
| Full precision (bf16) | 15.5s/iter | 40GB |
| 7B persistent params | 32.8s/iter | 20GB |
| Minimal (0 params) | 42.6s/iter | 5GB |

*Benchmarks: 512×512, 81 frames, single A100*

### Features
- Audio-driven motion synthesis
- Text prompts for behavior control
- Various body ranges (close-up, half-body, full-body)
- Front and side-facing poses
- Characters and animals in various styles

### Parameters
- Audio guidance scale: 3-7 recommended

---

## LightX2V (Distillation Framework)

**Source:** https://github.com/ModelTC/LightX2V

### Supported Models
- LTX-2, HunyuanVideo-1.5, Wan2.1, Wan2.2, Qwen-Image variants
- 4-step distilled models without CFG

### VRAM
- **Minimum**: 8GB VRAM + 16GB RAM (with offloading)
- Supports H100 and RTX 4090D

### Performance
- Single GPU: 1.9x (H100), 1.5x (4090D)
- Multi-GPU (8x H100): 3.9x
- With distillation + FP8: up to 42x acceleration

### Quantization Options
- w8a8-int8
- w8a8-fp8
- w4a4-nvfp4
- FP8 per-tensor

### Key Features
- Sage Attention, Flash Attention
- Block-level offload
- TeaCache/MagCache
- CFG/Ulysses parallelism

---

## CausVid (Temporal Consistency)

**Source:** https://github.com/tianweiy/CausVid

### Purpose
Convert bidirectional diffusion to autoregressive for streaming generation

### Step Reduction
- 50 steps → 4 steps (DMD distillation)
- 3-step inference achieves 84.27 on VBench-Long

### Performance
- 9.4 FPS on single GPU
- 1.3 second initial latency, then streaming

### Architecture
- Block-wise causal attention
- KV caching for efficiency
- Asymmetric distillation (causal student, bidirectional teacher)

### LoRA Versions
- V1, V1.5, V2 available
- V2 quality nearly identical to base Wan 2.1

---

## ReCamMaster (Camera Control)

**Source:** https://github.com/KwaiVGI/ReCamMaster

### Purpose
Camera-controlled generative rendering from single video

### Supported Trajectories (10 presets)
1. Pan: Right/Left (5-45°)
2. Tilt: Up/Down (5-30°)
3. Zoom: In/Out
4. Translation: Up/Down with rotation
5. Arc: Left/Right with rotation
- Variable-speed trajectories supported

### Integration
- Migrated to Wan2.1
- Requires 81+ frames
- DiffSynth-Studio framework

### Applications
- Video stabilization
- Super-resolution
- Outpainting
- Autonomous driving data augmentation

---

## VideoX-Fun (Control Methods)

**Source:** https://github.com/aigc-apps/VideoX-Fun

### Control Methods
- Pose (skeletal)
- Canny (edges)
- Depth maps
- MLSD (line segments)
- Trajectory (path-based)
- Camera control
- Reference image

### Models
- CogVideoX-Fun-V1.1-2b-InP / 5b-InP
- Wan2.1-Fun-V1.1-14B-InP / 1.3B-InP
- Control variants for both sizes

### Hardware
- RTX 3060 (12GB) to A100 (80GB)
- ~60GB disk for weights
- CUDA 11.8/12.1, Python 3.10/3.11

### Resolution
- 256×256×49 to 1024×1024×49 frames

---

## Wan2GP (GPU-Poor Friendly)

**Source:** https://github.com/deepbeepmeep/Wan2GP

### VRAM Requirements
- As low as 6GB for certain models
- LTX-2 HD 720p (10s): 8GB
- LTX-2 HD 1080p (10s): 12GB
- LTX-2 HD 1080p (20s): 16GB

### Supported Hardware
- Old NVIDIA (RTX 10XX, 20XX)
- Modern NVIDIA
- AMD Radeon RX 76XX-79XX

### Supported Models
- Wan 2.1/2.2
- LTX-2 (with audio)
- Hunyuan Video
- Flux (Klein 4B/9B)
- Qwen, Z-Image
- Audio models (Heart Mula, Ace Step, Qwen3 TTS)

### Optimization Techniques
- Quantization: int8, fp8, gguf, NV FP4, Nunchaku
- Memory profiles (1-5) trade speed for VRAM
- Sliding window for long videos
- Text encoder caching

---

## ComfyUI Wan 2.1 Tutorial

**Source:** https://docs.comfy.org/tutorials/video/wan/wan-video

### Required Models

**Text Encoders (choose one):**
- umt5_xxl_fp16.safetensors
- umt5_xxl_fp8_e4m3fn_scaled.safetensors

**VAE:** wan_2.1_vae.safetensors

**CLIP Vision:** clip_vision_h.safetensors

### Text-to-Video
- Model: wan2.1_t2v_1.3B_fp16.safetensors

### Image-to-Video
- 480P: wan2.1_i2v_480p_14B_fp16.safetensors
- 720P: wan2.1_i2v_720p_14B_fp16.safetensors

### Notes
- FP16 recommended over BF16
- Update ComfyUI for native support

---

## ComfyUI VACE Tutorial

**Source:** https://docs.comfy.org/tutorials/video/wan/vace

### Models
- wan2.1_vace_14B_fp16.safetensors (or 1.3B)
- 1.3B: 480P only
- 14B: 480P and 720P

### Workflow Modes
- Text-to-Video
- Image-to-Video
- Video-to-Video (with control)

### Performance (4090)
- 720x1280, 81 frames: ~40 minutes
- 640x640, 49 frames: ~7 minutes

### Parameters
- Resolution must be divisible by 16
- 720P produces superior quality
- First-last frame: length-1 divisible by 4

---

## ComfyUI Wan 2.2 Tutorial

**Source:** https://docs.comfy.org/tutorials/video/wan/wan2_2

### What's New
- MoE architecture (separate high/low noise experts)
- Cinematic control (lighting, color, composition)
- Enhanced motion and semantics

### Generation Modes
- **5B Hybrid**: Single model for T2V and I2V
- **14B T2V**: Two expert models
- **14B I2V**: Dual-expert setup

### VRAM
- 5B version fits on 8GB with ComfyUI native offloading
