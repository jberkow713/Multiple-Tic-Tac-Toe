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


# import csv
# import re
# with open("industry_words1.csv") as infile, open("output.csv", "w") as outfile:
#     for line in infile:
#         outfile.write(re.sub(r"\s*,\s*", " ", line))
# Adding Industry Keywords to Files


#Created output.csv, to use to capture all industry key words
df = pd.read_csv("output.csv")
# print(df.head(25))
df_1 = df['MajorField|Keywords']

df[['Field','Subfield']] = df_1.str.split('|', 1, expand=True)
# df = df.loc[df['Field', 'Subfield']]                                 
df = df[['Field','Subfield']]
# print(df.head())
Keywords = []
A = df['Field'].values

for x in A:
    B = tokenize(x)
    if B not in Keywords:
        Keywords.append(B)

Final_Industry_Keywords = []
for lst in Keywords:
    for a in lst:
        if a not in Final_Industry_Keywords:
            Final_Industry_Keywords.append(a)
Final_Useful_Industry_Words_Stemmed = []
for word in Final_Industry_Keywords:
    x = stemmer.stem(word)
    if x not in Final_Useful_Industry_Words_Stemmed:
        Final_Useful_Industry_Words_Stemmed.append(x)
Final_Useful_Industry_Words_Stemmed.remove('and')
Final_Useful_Industry_Words_Stemmed.remove('of')



Keywords2 = []
Final_Industry_Keywords2 = []
B = df['Subfield'].values
for x in B:
    C = tokenize(x)
    if C not in Keywords2:
        Keywords2.append(C)

Final_Industry_Keywords2 = []
for lst in Keywords2:
    for a in lst:
        if a not in Final_Industry_Keywords2:
            Final_Industry_Keywords2.append(a)
Final_Useful_Industry_Words_Stemmed2 = []
for word in Final_Industry_Keywords2:
    x = stemmer.stem(word)
    if x not in Final_Useful_Industry_Words_Stemmed2:
        Final_Useful_Industry_Words_Stemmed2.append(x)
Final_Useful_Industry_Words_Stemmed2.remove('and')
Final_Useful_Industry_Words_Stemmed2.remove('of')
Final_Useful_Industry_Words_Stemmed2.remove('to')
# print(Final_Useful_Industry_Words_Stemmed2)    


#Add these lemmas to the ones below, for full list of industry lemmas


Industry_Words = []
List_Codes = ["Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction" ,\
        "Utilities", "Construction" , "Manufacturing", "Transportation and Warehousing", "Wholesale Trade", "Retail Trade",
        "Information", "Finance and Insurance", "Real Estate and Rental and Leasing",\
            "Professional, Scientific, and Technical Services", "Management of Companies and Enterprises",\
                "Administrative and Support and Waste Management and Remediation Services", "Educational Services",\
                    "Health Care and Social Assistance", "Arts, Entertainment, and Recreation", "Accommodation and Food Services",\
                       "Public Administration", "restaurant" ]
for phrase in List_Codes:
    A = tokenize(phrase)
    Industry_Words.append(A)
Useful_Industry_Words = []
for lst in Industry_Words:
    for word in lst:
        if word not in Useful_Industry_Words:
            Useful_Industry_Words.append(word)
Useful_Industry_Words.remove('and')
Useful_Industry_Words.remove('of')
Useful_Industry_Words.remove('services')
Useful_Industry_Words_Stemmed = []

for word in Useful_Industry_Words:
    x = stemmer.stem(word)
    if x not in Useful_Industry_Words_Stemmed:
        Useful_Industry_Words_Stemmed.append(x)
# print(Useful_Industry_Words_Stemmed)    
# print(Final_Useful_Industry_Words_Stemmed)



#These represent all the Major Field Keywords, Useful_Industry_Words_Stemmed



for word in Final_Useful_Industry_Words_Stemmed:
    if word not in Useful_Industry_Words_Stemmed:
        Useful_Industry_Words_Stemmed.append(word)
for word in Useful_Industry_Words_Stemmed:
    if len(word) <3:
        Useful_Industry_Words_Stemmed.remove(word)


#These represent Subfield Keywords, Useful_Industry_Words_Stemmed2

Useful_Industry_Words_Stemmed2 = []
for word in Final_Useful_Industry_Words_Stemmed2:
    if word not in Useful_Industry_Words_Stemmed2 :
        Useful_Industry_Words_Stemmed2.append(word)
Useful_Industry_Words_Stemmed2 = sorted(Useful_Industry_Words_Stemmed2)
# for x in Useful_Industry_Words_Stemmed:
#     if len(x) <3:
#         Useful_Industry_Words_Stemmed.remove(x)
Useful_Industry_Final_Words2 = []
for x in Useful_Industry_Words_Stemmed2:
    if len(x) >=3:
        Useful_Industry_Final_Words2.append(x)

List_Codes2 = ["Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction" ,\
        "Utilities", "Construction" , "Manufacturing", "Transportation and Warehousing", "Wholesale Trade", "Retail Trade",
        "Information", "Finance and Insurance", "Real Estate and Rental and Leasing",\
            "Professional, Scientific, and Technical Services", "Management of Companies and Enterprises",\
                "Administrative and Support and Waste Management and Remediation Services", "Educational Services",\
                    "Health Care and Social Assistance", "Arts, Entertainment, and Recreation", "Accommodation and Food Services",\
                       "Public Administration" ]



