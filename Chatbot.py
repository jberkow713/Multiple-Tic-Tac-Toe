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
import random 

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
#   json.dump(model, fp)    

# def get_w2v2(sentence, model):
#     """
#     :param sentence: inputs a single sentences whose word embedding is to be extracted.
#     :param model: inputs glove model.
#     :return: returns numpy array containing word embedding of all words    in input sentence.
#     """
#     list_vec = []
#     b = sentence.lower()
#     b = re.sub(r'[^\w\s]','',b)
#     A = b.split()
#     for word in A:
#         for k, v in model.items():
#             if k == word:
#                 list_vec.append(v)
#     if len(list_vec)>=1:
#         return list_vec
#     else:
#         for k,v in model.items():
#             if k == 'the':
#                 list_vec.append(v)
#         return 0

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
def get_w2v2(sentence, model):
    """
    :param sentence: inputs a single sentences whose word embedding is to be extracted.
    :param model: inputs glove model.
    :return: returns numpy array containing word embedding of all words    in input sentence.
    """
    list_vec = []
    b = sentence.lower()
    b = re.sub(r'[^\w\s]','',b)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(b)
    x = [token.pos_ for token in doc]
    
    A = b.split()
    # print(A)

    
    Acceptable_POS = ['NOUN', 'ADJ', 'ADV', 'PROPN', 'VERB']
    Text_Dict = dict(zip(A, x))
    
    not_used = ['is', 'the', 'a', 'and']
    A_ = []
    for k,v in Text_Dict.items():
        if v in Acceptable_POS:
            if k not in not_used and len(k)>2:
                A_.append(k)   
    
    final_words = []
    for word in A_:
        for k, v in model.items():
            if k == word:
                final_words.append(k)
                list_vec.append(v)
    # print(final_words)            
    return list_vec  

