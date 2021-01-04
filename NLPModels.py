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
               
        # if len(word)>=4 and POS in Acceptable_POS and 'servic' not in word:
        if len(word)>=4 and POS in Acceptable_POS:

            count = 0
            for wrd in Useful_Industry_Words_Stemmed:
                if count ==1:
                    break
                if wrd in word:
                    for i in range(0,1):
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
M = " is one of the computer chip companies, Intel offers platform products that incorporate various components and technologies, including a microprocessor and chipset, a stand-alone SoC, or a multichip package."
N = 'Semiconductors and Related Devices'
O = "engages in the provision of health care services. It operates through the following segments: Pharmacy Services, Retail or Long Term Care, Health Care Benefits, and Corporate. ... The Retail or Long Term Care segment includes selling of prescription drugs and assortment of general merchandise."
P = "RETAIL-DRUG STORES AND PROPRIETARY STORES"
Q = " operates an international chain of membership warehouses, mainly under the 'Costco Wholesale' name, that carry quality, brand-name merchandise at substantially lower prices than are typically found at conventional wholesale or retail sources."
R = "Variety Stores"
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
    Top2 = Similarities[0:3]
    Top2_Scores = []
    Top_Choice = max(x, key=x.get)
    Top_Choices = []
    for y in Top2:
        for k,v in x.items():
            if y == v:
                Top2_Scores.append(v)
                Top_Choices.append(k)
            
    if Top2_Scores[0] > Top2_Scores[1] * (1.1):
        return Top_Choice, Top2_Scores[0]
    else:
        return Top_Choices, Top_Choice, Top2_Scores



Z = " operates as a chain of restaurants. The Company offers sandwiches, wraps, salads, drinks, breads, and other food services. Subway Restaurants serves customers worldwide."            
ZZ = "operates as a technology platform for people and things mobility. The firm offers multi-modal people transportation, restaurant food delivery, and connecting freight carriers and shippers."
YY = "We partner with biopharma companies, care providers, pharmacies, manufacturers, governments and others to deliver the right medicines, medical products and healthcare services to the patients who need them, when they need them — safely and cost-effectively."
AB = " is a holding company. The Company is a provider of telecommunications, media and technology services globally. The Company operates through four segments: Communication segment, WarnerMedia segment, Latin America segment and Xandr segment. ... The Xandr segment provides advertising services."
# print(get_relevant_sentence_desc(I))
AC = "  vehicle builder that makes and sells a range of RVs, from motor homes to travel trailers, as well as related parts. "
List_Codes3 = ["Agriculture, Forestry, Fishing,  Hunting", "Mining, Quarrying,  Oil, Gas Extraction" ,\
        "Utilities", "Construction" , "Manufacturing", "Transportation", "Wholesale Trade", "Retail Sales ",
        "Finance, Insurance, Investments", "Housing, Apartments", "Rental, Leasing",\
            "Health Care", "Arts, Entertainment", "Restaurants, Food",\
                    "Communications" ]



print(get_relevant_sentence_desc(AB))
print(cosine("food", "range", model))
print(find_SEC_branch(AB,List_Codes3,model))   
# print(check_in_list('applesauce', List_Codes2))

       
#Uber --  'Accommodation and Food Services', 



