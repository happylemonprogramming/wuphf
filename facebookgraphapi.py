import requests
# page_id = '109784668695709'
# page_access_token = 'EAAH4DU8nw4UBAJvZBXGi2k5DyAq9x5rGdECEGZAq55nEQvvWfpZASF0ZAQuFuhs9zxUrCV2RW5mmMGZBIfktYDaP3pJo2GcnSWC1XFpLU0XCzspl8fzrTuiGmnwQcIcOz0w5J8SqhMZBcIZCIDV4EWEZCGkKwM9PZCUo17lb0dyKd3PxFX0Qei6Osun80mZBhWxQbOZCYQGt7KbmK507efIalL5'
user_access_token = 'EAAH4DU8nw4UBAC11JO1oWMR9caQT88znQJ5a5zoft4E0TSsJq2zX7bzJzrQZAdSZCuMAvgvzFZBTztauemvoXtHfbENOA4k0c7z7qjR54zwe6JSHVgWZCLMwyQg6YrXTbV191rknZAIVXguTt6fflPJfDXUAAEk7HHSzFNETQQyAmRtJXQMTGHspy9ZBebDVr4TrpqCGwcMMvkZAgRaoC0u8imEzPNFns8ZD'


def facebook_post(caption, media):
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