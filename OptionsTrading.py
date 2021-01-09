from NLPModels import *
from CompanyName import *

import yfinance as yf
from yfinance import Ticker
import json
import matplotlib.pyplot as plt
import pandas as pd
import datetime

from pandas_datareader import data, wb, Options

# define variables:
# ticker_nm: Ticker = yf.Ticker("FB")
# # print(ticker_nm)


# # get detailed stock info
# x = ticker_nm.info
# print(x)

# URL = 'https://finance.yahoo.com/quote/FB/options?p=FB'
# html_text = requests.get(URL).text
# soup = BeautifulSoup(html_text, 'html.parser')
# A = soup.find("div", {"class": "W(100%)"})
# # B = (A.find('div'))
# # # print(B)
# # print(B)
# for link in A.find_all('a'):
#     B = (link.get('href'))
#     if "FB/options?strike=" in B:
#         print(B)
URL = 'https://finance.yahoo.com/quote/FB/options?p=FB'
html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, 'html.parser')
A = soup.find("div", {"class": "W(100%)"})
B = (A.get_text())
C =(B.split())
Option_Names = []
for x in C:
    if "FB2101" in x:
        Option_Names.append(x)
Options_Better = []
for x in Option_Names:
    a = x.split('%')
    b = a[-1].split('FB')
    contract_name = ''.join(('FB',b[-1][0:15]))
    Options_Better.append(contract_name)
    # Options_Better.append(contract_name)
    # Options_Better.append(b[-1][0:15])
print(Options_Better)

#Options_Better is a list of Contract Names:
# More to come     


#if contains -








# <tr class="data-row4 Bgc($hoverBgColor):h BdT Bdc($seperatorColor) H(33px) in-the-money Bgc($hoverBgColor)"


# URL2 = 'https://finance.yahoo.com/quote/FB/options?p=FB'
# html_text = requests.get(URL2).text
# soup = BeautifulSoup(html_text, 'html.parser')
# B = soup.find("div", {"class": "data-row4 Bgc($hoverBgColor):h BdT Bdc($seperatorColor) H(33px) in-the-money Bgc($hoverBgColor)"})
# # B = str(A.find('p'))
# print(B)

# <div class="Pb(10px)"

# <div class="W(100%) "><table class="calls W(100%) Pos(r) Bd(0) Pt(0) list-options">

# import pandas_datareader as web
# from pandas_datareader import Options

# import datetime

# # start = datetime.datetime(2010, 1, 1)

# # end = datetime.datetime(2013, 1, 27)

# # f = web.DataReader("FB", 'yahoo', start, end)
# # print(f)


# Fb = Options('fb', 'yahoo')

# data = Fb.get_all_data()
# B = Fb.expiry_dates

# # A = data.iloc[0:5, 0:5]
# print(B)