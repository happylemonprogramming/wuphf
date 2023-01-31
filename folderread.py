import os
from tweet import tweet, tweet_video
from poststatus import *
from instagram import instagram_post
from facebook import facebook_post
import time

def folderread(folder, times):
# Get the names of the files in the 'images' folder
# folder = 'C:/Users/clayt/Pictures/AI Images/' # Maybe make this a user input on website alongside the prompt for demo
    path = repr(folder)
    paths = path[1:-1]
    filenames = os.listdir(paths)
    cost = 0

    for filename in filenames:
        response = poststatus(filename[0:-4])
        # print(response)

        # If video upload via special video function, else normal function
        if ".mov" or ".mp4" in filename:
            AI_reply = response[0][2:]
            cost = cost + response[1]
            tweet_video(str(AI_reply), paths + '/' + filename)
                # TODO: Maximum video upload is 30s on Tweepy
            # instagram_post(str(AI_reply), paths + '/' + filename)
                # TODO: instagram auto uploads as reels, which issues a pop-up; xpath below:
                # /html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button
            # facebook_post(str(AI_reply), paths + '/' + filename)
                # TODO: pop-up in the way "is not clickable at point (204, 97). Other element would receive the click:"
        elif ".jpg" or ".png" in filename:
        # else:
            AI_reply = response[0][2:]
            cost = cost + response[1]
            tweet(str(AI_reply),paths + '/' + filename)
            # instagram_post(str(AI_reply), paths + '/' + filename)
            # facebook_post(str(AI_reply), paths + '/' + filename)
        # Wait for X seconds
        time.sleep(times)
    return AI_reply, cost
