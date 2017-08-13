import json
import oauth2
import requests

from keys import MY_KEY, MY_KEY_SECRET, MY_TOKEN, MY_TOKEN_SECRET
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

KEY = MY_KEY
KEY_SECRET = MY_KEY_SECRET
TOKEN = MY_TOKEN
TOKEN_SECRET = MY_TOKEN_SECRET

oauth = OAuth1(TOKEN, TOKEN_SECRET, KEY, KEY_SECRET)
r = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=nathantspencer&include_rts=false", auth=oauth)
print(r)
