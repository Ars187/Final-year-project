from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
dir = "D:\\Project\\Dataset\\CwS\\"
filename = "chunk"
AudioSegment.ffmpeg = "C:\\Users\\arung\\Downloads\\ffmpeg-2023-10-04-git-9078dc0c52-full_build\\bin\\ffmpeg.exe"

list_files = os.listdir("D:\\Project\\Dataset\\CwS\\")
path = "\\audio\\"
for i in list_files:
    for j in os.listdir(dir + i + path):
        p = dir + i + "\\chunks\\" + os.path.splitext(os.path.basename(j))[0]
        os.makedirs(p)
        audio = AudioSegment.from_mp3(dir + i + path + j)
        audio = audio + 10
        chunks = split_on_silence(audio, min_silence_len=2000,  silence_thresh=-40, keep_silence = 500)# Adjust this per requirement
        for k, chunk in enumerate(chunks):
            chunk.export(f"{p}\\{filename}{k}.wav", format="wav")
        print(f"Successfully split the audio file into {len(chunks)} chunks.")
        
