from googlesearch import search

#goal is to create function that parses this and returns a list of company names:
#The get_13F function returns a dictionary

# We can then parse the dictionary with this function, to return all of the names of the companies
# Which the venture company has invested in 


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
    "size": 5
  },
  "filings": [
    {
      "id": "7f0f4bef0462d7deba0f0a9c210eef17",
      "accessionNo": "0001558370-21-000043",
      "cik": "84129",
      "ticker": "RAD",
      "companyName": "RITE AID CORP",
      "companyNameLong": "RITE AID CORP (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-06T13:21:11-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/0001558370-21-000043.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/0001558370-21-000043-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128x10q.htm",
      "entities": [
        {
          "companyName": "RITE AID CORP (Filer)",
          "cik": "84129",
          "irsNo": "231614034",
          "stateOfIncorporation": "DE",
          "fiscalYearEnd": "0227",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-05742",
          "filmNo": "21509809",
          "sic": "5912 Retail-Drug Stores and Proprietary Stores"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/84129/000155837021000043/rad-20201128x10q.htm",
          "type": "10-Q",
          "size": "3482254"
        },
        {
          "sequence": "2",
          "description": "EX-22",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128xex22.htm",
          "type": "EX-22",
          "size": "55534"
        },
        {
          "sequence": "3",
          "description": "EX-31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128xex31d1.htm",
          "type": "EX-31.1",
          "size": "11353"
        },
        {
          "sequence": "4",
          "description": "EX-31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128xex31d2.htm",
          "type": "EX-31.2",
          "size": "11958"
        },
        {
          "sequence": "5",
          "description": "EX-32",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128xex32.htm",
          "type": "EX-32",
          "size": "9740"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/0001558370-21-000043.txt",
          "type": " ",
          "size": "13922672"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "EX-101.SCH",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128.xsd",
          "type": "EX-101.SCH",
          "size": "70854"
        },
        {
          "sequence": "7",
          "description": "EX-101.CAL",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128_cal.xml",
          "type": "EX-101.CAL",
          "size": "111725"
        },
        {
          "sequence": "8",
          "description": "EX-101.DEF",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128_def.xml",
          "type": "EX-101.DEF",
          "size": "275802"
        },
        {
          "sequence": "9",
          "description": "EX-101.LAB",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128_lab.xml",
          "type": "EX-101.LAB",
          "size": "688943"
        },
        {
          "sequence": "10",
          "description": "EX-101.PRE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128_pre.xml",
          "type": "EX-101.PRE",
          "size": "528958"
        },
        {
          "sequence": "11",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/84129/000155837021000043/rad-20201128x10q_htm.xml",
          "type": "XML",
          "size": "3154466"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-28",
      "effectivenessDate": "2020-11-28"
    },
    {
      "id": "fe65438f11236353eb781e137076ecf1",
      "accessionNo": "0001140361-21-000322",
      "cik": "1820144",
      "ticker": "TINV",
      "companyName": "Tiga Acquisition Corp.",
      "companyNameLong": "Tiga Acquisition Corp. (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-06T13:00:38-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/0001140361-21-000322.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/0001140361-21-000322-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/brhc10018625_10q.htm",
      "entities": [
        {
          "companyName": "Tiga Acquisition Corp. (Filer)",
          "cik": "1820144",
          "irsNo": "000000000",
          "stateOfIncorporation": "E9",
          "fiscalYearEnd": "1231",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-39714",
          "filmNo": "21509728",
          "sic": "6770 Blank Checks"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/brhc10018625_10q.htm",
          "type": "10-Q",
          "size": "249226"
        },
        {
          "sequence": "2",
          "description": "EXHIBIT 31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/brhc10018625_ex31-1.htm",
          "type": "EX-31.1",
          "size": "13920"
        },
        {
          "sequence": "3",
          "description": "EXHIBIT 31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/brhc10018625_ex31-2.htm",
          "type": "EX-31.2",
          "size": "12636"
        },
        {
          "sequence": "4",
          "description": "EXHIBIT 32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/brhc10018625_ex32-1.htm",
          "type": "EX-32.1",
          "size": "5634"
        },
        {
          "sequence": "5",
          "description": "EXHIBIT 32.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/brhc10018625_ex32-2.htm",
          "type": "EX-32.2",
          "size": "5093"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/0001140361-21-000322.txt",
          "type": " ",
          "size": "2171286"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/tinv-20200930.xml",
          "type": "EX-101.INS",
          "size": "200281"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/tinv-20200930.xsd",
          "type": "EX-101.SCH",
          "size": "32148"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/tinv-20200930_cal.xml",
          "type": "EX-101.CAL",
          "size": "13387"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/tinv-20200930_def.xml",
          "type": "EX-101.DEF",
          "size": "213082"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/tinv-20200930_lab.xml",
          "type": "EX-101.LAB",
          "size": "316102"
        },
        {
          "sequence": "11",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1820144/000114036121000322/tinv-20200930_pre.xml",
          "type": "EX-101.PRE",
          "size": "247283"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-09-30",
      "effectivenessDate": "2020-09-30"
    },
    {
      "id": "7a5ab1a5a0d37c761c0c3b2dac186891",
      "accessionNo": "0001564590-21-000354",
      "cik": "33002",
      "ticker": "EBF",
      "companyName": "ENNIS, INC.",
      "companyNameLong": "ENNIS, INC. (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-06T11:48:33-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/0001564590-21-000354.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/0001564590-21-000354-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-10q_20201130.htm",
      "entities": [
        {
          "companyName": "ENNIS, INC. (Filer)",
          "cik": "33002",
          "irsNo": "750256410",
          "stateOfIncorporation": "TX",
          "fiscalYearEnd": "0228",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-05807",
          "filmNo": "21509540",
          "sic": "2761 Manifold Business Forms"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/33002/000156459021000354/ebf-10q_20201130.htm",
          "type": "10-Q",
          "size": "2243969"
        },
        {
          "sequence": "2",
          "description": "EX-31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-ex311_7.htm",
          "type": "EX-31.1",
          "size": "16163"
        },
        {
          "sequence": "3",
          "description": "EX-31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-ex312_8.htm",
          "type": "EX-31.2",
          "size": "16204"
        },
        {
          "sequence": "4",
          "description": "EX-32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-ex321_9.htm",
          "type": "EX-32.1",
          "size": "6723"
        },
        {
          "sequence": "5",
          "description": "EX-32.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-ex322_6.htm",
          "type": "EX-32.2",
          "size": "6794"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/0001564590-21-000354.txt",
          "type": " ",
          "size": "7806976"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "45530"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "71574"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "121576"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "367590"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "289158"
        },
        {
          "sequence": "11",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/33002/000156459021000354/ebf-10q_20201130_htm.xml",
          "type": "XML",
          "size": "1487173"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "0e08a2ba15eb92aa139949ec6466c5db",
      "accessionNo": "0001477932-21-000050",
      "cik": "1517389",
      "ticker": "JFIL",
      "companyName": "Jubilant Flame International, Ltd",
      "companyNameLong": "Jubilant Flame International, Ltd (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-06T10:16:56-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/0001477932-21-000050.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/0001477932-21-000050-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil_10q.htm",
      "entities": [
        {
          "companyName": "Jubilant Flame International, Ltd (Filer)",
          "cik": "1517389",
          "irsNo": "272775885",
          "stateOfIncorporation": "NV",
          "fiscalYearEnd": "0228",
          "type": "10-Q",
          "act": "34",
          "fileNo": "000-55543",
          "filmNo": "21509320",
          "sic": "7371 Services-Computer Programming Services"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "FORM 10-Q",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil_10q.htm",
          "type": "10-Q",
          "size": "261163"
        },
        {
          "sequence": "2",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil_ex311.htm",
          "type": "EX-31.1",
          "size": "10975"
        },
        {
          "sequence": "3",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil_ex312.htm",
          "type": "EX-31.2",
          "size": "10632"
        },
        {
          "sequence": "4",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil_ex321.htm",
          "type": "EX-32.1",
          "size": "4295"
        },
        {
          "sequence": "5",
          "description": "CERTIFICATION",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil_ex322.htm",
          "type": "EX-32.2",
          "size": "4316"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/0001477932-21-000050.txt",
          "type": " ",
          "size": "993017"
        }
      ],
      "dataFiles": [
        {
          "sequence": "6",
          "description": "XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil-20201130.xml",
          "type": "EX-101.INS",
          "size": "74728"
        },
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "15282"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "90330"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "22281"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "73871"
        },
        {
          "sequence": "11",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1517389/000147793221000050/jfil-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "28634"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    },
    {
      "id": "8398dd7730ce727993390c0469120523",
      "accessionNo": "0001170010-21-000003",
      "cik": "1170010",
      "ticker": "KMX",
      "companyName": "CARMAX INC",
      "companyNameLong": "CARMAX INC (Filer)",
      "formType": "10-Q",
      "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
      "filedAt": "2021-01-06T10:01:52-05:00",
      "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/0001170010-21-000003.txt",
      "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/0001170010-21-000003-index.htm",
      "linkToXbrl": "",
      "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130.htm",
      "entities": [
        {
          "companyName": "CARMAX INC (Filer)",
          "cik": "1170010",
          "irsNo": "541821055",
          "stateOfIncorporation": "VA",
          "fiscalYearEnd": "0228",
          "type": "10-Q",
          "act": "34",
          "fileNo": "001-31420",
          "filmNo": "21509305",
          "sic": "5500 Retail-Auto Dealers &amp; Gasoline Stations"
        }
      ],
      "documentFormatFiles": [
        {
          "sequence": "1",
          "description": "10-Q",
          "documentUrl": "https://www.sec.gov/ix?doc=/Archives/edgar/data/1170010/000117001021000003/kmx-20201130.htm",
          "type": "10-Q",
          "size": "2288307"
        },
        {
          "sequence": "2",
          "description": "EX-10.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/exhibit101-consultingagree.htm",
          "type": "EX-10.1",
          "size": "40633"
        },
        {
          "sequence": "3",
          "description": "EX-31.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/q3fy21ex311.htm",
          "type": "EX-31.1",
          "size": "10244"
        },
        {
          "sequence": "4",
          "description": "EX-31.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/q3fy21ex312.htm",
          "type": "EX-31.2",
          "size": "10173"
        },
        {
          "sequence": "5",
          "description": "EX-32.1",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/q3fy21ex321.htm",
          "type": "EX-32.1",
          "size": "6660"
        },
        {
          "sequence": "6",
          "description": "EX-32.2",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/q3fy21ex322.htm",
          "type": "EX-32.2",
          "size": "7402"
        },
        {
          "sequence": "12",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_g1.jpg",
          "type": "GRAPHIC",
          "size": "30546"
        },
        {
          "sequence": "13",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_g2.jpg",
          "type": "GRAPHIC",
          "size": "21894"
        },
        {
          "sequence": "14",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_g3.jpg",
          "type": "GRAPHIC",
          "size": "39542"
        },
        {
          "sequence": "15",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_g4.jpg",
          "type": "GRAPHIC",
          "size": "20911"
        },
        {
          "sequence": " ",
          "description": "Complete submission text file",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/0001170010-21-000003.txt",
          "type": " ",
          "size": "10065247"
        }
      ],
      "dataFiles": [
        {
          "sequence": "7",
          "description": "XBRL TAXONOMY EXTENSION SCHEMA DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130.xsd",
          "type": "EX-101.SCH",
          "size": "59449"
        },
        {
          "sequence": "8",
          "description": "XBRL TAXONOMY EXTENSION CALCULATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_cal.xml",
          "type": "EX-101.CAL",
          "size": "89943"
        },
        {
          "sequence": "9",
          "description": "XBRL TAXONOMY EXTENSION DEFINITION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_def.xml",
          "type": "EX-101.DEF",
          "size": "332795"
        },
        {
          "sequence": "10",
          "description": "XBRL TAXONOMY EXTENSION LABEL LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_lab.xml",
          "type": "EX-101.LAB",
          "size": "685980"
        },
        {
          "sequence": "11",
          "description": "XBRL TAXONOMY EXTENSION PRESENTATION LINKBASE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_pre.xml",
          "type": "EX-101.PRE",
          "size": "466424"
        },
        {
          "sequence": "16",
          "description": "EXTRACTED XBRL INSTANCE DOCUMENT",
          "documentUrl": "https://www.sec.gov/Archives/edgar/data/1170010/000117001021000003/kmx-20201130_htm.xml",
          "type": "XML",
          "size": "2023407"
        }
      ],
      "seriesAndClassesContractsInformation": [],
      "periodOfReport": "2020-11-30",
      "effectivenessDate": "2020-11-30"
    }
  ]
}


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
      return g_clean[0]
# print(googleSearch("CVS"))      

def Company_Description_Links(Dict):
  '''
  This function takes in a Dictionary, returns a dictionary of the company name and its
  yahoo finance company symbol to be used in yahoo finance searching
  '''
  Company_Names = Find_Company_Name(Dict)
  lst = []
  for x in Company_Names:
    y = x + ' '+ "yahoo finance stock symbol"
    lst.append(y)
  Link_List = []
  
  for x in lst:
    a = googleSearch(x)
   
    Link_List.append(a)
          # break
    
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



import yfinance as yf
from yfinance import Ticker
import json
import matplotlib.pyplot as plt

def get_summary(Stock_Symbol):
  ticker_nm: Ticker = yf.Ticker(Stock_Symbol)

  x = ticker_nm.info
  for k,v in x.items():
    if k == "longBusinessSummary":
      return(v)

# print(get_summary("kmx"))      

# def get_comp_description_Dict(Dict):

#   A = Company_Description_Links(Dict)
#   Websites = []
#   for x in A.values():
#     Websites.append(x)

def get_comp_description_Dict(Dict):

  A = Company_Description_Links(Dict)
  Websites = []
  for x in A.values():
    Websites.append(x)
  Symbols = []
  for x in Websites:
    a = x.split('/')
    if '%' not in a[-2]:
      Symbols.append(a[-2])
    else:
      b = a[-2].split('%')
      Symbols.append(b[0])

  #Symbols is a list of all ticker symbols to be fed into yahoo_finance
  Summary_List = []
  for x in Symbols:
    desc = get_summary(x)
    if desc != None:
      Summary_List.append(desc)
  
  return Summary_List

# print(get_comp_description_Dict(B)) 
# print(get_summary('TINV-UN'))    