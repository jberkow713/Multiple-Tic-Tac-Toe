import os
import pandas as pd
from glob import glob
import json

import os
# Create Conditions list of text lists 
# Create Symptoms list of text lists

directory = r"C:\Users\JayBeast\Multiple-Tic-Tac-Toe\training_data"
Conditions = []
Symptoms = []
for filename in os.listdir(directory):
    
    # Each file must have a condition and symptom, in order to be added
    
    if filename.endswith(".txt"):        
        PATH = os.path.join(directory, filename)                
        df = open(PATH, "r")
        lines = df.readlines()
        lines = [x.strip() for x in lines]                
        
        start = False 
        # Create Condition List for each patient, Selecting History of Present Illness up to Physical Exam
        Condition = []
        for line in lines:                        
            if line == "Physical Exam:":
                # Conditions.append(Condition)
                break 
            if start == True:
                Condition.append(line)
            if line == "History of Present Illness:":
                start = True
                
        start = False 
        # Create Symptom List for each patient, Selecting History of Present Illness up to Physical Exam
        Symptom = []
        for line in lines:                        
            if line == "Major Surgical or Invasive Procedure:":
                break 
            if start == True:
                Symptom.append(line)
                start = False
            if line == "Chief Complaint:":
                start = True
        
        start = False 
        for line in lines:                        
            if line == "Discharge Condition:":
                # Symptoms.append(Symptom)
                break 
            if start == True:
                Symptom.append(line)
            if line == "Discharge Diagnosis:":
                start = True                       

        if Condition!=[] and Symptom!=[]:
            Conditions.append(Condition)
            Symptoms.append(Symptom)

        df.close()

# Initially Saving the Data to two json files to be loaded in later for topic modeling

with open('Conditions.json', 'w') as f:
    json.dump(Conditions , f)
with open('Symptoms.json', 'w') as f:
    json.dump(Symptoms, f)    


# Now that there are two lists, one with Conditions, one with Symptoms, time for topic modeling
# Clean data, etc

    