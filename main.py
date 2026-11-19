#!/usr/bin/env python3
"""Copy the entry image to the output directory, verifying its basic integrity."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "entry.png"
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

def main() -> None:
    data = SOURCE.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("entry.png is not a PNG")
    if len(data) > 1024 * 1024:
        raise ValueError("entry.png exceeds 1 MiB")
    # IHDR stores width and height in bytes 16..24 as big-endian uint32s.
    width, height = (int.from_bytes(data[i:i + 4], "big") for i in (16, 20))
    if max(width, height) > 1024:
        raise ValueError("entry.png exceeds 1024x1024")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "entry.png").write_bytes(data)

if __name__ == "__main__":
    main()
