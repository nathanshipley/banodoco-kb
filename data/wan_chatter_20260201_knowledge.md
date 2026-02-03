# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2026-02-01 to 2026-02-03*


## Technical Discoveries

- **NVFP4 conversion for Wan models**
  - T2V and I2V models being converted to NVFP4 format for improved performance
  - *From: topmass*

- **MOVA model negative prompts behavior**
  - Do NOT use Wan's usual negative prompts with MOVA; it fucks up the generation. Let the negative field blank, their hidden negatives seem to work fine
  - *From: Stef*

- **LightX2V LoRAs may work with different models**
  - Existing LightX2V LoRAs might work with different datasets and 24fps models, though 80% won't be able to
  - *From: yi*

- **8-step distill LoRA training possibility**
  - 8 step 'distill' lora can be easily trained with recent techniques and will preserve more motion than the lightx2v lora
  - *From: yi*

- **SkyReels V3 model compatibility**
  - SkyReels V3 'V2V' model runs in Pusa workflow - same workflow, just change models. It's distilled already and better than Pusa
  - *From: Kijai*

- **Self-refine video enhancement**
  - Self-refine significantly improves video quality, worth the extra 50% processing time. Much better quality improvement especially on 1.3B models
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** MOVA installation breaks dependencies
  - **Solution:** It downgrades protobuf which breaks ComfyUI venv. Had to reinstall from scratch and make separate ComfyUI for MOVA experiments
  - *From: Stef*

- **Problem:** Green noise glitch with Wan2.2 after multiple generations
  - **Solution:** Restarting ComfyUI fixes the issue. Clearing model and execution cache doesn't help
  - *From: halkony*

- **Problem:** Batch extend with latents doesn't work properly
  - **Solution:** Not properly possible because first latent is single frame, breaks temporal continuity. You get glitches when decoding (1 4 4 4 4 1 4 4 4 pattern)
  - *From: Kijai*

- **Problem:** Mask visibility in lipsync workflow
  - **Solution:** Use 'Image Composite Masked' with faded edges to composite the masked region to original input. Should always be done as latent masking puts everything through VAE
  - *From: Kijai*


## Model Comparisons

- **MOVA vs LTX speed**
  - MOVA 1 hour generation for 8 sec 720p videos, but speed complaints unfair since Wan2.2 is same speed. LTX 'cheats' with highly compressed VAE while MOVA has proper VAE handling fine details and fast movements
  - *From: yi*

- **HuMo vs InfiniteTalk for lipsync**
  - HuMo is SOTA from quality standpoint, but can't do infinite frames natively like InfiniteTalk. Use HuMo as second pass
  - *From: Dream Making*

- **SkyReels V3 vs Phantom/HuMo**
  - SkyReels reference model doesn't seem as good as Phantom/Humo
  - *From: JohnDopamine*

- **DMD vs Consistency models**
  - DMD is super destructive distillation method, consistency model is much less destructive alternative. DMD has high quality but collapses variance/diversity
  - *From: mallardgazellegoosewildcat2*


## Tips & Best Practices

- **Use HuMo in V2V mode**
  - Context: Feed WanVideoSampler 'samples' input using 'wan encode' and set denoise lower than 1
  - *From: Dream Making*

- **Composite masked regions properly**
  - Context: Always composite masked region to original input with faded edges since latent masking puts everything through VAE
  - *From: Kijai*

- **SkyReels V3 usage**
  - Context: Can use Pusa example workflow, just change model and remove the loras. Uses zero noise, not custom noise
  - *From: Kijai*

- **Self-refine integration**
  - Context: Put self-refine node between wire connecting to sampler's 'image_embeds' input
  - *From: JohnDopamine*


## News & Updates

- **NVFP4 converted models being uploaded**
  - T2V wan models and i2v models being converted and uploaded to HuggingFace
  - *From: topmass*

- **New reward LoRA for Wan2.1**
  - CodeGoat24/Wan2.1-T2V-14B-UnifiedReward-Flex-lora released, could work on low noise model
  - *From: yi*

- **Causal-Forcing method released**
  - New technique from thu-ml, though examples show high-contrast, overexposed artifacts typical of CFG issues
  - *From: JohnDopamine*

