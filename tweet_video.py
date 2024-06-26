import os
import sys
import time

import json
import requests
from requests_oauthlib import OAuth1
import tweepy


MEDIA_ENDPOINT_URL = 'https://upload.twitter.com/1.1/media/upload.json'
POST_TWEET_URL = 'https://api.twitter.com/1.1/statuses/update.json'


# App specific
consumer_key = os.environ.get('twitter_consumer_key')
consumer_secret = os.environ.get('twitter_consumer_secret')
# User specific
access_token = os.environ.get('twitter_access_token')
access_token_secret = os.environ.get('twitter_access_token_secret')
# # OAuth 2.0 Client Tokens
# client_id = os.environ.get('twitter_client_id')
# client_secret = os.environ.get('twitter_client_secret')

def tweet_video(caption, imgurl, twitter_token, twitter_secret):

    oauth = OAuth1(consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=twitter_token,
    resource_owner_secret=twitter_secret)


    class VideoTweet(object):

        def __init__(self, file_name):
            '''
            Defines video tweet properties
            '''
            # # Check for https
            if 'https:' in file_name.lower() or 'http:' in file_name.lower():
                self.video_url = file_name
            else:
                self.video_url = "https:" + file_name
            print("Video URL: ", self.video_url)
            self.total_bytes = self.get_file_size(self.video_url)
            # self.video_filename = file_name #local file
            # self.total_bytes = os.path.getsize(self.video_filename) #local file
            self.media_id = None
            self.processing_info = None

        def get_file_size(self, url):
            '''
            Returns file size in bytes
            '''
            print("URL: ", url)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(url, headers=headers)
            print(response)
            response = requests.head(url)
            print("Response: ", response)
            if 'Content-Length' in response.headers:
                return int(response.headers['Content-Length'])
            else:
                raise ValueError('Unable to determine file size.')


        def upload_init(self):
            '''
            Initializes Upload
            '''
            print('INIT')

            request_data = {
            'command': 'INIT',
            'media_type': 'video/mp4',
            'total_bytes': self.total_bytes,
            'media_category': 'tweet_video'
            }

            req = requests.post(url=MEDIA_ENDPOINT_URL, data=request_data, auth=oauth)
            media_id = req.json()['media_id']

            self.media_id = media_id

            print('Media ID: %s' % str(media_id))


        def upload_append(self):
            '''
            Uploads media in chunks and appends to chunks uploaded
            '''
            segment_id = 0
            bytes_sent = 0
            # file = open(self.video_filename, 'rb') #local file
            resp = requests.get(self.video_url, stream=True)

            while bytes_sent < self.total_bytes:
                #   chunk = file.read(4*1024*1024) #local file
                chunk = resp.raw.read(4*1024*1024)
                
                print('APPEND')

                request_data = {
                    'command': 'APPEND',
                    'media_id': self.media_id,
                    'segment_index': segment_id
                }

                files = {
                    'media':chunk
                }

                req = requests.post(url=MEDIA_ENDPOINT_URL, data=request_data, files=files, auth=oauth)

                if req.status_code < 200 or req.status_code > 299:
                    print(req.status_code)
                    print(req.text)
                    sys.exit(0)

                segment_id = segment_id + 1
                #   bytes_sent = file.tell() #local file
                bytes_sent = bytes_sent + len(chunk)

                print('%s of %s bytes uploaded' % (str(bytes_sent), str(self.total_bytes)))

            print('Upload chunks complete.')


        def upload_finalize(self):
            '''
            Finalizes uploads and starts video processing
            '''
            print('FINALIZE')

            request_data = {
            'command': 'FINALIZE',
            'media_id': self.media_id
            }

            req = requests.post(url=MEDIA_ENDPOINT_URL, data=request_data, auth=oauth)
            print(req.json())

            self.processing_info = req.json().get('processing_info', None)
            self.check_status()


        def check_status(self):
            '''
            Checks video processing status
            '''
            if self.processing_info is None:
                return

            state = self.processing_info['state']

            print('Media processing status is %s ' % state)

            if state == u'succeeded':
                return

            if state == u'failed':
                sys.exit(0)

            check_after_secs = self.processing_info['check_after_secs']
        
            print('Checking after %s seconds' % str(check_after_secs))
            time.sleep(check_after_secs)

            print('STATUS')

            request_params = {
            'command': 'STATUS',
            'media_id': self.media_id
            }

            req = requests.get(url=MEDIA_ENDPOINT_URL, params=request_params, auth=oauth)
            
            self.processing_info = req.json().get('processing_info', None)
            self.check_status()

        # v1 Posting [Depracated]
        def tweet(self):
            '''
            Publishes Tweet with attached video
            '''
            request_data = {
            'status': caption,
            'media_ids': self.media_id
            }

            req = requests.post(url=POST_TWEET_URL, data=request_data, auth=oauth)
            # print(req.json())

        # v2 Posting
        def tweetv2(self):
            '''
            Publishes Tweet under new API version
            '''
            client = tweepy.Client(
                consumer_key=consumer_key, consumer_secret=consumer_secret,
                access_token=access_token, access_token_secret=access_token_secret
            )
            response = client.create_tweet(
                text=caption, media_ids=[self.media_id]
            )


    # if __name__ == '__main__':
    videoTweet = VideoTweet(imgurl)
    videoTweet.upload_init()
    videoTweet.upload_append()
    videoTweet.upload_finalize()
    videoTweet.tweetv2()