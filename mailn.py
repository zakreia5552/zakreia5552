import os
import tweepy 

# جلب القيم السرية من متغيرات البيئة
API_KEY = os.getenv('EGun3g74yanADDkfkvcIKxIdA')
API_SECRET_KEY = os.getenv('9qsCqpKmWtlGmqHHl08jbkPOrhzcu9KosaqwASlYxXcVuAEevH')
ACCESS_TOKEN = os.getenv('3076980989-wDRfV6lz1vE87qN7yZZPaAgDst2VwFxkaDnA63N')
ACCESS_TOKEN_SECRET = os.getenv('O3nP86PC3KMDgjqOyxXg2VgGpWzTdcYJWKpJY4lMz0pwL') 

# التأكد من أن القيم السرية تم جلبها بنجاح
if not all([API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    raise ValueError("All API keys and tokens must be set in environment variables.") 

# إعداد التوثيق مع تويتر
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 

# دالة لمتابعة المتابعين الجدد تلقائيًا
def auto_follow_followers():
    for follower in tweepy.Cursor(api.followers).items():
        try:
            if not follower.following:
                follower.follow()
                print(f"Followed {follower.screen_name}")
        except tweepy.TweepError as e:
            print(f"Error following {follower.screen_name}: {e}") 

# استدعاء الدالة لتشغيلها
auto_follow_followers()
