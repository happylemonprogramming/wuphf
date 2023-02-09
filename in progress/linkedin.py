import requests

# Define the LinkedIn API endpoint for making a post
post_url = "https://api.linkedin.com/v2/ugcPosts"

# Define the access token for the LinkedIn API
access_token = "AQVz9GYvZpozByKdynfyI6fyJ7dHcSLTgshAZPyTeq7uXLnMu_4lkynpR1ED-_hb3-As5qpSs7iUuz-h1piD_SKB4fOTY9kR4IudipTH1xIv9ks_RJXAScJWL2JCTH3Km2bEuwRKf_jRZvMTAngqSC-3XdhqaT7z7hKG2jEMLhxHFdj6oxDwQy4rfqFV7ZEdVKATa7q34FvqNdb2x2Nn5f3Q7d0vfUvE7fwfYub1qwWKLxsvH0Gn5lFkEAlXkO39buYxw-MSiTBi-BxwU7M4KmorZWo_9ZIi57DjRO4Wcn_tNn8viJX3OuAv56K6ux3v4c0m5PH3j1Khx5IVEoVYdUV4zO7ZCA"

# Define the headers for the API request
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Define the post data
post_data = {
    "author": "urn:li:company:90460264", #can only get from 'r_liteprofile' permissions
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello from the LinkedIn API!"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

# Make the API request to create a post
response = requests.post(post_url, headers=headers, json=post_data)

# Check the status code of the API response
if response.status_code == 201:
    print("Post created successfully!")
else:
    print(f"Error creating post: {response.text}")


