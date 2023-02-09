import google.auth
import googleapiclient.discovery
import requests

# First, create a credentials object and authorize an API client
creds, project_id = google.auth.default()
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=creds)

# Define the request body for the video post
request_body = {
    'snippet': {
        'title': 'My Example Video',
        'description': 'This is a sample video posted through the YouTube API.',
        'tags': ['example', 'api', 'video'],
        'categoryId': 22  # 22 is the ID for the "People & Blogs" category
    },
    'status': {
        'privacyStatus': 'private'  # or 'public', 'unlisted', etc.
    }
}

# Get the video data from the URL
response = requests.get('https://example.com/video.mp4')
video_data = response.content

# Make the request to create the video
response = youtube.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=video_data,
    media_mime_type='video/mp4'
).execute()

# The response will contain the video's ID, which you can use to access the video in the future
video_id = response['id']
print(f'Successfully posted video with ID: {video_id}')
