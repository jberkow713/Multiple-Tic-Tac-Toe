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

for word in Final_Useful_Industry_Words_Stemmed:
    if word not in Useful_Industry_Words_Stemmed:
        Useful_Industry_Words_Stemmed.append(word)
#We now have a list of key words to reflect the INDUSTRY, 
#These words will be given extra weight if found in a company description
for word in Final_Useful_Industry_Words_Stemmed2:
    if word not in Useful_Industry_Words_Stemmed:
        Useful_Industry_Words_Stemmed.append(word)
Useful_Industry_Words_Stemmed = sorted(Useful_Industry_Words_Stemmed)
# for x in Useful_Industry_Words_Stemmed:
#     if len(x) <3:
#         Useful_Industry_Words_Stemmed.remove(x)
Useful_Industry_Final_Words = []
for x in Useful_Industry_Words_Stemmed:
    if len(x) >=3:
        Useful_Industry_Final_Words.append(x)


# print((Useful_Industry_Final_Words[0:5]))        

#Now want to find key words in specific branches, add these to this list as well
 





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

def get_relevant_sentence_desc(input_str:str):
    '''
    Get relevant words in description, tokenize them and match them using tense, and if they are 
    industry specific words
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
    Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB'] 
    # 'PRON']
    Acceptable_POS = ['NOUN', 'PRON', 'VERB', 'ADJ' ]
    Acceptable_words = []
    Tenses = []
    #Weighting certain words by adding them double for specific tenses
    for word, POS in Text_Dict.items():
        #Force words to be 3 letters or greater to count
        if len(word)>=4:
            if "servic" not in word :

                if POS in Acceptable_POS:
                    for wrd in Useful_Industry_Final_Words:
                        if wrd in word:
     

                            Acceptable_words.append(word)
                            Tenses.append(POS)
                
                           
                    # else:
                    #     Acceptable_words.append(word)
                    #     if POS == 'NOUN':
                    #         Acceptable_words.append(word)
                    #     Tenses.append(POS)
                                     

                    
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
    Acceptable_POS = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB'] 
    # Acceptable_POS = ['NOUN', 'PRON', 'VERB', 'ADJ' ]
    Acceptable_words = []
    
    #Weighting certain words by adding them double for specific tenses
    for word, POS in Text_Dict.items():
        if POS in Acceptable_POS:
            Acceptable_words.append(word)

            for wrd in Useful_Industry_Final_Words:
                if wrd in word:
                    Acceptable_words.append(word)    

            
            
                
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
# C = 'state commercial banks'

# print(get_relevant_sentence_industry(G))
print(get_relevant_sentence_desc(I))
print(get_relevant_sentence_industry(J))
print(Advanced_cosine_sentence(I,J,model))
print(cosine_sentence(I,J,model))


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






def find_SEC_branch(company_descript, model):
    '''
    Compares company description to List of SEC industry branches, finds and returns top 2 closest matches
    '''
    List_Codes = ["Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction" ,\
        "Utilities", "Construction" , "Manufacturing", "Transportation and Warehousing", "Wholesale Trade", "Retail Trade",
        "Information", "Finance and Insurance", "Real Estate and Rental and Leasing",\
            "Professional, Scientific, and Technical Services", "Management of Companies and Enterprises",\
                "Administrative and Support and Waste Management and Remediation Services", "Educational Services",\
                    "Health Care and Social Assistance", "Arts, Entertainment, and Recreation", "Accommodation and Food Services",\
                       "Public Administration" ]

    Similarities = []
    for x in List_Codes:
        y = Advanced_cosine_sentence(company_descript, x, model)
        Similarities.append(y)
    
    x = dict(zip(List_Codes, Similarities))
    Similarities = sorted(Similarities, reverse=True)
    Top2 = Similarities[0:2]
    Top2_Scores = []
    Top_Choice = max(x, key=x.get)
    Top_Choices = []
    for y in Top2:
        for k,v in x.items():
            if y == v:
                Top2_Scores.append(v)
                Top_Choices.append(k)  
    return Top_Choices, Top_Choice, Top2_Scores




# DF = pd.read_csv("https://raw.githubusercontent.com/saintsjd/sic4-list/master/sic-codes.csv")

# #Column names = Division, Major Group, Industry Group, SIC, Description

# df0 = DF.loc[DF['Division']=='A']
# df1 = DF.loc[DF['Division']=='B']
# df2 = DF.loc[DF['Division']=='C']
# df3 = DF[DF['Division'] == "D"]
# df4 = DF[DF['Division'] == "E"]
# df5 = DF[DF['Division'] == "F"]
# df6 = DF[DF['Division'] == "G"]
# df7 = DF[DF['Division'] == "H"]
# df8 = DF[DF['Division'] == "I"]
# df9 = DF[DF['Division'] == "J"]
# List_of_Dataframes = [df0, df1, df2, df3, df4, df5, df6, df7, df8, df9]

# List_of_updated_Dataframes = []
# for x in List_of_Dataframes:
#     x = x.drop(['Division', 'Major Group', 'Industry Group'], axis=1)
#     List_of_updated_Dataframes.append(x)

# '''
# #Following are the keys in the dictionary:
# # Values will be nested dictionaries, of all SIC Codes in that range as keys: Their description as Values
# 0100-0999 "A: Agriculture, Forestry, Fishing"
# 1000-1499 "B: Mining"
# 1500-1799 "C: Construction"
# 1800-1999 not used
# 2000-3999 "D: Manufacturing"
# 4000-4999 "E: Transportation, Communcations, Electric, Gas, and Sanitation"
# 5000-5199 "F: Wholesale Trade"
# 5200-5999 "G: Retail Trade"
# 6000-6799 "H: Finance, Insurance, Real Estate"
# 7000-8999 "I: Services"
# 9100-9729 "J: Publc Administration"
# '''


