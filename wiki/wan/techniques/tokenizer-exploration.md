---
title: UMT5 Tokenizer Exploration
aliases: [tokenizer-exploration, umt5-tokens, special-tokens]
last_updated: 2025-03-14
---

# UMT5 Tokenizer Exploration

The UMT5-XXL text encoder used by Wan contains special tokens and leftover training tokens that can be used to influence generation in interesting ways. These tokens can target specific datasets, modify style, or produce unusual effects.

> "you can make some weird shit with leftover tokens they have in there" — fredbliss, March 14, 2025

---

## Overview

**Discovered:** March 14, 2025 by fredbliss

**Key insight:** The UMT5 tokenizer contains special tokens used during training for different tasks and datasets. These tokens remain functional and can be used in prompts to influence generation.

**Vocabulary size:** 256,300 tokens

---

## Token Categories

### Dataset Targeting Tokens

These tokens were used during training to identify different data sources:

```
['[eod]', '[web]', '[wiki]', '[translate]', '[convo]', '[fc]', '[ffc]', '[code]', '[book]', '[c4]', '[news]', '[forum]', '[eot]']
```

**Usage:** Prefix or include in prompt to target specific training data characteristics.

**Examples:**
- `[wiki] <your prompt>` — Target Wikipedia-style data
- `[web] <your prompt>` — Target web content
- `[book] <your prompt>` — Target book-style content
- `[translate] <your prompt>` — Target translation data

> "a prompt of `[wiki] <x>` where x is your prompt, or rearranging that word, should target wiki data" — fredbliss, March 14, 2025

### Extra ID Tokens

High-ID tokens used for various T5 tasks:

```
['<extra_id_199>', '<extra_id_198>', '<extra_id_197>', ..., '<extra_id_0>']
```

**Usage:** Can be inserted into prompts for subtle effects.

**Example:**
```
[Subject]: Jim and Tom eat a <extra_id_100> hamburger
[Setting]: A 1950s diner
[Style]: 3D cartoon animation, bright colors, smooth shading <extra_id_50>
```

### Special Character Tokens

Odd tokens including emojis, mathematical symbols, and non-Latin scripts:

```
['😞', '🌽', '🍷', '⛪', '👯', '🏢', '🐊', '📔', '🖐', '⚓', ...]
```

**Usage:** Can produce unusual or unexpected results.

**Example:**
- Prompt: `🏏` (cricket bat emoji)
- Prompt: `▁Mexik` (partial word token)

### Hex Tokens

Low-level byte tokens:

```
['<0x00>', '<0x01>', '<0x02>', ..., '<0xA3>', '<0xED>', '<0xF3>', ...]
```

**Usage:** Experimental; effects unclear.

---

## Prompt Format

fredbliss's recommended prompt structure:

```
[Subject]: <description>
[Setting]: <location/environment>
[Style]: <visual style>
[Camera]: <camera angle/movement>
[Mood]: <emotional tone>
```

**With special tokens:**
```
[Subject]: Jim and Tom eat a <extra_id_100> hamburger
[Setting]: A 1950s diner
[Style]: 3D cartoon animation, bright colors, smooth shading <extra_id_50>
[Camera]: Medium shot
[Mood]: Comical
```

---

## Observed Effects

### Dataset Tokens

**[wiki]:**
- Subtle style changes
- May produce more encyclopedic or formal content
- Example: Adding `[wiki]` to style field changes visual characteristics slightly

**[translate]:**
- Tested with various prompts
- Effects not fully documented
- May influence multilingual aspects

### Combination Effects

**Multiple dataset tokens:**
- `[translate] [wiki]` — Combining tokens produces compound effects
- `[wiki] [eod]` — End-of-document marker with wiki targeting

### Negative Prompts

> "OH its also possible to put them in the negative prompt!" — fredbliss, March 14, 2025

Special tokens can be used in negative prompts to avoid certain data characteristics.

---

## T5 Task Prefixes

UMT5 was trained on various tasks with specific prefixes. These can be used to invoke task-specific behavior:

**Summarization:**
```
[Prefix]: summarize:
[Subject]: Jim and Tom eat a very large and detailed hamburger with many toppings in a retro 1950s diner with lots of decorations on the wall.
[Style]: 3D cartoon animation
[Camera]: Medium shot
[Mood]: Comical
```

**Hypothesis:** Using summarization prefix might compress concepts into embeddings, potentially allowing more information in a single prompt.

> "it made me wonder if we can summarize from t5 -> sumamrized embeddings and then concat the embeddings to get more concepts into a single embedding" — fredbliss, March 14, 2025

---

## Extraction Method

fredbliss used Python to scrape the UMT5 tokenizer:

**Strategies:**
1. **Strategy 1:** Identify odd tokens (7,640 found)
2. **Strategy 2:** Filter by specific patterns (200 found)
3. **Strategy 3:** Keyword filter (200 found)

**Code approach:**
- Load UMT5 tokenizer
- Iterate through vocabulary
- Filter by various criteria (special characters, ID ranges, keywords)
- Export interesting tokens

---

## Visual Examples

### Baseline Prompt
```
[Subject]: Jim and Tom eat a hamburger
[Setting]: A 1950s diner
[Style]: 3D cartoon animation, bright colors, smooth shading
[Camera]: Medium shot
[Mood]: Comical
```

### With [wiki] Token
```
[Subject]: Jim and Tom eat a hamburger
[Setting]: A 1950s diner
[Style]: 3D cartoon animation, bright colors, smooth shading, [wiki]
[Camera]: Medium shot
[Mood]: Comical
```

