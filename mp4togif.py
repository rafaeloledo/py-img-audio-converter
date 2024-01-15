import imageio
import sys

if (imageio is None):
    print("imageio not found: pip install imageio[ffmpeg]")

if len(sys.argv) < 3:
    print("usage: python mp4togif.py input_file.mp4 output_file.gif")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    video = imageio.get_reader(input_file)
    frames = [frame for frame in video]
    fps = 10
    imageio.mimsave(output_file, frames, duration=1/fps)
    print(f"Successfully converted the {input_file} to {output_file}")
except Exception as e:
    print(f"Error: {e}")
