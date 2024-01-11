import os
import re
import librosa
import numpy as np
import warnings
from sklearn.metrics import normalized_mutual_info_score

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def load_audio(file_path):
    # Load audio file using librosa
    audio, _ = librosa.load(file_path, sr=None)
    return audio

def calculate_nmi(audio_file1, audio_file2):
    # Load audio files
    signal1 = load_audio(audio_file1)
    signal2 = load_audio(audio_file2)

    # Ensure the signals have the same length
    min_len = min(len(signal1), len(signal2))
    signal1 = signal1[:min_len]
    signal2 = signal2[:min_len]

    # Compute the magnitude spectrogram
    Sxx1 = np.abs(librosa.stft(signal1))
    Sxx2 = np.abs(librosa.stft(signal2))

    # Extract MFCC features
    mfcc1 = librosa.feature.mfcc(S=librosa.power_to_db(Sxx1))
    mfcc2 = librosa.feature.mfcc(S=librosa.power_to_db(Sxx2))

    # Flatten the matrices to 1D arrays
    flat_mfcc1 = mfcc1.flatten()
    flat_mfcc2 = mfcc2.flatten()

    # Calculate normalized mutual information
    nmi = normalized_mutual_info_score(flat_mfcc1, flat_mfcc2)
    return nmi

# Example usage
dir = "E:\\Project\\Dataset\\Cws\\mit039\\combined\\"
files = os.listdir(dir)
doc = "E:\\Project\\Dataset\\Cws\\mit039\\audiogt\\"
gt = os.listdir(doc)
k=0
c=1
warnings.simplefilter('ignore')
for i in files:
    print(f"Lecture {c}")
    c=c+1
    for j in sorted_alphanumeric(os.listdir(dir+i)):
        try:
            audio_file1 = dir+i+"\\"+j
            audio_file2 = doc + gt[k]
            k=k+1
            nmi_value = calculate_nmi(audio_file1, audio_file2)
            print(f"Normalized Mutual Information: {nmi_value}")
        except: 
            print("Error")



