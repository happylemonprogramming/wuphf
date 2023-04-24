# Supermeme API
import requests
import json
url = "https://2db6ff8c-58b2-4ff5-b4b1-a3cc5e161570.mock.pstmn.io/api/v1/meme/text"

payload = "{\n  \"text\": \"bitcoin and red meat\"\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
print(response.json()['memes'][0]['image'])