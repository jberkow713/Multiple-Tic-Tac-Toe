from googlesearch import search
from NLPModels import *
import time
#goal is to create function that parses this and returns a list of company names:
#The get_13F function returns a dictionary

# We can then parse the dictionary with this function, to return all of the names of the companies
# Which the venture company has invested in 




 

#Want to create a function that takes this data, and runs each company through google site, to get a 
#list of strings, each string will be the company description from google....
# We use for x in Find_Company_Name(dict):
#           then our google function of "x company description"

# Then operate on the string using advance cosine, to match each one up to a particular industry
# so then we will have a list of company names, and their SEC classifications, Key, and Value
#Dict = {Company:Classification, Company2:Classification, etc...}

# We want an overall classification for the venture capital firm
# Take each value for each key, place in a list, then make a count_Dictionary, using counter or whatever,
# To create a dictionary of {Classification:Count, Classification:Count, etc}
# Take top 3 Classifications, based on Count, and Put in list of descending order, with 

#[Classification_1, and its % of overall classifications, Classification_2, and its % of overall classifications,\
# Classification_3, and its % of overall classifications]  
 
#If we can get the proper string returned from Google, we can make this work

# "https://www.geeksforgeeks.org/performing-google-search-using-python-code/'
#Easy solution to part 1, above
B = {
  "total": {
    "value": 10000,
    "relation": "gte"
  },
  "query": {
    "from": 0,
    "size": 10
  },
  "filings": [
    {
      "id": "859e1b4499eea7884c84b93a272b839a",
      "accessionNo": "0001171843-21-000188",
      "cik": "1071840",
      "ticker": "WNDW",
      "companyName": "SolarWindow Technologies, Inc.",
      "companyNameLong": "SolarWindow Technologies, Inc. (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T16:22:40-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/0001171843-21-000188.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/0001171843-21-000188-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/f10q_010821.htm",
      "entities": [
        {
          "companyName": "SolarWindow Technologies, Inc. (Filer)",
          "cik": "1071840",
          "irsNo": "593509694",
          "stateOfIncorporation": "NV",
          "fiscalYearEnd": "0831",
          "type": "10-Q",
          "act": "34",
          "fileNo": "333-127953",
          "filmNo": "21517710",
          "sic": "2860 Industrial Organic Chemicals"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "FORM 10-Q",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/f10q_010821.htm",
          "type": "10-Q",
          "size": "325479"
        },
        {
          "sequence": "2",
          "description": "EXHIBIT 10.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/exh_101.htm",
          "type": "EX-10.1",
          "size": "74311"
        },
        {
          "sequence": "3",
          "description": "EXHIBIT 31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/exh_311.htm",
          "type": "EX-31.1",
          "size": "9158"
        },
        {
          "sequence": "4",
          "description": "EXHIBIT 31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/exh_312.htm",
          "type": "EX-31.2",
          "size": "9102"
        },
        {
          "sequence": "5",
          "description": "EXHIBIT 32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/exh_321.htm",
          "type": "EX-32.1",
          "size": "4720"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/0001171843-21-000188.txt",
          "type": " ",
          "size": "2604647"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL INSTANCE FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/wndw-20201130.xml",
          "type": "EX-101.INS",
          "size": "423389"
        },
        {
          "sequence": "7",
          "description": "XBRL SCHEMA FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/wndw-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "35517"
        },
        {
          "sequence": "8",
          "description": "XBRL CALCULATION FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/wndw-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "39050"
        },
        {
          "sequence": "9",
          "description": "XBRL DEFINITION FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/wndw-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "120515"
        },
        {
          "sequence": "10",
          "description": "XBRL LABEL FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/wndw-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "219540"
        },
        {
          "sequence": "11",
          "description": "XBRL PRESENTATION FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1071840/000117184321000188/wndw-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "195851"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "1a7b6053e5d254ab4d13e6ed3832b3b4",
      "accessionNo": "0001104659-21-002471",
      "cik": "1820201",
      "ticker": "SGAM",
      "companyName": "Seaport Global Acquisition Corp",
      "companyNameLong": "Seaport Global Acquisition Corp (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T16:10:37-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/0001104659-21-002471.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/0001104659-21-002471-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/tm211914d1_10q.htm",
      "entities": [
        {
          "companyName": "Seaport Global Acquisition Corp (Filer)",
          "cik": "1820201",
          "irsNo": "852157010",
          "stateOfIncorporation": "DC",
          "fiscalYearEnd": "1231",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-39741",
          "filmNo": "21517587",
          "sic": "6770 Blank Checks"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "FORM 10-Q",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/tm211914d1_10q.htm",
          "type": "10-Q",
          "size": "191643"
        },
        {
          "sequence": "2",
          "description": "EXHIBIT 31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/tm211914d1_ex31-1.htm",
          "type": "EX-31.1",
          "size": "11568"
        },
        {
          "sequence": "3",
          "description": "EXHIBIT 31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/tm211914d1_ex31-2.htm",
          "type": "EX-31.2",
          "size": "11488"
        },
        {
          "sequence": "4",
          "description": "EXHIBIT 32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/tm211914d1_ex32-1.htm",
          "type": "EX-32.1",
          "size": "4742"
        },
        {
          "sequence": "5",
          "description": "EXHIBIT 32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/tm211914d1_ex32-2.htm",
          "type": "EX-32.1",
          "size": "4715"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/0001104659-21-002471.txt",
          "type": " ",
          "size": "1629175"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/sgam-20200930.xml",
          "type": "EX-101.INS",
          "size": "135113"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/sgam-20200930.xsd",
          "type": "EX-101.SCH",
          "size": "30156"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/sgam-20200930_cal.xml",
          "type": "EX-101.CAL",
          "size": "11269"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/sgam-20200930_def.xml",
          "type": "EX-101.DEF",
          "size": "117891"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/sgam-20200930_lab.xml",
          "type": "EX-101.LAB",
          "size": "193571"
        },
        {
          "sequence": "11",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820201/000110465921002471/sgam-20200930_pre.xml",
          "type": "EX-101.PRE",
          "size": "183244"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-09-30",
      "effectivenessDate": "2020-09-30"
    },
    {
      "id": "a816c6a1d66db040f2fbd0e78ce68eee",
      "accessionNo": "0001161697-21-000045",
      "cik": "1543066",
      "ticker": "EWST",
      "companyName": "E-WASTE CORP.",
      "companyNameLong": "E-WASTE CORP. (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T14:40:47-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/0001161697-21-000045.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/0001161697-21-000045-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/form_10-q.htm",
      "entities": [
        {
          "companyName": "E-WASTE CORP. (Filer)",
          "cik": "1543066",
          "irsNo": "454390042",
          "stateOfIncorporation": "FL",
          "fiscalYearEnd": "0228",
          "type": "10-Q",
          "act": "34",
          "fileNo": "333-180251",
          "filmNo": "21517108",
          "sic": "4953 Refuse Systems"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "FORM 10-Q QUARTERLY REPORT FOR 11-30-2020",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/form_10-q.htm",
          "type": "10-Q",
          "size": "394630"
        },
        {
          "sequence": "2",
          "description": "PROMISSORY NOTE DATED 11-25-2020 - HOMETOWN INTERNATIONAL, INC.",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ex_4-1.htm",
          "type": "EX-4",
          "size": "25662"
        },
        {
          "sequence": "3",
          "description": "CONSULTING AGREEMENT WITH TRYON CAPITAL, LLC, DATED 09-25-2020",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ex_10-1.htm",
          "type": "EX-10",
          "size": "22564"
        },
        {
          "sequence": "4",
          "description": "CONSULTING AGREEMENT WITH BENZIONS LLC DATED 12-01-2020",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ex_10-2.htm",
          "type": "EX-10",
          "size": "21806"
        },
        {
          "sequence": "5",
          "description": "RULE 13(A)-14(A)/15(D)-14(A) CERTIFICATION OF PRINCIPAL EXECUTIVE AND FINANCIAL ",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ex_31-1.htm",
          "type": "EX-31",
          "size": "6264"
        },
        {
          "sequence": "6",
          "description": "RULE 1350 CERTIFICATION OF CHIEF EXECUTIVE AND FINANCIAL OFFICER",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ex_32-1.htm",
          "type": "EX-32",
          "size": "4846"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/0001161697-21-000045.txt",
          "type": " ",
          "size": "1698673"
        }
      ],
      "dataFiles": [
        {
          "sequence": "7",
          "description": "XBRL INSTANCE FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ewst-20201130.xml",
          "type": "EX-101.INS",
          "size": "223332"
        },
        {
          "sequence": "8",
          "description": "XBRL SCHEMA FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ewst-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "19727"
        },
        {
          "sequence": "9",
          "description": "XBRL CALCULATION FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ewst-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "23370"
        },
        {
          "sequence": "10",
          "description": "XBRL DEFINITION FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ewst-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "45342"
        },
        {
          "sequence": "11",
          "description": "XBRL LABEL FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ewst-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "128620"
        },
        {
          "sequence": "12",
          "description": "XBRL PRESENTATION FILE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1543066/000116169721000045/ewst-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "101688"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "090a04819aec640dd99e39916099adc3",
      "accessionNo": "0000723254-21-000002",
      "cik": "723254",
      "ticker": "CTAS",
      "companyName": "CINTAS CORP",
      "companyNameLong": "CINTAS CORP (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T13:10:39-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/0000723254-21-000002.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/0000723254-21-000002-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130.htm",
      "entities": [
        {
          "companyName": "CINTAS CORP (Filer)",
          "cik": "723254",
          "irsNo": "311188630",
          "stateOfIncorporation": "WA",
          "fiscalYearEnd": "0531",
          "type": "10-Q",
          "act": "34",
          "fileNo": "000-11399",
          "filmNo": "21516730",
          "sic": "2320 Men&apos;s &amp; Boys&apos; Furnishgs, Work Clothg, &amp; Allied Garments"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/723254/000072325421000002/ctas-20201130.htm",
          "type": "10-Q",
          "size": "1631625"
        },
        {
          "sequence": "5",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130_g1.jpg",
          "type": "GRAPHIC",
          "size": "1501255"
        },
        {
          "sequence": "8",
          "description": "EX-31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-ex311x2020x11x30x10q.htm",
          "type": "EX-31.1",
          "size": "13750"
        },
        {
          "sequence": "9",
          "description": "EX-31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-ex312x2020x11x30x10q.htm",
          "type": "EX-31.2",
          "size": "12538"
        },
        {
          "sequence": "10",
          "description": "EX-32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-ex321x2020x11x30x10q.htm",
          "type": "EX-32.1",
          "size": "5966"
        },
        {
          "sequence": "11",
          "description": "EX-32.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-ex322x2020x11x30x10q.htm",
          "type": "EX-32.2",
          "size": "5971"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/0000723254-21-000002.txt",
          "type": " ",
          "size": "10523381"
        }
      ],
      "dataFiles": [
        {
          "sequence": "2",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "40799"
        },
        {
          "sequence": "3",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "95413"
        },
        {
          "sequence": "4",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "175760"
        },
        {
          "sequence": "6",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "508096"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "319945"
        },
        {
          "sequence": "12",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723254/000072325421000002/ctas-20201130_htm.xml",
          "type": "XML",
          "size": "1483498"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "ff94d449bfdc28147f5ef1b2d5c35eba",
      "accessionNo": "0000723125-21-000012",
      "cik": "723125",
      "ticker": "MU",
      "companyName": "MICRON TECHNOLOGY INC",
      "companyNameLong": "MICRON TECHNOLOGY INC (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T12:49:12-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/0000723125-21-000012.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/0000723125-21-000012-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203.htm",
      "entities": [
        {
          "companyName": "MICRON TECHNOLOGY INC (Filer)",
          "cik": "723125",
          "irsNo": "751618004",
          "stateOfIncorporation": "DE",
          "fiscalYearEnd": "0902",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-10658",
          "filmNo": "21516617",
          "sic": "3674 Semiconductors &amp; Related Devices"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/723125/000072312521000012/mu-20201203.htm",
          "type": "10-Q",
          "size": "1504983"
        },
        {
          "sequence": "2",
          "description": "EX-31.1 CEO CERT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/a2021q1ex31-1xceocert.htm",
          "type": "EX-31.1",
          "size": "10001"
        },
        {
          "sequence": "3",
          "description": "EX-31.2 CFO CERT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/a2021q1ex31-2xcfocert.htm",
          "type": "EX-31.2",
          "size": "10026"
        },
        {
          "sequence": "4",
          "description": "EX-32.1 906 CEO CERT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/a2021q1ex32-1x906ceocert.htm",
          "type": "EX-32.1",
          "size": "3787"
        },
        {
          "sequence": "5",
          "description": "EX-32.2 906 CFO CERT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/a2021q1ex32-2x906cfocert.htm",
          "type": "EX-32.2",
          "size": "3789"
        },
        {
          "sequence": "11",
          "description": "GRAPHIC",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_g1.jpg",
          "type": "GRAPHIC",
          "size": "1338945"
        },
        {
          "sequence": "12",
          "description": "GRAPHIC",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_g2.jpg",
          "type": "GRAPHIC",
          "size": "89246"
        },
        {
          "sequence": "13",
          "description": "GRAPHIC",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_g3.jpg",
          "type": "GRAPHIC",
          "size": "487126"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/0000723125-21-000012.txt",
          "type": " ",
          "size": "11787689"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203.xsd",
          "type": "EX-101.SCH",
          "size": "49672"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_cal.xml",
          "type": "EX-101.CAL",
          "size": "98431"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_def.xml",
          "type": "EX-101.DEF",
          "size": "220403"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_lab.xml",
          "type": "EX-101.LAB",
          "size": "686626"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_pre.xml",
          "type": "EX-101.PRE",
          "size": "410536"
        },
        {
          "sequence": "14",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/723125/000072312521000012/mu-20201203_htm.xml",
          "type": "XML",
          "size": "1452311"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-12-03",
      "effectivenessDate": "2020-12-03"
    },
    {
      "id": "6257342acd6182d243fb65716002acc8",
      "accessionNo": "0001275187-21-000005",
      "cik": "1275187",
      "ticker": "ANGO",
      "companyName": "ANGIODYNAMICS INC",
      "companyNameLong": "ANGIODYNAMICS INC (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T12:06:30-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/0001275187-21-000005.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/0001275187-21-000005-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130.htm",
      "entities": [
        {
          "companyName": "ANGIODYNAMICS INC (Filer)",
          "cik": "1275187",
          "irsNo": "113146460",
          "stateOfIncorporation": "DE",
          "fiscalYearEnd": "0531",
          "type": "10-Q",
          "act": "34",
          "fileNo": "000-50761",
          "filmNo": "21516461",
          "sic": "3841 Surgical &amp; Medical Instruments &amp; Apparatus"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/1275187/000127518721000005/ango-20201130.htm",
          "type": "10-Q",
          "size": "1465495"
        },
        {
          "sequence": "2",
          "description": "EX-10.4.6",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/psu2020agreement.htm",
          "type": "EX-10.4.6",
          "size": "95422"
        },
        {
          "sequence": "3",
          "description": "EX-31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/a11302020-exx311.htm",
          "type": "EX-31.1",
          "size": "10737"
        },
        {
          "sequence": "4",
          "description": "EX-31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/a11302020-exx312.htm",
          "type": "EX-31.2",
          "size": "10760"
        },
        {
          "sequence": "5",
          "description": "EX-32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/a11302020-exx321.htm",
          "type": "EX-32.1",
          "size": "4943"
        },
        {
          "sequence": "6",
          "description": "EX-32.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/a11302020-exx322.htm",
          "type": "EX-32.2",
          "size": "4999"
        },
        {
          "sequence": "12",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130_g1.gif",
          "type": "GRAPHIC",
          "size": "11810"
        },
        {
          "sequence": "13",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/image1a.jpg",
          "type": "GRAPHIC",
          "size": "28516"
        },
        {
          "sequence": "14",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/image3a.jpg",
          "type": "GRAPHIC",
          "size": "35014"
        },
        {
          "sequence": "15",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/image_01a.jpg",
          "type": "GRAPHIC",
          "size": "32630"
        },
        {
          "sequence": "16",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/image_41a.jpg",
          "type": "GRAPHIC",
          "size": "857"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/0001275187-21-000005.txt",
          "type": " ",
          "size": "7077886"
        }
      ],
      "dataFiles": [
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "49125"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "98703"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "209151"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "551505"
        },
        {
          "sequence": "11",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "355779"
        },
        {
          "sequence": "17",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1275187/000127518721000005/ango-20201130_htm.xml",
          "type": "XML",
          "size": "1214163"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "c3c77a7c0a2bb31c4fb9cf133e00852a",
      "accessionNo": "0000886206-21-000005",
      "cik": "886206",
      "ticker": "FC",
      "companyName": "FRANKLIN COVEY CO",
      "companyNameLong": "FRANKLIN COVEY CO (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T10:45:30-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/0000886206-21-000005.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/0000886206-21-000005-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130x10q.htm",
      "entities": [
        {
          "companyName": "FRANKLIN COVEY CO (Filer)",
          "cik": "886206",
          "irsNo": "870401551",
          "stateOfIncorporation": "UT",
          "fiscalYearEnd": "0831",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-11107",
          "filmNo": "21516112",
          "sic": "8741 Services-Management Services"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/886206/000088620621000005/fc-20201130x10q.htm",
          "type": "10-Q",
          "size": "2183126"
        },
        {
          "sequence": "2",
          "description": "EX-31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130xex31_1.htm",
          "type": "EX-31.1",
          "size": "12552"
        },
        {
          "sequence": "3",
          "description": "EX-31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130xex31_2.htm",
          "type": "EX-31.2",
          "size": "13586"
        },
        {
          "sequence": "4",
          "description": "EX-32",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130xex32.htm",
          "type": "EX-32",
          "size": "9180"
        },
        {
          "sequence": "5",
          "description": "GRAPHIC",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130x10qg001.jpg",
          "type": "GRAPHIC",
          "size": "4713"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/0000886206-21-000005.txt",
          "type": " ",
          "size": "7102741"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "EX-101.SCH",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "28876"
        },
        {
          "sequence": "7",
          "description": "EX-101.CAL",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "47421"
        },
        {
          "sequence": "8",
          "description": "EX-101.DEF",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "83296"
        },
        {
          "sequence": "9",
          "description": "EX-101.LAB",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "236855"
        },
        {
          "sequence": "10",
          "description": "EX-101.PRE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "217127"
        },
        {
          "sequence": "11",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/886206/000088620621000005/fc-20201130x10q_htm.xml",
          "type": "XML",
          "size": "1557573"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "6c56e5ee502997f571e514b8ff1447eb",
      "accessionNo": "0000916789-21-000005",
      "cik": "916789",
      "ticker": "HELE",
      "companyName": "HELEN OF TROY LTD",
      "companyNameLong": "HELEN OF TROY LTD (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T10:12:56-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/0000916789-21-000005.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/0000916789-21-000005-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130.htm",
      "entities": [
        {
          "companyName": "HELEN OF TROY LTD (Filer)",
          "cik": "916789",
          "irsNo": "742692550",
          "stateOfIncorporation": "D0",
          "fiscalYearEnd": "0229",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-14669",
          "filmNo": "21516037",
          "sic": "3634 Electric Housewares &amp; Fans"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/916789/000091678921000005/hele-20201130.htm",
          "type": "10-Q",
          "size": "2490079"
        },
        {
          "sequence": "2",
          "description": "EX-31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/fy21_q3xexhibit311.htm",
          "type": "EX-31.1",
          "size": "9668"
        },
        {
          "sequence": "3",
          "description": "EX-31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/fy21_q3xexhibit312.htm",
          "type": "EX-31.2",
          "size": "9678"
        },
        {
          "sequence": "4",
          "description": "EX-32",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/fy21_q3xexhibit32.htm",
          "type": "EX-32",
          "size": "6018"
        },
        {
          "sequence": "10",
          "description": "HELEN OF TROY LOGO",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130_g1.jpg",
          "type": "GRAPHIC",
          "size": "50515"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/0000916789-21-000005.txt",
          "type": " ",
          "size": "10164351"
        }
      ],
      "dataFiles": [
        {
          "sequence": "5",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "48562"
        },
        {
          "sequence": "6",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "97873"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "345137"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "701952"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "474178"
        },
        {
          "sequence": "11",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/916789/000091678921000005/hele-20201130_htm.xml",
          "type": "XML",
          "size": "2014150"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "b30010223c46c423d5a00943359dfd48",
      "accessionNo": "0001171843-21-000175",
      "cik": "875582",
      "ticker": "NTIC",
      "companyName": "NORTHERN TECHNOLOGIES INTERNATIONAL CORP",
      "companyNameLong": "NORTHERN TECHNOLOGIES INTERNATIONAL CORP (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T09:00:30-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/0001171843-21-000175.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/0001171843-21-000175-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ntic20201130_10q.htm",
      "entities": [
        {
          "companyName": "NORTHERN TECHNOLOGIES INTERNATIONAL CORP (Filer)",
          "cik": "875582",
          "irsNo": "410857886",
          "stateOfIncorporation": "DE",
          "fiscalYearEnd": "0831",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-11038",
          "filmNo": "21515826",
          "sic": "3470 Coating, Engraving &amp; Allied Services"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "FORM 10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/875582/000117184321000175/ntic20201130_10q.htm",
          "type": "10-Q",
          "size": "1066970"
        },
        {
          "sequence": "2",
          "description": "EXHIBIT 31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ex_219651.htm",
          "type": "EX-31.1",
          "size": "10966"
        },
        {
          "sequence": "3",
          "description": "EXHIBIT 31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ex_219652.htm",
          "type": "EX-31.2",
          "size": "11476"
        },
        {
          "sequence": "4",
          "description": "EXHIBIT 32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ex_219653.htm",
          "type": "EX-32.1",
          "size": "5256"
        },
        {
          "sequence": "5",
          "description": "EXHIBIT 32.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ex_219654.htm",
          "type": "EX-32.2",
          "size": "5043"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/0001171843-21-000175.txt",
          "type": " ",
          "size": "5204733"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ntic-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "55309"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ntic-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "46205"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ntic-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "343347"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ntic-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "303505"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ntic-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "372012"
        },
        {
          "sequence": "11",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/875582/000117184321000175/ntic20201130_10q_htm.xml",
          "type": "XML",
          "size": "754483"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "cfeba6395ee84d94db928be8db82750d",
      "accessionNo": "0001477932-21-000120",
      "cik": "1730869",
      "ticker": "OBTX",
      "companyName": "OBITX, Inc.",
      "companyNameLong": "OBITX, Inc. (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-08T08:47:42-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/0001477932-21-000120.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/0001477932-21-000120-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obitx_10q.htm",
      "entities": [
        {
          "companyName": "OBITX, Inc. (Filer)",
          "cik": "1730869",
          "irsNo": "821091922",
          "stateOfIncorporation": "DE",
          "fiscalYearEnd": "0131",
          "type": "10-Q",
          "act": "34",
          "fileNo": "000-56142",
          "filmNo": "21515805",
          "sic": "7372 Services-Prepackaged Software"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "FORM 10-Q",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obitx_10q.htm",
          "type": "10-Q",
          "size": "489721"
        },
        {
          "sequence": "2",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obitx_ex311.htm",
          "type": "EX-31.1",
          "size": "10942"
        },
        {
          "sequence": "3",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obitx_ex312.htm",
          "type": "EX-31.2",
          "size": "10989"
        },
        {
          "sequence": "4",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obitx_ex321.htm",
          "type": "EX-32.1",
          "size": "5389"
        },
        {
          "sequence": "5",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obitx_ex322.htm",
          "type": "EX-32.2",
          "size": "5467"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/0001477932-21-000120.txt",
          "type": " ",
          "size": "3168033"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obtx-20201031.xml",
          "type": "EX-101.INS",
          "size": "583496"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obtx-20201031.xsd",
          "type": "EX-101.SCH",
          "size": "46259"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obtx-20201031_lab.xml",
          "type": "EX-101.LAB",
          "size": "231149"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obtx-20201031_cal.xml",
          "type": "EX-101.CAL",
          "size": "36606"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obtx-20201031_pre.xml",
          "type": "EX-101.PRE",
          "size": "217478"
        },
        {
          "sequence": "11",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1730869/000147793221000120/obtx-20201031_def.xml",
          "type": "EX-101.DEF",
          "size": "150231"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-10-31",
      "effectivenessDate": "2020-10-31"
    }
  ]
}


import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse

def Find_Company_Name(Dict):
  Company_Names = []
  for k,v in Dict.items():
    if k == 'filings':
      for x in v:
        for k,v in x.items():
          if k == 'entities':
            for x in v:
              for k,v in x.items():
                if k == 'companyName':
                  Company_Names.append(v)

  Amended_Company_Names = []
  for x in Company_Names:
    y = x.split(' ')
    y = y[:-1]
    x = str(' '.join(y))
    if x not in Amended_Company_Names:
      if x != "PRIVATE ASSET MANAGEMENT INC":
        Amended_Company_Names.append(x)
  return(Amended_Company_Names)

# idx_rnd = randint(0, 15)

# Proxies


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
# print(googleSearch("CVS"))      

def Company_Description_Links(Dict):
  '''
  This function takes in a Dictionary, returns a dictionary of the company name and its
  yahoo finance company symbol to be used in yahoo finance searching
  '''
  Company_Names = Find_Company_Name(Dict)
  Link_List = []
  for x in Company_Names:
    y = x + ' '+ "yahoo finance symbol"
    a = googleSearch(y)
    Link_List.append(a)
  
      
  Company_Website_Dict = dict(zip(Company_Names, Link_List))  
  return Company_Website_Dict

# print(Company_Description_Links(B))


# print(googleSearch("Tesla company description"))
# URL = 'https://www.wsj.com/market-data/quotes/JFIL/company-people'
# import requests
# # A = Company_Description_Links(B)
# # Description_List = []
# # for value in A.values():
# #   URL = str(value)

# #   page = requests.get(URL)
# #   Description_List.append(page)
# # print(Description_List)  


# # page = requests.get(URL)
# # print(page)
# # URL = 'https://realpython.com/beautiful-soup-web-scraper-python/'
# # page = requests.get(URL)
# # print(page)

# # So the wall street journal does not allow get requests to their stupid site, we have to replace
# # # all wsj requests with equivalent bloomberg requests
# # import urllib.request

# # wp = urllib.request.urlopen('https://finance.yahoo.com/quote/NVDA/profile/')
# # pw = wp.read()
# # print(pw)


# # page = urllib2.urlopen(URL)

# # soup = BeautifulSoup(page.content, 'html.parser')
# # results = soup.find(id='ResultsContainer')
# # print(results.prettify())

# import pandas as pd
# from bs4 import BeautifulSoup
# URL = 'https://www.reuters.com/companies/JFIL.PK'
# html_text = requests.get(URL).text
# soup = BeautifulSoup(html_text, 'html.parser')
# A = soup.find("div", {"class": "Profile-about-1d-H-"})
# print(A)

# #For reuters, we have a way to directly find the ABOUT info and return it in HTML form
# # Need to find this for each of the different possible websites



# # <div class="Profile-about-1d-H-"

# # from selenium import webdriver
# # import time
# # from bs4 import BeautifulSoup

# # <div class="noMargin__bb878349"><section class="companyProfileOverview__aa874298 down__74925925">
# print('=========')

# URL2= "https://stockanalysis.com/stocks/tinv/"
# html_text = requests.get(URL2).text
# soup = BeautifulSoup(html_text, 'html.parser')
# A = soup.find("div", {"class": "sidew descr"})
# print(A)

# print('-----------')

# # # print(A)
# # <div class="noMargin__bb878349"
# # document.querySelector("#root > div > section > div.noMargin__bb878349 > section > section.info__d075c560 > div")
# URL3 = "https://www.marketwatch.com/investing/stock/jfil"
# html_text = requests.get(URL3).text
# soup = BeautifulSoup(html_text, 'html.parser')
# # B= soup.find("div", {"class": "element element--description "})
# table = soup.find('div',{"class": "element element--description"})
# print(table)
# # print(B)
# print("---------------------")
# <p class="description__text">

# URL4 = "https://www.bloomberg.com/profile/company/TINV/U:US"
# html_text = requests.get(URL4).text
# soup = BeautifulSoup(html_text, 'html.parser')
# # B= soup.find("div", {"class": "element element--description "})
# table = soup.find('div',{"class": "fence-body"})
# print(table)




# # <div class="asset-profile-container full Mb(25px) smartphone_Px(20px)" 
# print(B)
# <div class="asset-profile-container full Mb(25px) smartphone_Px(20px)" data-test="asset-profile">
# <div class="element element--description ">

# <section class="info__d075c560">

# driver = webdriver.Ie(r"C:\Users\JayBeast\Desktop\Selenium\IEDriverServer.exe")
# pd.options.display.float_format = '{:.0f}'.format
# driver.get(url)

# time.sleep(5)
# content = driver.page_source.encode('utf-8').strip()
# soup = BeautifulSoup(content,"html.parser")
# officials = soup.find("div", {"class":"description__ce057c5c"})

# for entry in officials:
#     print(str(entry))


#Create Proxy list
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
        IP_addresses.append(x)
        count+=1  
      
    if count == 16:
      break 
  return(IP_addresses)


import yfinance as yf
from yfinance import Ticker
import json
import matplotlib.pyplot as plt

def get_summary(Stock_Symbol):
  '''
  '''
  Stock_Symbol = Stock_Symbol.upper()
  # if yf.Ticker(Stock_Symbol) == None:
  #   return "Empty"
      
  ticker_nm: Ticker = yf.Ticker(Stock_Symbol)
    
  try:
    x = ticker_nm.info
    for k,v in x.items():
      if k == "longBusinessSummary":
           
        return v

  except Exception as e:
    A = repr(e)
    if A == 'KeyError("regularMarketOpen")':
      return "Empty"
    # print (repr(e))
  
   
    


import random
from collections import Counter
def get_comp_description_Dict(Dict):

  '''
  Takes in an SEC Dictionary, finds the companies venture has invested in,
  Finds the symbols of companies through google search,
  Returns list of company descriptions of given companies through Yahoo Finance
  If description does not exist, does not return description
  Will amend to eventually look elsewhere for those missing descriptions
  '''

  A = Company_Description_Links(Dict)
  
  Websites = []
  for x in A.values():
    if "quote" in x:
      Websites.append(x)
  Symbols = []
  for x in Websites:
    a = x.split('/')
    print(a)
    if '%' not in a[4]:
      Symbols.append(a[4])
    else:
      b = a[4].split('%')
      Symbols.append(b[0])
  print(Symbols)    

  #Symbols is a list of all ticker symbols to be fed into yahoo_finance
  Summary_List = []
  
  for x in Symbols:
    
    desc = get_summary(x)
    rand = random.randint(3,5)
    time.sleep(rand)
    
    if desc != None:
      Summary_List.append(desc)
    elif desc == None:
      a = x.split('-')
      URL = "https://stockanalysis.com/stocks/!/"
      URL2 = URL.replace('!', a[0])
      html_text = requests.get(URL2).text
      soup = BeautifulSoup(html_text, 'html.parser')
      A = soup.find("div", {"class": "sidew descr"})
      B = str(A.find('p'))

      C =re.split(r'(?<=\.) ', B)
      Summary_List.append(C[0])


      
  
  return Summary_List


def Get_General_Classification(Dict, Industry_List):
  '''
  This function will combine parsing the SEC reports and the NLP model
  It will return a general classification of the top 2 industry classifiers for the given list
  '''
  Comp_Info = get_comp_description_Dict(Dict)

  Venture_Classification = []
  for x in Comp_Info:
    xx = find_SEC_branch(x ,Industry_List, model)
    Venture_Classification.append(xx)
  
  Tallies = []
  for x in Venture_Classification:
    for classifier in x:
      if classifier in Industry_List:
        Tallies.append(classifier)

  Counter_Dict = Counter(Tallies)
  tally_list = []
  for v in Counter_Dict.values():
    tally_list.append(v)
  sorted_tallies = sorted(tally_list, reverse=True)
  Classification = []
  for k,v in Counter_Dict.items():
    if v == sorted_tallies[0]:
      Classification.append(k)
    if v == sorted_tallies[1]:
      Classification.append(k)       

  return (Classification)

def Find_Misfiling_CIK(Company:str):
  x = Company + ' ' +  "sec.report CIK"

  Findings = googleSearch(x)
  
  CIK_Findings = []
  CIK_Findings_Edgar = []

  for X in Findings:
    
    if "sec.report/CIK" in X:
      CIK_Findings.append(X)
  
  for X in Findings:
    if "edgar/data" in X:
      CIK_Findings_Edgar.append(X)

  Potential_CIK_Numbers = []
  
  for x in CIK_Findings:
    
    B = x.split('/CIK/')
    C = B[1].split('/')
    Potential_CIK_Numbers.append(C[0])
  for x in CIK_Findings_Edgar:
    B = x.split('data/')
    C = B[1].split('/')


    Potential_CIK_Numbers.append(C[0])
  print(Potential_CIK_Numbers)
  if len(Potential_CIK_Numbers)<1:
    return "non-conclusive"  
  Potential_CIK_Numbers1 = []
  
  for x in Potential_CIK_Numbers:
    if x != "Search":
      y =int(x)
      Potential_CIK_Numbers1.append(y)

  
  D = {x:Potential_CIK_Numbers1.count(x) for x in Potential_CIK_Numbers1}
  Counts = []
  for v in D.values():
    Counts.append(v)
  if max(Counts)>1:
        
    CIK_Key = max(D, key=D.get)
    print(CIK_Key)
    return CIK_Key
  else:
    print("non-conclusive")
    return "non-conclusive"  
# print(Get_General_Classification(B, Industry_Codes))
 

SEC_DICT = {
	"status": "ok",
	"cik_verticals": "successful",
	"investor info": {
		"companyName": "Spectrum Equity Management, Inc. (Filer)",
		"cik": "1657260",
		"irsNo": "043190022",
		"stateOfIncorporation": "DE"
	},
	"holdings": {
		"numberOfHoldingsAnalyzed": 3,
		"totalHoldingsAmount(dollars)": 3243173000,
		"verticals": {
			"7374 Services-Computer Processing & Data Preparation": {
				"totalHoldingsInVertical(dollars)": 112238000,
				"companies": {
					"Nonsense industries inc.": {
						"amountHeld(dollars)": 112238000,
						"cik": "1365038",
						"irsNo": "204731239",
						"stateOfIncorporation": "DE"
					}
				}
			},
			"7370 Services-Computer Programming, Data Processing, Etc.": {
				"totalHoldingsInVertical(dollars)": 454069000,
				"companies": {
					"SVMK Inc": {
						"amountHeld(dollars)": 454069000,
						"cik": "1739936",
						"irsNo": "800765058",
						"stateOfIncorporation": "DE"
					}
				}
			}
		},
		"misfiledHoldingsAmounts": {
			"GoodRx Holdings, Inc.": 2676866000
		}
	}
}
from scholarly import scholarly
from scholarly import ProxyGenerator
from random import randint

# Random Number

#Get Company and amount invested for SEC Filings
def Classify_Investor(SEC_DICTIONARY):
  '''
  Takes in SEC Dictionary, returns a dictionary:
  {Amount_Invested: Company Description, Amount_Invested: Company Description, ...}
  '''


  None_Count = 0
  Misfiled_Holdings = []
  CIK_Numbers = []
  
  Company_List = []
  Invested_Amount = []
  Total_Investment = 0
  list_of_sec_labels = []
  for k,v in SEC_DICTIONARY.items():
    if k == "holdings":
      for k,v in v.items():
        if k == "verticals":
          for k,v in v.items():
            list_of_sec_labels.append(k)
  Counts = []
  for k,v in SEC_DICTIONARY.items():
    if k == "holdings":
      for k,v in v.items():
        if k == "verticals":
          for k,v in v.items():
            for x in list_of_sec_labels:
              if k == x:
                for k,v in v.items():
                  if k == "companies":
                    Counts.append(len(v))

  Default_Label_List = []
  index = 0
  while index<len(Counts):
    a = Counts[index]
    
    while a > 0:
      Default_Label_List.append(list_of_sec_labels[index])
      a -=1 
    index+=1
  
  print(Default_Label_List)
  print(len(Default_Label_List))
          # Have to get a way to count number of companies for each thing in Default DEscription
          #    
          # for values in v.values():
          #   for k,v in values.items():
          #     if k == "companies":
          #       Dict_Len.append(v)
                  
  for x,y in SEC_DICTIONARY.items():
    if x == "holdings":
      for z,q in y.items():
        if z == "totalHoldingsAmount(dollars)":
          Total_Investment += q
          
        elif z == "verticals":
          for values in q.values():
            for k,v in values.items():
              if k == "companies":
                for key, value in v.items():
                  Company_List.append(key)
                  for k,v in value.items():
                    if k == 'amountHeld(dollars)':
                      Invested_Amount.append(v)
        elif z == "misfiledHoldingsAmounts":
          for k,v in q.items():
            Company_List.append(k)
            
            Misfiled_Holdings.append(k)
            Invested_Amount.append(v)
  # print(len(Invested_Amount))
  print(Company_List)
  print(len(Company_List))
  print(Invested_Amount)
  print(len(Invested_Amount))


  # for x in Misfiled_Holdings:
  #   CIK = Find_Misfiling_CIK(x)
  #   rand = random.randint(2,4)
  #   time.sleep(rand)

  #   CIK_Numbers.append(CIK)
  # # for x in CIK_Numbers:
  # #   y = "sec.report" + " " + str(x)
  # #   a = googleSearch(y)
  # #   Potential_Names_List.append(a)
  # # print(Potential_Names_List)  

  # Misfiled_Holdings_Dict = dict(zip(Misfiled_Holdings, CIK_Numbers))
  
  Symbol_List = []
  
  for x in Company_List:
    y = x + ' ' + "yahoo finance symbol"
    a = googleSearch(y)
    Symbol_List.append(a)
    rand = random.randint(2,4)
    time.sleep(rand)


      
  Company_Website_Dict = dict(zip(Company_List, Symbol_List))
  
  Websites = []
  
  for y in Company_Website_Dict.values():
    Individ_Website = []
    for x in y:
      if "quote" in x:
        Individ_Website.append(x)
    Websites.append(Individ_Website)
  
  # print(Websites)       
  Symbols = []
  
  for x in Websites:
    Symbols2 = []
    Symbols3 = []
    
    for y in x:

      a = y.split('/')
    
      if '%' not in a[4]:
        Symbols2.append(a[4])
      
      else:
        b = a[4].split('%')
        Symbols2.append(b[0])
    for x in Symbols2:
      x = x.upper()
      Symbols3.append(x)
    #Symbols3 is a list of symbols for a given company
    #['LUV', 'LUV', 'LUV', 'LUV']
    Counter2 = 0 
    if len(Symbols3) == 0:
      Symbols.append("zzzzzz"+str(Counter2))
      Counter2+=1
      
    if len(Symbols3) > 0:
      symbols4 = Counter(Symbols3)
      A= max(symbols4, key=symbols4.get)

      Symbols.append(A)

                

  print(len(Symbols))
  print(len(Invested_Amount))
    
  Summary_List = []
  
  E = list(enumerate(Symbols))
  
  for symbol in Symbols:
    print(len(Summary_List))
    
    desc = get_summary(symbol)
    
    rand = random.randint(2,5)
    time.sleep(rand)
    
    if desc != None:
      Summary_List.append(desc)
      print(desc)
    
        
    if desc == None:       
      for y in E:
        
        if symbol in y[1]:
          position = y[0]
          print(position)
      if position <= len(Default_Label_List)-1:
          None_Count +=1
          Summary_List.append(Default_Label_List[position])
      elif position > len(Default_Label_List)-1:
        Summary_List.append("Agriculture, Space technology, retail, and clowns")
        Total_Investment -= Invested_Amount[position]
        Invested_Amount[position] = 0
         

          
            #In this case, we want to remove from the Invested_Amount list the amount at this position
  print(Summary_List)
  print(Total_Investment)
  print(Invested_Amount)
  # Amount_Classifier_Dict = dict(zip(Invested_Amount, Summary_List))
  
  Investment_Tallies = [0] * len(Industry_Codes)
  Investment_Dict = dict(zip(Industry_Codes, Investment_Tallies))
  #Investment Dict is going to be a list of industries as keys, and investments as values 
  Industry_List = []
  #Industry list is a list of industries based on company descriptions 
  for x in Summary_List:
    industry = find_SEC_branch(x, Industry_Codes, model)
    print(industry)
    Industry_List.append(industry)
    
  
  #Investment_list has investment amounts, Industry List relates those investment amounts to 
  # Specific industry in the Investment dict, which is then added to value in Investment Dict
  print(Industry_List)
  
  index = 0
  while index <= len(Industry_List)-1:

    sector = Industry_List[index]
    
    for Industry in Investment_Dict.keys():
      if sector == Industry:
        Investment_Dict[Industry] += Invested_Amount[index]
    
    index +=1     
        
  print(Investment_Dict)      
  #Convert to Percentages
  Final_List = []
  Final_List2 = []
  for industry, investment in Investment_Dict.items():
    
    if investment > 0:
      investment = investment/ Total_Investment
      investment = round(investment, 3)
      Final_List.append(industry)
      Final_List2.append(investment)

  Final_Dict = dict(zip(Final_List, Final_List2))  

  print(Total_Investment)
  # return Final_Dict, Misfiled_Holdings_Dict, None_Count
  return Final_Dict
  # return Investment_Dict         

# print(get_summary("lfgr"))
# if get_summary("lfgr") == None:
#   print("hi")
# print(Classify_Investor(SEC_DICT))

with open('aak_test.json') as f:
  Berkshire = json.load(f)
print(Berkshire)  

# print(Classify_Investor(Berkshire))

def Organize_Sec_Dict(Dict):
  '''
  Takes in SEC Dictionary, returns a Dictionary as follows:
  {Vertical:[[CIK, Company, Investment]], Vertical:[[CIK, Company, Investment], [CIK, Company, Investment], etc], etc}
  Misfiled_Holding_Dictionary: {Misfiled_Company: Investment, Misfiled_Company: Investment, etc}
  '''


  
  Invested_Amount = []
  CIK_Numbers = []
  
  list_of_sec_labels = []
  for k,v in Dict.items():
    if k == "holdings":
      for k,v in v.items():
        if k == "verticals":
          for k,v in v.items():
            list_of_sec_labels.append(k)
        elif k == "misfiledHoldingsAmounts":
          Misfiled_Dict = v     
  Counts = []
  Companies = []
  for k,v in Dict.items():
    if k == "holdings":
      for k,v in v.items():
        if k == "verticals":
          for k,v in v.items():
            for x in list_of_sec_labels:
              if k == x:
                for k,v in v.items():
                  if k == "companies":
                    Counts.append(len(v))
                                  
                    for a,b in v.items():
                      Companies.append(a)
                      for k,v in b.items():
                        if k == 'amountHeld(dollars)':
                          Invested_Amount.append(str(v))
                        if k == 'cik':
                          CIK_Numbers.append(v)  

                      
                      
                      

  Default_Label_List = []
  index = 0
  while index<len(Counts):
    a = Counts[index]
    
    while a > 0:
      Default_Label_List.append(list_of_sec_labels[index])
      a -=1 
    index+=1

  vertical_dict = dict(zip(Companies, Default_Label_List))


  Vertical_List = []  
  for x in Default_Label_List:
    if x not in Vertical_List:
      Vertical_List.append(x)

  Vertical_List_of_Lists = []
  for x in Vertical_List:
    Individ_List = []
    for y in Default_Label_List:
      if y ==x:
        Individ_List.append(y)
    Vertical_List_of_Lists.append(Individ_List)

  List_of_Name_Lists = []
  for x in Vertical_List_of_Lists:
    Name_List = []
    for y in x:
      for k,v in vertical_dict.items():
        if v == y:
          if k not in Name_List:
            Name_List.append(k)
    List_of_Name_Lists.append(Name_List)
  Verticals = []
  for x in Vertical_List_of_Lists:
    for y in x:
      if y not in Verticals:
        Verticals.append(y)
  
  Company_Investment = [', '.join(x) for x in zip(Companies, Invested_Amount)]

  CIK_Dict = dict(zip(CIK_Numbers, Company_Investment))


  CIK_Combined_List = []
  for k,v in CIK_Dict.items():
    combined = []
    combined.append(k)
    combined.append(v)
    CIK_Combined_List.append(combined)

  Final_Final_List = []
  for x in List_of_Name_Lists:
    Final_Combined_List = []
    for y in x:
      
      for a in CIK_Combined_List:
        for b in a:
          if y in b:
            Final_Combined_List.append(a)
    Final_Final_List.append(Final_Combined_List)

  Vertical_Final_Dict = dict(zip(Verticals, Final_Final_List))
  return Vertical_Final_Dict, Misfiled_Dict
  

print(Organize_Sec_Dict(Berkshire))  











                


                       
          










          

                        