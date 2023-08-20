# Build an API for wuphf
# Standard library imports
import time
import datetime
import json
import random
import subprocess
import re

# AI API
from caption import *
from texttoimage import *
from removebg import *

# Twitter API
from tweet import *
from twittertemptoken import *
from twitterpermanenttoken import *

# META API
from facebookgraphapi import *
from instagramgraphapi import *
from metakeygenerator import *

# YouTube API
from youtube import *

# Strike API
from lightningpay import *
from qrcodegenerator import *

# # Other Python files and functions
# from imagereadlightdark import *

# Web Server Library
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
# Should be an environmental variable
app.config["SECRET_KEY"] = os.environ.get('flasksecret')

# __________________________________________________________________________________________________________________________________________________________
# Route for AI generated text
@app.route('/tags2captions', methods=["POST"])
def status():
  #Example JSON
    # JSON Body = {"name": "lemon", "tonality": "spicy", "influencer": "vanilla ice",
    # "imgurl":"aws.lemonissosmart.com/img", "tags": "pickle bananas chimpanzees"}

  # Variable loading for JSON
  json_data = request.get_json()
  name = json_data['name']
  tonality = json_data['tonality']
  influencer = json_data['influencer']
  imgurl = json_data['imgurl']
  tags = json_data['tags']
  # NOTE: using a list of tags of images would slow down the HTTP return; better to have the API called several times
  # NOTE: paradox exists that the more images that are uploaded, the more bubble work there is; but that's more reliable than running list in the API [worthwhile tradeoff]
  
  # if imgurl.endswith['.png', '.jpg', '.jpeg', '.gif']:
  # AI text generation
  response = caption(tonality,influencer,tags)
  # Transform to dictionary format
  dictionary = {'caption': response[0], 'cost': response[1]}

  # elif imgurl.endswith['.mp4']: #TODO: add video support for YouTube
  #   # AI text generation
  #   response = caption(tonality,influencer,tags)
  #   # AI video title & description generation
  #   title = youtube_title(tonality,influencer,tags)
  #   description = youtube_description(tonality,influencer,tags)
  #   # Total cost of AI text generation
  #   cost = response[1]+title[1]+description[1]
  #   # Transform to dictionary format
  #   dictionary = {'caption': response[0], 'title': title[0], 'description': description[0], 'cost': cost}
  # else:
  #   dictionary = {'caption': 'Error: Image format not supported', 'cost': 0}

  # Transform to JSON
  api_response = json.dumps(dictionary)
  return api_response
# __________________________________________________________________________________________________________________________________________________________

