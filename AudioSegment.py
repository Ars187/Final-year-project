from pydub import AudioSegment
import os
dir = "D:\\Project\\Dataset\\CwS\\"
filename = "chunk"
AudioSegment.ffmpeg = "C:\\Users\\arung\\Downloads\\ffmpeg-2023-10-04-git-9078dc0c52-full_build\\bin\\ffmpeg.exe"

list_files = ["mit035","mit038","mit039","mit049","mit057","mit075","mit088"] #os.listdir("D:\\Project\\Dataset\\CwS\\")
path = "\\audio\\"
for i in list_files:
    for j in os.listdir(dir + i + path):
        p = dir + i + "\\chunks\\" + os.path.splitext(os.path.basename(j))[0]
        os.makedirs(p)
        audio = AudioSegment.from_mp3(dir + i + path + j)
        audio = audio + 10
        chunk_length = 8 * 1000 # in milliseconds
        chunks = [audio[i:i + chunk_length] for i in range(0, len(audio), chunk_length)]
        for k, chunk in enumerate(chunks):
            chunk.export(f"{p}\\{filename}{k}.wav", format="wav")

        print(f"Successfully split the audio file into {len(chunks)} chunks.")