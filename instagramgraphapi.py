# This python script uses the instagram graph API to post an image
# to an instagram business account. The script assumes your instagram
# business account is connected to a facebook page. The script also
# assumes you have a long lived access token for the instagram business

# Standard Libraries
import requests
import os

# Environment Variables for Facebook Credentials
user_access_token = os.environ.get('meta_user_access_token')

# API Function to post to Instagram
def instagram_post(caption, media):
    # # Get Pages ID
    id_url = "https://graph.facebook.com/me/accounts"
    id_data = {"access_token": user_access_token}
    response = requests.get(id_url, params=id_data)
    page_id = response.json()['data'][0]['id']

    # # Get Instagram Business Account ID
    instabiz_url = f"https://graph.facebook.com/{page_id}"
    instabiz_data = {"access_token": user_access_token, "fields": "instagram_business_account"}
    response = requests.get(instabiz_url, params=instabiz_data)
    instabiz_id = response.json()['instagram_business_account']['id']

    # # Post to Container (Staging)
    container_url = f"https://graph.facebook.com/{instabiz_id}/media"
    container_data = {
        "access_token": user_access_token, 
        "image_url": media,
        "caption": caption
        }
    response = requests.post(container_url, params=container_data)
    container_id = response.json()['id']

    # # Post to Instagram
    post_url = f"https://graph.facebook.com/{instabiz_id}/media_publish"
    post_data = {
        "access_token": user_access_token, 
        "creation_id": container_id
        }
    response = requests.post(post_url, params=post_data)
    post_id = response.json()['id']

    # Procedure for Reels and Carousels
    # https://developers.facebook.com/docs/instagram-api/guides/content-publishing

    # Post Return
    if response.status_code == 200:
        # success
        return post_id
    else:
        # failure
        return "Request failed with status code:", response.status_code, response.json()