---
title: Wan Video Generation Ecosystem Overview
aliases: [wan, wanx, wan-ai]
last_updated: 2025-02-23
---

# Wan Video Generation Ecosystem Overview

Wan (also branded as WanX) is Alibaba's family of open-source video generation models. The ecosystem centers around the [[wan-2.1]] base models released in February 2025, with various specialized derivatives and control systems built on top.

## Upcoming Release: Wan 2.1 (WanX 2.1)

As of late February 2025, Alibaba announced the upcoming open-source release of Wan 2.1 (marketed as "WanX 2.1"), scheduled for release in the week following February 23, 2025.

### Known Specifications

- **Model sizes:** 1.3B and 14B parameter variants
- **Architecture:** 14B model comparable to Hunyuan Video (13B)
- **Quality:** Preview videos show "next level" quality with strong prompt adherence
- **HuggingFace presence:** Model links already present in HuggingFace space code, suggesting imminent release

### Available Variants (Announced)

| Variant | Purpose | Notes |
|---------|---------|-------|
| Wan 2.1 T2V 1.3B | Text-to-video, consumer GPUs | Smallest variant |
| Wan 2.1 T2V 14B | Text-to-video, flagship | Comparable to Hunyuan 13B |
| Wan 2.1 I2V Plus | Image-to-video | API pricing: $0.14/second |

### Community Expectations

**Positive signals:**
- HuggingFace space already exists with model links in code
- Alibaba has committed to open-source release
- Preview videos show exceptional quality
- Multiple model variants planned for release

**Concerns:**
- Uncertainty about which variants will be fully open-sourced
- "Plus" branding suggests possible paid/limited versions
- History of companies releasing limited versions after strong previews (e.g., SkyReels)

> "I always keep my expectations low, but hope for the best." — TK_999, Discord #wan_chatter, Week 2025-W08

### API Access

While awaiting open-source release, API access is available through:
- Chinese platform: https://tongyi.aliyun.com/wanxiang/videoCreation (requires Chinese phone number)
- API endpoint: https://302ai-en.apifox.cn/api-254095110 (legitimacy uncertain)
- Official Alibaba API documentation available

### Benchmark Dataset

Alibaba released a benchmark dataset for Wan 2.1 evaluation, featuring:
- Large collection of test videos
- Prompts embedded in filenames
- Variety of styles (watercolor, Van Gogh, etc.)
- Example: "Gwen Stacy reading a book, watercolor painting"

## Model Family

The Wan ecosystem includes:

- **[[wan-2.1]]** — Base T2V and I2V models (upcoming open-source release)
- **[[wan-2.2]]** — Dual high/low noise MoE architecture
- **[[vace]]** — Unified control system for depth, pose, inpainting, style transfer
- **[[phantom]]** — Character consistency from reference images
- **[[wananimate]]** — Pose-driven character animation
- **[[humo]]** — Audio-driven video generation

And many other derivatives built on the Wan base models.

## Hardware Requirements

**Expected requirements (based on 14B size):**
- Similar VRAM needs to Hunyuan Video (13B)
- 1.3B variant designed for consumer GPUs
- Community discussion of "4090 version" optimization

## Community Reception

Early reactions to preview videos:
- "Next level" quality — said2000_0
- Strong prompt adherence without prompt engineering
- I2V quality comparable to Kling
- Surprise at quality from "just" 14B parameters

## See Also

- [[wan-2.1]] — Base model family (pending full documentation after release)
- [[wan-2.2]] — Advanced MoE variant
- [[choosing-a-model]] — Guide to selecting the right Wan variant

## External Resources

- [WanX 2.1 HuggingFace Space](https://huggingface.co/spaces/WanX-AI/WanX2.1)
- [Alibaba Model Studio API Documentation](https://help.aliyun.com/zh/model-studio/getting-started/new-model-announcement)
- [Tongyi WanXiang Platform](https://tongyi.aliyun.com/wanxiang/videoCreation) (Chinese, requires phone number)
