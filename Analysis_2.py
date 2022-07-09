import numpy as np
import spacy
import gensim
from gensim.models import CoherenceModel, LdaModel, HdpModel, LsiModel
from gensim.corpora import Dictionary
import pyLDAvis.gensim
import os, re, operator, warnings
import json
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
    return dictionary, corpus

Dict, Corpus =  create_corpus(Conditions, Tenses, 2)
Dict_2, Corpus_2 = create_corpus(Symptoms, Tenses, 2)

# lsimodel = LsiModel(corpus=Corpus, num_topics=10, id2word=Dict)
# print(lsimodel.show_topics(num_topics=5))

hdp_model_conditions = HdpModel(corpus=Corpus, id2word=Dict)
print(hdp_model_conditions.show_topics())

hdp_model_symptoms = HdpModel(corpus=Corpus_2, id2word=Dict_2)
print(hdp_model_symptoms.show_topics())

# lda_model = LdaModel(corpus=Corpus, num_topics=10, id2word=Dict)
# print(lda_model.show_topics())

# Going with the hdp_model for evaluation




  