from typing import Text
import tweepy
from tweepy import Stream
from collections import Counter
from streamtesting3 import Tesla

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


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
    def create_user_dictionary(self, user_key ):
        A = self.create_list('user')
        list = []
        for x in A:
            b = (x['screen_name'])
            list.append(b)
        list2 = []
        for x in A:
            b = (x[user_key])
            list2.append(b)

        DICT = dict(zip(list, list2))
        return DICT         

T = TweetParser(Tesla())

# print(T.find_top_keys(T.Hashtags, 5))
# print(T.find_top_keys(T.Callouts, 5))
# print(T.textlist)
# A = T.find_most_active_users(10)
# print(A)
# print(T.find_top_keys(T.Hashtags, 10))
# print(T.find_top_keys(T.Callouts, 10))
T = TweetParser(Tesla())
print(T.create_user_dictionary('friends_count'))  
    



     




