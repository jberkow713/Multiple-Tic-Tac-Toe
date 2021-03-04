from NLPModels import *
from bs4 import BeautifulSoup
import requests

Leadership_Keywords = ['haired','Controlled','Coordinated','Executed','Headed','Operated','Orchestrated',\
    'Organized','Oversaw','Planned','Produced','Programmed']

Creation_Keywords = ['Administered','Built','Charted','Created','Designed','Developed','Devised',\
    'Founded', 'Engineered','Established', 'Formalized','Formed','Formulated','Implemented',\
        'Incorporated','Initiated','Instituted','Introduced','Launched','Pioneered','Spearheaded']

Efficiency_Keywords = ['Conserved','Consolidated','Decreased','Deducted','Diagnosed','Lessened',\
    'Reconciled','Reduced','Yielded']


Growth_Boosting_Keywords = ['Accelerated','Achieved','Advanced','Amplified','Boosted','Capitalized',\
    'Delivered','Enhanced','Expanded','Expedited','Furthered','Gained','Generated','Improved',\
        'Lifted','Maximized','Outpaced','Stimulated','Sustained']


Process_Improving_Keywords = ['Centralized','Clarified','Converted','Customized','Influenced',\
    'Integrated','Merged','Modified','Overhauled','Redesigned','Refined','Refocused','Rehabilitated',\
        'Remodeled','Reorganized','Replaced','Restructured','Revamped','Revitalized','Simplified',\
            'Standardized','Streamlined','Strengthened','Updated','Upgraded','Transformed']


Management_Keywords = ['Aligned','Cultivated','Directed','Enabled','Facilitated','Fostered','Guided',\
    'Hired','Inspired','Mentored','Mobilized','Motivated','Recruited','Regulated','Shaped','Supervised',\
        'Taught','Trained','Unified','United']


Client_Based_Keywords = ['Acquired','Forged','Navigated','Negotiated','Partnered','Secured']


Consulting_Keywords = ['Advised','Advocated','Arbitrated','Coached','Consulted','Educated'\
    'Fielded','Informed','Resolved']


Research_Analysis_Keywords = ['Analyzed','Assembled','Assessed','Audited','Calculated','Discovered',\
    'Evaluated','Examined','Explored','Forecasted','Identified','Interpreted','Investigated',\
        'Mapped','Measured','Qualified','Quantified','Surveyed','Tested','Tracked']


Writing_Communication_Keywords = ['Authored','Briefed','Campaigned','Co-authored','Composed','Conveyed',\
    'Convinced','Corresponded','Counseled','Critiqued','Defined','Documented','Edited','Illustrated',\
        'Lobbied','Persuaded','Promoted','Publicized','Reviewed']


Management_Enforcement_Keywords = ['Authorized','Blocked','Delegated','Dispatched','Enforced','Ensured',\
    'Inspected','Itemized','Monitored','Screened','Scrutinized','Verified']


Goal_Oriented_Keywords = ['Attained','Awarded','Completed','Demonstrated','Earned','Exceeded','Outperformed',\
    'Reached','Showcased','Succeeded','Surpassed','Targeted']

Type_Classifier = ["Goal", "Enforcement", "Writing, Communication", "Research",\
    "Consulting", "Delegation", 'Client', 'Method, Process', 'Growth', 'Efficiency',\
        'Leadership']

#Goal is to analyze a resume, figure out which of the list of keywords has highest value upon resume
# We're going to use the NLPModel from SEC to start

Lst_Types = [Goal_Oriented_Keywords, Management_Enforcement_Keywords, Writing_Communication_Keywords,\
    Research_Analysis_Keywords, Consulting_Keywords, Management_Keywords, Client_Based_Keywords, \
        Process_Improving_Keywords, Growth_Boosting_Keywords, Efficiency_Keywords,\
            Leadership_Keywords]
# print(Lst_Types[0])

Classifier_Dict = dict(zip(Type_Classifier, Lst_Types))
# print(Classifier_Dict) 
HR = "Human resources specialists are responsible for recruiting, screening, interviewing and placing workers. They may also handle employee relations, payroll, benefits, and training. Human resources managers plan, direct and coordinate the administrative functions of an organization."    
B = "work with organisations to help them improve their processes and systems. They conduct research and analysis in order to come up with solutions to business problems and help to introduce these systems to businesses and their clients."
# A = find_SEC_branch(B, Type_Classifier, model)
# print(get_relevant_sentence_desc(B))
# print(A)

