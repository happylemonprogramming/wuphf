# Use the media_upload method to upload the image to Twitter
import tweepy
import requests

# Replace these values with your own Twitter API credentials
# Need to make private!
consumer_key = "hbZzwAJE94vjuVpvEURtKfGXR"
consumer_secret = "lowCf0fsfKPOKwU9vtzDxwOMwsIxLd2SWiQYsa6ZzzQE3msB0Q"
access_token = "1373830285607899136-pVXqgGJSIVdeu5rb4G3x6QyTDaDHrd"
access_token_secret = "5jtSSfgTYq3bx7bhaXMHaLfeWXPqBozlJYwN6xzUeaPsb"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def tweet_video(status,media):
    upload = api.media_upload(media) #Didn't work, but didn't error
    api.update_status(status=status, media_ids=[upload.media_id_string])
    # api.chunked_upload(media) #Throws an error
    return None

# Function to have text completion AI create a status and image based on prompt
def tweet(status, media):
    # tweet with image if local file
    # api.update_status_with_media(status, media)

    url = media
    response = requests.get(url)

    # tweet image and status
    with open("image.png", "wb") as f:
        f.write(response.content)
    api.update_status_with_media(status, 'image.png')
    message = "Tweeted Successfully!"
    return message

# Function to get 'Home' timeline
def timeline():

    my_timeline = api.home_timeline()

    # Return first timeline tweet, username and url
    return my_timeline[0].text,my_timeline[0].user.screen_name, my_timeline[0].user.url

# # Function to get the latest tweet
# def latest_tweet():

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

# Function to get embed html code for tweet url
def embed_tweet(tweet_url):
    embed = api.get_oembed(tweet_url) 
    # Split the string into a list of words
    words = embed['html'].split()
    # Iterate over the list of words
    links = []
    for word in words:
        # Check if the current word is not the word to keep
        if "http" in word:
            # Add word to list
            links.append(word)

    # Links list may contain multiple several links, likely in the order below
    # 1 and 2 http to ?, 3 is link to post, 4 is also link to post, 5 is widgets
    # Remove last 3 since they are consistent
    hashnoise = links[:-3] # 'noise' ecause it has lingering characters from split that aren't part of link
    hashtags = []
    i = 0
    for tag in hashnoise:
        start = hashnoise[i].find('http')
        end = hashnoise[i].find('?')
        hashtags.append(hashnoise[i][start:end])
        i = i+1

    return embed['html'], hashtags

