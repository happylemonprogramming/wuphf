from tweet import *
from facebookgraphapi import *
from instagramgraphapi import *
# from youtube import *
import time
import datetime

# Imported arguments from API
# User Name
name = sys.argv[1]

# Post Content
caption = sys.argv[2]
imgurl = sys.argv[3]
post_time = sys.argv[7]
# Heroku Notification
print('How the Input is Received:')
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[7])
print('How the Input is Parsed:')
print(caption)
print(imgurl)
print(post_time)

# Key Storage
meta_key = sys.argv[4]
twitter_token = sys.argv[5]
twitter_secret = sys.argv[6]

# TODO: For YouTube
# tags = sys.argv[8]
# tonality = sys.argv[9]
# influencer = sys.argv[10]
# i = sys.argv[11]

# # For 1 post_________________________________________________________
# # Parse the input string into a datetime object
# target_date_str = youtube_key
# target_date = datetime.datetime.strptime(target_date_str, "%b %d, %Y %I:%M %p")

# # Add 8 hours to target_date to convert to UTC (Universal Time Coordinated)
# target_date += datetime.timedelta(hours=7) # 8 hours for PST less 1 for DST
# print('wuphf Youtube Key: ', youtube_key)
# print('wuphf Converted Date: ', target_date)
# print('Server Datetime: ', datetime.datetime.now())

# # Check if target_date is in the future
# while datetime.datetime.now() < target_date:
#     time.sleep(60)  # Wait for 1 minute
# else:
#     start_time = time.time()
#     print('wuphf.py is running')
#     # Twitter submission
#     Twitter = tweet(caption, imgurl, twitter_token, twitter_secret)
#     twitter_time = time.time()-start_time
#     relay1 = time.time()
#     print('Twitter time: ', twitter_time)
#     # Facebook submission
#     Facebook = facebook_post(caption, imgurl, meta_key)
#     facebook_time = time.time()-relay1
#     relay2 = time.time()
#     print('Facebook time: ', facebook_time)
#     # Instagram submission
#     Instagram = instagram_post(caption, imgurl, meta_key)
#     instagram_time = time.time()-relay2
#     relay3 = time.time()
#     print('Instagram time: ', instagram_time)
#     # # YouTube submission [NEED TO FIGURE OUT CALLBACK URI FROM CLIENT_SECRETS.JSON]
#     # if imgurl.endswith('mp4'):
#     #     YouTube = youtube_upload(imgurl, youtube_key, name, tonality, influencer, tags)
#     #     youtube_time = time.time()-relay3
#     #     print('YouTube time: ', youtube_time)
#     total_time = time.time()-start_time
#     print('Total time: ', total_time)



# Multipost_________________________________________________________
target_date_list = post_time
for i in range(len(target_date_list)):
    target_date = datetime.datetime.strptime(target_date_list[i]+"m", "%b %d, %Y %I:%M %p")
    
    # Add 8 hours to target_date to convert to UTC (Universal Time Coordinated)
    target_date += datetime.timedelta(hours=7) # 8 hours for PST less 1 for DST

    # Heroku Notification
    print('Post Time: ', target_date)
    print('Server Datetime: ', datetime.datetime.now())

    # Check if target_date is in the future
    while datetime.datetime.now() < target_date:
        time.sleep(60)  # Wait for 1 minute
    else:
        start_time = time.time()
        # Heroku Notification
        print('wuphf.py is running')

        # Twitter submission
        Twitter = tweet(caption[i], imgurl[i], twitter_token, twitter_secret)
        twitter_time = time.time()-start_time
        relay1 = time.time()

        # Heroku Notification
        print('Twitter time: ', twitter_time)

        # Facebook submission
        Facebook = facebook_post(caption[i], imgurl[i], meta_key)
        facebook_time = time.time()-relay1
        relay2 = time.time()
        # Heroku Notification
        print('Facebook time: ', facebook_time)

        # Instagram submission
        Instagram = instagram_post(caption[i], imgurl[i], meta_key)
        instagram_time = time.time()-relay2
        relay3 = time.time()
        # Heroku Notification
        print('Instagram time: ', instagram_time)

        # # YouTube submission [NEED TO FIGURE OUT CALLBACK URI FROM CLIENT_SECRETS.JSON]
        # if imgurl.endswith('mp4'):
        #     YouTube = youtube_upload(imgurl, youtube_key, name, tonality, influencer, tags)
        #     youtube_time = time.time()-relay3
        #     print('YouTube time: ', youtube_time)

        # Heroku Notification of total time
        total_time = time.time()-start_time
        print('Total time: ', total_time)

# # 30 second video test
# twitter_time = 14.7 seconds
# Facebook_time = 24.7 seconds
# Instagram_time = 52.9 seconds
# youtube_time = 16.1 seconds
# total_time = 108.5 seconds