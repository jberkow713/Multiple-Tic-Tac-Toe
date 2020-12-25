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
# print(vec("cow", model))        

def cosine(v1, v2, model):
    #Compares distances between 2 words in terms of cosine similarity 
    v1 = vec(v1, model)
    v2 = vec(v2, model)
    
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

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

def get_relevant_sentence_desc(input_str:str):

    nlp = spacy.load("en_core_web_sm")
    input_str = input_str.replace(',','')
    input_str = input_str.replace('.', '')
    input_str = input_str.replace('-', ' ')
    input_str = input_str.replace('&', 'and')
    inpt = input_str.lower()
    
    doc = nlp(inpt)
    x = [token.pos_ for token in doc]
    text = input_str.split()
    
    Text_Dict = dict(zip(text, x))
    Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB', 'PRON']
    # Acceptable_POS = ['NOUN', 'PRON', 'VERB', 'ADJ' ]
    Acceptable_words = []
    #Weighting certain words by adding them double for specific tenses
    for word, POS in Text_Dict.items():
        #Force words to be 3 letters or greater to count
        if len(word)>=3:
            if "servic" not in word:

                if POS in Acceptable_POS:
                    Acceptable_words.append(word)
                #Count Nouns and Verbs Double in the average by doubling their specific counts
                if POS == 'NOUN':
                    Acceptable_words.append(word)
                if POS == 'VERB':
                    Acceptable_words.append(word)    
            
                
    sentence = ' '.join(word for word in Acceptable_words)    

    return(sentence)

