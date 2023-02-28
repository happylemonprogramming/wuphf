# Build an API for wuphf
# Standard library imports
import time
import datetime
import json
import random

# AI API
from caption import *

# Twitter API
from tweet import *
from twittertemptoken import *
from twitterpermanenttoken import *

# META API
from facebookgraphapi import *
from instagramgraphapi import *
from metakeygenerator import *

# Other Python files and functions
from imagereadlightdark import *

# Web Server Library
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
# Should be an environmental variable
app.config["SECRET_KEY"] = os.environ.get('flasksecret')

# __________________________________________________________________________________________________________________________________________________________
# Route for AI generated text
@app.route('/', methods=["POST"])
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

  # AI text generation
  response = caption(tonality,influencer,tags)
  # Transform to dictionary format
  dictionary = {"api_output": response[0], 'random': response[1]}
  # Transform to JSON
  api_response = json.dumps(dictionary)
  return api_response
# __________________________________________________________________________________________________________________________________________________________

# Route for mass social media posting
@app.route('/post', methods=["POST"])
def post():
  #Example JSON
    # JSON Body = {"name": "lemon", "caption": "it works! #yay #moneymaker", "imgurl":"aws.lemonissosmart.com/img"}
    # JSON Body = {
    #               'name': 'Lemon', 
    #               'caption': "\n\nJust when I thought I've seen it all, my buddy calls me to come over and watch a dinosaur and lemon battle. This ain't no ordinary fight club! #DaveChappelle, \n\nI just got struck by lightning while making a lemonade... oh well, at least the drink will be extra strong this time! #LightningLemon #DaveChappelle", 
    #               'imgurl': '//s3.amazonaws.com/appforest_uf/f1675978942446x792425085319267600/Lemon%20%26%20T-Rex.png, //s3.amazonaws.com/appforest_uf/f1675978976428x846564285372801800/Lightning%20%26%20Lemon%202.png', 
    #               'meta_key': 'EAAH4DU8nw4UBAHB6u6PtNoKkeUWOEz19BKVdZB7YJTlJG7c504VZCTuMe40gu51TbOIWJyFE9SZAwatdZBSzEZCLNFbrZBPTBIlOF9b6ZC9VS3J2Bd2LPy9kKtT3pAWvl8wuzPjhsK7N1WyEeZCLIHDlbPziG48d2DlZBXYKzL5lE8LLZCSqdJPm46', 
    #               'twitter_token': '1373830285607899136-pVXqgGJSIVdeu5rb4G3x6QyTDaDHrd', 
    #               'twitter_secret': '5jtSSfgTYq3bx7bhaXMHaLfeWXPqBozlJYwN6xzUeaPsb'}
  # Variable loading for JSON
  json_data = request.get_json()
  print("API JSON data: ")
  print(json_data)
  # dictionary_data = json.loads(json_data)
  # name = dictionary_data['name']
  # caption = list(dictionary_data['caption'])
  # imgurl = list(dictionary_data['imgurl'])
  # meta_key = dictionary_data['meta_key']
  # twitter_token = dictionary_data['twitter_token']
  # twitter_secret = dictionary_data['twitter_secret']
  # print(caption)
  # print(type(caption))
  # print(imgurl)
  # print(type(imgurl))
  name = json_data['name']
  captions = json_data['caption'][1:].split(', \n\n')
  imgurls = json_data['imgurl'].split(', ')
  meta_key = json_data['meta_key']
  twitter_token = json_data['twitter_token']
  twitter_secret = json_data['twitter_secret']

  print("API Twitter Token: " + twitter_token)
  print("API Twitter Secret: " + twitter_secret)
  i=0

  for caption in captions:
    imgurl = "https:" + imgurls[i]
    # Twitter submission
    Twitter = tweet(caption, imgurl, twitter_token, twitter_secret)
    # Facebook submission
    Facebook = facebook_post(caption, imgurl, meta_key)
    # Instagram submission
    Instagram = instagram_post(caption, imgurl, meta_key)
    i+=1


  output = {'Twitter': Twitter, 'Facebook': Facebook, 'Instagram': Instagram}
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

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True) # Change host back to 0.0.0.0, if needed or http(s)://127.0.0.1