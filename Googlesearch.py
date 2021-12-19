from typing_extensions import final
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
import time
import json
from collections import Counter


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
      a = conference.split()
      
      endings = ['.', '?', '!', '--']

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
      #Operator_Speech is the list

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

      length = len(ANALYST_BREAKS)
      index = 0

      Analyst_Speech = []

      while length >0:
        next = 0
        cur = ANALYST_BREAKS[index]+2
        found = False
        
        for x in UPDATED_BREAKS:
          if found == True:
            break     
          if x >cur:
            next +=x
            found = True
            break   

        speech = updated_transcript[cur:next]
        if len(speech)>0:
      
          speech = speech[:-1]
          
          # print(speech)
          updated_speech  = []
          for x in speech[:-1]:
            updated_speech.append(x)
            

          for x in endings:
            if x in speech[-1]:
              ending = speech[-1].split(x)
              updated_speech.append(ending[0]+x)
              break 
          Analyst_Speech.append(" ".join(updated_speech))    
        else:
          Analyst_Speech.append([])
        
        index +=1
        length -=1
      #Analyst Speech now represents All Analyst speech in the transcript
      #Analyst_Speech is the list

      Big_List = sorted(ANALYST_BREAKS+UPDATED_BREAKS+breaks)


      #Find most common titles for the speakers in this transcript
      TITLE_COUNTER = []
      for x in UPDATED_BREAKS:
        y = updated_transcript[x+1:x+10]
        for z in y:
          if z[0].isupper()==True:
            if len(z)>4:
              TITLE_COUNTER.append(z)

      a = (Counter(TITLE_COUNTER))
      possible_title_words = []
      for x in a.most_common(12):
        possible_title_words.append(x[0])
      possible_title_words.append('of')
      possible_title_words.append('and')

      if 'Thank' in possible_title_words:
        possible_title_words.remove('Thank')
      if 'Thanks' in possible_title_words:
        possible_title_words.remove('Thanks')

      for x in possible_title_words:
        if ',' in x:
          possible_title_words.remove(x)
      for x in possible_title_words:
        if '.' in x:
          possible_title_words.remove(x)

      #possible_title_words is now a list of the most common words and titles in theory

      name_list = []
      titles_list = []
      text_list = []

      length = len(UPDATED_BREAKS)
      index = 0
      while length >0:
        correct_names = []
        correct_titles = []
        text = []

        cur = UPDATED_BREAKS[index]
        names = updated_transcript[cur-2:cur]
        titles = updated_transcript[cur+1:cur+10]
        
        to_split = names[0]
        
        for y in endings:
          if y in to_split:
            
            new = to_split.split(y)      
            
            correct_names.append(new[-1])
            correct_names.append(names[-1])
            break 
        
        if y not in to_split:

          correct_names.append(names[0])
          correct_names.append(names[1])
          
        name_list.append(' '.join(correct_names))

        #use the list possible_title_words to figure out the titles or people

        for x in titles:
          if x in possible_title_words:
            correct_titles.append(x)

          else:
            break

        titles_list.append(' '.join(correct_titles))  
        #use the list possible_title_words to figure out the titles or people

        #get length of titles_list to find where to start text search
        LEN = len(correct_titles)
        text_start = cur + LEN + 1
        found = False 
        for x in Big_List:
          if found == True:
            break
          if x > text_start:
        
            for y in updated_transcript[text_start:x-2]:
              text.append(y)

            last = updated_transcript[x-2]
                  
            for x in endings:
              if x in last:
                ending = last.split(x)
                text.append(ending[0])
            
            found = True
            break  

        text_list.append(' '.join(text))    
            
        index +=1
        length -=1

      final_speaker_list = []
      a = len(text_list)
      index = 0

      while a >0:
        name = name_list[index]
        title = titles_list[index]
        text = text_list[index]

        final_speaker_list.append((name, title, text))
        index +=1
        a -=1
    
      print(Operator_Speech)
      print('---------------------------------------------------------')
      print(Analyst_Speech)
      print('----------------------------------------------------')
      print(final_speaker_list)
      print('-----------------------------------------------------')
      print('DONE, NEXT REPORT')
      print('-----------------------------------')
    
        

#Run on Microsoft 2021
#Working!





Search = find_useful_searches('microsoft', 2021)

