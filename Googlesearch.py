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
# print(googleSearch("apple transcripts 2021"))

# print(googleSearch('standard charter PLC transcripts 2021'))

def find_useful_searches(company_name, year):
  list = googleSearch(company_name+'transcripts'+str(year))
  final_links = []
  for x in list:
    if 'fool.com/earnings/call-transcripts' in x:
      final_links.append(x)
    if 'seekingalpha.com' in x:
      if 'earnings/transcripts' in x:
        final_links.append(x)

  return final_links

print(find_useful_searches('apple', 2021))



