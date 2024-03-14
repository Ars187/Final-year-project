# Automated Video Segmentation

### Objective

* The main objective of our project is to create an automatically applied 
lecture video segmentation system that splits lectures into bite-sized 
topics using audio and video features.


### Pipeline

#### Step 1 : Audio Extraction - Use "Audio_extractor.py" file to extract the audio from video.
#### Step 2 : Audio Segmentation - Use "AudioSegment.py" file to segment the audio into chunks based on the silence in the audio.
#### Step 3 : Audio Transcription - Use "AudioTranscriber.py" file to transcribe the audio into text.
#### Step 4 : Embedding and Clustering - Use "Embedding_bert.py" file to embed the text files and cluster the embeds. It also converts the text clusters into audio.
#### Step 5 : Title extraction - Use "Cluster title.py" to extract the keywords from the audio file which will be used for generating a title for each cluster.

### Use "nmi.py" for finding the normalised mutual information between the ground truth and the segmentation.

