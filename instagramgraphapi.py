import requests
# page_id = '109784668695709'
# page_access_token = 'EAAH4DU8nw4UBAJvZBXGi2k5DyAq9x5rGdECEGZAq55nEQvvWfpZASF0ZAQuFuhs9zxUrCV2RW5mmMGZBIfktYDaP3pJo2GcnSWC1XFpLU0XCzspl8fzrTuiGmnwQcIcOz0w5J8SqhMZBcIZCIDV4EWEZCGkKwM9PZCUo17lb0dyKd3PxFX0Qei6Osun80mZBhWxQbOZCYQGt7KbmK507efIalL5'
# user_access_token = 'EAAH4DU8nw4UBAC11JO1oWMR9caQT88znQJ5a5zoft4E0TSsJq2zX7bzJzrQZAdSZCuMAvgvzFZBTztauemvoXtHfbENOA4k0c7z7qjR54zwe6JSHVgWZCLMwyQg6YrXTbV191rknZAIVXguTt6fflPJfDXUAAEk7HHSzFNETQQyAmRtJXQMTGHspy9ZBebDVr4TrpqCGwcMMvkZAgRaoC0u8imEzPNFns8ZD'
# user_access_token = 'EAAH4DU8nw4UBAEN4yStJD7pN97BrQawZB8dk84ZBwJOl7Q1FWJhMvDo00WwiEkrbDdxZBa3V0ttnBhoZCWZBSHPHZCBbovjQxHPZC7ZC6xqodBiQAZAZCO837A9ikbDLIFC6WuOPmEoCW7Cpj25S0Krd7hx4TqpZB7ikFByLh4ZBBvuwrcNUtvLFoCGIR7YsdSuZBhvyZAHVDczHEJtQFeJ6X200WS'
long_token = {'access_token': 'EAAH4DU8nw4UBACivuCaPZCI7t3gg0o3RffYRu60OZBxG4MvinT5vZAgUe2tfnNaUsn7PMrTpHAQlDCCkeWx6lYmbcaw2vxIclMUZA7ept8j61lgGKjeP3ZC8ZCc4NNcHt2VeFEaukfcz3VWO3U0JbJ7WPIjY2GMj54khhvG1A7ZBnJdwM8LYZA0ZA', 'token_type': 'bearer', 'expires_in': 5173275}
user_access_token = long_token['access_token']

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

    # # Post to Container
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