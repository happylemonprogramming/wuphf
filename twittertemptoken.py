# Using OAuth1Session
from requests_oauthlib import OAuth1Session

# Using OAuth1 auth helper
import requests
from requests_oauthlib import OAuth1
import os

# App specific
client_key = os.environ.get('twitter_consumer_key')
client_secret = os.environ.get('twitter_consumer_secret')

def get_twitter_temp_token():
    request_token_url = 'https://api.twitter.com/oauth/request_token'

    # Using OAuth1Session
    oauth = OAuth1Session(client_key, client_secret=client_secret)
    fetch_response = oauth.fetch_request_token(request_token_url)
    
    oauth_token = fetch_response['oauth_token']
    oauth_token_secret = fetch_response['oauth_token_secret']
    return oauth_token, oauth_token_secret

# var = get_twitter_temp_token()
# print(var)
# step2url = 'https://api.twitter.com/oauth/authorize?'
# step2url += f"oauth_token={var[0]}&"
# step2url += f"oauth_token_secret={var[1]}&"
# step2url += f"oauth_callback_confirmed=True"
# print(step2url)