def Find_Useful_Keywords(Description, Keyword_List, model):
    A = find_SEC_branch(Description, Keyword_List, model)
    # print(A)
    Keywords = []
    for x in A:
        for k,v in Classifier_Dict.items():
            if x == k:
                Keywords.append(v)

    return Keywords       
    

C = Find_Useful_Keywords(HR, Type_Classifier, model)
print(C)
# A = find_SEC_branch(HR, Type_Classifier, model)
# for x in A:
#     for k,v in Classifier_Dict.items():
#         if x == k:
#             print(v)

#C represents a list of useful words to put in resume, based on the classification of the job description
# B is a job description, Classify B, find keywords, and now need to put these words into resume
# So we should look for a way to substitute words in existing resume, with these words, if they are synonyms
#    
# For each word in the Find_Useful_Keywords list, we want to scan over the resume, and check if a word in 
# the resume, is a synonm of one of these words



# URL2= "https://www.google.com/search?sxsrf=ALeKk01TsfW8FLlKYw0zfL_6rMgE6LvPQQ:1610117081689&ei=2W_4X4-sKce05NoP7cWagA8&q=finance+jobs+boston&oq=finance+jobs+boston&gs_lcp=CgZwc3ktYWIQAzIFCAAQyQMyAggAMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoFCAAQkQI6CAgAELEDEJECOggIABCxAxDJAzoFCAAQkgM6CAgAELEDEIMBOgQIABAKUL-gpgFYy7OmAWDJtKYBaABwAXgCgAGHA4gB_QuSAQc4LjEuMS4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&uact=5&ibp=htl;jobs&sa=X&ved=2ahUKEwiZsbjZ04zuAhXxFVkFHXepDZ8Qkd0GMAB6BAgHEAE#fpstate=tldetail&htivrt=jobs&htiq=finance+jobs+boston&htidocid=rHpxlL7RYsjC_ZmdAAAAAA%3D%3D&sxsrf=ALeKk03IAFeEKBKBhBIA6vnOBiOf9rAkTQ:1610119807653"
# html_text = requests.get(URL2).text
# soup = BeautifulSoup(html_text, 'html.parser')
# # <div class="YgLbBe">
# A = soup.find("div", {"class": "HBvzbc"})
# print(A)

# # <span class="HBvzbc" 

