from typing import Text
import tweepy
from tweepy import Stream
from collections import Counter
from streamtesting3 import Tesla
import datetime
from datetime import datetime


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
def find_time_windows(list_of_times, window_length, sec=True):
    if sec == False:
        window_length = window_length*60

    length = len(list_of_times)
    
    index = 1
    list_of_windows = []
    mini_list = []
    

    while length >1:              
        
        starting_time = list_of_times[0]  
        
        time = list_of_times[index]        
       
        difference = time-starting_time
        
        if difference <= window_length:
            mini_list.append(time)
                    
            index +=1
            

            
        if difference > window_length:
            mini_list.insert(0,starting_time)
            
            list_of_windows.append(mini_list)
            
            for _ in range(index):
                list_of_times.remove(list_of_times[0])
               
            index = 1
            mini_list = []
        
        length -=1
        if length ==1:
            
            mini_list.insert(0,starting_time)
            
            list_of_windows.append(mini_list)

        # print(len(list_of_times), index)
    return list_of_windows 




class TweetParser():
    def __init__(self, Dict_List):
        self.Dict_List = Dict_List
        self.textlist = self.createtext()
        self.Hashtags = []
        self.Callouts = []
        self.create_Hashtags_and_Callouts()
        self.keys = ['in_reply_to_user_id_str', 'in_reply_to_user_id', 'timestamp_ms', 'coordinates', \
            'favorite_count', 'lang', 'possibly_sensitive', 'extended_entities', 'user', 'retweet_count',\
                 'truncated', 'place', 'retweeted', 'quoted_status_id', 'text', 'is_quote_status', 'extended_tweet',\
                      'retweeted_status', 'created_at', 'quoted_status_permalink', 'filter_level', 'id_str', 'geo',\
                           'id', 'entities', 'reply_count', 'quoted_status', 'contributors', 'display_text_range',\
                                'quoted_status_id_str', 'in_reply_to_status_id_str', 'in_reply_to_status_id', 'source',\
                                     'quote_count', 'favorited', 'in_reply_to_screen_name']
        self.user_keys = ['id', 'id_str', 'name', 'screen_name', 'location', 'url', 'description', \
            'translator_type', 'protected', 'verified', 'followers_count', 'friends_count', 'listed_count', \
                'favourites_count', 'statuses_count', 'created_at', 'utc_offset', 'time_zone', 'geo_enabled', \
                    'lang', 'contributors_enabled', 'is_translator', 'profile_background_color', 'profile_background_image_url', \
                        'profile_background_image_url_https', 'profile_background_tile', 'profile_link_color', \
                            'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color',\
                                 'profile_use_background_image', 'profile_image_url', 'profile_image_url_https',\
                                      'profile_banner_url', 'default_profile', 'default_profile_image', 'following',\
                                           'follow_request_sent', 'notifications', 'withheld_in_countries']
    def createtext(self):
        Text = []
        for x in self.Dict_List:
            for k,v in x.items():
                if k =='text':
                    Text.append(v)
        return Text            
    def create_Hashtags_and_Callouts(self):
        for x in self.textlist:
            b = x.split()
            for a in b:
                if '#' in a:
                    self.Hashtags.append(a)
                elif '@' in a:
                    self.Callouts.append(a)
    
    def find_top_keys(self, List, num_keys):
        DICT = Counter(List)
        vals = []

        for val in DICT.values():
            vals.append(val)
        vals = sorted(vals, reverse=True)
        
        top_vals = []
        index = 0

        while num_keys >0:
            val = vals[index]
            top_vals.append(val)
            index +=1
            num_keys -=1
        
        top_keys = []
                
        for x in top_vals:
            for k,v in DICT.items():
                if x == v:
                    top_keys.append(k)
                    Copy_Dict = removekey(DICT, k)
                    DICT = Copy_Dict        
        
        top_dict = dict(zip(top_keys, top_vals))
        return top_dict
    def create_list(self, key):
        LIST = []
        for x in self.Dict_List:
            for k,v in x.items():
                if k ==key:
                    LIST.append(v)
        return LIST  
    def find_most_active_users(self, num):
        A = self.create_list('user')
        list = []
        for x in A:
            b = (x['screen_name'])
            list.append(b)
        B = self.find_top_keys(list, 10)
        return B
    def create_user_dictionary(self, user_key):
        
        A = self.create_list('user')
                
        list = []
        for x in A:
            b = (x['screen_name'])
            list.append(b)
        if user_key in self.user_keys:

            list2 = []
            for x in A:
                b = (x[user_key])
                list2.append(b)

            DICT = dict(zip(list, list2))
            return DICT         
        
        elif user_key in self.keys:
            for x in self.Dict_List:
                lst = self.create_list(user_key)
                DICT = dict(zip(list, lst))
                return DICT 
        else:
            return 'Sorry that is not a valid key'
    def find_time_stamps_by_duration(self, window, sec=True):
        timestamps = self.create_list('timestamp_ms')
        times = [round(int(x)/1000) for x in timestamps]
        if sec == True:
            Organized_Times = find_time_windows(times, window, sec=True)
        elif sec == False:
            Organized_Times = find_time_windows(times, window, sec=False)
        return Organized_Times
    def find_users_by_time_stamps(self, window, Option):
        
        if Option == True:
            Organized_Times = self.find_time_stamps_by_duration(window, sec=True)
        if Option == False:
            Organized_Times = self.find_time_stamps_by_duration(window, sec=False)
                
        User_list = []              
        
        for list in Organized_Times:
            small_list = []
            for y in list:
                for x in self.Dict_List:
                    a = x['timestamp_ms']
                    time = round(int(a)/1000)
                    if time == y:
                
                        a = x['user']
                        b = a['screen_name']
                        small_list.append(b)

            User_list.append(small_list)

        return User_list        
    def find_Tweets_by_Window(self, window, Option):
        if Option == True:
            Users = self.find_users_by_time_stamps(window, True)
        elif Option == False:
           Users = self.find_users_by_time_stamps(window, False)     

        Tweets_by_Window = []
        for x in Users:
            count = 0
            for y in x:
                count +=1
            Tweets_by_Window.append(count)
        return Tweets_by_Window 
    
    
    def find_hashes_by_time(self, window, Option):
        
        if Option == True:
            A = self.find_users_by_time_stamps(window, True)
        elif Option == False:
            A = self.find_users_by_time_stamps(window, False)
        Hash_List = []
        for LIST in A:
            txt = []
            for x in Tesla():
                c = x['text']
                a = x['user']
                b = a['screen_name']
                # print(a)
                for x in LIST:
                    if x == b:
                        txt.append(c)
            txt2 = []
            for x in txt:
                a = x.split()
                txt2.append(a)
            txt3 = []
            for x in txt2:
                for y in x:
                    if '#' in y:
                        txt3.append(y)

            Hashes = Counter(txt3)
            Hash_List.append(Hashes)
        return Hash_List


