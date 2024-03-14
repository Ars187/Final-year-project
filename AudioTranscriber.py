import whisper
import os 
import re
import os.path

model = whisper.load_model('base')
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

dir = "D:\\Project\\Dataset\\CwS\\mit038\\chunks\\"
list_files = os.listdir(dir)
for i in list_files:
    path = "D:\\Project\\Dataset\\CwS\\mit038\\transcribed\\" + i
    os.makedirs(path)
    for j in sorted_alphanumeric(os.listdir(dir + i)):
        try:
            res = model.transcribe(dir+i+"\\"+j, fp16 = False)
            # print("Tran: ",res['text'])
            completeName = os.path.join(path, f"trans_{j}"+".txt")  
            file1 = open(completeName, "w", encoding="utf-8")
            file1.write(res['text'])
            file1.close()
        except:
            print("Error")

