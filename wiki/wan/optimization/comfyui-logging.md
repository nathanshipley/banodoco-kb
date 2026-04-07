---
title: ComfyUI Error Logging
aliases: [error-logging, colored-errors, comfy-errors]
last_updated: 2025-03-13
---

# ComfyUI Error Logging

A common usability issue with ComfyUI is that errors and regular print statements look similar in the console, making it easy to miss critical error messages.

## The Problem

> "omg how do I always miss these it looks the same an error and a print all cluttered, is it possible to make them huge and red?" — Juampab12, March 13, 2025

Errors in ComfyUI console output:
- Look similar to regular print statements
- Easy to miss in cluttered output
- No visual distinction (color, size, formatting)
- Can lead to wasted time debugging when errors are overlooked

**Example of missed error:**
```
ERROR lora diffusion_model.patch_embedding.weight shape '[1536, 16, 1, 2, 2]' is invalid for input of size 196608
```

This critical error was initially missed because it blended in with other console output.

---

## Current Status

As of March 13, 2025, Kijai is actively working on improving error logging:

> "I was literally just wondering about how to do error logging in color the best way" — Kijai, March 13, 2025

No solution has been implemented yet, but the issue is recognized and being addressed.

---

## Workarounds

### Copy/Paste to Text Editor

spacepxl's recommended approach:

> "I often just copy/paste into a text editor and ctrl-f" — spacepxl, March 13, 2025

**Process:**
1. Copy console output
2. Paste into text editor (VSCode, Notepad++, etc.)
3. Use Ctrl+F to search for "ERROR" or "error"
4. Review all errors systematically

**Advantages:**
- Works immediately without code changes
- Allows systematic review of all errors
- Can save console output for later reference

**Disadvantages:**
- Extra step required
- Interrupts workflow
- Doesn't prevent errors from being missed initially

---

## Desired Features

Community requests for improved error logging:

1. **Color coding:**
   - Errors in red
   - Warnings in yellow
   - Info in default color

2. **Size/formatting:**
   - Larger text for errors
   - Bold or highlighted
   - Clear visual separation

3. **Error summary:**
   - List of all errors at end of execution
   - Count of errors/warnings
   - Quick reference to error locations

---

## Technical Considerations

Kijai noted the challenge:

> "I was literally just wondering about how to do error logging in color the best way" — Kijai, March 13, 2025

**Challenges:**
- Console color support varies by platform (Windows, Linux, Mac)
- Terminal emulator compatibility
- Integration with existing logging systems
- Performance impact of formatting

**Potential solutions:**
- ANSI color codes (cross-platform)
- Rich library for Python (advanced formatting)
- Custom logging handler
- Separate error log file

---

## See Also

- [[troubleshooting]] — General troubleshooting guide
- [[comfyui]] — ComfyUI setup and usage

