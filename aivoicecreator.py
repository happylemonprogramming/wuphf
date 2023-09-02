from elevenlabs import generate, play, voices, set_api_key, stream, save
import os
import requests

set_api_key(os.environ.get('elevenlabsapikey'))

def aispeech(text=None,voice='Bella',output='speechoutput.wav',text_file=None):
    voiceList = ['Rachel', 'Domi', 'Bella', 'Antoni', ' Elli', 'Josh', 'Arnold', 'Adam', 'Sam']
    putin = '2tfqZPGDSMcLjnTVNO2o'
    # rachel is meh, domi is female, bella best story teller, elli is kiddish
    # josh is rugged, arnold is like a car salesman, energetic, adam is more news anchor, sam is teenager (male)

    if text_file != None:
        # Open the text file in read mode
        with open(text_file, 'r') as file:
            # Read the entire contents of the file into a variable
            text = file.read()

    # for voice in voiceList:
    audio = generate(
    text=text,
    voice=voice,
    # voice=voiceList[voice_index],
    model="eleven_monolingual_v1")

    save(audio, output)
    return output


def addvoice(audio,name):
    url = "https://api.elevenlabs.io/v1/voices/add"

    headers = {
    "Accept": "application/json",
    "xi-api-key": os.environ.get('elevenlabsapikey')}

    data = {
        'name': name}

    files = [
        ('files', (audio, open(audio, 'rb'), 'audio/mpeg'))]

    response = requests.post(url, headers=headers, data=data, files=files)
    output = response.text

    return output