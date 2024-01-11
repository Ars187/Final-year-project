import whisper
# import speech_recognition as sr
import os 
import re
import os.path

model = whisper.load_model('base')
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

dir = "D:\\Project\\Dataset\\CwS\\mit039\\chunks\\"
list_files = os.listdir(dir)
for i in list_files:
    path = "D:\\Project\\Dataset\\CwS\\mit039\\transcribed\\" + i
    os.makedirs(path)
    for j in sorted_alphanumeric(os.listdir(dir + i)):
        try:
            res = model.transcribe(dir+i+"\\"+j, fp16 = False)
            print("Tran: ",res['text'])
            completeName = os.path.join(path, f"trans_{j}"+".txt")  
            file1 = open(completeName, "w")
            file1.write(res['text'])
            file1.close()
        except:
            print("Error")

# filenames = os.listdir("E:\\Project\\Dataset\\CwS\\mit039\\transcribed\\")
# for i in filenames:
#     os.makedirs("E:\\Project\\Dataset\\CwS\\mit039\\transcribed_combined\\"+i)
#     with open("E:\\Project\\Dataset\\CwS\\mit039\\transcribed_combined\\"+i+"\\result.txt", 'w') as outfile:
#         for j in sorted_alphanumeric(os.listdir("E:\\Project\\Dataset\\CwS\\mit039\\transcribed\\"+i)):
#             with open("E:\\Project\\Dataset\\CwS\\mit039\\transcribed\\" + i + "\\" + j) as infile:
#                 for line in infile:
#                     outfile.write(line)


# output_ext="txt"
# list_files = sorted_alphanumeric(os.listdir(dir))
# for i in list_files:
#     filename = dir+i
#     # initialize the recognizer
#     r = sr.Recognizer()
#     # open the file
#     with sr.AudioFile(filename) as source:
#         # listen for the data (load audio to memory)
#         try:
#             audio_data = r.record(source)
#             # recognize (convert from speech to text)
#             text = r.recognize_google(audio_data, language = 'en-US')
#             file = open(f'{path}{i}.{output_ext}',"w")
#             file.write(text)
#             print(text)
#             file.close()
#         except sr.UnknownValueError as e:
#             print("Error:", str(e))        
             

# filenames = sorted_alphanumeric(os.listdir(path))
# with open("D:\\Project\\CwS\\chunks\\transcribed\\comparison\\result1.txt", 'w') as outfile:
#     for fname in filenames:
#         print(fname)
#         try:
#             with open(path+fname) as infile:
#                 for line in infile:
#                     outfile.write(line)
#         except:
#             print("Error")