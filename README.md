# Gradio Goods Generator

This repository contains a small Gradio app that uses the `google-genai` SDK to generate "character goods" (merch-style images) from an uploaded photo.

Files added:
- `app.py` — Gradio frontend
- `generator.py` — wrapper that calls `google-genai` and returns image bytes and caption
- `requirements.txt` — Python dependencies
- `.env.example` — example for `GEMINI_API_KEY`

Quick start (Windows PowerShell):

1. Create and activate a virtual environment (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements:

```powershell
pip install -r requirements.txt
```

3. Set your Gemini API key in the environment and run the app:

```powershell
$env:GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
python app.py
```

Open the local Gradio URL printed in the terminal and upload a photo.

Notes:
- The code expects `google-genai`'s `generate_content_stream` API similar to the example in `test.py`.
- `test.py` was updated to use the `GEMINI_API_KEY` environment variable.
# nano-banana-pro