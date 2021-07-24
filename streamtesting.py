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
    def find_users_in_time_window(self, window, sec=True):
        #Time_Dict maps all timestamps to users
        
        Time_Dict = self.create_user_dictionary('timestamp_ms')      
          
        
        keys = []
        values = []
        print(len(values))
        for k,v in Time_Dict.items():
            keys.append(k)
            values.append(round(int(v)/1000))
        Time_Dict = dict(zip(keys, values))
        print(len(values))           

        #Time_Windows = List of Lists of sorted timestamps for given window duration
        B = self.create_list('timestamp_ms')
        times = []
        for x in B:
            date = round(int(x)/1000)
            times.append(date)
        times = sorted(times)
        if sec == True:
            Time_Windows = find_time_windows(times,window)
        elif sec == False:
            Time_Windows = find_time_windows(times, window, sec=False)    
        Lengths = []
        count = 0
        
        for x in Time_Windows:
            for vals in x:
                count +=1
            Lengths.append(count)
            count = 0
      
       
        length = len(Lengths)
        index = 0
        Big_List = []
        index_2 = 0 
        Done = False 
        while length >0:
            val = Lengths[index]
            
            Small_List = []
            while val >0:
                
                VAL = keys[index_2]
                
                
                Small_List.append(VAL)
                if VAL == keys[-1]:
                    
                    Done == True
                    break 
                index_2 +=1
                val -=1
            
            index +=1
            length -=1
            Big_List.append(Small_List)             

        Big_List.remove(Big_List[-1])        
        
        return Big_List


T = TweetParser(Tesla())

# print(T.find_top_keys(T.Hashtags, 5))
# print(T.find_top_keys(T.Callouts, 5))
# print(T.textlist)
# A = T.find_most_active_users(10)
# print(A)
print(T.find_top_keys(T.Hashtags, 10))
# print(T.find_top_keys(T.Callouts, 10))
T = TweetParser(Tesla())
A = T.create_user_dictionary('timestamp_ms')

times = []
for v in A.values():
    date = round(int(v)/1000)
    times.append(date)
print(len(times))


    
A = T.find_users_in_time_window(30)
for x in A:
    print(x)
    


#1)Tweets by 30 second windows: [14, 19, 22, 17, 14, 19, 11, 25, 7, 25, 16]
#  
# Users by 30 second increments
#2)

# ['intwastaken', 'EdGriffith2', 'imathreatsueme', 'MrSatyaJit06', 'LukeShoeFitter', 'TinaRoy73771752', 'commander_cruz', 'TeslaForThe_Win', 'tslaqpodcast', 'ScotJChrisman', 'JCDentonNetRnnr', 'HanNing0609', 'utkarsh85129791', 'WhyTesla15']
# ['Scott2Loudly', 'dohmanbob', 'Thesolidinvest1', 'Duane_MS_Dhoni', 'ahsanbutt', 'laerisee', 'Whenthe50930605', 'aiacides', 'usnews18_com', 'TNR_Gold', 'ClassInvestor', 'IBD_Aparna', 'EV_Stevee', 'bagguley', 'praveen77321', 'GeekInfoNow', 'InvestorIdeas', 'jayceejames', 'nytimestech']
# ['PrinsenRobert', 'kylaschwaberow', 'Mike121948', 'Zxcxz_xyz', 'CryptoBowski', 'Leesanfr1', 'AustinTeslaClub', '1_Oreo_1', 'TSLAQrabbithole', 'LenePuah', 'Doge4faithfull', 'jacleena', 'NayakRkk', 'crypto_punx', 'Scifo15th', 'Livetradingnews', 'Asset_7', 'FinancialTimes', 'Jeff1601', 'MikeNasser91', 'uzohak', 'DedicNed']
# ['Marcus08090087', 'rickpaulphoto', 'satoshidreams1', 'my_Book_of_Eli', 'Thearoged', 'broapmax', 'CryptoMyoGirl', 'TheWoolCorner', 'StarBoy_09', 'AndrewL07811963', 'warpig4130', 'barkleesanders', 'Techgnostik', 'superchatboiz', 'y_permatamora', 'carlos27edgar', 'ShahLVL']
# ['KevinBCook', 'MrSockpuppet', 'eduardo06424849', 'investorNPress', 'StalinSSR', 'MUI_MaxHolloway', 'BugabooJester', 'PandaSWP', 'BijliWaliGaadi', 'dealbook', 'CrankStartMedia', 'ClayIMFWTF', 'JFrusci', 'pamikins62']
# ['DavidRDutch', 'DeplorableRich5', 'Ink_Songwriter', 'MooningD', 'Spikebmth', 'BehnanSemih', 'candidate7153', 'TerryKanu', 'imshivmgoyal', 'TeslaChillMode', 'pat25854', 'smileysteph', 'JCobrae', 'realAlbanHoxha', 'ConnectingODots', 'YosarianTwo', 'The_Amit_Rana', 'AlBluson', 'cryptoderanged']
# ['NVanSpartan', 'jluckyriego', 'FinTwitTSLA', 'Kenneth91250415', 'Ashokku42459973', 'Tre_Main_Event', 'RealTeslaNorth', 'Jacques66506078', 'Imhariom_bronex', 'PratyushMalli20', 'world_news_eng']
# ['KalthoffKevin', 'Surajmo67748814', 'shubham97212324', 'timetravelart', 'PaulAdams72', 'OndrejBobal', 'gigglehertz', 'Cryptocuban1', 'mhadtk', 'The_Commenting', 'guacamole_in', 'usernamedn0ne', 'TeslaNY', 'hunnyhoney1212', 'up_camping', 'defi_pulse', 'AshokRPatil09', 'EliPasternak', 'JamesHoffmann3', 'aleks211969', 'futchasfu', 'SamuelKunemoemi', 'NSL_Photography', 'BitcoinW0rld', 'Writer_StevenL']
# ['viriyabot', 'StanStandard', 'AMYRO551', 'MrMan12486375', 'daanielme', 'MBrae3', 'InvestorSwan']
# ['myEVreview', 'DaCryptoMonkey', 'Watsay', 'trostrumnet', 'Sukhi_sukhraj', 'Constitutiongal', 'GTuranova', 'adamwellinform', 'Chadwright_', 'MonicaGwenlover', 'BoyprematureRr', 'gwestr', 'isukatsmsh', 'wolfofcrypto89', 'Gays4Tesla', 'Umesh25572659', 'Brownboi9365', 'tesflowtravel', 'NorCalWineLady', 'iKadm0s', 'Man89445040', 'b437d3fe9441419', 'jamicianmecrazy']


#3) Most used hashtag: {'#Bitcoin': 24, '#Tesla': 15, '#ethereum': 6, '#Bitcoin"': 6, '#zhengzhouflood': 5, \
# '#bitcoin.': 4, '#dogecoin,"': 4, '#tesla': 3, '#Model3': 3, '#Doge': 2}

#4)Hashtags in last 30 seconds Counter({'#ethereum': 2, '#Bitcoin': 2, '#zhengzhouflood': 1, '#bitcoin,': 1, '#dogecoin!': 1, '#Bitcoin"': 1, '#bitcoin.': 1, '#dogecoin,"': 1})

#5) Used Built in class functionality to find moving average of any given window of time for dataset :)


def find_hashes_by_time(window):
    T = TweetParser(Tesla())
    A = T.find_users_in_time_window(window)
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

print(find_hashes_by_time(60))

   



     




