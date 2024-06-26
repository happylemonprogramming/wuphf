# This python script uses the instagram graph API to post an image
# to an instagram business account. The script assumes your instagram
# business account is connected to a facebook page. The script also
# assumes you have a long lived access token for the instagram business

# Standard Libraries
import requests
import os
import time

# Environment Variables for Facebook Credentials
user_access_token = os.environ.get('meta_user_access_token')

# API Function to post to Instagram
def instagram_post(caption, media, user_access_token):
    # # Check for https
    if 'https:' in media or 'http:' in media:
        pass
    else:
        media = "https:" + media

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
    # filetype = str(media[-3:])

    # if filetype == "jpg" or filetype == "png" or filetype == "gif":
    if "jpg" in media.lower() or "png" in media.lower() or "gif" in media.lower():
        container_data = {
            "access_token": user_access_token, 
            "image_url": media,
            "caption": caption
            }
    # elif filetype == "mp4":
    elif "mp4" in media.lower():
        container_data = {
            "access_token": user_access_token, 
            "media_type": "REELS",
            "video_url": media,
            "caption": caption
            }
    response = requests.post(container_url, params=container_data)
    print(response.json())
    container_id = response.json()['id']
    print(container_id)
    # # Post to Instagram
    check = None
    retry = 0
    while check is None and retry < 10:
        post_url = f"https://graph.facebook.com/{instabiz_id}/media_publish"
        post_data = {
            "access_token": user_access_token, 
            "creation_id": container_id
            }
        response = requests.post(post_url, params=post_data)
        # post_id = response.json()['id'] # Getting KeyError: 'id'

        # Procedure for Reels and Carousels
        # https://developers.facebook.com/docs/instagram-api/guides/content-publishing

        # Post Return
        if response.status_code == 200:
            # success
            check = "Success!"
            return check
        elif response.status_code == 400:
            check = None
            time.sleep(5)
            retry += 1
            print(response.json())
            print(f"Attempting to retry #{retry}")
        else:
            # failure
            check = "Failure!"
            return "Request failed with status code:", response.status_code, response.json()
        
if __name__ == "__main__":
    caption = "Started a new project last week. Text the first build at 19098940201. It's free until I run out of money. #AI #opensource #python #ChatGPT"
    videourl = 'https://db9c2d0e80dc9774067d0f439aa504a7.cdn.bubble.io/f1684127134722x917782188619789700/SMS%20AI%20Short%20-%20Made%20with%20Clipchamp%20%281%29.mp4?AWSAccessKeyId=AKIATBBF73RNGVJNFEZN&Expires=1684127529&Signature=4UerfLMJVnAnEZD7EPdJ4%2BPGK%2Fo%3D'
    test = instagram_post(caption, videourl, user_access_token)
    print(test)