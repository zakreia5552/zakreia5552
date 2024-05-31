import os
import tweepy

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def auto_follow_followers():
    for follower in tweepy.Cursor(api.followers).items():
        try:
            if not follower.following:
                follower.follow()
                print(f"Followed {follower.screen_name}")
        except tweepy.TweepError as e:
            print(f"Error following {follower.screen_name}: {e}")

auto_follow_followers()