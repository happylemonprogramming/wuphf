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

  # Variable loading for JSON
  json_data = request.get_json()
  name = json_data['name']
  caption = json_data['caption']
  imgurl = json_data['imgurl']

  # Twitter submission
  Twitter = tweet(caption, imgurl)
  # Facebook submission
  Facebook = facebook_post(caption, imgurl)
  # Instagram submission
  Instagram = instagram_post(caption, imgurl)
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
  print(oauth_token)
  print(oauth_verifier)

  # Twitter Key Generator
  twitter_key = get_twitter_permanent_token(oauth_token, oauth_verifier)
  dictionary = {"oauth_token": twitter_key[0], 'oauth_token_secret': twitter_key[1], 'user_id': twitter_key[2], 'screen_name': twitter_key[3]}
  api_response = json.dumps(dictionary)

  return api_response

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True) # Change host back to 0.0.0.0, if needed or http(s)://127.0.0.1