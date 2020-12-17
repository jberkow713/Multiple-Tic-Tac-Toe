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

List_of_Divisions = ["A: Agriculture, Forestry, Fishing", "B: Mining", "C: Construction", "D: Manufacturing", \
    "E: Transportation, Communcations, Electric, Gas, and Sanitation", "F: Wholesale Trade", \
        "G: Retail Trade", "H: Finance, Insurance, Real Estate", "I: Services", "J: Publc Administration"]

#list of updated dataframes with only SIC Codes and Descriptions
# Need to turn these into dictionary objects with SIC Codes as Keys, descriptions as values
# print(List_of_updated_Dataframes[0])
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

# print(Dict_List)
#Finally works! List of Dictionaries, with SIC Codes as KEYS and Descriptions as Values

Final_Dict = dict(zip(List_of_Divisions, Dict_List))
SIC_Keys = []

for x in Final_Dict.values():
    for y in x.keys():
        SIC_Keys.append(y)
        
def SIC_SEARCH(SIC_CODE:int):
    '''
    Input SIC Code, output is the Main branch of the SEC, along with a detailed description 
    of the business type
    '''
    Descript = []
    if SIC_CODE not in SIC_Keys:
        return "Sorry, not valid key"

    for x in Final_Dict.values():
        for y,z in x.items():
            if y == SIC_CODE:
                Descript.append(z)
    #Once we have description from SIC_CODE input, we find the specific branch it correlates to
    for b,x in Final_Dict.items():
        for k in x.values():
            if Descript[0] == k:
                Descript.insert(0,b)

    return(Descript)            

# print(SIC_SEARCH(7215))

#Now, want to figure out a way to train algorithm to predict what SIC Code and 
# Category a non SIC description Would fall under 
# We have a list of descriptions, lets put that into an actual list

Description_List = []
for x in Final_Dict.values():
    for y in x.values():
        Description_List.append(y)

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
'''
Big_List = []
for y in Description_List:
    A=(tokenize(y))       
    for x in A:
        Big_List.append(x)
#So now we have a list of all the words contained, let's clean it a little bit
# print(Big_List)
Stemmed_List = []
ps = PorterStemmer()  

for x in Big_List:
    ps.stem(x)
    Stemmed_List.append(x)
               
nlp = spacy.load("en_core_web_lg")
STOP_WORDS = nlp.Defaults.stop_words

Final_Big_List = []
for token in Stemmed_List:
    if token not in STOP_WORDS:
        Final_Big_List.append(token)

Word_Counts_Dict = Counter(Final_Big_List)
# print(Word_Counts_Dict)
#Word_Counts_Dict represents a dictionary with all lemmatized, non-stop words, in SIC descriptions and their count
'''

# vect = CountVectorizer()
# vect.fit(SIC_DOC)
# dtm = vect.transform(SIC_DOC)
# # print(vect.get_feature_names())
# dtm2 = pd.DataFrame(dtm.todense(), columns=vect.get_feature_names())

# # row = dtm2.mean(axis=1)
# # print(row.head(20))

# #Create tfidf vectorizer for the SIC_DOC
# tfidf = TfidfVectorizer(stop_words='english', 
#                         ngram_range=(1,1),
#                         max_df=500,
#                         min_df=1,
#                         tokenizer=tokenize,
#                         max_features=5000)

# dtm = tfidf.fit_transform(SIC_DOC)
# dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())

# # dist_matrix  = cosine_similarity(dtm)
# # df = pd.DataFrame(dist_matrix)
# # print(df[df[0] < 1][0].sort_values(ascending=False)[:5])                     

# nn = NearestNeighbors(n_neighbors=1, algorithm='kd_tree')
# nn.fit(dtm)

# # print(nn.kneighbors([dtm.iloc[0].values]))
# #This will match up the specific SIC code with the nearest neighbors vector distances, find most similar SIC code descriptions
# # The idea, is to take a random sample description, run it through the nearest neighbors model, have whatever it finds to be nearest neighbor,
# # Have it then associate that number with the description that exists in our description list. 

# random_description = ["Designs, manufactures and markets mobile communication "]
# random2 = ["creates products and manufactures clothing lines "]
# new = tfidf.transform(random_description)
# A = (nn.kneighbors(new.todense()))
# lists = []
# for x in A:
#     for y in x:
#         for z in y:
#             lists.append(z)

# A = (SIC_DOC[lists[1]])
# A = A.replace('.','')
# # print(A)
# print(A in Description_List)
# print(Final_Dict)


def ADVANCED_SIC_SEARCH(SIC_CODE:int, Description:str):
    '''
    So in this function, we want to be able to enter either an SIC_Code or a description.
    If description is being entered, enter 0 for SIC_CODE 
    '''
    Descript = []
    
    #This runs if there is a company description and not an SIC Code
    if Description:
    # if SIC_CODE not in SIC_Keys:

        Description_List = []
        for x in Final_Dict.values():
            for y in x.values():
                Description_List.append(y)
        
        SIC_DOC = []
        for x in Description_List:
            x = x + "."
        
            SIC_DOC.append(x)
        
        tfidf = TfidfVectorizer(stop_words='english', 
                        ngram_range=(1,1),
                        max_df=500,
                        min_df=1,
                        tokenizer=tokenize,
                        max_features=5000)

        dtm = tfidf.fit_transform(SIC_DOC)
        dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())

        nn = NearestNeighbors(n_neighbors=1, algorithm='kd_tree')
        nn.fit(dtm)

        Description = [Description]
        new = tfidf.transform(Description)
        A = (nn.kneighbors(new.todense()))
        
        lists = []
        for x in A:
            for y in x:
                for z in y:
                    lists.append(z)

        Description_Final = (SIC_DOC[lists[1]])
        Description_Final = Description_Final.replace('.','')
        
        Descript.append(Description_Final)
        
        for b,x in Final_Dict.items():
            for k in x.values():
                if Descript[0] == k:
                    Descript.insert(0,b)

        return(Descript) 

    #This runs if the SIC Code is valid
    for x in Final_Dict.values():
        for y,z in x.items():
            if y == SIC_CODE:
                Descript.append(z)
    #Once we have description from SIC_CODE input, we find the specific branch it correlates to
    for b,x in Final_Dict.items():
        for k in x.values():
            if Descript[0] == k:
                Descript.insert(0,b)

    return(Descript) 



print(ADVANCED_SIC_SEARCH(0, "designs quantum mechanic books to be distributed to public"))



    




















        




