# NotebookLM Upload Files

Combined knowledge files ready for upload to Google NotebookLM.

## Folder Structure

```
for_notebooklm/
├── README.md                    # This file
├── ltx2/                        # LTX Video 2 knowledge
│   └── YYYY-MM-DD/              # Extraction date
│       ├── *_combined.md        # Upload this file to NotebookLM
│       └── manifest.txt         # What's included
├── wan/                         # Wan Video knowledge (future)
│   └── ...
└── [other models]/
```

## How to Use

1. Navigate to the model folder (e.g., `ltx2/`)
2. Find the latest dated folder
3. Upload the `*_combined.md` file to NotebookLM
4. Check `manifest.txt` to see what's included

## Updating NotebookLM

When new extractions are made:
1. A new dated folder will be created
2. Upload the new combined file to NotebookLM
3. Remove old sources if desired (or keep for comparison)

## Current Extractions

| Model | Latest | Coverage | Size |
|-------|--------|----------|------|
| LTX Video 2 | 2026-02-01 | Jan 6-31, 2026 | 695KB |