def Avg_sentence_vec_2(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    Vectors = get_w2v2(sentence,model)
    if len(Vectors)>0:
        Avg_Vector =  np.average(Vectors, axis=0)
        return Avg_Vector   
    else:
        return np.zeros(300)




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
def Vec_for_Clustering_2(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    If vector does not exist returns bunch of 0s so as not to ruin Clustering function below
    '''
    
    Vectors = get_w2v2(sentence, model)
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
      

def find_POS_tuple(sentence):
    #returns list of tuples to cover duplicate words not covered in dict
    nlp = spacy.load("en_core_web_sm")
    
    inpt = tokenize(str(sentence))
    inpt = ' '.join(word for word in inpt) 

    doc = nlp(inpt)
    x = [token.pos_ for token in doc]

    text = inpt.split()
    tuple_list = []
    
    length = len(x)
    index = 0
    while length >0:
        a = x[index]
        b = text[index]
        c = (b,a, index)
        tuple_list.append(c)

        index +=1
        length -=1 
   
    return tuple_list 

def find_object_importance(sentence):
    '''
    Parses sentence to find words of interest and descriptive words for each
    '''
    secondary_terms = []
    structure = find_POS_tuple(sentence)
    for x in structure:
        if x[1]== 'PRON':
            secondary_terms.append(x[0])
    
    order = list(enumerate(structure))
    
    valuable_terms = []
    for x in order:
        if x[1][1] == 'DET':
            num = x[0]+1 
            count = 0 
            noun_search = True
            while noun_search == True:
                 nxt = order[num]
                 if nxt[1][1]=='NOUN':
                     value = (nxt[1][0], count)
                     valuable_terms.append(value)
                     noun_search = False
                 else:
                     num +=1
                     count +=1      
    return valuable_terms, secondary_terms

def Pronoun_Type(pronoun):
    Pronoun_Dict = {'Personal':['i', 'we', 'you', 'he', 'she', 'it', 'they'], 'Object':['me', 'us', 'you', 'her', 'him', 'it' , 'them'], \
        'Possessive': ['mine', 'ours', 'yours', 'your', 'her', 'his', 'their'],\
            'Reflexive':['myself', 'yourself', 'herself', 'himself', 'itself', 'ourselves', 'yourselves', 'themselves'],\
                'Intensive': ['myself', 'yourself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'],\
                    'Indefinite': ['ALL', 'another', 'ANY', 'anybody', 'anyone', 'anything', 'both', 'each', 'either', \
                        'everybody', 'everyone', 'everything', 'few', 'many', 'most', 'neither', 'nobody', 'none', 'no one',\
                            'nothing', 'one', 'other', 'others', 'several', 'some', 'somebody', 'someone', 'something', 'such'], \
                                'Demonstrative': ['such', 'that','these', 'this', 'those'], \
                                    'Interrogative': ['what', 'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose'],\
                                        'Relative': ['as', 'that', 'what', 'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose'],\
                                            'Archaic': ['thou', 'thee', 'thy', 'thine', 'ye']}
    
    
    types = []
    for k,v in Pronoun_Dict.items():
        for x in v:
            
            if pronoun == x:
                types.append(k)
    if pronoun == 'all' or pronoun == 'any':
        return 'Indefinite'
    
    return types             


class Chatbot:
    #Class created to initially divide word list into sub categories, to be stored and used by Chatbot
    def __init__(self, word_count):
        self.model = model
        #list of words
        self.words = self.create_words(word_count)
        self.cluster = self.create_cluster()
        #List of Lists of ordered clustered words
        self.Ordered_Cluster_List = None
        self.Ordered_Cluster_Count = 0
        self.Reduced_Cluster_List = None
        self.Final_Cluster_List = []
        self.response = None
        self.response_list = None
        self.structure = None
        self.sentence_relationships = []   

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
    def create_cluster(self):
               
        Cluster_Dict = Cluster_Labels(self.words, model)
        self.cluster = Cluster_Dict
        return Cluster_Dict

    def create_word_cluster_list(self, *args):
        #Returns a list of lists for a cluster dictionary
        if len(args)==0:
            DICT = self.cluster
        if len(args)>0:
            DICT = args[0]    
        vals = set()
        lst = []

        for k,v in DICT.items():
            vals.add(int(v))
        for x in vals:
            lst.append(x)
        srted = sorted(lst)    

        length = len(srted)
        index = 0
        Big_List = []
        while length >0:
            curr_list = []
            for k,v in DICT.items():
                if v == str(srted[index]):
                    curr_list.append(k)
            Big_List.append(curr_list)
            length -=1
            index +=1
        
        if self.Ordered_Cluster_List == None:
            self.Ordered_Cluster_List = Big_List
        
        return Big_List    

    def recluster(self, list_, length):
        
        Reclustered_List_ = []
        #This list_ needs to be a list of lists
        
        for x in list_:            
            
            if len(x)<length and len(x)>=2:
                
                Reclustered_List_.append(x)         
        
            if len(x)>=length:                
                
                #Clustered_Dict for each list in our giant list that is passed in
                Reclustered_Dict = Cluster_Labels(x, model)
                               
                #This will be turned into a list of lists
                Reclustered_List = self.create_word_cluster_list(Reclustered_Dict)
                                
                length = len(Reclustered_List)
                index = 0
                new_reclustered_list = []
                while length >0:
                    curr = Reclustered_List[index]
                    if len(curr)>=2:
                        new_reclustered_list.append(curr)
                    length -=1
                    index +=1
                
                Reclustered_List_.append(new_reclustered_list)              
        
        self.Reduced_Cluster_List = Reclustered_List_

    def recluster_recursive(self, list_, length):
        #Takes Ordered_Cluster_List and recursively reduces lists into smaller, more intelligent lists of similar words
        
                #Takes Ordered_Cluster_List and recursively reduces lists into smaller, more intelligent lists of similar words
        if self.Ordered_Cluster_Count == len(self.Ordered_Cluster_List):
                return
        
        for x in list_:
                    
            if len(x)>1 and len(x)<=length:
                
                self.Final_Cluster_List.append(x)
                
                if x in self.Ordered_Cluster_List:
                    self.Ordered_Cluster_Count+=1
            if len(x)>length:
                Reclustered_Dict = Cluster_Labels(x, model)
                Reclustered_List = self.create_word_cluster_list(Reclustered_Dict)
                
                if x in self.Ordered_Cluster_List:
                    self.Ordered_Cluster_Count+=1
                self.recluster_recursive(Reclustered_List, length)            
    
    
    def find_object_importance_recursive(self, sentence):
        # '''
        # Purpose of this function is to dissect the sentence into objects relating to other objects
        # input: sentence string
        # output: dictionary of one or many main objects and their connection to other words in the original sentence
        # '''
        
        self.structure = find_POS_tuple(sentence)
                
        if len(self.structure)== 0:
            return 

        primary_object = []
        current_pos = []
        for word in self.structure:
            
            if word[1] == 'PRON':
                
                pronoun = word[0]
                usable_objects = ['Personal', 'Object']
                                
                if Pronoun_Type(pronoun)[0] not in usable_objects:
                    
                    primary_object.append(pronoun)
                        
                if Pronoun_Type(pronoun)[0] in usable_objects:
                    
                    primary_object.append(word[0])
                    current_pos.append(word[2])
                    break 
                

            elif word[1] == 'DET':
                pos = word[2]
                for word in self.structure[pos+1:]:
                    if word[1]=='NOUN':
                        primary_object.append(word[0])
                        current_pos.append(word[2])
                        break
                break
        # find the initial object and its position, now look for nouns that follow
        amended_sentence = []
        self.structure = self.structure[current_pos[0]+1:]
        for word in self.structure:
            amended_sentence.append(word[0])

        sentence = ' '.join(amended_sentence)
        #Resetting the index value at start of self.structure to 0 so easier to manipulate
        self.structure = find_POS_tuple(sentence)
        
        related_nouns = []
        
        end_pos = []
        current_sentence = []

        for word in self.structure:
            if word[1]== 'NOUN':
                related_nouns.append(word[0])
                current_pos = word[2]
                
                break 
        
        for word in self.structure:
            if word[2]>current_pos:
                current_sentence.append(word[0])

        current_sentence = ' '.join(current_sentence)
             
        current_structure = find_POS_tuple(current_sentence)
        
        words_prior_to_verb = []

        for word in current_structure:
            if word[1]=='VERB':
                verb_location = word[2]
                break
        for word in current_structure:
            if word[2] < verb_location:
                if word[1] == 'NOUN':
                    related_nouns.append(word[0])

        
        for word in self.structure:
            if word[0] == related_nouns[-1]:
                last_noun_position = word[2]
        

        verbs = []
        for word in self.structure:
            if word[2] < last_noun_position:
                if word[1] == 'VERB':
                    verbs.append(word[0])
        
        final_connection = []
        for word in primary_object:
            final_connection.append(word)
        for word in verbs:
            final_connection.append(word)
        for word in related_nouns:
            final_connection.append(word)

        current_sentence = ' '.join(final_connection)
        #put current relationships into classes attribute to store it before recursion
        self.sentence_relationships.append(current_sentence)
        
        continued_sentence = []

        for word in self.structure:
            if word[2]>last_noun_position:
                continued_sentence.append(word[0])
        

        self.structure = find_POS_tuple(' '.join(continued_sentence))        

        #TODO 
        # Have parsed the original sentence, using parts of speech, we have created relationship between the primary object
        # and the nouns, using the verbs
        # then we want to run this function recursively, but we need to deal with conjunctions, and all of the fringe cases
        # where the next part of the sentence starts either with a conjunction, or a non personal pronoun
        # in which case, we simply want to link the following sentence back to the original primary object...
        # which we can do by referencing the sentence relationships, finding which of the words was the primary object,
        # and so on
        
    
    def find_response_list(self, user_response):
        chatbot_possible_response = []
        user_response = user_response.lower().replace('?', '')
        user_response = user_response.split()
        overall_usable_words = []
        for list in self.Final_Cluster_List:
            for word in user_response:
                if word in list:
                    overall_usable_words.append(list)
        
        
        self.response_list = overall_usable_words
        return self.response_list 


chatty = Chatbot(500)
chatty.create_word_cluster_list()

# chatty.recluster_recursive(chatty.Ordered_Cluster_List,10)
# print(chatty.Final_Cluster_List)
# print(len(chatty.Final_Cluster_List))
chatty.find_object_importance_recursive('the cat jumped over the moon ')
print(chatty.sentence_relationships)





# chatty.create_cluster()
# chatty.create_word_cluster_list(chatty.cluster)


# chatty.recluster_recursive(chatty.Ordered_Cluster_List)
# print(chatty.Final_Cluster_List)

# print(chatty.find_response_list('I walked to the park on a Sunday'))

# print(chatty.response)
# print(chatty.response_list)






