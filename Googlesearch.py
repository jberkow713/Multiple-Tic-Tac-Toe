from typing_extensions import final
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
import time
import json

def googleSearch(query):
    g_clean = [ ] 
    url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query)
    try:
      html = requests.get(url)
      if html.status_code==200:
        soup = BeautifulSoup(html.text, 'lxml')
        a = soup.find_all('a') 
        for i in a:
          k = i.get('href')
          try:
            m = re.search("(?P<url>https?://[^\s]+)", k)
            n = m.group(0)
            rul = n.split('&')[0]
            domain = urlparse(rul)
            if(re.search('google.com', domain.netloc)):
              continue
            else:
              g_clean.append(rul)
          except:
            continue
    except Exception as ex:
      print(str(ex))
    finally:
      return g_clean[0:5]
# print(googleSearch("standard chartered plc transcripts 2021"))

def find_useful_searches(company_name, year):
  list = googleSearch(company_name + ' transcripts'+' '+ str(year))
    
  final_links = []
  
  motleyflag = False  
  for x in list:
    if 'seekingalpha.com' in x:
      if 'earnings/transcripts' in x:
        final_links.append(x)
            
    if 'fool.com/earnings/call-transcripts' in x:
      final_links.append(x)
      motleyflag = True 
  
  if motleyflag == True:
    for x in final_links:
      if 'seekingalpha.com' in x:
        final_links.remove(x)
    return 'Motley', final_links
  
  if motleyflag == False:
    for x in final_links:
      if 'seekingalpha.com' in x:
        if 'earnings/transcripts' in x:
          return x   

# print(find_useful_searches('apple', 2021))

#Essentially, if Motley fool can be used to scrape for transcripts, the sites returned through the previous function
#Will be fed into the Motley Scraper class, as a list, and each one of those links will be trancribed from the Motley Fool
#Website and eventually put into a table

#Otherwise, a Seekingalpha class will have to do the rest

class Motley_Scraper():

  def __init__(self, list_of_links, year):
    self.list_of_links = list_of_links
    self.year = year
    self.conversation_list = []
    self.individual_conversations = []
    self.titles = ['Officer', 'Analyst', 'Relations', 'Head', 'Director', 'Chief', 'Senior', 'President']
    self.sentence_enders = [".", '!', '?', ","]
  
  def create_conversation_list(self):
    'Scrapes Motley Fool and creates conversation'

    for x in self.list_of_links:
      
      html_page = requests.get(x).text
      
      soup = BeautifulSoup(html_page, 'html.parser')

      A = soup.find("div", {"class": "content-container"})
      A = A.text
      B =A.split()

      count = 0
      for x in B:
        count +=1
        if str(self.year) in x:
          
          start_val = count
          break
      
      count = 0   
      
      for x in B:
        count +=1   
        if '[Operator' in x:
          end_val = count
          if B[end_val+1]=='signoff]':
            break

      text = B[start_val:end_val-1]
      #full_text creates relevant text for the particular document
      full_text = ' '.join(text)

      self.conversation_list.append(full_text)

      time.sleep(5)
  
  def subdivide_conversations(self):
    'Divides full conversation into smaller list of (Speaker, Speech)'    

    for conference in self.conversation_list:
      A = conference.split()

     
      index = 0
      speaker_indices = []
      
      length = len(A)

      while length >0:

        word = A[index]
          
        if word == '--':
          current = index
          
          val = current              
          
          for next_word in A[current:current+15]:
            
            for x in self.titles:
              if x in next_word:

                target = val     
              
                speaker_list = A[current-2:current]
                punct_flag = False
                for x in self.sentence_enders:
                                    
                                
                  if x in speaker_list[0]:
                    punct_flag = True
                    divider = x                

                    speaker = speaker_list[0].split(divider)[1]+ ' ' + speaker_list[1]
                    
                    if (speaker, index+1) not in speaker_indices:
                      speaker_indices.append((speaker, target))                 
                
                if punct_flag == False:
                  speaker = speaker_list[0]+' '+ speaker_list[1]
                  if (speaker, index+1) not in speaker_indices:
                      speaker_indices.append((speaker, target)) 
            val +=1

          index +=15
          length -=15
        
        index +=1
        length -=1

      speakers = []
      speaker_vals = []
           

      for x in speaker_indices:
        speakers.append(x[0])
        speaker_vals.append(x[1])
      
      speaker_length = len(speakers)

      index = 0

      while speaker_length >0:
        
        current = speaker_vals[index]
        
        if index+1 <len(speakers):
          next = speaker_vals[index+1]
          next -=3          

          text = A[current:next+1]
          
          if len(text)>0:

            for x in self.sentence_enders:
              if x in text[-1]:
                new = text[-1].split(x)
                replace = new[0]
                text[-1]=replace
            
          speaker_speech = (' '.join(text))
        
        if index+1 == len(speakers):

          text = A[current:]
          if len(text)>0:
          
            for x in self.sentence_enders:
              if x in text[-1]:
                new = text[-1].split(x)
                replace = new[0]
                text[-1]=replace
          
          speaker_speech = (' '.join(text))
        self.individual_conversations.append((speakers[index], speaker_speech, self.year))       
        
        index+=1
        speaker_length -=1
      for x in self.individual_conversations:
        if len(x[1])<20:
          self.individual_conversations.remove(x)
      self.individual_conversations= self.individual_conversations[0:-2]


