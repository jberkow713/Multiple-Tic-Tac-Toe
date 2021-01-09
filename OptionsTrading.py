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
Contract_Names = []
Trading_Data = []
Trading_Times = []
Last_Trading_Date = []
for x in C:
    if "FB" in x:

        a = x.split('%')
        b = a[-1].split('FB')
        contract_name = ''.join(('FB',b[-1][0:15]))
        Contract_Names.append(contract_name)
       
    for y in Contract_Names:
        if y in x or "AM" in x or "PM" in x or "EST" in x:
            if x not in Trading_Data:
                Trading_Data.append(x)
for x in C:
    if ":" in x:
        if "AM" in x or "PM" in x:
            Trading_Times.append(x)
Trading_Times = Trading_Times[1:]
for x in Trading_Data:
    for y in Contract_Names:
        if y in x:
            if x not in Last_Trading_Date:
                a = x.split('%')
                Last_Trading_Date.append(a[-1])
Last_Trading_Date = Last_Trading_Date[1:]
Contract_Names = Contract_Names[1:] 
# print(Contract_Names)
# print(Last_Trading_Date)
# print(Trading_Times)    
# print(Trading_Data)
cleaned_contracts = []
for y in Last_Trading_Date:
    for x in Contract_Names:
            
        if x in y:
            z = y.replace(x,'')
            cleaned_contracts.append(z)
# print(cleaned_contracts)
cleaned_contracts_final = []
for x in cleaned_contracts:
    x = x.replace("Volatility", '')
    cleaned_contracts_final.append(x)

Last_Trade_Date = [i + ' ' + j + ' ' + 'EST' for i, j in zip(cleaned_contracts_final, Trading_Times)] 
print(Contract_Names)                     
print(Last_Trade_Date)
print(len(Contract_Names))
print(len(Last_Trade_Date))
print(len(Trading_Times))
    # y = x.replace('.good','')





#Trading times is Time of day in last trade date
          
                        




Contract_Names = Contract_Names[1:]

# print(Trading_Data)
   


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