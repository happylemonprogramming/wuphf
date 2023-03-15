from tweet import *
from facebookgraphapi import *
from instagramgraphapi import *
# from youtube import *
import time

name = sys.argv[1]
caption = sys.argv[2]
imgurl = sys.argv[3]
meta_key = sys.argv[4]
twitter_token = sys.argv[5]
twitter_secret = sys.argv[6]
youtube_key = sys.argv[7]
tags = sys.argv[8]
tonality = sys.argv[9]
influencer = sys.argv[10]
i = sys.argv[11]


print(youtube_key)


import datetime
import time

# Parse the input string into a datetime object
target_date_str = youtube_key
target_date = datetime.datetime.strptime(target_date_str, "%b %d, %Y %I:%M %p")
print(target_date)
print(datetime.datetime.now())
if datetime.datetime.now() < target_date:
    print('i knew it')
while datetime.datetime.now() < target_date:
    time.sleep(60)  # Wait for 1 minute
else:
    start_time = time.time()

    # Twitter submission
    Twitter = tweet(caption, imgurl, twitter_token, twitter_secret)
    twitter_time = time.time()-start_time
    relay1 = time.time()
    print('Twitter time: ', twitter_time)
    # Facebook submission
    Facebook = facebook_post(caption, imgurl, meta_key)
    facebook_time = time.time()-relay1
    relay2 = time.time()
    print('Facebook time: ', facebook_time)
    # Instagram submission
    Instagram = instagram_post(caption, imgurl, meta_key)
    instagram_time = time.time()-relay2
    relay3 = time.time()
    print('Instagram time: ', instagram_time)
    # # YouTube submission [NEED TO FIGURE OUT CALLBACK URI FROM CLIENT_SECRETS.JSON]
    # if imgurl.endswith('mp4'):
    #     YouTube = youtube_upload(imgurl, youtube_key, name, tonality, influencer, tags)
    #     youtube_time = time.time()-relay3
    #     print('YouTube time: ', youtube_time)
    total_time = time.time()-start_time
    print('Total time: ', total_time)


# # 30 second video test
# twitter_time = 14.7 seconds
# Facebook_time = 24.7 seconds
# Instagram_time = 52.9 seconds
# youtube_time = 16.1 seconds
# total_time = 108.5 seconds