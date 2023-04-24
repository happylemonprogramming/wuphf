import openai
import os

# API Key
openai.api_key = os.environ["openaiapikey"]

def texttoimage(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
    )

    print(response['data'][0]['url'])
    ai_output = response['data'][0]['url']
    cost = 0.02
    return ai_output, cost