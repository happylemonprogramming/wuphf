from tweet import *
from facebookgraphapi import *
from instagramgraphapi import *
from nostrpublish import *
# from youtube import *
import time
import datetime

# Imported arguments from API
if len(sys.argv) > 1:
    print(sys.argv, len(sys.argv))
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
    facebook_key = sys.argv[4]
    twitter_token = sys.argv[5]
    twitter_secret = sys.argv[6]
    instagram_key = sys.argv[12]
    nostr_key = sys.argv[13] #TODO: make part of workflow
    print('Nostr Key: ', nostr_key)
    print('Twitter Keys: ', twitter_secret, twitter_token)
    print('Facebook Key: ', facebook_key)
    print('Instagram Key: ', instagram_key)

else:
    print('No arguments')


# TODO: For YouTube
# tags = sys.argv[8]
# tonality = sys.argv[9]
# influencer = sys.argv[10]
# i = sys.argv[11]

# For 1 post_________________________________________________________
# Parse the input string into a datetime object
target_date_str = post_time
target_date = datetime.datetime.strptime(target_date_str, "%b %d %Y %I:%M %p")

# Add hours to target_date to convert to UTC (Universal Time Coordinated)
# target_date += datetime.timedelta(hours=7) # 8 hours for PST less 1 for DST
target_date += datetime.timedelta(hours=3) # +4 hours for EST, 3 for Texas

print('Requested Media: ', imgurl)
print('Requested Caption: ', caption)
print('Requested Time: ', post_time)
print('wuphf Converted Date: ', target_date)
print('Server Datetime: ', datetime.datetime.now())

# Check if target_date is in the future
while datetime.datetime.now() < target_date:
    time.sleep(60)  # Wait for 1 minute
else:
    start_time = time.time()
    print('wuphf.py is running')
    # Nostr submission
    try:
        if nostr_key != 'None':
            print('Nostr Post Processing')
            kind = 1
            Nostr = nostrpost(nostr_key,kind,caption,imgurl,None,None)
            print('Nostr Completed')
    except:
        print('Nostr Post Error')
    # Twitter submission
    try:
        if twitter_secret != 'None' or twitter_token != 'None':
            print('Twitter Post Processing')
            Twitter = tweet(caption, imgurl, twitter_token, twitter_secret)
            print('Twitter Completed')
    except:
        print('Twitter Post Error')

    # Facebook submission
    try:
        if facebook_key != 'None':
            print('Facebook Post Processing')
            Facebook = facebook_post(caption, imgurl, facebook_key)
            print('Facebook Completed')
    except:
        print('Facebook Post Error')

    # Instagram submission
    try:
        if instagram_key != 'None':
            print('Instagram Post Processing')
            Instagram = instagram_post(caption, imgurl, instagram_key)
            print('Instagram Completed')
    except:
        print('Instagram Post Error')

    # # YouTube submission [NEED TO FIGURE OUT CALLBACK URI FROM CLIENT_SECRETS.JSON]
    # if imgurl.endswith('mp4'):
    #     YouTube = youtube_upload(imgurl, youtube_key, name, tonality, influencer, tags)
    #     youtube_time = time.time()-relay3
    #     print('YouTube time: ', youtube_time)

    total_time = time.time()-start_time
    print('Total time: ', total_time)


# # Multipost_________________________________________________________
# target_date_list = post_time
# for i in range(len(target_date_list)):
#     target_date = datetime.datetime.strptime(target_date_list[i], "%b %d %Y %I:%M %p")
    
#     # Add 8 hours to target_date to convert to UTC (Universal Time Coordinated)
#     target_date += datetime.timedelta(hours=7) # 8 hours for PST less 1 for DST

#     # Heroku Notification
#     print('Post Time: ', target_date)
#     print('Server Datetime: ', datetime.datetime.now())

#     # Check if target_date is in the future
#     while datetime.datetime.now() < target_date:
#         time.sleep(60)  # Wait for 1 minute
#     else:
#         start_time = time.time()
#         # Heroku Notification
#         print('wuphf.py is running')

#         # Twitter submission
#         Twitter = tweet(caption[i], imgurl[i], twitter_token, twitter_secret)
#         twitter_time = time.time()-start_time
#         relay1 = time.time()

#         # Heroku Notification
#         print('Twitter time: ', twitter_time)

#         # Facebook submission
#         Facebook = facebook_post(caption[i], imgurl[i], meta_key)
#         facebook_time = time.time()-relay1
#         relay2 = time.time()
#         # Heroku Notification
#         print('Facebook time: ', facebook_time)

#         # Instagram submission
#         Instagram = instagram_post(caption[i], imgurl[i], meta_key)
#         instagram_time = time.time()-relay2
#         relay3 = time.time()
#         # Heroku Notification
#         print('Instagram time: ', instagram_time)

#         # # YouTube submission [NEED TO FIGURE OUT CALLBACK URI FROM CLIENT_SECRETS.JSON]
#         # if imgurl.endswith('mp4'):
#         #     YouTube = youtube_upload(imgurl, youtube_key, name, tonality, influencer, tags)
#         #     youtube_time = time.time()-relay3
#         #     print('YouTube time: ', youtube_time)

#         # Heroku Notification of total time
#         total_time = time.time()-start_time
#         print('Total time: ', total_time)

# # 30 second video test
# twitter_time = 14.7 seconds
# Facebook_time = 24.7 seconds
# Instagram_time = 52.9 seconds
# youtube_time = 16.1 seconds
# total_time = 108.5 seconds