T = TweetParser(Tesla())

# print(T.find_top_keys(T.Hashtags, 5))
# print(T.find_top_keys(T.Callouts, 5))
# print(T.textlist)
# A = T.find_most_active_users(10)
# print(A)
# print(T.find_top_keys(T.Hashtags, 10))
# print(T.find_top_keys(T.Callouts, 10))
T = TweetParser(Tesla())

A = T.find_users_by_time_stamps(30, True)
print(T.find_Tweets_by_Window(30, True))  
print(T.find_top_keys(T.Hashtags, 10))



    
#Problems and solutions: 

#1)Tweets by 30 second windows: [26, 33, 42, 31, 28, 31, 11, 39, 7, 45, 22]
#  print(T.find_Tweets_by_Window(30, True))  

# Users by 30 second increments

# 2) A = T.find_users_by_time_stamps(30, True)
# [['intwastaken', 'EdGriffith2', 'imathreatsueme', 'MrSatyaJit06', 'LukeShoeFitter', 'MrSatyaJit06', 'LukeShoeFitter',\
#  'TinaRoy73771752', 'commander_cruz', 'TinaRoy73771752', 'commander_cruz', 'TeslaForThe_Win', 'tslaqpodcast', 'ScotJChrisman',\
#  'JCDentonNetRnnr', 'ScotJChrisman', 'JCDentonNetRnnr', 'HanNing0609', 'utkarsh85129791', 'WhyTesla15', 'HanNing0609',\
#  'utkarsh85129791', 'WhyTesla15', 'HanNing0609', 'utkarsh85129791', 'WhyTesla15'], ['Scott2Loudly', 'dohmanbob',\
#  'Scott2Loudly', 'dohmanbob', 'Thesolidinvest1', 'Duane_MS_Dhoni', 'ahsanbutt', 'Duane_MS_Dhoni', 'ahsanbutt', 'laerisee',\
#  'Whenthe50930605', 'laerisee', 'Whenthe50930605', 'aiacides', 'usnews18_com', 'TNR_Gold', 'ClassInvestor', 'usnews18_com',\
#  'TNR_Gold', 'ClassInvestor', 'usnews18_com', 'TNR_Gold', 'ClassInvestor', 'IBD_Aparna', 'EV_Stevee', 'bagguley', 'praveen77321', \
# 'TNR_Gold', 'TNR_Gold', 'GeekInfoNow', 'TNR_Gold', 'GeekInfoNow', 'InvestorIdeas'], ['jayceejames', 'nytimestech', 'jayceejames', \
# 'nytimestech', 'PrinsenRobert', 'kylaschwaberow', 'PrinsenRobert', 'kylaschwaberow', 'Mike121948', 'Zxcxz_xyz', 'CryptoBowski', \
# 'Mike121948', 'Zxcxz_xyz', 'CryptoBowski', 'Mike121948', 'Zxcxz_xyz', 'CryptoBowski', 'Leesanfr1', 'AustinTeslaClub', \
# 'Leesanfr1', 'AustinTeslaClub', '1_Oreo_1', 'TSLAQrabbithole', '1_Oreo_1', 'TSLAQrabbithole', 'LenePuah', \
# 'Doge4faithfull', 'LenePuah', 'Doge4faithfull', 'jacleena', 'NayakRkk', 'crypto_punx', 'Scifo15th',\
#  'praveen77321', 'Scifo15th', 'praveen77321', 'Livetradingnews', 'Asset_7', 'FinancialTimes', 'Jeff1601', \
# 'FinancialTimes', 'Jeff1601'], ['MikeNasser91', 'uzohak', 'DedicNed', 'MikeNasser91', 'uzohak', 'DedicNed', \
# 'MikeNasser91', 'uzohak', 'DedicNed', 'Mike121948', 'Marcus08090087', 'uzohak', 'rickpaulphoto',\
#  'satoshidreams1', 'my_Book_of_Eli', 'rickpaulphoto', 'satoshidreams1', 'my_Book_of_Eli', 'rickpaulphoto', \
# 'satoshidreams1', 'my_Book_of_Eli', 'Thearoged', 'broapmax', 'CryptoMyoGirl', 'TheWoolCorner', 'InvestorIdeas', \
# 'StarBoy_09', 'AndrewL07811963', 'StarBoy_09', 'AndrewL07811963', 'Thesolidinvest1'], ['warpig4130', \
# 'barkleesanders', 'Techgnostik', 'warpig4130', 'barkleesanders', 'Techgnostik', 'warpig4130', 'barkleesanders', 'Techgnostik', \
# 'superchatboiz', 'y_permatamora', 'carlos27edgar', 'ShahLVL', 'carlos27edgar', 'ShahLVL', 'KevinBCook', 'MrSockpuppet', 'eduardo06424849',\
#  'investorNPress', 'MrSockpuppet', 'eduardo06424849', 'investorNPress', 'MrSockpuppet', 'eduardo06424849', 'investorNPress', \
# 'StalinSSR', 'MUI_MaxHolloway', 'BugabooJester'], ['PandaSWP', 'BijliWaliGaadi', 'dealbook', 'CrankStartMedia', 'ClayIMFWTF',\
#  'JFrusci', 'pamikins62', 'DavidRDutch', 'pamikins62', 'DavidRDutch', 'DeplorableRich5', 'Ink_Songwriter', 'MooningD', \
# 'Spikebmth', 'MooningD', 'Spikebmth', 'BehnanSemih', 'candidate7153', 'TerryKanu', 'BehnanSemih', 'candidate7153', \
# 'TerryKanu', 'BehnanSemih', 'candidate7153', 'TerryKanu', 'candidate7153', 'imshivmgoyal', 'TeslaChillMode', \
# 'imshivmgoyal', 'TeslaChillMode', 'pat25854'], ['smileysteph', 'JCobrae', 'StarBoy_09', 'realAlbanHoxha', \
# 'ConnectingODots', 'YosarianTwo', 'Marcus08090087', 'The_Amit_Rana', 'AlBluson', 'cryptoderanged', 'NVanSpartan'], \
# ['jluckyriego', 'FinTwitTSLA', 'Kenneth91250415', 'jluckyriego', 'FinTwitTSLA', 'Kenneth91250415', 'jluckyriego',\
#  'FinTwitTSLA', 'Kenneth91250415', 'Ashokku42459973', 'Tre_Main_Event', 'Doge4faithfull', 'RealTeslaNorth', \
# 'Tre_Main_Event', 'Tre_Main_Event', 'Tre_Main_Event', 'Jacques66506078', 'Imhariom_bronex', 'PratyushMalli20', \
# 'world_news_eng', 'Tre_Main_Event', 'world_news_eng', 'Tre_Main_Event', 'KalthoffKevin', 'TNR_Gold', 'KalthoffKevin',\
#  'TNR_Gold', 'Surajmo67748814', 'shubham97212324', 'Surajmo67748814', 'shubham97212324', 'Tre_Main_Event', \
# 'Tre_Main_Event', 'timetravelart', 'Tre_Main_Event', 'timetravelart', 'PaulAdams72', 'OndrejBobal', 'gigglehertz'],\
#  ['Cryptocuban1', 'mhadtk', 'The_Commenting', 'guacamole_in', 'usernamedn0ne', 'TeslaNY', 'hunnyhoney1212'], \
# ['up_camping', 'defi_pulse', 'AshokRPatil09', 'EliPasternak', 'JamesHoffmann3', 'aleks211969', 'futchasfu', \
# 'SamuelKunemoemi', 'NSL_Photography', 'BitcoinW0rld', 'Writer_StevenL', 'NSL_Photography', 'BitcoinW0rld', \
# 'Writer_StevenL', 'NSL_Photography', 'BitcoinW0rld', 'Writer_StevenL', 'viriyabot', 'StanStandard', 'AMYRO551',\
#  'viriyabot', 'StanStandard', 'AMYRO551', 'viriyabot', 'StanStandard', 'AMYRO551', 'MrMan12486375', 'daanielme',\
#  'MrMan12486375', 'daanielme', 'MBrae3', 'InvestorSwan', 'myEVreview', 'DaCryptoMonkey', 'Watsay', 'trostrumnet', \
# 'Sukhi_sukhraj', 'Watsay', 'trostrumnet', 'Sukhi_sukhraj', 'Watsay', 'trostrumnet', 'Sukhi_sukhraj', \
# 'Constitutiongal', 'GTuranova'], ['adamwellinform', 'Chadwright_', 'adamwellinform', 'Chadwright_', \
# 'MonicaGwenlover', 'BoyprematureRr', 'gwestr', 'isukatsmsh', 'wolfofcrypto89', 'Gays4Tesla', 'Umesh25572659', \
# 'Brownboi9365', 'tesflowtravel', 'NorCalWineLady', 'iKadm0s', 'NorCalWineLady',\
#  'iKadm0s', 'Man89445040', 'b437d3fe9441419', 'Man89445040', 'b437d3fe9441419', 'jamicianmecrazy']]


