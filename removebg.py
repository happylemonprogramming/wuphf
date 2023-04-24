# rnoLUbufSzBi8dMkytzqpcMj

# URL
import requests
import os
from io import BytesIO

# API Key
removebgapikey = os.environ["removebgapikey"]

def removebgurl(image_url, filename):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': image_url,
            'size': 'auto'
        },
        headers={'X-Api-Key': removebgapikey},
    )
    if response.status_code == requests.codes.ok:
        print(response)
        with open(filename, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

# # Local File
def removebglocal(image_path, filename):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        # files={'image_file': open(image_path, 'rb')}, # Local File
        files={'image_file': ('image.png', image_path, 'image/png')}, # Stream
        data={'size': 'auto'},
        headers={'X-Api-Key': removebgapikey},
    )
    if response.status_code == requests.codes.ok:
        print(response)
        stream = BytesIO(response.content) # Stream
        # with open(filename, 'wb') as out: # Local File
        #     out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
        stream = response.text
    return stream

if __name__ == "__main__":
    removebgurl('https://media.discordapp.net/attachments/939751705732599818/1099450888566865981/IMG_0395.jpg?width=744&height=993', 'piperedit.png')
    # var = removebglocal(r"C:\Users\clayt\Pictures\iPhone Import\IMG_0395.JPG", 'forjulie.png')
    # print(var)