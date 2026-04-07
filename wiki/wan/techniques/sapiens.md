---
title: Sapiens Preprocessors for Wan
aliases: [sapiens, sapiens-pose, sapiens-depth, sapiens-normals]
last_updated: 2025-04-03
---

# Sapiens Preprocessors for Wan

Sapiens is Facebook's state-of-the-art human understanding model that provides superior pose estimation, depth maps, and normal maps for human subjects. It offers significant improvements over traditional preprocessors like DWPose and is particularly effective with VACE for video generation.

**Release:** August 2024 (Facebook Research)

**ComfyUI Support:** Added by Kijai on April 3, 2025

---

## Overview

Sapiens is a suite of models for human-centric computer vision tasks:
- **Pose estimation** (body and face)
- **Depth estimation** (human-focused)
- **Normal map generation**
- **Segmentation** (human parts)

Unlike general-purpose preprocessors, Sapiens is specifically trained on human subjects and provides:
- Superior temporal stability
- Better facial detail
- More accurate body pose
- High-quality normal maps for relighting

> "sapiens normals" -- Kijai, April 3, 2025 [🔥x7]

---

## Advantages Over Other Preprocessors

### vs DWPose

| Aspect | DWPose | Sapiens Pose |
|--------|--------|-------------|
| **Facial detail** | Basic landmarks | Superior facial tracking |
| **Temporal stability** | Good | Excellent |
| **Body accuracy** | Good | Better |
| **Hands** | Inconsistent | More reliable |
| **Training data** | General | Human-specific |

### vs Mediapipe Face

| Aspect | Mediapipe | Sapiens Face |
|--------|-----------|-------------|
| **Detection rate** | May miss faces | More reliable |
| **Facial landmarks** | 2D landmarks | 3D-aware pose |
| **Temporal stability** | Moderate | Excellent |
| **Integration** | Face only | Full body + face |

### vs Standard Depth/Normals

| Aspect | Standard | Sapiens |
|--------|----------|--------|
| **Human focus** | General scene | Human-optimized |
| **Temporal stability** | Variable | Excellent |
| **Detail preservation** | Good | Superior for humans |
| **Background** | Better | Human-focused |

---

## Available Models

**HuggingFace repositories:**

- `facebook/sapiens-pose-1b-torchscript`
- `facebook/sapiens-depth-1b-torchscript`
- `facebook/sapiens-normal-1b-torchscript`
- `facebook/sapiens-seg-1b-torchscript`

**Model sizes:**
- 1B parameter models (torchscript format)
- Optimized for inference
- Single resolution input (limitation)

---

## ComfyUI Setup

**Kijai's implementation:**

Sapiens support was added to Kijai's "Follow Your Emoji" wrapper on April 3, 2025:

- Repository: `ComfyUI-WanVideoWrapper` (Kijai)
- Nodes: Sapiens pose, depth, normals preprocessors
- Format: Torchscript models

**Alternative nodes:**

- `ComfyUI_Sapiens` (smthemex) -- Community implementation

> "are these the sapiens nodes everyone is using? https://github.com/smthemex/ComfyUI_Sapiens" -- ArtOfficial, April 3, 2025

---

## Usage with VACE

### Pose Control

**Sapiens Pose is superior to DWPose for:**
- Facial expressions and lip sync
- Hand positioning
- Full body tracking with face detail
- Temporal consistency

**Workflow:**
1. Process video with Sapiens Pose
2. Connect to VACE input_frames
3. Optionally add reference image
4. Generate with standard VACE settings

**Lip sync applications:**

Multiple users noted Sapiens' potential for lip sync:

> "I can feel the lipsync module based on wan coming soon" -- melmass, April 3, 2025

The superior facial tracking makes it ideal for audio-driven animation.

**Comparison results (April 3, 2025):**

Users compared Sapiens pose to DWPose for lip sync:
- **DWPose:** Random mouth movements, poor facial tracking
- **Sapiens:** Better facial detail, more accurate tracking
- **Animated vs realistic:** Sapiens works better with realistic faces

> "also an animated monkey vs realistic face" -- dawniii, April 3, 2025

Sapiens may struggle with highly stylized/animated characters compared to realistic humans.

### Depth Maps

**Sapiens Depth provides:**
- Human-focused depth estimation
- Better temporal stability than general depth models
- Superior detail on faces and hands

**Use cases:**
- Character animation with depth control
- Combining with pose for multi-control
- Scene understanding with human subjects

