import os
import pandas as pd
from glob import glob

import os
# Need to create parser here, to put txt file into pandas df
# Need to divide the text files into Two Categories:
# 1) Condition
# 2) Symptoms

#Each list will represent Condition:Symptom
# Each one will be ordered, and the models will go through at the end, classifying Conditions, and symptoms
# Into one Dataframe

directory = r"C:\Users\JayBeast\Multiple-Tic-Tac-Toe\training_data"
Conditions = []
Symptoms = []
for filename in os.listdir(directory):
    
    if filename.endswith(".txt"):             
        
        PATH = os.path.join(directory, filename)                
        df = open(PATH, "r")
        lines = df.readlines()
        start = False 
        # Create Condition List for each patient, Selecting History of Present Illness up to Physical Exam
        Condition = []
        for line in lines:
            line = line.strip()
            
            if line == "Physical Exam:":
                Conditions.append(Condition)
                break 
            if start == True:
                Condition.append(line)

            if line == "History of Present Illness:":
                start = True
        start = False 
        # Create Symptom List for each patient, Selecting History of Present Illness up to Physical Exam
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

print(len(Conditions))
print(len(Symptoms))

# Now that there are two lists, one with Conditions, one with Symptoms, time for topic modeling
# Clean data, etc

    