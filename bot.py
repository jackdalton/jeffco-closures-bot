from creds import *
from keywords import keywords
from time import sleep
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def check_tweets():
    tweets = api.user_timeline("JeffcoSchoolsCo", count=1)
    text = tweets[0].text
    found = False
    for i in keywords:
        if i in text.lower():
            api.retweet(tweets[0].id)
            print("RT:\n%s" % text)
            found = True
    if not found:
        print("No keywords found:\n%s" % text)
    print("Tweet URL: %s" % tweets[0].entities["urls"][0]["url"])
    sleep(90)
    check_tweets()


check_tweets()
print("Running...")
