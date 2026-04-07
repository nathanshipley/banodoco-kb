---
title: WanSeamlessFlow (Prompt Blending)
aliases: [seamless-flow, wanseamlessflow, prompt-blending, granular-text-encode]
last_updated: 2025-03-17
---

# WanSeamlessFlow (Prompt Blending)

WanSeamlessFlow is an experimental technique for creating smooth transitions between multiple prompts in a single video generation by blending text embeddings at the frame level. Developed by fredbliss on March 17, 2025.

> "basically trying to do a smarter blend by creating more granular embeddings and blending at each timestep" — fredbliss, March 17, 2025

---

## Overview

WanSeamlessFlow addresses a fundamental limitation in multi-prompt video generation: transitions between prompts are often abrupt or produce artifacts (whiteouts, color shifts, etc.). By creating intermediate embeddings and blending them smoothly across frames, it aims to create more natural scene transitions.

**Key features:**
- Blends text embeddings based on frame position
- Supports multiple blend functions (linear, smooth, ease-in/out, sine, etc.)
- Can optimize prompt order automatically using nearest-neighbor search
- Works with context windowing for long videos
- Provides ASCII visualization of blend zones

**Status:** Experimental, active development as of March 17, 2025

---

## Installation

### Requirements

1. **Fork of Kijai's wrapper:**
   ```bash
   git clone https://github.com/fblissjr/fork-ComfyUI-WanVideoWrapper
   ```

2. **WanSeamlessFlow nodes:**
   ```bash
   git clone https://github.com/fblissjr/ComfyUI-WanSeamlessFlow
   ```

3. **Load example workflow:**
   - Located in `example_workflows/wanvideo_seamlessflow_long_T2V_example_01`

**Note:** The fork includes patches to Kijai's wrapper required for the technique to work. You can keep both the original wrapper and the fork installed.

---

## How It Works

### The Problem

> "we're blending text embeddings based purely on frame position, with no awareness of what the visual content actually looks like.... this means the transitions are 'time-based' rather than 'content-based' which sucks" — fredbliss, March 17, 2025

Standard multi-prompt workflows (using `|` separator) apply each prompt to a specific window of frames. When prompts are very different, this creates jarring transitions:

**Example issue:**
```
Prompt: "night forest with moonlight|day forest with sunlight"
Result: Extreme whiteout in middle frames as model tries to blend dark and bright
```

### The Solution

**WanSeamlessFlow creates intermediate embeddings:**

1. Parse prompts separated by `|`
2. Generate embeddings for each prompt
3. Create transition embeddings between main prompts
4. Blend embeddings smoothly across frames using mathematical functions
5. Apply blended embeddings at each sampling step

**Visualization example:**
```
viz: Transition visualization for 81 frames with 9 prompts
Section size: 9.0 frames, Blend width: 12 frames, Method: smooth

   0 ·░░░▒▒····░░░▒▒····░░░▒▒····░░░▒▒····░░░▒▒····░░░▒▒····░░░▒▒····░░░▒▒▓▓▓·▓▓▓▒▒░░   79
  80 ░   80

Legend:
┃ - Section boundary
▓▒░· - Blend zone (▓=strongest blend)
╶ - Regular frame
```

---

## Nodes

### WanVideoSmartBlend

**Purpose:** Main blending node that applies smooth transitions between prompts

**Inputs:**
- `text_embeds` — From WanVideoGranularTextEncode or standard text encode
- `blend_width` — Number of frames for blend zone (default: 8)
- `blend_method` — Interpolation function (linear, smooth, ease-in, etc.)
- `optimize_order` — Automatically reorder prompts for smoothest transitions

**Outputs:**
- `blended_embeds` — Smoothly blended embeddings
- `blend_info` — Metadata about blending

### WanVideoGranularTextEncode

**Purpose:** Creates intermediate transition prompts automatically

**Inputs:**
- `t5` — Text encoder
- `base_prompts` — Main prompts separated by `|`
- `negative_prompt` — Standard negative
- `transition_strength` — How strongly to blend (0.0-1.0, default: 0.5)
- `transition_count` — Number of intermediate prompts (default: 3)

**How it generates transitions:**
```python
if blend < 0.1:
    transition_prompt = f"{current_prompt}, transitioning to {next_prompt}"
else:
    transition_prompt = f"{current_prompt} ({1-blend:.2f}), {next_prompt} ({blend:.2f})"
```

**Example:**
- Main prompts: `"forest at night|forest at day"`
- Generates: `"forest at night", "forest at night, transitioning to forest at day", "forest at night (0.67), forest at day (0.33)", "forest at night (0.33), forest at day (0.67)", "forest at day"`

### WanVideoBlendVisualizer

**Purpose:** Shows ASCII visualization of blend zones in console

**Output:** Console visualization showing where blends occur across the video timeline

---

## Blend Functions

