import json
import oauth2
import pandas as pd
import requests

from collections import namedtuple
from keys import MY_KEY, MY_KEY_SECRET, MY_TOKEN, MY_TOKEN_SECRET
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

if __name__ == "__main__":
    KEY = MY_KEY
    KEY_SECRET = MY_KEY_SECRET
    TOKEN = MY_TOKEN
    TOKEN_SECRET = MY_TOKEN_SECRET

    BASE_URL = "https://api.twitter.com/1.1/statuses/"
    TIMELINE_URL = BASE_URL + "user_timeline.json?screen_name=WVUDOT&count=400&trim_user=true"

    consumer = oauth2.Consumer(key=MY_KEY, secret=MY_KEY_SECRET)
    token = oauth2.Token(key=MY_TOKEN, secret=MY_TOKEN_SECRET)
    client = oauth2.Client(consumer, token)
    response, content = client.request(TIMELINE_URL, "GET")

    tweets = []
    json = json.loads(content.decode("utf-8"))
    for item in json:
        tweet = {}
        tweet["id"] = item["id"]
        tweet["created_at"] = item["created_at"]
        tweet["text"] = item["text"]
        tweets.append(tweet)
    print(tweets)
