from typing_extensions import final
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse


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
    return final_links
  
  if motleyflag == False:
    for x in final_links:
      if 'seekingalpha.com' in x:
        if 'earnings/transcripts' in x:
          return x   


print(find_useful_searches('standard chartered PLC', 2021))

# 'https://seekingalpha.com/symbol/SCBFF/earnings/transcripts', 
# 'https://seekingalpha.com/article/4444561-standard-chartered-plc-scbff-ceo-william-winters-on-q2-2021-results-earnings-call-transcript',
#  'https://www.alacrastore.com/thomson-streetevents-transcripts/Q1-2021-Standard-Chartered-PLC-Earnings-Call-T14628598',
# 'https://www.sc.com/en/investors/', 'https://www.sc.com/en/investors/events-and-presentations/'


#TODO 

#from the list of links, need to create two web scraping classes, one for seekingalpha, one for motleyfool
#each will pull text from specific yearly calls



