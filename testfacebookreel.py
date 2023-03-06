import requests
import os

user_access_token = os.environ.get('meta_user_access_token')
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

# Publish
url = f'https://graph.facebook.com/v13.0/{page_id}/video_reels'
params = {'access_token': page_access_token}
data = {'video_id': 9150088695016322, 'upload_phase': 'finish', 'video_state': 'PUBLISHED', 'description': 'testing'}
response = requests.post(url, params=params, data=data)
print("PUBLISH: ", response.json())