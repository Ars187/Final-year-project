from jiwer import wer
import pysrt
file = open("D:\\Project\\CwS\\chunks\\transcribed\\comparison\\result.txt", "r")
string = file.read()
file.close()
file = open("D:\\Project\\CwS\\chunks\\transcribed\\comparison\\result1.txt", "r")
string1 = file.read()
file.close()
string2 = ""
subs = pysrt.open("D:\\Project\\CwS\\mit039\\segmentation\\subtitles\\MIT8_20IAP21_lec01_300k.srt")
for sub in subs:
    string2 += " "+ sub.text
string2  = string2.replace("\n", " ")
string2 = string2.replace("[INAUDIBLE]","")
string2 = string2.replace("MARKUS KLUTE","")
string2 = string2.replace("  "," ")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for ele in string:
    if ele in punc:
        string = string.replace(ele, "")
for ele in string1:
    if ele in punc:
        string1 = string1.replace(ele, "")        
for ele in string2:
    if ele in punc:
        string2 = string2.replace(ele, "")
print(string2)
w = wer(string2, string)
print(w)
w1 = wer(string2, string1)
print(w1)