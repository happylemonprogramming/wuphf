# # Step 1
# https://developer.twitter.com/en/docs/authentication/api-reference/request_token
# curl --request POST \
#   --url 'https://api.twitter.com/oauth/request_token?oauth_callback=$HTTP_ENCODED_CALLBACK_URL' \
#   --header 'Authorization: OAuth oauth_consumer_key="$oauth_consumer_key", oauth_nonce="$oauth_nonce", oauth_signature="oauth_signature", oauth_signature_method="HMAC-SHA1", oauth_timestamp="$timestamp", oauth_version="1.0"'
# # Step 2
# https://developer.twitter.com/en/docs/authentication/api-reference/authenticate
# https://developer.twitter.com/en/docs/authentication/api-reference/authorize
# # Step 3
# https://developer.twitter.com/en/docs/authentication/api-reference/access_token

# Libraries
import requests
import urllib.parse
import time
import hmac
import hashlib
import base64
import os

# App specific
consumer_key = os.environ.get('twitter_consumer_key')
consumer_secret = os.environ.get('twitter_consumer_secret')

# Set your callback URL here
callback_url = 'https://twitter.com/lemonknowsall'

# Generate nonce and timestamp
timestamp = str(int(time.time()))
nonce = timestamp

# Define the OAuth signature method and version
signature_method = 'HMAC-SHA1'
oauth_version = '1.0'

# Encode the callback URL
encoded_callback_url = urllib.parse.quote(callback_url, safe='')

# Construct the base string
base_string = f'POST&{urllib.parse.quote("https://api.twitter.com/oauth/request_token", safe="")}&'
base_string += f'oauth_callback%3D{encoded_callback_url}%26'
base_string += f'oauth_consumer_key%3D{consumer_key}%26'
base_string += f'oauth_nonce%3D{nonce}%26'
base_string += f'oauth_signature_method%3D{signature_method}%26'
base_string += f'oauth_timestamp%3D{timestamp}%26'
base_string += f'oauth_version%3D{oauth_version}'

# Create the signing key
signing_key = f'{urllib.parse.quote(consumer_secret, safe="")}&'

# Generate the signature
signature = base64.b64encode(hmac.new(signing_key.encode('utf-8'), base_string.encode('utf-8'), hashlib.sha1).digest())

# Encode the signature
encoded_signature = urllib.parse.quote(signature, safe='')

# Construct the request URL
url = "https://api.twitter.com/oauth/request_token?"
url += f"oauth_callback={encoded_callback_url}"+"&"
url += f"oauth_consumer_key={consumer_key}"+"&"
url += "oauth_signature_method=HMAC-SHA1"+"&"
url += "oauth_version=1.0"+"&"
url += f"oauth_timestamp={timestamp}"+"&"
url += f"oauth_nonce={nonce}"+"&"
url += f"oauth_signature={encoded_signature}"

response = requests.request("POST", url)

print(response.text)