# Route for mass social media posting
@app.route('/post', methods=["POST"])
def post():
  #Example JSON
    # JSON Body = {
    #               'name': 'Lemon', 
    #               'caption': "\n\nJust when I thought I've seen it all, my buddy calls me to come over and watch a dinosaur and lemon battle. This ain't no ordinary fight club! #DaveChappelle, \n\nI just got struck by lightning while making a lemonade... oh well, at least the drink will be extra strong this time! #LightningLemon #DaveChappelle", 
    #               'imgurl': '//s3.amazonaws.com/appforest_uf/f1675978942446x792425085319267600/Lemon%20%26%20T-Rex.png, //s3.amazonaws.com/appforest_uf/f1675978976428x846564285372801800/Lightning%20%26%20Lemon%202.png', 
    #               'meta_key': 'abc123', 
    #               'twitter_token': 'abc-123', 
    #               'twitter_secret': 'abc123',
    #               'schedule': 'abc123',
    #               'influencer': 'Dave Chappelle',
    #               'tags': 'rocket space AI',
    #               'tonality': 'spicy'}

  # Variable loading for JSON
  print("NEW POST REQUEST HAS BEEN INITIATED")
  json_data = request.get_json()
  print('JSON data:', json_data)
  name = json_data['name']
  # Key management
  if 'facebook_key' in json_data:
    facebook_key = json_data['facebook_key']
  else:
    facebook_key = 'None'
  if 'instagram_key' in json_data:
    instagram_key = json_data['instagram_key']
  else:
    instagram_key = 'None'
  if 'meta_key' in json_data:
    meta_key = json_data['meta_key']
  else:
    meta_key = 'None'
  if 'twitter_token' and 'twitter_secret' in json_data:
    twitter_token = json_data['twitter_token']
    twitter_secret = json_data['twitter_secret']
  else:
    twitter_token = 'None'
    twitter_secret = 'None'

  # Key logic
  if 'twitter_secret' and 'twitter_token' and 'meta_key' not in json_data:
    output = {'Twitter': 'Optional', 'Facebook': 'Optional', 'Instagram': 'Optional'}
  # elif twitter_secret and twitter_token and meta_key != 'None':
  #   output = {'Twitter': 'Null', 'Facebook': 'Null', 'Instagram': 'Null'} #TODO: add errors
  else:
    # captions = json_data['caption'].split(',  ') #TODO: fix this hacky way of splitting the captions with double spaces
    captions = json_data['caption']
    captions = captions[:-15] #Remove last UNIX Timestamp (TODO: this assumes there is one; not true on initialization)
    # Split the string into a list of substrings, using UNIX Timestamp as the delimiter
    pattern = re.compile(r', 168\d{10}, ')
    captions = pattern.split(captions)
    captions = [content.strip('"') for content in captions if not content.strip().isdigit()]

    imgurls = json_data['imgurl'].split(', ')

    # Time management
    time_string = json_data['schedule'] #TODO: I think this needs to be split?
    # Split the string into a list of substrings, using ", " as the delimiter
    substrings = time_string.split(", ")

    post_times = []

    # Initialization hack
    if time_string == 'Aug 19 2023 3:09 pm':
      post_times.append[time_string]
    else:
      # Combine every two elements together in the list
      for i in range(0, len(substrings), 2):
          post_times.append(substrings[i] + " " + substrings[i+1])
      print('API Print Time 1:', post_times, len(post_times))

    tags = json_data['tags']
    tonality = json_data['tonality']
    influencer = json_data['influencer']
    i=0

    # Heroku Notification
    print('API Type: ', type(post_times)) #TODO: currently used for passing the date to the subprocess

    # Check if there are more captions than images
    if len(captions) != len(imgurls):
      listOfPosts = min(len(captions), len(imgurls))
    else:
      listOfPosts = len(captions)

    # Loop through all posts
    for item in range(listOfPosts): #TODO: can probably change 'item' for 'i' and then delete i = 0
      imgurl = imgurls[i]
      caption = captions[i]
      print(i)
      print(item)
      post_time = post_times[i]
      print('API Print Time 2:', post_time)
      print(item, imgurl, caption, post_time)
      # Post to social media via subprocess so customer return is immediate on Heroku and Bubble (otherwise timeouts trigger and re-post)
      subprocess.Popen(["python", "wuphf.py", name, caption, imgurl, facebook_key, twitter_token, twitter_secret, post_time, tags, tonality, influencer, str(i), instagram_key])
      i+=1
      # Heroku Notification
      print('There are ' + str(len(captions)) + ' captions. You just finished caption #' + str(i) + '.')

      # # Break loop if there are more than 2 posts
      # if i >= 2:
      #   print('BREAK CODE TO STOP POSTING') #Otherwise timeouts trigger and re-post
      #   break

    # Response back to Bubble
    output = {'Twitter': 'Check', 'Facebook': 'Check', 'Instagram': 'Check'} #TODO: add errors
      
  api_response = json.dumps(output)

  return api_response
# __________________________________________________________________________________________________________________________________________________________

# Route for Meta Key Generator
@app.route('/secret', methods=["POST"])
def secret():
  #Example JSON
    # JSON Body = {"code": "LKJalskjdfiojuiopFIOYuigasgfdjgfGjgjF", "redirecturl": "aws.lemonissosmart.com/img"}

  # Variable loading for JSON
  json_data = request.get_json()
  code = json_data['code']
  redirect_original = json_data['redirecturl']

  # Meta Key Generator
  long_key = get_access_token(redirect_original, code)
  api_response = json.dumps(long_key)

  return api_response
# __________________________________________________________________________________________________________________________________________________________

# Route for Twitter Token Generator
@app.route('/twittertoken', methods=["GET"])
def twittertoken():
  # Twitter Token Generator
  temp_token = get_twitter_temp_token()
  dictionary = {"oauth_token": temp_token[0], 'oauth_token_secret': temp_token[1]}
  api_response = json.dumps(dictionary)
  return api_response

