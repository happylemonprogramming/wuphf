# OpenAI prompt generator
import openai
import os

# API Key
openai.api_key = os.environ["openaiapikey"]

def caption(tonality,influencer,tags):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Using the tags: {tags}, create a {tonality} post in tweet format in the voice of {influencer} without referencing {influencer}: ',
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

    AI_response = response['choices'][0]['text'].replace('\n\n', '')
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


# def emily_function(prompt):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.9,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0.0,
#         presence_penalty=0.6,
#         stop=[" Human:", " AI:"]
#     )

#     AI_response = response['choices'][0]['text']
#     cost = 0.02*(int(response['usage']['total_tokens']))/1000
#     return AI_response, cost

def emily_function(prompt):
    try:
        # AI integration
        output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a social media manager."},
                # TODO consider allowing user to create their own prompt as a function
                # The prompt can be anything: a therapist, doctor, mechanic, friend, teacher, etc...
            {"role": "user", "content": prompt}
                # TODO consider recursive calls to the assistant that allows the assistant to have context
            ]
        )
        AI_response = output['choices'][0]['message']['content']
    except:
        AI_response = 'Try again later, AI server overloaded :('

    # Total AI cost
    cost = float(0.002 * int(output['usage']['total_tokens'])/1000)
    return AI_response, cost

if __name__ == '__main__':
    # print(caption('funny','Kevin Hart', 'bananas, chocolate, mint')[0])
    tags = ['berry-picking', 'farming','fresh','farm-to-table']
    tonality = 'inspring'
    influencer = 'Erin Benzakein'
    prompt = f'Using the tags: {tags}, create a {tonality} post in tweet format in the voice of {influencer} without referencing {influencer}.'
    output = emily_function(prompt)
    print(output[0])