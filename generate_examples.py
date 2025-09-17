"""
generate_examples.py

This script generates simple test images (circle, square, triangle)
for the autostereogram project and saves them into assets/examples/.

Usage:
    python generate_examples.py
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw

# --- Configuration ---
OUTPUT_DIR = Path("assets/examples/")
IMAGE_SIZE = (256, 256)  # width x height in pixels

def create_output_dir():
    """
    Create the output directory if it does not exist.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✅ Output directory ready: {OUTPUT_DIR}")

def generate_circle():
    """
    Generate a white circle on black background.
    """
    img = Image.new("RGB", IMAGE_SIZE, "black")
    draw = ImageDraw.Draw(img)
    draw.ellipse([56, 56, 200, 200], fill="white")
    path = OUTPUT_DIR / "circle.png"
    img.save(path)
    print(f"✅ Circle image saved: {path}")

def generate_square():
    """
    Generate a white square on black background.
    """
    img = Image.new("RGB", IMAGE_SIZE, "black")
    draw = ImageDraw.Draw(img)
    draw.rectangle([70, 70, 180, 180], fill="white")
    path = OUTPUT_DIR / "square.png"
    img.save(path)
    print(f"✅ Square image saved: {path}")

def generate_triangle():
    """
    Generate a white triangle on black background.
    """
    img = Image.new("RGB", IMAGE_SIZE, "black")
    draw = ImageDraw.Draw(img)
    draw.polygon([(128, 40), (40, 200), (216, 200)], fill="white")
    path = OUTPUT_DIR / "triangle.png"
    img.save(path)
    print(f"✅ Triangle image saved: {path}")

def main():
    """
    Main function to generate all test images.
    """
    create_output_dir()
    generate_circle()
    generate_square()
    generate_triangle()
    print("🎉 All test images generated successfully!")

if __name__ == "__main__":
    main()
