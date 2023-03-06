# Use the media_upload method to upload the image to Twitter
import tweepy
import requests
from datetime import datetime
import os

# Resources
# Need to visit website below to implement logging in with Twitter:
# https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens#:~:text=Twitter%20allows%20you%20to%20obtain,having%20them%20authorize%20your%20application.
# User needs to have "Allow this app to be used to Sign in with Twitter?” option is enabled.
# https://developer.twitter.com/en/docs/authentication/guides/log-in-with-twitter
# https://developer.twitter.com/en/docs/authentication/api-reference/request_token

# App specific
consumer_key = os.environ.get('twitter_consumer_key')
consumer_secret = os.environ.get('twitter_consumer_secret')
# User specific
access_token = os.environ.get('twitter_access_token')
access_token_secret = os.environ.get('twitter_access_token_secret')
# OAuth 2.0 Client Tokens
client_id = os.environ.get('twitter_client_id')
client_secret = os.environ.get('twitter_client_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# Function to have text completion AI create a status and image based on prompt
def tweet(status, media, access_token, access_token_secret):
    # Common tweepy API code insert
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # identify filetype
    filetype = str(media[-3:])
    url = media
    response = requests.get(url)
    filename = f"media.{filetype}"

    # download media from user
    with open(filename, "wb") as f:
        f.write(response.content)

    # upload media to twitter
    if filetype == "jpg" or filetype == "png" or filetype == "gif" or filetype == "mp4":
    #     api.update_status_with_media(status, filename) #This method is deprecated
        mediaIDcreator = api.media_upload(filename)
        api.update_status(status, media_ids=[mediaIDcreator.media_id_string])
        message = "Success!"
    else:
        message = "Wrong File Upload Type!"
    return message

# def tweet_video(status,media,access_token,access_token_secret):
#     # Common tweepy API code insert
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth)

#     upload = api.media_upload(media) #Didn't work, but didn't error
#     api.update_status(status=status, media_ids=[upload.media_id_string])
#     # api.chunked_upload(media) #Throws an error
#     return None

# # Function to get 'Home' timeline
# def timeline(access_token,access_token_secret):
#     # Common tweepy API code insert
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth)

#     my_timeline = api.home_timeline()

#     # Return first timeline tweet, username and url
#     return my_timeline[0].text,my_timeline[0].user.screen_name, my_timeline[0].user.url

# # Function to get the latest tweet
# def latest_tweet():
    # # Common tweepy API code insert
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)
#     my_page = api.user_timeline(screen_name="lemonknowsall", count=1)

#     # Iterate over the tweets in the timeline
#     for tweet in my_page:
#         #URL position changes in tweets for some reason?
#         if tweet.entities['urls'] == []:
#             tweet_url = tweet.entities['media'][0]['expanded_url'][:-7] #Doesn't like Hercules because of /photo/1 suffix so I did [:-7], we'll see
#         else:
#             tweet_url = tweet.entities['urls'][0]['expanded_url']
#         if 'web' in tweet_url:
#             tweet_url = tweet_url.replace('i/web','lemonknowsall') #Sometimes happens? Maybe works?

#     return my_page[0].text, my_page[0].user.screen_name, tweet_url

# # Function to get embed html code for tweet url
# def embed_tweet(tweet_url, access_token, access_token_secret):
#     # Common tweepy API code insert
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth)

#     embed = api.get_oembed(tweet_url) 
#     # Split the string into a list of words
#     words = embed['html'].split()
#     # Iterate over the list of words
#     links = []
#     for word in words:
#         # Check if the current word is not the word to keep
#         if "http" in word:
#             # Add word to list
#             links.append(word)

#     # Links list may contain multiple several links, likely in the order below
#     # 1 and 2 http to ?, 3 is link to post, 4 is also link to post, 5 is widgets
#     # Remove last 3 since they are consistent
#     hashnoise = links[:-3] # 'noise' ecause it has lingering characters from split that aren't part of link
#     hashtags = []
#     i = 0
#     for tag in hashnoise:
#         start = hashnoise[i].find('http')
#         end = hashnoise[i].find('?')
#         hashtags.append(hashnoise[i][start:end])
#         i = i+1

#     return embed['html'], hashtags

# # Function to have text completion AI create a status and image based on prompt
# def schedule_tweet(status, media, access_token, access_token_secret): #Need to debug further and might be able to do solely on bubble.io
#     # Common tweepy API code insert
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth)
    
#     # tweet with image if local file
#     # api.update_status_with_media(status, media)
    
#     date='2023-02-20'
#     time='18:30:00'
#     year = int(date[0:4])
#     month = int(date[5:7])
#     day = int(date[8:10])
#     hour = int(time[0:2])
#     minute = int(time[3:5])
#     second = int(time[6:8])
#     scheduled_time = datetime(year, month, day, hour, minute, second)
#     url = media
#     response = requests.get(url)

#     # tweet image and status
#     with open("image.png", "wb") as f:
#         f.write(response.content)

#     api.update_status_with_media(status, 'image.png',scheduled_at=scheduled_time)
#     message = "Success!"
#     return message