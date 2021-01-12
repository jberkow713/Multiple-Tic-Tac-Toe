import requests
from bs4 import BeautifulSoup
import re
def create_Proxy_List():

  from lxml.html import fromstring
  url = 'https://free-proxy-list.net/'
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, 'html.parser')
  IP_addresses = []
  A = soup.find("div", {"class": "table-responsive"})
  B = (A.get_text())
  C =(B.split())

  count = 0
  for x in C:
    
    if 'ago' in x:
      x = x.lower()
      x = re.sub('[a-z]', '', x)
      if  x.endswith('80')== True and x.endswith('8080')==False:
        x = x[:-2]
        x = x + ":80"
        IP_addresses.append(x)
        count+=1  
      
    if count == 16:
      break 
  return(IP_addresses)
ROTATING_PROXY_LIST = create_Proxy_List()

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
}