if Search[0]== 'Motley':
  A = Motley_Scraper(Search[1], 2021)
  A.create_conversation_list()
  
  A.subdivide_conversations()







#The same function as in the class, only separate  

def parse_text(text):
    
  a = text.split()
  endings = ['.', '?', '!', '--']

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
  #Operator_Speech is the list


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


  length = len(ANALYST_BREAKS)
  index = 0

  Analyst_Speech = []

  while length >0:
    next = 0
    cur = ANALYST_BREAKS[index]+2
    found = False
    
    for x in UPDATED_BREAKS:
      if found == True:
        break     
      if x >cur:
        next +=x
        found = True
        break   

    speech = updated_transcript[cur:next]
    if len(speech)>0:
        
      speech = speech[:-1]
      
      # print(speech)
      updated_speech  = []
      for x in speech[:-1]:
        updated_speech.append(x)
        

      for x in endings:
        if x in speech[-1]:
          ending = speech[-1].split(x)
          updated_speech.append(ending[0]+x)
          break 
      Analyst_Speech.append(" ".join(updated_speech))    
    else:
      Analyst_Speech.append([])

    index +=1
    length -=1
  #Analyst Speech now represents All Analyst speech in the transcript
  #Analyst_Speech is the list

  Big_List = sorted(ANALYST_BREAKS+UPDATED_BREAKS+breaks)


  #Find most common titles for the speakers in this transcript
  TITLE_COUNTER = []
  for x in UPDATED_BREAKS:
    y = updated_transcript[x+1:x+10]
    for z in y:
      if z[0].isupper()==True:
        if len(z)>4:
          TITLE_COUNTER.append(z)

  a = (Counter(TITLE_COUNTER))
  possible_title_words = []
  for x in a.most_common(12):
    possible_title_words.append(x[0])
  possible_title_words.append('of')
  possible_title_words.append('and')

  if 'Thank' in possible_title_words:
    possible_title_words.remove('Thank')
  if 'Thanks' in possible_title_words:
    possible_title_words.remove('Thanks')

  for x in possible_title_words:
    if ',' in x:
      possible_title_words.remove(x)
  for x in possible_title_words:
    if '.' in x:
      possible_title_words.remove(x)

  #possible_title_words is now a list of the most common words and titles in theory

  name_list = []
  titles_list = []
  text_list = []

  length = len(UPDATED_BREAKS)
  index = 0
  while length >0:
    correct_names = []
    correct_titles = []
    text = []

    cur = UPDATED_BREAKS[index]
    names = updated_transcript[cur-2:cur]
    titles = updated_transcript[cur+1:cur+10]
    
    to_split = names[0]
    
    for y in endings:
      if y in to_split:
        
        new = to_split.split(y)      
        
        correct_names.append(new[-1])
        correct_names.append(names[-1])
        break 
    
    if y not in to_split:

      correct_names.append(names[0])
      correct_names.append(names[1])
      
    name_list.append(' '.join(correct_names))

    #use the list possible_title_words to figure out the titles or people

    for x in titles:
      if x in possible_title_words:
        correct_titles.append(x)

      else:
        break

    titles_list.append(' '.join(correct_titles))  
    #use the list possible_title_words to figure out the titles or people

    #get length of titles_list to find where to start text search
    LEN = len(correct_titles)
    text_start = cur + LEN + 1
    found = False 
    for x in Big_List:
      if found == True:
        break
      if x > text_start:
    
        for y in updated_transcript[text_start:x-2]:
          text.append(y)

        last = updated_transcript[x-2]
              
        for x in endings:
          if x in last:
            ending = last.split(x)
            text.append(ending[0])
        
        found = True
        break  

    text_list.append(' '.join(text))    
        
    index +=1
    length -=1

  final_speaker_list = []
  a = len(text_list)
  index = 0

  while a >0:
    name = name_list[index]
    title = titles_list[index]
    text = text_list[index]

    final_speaker_list.append((name, title, text))
    index +=1
    a -=1



  print(Operator_Speech)
  print('----------------')
  print(Analyst_Speech)
  print('-------------------')
  print(final_speaker_list)
  print('-------------------')

# with open('Apple_transcripts.json') as f:
#   Transcript = json.load(f)

# for x in Transcript:
#   parse_text(x)





  
    


