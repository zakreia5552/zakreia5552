import tweepy

API_KEY = '3SfJuVbllc78dy7yYf9ulTAvV'
API_SECRET_KEY = 'rhgnrFbvPkzWFAHaOVRMn4T42lK47Nn0zznLLJqKnHaUni7CDC'
ACCESS_TOKEN = '3076980989-u3mdBIKDE5WQAXvWHA8yf1TURkxTmgfUnOzDbwM'
ACCESS_TOKEN_SECRET = 'lcdhIIpsuAmFYYiYHm8rG495jrcEq5fRRCPPQALSsJ5EN'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def auto_follow_followers():
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            follower.follow()
            print(f"Followed {follower.screen_name}")

auto_follow_followers()
