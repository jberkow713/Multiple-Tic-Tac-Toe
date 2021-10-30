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

#Otherwise, a seekingalpha class will have to do the rest

class Motley_Scraper():

  def __init__(self, list_of_links):
    self.list_of_links = list_of_links
    
    self.conversation_list = []
  
  def conversation(self):
    for x in self.list_of_links:
      
      html_page = requests.get(x).text
      
      soup = BeautifulSoup(html_page, 'html.parser')

      A = soup.find("div", {"class": "content-container"})
      A = A.text
      B =(A.split())

      count = 0
      for x in B:
        count +=1
        if 'Operator' in x:
          y = x.replace('Operator', '')
          start_val = count
          break
      count = 0   
      for x in B:
        count +=1   
        if '[Operator' in x:
          end_val = count
          break   
      text = B[start_val:end_val-1]
      text.insert(0,y)
      full_text = ' '.join(text)

      self.conversation_list.append(full_text)

      time.sleep(5)

# A = Motley_Scraper(["https://www.fool.com/earnings/call-transcripts/2021/10/29/apple-aapl-q4-2021-earnings-call-transcript/"])
B = 'https://www.fool.com/earnings/call-transcripts/2021/07/28/apple-aapl-q3-2021-earnings-call-transcript/'
C = Motley_Scraper([B])
C.conversation()
print(C.conversation_list)
# A.conversation()
# print(A.conversation_list)

#TODO 

#from the list of links, need to create two web scraping classes, one for seekingalpha, one for motleyfool
#each will pull text from specific yearly calls



