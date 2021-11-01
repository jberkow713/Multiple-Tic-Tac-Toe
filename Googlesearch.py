from typing_extensions import final
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
import time

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
  
  def conversation(self):
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
              # for word in A:
          # index +=1
        if word == '--':
          current = index
          # print(current)
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
      final_speeches = []     
      

      for x in speaker_indices:
        speakers.append(x[0])
        speaker_vals.append(x[1])
      # print(speakers, speaker_vals)

      # print(speakers)
      # print(speaker_vals)
      speaker_length = len(speakers)

      index = 0

      while speaker_length >0:
        
        current = speaker_vals[index]
        
        if index+1 <len(speakers):
          next = speaker_vals[index+1]
          next -=3          

          text = A[current:next]
          
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
        self.individual_conversations.append((speakers[index], speaker_speech))
                
        
        
        index+=1
        speaker_length -=1
      for x in self.individual_conversations:
        if len(x[1])<20:
          self.individual_conversations.remove(x)
      self.individual_conversations= self.individual_conversations[0:-2]

Search = find_useful_searches('apple', 2021)
if Search[0]== 'Motley':
  A = Motley_Scraper(Search[1], 2021)
  A.conversation()
  # print(A.conversation_list)
  A.subdivide_conversations()
  
  print(A.individual_conversations)

#Example of how the format is returned: List of Tuples(Speaker:Text)

# ('Zach Kirkhorn', "Financial Officer I mean we are carrying some amount of costs associated with the factories today. 
# And so the incremental cost associated with turning the factories, it's not 100% of a factory, if that's what you're
#  getting at in your question"),

#  ('Jed Dorsheimer', "Genuity -- Analyst Yes, yes. That's what I was getting at"),
# etc...








