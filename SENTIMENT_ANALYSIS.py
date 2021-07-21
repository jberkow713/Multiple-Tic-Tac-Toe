
from inspect import CO_ASYNC_GENERATOR
import pandas as pd
from Chatbot import *
import itertools

def Cluster_Tweets(Name, Dict, model):
    '''
    Takes a list of words, clusters them based on their average vector
    '''
    List = []
    # List2 = []
    Users = []
    count = 0
    for k,v in Dict.items():
        Users.append((k,count))
        List.append(v)
        # List2.append((v, count))
        count +=1
    
    list_of_vectors = [Vec_for_Clustering_2(x, model).tolist() for x in List]        
    nparray = np.array(list_of_vectors)    

       
    clusters = int(math.ceil(math.sqrt(len(list_of_vectors))))
    if len(list_of_vectors)<45:
        clusters2 = 15
    if len(list_of_vectors)>=45:
        clusters2 = 25

    kmeans = KMeans(n_clusters=clusters2, random_state=45).fit(nparray)
    categorized_list = kmeans.labels_
    string_list = [str(x) for x in categorized_list]
    print(string_list)
    
    Categorized_Dict = dict(zip(List, string_list))
   


    clusters = []
    for k,v in Categorized_Dict.items():
        clusters.append(v)
    
    length = len(clusters)
    index = 0
    cluster_holder = []

    while length >0:
        User = Users[index][0]
        cluster = clusters[index]
        Vals = (User, cluster)
        cluster_holder.append(Vals)
        index +=1
        length -=1
       

    Cluster = 0
    for x in cluster_holder:
        if x[0]==Name:
            Cluster += int(x[1])
           
    Friends = []
    for x in cluster_holder:
        if int(x[1])==Cluster:
            if x[0] != Name:
                Friends.append(x[0])
    
    return Friends


df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding='latin-1') 
df.columns =['', 'ID', 'Date',  'Code', 'Name', 'Tweet' ]
def rand_val():
    rand = random.randint(0,1600000)
    return rand


class TwitterFriendFinder():
    '''
    This class will be used to run analysis on tweets and return corresponding friends to the user
    '''
    def __init__(self, name, dataframe, num_users):
        self.name = name 
        self.dataframe = dataframe 
        self.num_users = num_users
        self.users = self.create_users()
        self.tweets_list = self.find_user_tweets()
        self.user_dict = dict(zip(self.users, self.tweets_list))
        self.friends = self.find_twitter_friends()

    def create_users(self):
        Random_Names = []
        for i in range(self.num_users):
            rand = rand_val()
            x =self.dataframe.loc[[rand_val()]]
            y = x['Name'].values[0]
            Random_Names.append(y)
        Random_Names.append(self.name)
        
        return Random_Names            
    
    def find_user_tweets(self):
        TWEETS = []
        for user in self.users:
            
            name_df = self.dataframe.loc[self.dataframe['Name'] == user]
            tweets = name_df['Tweet'].tolist()
            tweets = ' '.join(tweets)

            TWEETS.append(tweets)
        
        return TWEETS
    
    def find_twitter_friends(self):
        clustered = (Cluster_Tweets(self.name, self.user_dict, model))
        if len(clustered)>0:
            return clustered
        else:
            return 'Sorry you have found no friends on this search, please search again'

Parser = TwitterFriendFinder('nemcy',df, 48)

print(Parser.friends)

print(len(Parser.friends))



