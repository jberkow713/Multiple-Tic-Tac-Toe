import numpy as np
import spacy
import gensim
from gensim.models import CoherenceModel, LdaModel
from gensim.corpora import Dictionary
import pyLDAvis.gensim
import os, re, operator, warnings
import json
warnings.filterwarnings('ignore')
nlp = spacy.load('en_core_web_sm')
stopwords = nlp.Defaults.stop_words

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

def return_text(List, tenses, Length):
    # Parses a list of lists, returns a list of cleaned joined strings
    Parsed = parse_list(List)
    return [clean_text(x, tenses,Length) for x in Parsed]  

def create_corpus(List_of_Lists, tenses, length):
    TEXTS = return_text(List_of_Lists, tenses, length)
    bigram = gensim.models.Phrases(TEXTS)
    texts = [bigram[x] for x in TEXTS]

    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(x) for x in texts]
    return corpus

Corpus = create_corpus(Conditions, Tenses, 2)
print(Corpus)

   

# Create function to clean text


  