def Avg_sentence_vec(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
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





def get_relevant_sentence_desc(input_str:str):
    '''
    Get relevant words in description, tokenize them and match them using tense, and if they are 
    industry specific words
    Specifically target Industry Keywords that do not appear in classification terms, to minimize bias 
    '''
    nlp = spacy.load("en_core_web_sm")
    input_str = input_str.replace('-', ' ')
    inpt = tokenize(input_str)
    inpt = ' '.join(word for word in inpt) 

    doc = nlp(inpt)
    x = [token.pos_ for token in doc]
    text = inpt.split()
    # text = input_str.split()
    
    Text_Dict = dict(zip(text, x))
    # Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB'] 
    # 'PRON']
    Acceptable_POS = ['NOUN']
    Final_Acceptable_Words = []
    
    #Weighting certain words by adding them double for specific tenses
    for word, POS in Text_Dict.items():

        # Final_Acceptable_Words.append(word)
               
        # if len(word)>=4 and POS in Acceptable_POS and 'servic' not in word:
        if len(word)>=4 and POS in Acceptable_POS:

            count = 0
            for wrd in Useful_Industry_Words_Stemmed:
                if count ==1:
                    break
                if wrd in word:
                    for i in range(0,2):
                        Final_Acceptable_Words.append(word)
                    count +=1
            for wrd in Useful_Industry_Final_Words2:
                if count == 1:
                    break 
                if wrd in word:
                    Final_Acceptable_Words.append(word)
                    count +=1

                    
    sentence = ' '.join(word for word in Final_Acceptable_Words)    

    return(sentence)
def get_relevant_sentence_desc2(input_str:str):
    '''
    Get relevant words in description, tokenize them and match them using tense, and if they are 
    industry specific words
    Specifically target Industry Keywords that do not appear in classification terms, to minimize bias 
    '''
    
    input_str = input_str.replace('-', ' ')
    inpt = tokenize(input_str)
    inpt = ' '.join(word for word in inpt) 

    
    text = inpt.split()
          
   
                    
    sentence = ' '.join(word for word in text)    

    return(sentence)



def Advanced_Avg_sentence_vec_desc(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    sentence = get_relevant_sentence_desc(sentence)
    #Have to turn this list of relevant words into a new string
    
    Vectors = get_w2v(sentence,model)
    Avg_Vector =  np.average(Vectors, axis=0)
    return Avg_Vector

def get_relevant_sentence_industry(input_str:str):

    nlp = spacy.load("en_core_web_sm")
    input_str = input_str.replace('-', ' ')
    inpt = tokenize(input_str)
    inpt = ' '.join(word for word in inpt) 
    
    doc = nlp(inpt)
    x = [token.pos_ for token in doc]
    text = inpt.split()
    # text = input_str.split()
    
    Text_Dict = dict(zip(text, x))
    # Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB', 'PRON' ] 
    # Acceptable_POS = ['NOUN', 'PRON', 'VERB', 'ADJ' ]
    Final_Acceptable_Words = []
    
    #Weighting certain words by adding them double for specific tenses
    for word, POS in Text_Dict.items():
        if len(word)>=3 :
            Final_Acceptable_Words.append(word)
        if word in Useful_Industry_Final_Words2:
            Final_Acceptable_Words.append(word)    
            
                   
                
    sentence = ' '.join(word for word in Final_Acceptable_Words)    

    return(sentence)

def Advanced_Avg_sentence_vec_industry(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    sentence = get_relevant_sentence_industry(sentence)
    #Have to turn this list of relevant words into a new string
    
    Vectors = get_w2v(sentence,model)
    Avg_Vector =  np.average(Vectors, axis=0)
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
# B = "designs, manufactures and markets mobile communication and media devices, personal computers and portable digital music players. The Company sells a range of related software, services, accessories, networking solutions, and third-party digital content and applications"

# C = "world's leading specialist in providing institutional investors with investment servicing, investment management and investment research and trading services"
# D = "general merchandise retailer selling products through its stores and digital channels. The Company's general merchandise stores offer an edited food assortment, including perishables, dry grocery, dairy and frozen items"
# E = 'Department Stores'
# F = 'electronic computers'
# G = 'STATE COMMERCIAL BANKS'
# H = 'retail-variety stores'

# I = "fast food, limited service restaurant with more than 35,000 restaurants in over 100 countries."
# J = "Fast-food restaurant, chain"
# K = "vast Internet-based enterprise that sells books, music, movies, housewares, electronics, toys, and many other goods, either directly or as the middleman between other retailers "
# L = "RETAIL-CATALOG & MAIL-ORDER HOUSES"
# M = " is one of the computer chip companies, Intel offers platform products that incorporate various components and technologies, including a microprocessor and chipset, a stand-alone SoC, or a multichip package."
# N = 'Semiconductors and Related Devices'
# O = "engages in the provision of health care services. It operates through the following segments: Pharmacy Services, Retail or Long Term Care, Health Care Benefits, and Corporate. ... The Retail or Long Term Care segment includes selling of prescription drugs and assortment of general merchandise."
# P = "RETAIL-DRUG STORES AND PROPRIETARY STORES"
# Q = " operates an international chain of membership warehouses, mainly under the 'Costco Wholesale' name, that carry quality, brand-name merchandise at substantially lower prices than are typically found at conventional wholesale or retail sources."
# R = "Variety Stores"
# print(get_relevant_sentence_desc(K))
# print(get_relevant_sentence_industry(L))
# # print(get_relevant_sentence_industry(J))
# print(Advanced_cosine_sentence(K ,L,model))
# print(cosine_sentence(I,J,model))


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

# Sector	Description
# 11	Agriculture, Forestry, Fishing and Hunting
# 21	Mining, Quarrying, and Oil and Gas Extraction
# 22	Utilities
# 23	Construction
# 31-33	Manufacturing
# 42	Wholesale Trade
# 44-45	Retail Trade
# 48-49	Transportation and Warehousing
# 51	Information
# 52	Finance and Insurance
# 53	Real Estate and Rental and Leasing
# 54	Professional, Scientific, and Technical Services
# 55	Management of Companies and Enterprises
# 56	Administrative and Support and Waste Management and Remediation Services
# 61	Educational Services
# 62	Health Care and Social Assistance
# 71	Arts, Entertainment, and Recreation
# 72	Accommodation and Food Services
# 81	Other Services (except Public Administration)
# 92	Public Administration

def find_SEC_branch(company_descript, industry_list, model):
    '''
    Compares company description to List of SEC industry branches, finds and returns top 2 closest matches
    '''
    
    Similarities = []
    for x in industry_list:
        y = Advanced_cosine_sentence(company_descript, x, model)
        Similarities.append(y)
    
    x = dict(zip(industry_list, Similarities))
    Similarities = sorted(Similarities, reverse=True)
    Top5 = Similarities[0:6]
    
    # Top_Choice = max(x, key=x.get)
    # return Top_Choice
    
    Top_Choices = []
    for y in Top5:
        for k,v in x.items():
            if y == v:
                               
                Top_Choices.append(k)
    Final_Dict = dict(zip(Top_Choices, Top5))
    return Final_Dict        
    # if Top2_Scores[0] > Top2_Scores[1] * (1.1):
    #     return Top_Choice, Top2_Scores[0]
    # else:
    #     Final_returned_scores = []
    #     Final_returned_keys = []
    #     for x in Top2_Scores:
    #         if (x / Top2_Scores[0]) >.9:
    #             Final_returned_scores.append(x)
    #             top_dict = dict(zip(Top_Choices, Top2_Scores))
    #             for k,v in top_dict.items():
    #                 for x in Final_returned_scores:
    #                     if x == v:
    #                         if k not in Final_returned_keys:
    #                             Final_returned_keys.append(k)
    #     # return  Top_Choice, Top2_Scores[0], Final_returned_keys
    #     return Final_returned_keys
        # return [Top_Choice]


# Z = " operates as a chain of restaurants. The Company offers sandwiches, wraps, salads, drinks, breads, and other food services. Subway Restaurants serves customers worldwide."            
# ZZ = "operates as a technology platform for people and things mobility. The firm offers multi-modal people transportation, restaurant food delivery, and connecting freight carriers and shippers."
# YY = "We partner with biopharma companies, care providers, pharmacies, manufacturers, governments and others to deliver the right medicines, medical products and healthcare services to the patients who need them, when they need them — safely and cost-effectively."
# AB = " is a holding company. The Company is a provider of telecommunications, media and technology services globally. The Company operates through four segments: Communication segment, WarnerMedia segment, Latin America segment and Xandr segment. ... The Xandr segment provides advertising services."
# # print(get_relevant_sentence_desc(I))
# AC = "  vehicle builder that makes and sells a range of RVs, from motor homes to travel trailers, as well as related parts. "
Industry_Codes = ["Agriculture, Forestry, Fishing,  Hunting", "Mining, Quarrying,  Oil, Gas Extraction" ,\
        "Utilities", "Construction" , "Manufacturing", "Transportation", "Wholesale Trade", "Retail Sales ",
        "Investment ", "Finance, Insurance", "Housing, Apartments", "Rental, Leasing",\
            "Health Care", "Arts, Entertainment", "Restaurants, Food",\
                    "Communications, Technology"]
 
# AD = "We assessed the oral health of the Pine Ridge Oglala Lakota people, described a new oral health assessment tool for Indigenous people, and suggested ways to improve Native oral health."
# AE = 'a technology company. The Company develops, licenses, and supports a range of software products, services and devices.'
# AF = 's an aerospace company, which engages in the manufacture of commercial jetliners and defense, space and security systems. It operates through the following segments: Commercial Airplanes; Defense, Space and Security; Global Services; and Boeing Capital.'
# AG = 'sports broadcasting world. The company is the leading cable sports broadcaster, reaching about 100 million US viewers per month with its stable of channels'
# AH = 'vertically integrated to find, extract and supply oil, natural gas and petroleum. Part of the sixth largest non state-owned energy companies, BP also owns a convenience store chain that is attached to their gas stations'
# print(Useful_Industry_Words_Stemmed)
# print(get_relevant_sentence_desc(AH))
# # print(get_relevant_sentence_desc2(B))
# print(cosine("communications", "systems", model))
# print(find_SEC_branch(AH ,Industry_Codes,model))   
# print(check_in_list('applesauce', List_Codes2))
#ESPN-Arts/Entertainment, Comm/Tech
#Boeing-Manufacturing, Comm/Tech
#State Street, Finance/Insurance
#Bp-Oil, Gas, Extraction / Retail Sales
#        
#Take company and what it invests in, classify all the companies, get an overall classification
#Take researchers and what they do, classify them through their patents and papers,

# Match up companies/Researchers 



#Want to create a program that can take a list of companies that company invests in, 
# get their company descriptions, feed it in to the model, and return the top 3 industries, and their
# percentages 

# In theory, access the edgar forms, and for every one of the companies in a particular companies verticals
# Make a request to google to type in the "company name" + company description

# You take this information, from the request, and you turn it into a variable called A,
#You then throw A into 
# print(find_SEC_branch(A, Industry_Codes, model))

# Only take top result, for each request you receive a [classification]
# And then basically you tally up each classification, and how many, store in dictionary
# Take the top 3 counts and return them/total counts, come up with some kind of classifier


# from CompanyName import get_comp_description_Dict, B

# Comp_Info = get_comp_description_Dict(B)

# Venture_Classification = []
# for x in Comp_Info:
#     xx = find_SEC_branch(x ,Industry_Codes,model)
#     Venture_Classification.append(xx)

# print(Venture_Classification)

#Below is a list of topics, returned through topic modeling

# We want to create a function that finds the mean vector of the given list of words,
#based on the percentages, and then creates a sentence using these words, compares to SEC labels


A = {0: [('galaxies', 0.008033033135050972),
  ('star', 0.007667390799256399),
  ('stars', 0.0071363747871880335),
  ('galaxy', 0.006398559376539289),
  ('stellar', 0.00590602552411055),
  ('luminosity', 0.0041811545512308165),
  ('accretion', 0.00406705561837532),
  ('galactic', 0.004063655247023988),
  ('dust', 0.00398506551885823),
  ('redshift', 0.0038005927547548946)],
 1: [('gauge', 0.00665549309258827),
  ('theory', 0.005724815322517419),
  ('quark', 0.005655274948655314),
  ('mass', 0.004727720588864407),
  ('neutrino', 0.004359592715300164),
  ('gravity', 0.004038671637448339),
  ('theories', 0.003966772867577327),
  ('symmetry', 0.0036889748211034),
  ('supersymmetric', 0.003510064706527295),
  ('decays', 0.003504655620496048)],
 2: [('power', 0.029975451008550112),
  ('load', 0.017878218571160055),
  ('charging', 0.01641773807907874),
  ('microgrid', 0.014865294901497805),
  ('electricity', 0.013517226389844489),
  ('loads', 0.013396071014300558),
  ('bus', 0.013172744438483213),
  ('dispatch', 0.011976215628932191),
  ('voltage', 0.010845902463467009),
  ('microgrids', 0.008950662340487615)],
 3: [('channel', 0.03696932035054989),
  ('decoding', 0.03160578888897981),
  ('codes', 0.02927124699603399),
  ('channels', 0.020848970691399227),
  ('relay', 0.015116246352972018),
  ('rate', 0.012016231070576323),
  ('block', 0.011577822853069552),
  ('decodable', 0.011047436302189021),
  ('source', 0.01067780996760743),
  ('fading', 0.009945501471587187)],
 4: [('authentication', 0.04275510285507988),
  ('iot', 0.03229832025969636),
  ('security', 0.028507433593069037),
  ('privacy', 0.02443183908083926),
  ('wireless', 0.016116545062240674),
  ('service', 0.011963531659393675),
  ('secure', 0.011205191667617555),
  ('protocol', 0.01009286477598365),
  ('sdp', 0.009604488821004861),
  ('protocols', 0.009498615048742153)],
 5: [('channel', 0.022522214142983533),
  ('mimo', 0.019498268661763338),
  ('interference', 0.017705758441225395),
  ('wireless', 0.01747969595448109),
  ('antennas', 0.013269760663337215),
  ('downlink', 0.010809044100844005),
  ('beamforming', 0.010145708815418712),
  ('antenna', 0.009990904493017013),
  ('uplink', 0.008969258304053866),
  ('transmit', 0.007851261685063294)],
 6: [('neurons', 0.03562425110971791),
  ('synaptic', 0.0329266694360079),
  ('spiking', 0.028127469391903307),
  ('spikes', 0.02015479837698916),
  ('neuron', 0.016187457002103094),
  ('firing', 0.012786273965412643),
  ('plasticity', 0.012219957065219077),
  ('nervous', 0.010959663398925124),
  ('synapses', 0.009326855547835211),
  ('neuronal', 0.009302214635533457)],
 7: [('brain', 0.0622238290850548),
  ('neuroimaging', 0.018743291346356727),
  ('resting', 0.015751152143612675),
  ('fmri', 0.014214574704109377),
  ('disorders', 0.013631484615532168),
  ('neuroelectric', 0.0128834587181267),
  ('thalamic', 0.0128834587181267),
  ('healthy', 0.01093507107670872),
  ('schizophrenia', 0.009628708461543048),
  ('functional', 0.00931124348803306)],
 8: [('consensus', 0.03985417775041625),
  ('distributed', 0.03848534698055809),
  ('convergence', 0.024788992974828013),
  ('agent', 0.016073522804783635),
  ('failure', 0.012275883269400411),
  ('agents', 0.01078855130586233),
  ('multi', 0.01011846624320329),
  ('network', 0.009255369862107305),
  ('converge', 0.00880036253914785),
  ('protocol', 0.008644710027184243)],
 9: [('social', 0.027974589925207027),
  ('tweets', 0.02569996915423065),
  ('media', 0.021467748934648038),
  ('twitter', 0.01893681937680153),
  ('embedding', 0.018226100958195397),
  ('sentiment', 0.016790357879280772),
  ('textual', 0.01169390423435208),
  ('posts', 0.010688392341484297),
  ('network', 0.010188271864123426),
  ('embeddings', 0.009832374971658769)],
 10: [('language', 0.024604287297867632),
  ('word', 0.019055035692256056),
  ('embeddings', 0.013505484689028499),
  ('embedding', 0.012267091195072025),
  ('semantic', 0.01212366740413955),
  ('corpus', 0.010784312982212404),
  ('sentence', 0.010104649124082833),
  ('words', 0.00998142950097481),
  ('sentences', 0.007805864702682391),
  ('linguistic', 0.0075421771693835885)]}

Lst_words = []
Percentages = []
for k,v in A.items():
    if k == 6:
        for x in v:
            Lst_words.append(x[0])
            Percentages.append(x[1])
Topic_Dict = dict(zip(Lst_words, Percentages))
sorted_Percentages = sorted(Percentages, reverse=True)
# print(sorted_Percentages)
Words = []
for k,v in Topic_Dict.items():
    if v in sorted_Percentages[0:4]:
        Words.append(k)
        Words.append(k)
    else:
        Words.append(k)
Sentence_0 = ' '.join(Words)
         

def Advanced_Avg_sentence_vec_desc_2(sentence, model):
    '''
    Helper function used to find the average vector for all words in sentence
    Will improve using parts of speech, etc
    '''
    sentence = sentence 
    #Have to turn this list of relevant words into a new string
    
    Vectors = get_w2v(sentence,model)
    if len(Vectors)>0:
        Avg_Vector =  np.average(Vectors, axis=0)
        return Avg_Vector
    else:
        return np.zeros(300)

def Advanced_cosine_sentence_2(v1,v2, model):
    '''
    Finds cosine similarity between 2 sentences
    v1:First input is the company description
    v2:Second input is the industry description, aka SIC Code, etc...
    '''
    v1 = Advanced_Avg_sentence_vec_desc_2(v1, model)
    v2 = Advanced_Avg_sentence_vec_industry(v2, model)

    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

def Cosine_Similarity(v1, v2, model):
    v1 = v1
    v2 = Advanced_Avg_sentence_vec_desc_2(v2, model)

    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0
def Cosine_Similarity_2(v1, v2, model):
    
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0


import time
def find_SEC_branch_2(company_descript, industry_list, model):
    '''
    Compares company description to List of SEC industry branches, finds and returns top 2 closest matches
    '''
    start = time.time()

    

    Similarities = []
    Count = 0
    for x in industry_list:
        # with Pool(4) as p:
        #     y = p.starmap_async(Advanced_cosine_sentence_2(company_descript, x, model), industry_list)
        # with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        #     y = executor.map(Advanced_cosine_sentence_2(company_descript, x, model), industry_list, timeout=1, chunksize=4)
        # # with ThreadPoolExecutor(max_workers=1) as executor:
        # #     future = executor.submit(pow, 323, 1235)
        # #     print(future.result())
        # #     map(func, *iterables, timeout=None, chunksize=1)
        #     # a = y.result()
        #     print(y)
        #     Similarities.append(y)
            
        
        
        
        y = Advanced_cosine_sentence_2(company_descript, x, model)
        print(y)
        Count +=1
        print(Count)
        Similarities.append(y)

    x = dict(zip(industry_list, Similarities))
    Similarities = sorted(Similarities, reverse=True)
    # Top2 = Similarities[0:3]
    # Top2_Scores = []
    Top_Choice = max(x, key=x.get)
    end = time.time()
    for k,v in x.items():
        if Top_Choice == k:
            Highest_Percentage = v
    return Top_Choice, Highest_Percentage, (end - start)

Patent_Labels1 = []
with open('PatentDictwords.json') as f:
  Patents  = json.load(f)

for k,v in Patents.items():
    Patent_Labels1.append(v)




list_of_abstracts = ['A pesticide used to destroy weeds','A physical noise source is used to develop a first sequence of random bits.',\
     'An RNG circuit is connected to the parallel port of a computer. The circuit includes a flat source of white noise and a CMOS amplifier circuit compensated in the high frequency range.']

from sklearn.cluster import KMeans
import numpy as np



def Cluster_Labels(Label_List, model):
    
    list_of_vectors = []
    for x in Label_List:
        vector = Advanced_Avg_sentence_vec_desc_2(x, model)
        vec_to_list = vector.tolist()
        list_of_vectors.append(vec_to_list)
            
    nparray = np.array(list_of_vectors)    
    
    length = len(list_of_vectors)
    clusters = int(math.floor(math.sqrt(length)))
    # print(clusters)

    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(nparray)
    categorized_list = kmeans.labels_
    string_list = []
    for x in categorized_list:
        y = str(x)
        string_list.append(y)

    Categorized_Dict = dict(zip(Label_List, string_list))
    return Categorized_Dict

def Cluster_Label_with_Abstract(Label_list, List_of_Abstracts, model):

    Combined_List = Label_list + List_of_Abstracts

    list_of_vectors = []
    for x in Label_list:
        vector = Advanced_Avg_sentence_vec_desc_2(x, model)
        vec_to_list = vector.tolist()
        list_of_vectors.append(vec_to_list)
    for x in List_of_Abstracts:
        vector = Advanced_Avg_sentence_vec_desc_2(x, model)
        vec_to_list = vector.tolist()
        list_of_vectors.append(vec_to_list)

    nparray = np.array(list_of_vectors)    
    
    length = len(Combined_List)
    clusters = int(math.floor(math.sqrt(length)))
    print(clusters)
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(nparray)
    
    categorized_list = kmeans.labels_
    string_list = []
    for x in categorized_list:
        y = str(x)
        string_list.append(y)

    Categorized_Dict = dict(zip(Combined_List, string_list))
    return Categorized_Dict


def find_possible_label_words(Cluster_Value, Cluster_Dictionary):
    '''
    Takes Cluster Dictionary and specific Cluster value, creates list of possible label words
    for this cluster
    '''
    string_value = str(Cluster_Value)
    category = []
    for k,v in Cluster_Dictionary.items():
        if v == string_value:
            y = tokenize(k)
            for x in y:
                category.append(x)
           
    keys = []
    values = []
    Word_Count = Counter(category)
    for k,v in Word_Count.items():
        if v>2:
            values.append(v)
            keys.append(k)
    keys2 = []
    values2 = []
    if len(keys)<5:
        for k,v in Word_Count.items():
            keys2.append(k)
            values2.append(v)
        Possible_Label_Words = dict(zip(keys2, values2))
        return Possible_Label_Words    

    Possible_Label_Words = dict(zip(keys, values))        
    return Possible_Label_Words


def tokenize_input(LIST):
    words_to_remove = ['in', 'or', 'of', 'for', 'by', 'e.g.', 'a', 'to', 'the', 'and', 'eg', 'an', 'is', 'not',\
        'other', 'than', 'as', 'such', 'means']
    Amended_List = []
    for x in LIST:
        x = x.split(' ')

        for a in x:
            if "-" in a:
                b = a.split('-')
                x.remove(a)
                for c in b:
                    x.append(c)
        x = ' '.join(x)            

        inpt = tokenize(x)

        for y in list(inpt):
            y = y.lower()
            if y in words_to_remove or y.isalpha==False:
                inpt.remove(y)
        
        X = ' '.join(inpt)
        Amended_List.append(X)
    return Amended_List     

def tokenize_input_2(LIST):


    words_to_remove = ['in', 'or', 'of', 'for', 'by', 'e.g.', 'a', 'to', 'the', 'and', 'eg', 'an', 'is','not', \
        'other','than', 'as', 'such', 'means']
    Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB', 'PRON' ] 

    nlp = spacy.load("en_core_web_sm")
    New_List = []
    for x in LIST:

        inpt = x
        inpt = inpt.replace('-', ' ')
        inpt = tokenize(inpt)
        inpt = ' '.join(word for word in inpt)
    
        doc = nlp(inpt)
        x = [token.pos_ for token in doc]
        text = inpt.split()
        
        Text_Dict = dict(zip(text, x))
        
        New_String = ''

        for k,v in Text_Dict.items():
            if v in Acceptable_POS:
                if len(v)>2:
                    New_String+= k + " "
        New_List.append(New_String)




        



    word_check = lambda word: (word not in words_to_remove) or (not word.isalpha)
    splitter = lambda words: tokenize(' '.join([' '.join(word.split('-')) for word in words.lower().split()]))
    ammend_func = lambda description: ' '.join([token for token in splitter(description) if word_check(token)])

    Amended_List = [ammend_func(item) for item in New_List]

    return Amended_List   

# print(tokenize_input_2(Patent_Labels1))




def Words_by_Cluster(Label_List, model):
    '''
    Takes in a list of Patent Labels, Cleans the labels, Clusters them, returns for 
    each cluster a dictionary of the significant words, and their counts
    '''
    Fixed_List = tokenize_input_2(Label_List)
    Clustered_Dictionary = Cluster_Labels(Fixed_List, model)

    clusterlist = []
    for k,v in Clustered_Dictionary.items():
        if int(v) not in clusterlist:
            clusterlist.append(int(v))
    clusterlist = sorted(clusterlist)
    
    important_words = []
    for i in range(len(clusterlist)):
        labels = find_possible_label_words(i, Clustered_Dictionary)
        important_words.append(labels)
    
    Dict_of_Important_Words = dict(zip(clusterlist, important_words))
    
    with open('List_of_Clustered_Words.json', 'w') as fp:
        json.dump(Dict_of_Important_Words, fp)
    
    return Dict_of_Important_Words

# print(Words_by_Cluster(Amended_Patent_Labels, model))



def find_words_by_cluster(Cluster_Dictionary):

    keys = []
    lengths = []
    for k,v in Cluster_Dictionary.items():
        if k not in keys:
            keys.append(k)
    keys2=[]
    for x in keys:
        
        keys2.append(x)
    
    # print(keys)
    for k,v in Cluster_Dictionary.items():
        for x in keys:
            if x == k:
                lengths.append(len(v))
    Words_Per_Cluster = dict(zip(keys, lengths))
    return Words_Per_Cluster, keys

def put_words_in_list(Dictionary):
    List = []
    for k,v in Dictionary.items():
        if type(k) == str:
            List.append(k)
        if type(v) == str:
            List.append(v)
    return List 

from itertools import permutations 
from itertools import combinations

# with open('List_of_Clustered_Words.json') as f:
#     Vector_Dictionary = json.load(f)

# Cluster_Count_Dict = find_words_by_cluster(Vector_Dictionary)   
# print(Cluster_Count_Dict)



def create_possible_labels(Cluster_Dictionary):
    '''
    For given Clustered Dictionary of possible words to use, we return 
    Dictionary of {cluster: [List of all possible terms], cluster:[List of all possible terms], etc...}
    '''

    Cluster_Count_Dict = find_words_by_cluster(Cluster_Dictionary)
    # print(Cluster_Count_Dict)
    List_greater_Than_5 = []
    List_Less_Than_5 = []
    List_Less_Than_5_Counts = []
    Master_List = Cluster_Count_Dict[1]
    
    
    for k,v in Cluster_Count_Dict[0].items():
        
        if v >4:
            List_greater_Than_5.append(k)
        else:
            List_Less_Than_5.append(k)
            List_Less_Than_5_Counts.append(v)
            
    Master_List_Big = []
    for x in Master_List:
        if x in List_greater_Than_5:

            List_of_possible_Labels = []
            
            for k,v in Cluster_Dictionary.items():
                if k == str(x):
                    a = put_words_in_list(v)
                    
                    for i in range(1,4):
                        y = combinations(a,i)
                    
                        y = (' '.join(w) for w in y)
                        y = list(y)
                        for x in y:
                            List_of_possible_Labels.append(x)
            Master_List_Big.append(List_of_possible_Labels)
        
        elif x in List_Less_Than_5:

            Count = List_Less_Than_5_Counts[0]

            List_of_possible_Labels = []
            for k,v in Cluster_Dictionary.items():
                if k == str(x[0]):
                    a = put_words_in_list(v)
                    
                    for i in range(1,Count+1):
                        y = combinations(a,i)
                    
                        y = (' '.join(w) for w in y)
                        y = list(y)
                        for x in y:
                            List_of_possible_Labels.append(x)
            Master_List_Big.append(List_of_possible_Labels)
            del List_Less_Than_5_Counts[0]

    
    Master_Dict = dict(zip(Master_List, Master_List_Big))    

    return Master_Dict
def find_max_cluster_number(Cluster_Dictionary):

    Clusters = []
    
    for v in Cluster_Dictionary.values():
        if v not in Clusters:
            Clusters.append(v)
           
    Cluster_Int = []

    for x in Clusters:
        y = int(x)
        Cluster_Int.append(y)
    
    max_cluster = max(Cluster_Int)
    return max_cluster 

def find_avg_vectors_by_cluster(Cluster_Dictionary, model):
    '''
    Takes in Clustered Dictionary of Labels, and returns ONE average vector for each cluster, ordered
    by the amount of clusters
    '''
    maximum = find_max_cluster_number(Cluster_Dictionary)

    Avg_Vector_List= []

    for i in range(maximum+1):
        a = ''
        string = str(i)
        for k,v in Cluster_Dictionary.items():
            if v == string:
                a += k + " "
        A = Advanced_Avg_sentence_vec_desc_2(a, model)        
        Avg_Vector_List.append(A)
    
    return Avg_Vector_List

def find_length_of_clustered_labels(Labeled_Dictionary):

    keys =[]
    for k,v in Labeled_Dictionary.items():
        if k not in keys:
            keys.append(k)
    lengths = []
    for k,v in Labeled_Dictionary.items():
        for x in keys:
            if x == k:
                lengths.append(len(v))
    return lengths    
def find_best_label_by_cluster(Average_Vector_List, Labeled_Dictionary, cluster_number, model):

    
    Cosine_Similarities = []
    Labels = []
    for k,v in Labeled_Dictionary.items():
        if k == str(cluster_number):
            for x in v:
                cosine_sim = Cosine_Similarity(Average_Vector_List[cluster_number], x, model)
                # print(cosine_sim)
                Cosine_Similarities.append(cosine_sim)
                Labels.append(x)
    Cosine_Dict = dict(zip(Labels, Cosine_Similarities))
    Max = max(Cosine_Dict, key=Cosine_Dict.get)
    return Max






'''
#1)

Patent_Labels = []
with open('Patents_Dict2.json') as f:
  Patents  = json.load(f)

for k,v in Patents.items():
    Patent_Labels.append(v)
#open file and save the labels to a list
     
#2)

Amended_Patent_Labels = tokenize_input(Patent_Labels)
# Create an updated and cleaned list of labels 
#3) 

A = Cluster_Labels(Amended_Patent_Labels, model)
#Map each label to a particular cluster, based on average vector position of that label



with open('Labels_by_Cluster.json', 'w') as fp:
    json.dump(A, fp)
#Save mapping to dictionary    
with open('Labels_by_Cluster.json') as f:
    Labels_by_Cluster = json.load(f)    

B = find_avg_vectors_by_cluster(Labels_by_Cluster, model)       
# We now find the average vector position of each cluster by opening saved dictionary and mapping average
#vector position of each cluster
print(B)

#4)



Clustered = Words_by_Cluster(Amended_Patent_Labels, model)
#Now we find the individual words that make up each cluster, save them to 'list of clustered words'

#5)

with open('List_of_Clustered_Words.json') as f:
    Vector_Dictionary = json.load(f)
#open this file, save to Variable    

Giant_Dict = create_possible_labels(Vector_Dictionary)
# Create a list of all possible labels for the dictionary of clustered words

with open('Possible_Labels.json', 'w') as fp:
    json.dump(Giant_Dict, fp)
#Save this to file
    
#6)

with open('Possible_Labels.json') as f:
    Label_Dictionary = json.load(f)
#Open file of all possible labels for the words from the tokenized list of labels    

lengths = find_length_of_clustered_labels(Label_Dictionary)
print(lengths)
#Finding the lengths of each one of the clusters of labeled words, in the possible labels dictionary
#Lengths represents a list, ordered by cluster, of the total amount of labels in that cluster
#We want to find out which one of the newly created labels, in each cluster, 
# is closest to the average vector of the labels from the original tokenized list, which made up the clusters



#7)
'''

# with open('List_of_Clustered_Words.json') as f:
#     Vector_Dictionary = json.load(f)
  

# Giant_Dict = create_possible_labels(Vector_Dictionary)
# print(Giant_Dict)





import time

Patent_Labels = []
with open('Patents_Dict2.json') as f:
  Patents  = json.load(f)

for k,v in Patents.items():
    Patent_Labels.append(v)
#open file and save the labels to a list
     
#2)
def Create_Labels(Label_List, model):

    Amended_Patent_Labels = tokenize_input_2(Label_List)
    # Create an updated and cleaned list of labels 
    
    Clustered_Labels = Cluster_Labels(Amended_Patent_Labels, model)
    #Map each label to a particular cluster, based on average vector position of that label

    Avg_Vector_List = find_avg_vectors_by_cluster(Clustered_Labels, model)
    #Finding Average Vector for a given cluster of labels

    Words_by_Cluster(Amended_Patent_Labels, model)
    with open('List_of_Clustered_Words.json') as f:
        Vector_Dictionary = json.load(f)
  

    Giant_Dict = create_possible_labels(Vector_Dictionary)
    #Now we find the individual words that make up each cluster, save them to 'list_of_clustered_words'

    
    # Create a list of all possible labels for the dictionary of clustered words

    start = time.time()

    lengths = find_length_of_clustered_labels(Giant_Dict)
    #Finds length of newly created labels for a given cluster
    enum = list(enumerate(lengths))
    print(enum)
    best_labels = []
    Label_lists = []
    for x in enum:
        start2 = time.time()
        Best_Label = find_best_label_by_cluster(Avg_Vector_List, Giant_Dict, x[0], model)
        best_labels.append(Best_Label)
        Label_lists.append(x[0])
        end2 = time.time()
        time_taken = start2 - end2 
        print(f'{time_taken}, {Best_Label}, cluster complete')

    cluster_label_dict = dict(zip(Label_lists, best_labels))

    end = time.time()
    print(end - start)
    print(cluster_label_dict)
    with open('New_Label_List.json', 'w') as fp:
        json.dump(cluster_label_dict,  fp)
    return cluster_label_dict     

print(Create_Labels(Patent_Labels, model))

#For cluster with less than 2000 labels, we return a dictionary of the cluster, and the label
# Otherwise, we need to recluster the labels in lists >2000, find the avg vector position of each cluster,
# Find the cluster with the highest cosine similarity to the original lists avg vector position for that cluster,
# Take the labels from this cluster, and throw into the function   






'''
with open('Possible_Labels.json') as f:
    Label_Dictionary = json.load(f)

Cosine_Similarities = []
Labels = []
for k,v in Label_Dictionary.items():
    if k == '5':
        for x in v:
            cosine_sim = Cosine_Similarity(B[5], x, model)
            # print(cosine_sim)
            Cosine_Similarities.append(cosine_sim)
            Labels.append(x)
Cosine_Dict = dict(zip(Labels, Cosine_Similarities))
Max = max(Cosine_Dict, key=Cosine_Dict.get)
print(Max)
'''
#This label represents a generic label, with closest cosine similarity, to all the labels inside of the
# Original list of clustered labels             







# with open('Possible_Labels.json') as f:
#     Label_Dictionary = json.load(f)

# for k,v in Label_Dictionary.items():
#     if k == '0':
#         A = Cluster_Labels(v, model)
#         print(A)
#         B = find_avg_vectors_by_cluster(A, model)     
#         print(B)


       
# nlp = spacy.load("en_core_web_sm")

# inpt = 'Hello my name is Peter, such that I am a tiger means'
# inpt = tokenize(inpt)
# inpt = ' '.join(word for word in inpt)
# print(inpt) 

# doc = nlp(inpt)
# x = [token.pos_ for token in doc]
# text = inpt.split()
# # text = input_str.split()

# Text_Dict = dict(zip(text, x))
# print(Text_Dict)
# Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB', 'PRON' ] 
# Acceptable_POS = ['NOUN', 'PRON', 'VERB', 'ADJ' ]










  











def Classify_Researcher(List_of_Patents, Patent_Labels, Industry_Labels, model):
    '''
    input: Patent list of abstracts, in the form of strings, List of Patent Labels, List of Industry Labels, and a model
    output: Dictionary: {SEC_Field: Score, SEC_Field: Score, etc...}
    '''
    print(Industry_Labels)
    Amended_Patent_List = tokenize_input(List_of_Patents)
    print(Amended_Patent_List)
    Amended_Label_List = tokenize_input(Patent_Labels) 
    
    Categorized_Dictionary = Cluster_Label_with_Abstract(Amended_Label_List, Amended_Patent_List, model)
    
    #We have now clustered each abstract with all of the patent labels...we can now operate on this
    Classification_List = []
    for x in Amended_Patent_List:
        for k,v in Categorized_Dictionary.items():
            if x == k:
                Classification_List.append(v)
    # print(Classification_List)            
    
    Classification_List2 = []
    index = 0 
    length = len(Classification_List)
    while length >0:

        relevant_labels = []
        
        for k,v in Categorized_Dictionary.items():
            if v == Classification_List[index]:
                if k!= Amended_Patent_List[index]:
                    relevant_labels.append(k)
        
        # print(relevant_labels)
        print(len(relevant_labels))               
        
        x = Amended_Patent_List[index]

        outcome= find_SEC_branch_2(x, relevant_labels, model)
        SEC_Conversion_Dict = find_SEC_branch(outcome[0], Industry_Labels, model)
        Classification_List2.append(SEC_Conversion_Dict)
        
        relevant_labels.clear()
        length -=1
        index +=1


    
    SEC_Tallies = [0] * len(Industry_Labels)
    SEC_Dict = dict(zip(Industry_Labels, SEC_Tallies))

    for x in Classification_List2:
        for k,v in x.items():
            for a, b in SEC_Dict.items():
                if a == k:
                    SEC_Dict[a]+=v

    Final_Sec_Dict = {}
    values = []
    
    for v in SEC_Dict.values():
        values.append(v)
    summed = sum(values)
    for k,v in SEC_Dict.items():
        a = v / summed 
        Final_Sec_Dict[k]=a

    return Final_Sec_Dict 

patent_list = ['mug for drinking stuff', 'gardenhose spigot']
patent_labels = ['kitchenwares', 'gardening']
# # print(Cluster_Label_with_Abstract(patent_labels, patent_list, model))


# print(Classify_Researcher(patent_list, patent_labels, Industry_Codes, model))
Industry_Codes_New = ["Agriculture - Forestry - Fishing -  Hunting", "Mining - Quarrying -  Oil - Gas Extraction" ,\
        "Utilities", "Construction" , "Manufacturing", "Transportation", "Wholesale Trade", "Retail Sales ",
        "Investment ", "Finance - Insurance", "Housing - Apartments", "Rental - Leasing",\
            "Health Care", "Arts - Entertainment", "Restaurants - Food",\
                    "Communications - Technology"]  
a = Patent_Labels1
b = tokenize_input(a)
c = tokenize_input_2(a)

# d = list(enumerate(b))
# e = list(enumerate(c))






# print(Classify_Researcher(list_of_abstracts, a, Industry_Codes, model))
# a = Patent_Labels1
# b = tokenize_input(a)
# c = tokenize_input(b)
# if b == c:
#     print('True')






def find_SEC_branch_3(Single_Label, Patent_Label_List, model):
    '''
    Compares company description to List of SEC industry branches, finds and returns top 2 closest matches
    '''
       

    Similarities = []
    Count = 0
    for x in Patent_Label_List:
       
        
        
        y = Advanced_cosine_sentence_2(Single_Label, x, model)
        print(y)
        Count +=1
        print(Count)
        Similarities.append(y)

    Score_Dict = dict(zip(Patent_Label_List, Similarities))
    # Top2 = Similarities[0:3]
    # Top2_Scores = []
    Related_Keys = []

    for k,v in Score_Dict.items():
        if v>=.70 and k!=Single_Label:
            Related_Keys.append(k)
    return Single_Label, Related_Keys


from sklearn.cluster import KMeans
import numpy as np

def Organize_Sec_Dict(Dict):
  '''
  Takes in SEC Dictionary, returns a Dictionary as follows:
  {Vertical:[[CIK, Company, Investment]], Vertical:[[CIK, Company, Investment], [CIK, Company, Investment], etc], etc}
  Misfiled_Holding_Dictionary: {Misfiled_Company: Investment, Misfiled_Company: Investment, etc}
  '''


  
  Invested_Amount = []
  CIK_Numbers = []
  
  list_of_sec_labels = []
  for k,v in Dict.items():
    if k == "holdings":
      for k,v in v.items():
        if k == "verticals":
          for k,v in v.items():
            list_of_sec_labels.append(k)
        elif k == "misfiledHoldingsAmounts":
          Misfiled_Dict = v     
  Counts = []
  Companies = []
  for k,v in Dict.items():
    if k == "holdings":
      for k,v in v.items():
        if k == "verticals":
          for k,v in v.items():
            for x in list_of_sec_labels:
              if k == x:
                for k,v in v.items():
                  if k == "companies":
                    Counts.append(len(v))
                                  
                    for a,b in v.items():
                      Companies.append(a)
                      for k,v in b.items():
                        if k == 'amountHeld(dollars)':
                          Invested_Amount.append(str(v))
                        if k == 'cik':
                          CIK_Numbers.append(v)  

                      
                      
                      

  Default_Label_List = []
  index = 0
  while index<len(Counts):
    a = Counts[index]
    
    while a > 0:
      Default_Label_List.append(list_of_sec_labels[index])
      a -=1 
    index+=1

  vertical_dict = dict(zip(Companies, Default_Label_List))


  Vertical_List = []  
  for x in Default_Label_List:
    if x not in Vertical_List:
      Vertical_List.append(x)

  Vertical_List_of_Lists = []
  for x in Vertical_List:
    Individ_List = []
    for y in Default_Label_List:
      if y ==x:
        Individ_List.append(y)
    Vertical_List_of_Lists.append(Individ_List)

  List_of_Name_Lists = []
  for x in Vertical_List_of_Lists:
    Name_List = []
    for y in x:
      for k,v in vertical_dict.items():
        if v == y:
          if k not in Name_List:
            Name_List.append(k)
    List_of_Name_Lists.append(Name_List)
  Verticals = []
  for x in Vertical_List_of_Lists:
    for y in x:
      if y not in Verticals:
        Verticals.append(y)
  
  Company_Investment = [', '.join(x) for x in zip(Companies, Invested_Amount)]

  CIK_Dict = dict(zip(CIK_Numbers, Company_Investment))


  CIK_Combined_List = []
  for k,v in CIK_Dict.items():
    combined = []
    combined.append(k)
    combined.append(v)
    CIK_Combined_List.append(combined)

  Final_Final_List = []
  for x in List_of_Name_Lists:
    Final_Combined_List = []
    for y in x:
      
      for a in CIK_Combined_List:
        for b in a:
          if y in b:
            Final_Combined_List.append(a)
    Final_Final_List.append(Final_Combined_List)

  Vertical_Final_Dict = dict(zip(Verticals, Final_Final_List))
  return Vertical_Final_Dict

with open('aak_test.json') as f:
  Berkshire = json.load(f)

def Classify_Investor(SEC_DICT, Industry_Labels, model):

    Organized = Organize_Sec_Dict(SEC_DICT)
    Sectors = []
    Amounts = []
    Amounts_odd = []
    lenlist = []
    for k,v in Organized[0].items():
        Sectors.append(k)
        Sub_Amounts = []
        a = len(v)
        lenlist.append(a)
        for x in v:
            
            for lst in x:
                Sub_Amounts.append(lst)
            
        Amounts.append(Sub_Amounts)

    for x in Amounts:
        a = list(enumerate(x))
        for x in a:
            if x[0] %2 !=0:
                result = x[1].split(',')
                result = result[1].replace(' ', '')
                Amounts_odd.append(result)
                

    #amounts_odd represents all investments
    #lenlist represents how many items in amounts odd to add to smaller list, before moving on to next list
    length = len(lenlist)
    index = 0
    Vertical_Sums_Total = []
    smallindex = 0
    while length >0:
        a = lenlist[index]
        
        Vertical_Sums = []
        
        while a >0:
            
            Vertical_Sums.append(int(Amounts_odd[smallindex]))
            smallindex+=1
            a -=1
        
        Vertical_Sums_Total.append(sum(Vertical_Sums))
        Vertical_Sums.clear()
        length -=1
        index +=1

    Total_Sum = sum(Vertical_Sums_Total)
    Vertical_Percentages = []
    for x in Vertical_Sums_Total:
        y = float(x/Total_Sum)
        Vertical_Percentages.append(y)
    
    len_sectors = len(Sectors)
    index = 0
    Dictionary_List = []
    while len_sectors >0:


        a = Sectors[index]
        y = find_SEC_branch(a, Industry_Labels, model)
        b = Vertical_Percentages[index]

        updated_list = []
        for k,v in y.items():
            c = v*b 
            updated_list.append(c)
        updated_dict = dict(zip(Industry_Labels, updated_list))
        Dictionary_List.append(updated_dict)
        print("One Down, many to go")

        index +=1
        len_sectors -=1



    SEC_Tallies = [0] * len(Industry_Labels)
    SEC_Dict = dict(zip(Industry_Labels, SEC_Tallies))

    for x in Dictionary_List:
        for k,v in x.items():
            for a, b in SEC_Dict.items():
                if a == k:
                    SEC_Dict[a]+=v
    
    Final_Sec_Dict = {}
    values = []
    
    for v in SEC_Dict.values():
        values.append(v)
    summed = sum(values)
    for k,v in SEC_Dict.items():
        a = v / summed 
        Final_Sec_Dict[k]=a

    return Final_Sec_Dict 

with open('sec_yearly_split_13f_response.json') as f:
  Yearly = json.load(f)

def Create_Verticals_and_Amounts(SEC_DICT):
    
    Verticals = []
    Invested_Amounts = []
    for k,v in SEC_DICT.items():
        if k == 'yearly_holdings':
            for k,v in v.items():
                for k,v in v.items():
                    if k == 'verticals':
                        for k,v in v.items():
                            Verticals.append(k)
                            for k,v in v.items():
                                if k == 'totalHoldingsInVertical(dollars)':
                                    Invested_Amounts.append(v)
    return (Verticals, Invested_Amounts)

VERTICALS = Create_Verticals_and_Amounts(Yearly)[0]
INVESTED_AMOUNTS = Create_Verticals_and_Amounts(Yearly)[1]


def Classify_Investor_Updated(Verticals, Invested_Amounts, Industry_Labels, model):

    # Verticals = []
    # Invested_Amounts = []
    # for k,v in SEC_DICT.items():
    #     if k == 'yearly_holdings':
    #         for k,v in v.items():
    #             for k,v in v.items():
    #                 if k == 'verticals':
    #                     for k,v in v.items():
    #                         Verticals.append(k)
    #                         for k,v in v.items():
    #                             if k == 'totalHoldingsInVertical(dollars)':
    #                                 Invested_Amounts.append(v)
    # print(Verticals, len(Verticals),  Invested_Amounts, len(Invested_Amounts))                                
    

    Vertical_Set = set()
    for x in Verticals:
        Vertical_Set.add(x)
    print(len(Vertical_Set))
    print(Vertical_Set)
    Vertical_Tallies = [0] * len(Vertical_Set)
    Vertical_Dict = dict(zip(Vertical_Set, Vertical_Tallies))

    len_sectors = len(Verticals)
    index = 0

    while len_sectors>0:

        a = Verticals[index]
        b = Invested_Amounts[index]

        for k,v in Vertical_Dict.items():
            if k == a:
                
                Vertical_Dict[a] += b
            
        len_sectors -=1
        index +=1

    print(Vertical_Dict)
    Verticals_Updated = []
    Invested_Amounts_Updated = []

    for k,v in Vertical_Dict.items():
        Verticals_Updated.append(k)
        Invested_Amounts_Updated.append(v)  


    len_sectors = len(Verticals_Updated)
    index = 0
    Total = sum(Invested_Amounts_Updated)
    Dictionary_List = []
    while len_sectors >0:


        a = Verticals_Updated[index]
        y = find_SEC_branch(a, Industry_Labels, model)
        b = Invested_Amounts_Updated[index]
        Percentage = b / Total


        updated_list = []
        for k,v in y.items():
            c = v*Percentage
            updated_list.append(c)
        updated_dict = dict(zip(Industry_Labels, updated_list))
        Dictionary_List.append(updated_dict)
        print("One Down, many to go")

        index +=1
        len_sectors -=1



    SEC_Tallies = [0] * len(Industry_Labels)
    SEC_Dict = dict(zip(Industry_Labels, SEC_Tallies))

    for x in Dictionary_List:
        for k,v in x.items():
            for a, b in SEC_Dict.items():
                if a == k:
                    SEC_Dict[a]+=v

    Final_Sec_Dict = {}
    values = []

    for v in SEC_Dict.values():
        values.append(v)
    summed = sum(values)
    for k,v in SEC_Dict.items():
        a = v / summed 
        Final_Sec_Dict[k]=a

    return Final_Sec_Dict
# print(Classify_Investor_Updated(VERTICALS, INVESTED_AMOUNTS, Industry_Codes, model))



# print(Organize_Sec_Dict(Yearly))



# print(Classify_Investor(Berkshire, Industry_Codes, model))



    



       

        

