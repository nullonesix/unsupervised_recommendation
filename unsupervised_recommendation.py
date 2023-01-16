import pickle

with open('article_titles.pkl', 'rb') as doc:
    article_titles = pickle.load(doc)
with open('ml_wiki.pkl', 'rb') as doc:
    ml_wiki = pickle.load(doc)

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# "hello, world" -> ["hello", ",", "world"]

tokenized_article_titles = []
for title in article_titles:
    tokenized_article_titles.append(word_tokenize(title.lower()))
tokenized_ml_wiki = []
for subsection in ml_wiki:
    tokenized_ml_wiki.append(word_tokenize(subsection.lower()))

tokenized_data = tokenized_ml_wiki + tokenized_article_titles
# tokenized_data = tokenized_article_titles

# word2vec
# [A machine learning model to] cure all diseases
# [A machine     ?    model to] --> learning
#  1    0               0    0         0
#  0    1               0    0         0        
#  0    0               0    0         1
#  0    0               1    0         0
#  0    0               0    1         0
# ...  ...             ...  ...       ...

# input  = 1 1 0 1 1 ...
# output = 0 0 1 0 0 ...

# input --w1--> hidden --w2--> output
# a neural network with 2 layers: w1 and w2
# (vocab) (vocab, hidden) (hidden) (hidden, vocab) (vocab)
# 10,000                    100                    10,000
# tokenized_title --w1-->  vector

from gensim.models import Word2Vec

model = Word2Vec(tokenized_data, vector_size=100, window=5, min_count=1, workers=4)

# query = "A machine learning model to cure all diseases"
query = "metal sheet"

tokenized_query = word_tokenize(query.lower())

import numpy

def tokenized_title_to_vector(tokenized_title):
    token_vectors = []
    for token in tokenized_title:
        token_vectors.append(model.wv[token])
    title_vector = numpy.mean(token_vectors, axis=0)
    return title_vector

query_vector = tokenized_title_to_vector(tokenized_query)

from scipy.spatial.distance import cosine

def recommend(query_vector):
    scores = []
    for tokenized_article_title in tokenized_article_titles:
        article_title_vector = tokenized_title_to_vector(tokenized_article_title)
        score = cosine(query_vector, article_title_vector)
        scores.append(score)
    top_scoring_indices = numpy.argsort(scores)[::-1][:5]
    print()
    for rank, index in enumerate(top_scoring_indices):
        print(scores[index], article_titles[index])
    print()
        
recommend(query_vector)
# recommend(tokenized_title_to_vector(word_tokenize("Optimistic Meta-Gradients".lower())))
# recommend(tokenized_title_to_vector(word_tokenize("Progress measures for grokking via mechanistic interpretability".lower())))
# recommend(tokenized_title_to_vector(word_tokenize("Thompson Sampling with Diffusion Generative Prior".lower())))