WanSeamlessFlow supports multiple mathematical blend functions:

```python
class BlendFunctions:
    @staticmethod
    def linear(ratio):
        """Linear interpolation - direct proportional blend"""
        return ratio

    @staticmethod
    def smooth(ratio):
        """Smoothstep function: 3x^2 - 2x^3"""
        return ratio * ratio * (3 - 2 * ratio)

    @staticmethod
    def ease_in(ratio):
        """Quadratic ease in - accelerating blend"""
        return ratio * ratio

    @staticmethod
    def ease_out(ratio):
        """Quadratic ease out - decelerating blend"""
        return ratio * (2 - ratio)

    @staticmethod
    def sine(ratio):
        """Sinusoidal easing - natural motion curve"""
        return 0.5 - 0.5 * math.cos(ratio * math.pi)

    @staticmethod
    def circ(ratio):
        """Circular easing - mimics circular motion"""
        return 1 - math.sqrt(1 - ratio * ratio)

    @staticmethod
    def bounce(ratio):
        """Bounce easing - mimics a bouncing effect"""
        # [implementation details]
```

**Recommended:** `smooth` (smoothstep) for most use cases

---

## Prompt Order Optimization

When `optimize_order` is enabled, WanSeamlessFlow uses nearest-neighbor search to reorder prompts for smoothest transitions:

```python
# Calculate embedding centroids
means = [torch.mean(embed, dim=0).to(torch.float32).cpu().numpy() for embed in embeddings]

# Nearest neighbor ordering
order = [0]  # Start with first prompt
remaining = set(range(1, len(means)))

while remaining:
    curr = order[-1]
    best_dist = float("inf")
    best_next = None
    
    for i in remaining:
        dist = np.sum((means[curr] - means[i]) ** 2)
        if dist < best_dist:
            best_dist, best_next = dist, i
    
    order.append(best_next)
    remaining.remove(best_next)
```

**Example output:**
```
WanSmartBlend: Optimized prompt order: [0, 4, 8, 5, 7, 6, 3, 1, 2]
```

This reorders prompts so semantically similar ones are adjacent, reducing jarring transitions.

---

## Settings & Best Practices

### Frame Count

**Minimum:** 81 frames recommended

> "need more frames lol" — fredbliss, March 17, 2025

**Why:** Short videos don't have enough frames for smooth blends. With 25 frames and 3 prompts, blend zones occupy most of the video.

**Recommended:**
- 81 frames: Minimum for 2-3 prompts
- 120+ frames: Better for 3-5 prompts
- 161+ frames: For complex multi-scene transitions

### Blend Width

**Default:** 8 frames

**Guidelines:**
- **3-4 frames:** Sharp transitions (more like cuts)
- **8-12 frames:** Balanced (recommended)
- **15-20 frames:** Very gradual transitions

**Trade-off:** Wider blends are smoother but occupy more of the video.

### Prompt Crafting

**Critical: Prompts must be semantically similar**

> "you basically gotta try and find smooth transitions" — fredbliss, March 17, 2025

**Good example:**
```
night forest, dim lighting, moonlight|dawn forest with early light|day forest, moderate brightness, sunlight
```

**Bad example:**
```
night forest|bright day scene
```

**Why:** Extreme differences (dark→bright, forest→city) cause whiteouts and artifacts.

**Use "staging" prompts:**
```
A cat walking in the park|A cat sitting in the park|A fishbowl in the park|A fishbowl with colorful fish
```

Intermediate prompts bridge the semantic gap.

### Lighting Consistency

**Problem:** Lighting differences cause whiteouts

**Solution:** Control brightness explicitly in prompts:
```
forest at night, subtle moonlight|forest at dawn, soft light|forest in daylight, bright sunlight
```

Avoid: `dark night scene|bright day scene` (too extreme)

---

## Known Issues

### Whiteout Effect

**Cause:** Blending prompts with drastically different lighting

**Symptoms:** Extremely bright (white) frames in transition zones

**Why it happens:**
> "The model is trying to satisfy two conflicting prompt embeddings (e.g., 'dark night' and 'bright day'). It overcompensates with extreme brightness to find a middle ground." — fredbliss (via Claude), March 17, 2025

**Solutions:**
1. Use staging prompts (night → dawn → day)
2. Increase video length (more frames for gradual transition)
3. Reduce blend width for short videos
4. Match semantic elements between prompts
5. Control brightness explicitly in prompts

### Spaces After Pipes

**Issue:** Spaces after `|` delimiters can cause problems

**Wrong:** `prompt 1 | prompt 2 | prompt 3`
**Right:** `prompt 1|prompt 2|prompt 3`

> "those prompts are wrong cuz they have spaces after pipes - i think that causes problems" — fredbliss, March 17, 2025

Spaces may be parsed as separate prompts, creating unintended embeddings.

### Context Window Confusion

