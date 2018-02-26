from creds import *
from keywords import keywords
from time import sleep
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def log(text):
    print(text)
    file = open("log.txt", "a+")
    file.write("%s\n\n" % text)
    file.close()

def check_tweets():
    tweets = api.user_timeline("JeffcoSchoolsCo", count=1)
    text = tweets[0].text
    found = False
    for i in keywords:
        if i in text.lower():
            api.retweet(tweets[0].id)
            log("RT:\n%s" % text)
            found = True
    if not found:
        log("No keywords found:\n%s" % text)
    sleep(90) # sleep for 90 seconds
    check_tweets()


check_tweets()
log("Running...")
