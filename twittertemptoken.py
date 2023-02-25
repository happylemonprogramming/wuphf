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

# OAuth Token and Secret get passed to Bubble via API call
# Then Bubble uses the token and secret to get the user's profile via Twitter link (GET request)

# goto_browser_url = 'https://api.twitter.com/oauth/authorize'
# params = {'oauth_token': oauth_token, 'oauth_token_secret': oauth_token_secret, 'oauth_callback_confirmed': 'True'}
# r = requests.get(goto_browser_url, params=params)

# print(r)

# {
#     "oauth_token": "Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik",
#     "oauth_token_secret": "Kd75W4OQfb2oJTV0vzGzeXftVAwgMnEK9MumzYcM"
# }
# resource_owner_key = fetch_response.get('oauth_token')
# resource_owner_secret = fetch_response.get('oauth_token_secret')

# # Using OAuth1 auth helper
# oauth = OAuth1(client_key, client_secret=client_secret)
# r = requests.post(url=request_token_url, auth=oauth)
# r.content
# "oauth_token=Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik&oauth_token_secret=Kd75W4OQfb2oJTV0vzGzeXftVAwgMnEK9MumzYcM"
# from urlparse import parse_qs
# credentials = parse_qs(r.content)
# resource_owner_key = credentials.get('oauth_token')[0]
# resource_owner_secret = credentials.get('oauth_token_secret')[0]