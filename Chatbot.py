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
    Pronoun_Dict = {'Personal':['i, we, you, he, she, it, they'], 'Object':['me, us, you, her, him, it , them'], \
        'Possessive': ['mine', 'ours', 'yours', 'your', 'her', 'his', 'their'],\
            'Reflexive':['myself, yourself, herself, himself, itself, ourselves, yourselves, themselves'],\
                'Intensive': ['myself', 'yourself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'],\
                    'Indefinite': ['ALL', 'another', 'ANY', 'anybody', 'anyone', 'anything', 'both', 'each', 'either', \
                        'everybody', 'everyone', 'everything', 'few', 'many', 'most', 'neither', 'nobody', 'none', 'no one',\
                            'nothing', 'one', 'other', 'others', 'several', 'some', 'somebody', 'someone', 'something', 'such'], \
                                'Demonstrative': ['such', 'that','these', 'this', 'those'], \
                                    'Interrogative': ['what', 'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose'],\
                                        'Relative': ['as', 'that', 'what', 'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose'],\
                                            'Archaic': ['thou', 'thee', 'thy', 'thine', 'ye']}
    
    if pronoun == 'all' or pronoun == 'any':
        return 'Indefinite'
    types = []
    for k,v in Pronoun_Dict.items():
        for x in v:
        
            if pronoun == x:
                types.append(k)
    return types             

print(Pronoun_Type('all'))


            
def find_object_importance_main(sentence):
    '''
    Purpose of this function is to dissect the sentence into objects relating to other objects
    input: sentence string
    output: dictionary of one or many main objects and their connection to other words in the original sentence
    '''
    structure = find_POS_tuple(sentence)
    #[('the', 'DET', 0), ('cat', 'NOUN', 1), ('was', 'AUX', 2), ('going', 'VERB', 3), ('to', 'PART', 4), ('travel', 'VERB', 5), \
    # ('to', 'ADP', 6), ('the', 'DET', 7), ('beach', 'NOUN', 8), ('and', 'CCONJ', 9), ('the', 'DET', 10), \
    # ('market', 'NOUN', 11), ('but', 'CCONJ', 12), ('went', 'VERB', 13),\
    #  ('to', 'ADP', 14), ('the', 'DET', 15), ('zoo', 'NOUN', 16)]
    primary_object = [None]
    current_pos = [None]
    for word in structure:
        if word[1] == 'PRON':
            primary_object[0] = word[0]
            current_pos[0] = word[2]
            break
        elif word[1] == 'DET':
            pos = word[2]
            for word in structure[pos+1:]:
                if word[1]=='NOUN':
                    primary_object[0]= word[0]
                    current_pos[0] = word[2]
                    break
            break
    # find the initial object and its position, now look for verbs following
    related_verbs = []
    related_nouns = []
    end_pos = [None]
    structure = structure[current_pos[0]+1:]
    for word in structure:
        if word[1]== 'NOUN':
            related_nouns.append(word[0])
            end_pos[0] = word[2]





    print(structure)        
    print(primary_object)          
    




    #initialize it with either a determinant referring to a NOUN or a Pronoun: 
    # This initial noun or pronoun will be the primary object in the sentence until a new primary object is created
    # In this case, the precedes Cat, so cat is primary object:
    # Then we take the verbs which follow the primary object, store them in a list, until we reach a new NOUN
    # In this case, the first noun is beach....
    # Cat----going, travel, ----beach
    # At this point, Cat may have been replaced as primary object, but we dont know this for sure
    # We need to look for a verb following the first NOUN we see, 
    # If we do not find a verb before the next noun, then CAT, remains the primary object , and is ocnnected to the next noun implicitly
    # In this case, the conjunction, CCONJ 'and' connects the primary noun to the next noun
    
    # So I will try to structure it so that if I see a conjunction before a verb, following a noun, the primary noun stays primary noun, 
    # and the following noun remains tied to the primary noun

    # In this sentence, we see conjunctions following the first and 2nd nouns which follow the primary noun, keeping the primary noun as the 
    # main object relating to the various verbs and nouns that follow

    #So we basically will have a primary object list at all times
    # connect verbs to nouns
    #if primary object is replaced, then previous primary object and its relationships need to enter dictionary to be stored

    #verbs need to be connected from object to object...but in the case of conjunctions like and, verbs need to be extended to the next object 
    # as well





#Structure:
#Start with a main object, its either a prounoun, or a noun that follows a determinant
#This object is then attached to verbs, which are then attached to nouns, ...the nouns because they are attached as subjects to the initial
# object, do not replace the initial object as primary focus, they get stored in a subject list, related to the verbs
# that came before them
# dictionary of dictionaries, for a given sentence

#conjunctions like but will end the sentence 
# and whatever was the primary noun before, assuming it wasnt changed, will still be the primary noun in the following sentence

# The idea is to split a sentence into a few smaller sentences, each with primary nouns, verbs relating to those primary nouns, and nouns 
# relating to those verbs