#3) Most used hashtag: 
# print(T.find_top_keys(T.Hashtags, 10))
# {'#Bitcoin': 24, '#Tesla': 15, '#ethereum': 6, '#Bitcoin"': 6, '#zhengzhouflood': 5, \
# '#bitcoin.': 4, '#dogecoin,"': 4, '#tesla': 3, '#Model3': 3, '#Doge': 2}

#4)Hashtags in last 30 seconds Counter({'#ethereum': 2, '#Bitcoin': 2, '#zhengzhouflood': 1, '#bitcoin,': 1, '#dogecoin!': 1, '#Bitcoin"': 1, '#bitcoin.': 1, '#dogecoin,"': 1})
# A = T.find_hashes_by_time(30, True)
#print(A[0])
# A = T.find_hashes_by_time(30, True)
# print(A[0])
# Counter({'#Bitcoin': 6, '#ethereum': 5, '#Bitcoin"': 3, '#bitcoin.': \
# 3, '#dogecoin,"': 3, '#zhengzhouflood': 2, '#bitcoin,': 2, '#dogecoin!': 2})


#5) Used Built in class functionality to find moving average of any given window of time for dataset :)

# print(T.find_hashes_by_time(30, True))


# [Counter({'#Bitcoin': 6, '#ethereum': 5, '#Bitcoin"': 3, '#bitcoin.': 3, '#dogecoin,"': 3, '#zhengzhouflood': 2, '#bitcoin,': 2,\
#  '#dogecoin!': 2}), Counter({'#Tesla': 18, '#Bitcoin': 12, '#rEVolution': 6, '#Gold:': 6, '#DYOR': 6, '#ElectricCars': 6, \
# '#EVs': 6, '#BlockChain': 6, '#Crypto': 6, '#Ethereum': 3, '#skynews': 2, '#BreakingNews': 2, '#PleaseRetweet': 2, '#Tesla,': 1,\
#  '#zhengzhouflood': 1}), Counter({'#zhengzhouflood': 4, '#Tesla': 3, '#EV…': 3, '#Bitcoin': 2, '#Tezos"': 2, '#Doge': 2, '#Ethereum,': 2,\
#  '#tesla': 2, '#eCar': 2, '#bitcoin.': 2, '#ethereum': 2, '#dogecoin,"': 2, '#doge': 1, '#dogearmy': 1, '#shibainu': 1, '#ShibaArmy': 1,\
#  '#babydoge': 1, '#babyshibinu': 1, '#CyberTruck': 1}), Counter({'#Bitcoin': 12, '#Tesla': 4, '#SpaceX': 4, '#Bitcoin”': 4,\
#  '#cybertruck': 3, '#ListenToThis:': 3, '#NowPlaying': 3}), Counter({'#wsj': 3, '#nytimes': 3, '#business…': 3, \
# '#zhengzhouflood': 2, '#ethereum': 1, '#dogecoin': 1, '#doge': 1, '#upgrade': 1, '#dogethereum': 1, '#moon': 1,\
# '#mars': 1, '#dogelon': 1, '#crypto': 1, '#Tesla': 1, '#Bitcoin”': 1, '#Bitcoin': 1, '#SAFEMOON': 1}), \
# Counter({'#Bitcoin': 4, '#Cryptocurrency': 4, '#FinTech': 4, '#Digital': 4, '#Currency': 4, '#bitcoin.': 2, \
# '#ethereum': 2, '#dogecoin,"': 2, '#Bitcoi…': 1, '#tesla': 1, '#climateaction': 1, '#SocialMediaMarketing': 1,\
#  '#DigitalMarketing': 1, '#BSC': 1, '#BNB': 1, '#Polygon': 1, '#Matic': 1, '#ETH': 1, '#Tesla': 1}), \
# Counter({'#batterystorage': 1, '#Tesla': 1}), Counter({'#Tesla': 7, '#Doge': 3, '#Ethereum,': 3, '#rEVolution': 2, \
# '#Gold:': 2, '#DYOR': 2, '#ElectricCars': 2, '#EVs': 2, '#BlockChain': 2, '#Bitcoin': 2, '#Crypto': 2, '#bitcoin.': 1,\
#  '#ethereum': 1, '#dogecoin,"': 1, '#Model3': 1}), Counter({'#Bitcoin,"': 1, '#Tesla': 1, '#EV': 1, '#tesla': 1,\
#  '#selfdrive': 1, '#modelsex': 1, '#m…': 1}), Counter({'#Tesla': 8, '#Bitcoin': 6, '#ElonMusk': 3, '#bitcoin.”': 2,\
#  '#BITCOIN': 1, '#zhengzhouflood': 1, '#bitcoin': 1, '#BTC': 1, '#Model3': 1, '#Bitcoin"': 1}),\
#  Counter({'#Bitcoin': 10, '#Bitcoin"': 5, '#Tesla': 2, '#Model3': 2, '#bitcoin.': 1, '#ethereum': 1, '#dogecoin,"': 1})]



     




