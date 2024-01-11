from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
from pydub import AudioSegment
import os
import re


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


dir = "E:\\Project\\Dataset\\CwS\\mit039\\chunks\\"
docs = "E:\\Project\\Dataset\\CwS\\mit039\\transcribed\\"
list_files = os.listdir(docs)
for i in list_files:
    lst=[]
    embeds=[]
    chunk_file = sorted_alphanumeric(os.listdir(docs+i))
    for j in chunk_file:
        try:
            file = open(f'{docs}{i}\\{j}',"r")
            text = file.read()
            lst.append(text)
            file.close() 
        except:
            print("Error") 
        
    for k in lst:
        vectors = embedding_model.encode(k)
        embeds.append(vectors)
    print(embeds)

    ac = AgglomerativeClustering(n_clusters = None, distance_threshold = 2.8)
    agg_clusters = ac.fit_predict(embeds)

    clustered_text = {}
    for l, cluster_label in enumerate(agg_clusters):
        if cluster_label not in clustered_text:
            clustered_text[cluster_label] = []
        clustered_text[cluster_label].append(chunk_file[l])

    # Print the text chunks in each cluster
    # os.makedirs("E:\\Project\\Dataset\\CwS\\mit039\\combined\\"+ i)
    # os.makedirs("E:\\Project\\Dataset\\CwS\\mit039\\transcribed_combined\\"+i)
    # for cluster_label, chunks in clustered_text.items():
    #     print(f"Cluster {cluster_label} contains:")
    #     sound = []
    #     with open(f"E:\\Project\\Dataset\\CwS\\mit039\\transcribed_combined\\{i}\\{cluster_label}.txt", 'w') as outfile:
    #         for chunk in chunks:
    #             with open(f"E:\\Project\\Dataset\\CwS\\mit039\\transcribed\\{i}\\{chunk}") as infile:
    #                 for line in infile:
    #                     outfile.write(line)
    #             chunk = chunk.replace("trans_","")
    #             chunk = chunk.removesuffix(".txt")
    #             print(chunk)
    #             sound.append(AudioSegment.from_file(f"{dir}{i}\\{chunk}", format="wav"))
    #             combined = 0
    #             for x in sound:
    #                 combined += x 
    #         file_handle = combined.export(f"E:\\Project\\Dataset\\CwS\\mit039\\combined\\{i}\\{cluster_label}.mp3", format="mp3")
    


            