#if Apple transcripts use Motley to scrape, pass it into the scraper
'''
Search = find_useful_searches('apple', 2021)
if Search[0]== 'Motley':
  A = Motley_Scraper(Search[1], 2021)
  A.create_conversation_list()
  #let's store this in a json file to operate on
  # print(A.conversation_list)
  
  with open('Apple_transcripts.json', 'w') as f:
      json.dump(A.conversation_list, f)
'''


#lets open Apple Transcripts and operate on the text

#Begin here
with open('Apple_transcripts.json') as f:
  Transcript = json.load(f)

endings = ['.', '?', '!']
a = Transcript[0].split()
updated_transcript = []
#Find operator text up front, remove it possibly
operator_indices = []
breaks = []
count = 0
for x in a:

  if 'Operator' in x:
    operator_indices.append(count)
    op_split = x.split('Operator')
    updated_transcript.append('Operator')
    updated_transcript.append(op_split[1])
    count +=2
  
  else:
    updated_transcript.append(x)
    count +=1 

count = 0
for x in updated_transcript:
  if '--' in x:
    breaks.append(count)
    count +=1
  else:
    count +=1

ending_operator = []

for x in operator_indices:
  end_found = False
  for y in breaks:
    if end_found == True:
      
      break 
    if y >x:
      ending_operator.append(y)
      end_found = True 
      break

actual_endings = [x-1 for x in ending_operator]
operator_start = [x+1 for x in operator_indices]

length = len(actual_endings)
index = 0

while length >0:
  next = index+1    
  if index < len(actual_endings)-1:
    if actual_endings[next]-actual_endings[index]==0:
      del actual_endings[next]
      del operator_start[next]
  
  index +=1
  length -=1 

a = len(operator_start)
index = 0
Operator_Speech = []
while a >0:
  x = updated_transcript[operator_start[index]:actual_endings[index]]
  updated_x = []
  for val in x[:-1]:
    updated_x.append(val)
  aaa = x[-1]
  for z in endings:
    if z in aaa:
      zz = aaa.split(z)
      updated_x.append(zz[0])
  x1 = ' '.join(updated_x)
  Operator_Speech.append(x1)
  index +=1
  a-=1

#operator_speech now gives all speech from the operator for the text
BREAKS = []
for x in breaks:
  val = updated_transcript[x+1]
  if val[0] != 'I' and val[0].isupper()==True:
         
       
    BREAKS.append(x)

#BREAKS is a list of actual breaks where the speaker changes
Analyst_BREAKS = []
for x in BREAKS:

  after = updated_transcript[x:x+10]
  if 'Analyst' in after:
    Analyst_BREAKS.append(x)

length = len(Analyst_BREAKS)
index = 0

ANALYST_BREAKS = []

while length >0:
  cur = Analyst_BREAKS[index]
  next = Analyst_BREAKS[index+1]
  #remove all analyst possible values from BREAKS list first
  if cur in BREAKS:
    BREAKS.remove(cur)

  if next - cur <11:
    ANALYST_BREAKS.append(next)
    BREAKS.remove(next)
    index +=2
    length -=2
  elif next-cur >11:
    ANALYST_BREAKS.append(cur)
    index +=1
    length -=1

#cleaning up Breaks 
UPDATED_BREAKS = [x for x in BREAKS if updated_transcript[x+1] =='Chief' or updated_transcript[x+1]=='Director']

#UPDATED_BREAKS represents all breaks directly before company speaker speaks
#ANALYST_BREAKS represents all breaks directly before an analyst speaks
for x in UPDATED_BREAKS:
  print(updated_transcript[x-2:x])




#So now Analyst Breaks represents every break related to an analyst
#Breaks represents every break related to a speaker of the company








#TODO
#Parse rest of text, return list of speaker, title, text


  
    


