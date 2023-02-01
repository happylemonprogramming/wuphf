# Build a twitter bot that posts an image and text based on user prompt input
import time
import datetime

# Other Python files and functions
from tweet import *
from poststatus import *
from folderread import *
from imagereadlightdark import *
from facebook import *
from instagram import *
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
  

# Route for AI generated tweet and image generation
@app.route('/', methods=["POST"])
def post():
  #Example JSON
    # JSON Body = {"name": "lemon", "tonality": "spicy", "influencer": "vanilla ice",
    # "imgurl":"aws.lemonissosmart.com/img", "tags": "pickle bananas chimpanzees"}

  
  json_data = request.get_json()
  name = json_data['name']
  tonality = json_data['tonality']
  influencer = json_data['influencer']
  imgurl = json_data['imgurl']
  tags = json_data['tags']

  response = poststatus(tonality,influencer,tags)
  dictionary = {"api_output": response[0][3:], 'random': response[1]}
  api_response = json.dumps(dictionary)
  return api_response


# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) #Change host back to 0.0.0.0, if needed