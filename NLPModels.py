from __future__ import unicode_literals
from sklearn.datasets import fetch_20newsgroups
import pandas as pd
import pandas as pd
import re
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import spacy
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import re
from pprint import pprint
import json 
import math
import collections
import csv
import sys
import codecs
from collections import defaultdict
import string
import numpy as np
from numpy import dot
from numpy.linalg import norm




def hasNumbers(inputString):
    return inputString.isalpha()
    # return any(char.isalpha() for char in inputString)

def convert_to_binary(embedding_path):
    """
    Here, it takes path to embedding text file provided by glove.
    :param embedding_path: takes path of the embedding which is in text format or any format other than binary.
    :return: a binary file of the given embeddings which takes a lot less time to load.
    """
    f = codecs.open(embedding_path + ".txt", 'r', encoding='utf-8')
    wv = []
    
    with codecs.open(embedding_path + ".vocab", "w", encoding='utf-8') as vocab_write:
        count = 0
        
        for line in f:
            if count == 0:
                count +=1
            elif count>0 and count <500000:
                splitlines = line.split()
                
                if hasNumbers(splitlines[0].strip())== True:
                    vocab_write.write(splitlines[0].strip())
                    vocab_write.write("\n")
                    wv.append([float(val) for val in splitlines[1:]])
                    count +=1
               
         
            else:
                
                break    
                
                    
    np.save(embedding_path + ".npy", np.array(wv))

# convert_to_binary("glove.42B.300d")

def load_embeddings_binary(embeddings_path):
    """
    It loads embedding provided by glove which is saved as binary file. Loading of this model is
    about  second faster than that of loading of txt glove file as model.
    :param embeddings_path: path of glove file.
    :return: glove model
    """
    with codecs.open(embeddings_path + '.vocab', 'r', 'utf-8') as f_in:
        index2word = [line.strip() for line in f_in]
    wv = np.load(embeddings_path + '.npy')
    model = {}
    for i, w in enumerate(index2word):
        model[w] = wv[i]
    # with open('Embedding_Model.json', 'w') as fp:
    #     json.dump(model, fp) 
    return model

model = load_embeddings_binary("glove.42B.300d")
# with open('Embedding_Model.json', 'w') as fp:
#     json.dump(model, fp)    

def get_w2v(sentence, model):
    """
    :param sentence: inputs a single sentences whose word embedding is to be extracted.
    :param model: inputs glove model.
    :return: returns numpy array containing word embedding of all words    in input sentence.
    """
    list_vec = []
    b = sentence.lower()
    b = re.sub(r'[^\w\s]','',b)
    A = b.split()
    for word in A:
        for k, v in model.items():
            if k == word:
                list_vec.append(v)
    return list_vec
    # return np.array([model.get(val, np.zeros(300)) for val in sentence.split()], dtype=np.float64)

# print(get_w2v("how are you doing?", model))
# print(model["hello"])
# print(model["there"])
def vec(word,model):
    #Gets vector for specific word, given specific model
    for k,v in model.items():
        if word == k:
            return v
# print(vec("cow", model))        

# cosine similarity
def cosine(v1, v2, model):
    #Compares distances between 2 words in terms of cosine similarity 
    v1 = vec(v1, model)
    v2 = vec(v2, model)
    
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0
# print(cosine('dog', 'puppy', model))        

# print(cosine('dog', 'puppy', model) > cosine('horse', 'chicken', model))


def closest(model, vec_to_check, n=10):
    #Slow function, takes word, compares distance to all words in model, finds closest, will improve for speed
    token_list = []
    for key in model.keys():
        token_list.append(key)

    return sorted(token_list,
                  key=lambda x: cosine(vec_to_check, vec(x,model), model),
                  reverse=True)[:n]

# print(closest(model, 'pants', n=10 ))


def Avg_sentence_vec(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    Vectors = get_w2v(sentence,model)
    data = []
    for x in Vectors:
        data.append(x)
    Avg_Vector =  np.average(data, axis=0)
    return Avg_Vector   

def cosine_sentence(v1,v2, model):
    '''
    Finds cosine similarity between 2 sentences
    '''
    v1 = Avg_sentence_vec(v1, model)
    v2 = Avg_sentence_vec(v2, model)

    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

def get_relevant_sentence(input_str:str):

    nlp = spacy.load("en_core_web_sm")
    input_str = input_str.replace(',','')
    input_str = input_str.replace('.', '')
    input_str = input_str.replace('-', ' ')
    inpt = input_str.lower()
    
    doc = nlp(inpt)
    x = [token.pos_ for token in doc]
    text = input_str.split()
    
    Text_Dict = dict(zip(text, x))
    Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB', 'PRON']
    # Acceptable_POS = ['NOUN', 'PRON', 'VERB', 'ADJ' ]
    Acceptable_words = []
    for word, POS in Text_Dict.items():
        if POS in Acceptable_POS:
            Acceptable_words.append(word)
    sentence = ' '.join(word for word in Acceptable_words)    

    return(sentence)

def Advanced_Avg_sentence_vec(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    sentence = get_relevant_sentence(sentence)
    #Have to turn this list of relevant words into a new string
    # sentence = ' '.join(word for word in sentence)

    Vectors = get_w2v(sentence,model)
    data = []
    for x in Vectors:
        data.append(x)
    Avg_Vector =  np.average(data, axis=0)
    return Avg_Vector
def Advanced_cosine_sentence(v1,v2, model):
    '''
    Finds cosine similarity between 2 sentences
    '''
    v1 = Advanced_Avg_sentence_vec(v1, model)
    v2 = Advanced_Avg_sentence_vec(v2, model)

    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

# print(get_POS("hi I am a tuba"))    

# A =Avg_sentence_vec("Hi, I am a battleship", model)
# B= Avg_sentence_vec("Hello, I am a cruise ship", model)
A = "engages in retail and wholesale business. The Company offers an assortment of merchandise and services at everyday low prices. ... The Walmart International segment manages supercenters, supermarkets, hypermarkets, warehouse clubs, and cash & carry outside of the United States."
B = "designs, manufactures and markets mobile communication and media devices, personal computers and portable digital music players. The Company sells a range of related software, services, accessories, networking solutions, and third-party digital content and applications"
# print(Advanced_cosine_sentence(A, B, model))
# print(cosine_sentence(A,B,model))
# print('--------------')


C = "world's leading specialist in providing institutional investors with investment servicing, investment management and investment research and trading services"
D = "general merchandise retailer selling products through its stores and digital channels. The Company's general merchandise stores offer an edited food assortment, including perishables, dry grocery, dairy and frozen items"
E = 'Department Stores'
F = 'electronic computers'
G = 'STATE COMMERCIAL BANKS'
H = 'RETAIL-VARIETY STORES'
print(Advanced_cosine_sentence(A, E, model))
print(cosine_sentence(A,E, model))
print(get_relevant_sentence(A))
print(get_relevant_sentence(E))


#So far both models are close, quite predictive in terms of SIC Code and company description
#Advanced model may be better in the end, will just have to keep testing
#Next step is to integrate it with SIC codes, compare it's code to ALL SIC codes, and have it return one with 
# highest cosine similarity 