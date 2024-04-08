import sys
from PIL import Image

if (Image is None):
    print("Pillow not found: pip install Pillow")
    sys.exit(1)

if len(sys.argv) < 3:
    print("usage: python webptojpeg.py input_file.webp output_file{.jpeg, .jpg, .png}")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Extracting output format from the output file extension
output_format = output_file.split('.')[-1].lower()

if output_format not in ['jpeg', 'jpg', 'png']:
    print("Invalid output file format. Please choose either 'jpeg', 'jpg' or 'png'.")
    sys.exit(1)

try:
    with Image.open(input_file) as img:
        if output_format in ['jpeg', 'jpg']:
            img.convert("RGB").save(output_file, "JPEG")
        else:
            img.save(output_file, "PNG")
        print(f"Successfully converted the {input_file} to {output_file}")
except Exception as e:
    print(f"Error: {e}")
