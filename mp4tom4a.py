
import sys
from moviepy.editor import VideoFileClip

if (VideoFileClip is None):
    print("moviepy not found: pip install moviepy")

if len(sys.argv) < 3:
    print("usage: python mp4tom4a.py input_file.mp4 output_file.m4a")
    sys.exit(1)

input_file = sys.argv[1]    
output_file = sys.argv[2]

clip = VideoFileClip(input_file)

audio = clip.audio

audio_codec = "aac"

audio.write_audiofile(output_file, codec=audio_codec)

clip.close()

print(f"Successfully converted {input_file} to {output_file}.")
