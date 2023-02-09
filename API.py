# Build a twitter bot that posts an image and text based on user prompt input
import time
import datetime

# Other Python files and functions
from tweet import *
from caption import *
# from trash.folderread import *
from imagereadlightdark import *
from facebookgraphapi import *
# from instagram import *
import json
import random

# Web Server Library
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
# Should be an environmental variable
app.config["SECRET_KEY"] = "tootiefrootiebigbootie42069$$$"

# # Route for AI generated tweet and image generation
# @app.route('/', methods=["GET", "POST"])
# def index():
#   randomness = str(random.randint(1, 100))
#   test = {'ai_output': 'It worked! #blessed #frankiewillbeproud :)', 'random': randomness}
#   data = json.dumps(test)
#   print(type(data))
#   json_data = request.get_json()
#   print(json_data)
#   return 'JSON data: {}'.format(json_data)
  

# Route for AI generated text
@app.route('/', methods=["POST"])
def caption():
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


# Route for AI generated text
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
  output = {'Twitter': Twitter, 'Facebook': Facebook}
  api_response = json.dumps(output)

  return api_response

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) #Change host back to 0.0.0.0, if needed