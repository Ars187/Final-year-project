# from textblob import TextBlob
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import os
import nltk
import string
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('brown')

# def extract_noun_phrases(text):
#     blob = TextBlob(text)
#     return blob.noun_phrases

def clean_title(title):
    # Remove stopwords and punctuation from the title
    stop_words = set(nltk.corpus.stopwords.words('english') + list(string.punctuation))
    words = nltk.word_tokenize(title)
    cleaned_words = [word for word in words if word.lower() not in stop_words]
    
    return ' '.join(cleaned_words)
# #LDA
# dir = "D:\\Project\\Dataset\\Cws\\mit039\\transcribed_combined\\"
# for i in os.listdir(dir):
#     for j in os.listdir(dir+i):
#         # Sample essay
#         file = open(f'{dir}{i}\\{j}',"r")
#         essay = file.read()
#         file.close()
#         # Extract noun phrases from the essay
#         noun_phrases = extract_noun_phrases(essay)

#         # Clean the extracted noun phrases to create potential titles
#         cleaned_titles = [clean_title(title) for title in noun_phrases]

#         # Print the potential titles
#         print("Potential Titles:")
#         for title in cleaned_titles:
#             print(title)
            
#         # Select the best title (longest title in this case)
#         best_title = max(cleaned_titles, key=len)

#         # Print the best title
#         print("Best Title:", best_title)
#         try:
#             os.rename(f'{dir}{i}\\{j}',f'{dir}{i}\\{best_title}')
#         except:
#             os.rename(f'{dir}{i}\\{j}',f'{dir}{i}\\{best_title}1')



# Berttopic
vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="english")

model = BERTopic(
    vectorizer_model=vectorizer_model,
    language='english', calculate_probabilities=True,
    verbose=True
)
dir = "D:\\Project\\Dataset\\Cws\\mit039\\transcribed_combined\\"
for i in os.listdir(dir):
    for j in os.listdir(dir+i):
        # Sample essay
        file = open(f'{dir}{i}\\{j}',"r")
        essay = file.read()
        essay = essay.split(".")
        topics, probs = model.fit_transform(essay)
        # Get the representative words for the topic
        topic_repr_words = model.get_topic(topics[0])

        # Print the topic and representative words
        print(f"Topic: {topics[0]}")
        print(f"Representative Words: {topic_repr_words}")

        # Generate a title based on the representative words
        title = " ".join(topic_repr_words[:5][0][0])  # You can adjust the number of words as needed
        print(f"Generated Title: {title}")