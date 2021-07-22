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

T = TweetParser(Tesla())


print(T.find_top_keys(T.Hashtags, 10))
print(T.find_top_keys(T.Callouts, 10))