**Result:** "see how it changes subtly" — fredbliss

### Emoji Prompts

- `🏏` (cricket bat) — Produces cricket-related content
- Single emoji prompts work and produce relevant content

### Partial Word Tokens

- `▁Mexik` — Partial word for "Mexico"
- `▁kanskje ▁=>` — Norwegian word with arrow token

---

## Experimental Status

**As of March 14, 2025:**
- Initial exploration only (20 minutes of testing)
- Effects are subtle and not fully documented
- Workflow/inference script may not have been optimal
- More systematic testing needed

> "yeah but i dunno if my workflow / inference script was right" — fredbliss, March 14, 2025

> "Just need to build on top and explore i think" — fredbliss, March 14, 2025

---

## Potential Applications

### Dataset Targeting

- Use `[wiki]` for encyclopedic style
- Use `[book]` for literary style
- Use `[web]` for casual/modern style
- Use `[code]` for technical content

### Style Modification

- Insert extra_id tokens for subtle style variations
- Combine multiple dataset tokens for hybrid styles

### Concept Compression

- Use summarization prefix to compress long descriptions
- Potentially concatenate embeddings for more concepts per prompt

### Negative Prompting

- Use dataset tokens in negative to avoid certain styles
- Use special tokens to filter unwanted characteristics

---

## Token Lists

### Low ID Tokens (Task Markers)
```
['[eod]', '[web]', '[wiki]', '[translate]', '[convo]', '[fc]', '[ffc]', '[code]', '[book]', '[c4]', '[news]', '[forum]', '[eot]', '<0x00>', '<0x01>', '<0x02>', '<0x03>', '<0x04>', '<0x05>', '<0x06>']
```

### High ID Tokens (Extra IDs)
```
['<extra_id_199>', '<extra_id_198>', '<extra_id_197>', '<extra_id_196>', '<extra_id_195>', '<extra_id_194>', '<extra_id_193>', '<extra_id_192>', '<extra_id_191>', '<extra_id_190>', '<extra_id_189>', '<extra_id_188>', '<extra_id_187>', '<extra_id_186>', '<extra_id_185>', '<extra_id_184>', '<extra_id_183>', '<extra_id_182>', '<extra_id_181>', '<extra_id_180>']
```

### Sample Odd Tokens (Strategy 1)
```
['ட்', '്വ', '😞', 'ۖ', 'टि', '⟼', 'িজ', '▁জ', '్మ', 'దే', '🌽', '🍷', '̷', 'ၲ', 'रि', 'ரை', 'َى', '⛪', '▁ピ', '👯', '∥', 'ോള', '🏢', '🐊', '📔', '⌋', '̡', '។', '▁բ', '▁종', '➶', 'ಮು', 'ంత', '▁ர', 'ಸಾ', '🖐', '▁박', '▁치', '்ப', 'चि', '∈', 'ৃত', '۫', '⚓', 'ளா']
```

### Sample Odd Tokens (Strategy 2)
```
['〡', '፱', '⑧', 'ⅿ', 'ⅵ', '➂', '②', '㊽', '⁶', '⒖', 'Ⅰ', '㈩', '⑹', '⅓', '¹', '㉖', '⒕', '⓪', 'Ⅺ', '፲', 'ⅱ', '⒊', '❻', '⒒', '⅞', '⑼', '㈢', '⒑', 'Ⅾ', '⑴', '⅔', '⑥', '⒋', '୲', '⁹', '⒄']
```

### Sample Odd Tokens (Strategy 3 - Keyword Filter)
```
['<0xA3>', '<0xED>', '<0xF3>', '<extra_id_29>', '<0x71>', '<extra_id_23>', '>>', '<0x8A>', '\"<', '\\/', '<0x3A>', '$*', '<0xDB>', '§', '<extra_id_203>', '<0xCF>', '<extra_id_107>', '<0xC7>', '**', '▁(#', '<extra_id_18>', '<0x82>', '<0x2F>', '<0xAF>', '<0xD9>', '<extra_id_259>', '<extra_id_50>', '<extra_id_85>', ';\">', '?#', '<extra_id_246>', '<0x80>', '<extra_id_136>', '=>', '|', '▁>>>', '▁/>', '<0x83>', '<extra_id_140>', '<extra_id_194>', '<0xA2>', '<0xD0>', '<0xDD>']
```

---

## Community Interest

> "have any video examples using these tokens? in the main channel you said you can make weird videos." — TK_999, March 14, 2025

The community is interested in seeing more systematic exploration of these tokens and their effects on generation quality and style.

---

## Future Research

**Needed:**
- Systematic testing of each token category
- Documentation of visual effects
- Comparison of token combinations
- Integration with other prompting techniques
- Testing with different models (1.3B vs 14B)
- Exploration of negative prompt usage

**Questions:**
- Do these tokens work with Wan 2.2?
- Can they be combined with LoRAs?
- Do they affect motion or just style?
- Can summarization actually compress concepts?

---

## See Also

- [[wan-2.1]] — Base model using UMT5 encoder
- [[prompting]] — General prompting techniques
- [[multilingual]] — Multilingual prompting with UMT5

## External Resources

- [UMT5 Paper](https://arxiv.org/abs/2010.11934) — Original UMT5 research
- [T5 Documentation](https://huggingface.co/docs/transformers/model_doc/t5) — T5 model family documentation
