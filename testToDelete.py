# Build an API for wuphf
# Standard library imports
import json
import requests
# Web Server Library
from flask import Flask, render_template, jsonify, request


# Twitter API
from tweet import *

# META API
from facebookgraphapi import *
from instagramgraphapi import *

def post(json_data):
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
#   json_data = request.get_json()
  print("API JSON data: ")
  print(json_data)
  dictionary_data = json.loads(json_data)
  name = dictionary_data['name']
  caption = list(dictionary_data['caption'])
  imgurl = list(dictionary_data['imgurl'])
  meta_key = dictionary_data['meta_key']
  twitter_token = dictionary_data['twitter_token']
  twitter_secret = dictionary_data['twitter_secret']
  print(caption)
  print(type(caption))
  print(imgurl)
  print(type(imgurl))
  name = json_data['name']
  # caption = json_data['caption']
  # imgurl = json_data['imgurl']
  # meta_key = json_data['meta_key']
  # twitter_token = json_data['twitter_token']
  # twitter_secret = json_data['twitter_secret']
  # print(caption)
  # print(type(caption))
  # print(imgurl)
  # print(type(imgurl))
  # print("API Twitter Token: " + twitter_token)
  # print("API Twitter Secret: " + twitter_secret)

  # Twitter submission
  Twitter = tweet(caption, imgurl, twitter_token, twitter_secret)
  # Facebook submission
  Facebook = facebook_post(caption, imgurl, meta_key)
  # Instagram submission
  Instagram = instagram_post(caption, imgurl, meta_key)
  output = {'Twitter': Twitter, 'Facebook': Facebook, 'Instagram': Instagram}
  api_response = json.dumps(output)

  return api_response

json_data = '''{'name': 'Lemon', 'caption': "\n\nJust when I thought I've seen it all, my buddy calls me to come over and watch a dinosaur and lemon battle. This ain't no ordinary fight club! #DaveChappelle, \n\nI just got struck by lightning while making a lemonade... oh well, at least the drink will be extra strong this time! #LightningLemon #DaveChappelle", 'imgurl': '//s3.amazonaws.com/appforest_uf/f1675978942446x792425085319267600/Lemon%20%26%20T-Rex.png, //s3.amazonaws.com/appforest_uf/f1675978976428x846564285372801800/Lightning%20%26%20Lemon%202.png', 'meta_key': 'EAAH4DU8nw4UBAHB6u6PtNoKkeUWOEz19BKVdZB7YJTlJG7c504VZCTuMe40gu51TbOIWJyFE9SZAwatdZBSzEZCLNFbrZBPTBIlOF9b6ZC9VS3J2Bd2LPy9kKtT3pAWvl8wuzPjhsK7N1WyEeZCLIHDlbPziG48d2DlZBXYKzL5lE8LLZCSqdJPm46', 'twitter_token': '1373830285607899136-pVXqgGJSIVdeu5rb4G3x6QyTDaDHrd', 'twitter_secret': '5jtSSfgTYq3bx7bhaXMHaLfeWXPqBozlJYwN6xzUeaPsb'}'''
json_input = json.dumps(json_data)
dictionary_data = json.loads(json_data)
print(dictionary_data['name'])
