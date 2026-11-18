#!/usr/bin/env python3
"""
make.fun competition entry runner for news-image-20261117.
Copies the pre-rendered front page entry.png to the designated output path.
"""

import os
from pathlib import Path
import shutil

def main() -> None:
    # Resolve paths relative to this script's directory
    script_dir = Path(__file__).resolve().parent
    source_image = script_dir / "entry.png"
    
    if not source_image.is_file():
        raise FileNotFoundError(
            f"Expected source image does not exist: {source_image}"
        )

    # Determine output directory: MAKEFUN_OUTPUT_DIR env var or default /output
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_dir = Path(output_dir_env) if output_dir_env else Path("/output")
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    destination_image = output_dir / "entry.png"
    
    # Copy file bytes exactly
    shutil.copyfile(source_image, destination_image)
    print(f"Successfully copied {source_image} to {destination_image}")

if __name__ == "__main__":
    main()