### Normal Maps

**Sapiens Normals excel at:**
- Relighting human subjects
- Preserving surface detail
- Temporal consistency across frames

**Workflow for relighting:**
1. Generate Sapiens normal maps from video
2. Use as VACE control signal
3. Prompt for different lighting conditions
4. VACE respects normals while changing lighting

> "sapiens normals" -- Kijai, April 3, 2025 [🔥x7]

Community reaction suggests this is a particularly powerful feature.

---

## Multi-Control with Sapiens

**Depth + Pose combination:**

Users reported excellent results combining Sapiens depth and pose:

**Method 1: Overlay**
- Overlay pose skeleton on depth map
- Feed combined image to VACE
- Works but may have artifacts

**Method 2: Separate encodes**
- Use separate VACE encode nodes
- Chain via prev_vace_embeds
- Cleaner results, more control over strengths

**Recommended approach:**
- Sapiens Pose for character motion
- Sapiens Depth for scene structure
- Separate VACE encodes with different strengths

---

## Limitations

### Single Resolution

Sapiens torchscript models only support single input resolution:

> "Not yet, it's a bit clumsy to use because it only seems to support single resolution" -- Kijai, April 3, 2025

This makes it less flexible than other preprocessors that handle arbitrary resolutions.

**Workaround:**
- Resize input to supported resolution
- Process with Sapiens
- Resize output back to target resolution

### Aspect Ratio

Unclear if aspect ratio flexibility exists:

> "ratio too?" -- melmass, April 3, 2025

> "I think so, it didn't do anything in landscape, but could be wrong...it does run as long as the pixel count is same" -- Kijai, April 3, 2025

May work with different aspect ratios if total pixel count matches.

### Background Handling

Sapiens is human-focused:
- May not provide good depth/normals for backgrounds
- Best combined with general-purpose preprocessors for full scenes
- Ideal for human-centric content

### Stylized Content

Sapiens is trained on realistic humans:
- May not work well with highly stylized/animated characters
- Better suited for realistic or semi-realistic styles
- DWPose may be better for cartoon/anime content

---

## Performance

**Speed:**
- Torchscript models are optimized for inference
- Comparable to other preprocessors
- 1B parameter models are reasonably fast

**VRAM:**
- Moderate VRAM requirements
- Can be run on consumer GPUs
- Exact requirements depend on resolution

---

## Best Practices

1. **Use for human-centric content** -- Sapiens excels with people, not general scenes
2. **Combine with other preprocessors** -- Use general depth for backgrounds, Sapiens for humans
3. **Leverage temporal stability** -- Sapiens' consistency is its key advantage
4. **Test with realistic styles** -- Works best with realistic or semi-realistic content
5. **Use separate VACE encodes** -- Don't overlay multiple Sapiens outputs; chain them
6. **Consider for lip sync** -- Superior facial tracking makes it ideal for audio-driven work

---

## Comparison to Alternatives

| Preprocessor | Best For | Temporal Stability | Facial Detail | Speed |
|--------------|----------|-------------------|---------------|-------|
| **Sapiens Pose** | Realistic humans | Excellent | Superior | Moderate |
| **DWPose** | General use, anime | Good | Basic | Fast |
| **Mediapipe** | Face only | Moderate | Good | Fast |
| **Sapiens Depth** | Human depth | Excellent | Superior | Moderate |
| **Depth Anything V2** | General scenes | Good | Good | Fast |
| **Sapiens Normals** | Human relighting | Excellent | Superior | Moderate |
| **DSine** | General normals | Moderate | Good | Moderate |

---

## Future Development

**Potential improvements:**
- Multi-resolution support
- Better aspect ratio handling
- Integration with audio for lip sync
- Stylized content training

**Community interest:**

High interest in Sapiens for:
- Lip sync applications
- Character animation
- VFX compositing
- Relighting workflows

The strong community reaction suggests Sapiens will become a standard preprocessor for human-centric VACE workflows.

---

## See Also

- [[vace]] -- VACE control system that uses Sapiens
- [[wan-2.1]] -- Base model for VACE
- [[comfyui]] -- Platform for running Sapiens preprocessors

## External Resources

- [Sapiens GitHub](https://github.com/facebookresearch/sapiens)
- [Sapiens Models (HuggingFace)](https://huggingface.co/facebook)
- [ComfyUI_Sapiens (smthemex)](https://github.com/smthemex/ComfyUI_Sapiens)
- [Kijai WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
