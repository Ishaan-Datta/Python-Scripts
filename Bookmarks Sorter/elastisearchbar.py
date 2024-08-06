# later add in statistics and databse to analyze the massive library, detect common domains and ignore them in later searches
# maybe need to use vector approach to represent words
# natural language sorting: maybe list all keywords (not connector words (any generic verbs or nouns) any names basically)

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text1 = "hi my name is ishaan"
text2 = "hi my name is shaan"

# Convert the texts into TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([text1, text2])

# Calculate the cosine similarity between the vectors
similarity = cosine_similarity(vectors)
print(similarity)


# NEW
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("punkt")  # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


"""remove punctuation, lowercase, stem"""


def normalize(text):
    return stem_tokens(
        nltk.word_tokenize(text.lower().translate(remove_punctuation_map))
    )


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words="english")


def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


print(cosine_sim("a little bird", "a little bird"))
print(cosine_sim("a little bird", "a little bird chirps"))
print(cosine_sim("a little bird", "a big dog barks"))


# pip install spacy
# python -m spacy download en_core_web_sm
# Then use like so:

import spacy

nlp = spacy.load("en_core_web_sm")
doc1 = nlp("Hello hi there!")
doc2 = nlp("Hello hi there!")
doc3 = nlp("Hey whatsup?")

print(doc1.similarity(doc2))  # 0.999999954642
print(doc2.similarity(doc3))  # 0.699032527716
print(doc1.similarity(doc3))  # 0.699032527716
