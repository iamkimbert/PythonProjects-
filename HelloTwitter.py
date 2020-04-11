#Reference https://realpython.com/twitter-bot-python-tweepy/
#
# Kimberly Townsend
#
# Description:
#Trying to understand the twitter API
#To run this code you must activate venv (source ./venv/bin/activate)

import tweepy

#Authenticate to Twitter
#you must replace CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET with your own
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN","ACCESS_TOKEN_SECRET")

# Create API Object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Approved")
except:
    print("An Error has occured during Authentication")

# Methods for user timelines

#timeline = api.home_timeline()
#for tweet in timeline:
#    print(f"{tweet.user.name}said {tweet.text}")

# Methods for Users

#user = api.get_user("BarackObama")
#print(user.name)
#print(user.description)
#print(user.location)

#print("Last 20 Followers:")
#for follower in user.followers():
#    print(follower.name)

#Methods for followers
#api.create_friendship("DonaldTrump") #adds @twitter to the list of accounts that you follow
#print("friendship created")
api.destroy_friendship("DonaldTrump") #adds @twitter to the list of accounts that you follow
print("friendship destroyed")
