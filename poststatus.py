#OpenAI prompt generator
import openai

openai.api_key_path = '/Users/clayt/Documents/Programming/APIs/OpenAI API/AI.txt'

def poststatus(user_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt='Using the tags ' + user_prompt + ', create a post in tweet format: ',
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
