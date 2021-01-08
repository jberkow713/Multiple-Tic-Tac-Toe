from NLPModels import *

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

Type_Classifier = ["Goal", "Enforcement", "Writing, Communication", "Research, Analysis",\
    "Consulting", "Management", 'Client', 'Process improving', 'Growth Boosting', 'Efficiency',\
        'Leadership']

#Goal is to analyze a resume, figure out which of the list of keywords has highest value upon resume
# We're going to use the NLPModel from SEC to start

Lst_Types = [Goal_Oriented_Keywords, Management_Enforcement_Keywords, Writing_Communication_Keywords,\
    Research_Analysis_Keywords, Consulting_Keywords, Management_Keywords, Client_Based_Keywords, \
        Process_Improving_Keywords, Growth_Boosting_Keywords, Efficiency_Keywords,\
            Leadership_Keywords]
# print(Lst_Types[0])

Classifier_Dict = dict(zip(Type_Classifier, Lst_Types))
 
HR = "Human resources specialists are responsible for recruiting, screening, interviewing and placing workers. They may also handle employee relations, payroll, benefits, and training. Human resources managers plan, direct and coordinate the administrative functions of an organization."    
B = "work with organisations to help them improve their processes and systems. They conduct research and analysis in order to come up with solutions to business problems and help to introduce these systems to businesses and their clients."
# A = find_SEC_branch(B, Type_Classifier, model)
# print(get_relevant_sentence_desc(B))
# print(A)

def Find_Useful_Keywords(Description, Keyword_List, model):
    A = find_SEC_branch(Description, Keyword_List, model)
    Keywords = []
    for x in A[2]:
        for k,v in Classifier_Dict.items():
            if x == k:
                for x in v:
                    x = x.lower()
                    Keywords.append(x)
    return Keywords

C = Find_Useful_Keywords(HR, Type_Classifier, model)
print(C)    

