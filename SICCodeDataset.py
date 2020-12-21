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
import numpy as np
import re
import numpy as np
import pandas as pd
from pprint import pprint
import json 
import math





import spacy


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
# print(Final_Dict)
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

Big_List = []
for y in Description_List:
    A=(tokenize(y))       
    for x in A:
        Big_List.append(x)
# So now we have a list of all the words contained, let's clean it a little bit

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
        if token not in Final_Big_List:
            Final_Big_List.append(token)
# print(Final_Big_List)            

#Final Big_List represents all the words in our Description List, tokenized and everything

def get_word_vectors(words):
    # converts a list of words into their word vectors
    return [nlp(word).vector for word in words]

#We then apply this vectorization function to the list of words in our Description list from the SIC Descriptions
    
# pca = PCA(n_components=3)
# pca.fit(get_word_vectors(Description_List))
# new_word_vecs_3d = pca.transform(get_word_vectors(Description_List))
# New_Three_D_List = []
# for x in new_word_vecs_3d:
#     New_Three_D_List.append(x.tolist())
# print(New_Three_D_List)
# Full_Description_Dict =  dict(zip(Description_List, New_Three_D_List))

# with open('Full_Description_Vect_Dict.json', 'w') as fp:
#     json.dump(Full_Description_Dict, fp) 

# # Saving the dictionary to Json File
# Vect_Dict = dict(zip(Final_Big_List, Three_D_List))


# with open('Vect_Dict.json', 'w') as fp:
#     json.dump(Vect_Dict, fp)


#Vect_Dict is now a .json file with descriptions as keys, and 2d coordinate vectors as values
# We can operate on it
# 
#     


def Avg_Vector_Coordinate(Company_Description:str):
    '''
    This function takes in a string description, if words are in Vector Dictionary, converts their position to vectors, and takes
    Average of the x, and y coordinates, returns array
    '''
    with open('Vect_Dict.json') as f:
        Vector_Dictionary = json.load(f)
    A = tokenize(Company_Description)
    
    x_coord = 0
    y_coord = 0
    z_coord = 0
    count = 0
    for x in A:
        for word, vector in Vector_Dictionary.items():
            if x == word:
                x_coord += vector[0]
                y_coord += vector[1]
                z_coord += vector[2]
                count +=1
    Final_X_Coord = x_coord / count
    Final_Y_coord = y_coord /count 
    Final_Z_coord = z_coord /count 
    Position = []
    Position.append(Final_X_Coord)
    Position.append(Final_Y_coord)
    Position.append(Final_Z_coord)

    return(Position)

# print(Avg_Vector_Coordinate("sells computers"))
# Coordinate_Description_List = []
# for x in Description_List:
#     Coordinates = Avg_Vector_Coordinate(x)
#     Coordinate_Description_List.append(Coordinates)

# Vect_Dict_Description_List = dict(zip(Description_List, Coordinate_Description_List))
# with open('SIC_Description_Dict.json', 'w') as fp:
#     json.dump(Vect_Dict_Description_List, fp)


#We now have a Vector_Dict_Description_list with a 2d average vector position for EACH description, 
# We want to take a description, run it through the Avg_Vector_coordinate function,
# and take that 2d array, and find which of the keys in the SIC_Description_Dict, it is closest to in space
# by comparing values, euclidean distance, then return the key
#First, let's make helper function for finding distance between description list vectors and actual
# Company description vector



# def Euclidean_distance(Point_A, Point_B):


def Find_Minimum_Distance_Description(Company_Description:str):
    '''
    Point A = [x, y] type list,
    '''
    with open('SIC_Description_Dict.json') as f:
        Description_Vector_Dictionary = json.load(f)
    # Distance_list = []
    # for Description, Coordinate in Description_Vector_Dictionary.items():
    #     Distance_list.append(Coordinate)
    # print(Distance_list)

    Distance_list = []
    Coordinate_list = []
    Point_A = Avg_Vector_Coordinate(Company_Description)

    for Description, Coordinate in Description_Vector_Dictionary.items():
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(Point_A, Coordinate)]))
        Coordinate_list.append(Coordinate)
        Distance_list.append(distance)
    #Dictionary for reference later, of coordinates and their distances to the point
    #Had to convert to tuples
    tuple_list = tuple(tuple(x) for x in Coordinate_list)
    Point_to_Point_Dict = dict(zip(tuple_list, Distance_list))

    sorted_list = sorted(Distance_list)
    Closest = (sorted_list[0])
    #Closest is a value in the Point_to_Point_Dict
    Coord_needed = []
    for coordinate, distance in Point_to_Point_Dict.items():
        if Closest == distance:
            Coord_needed.append(coordinate)
    #Now that we have coordinate of closest point, go back to SIC_Desc_Dictionary, and match up 
    # With actual description
    SIC_Description_Coord = list(Coord_needed[0])

    Closest_Description = []
    for Description, Coordinate in Description_Vector_Dictionary.items():
        if SIC_Description_Coord == Coordinate:
            Closest_Description.append(Description)
    return Closest_Description[0]
            

#A great first step, will need more data and experimentation to make it more accurate

def ADVANCED_SIC_SEARCH(SIC_CODE):
    '''
    Args: Enter either an SIC_Code or a description.
    If a string is entered, function will assume it is a company description 
    If integer is entered, function will assume you are entering SIC Code
    Output: [General Classification, Detailed Description of Business]
    '''
    Descript = []
    #If description of business entered
    if isinstance(SIC_CODE, str) is True:
        
        Description_List = []
        for x in Final_Dict.values():
            for y in x.values():
                Description_List.append(y)
        
        SIC_DOC = []
        for x in Description_List:
            x = x + "."
        
            SIC_DOC.append(x)
        
        tfidf = TfidfVectorizer(stop_words='english', 
                        ngram_range=(1,5),
                        max_df=50,
                        min_df=1,
                        tokenizer=tokenize,
                        max_features=None)

        dtm = tfidf.fit_transform(SIC_DOC)
        dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())

        nn = NearestNeighbors(n_neighbors=1, algorithm='kd_tree')
        nn.fit(dtm)

        SIC_CODE = [SIC_CODE]
        new = tfidf.transform(SIC_CODE)
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
    #If SIC Code entered
    if isinstance(SIC_CODE, int) is True:
    
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

print(Find_Minimum_Distance_Description(" rents movies to local consumers "))
print(ADVANCED_SIC_SEARCH(" rents movies to local consumers "))
# print(SIC_SEARCH(112))
# print(Description_List)



