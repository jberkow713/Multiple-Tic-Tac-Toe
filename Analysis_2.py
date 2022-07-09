import numpy as np
import spacy
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
def num_there(s):
  return any(i.isdigit() for i in s)

def clean_text(text):
    new = re.sub('[^A-Za-z0-9]+', ' ', text)
    New = [x.lower() for x in new.split() if num_there(x)==False]
    # NLP objects for the cleaned text
    usable = ['NOUN', 'VERB', 'ADJ', 'ADV']
    doc = nlp(' '.join(New))
    cleaned = [x.lemma_ for x in doc if x.is_stop==False and x.pos_ in usable and len(x)>2]
    return ' '.join(cleaned)

def return_text(List):
    Parsed = parse_list(List)
    return [clean_text(x) for x in Parsed]  

print(return_text(Conditions))   

# Create function to clean text


  