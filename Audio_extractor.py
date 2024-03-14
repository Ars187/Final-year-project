import os
import pandas as pd
import sys
from moviepy.editor import VideoFileClip

DIRECTORY = "D:\\Project\\Dataset\\CwS\\"
dir = "\\audio"
path = "\\segmentation\\videos\\"

def convert_video_to_audio_moviepy(i,j, video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(j)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{DIRECTORY}{i}{dir}\\{filename}.{output_ext}")

list_files = os.listdir(DIRECTORY)

for i in list_files:
    if not os.path.exists(DIRECTORY+i+dir):
        os.mkdir(DIRECTORY+i+dir)
    list_video = list(os.listdir(DIRECTORY+i+path))
    for j in list_video:
        convert_video_to_audio_moviepy(i,j, DIRECTORY+i+path+j)

    


