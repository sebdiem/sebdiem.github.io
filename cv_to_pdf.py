#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf"]
# ///
"""
Print cv.html to PDF via Chrome headless.
Usage: uv run fix_pdf.py
Output: ~/Downloads/cv.pdf
"""

import subprocess
import fitz
from pathlib import Path

HTML   = Path(__file__).parent / "cv.html"
OUT    = Path.home() / "Downloads" / "cv.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ── Print to PDF via Chrome headless ──────────────────────────────────────────
print("🖨  Printing via Chrome headless…")
subprocess.run([
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--print-to-pdf={OUT}",
    "--print-to-pdf-no-header",
    "--no-pdf-header-footer",
    f"file://{HTML.resolve()}",
], check=True, capture_output=True)

print(f"✅ Saved to {OUT}")
