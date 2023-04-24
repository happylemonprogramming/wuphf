import os
import openai

openai.api_key = os.environ["openaiapikey"]

while True:
    question = input("\033[34mHow can I help?\n\033[0m")

    if question.lower() == "exit":
        print("\033[31mGoodbye!\033[0m")
        break
    
    completion = openai.Completion.create(
        # model = "gpt-3.5-turbo",
        # messages = [
        #     {"role": "system", "content": "You are a helpful assistant. Answer the given question"},
        #     {"role": "user", "content": question}
        # ])
        # model = "text-davinci-003",
        # prompt=f'You are a helpful assistant. Answer the given question.\n{question}\nAI:'
        model="text-davinci-003",
        prompt=f'Context: You are a helpful assistant. Answer the given question.\nUser: {question}\nAI: ',
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    print("\033[32m" + completion['choices'][0]['text'] + "\n")