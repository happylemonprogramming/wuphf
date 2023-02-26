# Standard library imports
import requests
import os
import json

# App specific
client_key = os.environ.get('twitter_consumer_key')
client_secret = os.environ.get('twitter_consumer_secret')

def get_twitter_permanent_token(temp_oauth_token, temp_oauth_verifier):
    # Construct the request URL
    url = "https://api.twitter.com/oauth/access_token?"
    url += f"oauth_token={temp_oauth_token}"+"&"
    url += f"oauth_verifier={temp_oauth_verifier}"

    # Make the request
    response = requests.request("POST", url)
    print("Permanent Response: " + response.text)

    # Split the string based on the "&" character
    parts = response.text.split("&")
    print("Permanent Parts: " + parts)
    # Loop through each part and split based on the "=" character
    for part in parts:
        key_value = part.split("=")
        print("Permanent Key Value: " + key_value)
        key = key_value[0]
        value = key_value[1]
        
        # If the key is "oauth_token", save the value
        if key == "oauth_token":
           oauth_token = value

        # If the key is "oauth_token_secret", save the value
        if key == "oauth_token_secret":
            oauth_token_secret = value

        # If the key is "user_id", save the value
        if key == "user_id":
            user_id = value

        # If the key is "screen_name", save the value
        if key == "screen_name":
            screen_name = value
        

    # dictionary = {"oauth_token": oauth_token, "oauth_token_secret": oauth_token_secret, "user_id": user_id, "screen_name": screen_name}
    # data = json.dumps(dictionary)
    return oauth_token, oauth_token_secret, user_id, screen_name