**Issue:** Blend visualization doesn't align with sampling steps

> "i still don't quite get the overall logic with context windowing. In my head, each step should traverse each prompt evenly, but from the logging i just pasted, it seems to follow some other pattern" — TK_999, March 17, 2025

**Explanation:**
- The visualization shows frame-level blending
- Sampling steps process all frames but in context windows
- Prompt indices in logs show which context window is being processed
- These don't map 1:1 to the visualization

**Key insight:**
> "At each denoising step (of your 25-30 total steps), it processes all frames. But it processes them in context windows (groups of frames that it can handle at once). These windows follow a complex pattern to ensure all frames are covered efficiently." — fredbliss (via Claude), March 17, 2025

### Artifacts with Extreme Transitions

**Example:**
```
Prompt: "A cat walking in the park|A fishbowl with many colorful fish"
Result: "lsd trip" — fredbliss, March 17, 2025
```

Extreme semantic jumps produce surreal/psychedelic transitions even with blending.

---

## Comparison to Standard Multi-Prompt

| Aspect | Standard `|` Separator | WanSeamlessFlow |
|--------|------------------------|------------------|
| **Transition type** | Hard cuts between prompts | Smooth blends |
| **Artifacts** | Common (whiteouts, color shifts) | Reduced (but not eliminated) |
| **Prompt requirements** | Any prompts work | Must be semantically similar |
| **Complexity** | Simple | More complex setup |
| **Frame requirements** | Works with any length | Needs 81+ frames |
| **Control** | Limited | High (blend functions, width, order) |

---

## Future Development

### Content-Aware Blending

**Current limitation:**
> "we're blending text embeddings based purely on frame position, with no awareness of what the visual content actually looks like" — fredbliss, March 17, 2025

**Proposed solution (TK_999's idea):**
1. Generate video with initial A|B prompts
2. Use vision model to analyze transition frames
3. Generate new prompts based on actual visual content
4. Regenerate with refined prompts

**Challenge:** Requires vision model integration (CLIP, LLaVA, etc.)

### Hierarchical Scene Embeddings

**Goal:** Automatically break complex prompts into scenes and sub-scenes

**Example:**
```
Input: "man does A, man does B, then C happens, then man does D"
Output: Hierarchical embedding structure with smooth transitions
```

**Status:** Conceptual, not yet implemented

### Semantic Search Integration

**Idea:** Use embedding search to find optimal intermediate prompts

> "'every AI problem ends in search'" — fredbliss, March 17, 2025

**Potential approach:**
- Store library of prompt embeddings
- Use nearest-neighbor search to find semantic bridges
- Automatically generate staging prompts

---

## Example Workflows

### Basic Day/Night Transition

**Prompts:**
```
night forest, dim lighting, moonlight|dawn forest with early light|day forest, moderate brightness, sunlight
```

**Settings:**
- Frames: 120
- Blend width: 12
- Blend method: smooth
- Optimize order: true

### Complex Scene Transition

**Prompts:**
```
crowded futuristic cyberpunk city street with neon lights and flying vehicles, camera slowly moving backward|city gradually transitions to suburbs with less buildings and more trees, camera continues moving backward|suburbs fade into a forest path with sunlight filtering through trees, camera continuing the same motion|path opens to a vast mountain vista with pristine lake reflecting clouds, camera still moving backward
```

**Settings:**
- Frames: 161
- Blend width: 15
- Blend method: smooth
- Optimize order: true
- Context windows: enabled

### Fantasy Landscape Transformation

**Prompts:**
```
hyper-detailed fantasy landscape with snowy mountains and crystal waterfalls at dawn, cinematic lighting|the same landscape transforming to summer with lush forests and flowers in full bloom, golden hour|the landscape at night with bioluminescent plants and a full moon, showing stars and aurora borealis
```

**Settings:**
- Frames: 81
- Blend width: 12
- Blend method: ease_out
- Optimize order: true

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Whiteout in transitions | Use staging prompts; control brightness explicitly |
| Jarring cuts | Increase blend width; use more intermediate prompts |
| Surreal/psychedelic results | Prompts too different; add semantic bridges |
| "NoneType" errors | Remove spaces after `|` delimiters |
| Transitions too fast | Increase frame count; reduce number of prompts |
| Transitions too slow | Reduce blend width; use fewer intermediate prompts |
| Prompt order seems wrong | Enable optimize_order; check console for reordering |

---

## See Also

- [[context-windows]] — Long video generation technique
- [[wan-2.1]] — Base model
- [[latent-guides]] — Alternative control method
- [[flowedit]] — Video-to-video technique

## External Resources

- [WanSeamlessFlow GitHub](https://github.com/fblissjr/ComfyUI-WanSeamlessFlow) — Node implementation
- [Fork of Kijai Wrapper](https://github.com/fblissjr/fork-ComfyUI-WanVideoWrapper) — Required patches
