import tweepy
import pandas as pd
import time
import json
import os

API_KEY = os.environ.get('API_KEY')
API_SECRET_KEY = os.environ.get('API_SECRET_KEY')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

BATCH_SIZE = 100
TIMER = 1

SOURCE = "FOLLOWERS"  # ["PARTICIPANTS", "FOLLOWERS"]
if SOURCE == "PARTICIPANTS":
    folder_output = '../data/twitter/follower_count'
    df_survey = pd.read_csv('../data/twitter/survey.csv')
    users = [x for x in df_survey['user']]
elif SOURCE == "FOLLOWERS":
    # Follow count of followers
    folder_output = '../data/twitter/follower_count_of_followers'
    with open('../data/twitter/followers/user_followers.json', 'r') as json_file:
        data_dict = json.load(json_file)
        users = [follower for followers_list in data_dict.values() for follower in followers_list]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
batch_count = 0
user_count = 0
batch_data = {}
for u in range(0,len(users)):
    print(str(u) + '/' + str(len(users)))
    user = users[u]
    time.sleep(TIMER)
    try:
        twitter_user = api.get_user(screen_name=user)
        # print(f"{twitter_user.screen_name} has {twitter_user.followers_count} followers.")
        batch_data[user] = twitter_user.followers_count
    except Exception as e:
        print(f"An error occurred for user {user}: {e}")
    user_count += 1
    if user_count == BATCH_SIZE:
        batch_count += 1
        user_count = 0
        with open(f"{folder_output}/user_followers_{batch_count}.json", 'w') as outfile:
            json.dump(batch_data, outfile)
        batch_data = {}
        # pd.to_csv(f"{folder_output}/user_followers_{batch_count}.csv")

# Final batch
if user_count > 0:
    batch_count += 1
    with open(f"{folder_output}/user_followers_{batch_count}.json", 'w') as outfile:
        json.dump(batch_data, outfile)

