#The idea is to get keywords used in resume analysis when it comes to how employers filter 
#What we want to do , is for a given job description, we want to create a model that can figure out 
# the main theme or themese of the given article

#So we can use the same type of analysis in NLPModels, to take in a given description, and have it filter
# into the below categories:

#Leadership, Creation, Efficiency, Growth_Boosting, Process_Improving, Management, 
#Client_Based, Consulting, Research Analysis, Writing/Communication, 
#Management_Enforcement, and Goal Oriented

#We call the above the main topic list, and basically write an SEC classification function, only 
#instead using job topics

#with company description, they were generally a paragraph long, we want to filter a page or so job 
#description, and turn it into 5-10 different paragraphs/sentences, and then judge each one accordingly
#Figuring out how to parse the resume and turn it into a topic, or several topics is one of the main 
#objectives for this project...but once we do this, we can compare these to the categories listed above




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