A = '''
The Public Service Commission of the District of Columbia (Commission), a leading utility regulatory agency, is looking for a talented Economist with utility or regulatory experience, who can make a professional difference in the Nation’s Capital. As an Economist, you will be involved in a challenging variety of utility regulatory projects, including: electric and gas rate design issues, ongoing economic analysis and monitoring efforts for electric and gas utility rate increase applications and multi-billion dollar projects of infrastructure upgrades, electric and gas distribution strategic initiatives, as well as distributed energy resource (DER) programs, including demand response, renewable energy sources, energy storage, microgrids, energy efficiency, etc.

In this role, you will have an opportunity to interface with key stakeholders from federal and state agencies, including other state public service commissions, FERC, DOE, and the credit rating agencies. You will also interface with professionals of Fortune 500 energy companies, energy developers and providers, as well as regulatory professionals from across the Nation. You will have opportunities to gain significant industry exposure and unmatched professional experience as a member of a leading regulatory agency with a proud 100+ year history of regulatory excellence.

This position is in the Office of Economics within the Office of Technical and Regulatory Analysis (OTRA) of the Commission. The Commission regulates the utilities and competitive companies that provide natural gas, electricity, and telecommunications services to District of Columbia ratepayers. The mission of the Commission is to serve the public interest by ensuring that financially healthy utilities provide safe, reliable and quality utility services at reasonable rates for District customers, while fostering grid modernization, conservation of natural resources, preservation of environmental quality, and advancement of the District's climate policy goals. OTRA advises the Commissioners on economic, accounting/financial, engineering, and compliance/enforcement issues in formal cases.

The economist performs economic and market-oriented studies related to the restructured natural gas, and electric industries in the District of Columbia. He/she will perform economic analyses of issues in gas and electric rate cases and other regulatory proceedings. Assist in preparing technical memoranda to the Commissioners in formal cases and other proceedings. Assist in analyzing and monitoring industry data and studies. Review tariffs and other filings to test economic foundation and compliance with Commission orders. The economist will assist in clean energy-related efforts, including implementation actions arising from the Clean Energy DC Act, and attending working groups in various proceedings. The economist will prepare working group meeting minutes, as assigned.

The economist will assist in analyzing and critiquing industry data and studies. Review submissions received from utility companies and intervenors in formal cases, investigations, and filings. Monitor company compliance with Commission-ordered requirements in formal cases.

Performs economic reviews, analyses, and research of Renewable Portfolio Standards (RPS) related issues. The economist will assist in the weekly processing of D.C. Renewable Energy Credit applications, collecting information on renewable resources and assisting in implementation of RPS rules and related legislation.

The Commission offers a competitive salary range, a generous travel stipend for public transportation, as well as an attractive benefits package. The Commission's benefits package encompasses a flexible menu of comprehensive benefits, including health, dental, vision, life and disability insurance options, as well as a strong set of portable retirement benefits and savings options. The Commission also offers attractive vacation and sick leave time, as well as paid holidays, consistent with District government provisions.

The Commission also seeks to optimize work-life balance through an attractive set of work schedule options, including: Flex time schedules, Teleworking options, and Alternative Work Schedules, available to employees after a probationary period. As an organization dedicated to professional development and learning, the Commission encourages staff to participate in regulatory and industry association activities, as well as educational and professional training. Tuition reimbursement may also be available.

Qualifications

Professional knowledge of concepts, methods and techniques sufficient to provide technical consultations and assistance as necessary to promote enhanced economic advisory services information. Knowledge of and skill in the application of analytical and evaluative concepts, methods, techniques, and practices as needed in the review of regulatory filings such as Commission orders, FERC orders, and proposed rulemakings by state and federal administrative authorities. Knowledge of utility restructuring, market power, mergers and acquisitions, cost of service, rate design and other utility industry issues. Knowledge of Commission rules, practices, and regulations. Knowledge and skill in econometrics and use of database programs, statistical programs, spreadsheet programs, and word processing programs. Ability to identify and evaluate economic issues from complex factual situations. Research skills necessary in communicating precisely and effectively, both orally and in writing.

Collective Bargaining Unit

This position is in the collective bargaining unit represented by AFSCME, District Council 20, and you may elect to join the union.

Education

Graduation from an accredited college or university with a bachelor’s degree in economics or related field with significant economics course work.

Work Experience

1-2 years of public utility experience in a regulatory agency or utility environment with respect to economics is preferred (internships and research programs included). Experience in economic analysis related to renewable energy and distributed energy resources is also desired.

Work Environment

The work is performed in an office setting.


'''
# B = find_SEC_branch(A, Type_Classifier, model)
# print(B)
# print(get_relevant_sentence_desc(A))
# C = Find_Useful_Keywords(A, Type_Classifier, model)
# print(C)

Words = ['analyzed', 'assembled', 'assessed', 'audited', 'calculated', 'discovered', 'evaluated', 'examined', 'explored', 'forecasted', 'identified', 'interpreted', 'investigated', 'mapped', 'measured', 'qualified', 'quantified', 'surveyed', 'tested', 'tracked', 'authored', 'briefed', 'campaigned', 'co-authored', 'composed', 'conveyed', 'convinced', 'corresponded', 'counseled', 'critiqued', 'defined', 'documented', 'edited', 'illustrated', 'lobbied', 'persuaded', 'promoted', 'publicized', 'reviewed', 'centralized', 'clarified', 'converted', 'customized', 'influenced', 'integrated', 'merged', 'modified', 'overhauled', 'redesigned', 'refined', 'refocused', 'rehabilitated', 'remodeled', 'reorganized', 'replaced', 'restructured', 'revamped', 'revitalized', 'simplified', 'standardized', 'streamlined', 'strengthened', 'updated', 'upgraded', 'transformed']


# from pyresparser import ResumeParser
# data = ResumeParser(r'C:/Users/JayBeast/Desktop/JesseBerkowitz-Resume.pdf').get_extracted_data()
# Experience_List = []
# for k,v in data.items():
#     if k == "experience":
#         Experience_List.append(v)
# for x in Experience_List:
#     print(x)       
