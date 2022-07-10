import numpy as np
import spacy
import gensim
from gensim.models import CoherenceModel, LdaModel, HdpModel, LsiModel
from gensim.corpora import Dictionary
import pyLDAvis.gensim
import os, re, operator, warnings
import json
from collections import Counter
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.colheader_justify', 'center')

# Setting the random seed
np.random.seed(57)
warnings.filterwarnings('ignore')
nlp = spacy.load('en_core_web_sm')
# importing stopwords
stopwords = nlp.Defaults.stop_words
# add words to stopwords
my_stopwords = [u'patient', u'start',u'history', u'note', u'pain', u'family',\
    u'report', u'normal', u'deny', u'give', u'prior', u'present', u'left', u'right', \
        u'received', u'denies', u'medical',u'given', u'daughter', u'noted',  u'found', u'days',\
            u'social', u'home', u'reports', u'years', u'year', u'started', u'past', \
                u'showed', u'presented', u'symptoms', u'developed', u'recent', u'lives', u'live', \
                    u'mother', u'admitted', u'week', u'diagnosed', u'diagnoses',\
                        u'admission', u'wife', u'diagnosis']

for word in my_stopwords:
    lexeme = nlp.vocab[word]
    lexeme.is_stop = True

# Open files with Conditions and Symptoms Text, store in Variables
f = open('Conditions.json')
Conditions = json.load(f)
g = open('Symptoms.json')
Symptoms = json.load(g)

def parse_list(List):
    # Create function to return joined strings of text from list of lists
    return [' '.join(x) for x in List]
 
def num_check(s):
    # Checks if a string contains a digit
    return any(i.isdigit() for i in s)

def clean_text(text, tenses, Length):
    # Cleans a string of text, based on allowable tenses, and min_length of a word
    new = re.sub('[^A-Za-z0-9]+', ' ', text)
    New = [x.lower() for x in new.split() if num_check(x)==False]
    # NLP objects for the cleaned text
    doc = nlp(' '.join(New))
    cleaned = [x.text for x in doc if x.is_stop==False and x.pos_ in tenses and len(x)>Length]
    return cleaned    

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
        self.Condition_Dict = {}
        self.Symptom_Dict = {}
        self.cond_symp_Dict = None
    
    def create_topic_models(self):
        # Creates topic models using Condition and Symptom Files and global functions
        Dict, Corpus =  create_corpus(self.Conditions, self.Tenses, self.Length)
        Dict_2, Corpus_2 = create_corpus(self.Symptoms, self.Tenses, self.Length)
        Condition_Model = LdaModel(corpus=Corpus,num_topics=self.num_topics, id2word=Dict)
        Symptom_Model = LdaModel(corpus=Corpus_2,num_topics=self.num_topics, id2word=Dict_2)
        self.condition_Corpus = Corpus 
        self.Symptom_Corpus = Corpus_2
        self.Condition_Dict = {}
        self.Symptom_Dict = {}
        self.condition_model = Condition_Model
        self.symptom_model = Symptom_Model
        return
    
    def create_Eval_Dict(self):
        # Creates Dictionary that evaluates medical files and returns
        # {0: Condition: Symptom/s...}
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
    
    def concat(self, topic):
    # Creates readable topics for a given topic model topic
        to_remove = ['+', '.', '*', '#', '"']        
        l = []
        Topic = ""
        for x in topic[1].split():
            l.append(''.join([i for i in x if not i.isdigit() and i not in to_remove]))
        for x in l:
            if len(x)>0:
                Topic+=x + ' '
        return Topic    
    
    def topics(self):
        # Concatenates topics into a Dictionary of Topic: String
        Cond_Topics = self.condition_model.print_topics()
        Symp_Topics = self.symptom_model.print_topics()
        for x in Cond_Topics:
            self.Condition_Dict[x[0]]=self.concat(x)
        for x in Symp_Topics:
            self.Symptom_Dict[x[0]]=self.concat(x)        

    def conditions_to_symptoms(self):
        # Evaluate Condition_Symptom Dictionary to find top 1-3 symptoms for each condition
        D = self.create_Eval_Dict()
        num_topics = self.num_topics
        Cond_Symp_Dict = {}
        for i in range(num_topics):            
            topics = []
            for v in D.values():
                for x,y in v.items():
                    if x ==i:
                        for z in y:
                            topics.append(z)
            C = Counter(topics)
            Top_3 = C.most_common(3)
            Sympts = [x[0] for x in Top_3]            
            Cond_Symp_Dict[i]=Sympts
        self.cond_symp_Dict = Cond_Symp_Dict    
        return Cond_Symp_Dict

    def display_results(self):
        # Create_Dataframe with Conditions Corresponding to Symptoms
        self.topics()
        df = pd.DataFrame.from_dict(self.Condition_Dict,orient='index')
        df.rename(columns = {0 : 'Conditions by Index'}, inplace = True)                
        print(df)
        print('-------------------------------------')
        df2 = pd.DataFrame.from_dict(self.Symptom_Dict,orient='index')
        df2.rename(columns = {0 : 'Symptoms by Index'}, inplace = True)
        print(df2)
        print('-------------------------------------')        
        df_3 = pd.DataFrame.from_dict(self.cond_symp_Dict,orient='index')
        df_3.rename(columns = {0 : 'Top Factor', 1 : '2nd Factor', 2: '3rd Factor'}, inplace = True)
        df_3 = (df_3.set_axis(['Condition ' + str(x) for x in range(self.num_topics)], axis=0))
        print(df_3)


