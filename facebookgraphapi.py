# This python script uses the facebook graph API to post an image to a business page
# The script also assumes you have a long lived access token

# Standard Libraries
import requests
import os
import time

# Environment Variables for Facebook Credentials
user_access_token = os.environ.get('meta_user_access_token')

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

    # Identify File Type
    filetype = str(media[-3:])
    print(filetype)
    media_url = 'https:'+media
    print(media_url)
    # Image Post
    if filetype == 'jpg' or filetype == 'png' or filetype == 'gif':
        print("IMAGE POST")
        post_url = f"https://graph.facebook.com/{page_id}/photos"
        post_data = {"message": caption, "url": media_url, "access_token": page_access_token}
        response = requests.post(post_url, json=post_data)
        print(response.json())

    # Video Post
    # https://developers.facebook.com/docs/video-api/guides/publishing/

    # Reel Post [EVENTUALLY SUCCESSFUL ON RETURN, BUT CAN'T FIND REELS POSTS ON PAGE]
    elif filetype == 'mp4':
        # Initialize Upload
        init_url = f"https://graph.facebook.com/v13.0/{page_id}/video_reels"
        # params = {'access_token': 'EAADI...'}
        init_data = {"upload_phase": "start", "access_token": page_access_token}
        response = requests.post(init_url, data=init_data)
        print("INITIALIZE UPLOAD: ", response.json())
        video_id=response.json()['video_id']

        # Upload Video
        upload_url = f'https://rupload.facebook.com/video-upload/v13.0/{video_id}'
        upload_headers = {'Authorization': 'OAuth '+page_access_token, 'file_url': media_url}
        response = requests.post(upload_url, headers=upload_headers)
        print("UPLOAD VIDEO: ", response.json())
        check = response.json()['success']

        status = None
        retry = 0
        while status != 'ready' and retry < 10:
            # Check Upload Status
            check_url = f'https://graph.facebook.com/v13.0/{video_id}'
            check_headers = {'Authorization': 'OAuth '+page_access_token}
            check_params = {'fields': 'status'}
            response = requests.get(check_url, headers=check_headers, params=check_params)
            print("CHECK UPLOAD STATUS: ", response.json())
            status = response.json()['status']['video_status']
            print(f'Video status is: {status}. Retry attempt: {retry}')
            time.sleep(30) # video processing takes a long time for facebook
            retry += 1
            if status == 'ready':
                # Publish
                url = f'https://graph.facebook.com/v13.0/{page_id}/video_reels'
                params = {'access_token': page_access_token}
                data = {'video_id': video_id, 'upload_phase': 'finish', 'video_state': 'PUBLISHED', 'description': caption}
                response = requests.post(url, params=params, data=data)
                print("PUBLISH: ", response.json())
            else:
                print('Video not ready')
                print(response.json())

    else:
        # Text Post
        post_url = f"https://graph.facebook.com/{page_id}/feed"
        post_data = {"message": caption, "access_token": page_access_token}
        response = requests.post(post_url, json=post_data)

    # Post Return
    if response.status_code == 200:
        # success
        return "Success!"
    else:
        # failure
        return "Request failed with status code:", response.status_code, response.json()