# Then we also need sort of a finalized idea of what happened, the 'but' can negate all previous imformation
# But we also want computer to be aware and sometimes refer to the things that did not happen
            



    
# print(find_object_importance('i was going to travel to the beach and then zoo'))
# print(find_POS_tuple('the cat was going to travel to the beach and the market, but went to the zoo'))
# print(find_POS_tuple('Today I saw a puppy climbing up a hill'))
find_object_importance_main('I climbed up the tree and then fell onto the ground which was covered in worms')

# find_descriptor_importance('i was going to travel to the beach and the market , but went to the zoo')

#Need parsing function to analyze relative importance of nouns based on some kind of structure, some kind of patterns,    


    






class Chatbot:
    #Class created to initially divide word list into sub categories, to be stored and used by Chatbot
    def __init__(self, word_count):
        self.model = model
        #list of words
        self.words = self.create_words(word_count)
        self.cluster = None
        #List of Lists of ordered clustered words
        self.Ordered_Cluster_List = None
        self.Ordered_Cluster_Count = 0
        self.Reduced_Cluster_List = None
        self.Final_Cluster_List = []
        self.response = None
        self.response_list = None  

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

    def create_word_cluster_list(self, cluster_dict):
        #Returns a list of lists for a cluster dictionary
        vals = set()
        lst = []

        for k,v in cluster_dict.items():
            vals.add(int(v))
        for x in vals:
            lst.append(x)
        srted = sorted(lst)    

        length = len(srted)
        index = 0
        Big_List = []
        while length >0:
            curr_list = []
            for k,v in cluster_dict.items():
                if v == str(srted[index]):
                    curr_list.append(k)
            Big_List.append(curr_list)
            length -=1
            index +=1
        
        if self.Ordered_Cluster_List == None:
            self.Ordered_Cluster_List = Big_List
        return Big_List    

    def recluster(self, list_):
        
        Reclustered_List_ = []
        #This list_ needs to be a list of lists
        
        for x in list_:            
            
            if len(x)<10 and len(x)>=2:
                
                Reclustered_List_.append(x)         
        
            if len(x)>=10:                
                
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

    def recluster_recursive(self, list_):
        if self.Ordered_Cluster_Count == len(self.Ordered_Cluster_List):
                return
        
        for x in list_:
                    
            if len(x)>1 and len(x)<=15:
                
                self.Final_Cluster_List.append(x)
                
                if x in self.Ordered_Cluster_List:
                    self.Ordered_Cluster_Count+=1
            if len(x)>15:
                Reclustered_Dict = Cluster_Labels(x, model)
                Reclustered_List = self.create_word_cluster_list(Reclustered_Dict)
                
                if x in self.Ordered_Cluster_List:
                    self.Ordered_Cluster_Count+=1
                self.recluster_recursive(Reclustered_List)
    
    def find_response_list(self, user_response):
        chatbot_possible_response = []
        user_response = user_response.lower().replace('?', '')
        user_response = user_response.split()
        overall_usable_words = []

        input_dict = find_objects(user_response)
        possible_replications = []
        possible_tenses = ['NOUN', 'PRON', 'DET']
        for k,v in input_dict.items():
            if v in possible_tenses:
                possible_replications.append(k)
        
        for x in user_response:
            for y in self.Final_Cluster_List:
                if x in y and x in possible_replications:
                    overall_usable_words.append(y)
                    
                    similarities_max = 0, None 
                    
                    rand = random.randint(0,10)
                    for z in y:                            
                        
                        if rand <5:                                
                            if z != x:

                                similarity = cosine(x, z, model)
                                if similarity > similarities_max[0]:
                                    similarities_max = similarity, z     
                        elif rand >=5:
                            similarity = cosine(x, z, model)
                            if similarity > similarities_max[0]:
                                similarities_max = similarity, z 
                    chatbot_possible_response.append(similarities_max[1])        
                
                elif x in y and x not in possible_replications:
                    overall_usable_words.append(y)
                    similarities_max = 0, None 
                    for z in y:
                        if z!= x:

                            similarity = cosine(x, z, model)
                            if similarity > similarities_max[0]:
                                similarities_max = similarity, z 


                    chatbot_possible_response.append(similarities_max[1])
        
        chatbot_possible_response = ' '.join(chatbot_possible_response)
        self.response = chatbot_possible_response
        self.response_list = overall_usable_words


#Create idea: teach computer what word in the response is the object, by telling it the object will follow specific
#words, like the, a, an, etc
# Create a function that parses the actual input to first figure out the object, subject, etc
# And treat words differently given their type of speech, importance, etc
#Using NLP for tenses etc...



# chatty = Chatbot(6000)
# chatty.create_cluster()
# chatty.create_word_cluster_list(chatty.cluster)

# chatty.recluster_recursive(chatty.Ordered_Cluster_List)

# chatty.find_response_list('I walked to the park on a Sunday')
# print(chatty.response)
# print(chatty.response_list)






