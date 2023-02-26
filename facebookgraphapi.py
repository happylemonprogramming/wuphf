# This python script uses the facebook graph API to post an image to a business page
# The script also assumes you have a long lived access token

# Standard Libraries
import requests
import os

# Environment Variables for Facebook Credentials
# user_access_token = os.environ.get('meta_user_access_token')

def facebook_post(caption, media, user_access_token):
    # # Get Pages ID
    id_url = "https://graph.facebook.com/me/accounts"
    id_data = {"access_token": user_access_token}
    response = requests.get(id_url, params=id_data)
    page_id = response.json()['data'][0]['id']

    # # Get Pages Access Token
    page_access_url = f'https://graph.facebook.com/{page_id}'
    page_access_data = {"fields": "access_token", "access_token": user_access_token}
    response = requests.get(page_access_url, params=page_access_data)
    page_access_token=response.json()['access_token']

    # # Text Post
    # post_url = f"https://graph.facebook.com/{page_id}/feed"
    # post_data = {"message": "AI did this", "access_token": page_access_token}
    # response = requests.post(post_url, json=post_data)
 
    # # Image Post
    post_url = f"https://graph.facebook.com/{page_id}/photos"
    post_data = {"message": caption, "url": media,"access_token": page_access_token}

    response = requests.post(post_url, json=post_data)

    # Post Return
    if response.status_code == 200:
        # success
        return response.json()
    else:
        # failure
        return "Request failed with status code:", response.status_code, response.json()