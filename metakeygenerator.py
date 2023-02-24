# # This python API assumes you are passing the variable "code" to obtain a Meta Facebook/Instagram Key that lives for 60 days
# __________________________________________________________________________________________________________________________________________________________
# # Example of how to get "code" from Facebook:
# # https://www.facebook.com/v16.0/dialog/oauth?client_id=554211022979973&redirect_uri=https%3A%2F%2twitter.com&scope=ads_management
# # GET request to obtain "code"
# url = "https://graph.facebook.com/v16.0/dialog/oauth?"
# # Your app ID from Facebook Developer portal
# url += f"client_id={meta_app_id}&"
# # URL to redirect to after authorization
# url += f"redirect_uri={redirect_encoded}&"
# # Permissions to request
# url += f"scope=ads_management"
# __________________________________________________________________________________________________________________________________________________________
# Standard Libraries
import requests
import urllib.parse
import os

# Environment Variables for Facebook Credentials
meta_app_id = os.environ.get('meta_app_id')
meta_app_secret = os.environ.get('meta_app_secret')

# API Function to get temporary access token
def get_access_token(redirect_original, code):
    # URL to redirect to after authorization percent encoded
    redirect_encoded = urllib.parse.quote(redirect_original, safe='')

    # GET request to get access token
    url = "https://graph.facebook.com/v16.0/oauth/access_token?"
    url += f"client_id={meta_app_id}&"
    url += f"redirect_uri={redirect_encoded}&"
    url += f"client_secret={meta_app_secret}&"
    url += f"code={code}"

    short_response = requests.request("GET", url)
    temp_access_token = short_response.json()['access_token']

    # Create long lived key
    key_url = "https://graph.facebook.com/v16.0/oauth/access_token"
    # Parameters for long lived key
    id_data = {
        "grant_type":"fb_exchange_token",
        "client_id": meta_app_id,
        "client_secret": meta_app_secret,
        "fb_exchange_token": temp_access_token}
    # GET request response
    long_response = requests.get(key_url, params=id_data)
    long_key = long_response.json()
    
    return long_key