def Advanced_Avg_sentence_vec_desc(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    sentence = get_relevant_sentence_desc(sentence)
    #Have to turn this list of relevant words into a new string
    
    Vectors = get_w2v(sentence,model)
    data = []
    for x in Vectors:
        data.append(x)
    Avg_Vector =  np.average(data, axis=0)
    return Avg_Vector

def get_relevant_sentence_industry(input_str:str):

    nlp = spacy.load("en_core_web_sm")
    input_str = input_str.replace(',','')
    input_str = input_str.replace('.', '')
    input_str = input_str.replace('-', ' ')
    input_str = input_str.replace('&', 'and')
    inpt = input_str.lower()
    
    doc = nlp(inpt)
    x = [token.pos_ for token in doc]
    text = input_str.split()
    
    Text_Dict = dict(zip(text, x))
    Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB', 'PRON']
    # Acceptable_POS = ['NOUN', 'PRON', 'VERB', 'ADJ' ]
    Acceptable_words = []
    #Weighting certain words by adding them double for specific tenses
    for word, POS in Text_Dict.items():
        if POS in Acceptable_POS:
            Acceptable_words.append(word)
        # if POS == 'NOUN':
        #     Acceptable_words.append(word)
        # if POS == 'VERB':
        #     Acceptable_words.append(word)    
            
                
    sentence = ' '.join(word for word in Acceptable_words)    

    return(sentence)
def Advanced_Avg_sentence_vec_industry(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    sentence = get_relevant_sentence_industry(sentence)
    #Have to turn this list of relevant words into a new string
    
    Vectors = get_w2v(sentence,model)
    data = []
    for x in Vectors:
        data.append(x)
    Avg_Vector =  np.average(data, axis=0)
    return Avg_Vector

def Advanced_cosine_sentence(v1,v2, model):
    '''
    Finds cosine similarity between 2 sentences
    v1:First input is the company description
    v2:Second input is the industry description, aka SIC Code, etc...
    '''
    v1 = Advanced_Avg_sentence_vec_desc(v1, model)
    v2 = Advanced_Avg_sentence_vec_industry(v2, model)

    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0


A = "engages in retail and wholesale business. The Company offers an assortment of merchandise and services at everyday low prices. ... The Walmart International segment manages supercenters, supermarkets, hypermarkets, warehouse clubs, and cash & carry outside of the United States."
B = "designs, manufactures and markets mobile communication and media devices, personal computers and portable digital music players. The Company sells a range of related software, services, accessories, networking solutions, and third-party digital content and applications"

C = "world's leading specialist in providing institutional investors with investment servicing, investment management and investment research and trading services"
D = "general merchandise retailer selling products through its stores and digital channels. The Company's general merchandise stores offer an edited food assortment, including perishables, dry grocery, dairy and frozen items"
E = 'Department Stores'
F = 'electronic computers'
G = 'STATE COMMERCIAL BANKS'
H = 'retail-variety stores'

I = "fast food, limited service restaurant with more than 35,000 restaurants in over 100 countries."
J = "Fast-food restaurant, chain"
K = "vast Internet-based enterprise that sells books, music, movies, housewares, electronics, toys, and many other goods, either directly or as the middleman between other retailers "
L = "RETAIL-CATALOG & MAIL-ORDER HOUSES"
#Apple, industry
# print(Advanced_cosine_sentence(B, F, model))
# print(cosine_sentence(B,F, model))
# print(get_relevant_sentence_desc(B))
# print(get_relevant_sentence_industry(F))

# #Target, industry
# print(Advanced_cosine_sentence(D, H, model))
# print(cosine_sentence(D,H, model))
# print(get_relevant_sentence_desc(D))
# print(get_relevant_sentence_industry(H))

# #Mcdonalds, industry
# print(Advanced_cosine_sentence(I, J, model))
# print(cosine_sentence(I,J, model))
# print(get_relevant_sentence_desc(I))
# print(get_relevant_sentence_industry(J))


#Advanced model seems like it has more potential
#Next step is to integrate it with SIC codes, compare it's code to ALL SIC codes, and have it return one with 
# highest cosine similarity 
# But we dont need to check within all the branches,
# We can run the description first against all the major SIC division keywords, and return the top 1 or 2, then just run the code
# Against all of the descriptions within those individual branches, to cut down on time tremendously

#This is a list of main branch descriptions:
# We can run Advanced Cosine Similarity to check for specific industry
'''
0100-0999 "A: Agriculture, Forestry, Fishing"
1000-1499 "B: Mining"
1500-1799 "C: Construction"
1800-1999 not used
2000-3999 "D: Manufacturing"
4000-4999 "E: Transportation, Communcations, Electric, Gas, and Sanitation"
5000-5199 "F: Wholesale Trade"
5200-5999 "G: Retail Trade"
6000-6799 "H: Finance, Insurance, Real Estate"
7000-8999 "I: Services"
9100-9729 "J: Public Administration"
'''
def find_SEC_branch(company_descript, model):
    '''
    Compares company description to List of SEC industry branches, finds and returns top 2 closest matches
    '''
    
    List_Codes = ["Agriculture, Forestry, Fishing", "Mining" ,"Construction" , "Manufacturing",\
        "Transportation, Communcations, Electric, Gas, and Sanitation", "Wholesale Trade", "Retail Trade",\
            "Finance, Insurance, Real Estate", "Services","Public Administration"]

    Similarities = []
    for x in List_Codes:
        y = Advanced_cosine_sentence(company_descript, x, model)
        Similarities.append(y)
    
    x = dict(zip(List_Codes, Similarities))
    Top_2 = []
    Similarity = sorted(Similarities, reverse=True)
    Top_2.append(Similarity[0])
    Top_2.append(Similarity[1])

    Relevant_Industries = []
    for y in Top_2:
        for k, v in x.items():
            if y == v:
                Relevant_Industries.append(k)

            

    # best_topic = max(x, key=x.get)
    return(Relevant_Industries)

# print(get_relevant_sentence_desc(K))
# print(find_SEC_branch(K, model))
# print(Advanced_cosine_sentence(K, L, model))
# print(cosine_sentence(K,L, model))
#Mcdonalds matched up to retail Trade: Correct
#State Street matched up to Finance, Insurance, Real Estate: Correct
#Apple matched up with Services: Correct
#Amazon:Correct
#Best Buy: Incorrect

#Next step, if necessary, run the description against ALL descriptions within the top 2 branches chosen from the model



DF = pd.read_csv("https://raw.githubusercontent.com/saintsjd/sic4-list/master/sic-codes.csv")

#Column names = Division, Major Group, Industry Group, SIC, Description

df0 = DF.loc[DF['Division']=='A']
df1 = DF.loc[DF['Division']=='B']
df2 = DF.loc[DF['Division']=='C']
df3 = DF[DF['Division'] == "D"]
df4 = DF[DF['Division'] == "E"]
df5 = DF[DF['Division'] == "F"]
df6 = DF[DF['Division'] == "G"]
df7 = DF[DF['Division'] == "H"]
df8 = DF[DF['Division'] == "I"]
df9 = DF[DF['Division'] == "J"]
List_of_Dataframes = [df0, df1, df2, df3, df4, df5, df6, df7, df8, df9]

List_of_updated_Dataframes = []
for x in List_of_Dataframes:
    x = x.drop(['Division', 'Major Group', 'Industry Group'], axis=1)
    List_of_updated_Dataframes.append(x)

'''
#Following are the keys in the dictionary:
# Values will be nested dictionaries, of all SIC Codes in that range as keys: Their description as Values
0100-0999 "A: Agriculture, Forestry, Fishing"
1000-1499 "B: Mining"
1500-1799 "C: Construction"
1800-1999 not used
2000-3999 "D: Manufacturing"
4000-4999 "E: Transportation, Communcations, Electric, Gas, and Sanitation"
5000-5199 "F: Wholesale Trade"
5200-5999 "G: Retail Trade"
6000-6799 "H: Finance, Insurance, Real Estate"
7000-8999 "I: Services"
9100-9729 "J: Publc Administration"
'''


List_Codes = ["Agriculture, Forestry, Fishing", "Mining" ,"Construction" , "Manufacturing",\
        "Transportation, Communcations, Electric, Gas, and Sanitation", "Wholesale Trade", "Retail Trade",\
            "Finance, Insurance, Real Estate", "Services","Public Administration"]


List_of_Divisions = ["A: Agriculture, Forestry, Fishing", "B: Mining", "C: Construction", "D: Manufacturing", \
    "E: Transportation, Communcations, Electric, Gas, and Sanitation", "F: Wholesale Trade", \
        "G: Retail Trade", "H: Finance, Insurance, Real Estate", "I: Services", "J: Publc Administration"]


SIC = []
Desc = []
Dict_List = []
Len_List = len(List_of_updated_Dataframes)
index = 0
Copied_List = []
while Len_List > 0:
    x = List_of_updated_Dataframes[index].copy()
    x['SIC'] = (x['SIC']).astype(int)
    A = x['SIC'].values
    for y in A:
        SIC.append(y)
        
    B = x['Description'].values
    for z in B:
        Desc.append(z)
    Dict = dict(zip(SIC, Desc))
    
    Dict_List.append(Dict)
    SIC.clear()
    Desc.clear()
    Len_List -=1
    index +=1

#MAIN DICTIONARY
Final_Dict = dict(zip(List_of_Divisions, Dict_List))

#LIST OF ALL SIC CODES
SIC_Keys = []
# print(Final_Dict)
for x in Final_Dict.values():
    for y in x.keys():
        SIC_Keys.append(y)

#LIST OF ALL DESCRIPTIONS IN SEC BRANCHES
Description_List = []
for x in Final_Dict.values():
    for y in x.values():
        Description_List.append(y)

SEC_MAIN_BRANCH_DICT = dict(zip(List_Codes, List_of_Divisions))

def Find_Relevant_Industry_Descriptions(company_descript, model):

    Relevant_Branches = find_SEC_branch(company_descript, model)
    Main_Branch_list = []
    for x in Relevant_Branches:
        for k,v in SEC_MAIN_BRANCH_DICT.items():
            if x == k:
                Main_Branch_list.append(v)
    #Main Branch Represents Branches of Descriptions to parse to compare to company_description
    Narrowed_Descriptions = []
    for x in Main_Branch_list:
        for y,z in Final_Dict.items():
            if x == y:
                for a in z.values():
                    Narrowed_Descriptions.append(a)
    return Narrowed_Descriptions


#We take old description list, filter it down so that terms are in our actual word vector dictionary

New_Description_list = []
for word in Description_List:
    A = get_w2v2(word,model)
    if A != 0:
        New_Description_list.append(word)

#Description.npy is avg_vectors of individual descriptions in New_Description_list
wv = np.load('Description.npy')
print(wv[10])

#New_Dict represents the "model" to compare company descriptions to once we have a company description
New_Dict = dict(zip(New_Description_list, wv))

def Advanced_cosine_sentence_2(v1,v2, model):
    '''
    Finds cosine similarity between 2 sentences
    v1:First input is the company description
    v2:Second input is the industry description, aka SIC Code, etc...
    model1: main model of all words
    model2: newly created model of only descriptions from SEC list
    '''
    v1 = Advanced_Avg_sentence_vec_desc(v1, model)
    v2 = v2 
    
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

#C = state street, so let's try it out
comparison_list = []
for x, y in New_Dict.items():
    A = Advanced_cosine_sentence_2(C, y, model)
    comparison_list.append(A)
print(comparison_list)    