- **TeleStyle released**
  - Style transfer tool with XL-quality results, works on Wan 2.1 1.3B model with cross-attention style transfer
  - *From: Tonon*


## Workflows & Use Cases

- **MOVA workflow usage**
  - Use case: 8GB cards may not work due to model size, requires separate environment to avoid dependency conflicts
  - *From: JohnDopamine*

- **HuMo as second pass lipsync**
  - Use case: Use HuMo for quality, pair with SVI for infinite frames capability
  - *From: Dream Making*

- **Masked lipsync with SAM3**
  - Use case: Use SAM3 for head masking in Infinite V2V workflow for lipsync, composite with faded edges
  - *From: Stef*


## Recommended Settings

- **MOVA negative prompts**: Leave blank
  - Wan's usual negative prompts break generation, hidden negatives work fine
  - *From: Stef*

- **SVI Pro motion latents**: 1
  - Real default value despite tooltip contradiction
  - *From: Kijai*

- **SVI Pro frame overlap**: 5
  - Recommended default setting
  - *From: JohnDopamine*

- **TeleStyle video inference steps**: 35
  - Increased from default 25 for better results
  - *From: Kytra*


## Concepts Explained

- **DMD (Distribution Matching Distillation)**: Super destructive distillation method that heavily collapses variance, reducing image variety but maintaining high quality. Every DMD distilled model has overexposed, high-contrast artifacts
  - *From: yi*

- **High/Low noise expert split**: Wan2.2 architecture constraint that some people avoid due to complexity, hence continued Wan2.1 development
  - *From: yi*

- **Per token timesteps**: Technique used by SkyReels, Pusa, Wan 5B, LTX2 for improved temporal control
  - *From: Kijai*


## Resources & Links

- **NVFP4 converted models** (model)
  - https://huggingface.co/topmass/ComfyUI-NVFP4/tree/main
  - *From: topmass*

- **Wan2.1 UnifiedReward LoRA** (lora)
  - https://huggingface.co/CodeGoat24/Wan2.1-T2V-14B-UnifiedReward-Flex-lora
  - *From: yi*

- **SCAIL Preview GGUF** (model)
  - https://huggingface.co/vantagewithai/SCAIL-Preview-GGUF/tree/main
  - *From: xwsswww*

- **Causal-Forcing** (repo)
  - https://github.com/thu-ml/Causal-Forcing
  - *From: JohnDopamine*

- **TeleStyle** (repo)
  - https://github.com/Tele-AI/TeleStyle
  - *From: Tonon*

- **ComfyUI WAN I2V Control** (tool)
  - https://github.com/shootthesound/comfyui-wan-i2v-control
  - *From: The Shadow (NYC)*

- **SkyReels V3 V2V model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/SkyReelsV3/Wan21-SkyReelsV3-V2V_fp8_scaled_mixed.safetensors
  - *From: Kijai*


## Known Limitations

- **MOVA hardware requirements**
  - 1 hour generation for 8sec 720p video, won't work with 8GB cards, went OOM on full VRAM setting
  - *From: Stef*

- **Wan2.2 training complexity**
  - Twice as hard to train new technologies for Wan2.2 because you have to train it twice (high and low noise)
  - *From: Ablejones*

- **TeleStyle heavy style limitations**
  - Breaks with heavy styles like big pixels, pushes toward realism when style image is heavily stylized
  - *From: Kytra*

- **Self-refine speed on 14B**
  - Insanely slow on 14B models, can't be bothered to test thoroughly
  - *From: Kijai*


## Hardware Requirements

- **MOVA VRAM/RAM**
  - Requires more than 8GB VRAM, went OOM on full VRAM setting, had to use mixed mode. Some people still run 8GB VRAM and 16GB RAM
  - *From: Stef*

- **Wan2.2 vs Wan2.1 resources**
  - Wan2.2 designed to run much more powerful inference without needing more VRAM than Wan2.1
  - *From: Ablejones*


## Community Creations

- **WanVideoWrapper** (node)
  - Kijai's wrapper system being sunset in favor of native implementations due to maintenance burden
  - *From: Kijai*

- **Self-refine video node** (node)
  - Video enhancement sampler that acts like different sampler, improves quality significantly
  - *From: Kijai*
