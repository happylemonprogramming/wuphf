import os
import openai

openai.api_key = os.environ["openaiapikey"]

# while True:
#     question = input("\033[34mHow can I help?\n\033[0m")

#     if question.lower() == "exit":
#         print("\033[31mGoodbye!\033[0m")
#         break
    
#     completion = openai.Completion.create(
#         # model = "gpt-3.5-turbo",
#         # messages = [
#         #     {"role": "system", "content": "You are a helpful assistant. Answer the given question"},
#         #     {"role": "user", "content": question}
#         # ])
#         # model = "text-davinci-003",
#         # prompt=f'You are a helpful assistant. Answer the given question.\n{question}\nAI:'
#         model="text-davinci-003",
#         prompt=f'Context: You are a helpful assistant. Answer the given question.\nUser: {question}\nAI: ',
#         temperature=0.9,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0.0,
#         presence_penalty=0.6,
#         stop=[" Human:", " AI:"]
#     )

#     print("\033[32m" + completion['choices'][0]['text'] + "\n")





# # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# ENGINE_ID = 'gpt-3.5-turbo'
# url = f'https://api.openai.com/v1/engines/%7BENGINE_ID%7D/completions'
# response = requests.get(url, verify=False)


# openai.organization = "org-qIq4qMOf1N8KMCE0p767a77o"
# openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Model.list())

output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input()}
        # TODO consider recursive calls to the assistant that allows the assistant to have context
        # https://youtu.be/4jxBwSmMw8s video on making a chat bot in bubble
        #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        #{"role": "user", "content": "Where was it played?"}
    ]
)

cost = float(0.002 * int(output['usage']['total_tokens']))
print(output['choices'][0]['message']['content'])
print(f"Cost: ${cost}")