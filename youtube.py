# Standard Python libraries
import httplib2
import os
import random
import sys
import time
import urllib.request
import io
import requests
import json
import random
from caption import youtube_title, youtube_description

# Youtube API libraries
from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload, MediaIoBaseUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from oauth2client.client import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google API Console at
# https://console.cloud.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.cloud.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted") # can have the user select

def youtube_upload(video_url, key, name, tonality, influencer, tags):
  #_____________________________________________________________
  # Credential function
  def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
      scope=YOUTUBE_UPLOAD_SCOPE,
      message=MISSING_CLIENT_SECRETS_MESSAGE)

    # key= '{"access_token": "ya29.a0AVvZVsrnJtHq-dI4c6a9Z_wsviPuOYlCaVP6wKsT0_hZY3TC8MG3-5nxVEJbI-9HgWvwpXNHb-CxzXEX_nboQassLgm8Q6s44Ik3QOXyw_PUhD8CTw7A6WvkBcMcBgKWgQR9PFc1Nhmsd4T3Tct4R0voeePjVeUaCgYKAfUSARASFQGbdwaIIBmFCH89f5TVHi-3DQcDQQ0166", "client_id": "1024637340506-mu8d453rjsf4570s4cpq4bpcusrgc79e.apps.googleusercontent.com", "client_secret": "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", "refresh_token": "1//06jLusM0ANN5MCgYIARAAGAYSNwF-L9Ir_nKCLOBbu4g2d5HT24yLPLkIZV4g-3fNRHGOK3vwKbScby2_6K9Dd2b90ALEXJDP7BI", "token_expiry": "2023-03-12T05:59:33Z", "token_uri": "https://oauth2.googleapis.com/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": null, "id_token_jwt": null, "token_response": {"access_token": "ya29.a0AVvZVsrnJtHq-dI4c6a9Z_wsviPuOYlCaVP6wKsT0_hZY3TC8MG3-5nxVEJbI-9HgWvwpXNHb-CxzXEX_nboQassLgm8Q6s44Ik3QOXyw_PUhD8CTw7A6WvkBcMcBgKWgQR9PFc1Nhmsd4T3Tct4R0voeePjVeUaCgYKAfUSARASFQGbdwaIIBmFCH89f5TVHi-3DQcDQQ0166", "expires_in": 3599, "scope": "https://www.googleapis.com/auth/youtube.upload", "token_type": "Bearer"}, "scopes": ["https://www.googleapis.com/auth/youtube.upload"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}'

    # instead of fighting the creation of this file, deliberately create it and save it as a string to pass back to samule  
    dictionary_output = json.loads(key)
    # Generate a 10-digit random number 
    identifier = random.randint(10**9, (10**10)-1)
    # File path to delete [DELETE FILE AFTER USING]
    file_path = f"{name}-{identifier}-oauth2.json"
    with open(file_path, "w") as f:
      json.dump(dictionary_output, f)

    # storage = Storage("%s-oauth2.json" % sys.argv[0])
    storage = Storage(file_path)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
      credentials = run_flow(flow, storage)
      # Read the file as a string
      with open(file_path) as json_file:
          new_key = json.load(json_file)
    else:
      new_key = key

    completion = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      http=credentials.authorize(httplib2.Http()))


    # return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    #   http=credentials.authorize(httplib2.Http()))
    return completion, file_path, new_key
  # _________________________________________________________________
  # def get_authenticated_service():
  #     flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
  #       scope=YOUTUBE_UPLOAD_SCOPE,
  #       message=MISSING_CLIENT_SECRETS_MESSAGE)

  #     credentials = run_flow(flow, StringStorage())

  #     return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  #       http=credentials.authorize(httplib2.Http()))

  # class StringStorage(Credentials):
  #     def __init__(self):
  #         self._credentials = None

  #     def put(self, credentials):
  #         self._credentials = credentials.to_json()

  #     def get(self):
  #         if self._credentials:
  #             return Credentials.from_json(self._credentials)
  #         else:
  #             return None
  #   # credentials_json = '{ "access_token": "YOUR_ACCESS_TOKEN", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "YOUR_REFRESH_TOKEN", "scope": "https://www.googleapis.com/auth/youtube.upload", "id_token": "YOUR_ID_TOKEN", "created": 1621554148 }'

  #   # credentials = Credentials.from_json(credentials_json)
  # _________________________________________________________________
  # Authorize the request and store authorization credentials.
  # def get_authenticated_service():
  #   flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, YOUTUBE_UPLOAD_SCOPE)
  #   credentials = flow.run_console()
  #   print(credentials)
  #   print(type(credentials))
  #   return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials = credentials)
    # Get credentials and create an API client
  # def get_authenticated_service():
  #   flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
  #       CLIENT_SECRETS_FILE, YOUTUBE_UPLOAD_SCOPE)
  #   credentials = flow.run_console()
  #   print(credentials)
  #   print(type(credentials))
  #   youtube = googleapiclient.discovery.build(
  #       YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=credentials)





    # _________________________________________________________________
  # # Upload function for local files
  # def initialize_upload(youtube):
  #   # # Tags seem to be optional
  #   # tags = None
  #   # if options.keywords:
  #   #   tags = options.keywords.split(",")

  #   body=dict(
  #     snippet=dict(
  #       title="hey dude",
  #       description="what's up",
  #       tags='test',
  #       # categoryId=options.category
  #       # Film & Animation (Category ID: 1)
  #       # Autos & Vehicles (Category ID: 2)
  #       # Music (Category ID: 10)
  #       # Pets & Animals (Category ID: 15)
  #       # Sports (Category ID: 17)
  #       # Short Movies (Category ID: 18)
  #       # Travel & Events (Category ID: 19)
  #       # Gaming (Category ID: 20)
  #       # Videoblogging (Category ID: 21)
  #       # People & Blogs (Category ID: 22)
  #       # Comedy (Category ID: 34)
  #       # Entertainment (Category ID: 24)
  #       # News & Politics (Category ID: 25)
  #       # Howto & Style (Category ID: 26)
  #       # Education (Category ID: 27)
  #       # Science & Technology (Category ID: 28)
  #       # Nonprofits & Activism (Category ID: 29)
  #       # Movies (Category ID: 30)
  #       # Anime/Animation (Category ID: 31)
  #       # Action/Adventure (Category ID: 32)
  #       # Classics (Category ID: 33)
  #       # Documentary (Category ID: 35)
  #       # Drama (Category ID: 36)
  #       # Family (Category ID: 37)
  #       # Foreign (Category ID: 38)
  #       # Horror (Category ID: 39)
  #       # Sci-Fi/Fantasy (Category ID: 40)
  #       # Thriller (Category ID: 41)
  #       # Shorts (Category ID: 42)
  #       # Shows (Category ID: 43)
  #       # Trailers (Category ID: 44)
  #       categoryId=22 
  #     ),
  #     status=dict(
  #       privacyStatus=VALID_PRIVACY_STATUSES[1] # private
  #     )
  #   )

  #   # Call the API's videos.insert method to create and upload the video.
  #   insert_request = youtube.videos().insert(
  #     part=",".join(body.keys()),
  #     body=body,
  #     # The chunksize parameter specifies the size of each chunk of data, in
  #     # bytes, that will be uploaded at a time. Set a higher value for
  #     # reliable connections as fewer chunks lead to faster uploads. Set a lower
  #     # value for better recovery on less reliable connections.
  #     #
  #     # Setting "chunksize" equal to -1 in the code below means that the entire
  #     # file will be uploaded in a single HTTP request. (If the upload fails,
  #     # it will still be retried where it left off.) This is usually a best
  #     # practice, but if you're using Python older than 2.6 or if you're
  #     # running on App Engine, you should set the chunksize to something like
  #     # 1024 * 1024 (1 megabyte).
  #     # media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
  #     media_body=MediaFileUpload("video.mp4", chunksize=-1, resumable=True)
  #   )

  #   resumable_upload(insert_request)


  # _________________________________________________________________
  # # Upload function for server files
  def initialize_upload(youtube, video_url):
    # Download the video file from the URL and create a MediaIoBaseUpload object
    video_content = requests.get('https:'+video_url).content
    video_stream = io.BytesIO(video_content)
    media = MediaIoBaseUpload(video_stream, mimetype='video/*', chunksize=-1, resumable=True)

    video_title = youtube_title(tonality, influencer, tags)
    video_description = youtube_description(tonality, influencer, tags)

    # Set the video metadata
    body=dict(
      snippet=dict(
        title=video_title[0], # can have AI generate title from tags
        description=video_description[0], # can have AI generate description from tags
        tags=tags, # can pull tags from bubble user database 
        categoryId=24 
      ),
      status=dict(
        privacyStatus=VALID_PRIVACY_STATUSES[1] # private
      )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
      part=",".join(body.keys()),
      body=body,
      media_body=media
    )

    resumable_upload(insert_request)






  # _________________________________________________________________

  # This method implements an exponential backoff strategy to resume a failed upload.
  def resumable_upload(insert_request):
  
    response = None
    error = None
    retry = 0
    while response is None:
      try:
        print("Uploading file...")
        status, response = insert_request.next_chunk()
        if response is not None:
          if 'id' in response:
            message = "Video id '%s' was successfully uploaded." % response['id']
          else:
            message = "The upload failed with an unexpected response: %s" % response
            exit(message)
      except HttpError as e:
        if e.resp.status in RETRIABLE_STATUS_CODES:
          error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                              e.content)
        else:
          raise
      except RETRIABLE_EXCEPTIONS as e:
        error = "A retriable error occurred: %s" % e

      if error is not None:
        print(error)
        retry += 1
        if retry > MAX_RETRIES:
          exit("No longer attempting to retry.")

        max_sleep = 2 ** retry
        sleep_seconds = random.random() * max_sleep
        print("Sleeping %f seconds and then retrying..." % sleep_seconds)
        time.sleep(sleep_seconds)

  # if __name__ == '__main__':
  # Execute user authentication and return YouTube service object
  youtube = get_authenticated_service()
  # Try to upload video
  try:
    # url = 'https://example.com/video.mp4' # Replace with the URL of the video you want to download
    # filename = 'video.mp4' # Replace with the desired filename for the saved file

    # urllib.request.urlretrieve(url, filename)
    # need to add logic for when video has downloaded, the upload it to the youtube account
    initialize_upload(youtube[0], video_url) # Upload the video where youtube[0] is the youtube service object tuple
  # Unless an error occurs
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
  # Delete file
  os.remove(youtube[1]) # Delete the credentials after upload
  return youtube[2]