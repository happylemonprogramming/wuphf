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

# Web Server Library
from flask import Flask, render_template, jsonify
from forms import CommentForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "tootiefrootiebigbootie42069$$$"

# Route for AI generated tweet and image generation
@app.route('/', methods=["GET", "POST"])
def index():
  test = {'ai_output': 'It worked! #blessed #frankiewillbeproud :)'}
  data = json.dumps(test)
  print(type(data))
  return data
  
# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) #Change host back to 0.0.0.0, if needed