Tenses = ['NOUN', 'VERB', 'ADJ']
Medic = Medical_Evaluator('Conditions.json', 'Symptoms.json', Tenses, 3, 10)
Medic.create_topic_models()
Medic.conditions_to_symptoms()
Medic.display_results()

Tenses_2 = ['NOUN', 'VERB', 'ADJ', 'ADV']
Medic_2 = Medical_Evaluator('Conditions.json', 'Symptoms.json', Tenses_2, 3, 15)
Medic_2.create_topic_models()
Medic_2.conditions_to_symptoms()
Medic_2.display_results()

'''
Medic Evaluator model 1: Medic

0  abdominal blood negative changes severe felt states repair disease fluid
1  abdominal disease increased month time renal nausea_vomiting negative denied severe
2  chest negative transferred disease multiple changes month cancer abdominal chronic
3  time bilateral negative today care baseline treated nausea_vomiting abdominal chest
4  chest significant time transferred location abdominal disease felt multiple placed
5  negative blood time placed abdominal foot cancer bleeding chest baseline
6  negative chest time disease abdominal transferred felt children stage severe
7  treated transferred abdominal time brain negative feeling nausea_vomiting bleeding fluid
8  abdominal chronic review_systems nausea_vomiting chest negative baseline time location bilateral
9  chest time abdominal blood significant hypertension negative location tobacco multiple
-------------------------------------
                                                    Symptoms by Index
0  blood failure anemia primary secondary cell cancer renal_failure atrial_fibrillation chronic
1  secondary primary bleeding hypertension cancer kidney chronic pulmonary coronary_artery mechanical
2  secondary failure infection primary atrial_fibrillation leakage disease renal_failure transfer acute_renal
3  secondary primary disease renal hypotension failure status chronic stage bleed
4  secondary bleed primary abdominal cell disease anemia severe kidney gastrointestinal
5  secondary primary status skin epidural swelling altered_mental deceased pulmonary resolved
6  status altered_mental renal_failure hypertension atrial_fibrillation failure primary exacerbation frequency seizures
7  secondary hypotension abdominal aortic primary liver common bypass post operative
8  failure secondary acute_renal primary syndrome bleeding distress infection status depression
9  bilateral hypotension secondary diabetes gastric hemorrhage renal stage acute_blood acute
-------------------------------------
             Top Factor  2nd Factor  3rd Factor
Condition 0  2           6           1
Condition 1  0           3           5
Condition 2  3           0           2
Condition 3  0           4           9
Condition 4  2           3           8
Condition 5  0           8           2
Condition 6  3           1           0
Condition 7  3           8           7
Condition 8  3           1           4
Condition 9  1           7           0

Medic Evaluator model 2: Medic_2


                                          Conditions by Index
0   negative chest currently time transferred abdominal surgery felt stable months
1   time chest currently acute stable significant placed transferred abdominal disease
2   chest time increased negative bleeding severe abdominal baseline initially chronic
3   transferred infection abdominal placed time chest known negative died currently
4   abdominal foot multiple bilateral disease placed significant negative artery blood
5   time chronic chest negative transferred review_systems nausea_vomiting care abdominal tobacco
6   negative blood multiple location disease felt recently died shortness_breath increased
7   denied nausea_vomiting diarrhea time abdominal recently month blood negative ercp
8   changes time location chest presents abdominal transferred placed cancer status
9   abdominal currently disease recently time care blood multiple placed chest
10  abdominal chest currently hospital improved initially disease negative treated likely
11  chest negative abdominal time placed discharged severe currently chronic cancer
12  blood negative disease husband recently children time chest currently improved
13  chest abdominal multiple negative tobacco transferred today recently nausea_vomiting significant
14  abdominal disease negative felt today month transferred tobacco weeks bilateral
-------------------------------------
                                                   Symptoms by Index
0   secondary failure stent requiring likely lower shock wound bleeding cell
1   failure primary secondary disease kidney acute_renal bilateral multiple transfer seizure
2   primary hypertension disease chronic pulmonary secondary embolism kidney requiring adrenal
3   renal_failure failure acute_chronic hypotension weakness anemia renal overload congestive_heart type
4   expired failure requiring secondary renal_failure dysgerminoma critical ovary thought pneumonia
5   failure respiratory primary cancer leakage sepsis infection pneumonia congestive_heart cell
6   secondary primary hypotension abdominal hemorrhage coronary_artery atrial_fibrillation failure chronic elevated
7   disease secondary gastric stage severe atrial_fibrillation chronic bipolar cancer hypotension
8   secondary primary failure liver acute artery intoxication altered_mental abuse ventricular
9   primary secondary acute hypertension pulmonary disease transfer high atrial_fibrillation status
10  status secondary primary failure hypertension disease post coronary_artery infection altered_mental
11  bleed secondary primary colitis infection metastatic small doctor upper ventricular
12  depression harvesting myocardial hypoglycemia greater saphenous coronary infarction anxiety bypass
13  primary secondary common repair abdominal aortic bypass pericardial effusion bleed
14  secondary primary abdominal diabetes bleed failure acute_chronic status heart_failure systolic
-------------------------------------
              Top Factor  2nd Factor  3rd Factor
Condition 0   1           0           14
Condition 1   0           6           14
Condition 2   10          0           8
Condition 3   0           10          5
Condition 4   9           13          7
Condition 5   6           0           9
Condition 6   6           2           0
Condition 7   0           6           12
Condition 8   8           11          1
Condition 9   0           11          1
Condition 10  0           14          9
Condition 11  0           14          6
Condition 12  6           7           2
Condition 13  6           1           14
Condition 14  0           3           10

''' 