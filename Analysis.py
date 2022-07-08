import os
import pandas as pd
from glob import glob

import os
# Need to create parser here, to put txt file into pandas df
# Need to divide the text files into Two Categories:
# 1) Condition
# 2) Symptoms
# Have to decide, when parsing txt files, which parts go in Condition Dict, and Which parts go in Symptoms
# Need to store the information in the format of list of lists, so that gensim can run topic modeling on it

#Each list will represent Condition:Symptom
# Each one will be ordered, and the models will go through at the end, classifying Conditions, and symptoms
# Into one Dataframe

directory = r"C:\Users\JayBeast\Multiple-Tic-Tac-Toe\training_data"
count = 0
Conditions = []
Symptoms = []
for filename in os.listdir(directory):
    if count == 15:
        break
    if filename.endswith(".txt"):
        
        count +=1
        # Do something with the file here
        PATH = os.path.join(directory, filename)
        
        df = open(PATH, "r")
        lines = df.readlines()
        start = False 
        # Create Condition List for each patient, Selecting History of Present Illness up to Physical Exam
        Condition = []
        for line in lines:
            line = line.strip()
            
            if line == "Pertinent Results:":
                Conditions.append(Condition)
                break 
            if start == True:
                Condition.append(line)

            if line == "History of Present Illness:":
                start = True
        start = False 
        # Create Condition List for each patient, Selecting History of Present Illness up to Physical Exam
        Symptom = []
        for line in lines:
            line = line.strip()
            
            if line == "Major Surgical or Invasive Procedure:":
                break 
            if start == True:
                Symptom.append(line)
                start = False

            if line == "Chief Complaint:":
                start = True
        
        for line in lines:
            line = line.strip()
            
            if line == "Discharge Condition:":
                Symptoms.append(Symptom)
                break 
            if start == True:
                Symptom.append(line)

            if line == "Discharge Diagnosis:":
                start = True                       
                   
        df.close()  

print(Conditions, len(Conditions))
print(Symptoms, len(Symptoms))

    