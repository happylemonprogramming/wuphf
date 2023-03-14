# OpenAI prompt generator
import openai
import os

# API Key
openai.api_key = os.environ["openaiapikey"]

def caption(tonality,influencer,tags):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Using the tags: {tags}, create a {tonality} post in tweet format in the voice of {influencer}: ',
        # prompt='Using the tags ' + tags + ', create a post in tweet format: ',
        # prompt='Take the following tags and put them into a tweet format: ' + user_prompt, # cuts off tweet
        # prompt='Using the tags ' + user_prompt + ', write a joke in tweet format: ', # terrible jokes
        # prompt='Using the tags ' + user_prompt + ', write a joke in the voice of Kevin Hart in tweet format: ', # hashtags Kevin Hart
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    AI_response = response['choices'][0]['text']
    cost = 0.02*(int(response['usage']['total_tokens']))/1000
    return AI_response, cost

def youtube_title(tonality,influencer,tags):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Using the tags: {tags}, create a {tonality} YouTube video title in the voice of {influencer}: ',
        # prompt='Using the tags ' + tags + ', create a post in tweet format: ',
        # prompt='Take the following tags and put them into a tweet format: ' + user_prompt, # cuts off tweet
        # prompt='Using the tags ' + user_prompt + ', write a joke in tweet format: ', # terrible jokes
        # prompt='Using the tags ' + user_prompt + ', write a joke in the voice of Kevin Hart in tweet format: ', # hashtags Kevin Hart
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    AI_response = response['choices'][0]['text']
    cost = 0.02*(int(response['usage']['total_tokens']))/1000
    return AI_response, cost

def youtube_description(tonality,influencer,tags):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Using the tags: {tags}, create a {tonality} YouTube video description in the voice of {influencer}: ',
        # prompt='Using the tags ' + tags + ', create a post in tweet format: ',
        # prompt='Take the following tags and put them into a tweet format: ' + user_prompt, # cuts off tweet
        # prompt='Using the tags ' + user_prompt + ', write a joke in tweet format: ', # terrible jokes
        # prompt='Using the tags ' + user_prompt + ', write a joke in the voice of Kevin Hart in tweet format: ', # hashtags Kevin Hart
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    AI_response = response['choices'][0]['text']
    cost = 0.02*(int(response['usage']['total_tokens']))/1000
    return AI_response, cost