import numpy as np
import spacy
import gensim
from gensim.models import CoherenceModel, LdaModel, HdpModel, LsiModel
from gensim.corpora import Dictionary
import pyLDAvis.gensim
import os, re, operator, warnings
import json

np.random.seed(57)

warnings.filterwarnings('ignore')
nlp = spacy.load('en_core_web_sm')
stopwords = nlp.Defaults.stop_words
# add words to stopwords
my_stopwords = [u'patient', u'history', u'note', u'pain', u'family',\
    u'report', u'normal', u'deny', u'give', u'prior']

for word in my_stopwords:
    lexeme = nlp.vocab[word]
    lexeme.is_stop = True

# Open files with Conditions and Symptoms Text, store in Variables
f = open('Conditions.json')
Conditions = json.load(f)
g = open('Symptoms.json')
Symptoms = json.load(g)

# Create function to parse this text and return joined strings of text
def parse_list(List):
    return [' '.join(x) for x in List]
def num_check(s):
  return any(i.isdigit() for i in s)

def clean_text(text, tenses, Length):
    # Cleans a string of text, based on allowable tenses, and min_length of a word
    new = re.sub('[^A-Za-z0-9]+', ' ', text)
    New = [x.lower() for x in new.split() if num_check(x)==False]
    # NLP objects for the cleaned text
    doc = nlp(' '.join(New))
    cleaned = [x.lemma_ for x in doc if x.is_stop==False and x.pos_ in tenses and len(x)>Length]
    return cleaned    

Tenses = ['NOUN', 'VERB', 'ADJ', 'ADV']

def return_text(List, tenses, Length, joined=False):
    # Parses a list of lists, returns a list of cleaned joined tokens, or strings
    Parsed = parse_list(List)
    if joined==False:
        return [clean_text(x, tenses,Length) for x in Parsed]
    elif joined==True:
        return [' '.join(clean_text(x, tenses,Length)) for x in Parsed]      

def create_corpus(List_of_Lists, tenses, length):
    TEXTS = return_text(List_of_Lists, tenses, length)
    bigram = gensim.models.Phrases(TEXTS)
    texts = [bigram[x] for x in TEXTS]

    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(x) for x in texts]
    return dictionary, corpus


# Creating Condition and Symptom Topic Models
'''
Dict, Corpus =  create_corpus(Conditions, Tenses, 2)
Dict_2, Corpus_2 = create_corpus(Symptoms, Tenses, 2)

Condition_Model = LdaModel(corpus=Corpus,num_topics=15, id2word=Dict)
Symptom_Model = LdaModel(corpus=Corpus_2,num_topics=15, id2word=Dict_2)
'''
# Dumping Condition Corpus and Symptom Corpus into JSON Files
'''
with open('Eval_Conditions.json', 'w') as f:
    json.dump(Corpus, f)
with open('Eval_Symptoms.json', 'w') as f:
    json.dump(Corpus_2, f)      
'''
# Opening Condition and Symptom Corpuses for evaluation
'''
f = open('Eval_Conditions.json')
BOW_Conditions = json.load(f)
g = open('Eval_Symptoms.json')
BOW_Symptoms = json.load(g)
'''

def tuple_sort(list,top_n):
    
    vals = sorted([x[1] for x in list], reverse=True)
    if len(vals)<top_n:
        top_n = len(vals)

    sorted_topics = []
    index = 0
    while top_n>0:
        val = vals[index]
        for x in list:
            if x[1]==val:
                sorted_topics.append(x[0])
                break 
        index +=1
        top_n -=1

    return sorted_topics

# Creating Analysis of individual topics using the above LDA Model, Saving into JSON_Dictionary
# Keys are Conditions, Values are the top 1-3 Symptoms corresponding to the condition
'''
Condition_Symptom_Dict = {}
count = 0
for x in range(len(BOW_Conditions)):
    Cond_Symp = {}
    Top_Condition = Condition_Model[BOW_Conditions[count]]
    A = tuple_sort(Top_Condition,1)
    Symptoms = Symptom_Model[BOW_Symptoms[count]]
    B = tuple_sort(Symptoms,3)
    Cond_Symp[A[0]]= B
    Condition_Symptom_Dict[count] = Cond_Symp
    count +=1

with open('Evaluation_Cond_Symp.json', 'w') as f:
    json.dump(Condition_Symptom_Dict, f)
'''
# Loading in the Evaluation Dictionary
'''
Eval_Dict = open('Evaluation_Cond_Symp.json')
Dict = json.load(Eval_Dict)
print(Dict) 
'''

class Medical_Evaluator:
    def __init__(self, Conditions_Json, Symptoms_Json, Tenses, Length, num_topics):
        Cond = open(Conditions_Json)
        self.Conditions = json.load(Cond)
        Sympt = open(Symptoms_Json)
        self.Symptoms = json.load(Sympt)
        self.Tenses = Tenses
        self.Length = Length
        self.num_topics = num_topics
        self.condition_Corpus = None
        self.Symptom_Corpus = None  
        self.condition_model = None 
        self.symptom_model = None
    
    def create_topic_models(self):
        Dict, Corpus =  create_corpus(self.Conditions, self.Tenses, self.Length)
        Dict_2, Corpus_2 = create_corpus(self.Symptoms, self.Tenses, self.Length)
        Condition_Model = LdaModel(corpus=Corpus,num_topics=self.num_topics, id2word=Dict)
        Symptom_Model = LdaModel(corpus=Corpus_2,num_topics=self.num_topics, id2word=Dict_2)
        self.condition_Corpus = Corpus 
        self.Symptom_Corpus = Corpus_2
        self.condition_model = Condition_Model
        self.symptom_model = Symptom_Model
        return
    
    def create_Eval_Dict(self):

        BOW_Conditions = self.condition_Corpus
        BOW_Symptoms = self.Symptom_Corpus

        Condition_Symptom_Dict = {}
        count = 0
        for x in range(len(BOW_Conditions)):
            Cond_Symp = {}
            Top_Condition = self.condition_model[BOW_Conditions[count]]
            A = tuple_sort(Top_Condition,1)
            Symptoms = self.symptom_model[BOW_Symptoms[count]]
            B = tuple_sort(Symptoms,3)
            Cond_Symp[A[0]]= B
            Condition_Symptom_Dict[count] = Cond_Symp
            count +=1
        return Condition_Symptom_Dict      

Medic = Medical_Evaluator('Conditions.json', 'Symptoms.json', Tenses, 2, 10)
Medic.create_topic_models()
print(Medic.create_Eval_Dict())

# TODO
'''
The Eval_Dict is a list of conditions and their corresponding topics, based on the medical documents
and the topic models

Need to first get the keywords for the topics themselves, then create a dataframe to connect
and correlate average condition to its symptoms 
'''




  