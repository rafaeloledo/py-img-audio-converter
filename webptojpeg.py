import sys
from PIL import Image

if (Image is None):
    print("Pillow not found: pip install Pillow")

if len(sys.argv) < 3:
    print("usage: python webptojpeg.py input_file.webp output_file.jpg")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with Image.open(input_file) as img:
        img.convert("RGB").save(output_file, "JPEG")
        print(f"Successfully converted the {input_file} to {output_file}")
except Exception as e:
    print(f"Error: {e}")