# List_Codes = ["Agriculture, Forestry, Fishing", "Mining" ,"Construction" , "Manufacturing",\
#         "Transportation, Communcations, Electric, Gas, and Sanitation", "Wholesale Trade", "Retail Trade",\
#             "Finance, Insurance, Real Estate", "Services","Public Administration"]


# List_of_Divisions = ["A: Agriculture, Forestry, Fishing", "B: Mining", "C: Construction", "D: Manufacturing", \
#     "E: Transportation, Communcations, Electric, Gas, and Sanitation", "F: Wholesale Trade", \
#         "G: Retail Trade", "H: Finance, Insurance, Real Estate", "I: Services", "J: Publc Administration"]

# SIC = []
# Desc = []
# Dict_List = []
# Len_List = len(List_of_updated_Dataframes)
# index = 0
# Copied_List = []
# while Len_List > 0:
#     x = List_of_updated_Dataframes[index].copy()
#     x['SIC'] = (x['SIC']).astype(int)
#     A = x['SIC'].values
#     for y in A:
#         SIC.append(y)
        
#     B = x['Description'].values
#     for z in B:
#         Desc.append(z)
#     Dict = dict(zip(SIC, Desc))
    
#     Dict_List.append(Dict)
#     SIC.clear()
#     Desc.clear()
#     Len_List -=1
#     index +=1
# Final_Dict = dict(zip(List_of_Divisions, Dict_List))


# SEC_MAIN_BRANCH_DICT = dict(zip(List_Codes, List_of_Divisions))

# def Find_Relevant_Industry_Descriptions(company_descript, model):

#     Relevant_Branches = find_SEC_branch(company_descript, model)
#     Main_Branch_list = []
#     for k,v in SEC_MAIN_BRANCH_DICT.items():
#         if Relevant_Branches == k:
#             Main_Branch_list.append(v)
#     Main_Branch_list = Main_Branch_list[0]        
#     #Main Branch Represents Branches of Descriptions to parse to compare to company_description
#     Narrowed_Descriptions = []
#     for y,z in Final_Dict.items():
#         if Main_Branch_list == y:
#             for a in z.values():
#                 Narrowed_Descriptions.append(a)
#     return Narrowed_Descriptions

# # print(Find_Relevant_Industry_Descriptions(I,model))


# #Description.npy is avg_vectors of individual descriptions in New_Description_list
# wv = np.load('Description.npy')
# with open('Description_list.json') as f:
#     Description_list = json.load(f)

# #New_Dict represents the "model" to compare company descriptions to once we have a company description
# New_Dict = dict(zip(Description_list, wv))




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

def Most_Relevant_Description(comp_descript, model):
    '''
    This will take a random company description's top matched SEC industry branch
    Check the relevant Descriptions within this branch, and return the description
    With highest cosine similarity between the company description, and the SEC descriptions
    '''
        
    Relevant_Descriptions = Find_Relevant_Industry_Descriptions(comp_descript, model)
    Descript_to_check = []
    for x in Relevant_Descriptions:
        if x in Description_list:
            Descript_to_check.append(x)
    
    Scores = []
    for x in Descript_to_check:
        for k,v in New_Dict.items():
            if x == k:
                B = Advanced_cosine_sentence_2(comp_descript, v, model)
                Scores.append(B)
   
    Score_Dict = dict(zip(Descript_to_check, Scores))
    Top_Scores = sorted(Scores, reverse=True)
    # best_topic = max(Score_Dict, key=Score_Dict.get)
    Top_Descriptions = []
    for x in Top_Scores[0:3]:
        for k,v in Score_Dict.items():
            if x == v:
                Top_Descriptions.append(k)
    return Top_Descriptions 

Z = " operates as a chain of restaurants. The Company offers sandwiches, wraps, salads, drinks, breads, and other food services. Subway Restaurants serves customers worldwide."            
ZZ = "operates as a technology platform for people and things mobility. The firm offers multi-modal people transportation, restaurant food delivery, and connecting freight carriers and shippers."

print(find_SEC_branch(D,model))   

#Uber --  'Accommodation and Food Services', 