# __________________________________________________________________________________________________________________________________________________________

# Route for Twitter Key Generator
@app.route('/twitterkey', methods=["POST"])
def twitterkey():
  #Example JSON
    # JSON Body = {"oauth_token": "yabbadabb", "oauth_verifier": "doooooooooooo"}

  # Variable loading for JSON
  json_data = request.get_json()
  oauth_token = json_data['oauth_token']
  oauth_verifier = json_data['oauth_verifier']
  print(json_data)

  # Twitter Key Generator
  twitter_key = get_twitter_permanent_token(oauth_token, oauth_verifier)
  dictionary = {"oauth_token": twitter_key[0], 'oauth_token_secret': twitter_key[1], 'user_id': twitter_key[2], 'screen_name': twitter_key[3]}
  api_response = json.dumps(dictionary)

  return api_response

# __________________________________________________________________________________________________________________________________________________________

# Route for Lightning Address Generation and Conversion Rate
@app.route('/lightning', methods=["GET"])
def lightning():
  # Lightning QR Code
  quote = lightning_quote()
  lninv = quote[0]
  conv_rate = quote[1]
  invid = quote[2]
  print(invid)
  dictionary = {"lninv": lninv, 'btcusdrate': conv_rate, "invoiceId": invid}
  api_response = json.dumps(dictionary)

  return api_response

# __________________________________________________________________________________________________________________________________________________________

# Route for Lightning Invoice Status
@app.route('/checkinvoice', methods=["POST"])
def checkinvoice():
  #Example JSON
  # JSON Body = {"oauth_token": "yabbadabb", "oauth_verifier": "doooooooooooo"}

  # Variable loading for JSON
  json_data = request.get_json()
  invoiceId = json_data['invoiceId']

  # Check Invoice Status
  status = invoice_status(invoiceId)
  dictionary = {"status": status}
  api_response = json.dumps(dictionary)

  return api_response

# __________________________________________________________________________________________________________________________________________________________

# Route for Lightning QR Code
@app.route('/qrcode', methods=["POST"])
def QR():
  #Example JSON
  # JSON Body = {"lninv": "lnbc1..."}

  # Variable loading for JSON
  json_data = request.get_json()
  print(json_data)
  lninv = json_data['lninv']
  # Lightning QR Code
  binaryimagedata = QR_Code(lninv)
  return binaryimagedata

# __________________________________________________________________________________________________________________________________________________________

# Route for AI generated text
@app.route('/emilyfunction', methods=["POST"])
def emily():
  #Example JSON
    # JSON Body = {"prompt": "create a caption for this:"}

  # Variable loading for JSON
  json_data = request.get_json()
  prompt = json_data['prompt']

  # AI generated text
  response = emily_function(prompt)
  
  # Transform to dictionary format
  dictionary = {'caption': response[0], 'cost': response[1]}

  # Transform to JSON
  api_response = json.dumps(dictionary)
  return api_response

# __________________________________________________________________________________________________________________________________________________________

# Route for AI generated image
@app.route('/aibackgroundimage', methods=["POST"])
def aibackgroundimage():
  #Example JSON
    # JSON Body = {"prompt": "create an image for this:"}

  # Variable loading for JSON
  json_data = request.get_json()
  prompt = json_data['prompt']

  # AI generated text
  response = texttoimage(prompt)
  
  # Transform to dictionary format
  dictionary = {'image_url': response[0], 'cost': response[1]}

  # Transform to JSON
  api_response = json.dumps(dictionary)
  return api_response

# __________________________________________________________________________________________________________________________________________________________

# Route for AI background removal
@app.route('/airemovebg', methods=["POST"])
def airemovebg():
  #Example JSON
    # JSON Body = {"image_url": "//s3...."}

  # Variable loading for JSON
  json_data = request.get_json()
  imgurl = json_data['image_url']

  # AI generated text
  response = removebgurl(imgurl, 'filename.jpg')
  
  # Transform to dictionary format
  dictionary = {'image_url': response[0], 'cost': response[1]}

  # Transform to JSON
  api_response = json.dumps(dictionary)
  return api_response

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True) # Change host back to 0.0.0.0, if needed or http(s)://127.0.0.1