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
from multiprocessing import Pool
import concurrent.futures
from sklearn.cluster import KMeans

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
            elif count>0 and count <300000:
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


def get_w2v2(sentence, model):
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
    if len(list_vec)>=1:
        return list_vec
    else:
        for k,v in model.items():
            if k == 'the':
                list_vec.append(v)
        return 0

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
    

def vec(word,model):
    #Gets vector for specific word, given specific model
    for k,v in model.items():
        if word == k:
            return v
      

def cosine(v1, v2, model):
    #Compares distances between 2 words in terms of cosine similarity 
    v1 = vec(v1, model)
    v2 = vec(v2, model)
    
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

def closest(model, vec_to_check, n=10):
    #Slow function, takes word, compares distance to all words in model, finds closest based on n
    token_list = []
    for key in model.keys():
        token_list.append(key)

    return sorted(token_list,
                  key=lambda x: cosine(vec_to_check, vec(x,model), model),
                  reverse=True)[:n]

# print(closest(model, 'pants', n=10 ))
def tokenize(text):
    """Parses a string into a list of semantic units (words)
    Args:
        text (str): The string that the function will tokenize.
    Returns:
        list: tokens parsed out by the mechanics of your choice
    """
    
    tokens = re.sub('[^a-zA-Z 0-9]', '', text)
    tokens = tokens.lower().split()
    
        
    return tokens 


from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer(language='english')


def Avg_sentence_vec(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    '''
    Vectors = get_w2v(sentence,model)
    Avg_Vector =  np.average(Vectors, axis=0)
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


def check_in_list(Word, List):
    
    Words = []
    for phrase in List:
        A = tokenize(phrase)
        for x in A:
            if x not in Words and len(x)>2:
            
                Words.append(x)
    
    for word in Words:
        x = stemmer.stem(word)
        if x not in Words:
            Words.append(x)            

    for x in Words:
        if x in Word:
            return True 
    else:
        return False

def Vec_for_Clustering(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    If vector does not exist returns bunch of 0s so as not to ruin Clustering function below
    '''
        
    Vectors = get_w2v(sentence,model)
    if len(Vectors)>0:
        Avg_Vector =  np.average(Vectors, axis=0)
        return Avg_Vector
    else:
        return np.zeros(300)


def Cluster_Labels(List, model):
    '''
    Takes a list of words, clusters them based on their average vector
    '''
    list_of_vectors = [Vec_for_Clustering(x, model).tolist() for x in List]        
    nparray = np.array(list_of_vectors)    
        
    clusters = int(math.floor(math.sqrt(len(list_of_vectors))))
    
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(nparray)
    categorized_list = kmeans.labels_
    string_list = [str(x) for x in categorized_list]
    
    Categorized_Dict = dict(zip(List, string_list))
    return Categorized_Dict                


# new_list_1 = []
# Cluster_Dict = Cluster_Labels(list_1, model)
# for k,v in Cluster_Dict.items():
#     if v == '1':
#         new_list_1.append(k)

# print(new_list_1)

class Chatbot:
    def __init__(self, word_count):
        self.model = model
        #list of words
        self.words = self.create_words(word_count)
        self.current_cluster = None 
    def create_words(self, word_count):
        counter = 0
        with open("glove.42B.300d.vocab", 'r',encoding='cp850') as file:
            words = []
            for line in file:
                if counter == word_count:
                    break    
                line=line.strip()
                words.append(line)
                counter +=1
            return words     
    def choose_cluster(self, cluster):
        list_ = []
        Cluster_Dict = Cluster_Labels(self.words, model)
        for k,v in Cluster_Dict.items():
            if v == str(cluster):
                list_.append(k)
        self.current_cluster = list_
        return list_

chatty = Chatbot(1000)
chatty.choose_cluster(1)
print(chatty.current_cluster)



