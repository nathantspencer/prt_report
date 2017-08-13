import code
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
    TIMELINE_URL = BASE_URL + "user_timeline.json?screen_name=WVUDOT"
    COUNT_URL = "&count="
    MAX_ID_URL = "&max_id="

    # Total number of tweets retrieved will be BATCHES_TO_RETRIEVE * 200
    BATCHES_TO_RETRIEVE = 16

    consumer = oauth2.Consumer(key=MY_KEY, secret=MY_KEY_SECRET)
    token = oauth2.Token(key=MY_TOKEN, secret=MY_TOKEN_SECRET)
    client = oauth2.Client(consumer, token)
    request_url = TIMELINE_URL + COUNT_URL + str(200)
    response, content = client.request(request_url, "GET")

    tweets = []
    for i in range(BATCHES_TO_RETRIEVE):
        content_json = json.loads(content.decode("utf-8"))
        max_id = -1
        for item in content_json:
            tweet = {}
            tweet["id"] = item["id"]
            tweet["created_at"] = item["created_at"]
            tweet["text"] = item["text"]
            if max_id == -1 or tweet["id"] < max_id:
                max_id = tweet["id"]
            tweets.append(tweet)
        request_url = TIMELINE_URL + COUNT_URL + str(200) + MAX_ID_URL + str(max_id - 1)
        response, content = client.request(request_url, "GET")

    data_frame = pd.DataFrame(tweets)

    # TODO: Cull non-relevant entries by their text content
