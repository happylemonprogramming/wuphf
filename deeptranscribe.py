from deepgram import Deepgram
import asyncio
import json
import os


DEEPGRAM_API_KEY = os.environ["deepgramapikey"]


# async def main():

#     # Initialize the Deepgram SDK
#     deepgram = Deepgram(DEEPGRAM_API_KEY)

#     FILE = 'https://s3.amazonaws.com/appforest_uf/f1678940868271x564994871606250500/aistorytelling.py%20-%20Untitled%20%28Workspace%29%20-%20Visual%20Studio%20Code%202023-01-02%2011-12-25.mp4'

#     source = {
#         'url': FILE
#     }

#     response = await asyncio.create_task(
#         deepgram.transcription.prerecorded(
#             source
#         )
#     )

#     print(json.dumps(response, indent=4))
#     output = json.dumps(response, indent=4)
# asyncio.run(main())


import requests
def getDeepgramTranscription(p_url):
    # Use this to get subtitles in English
    url = "https://api.deepgram.com/v1/listen?model=whisper-large&language=en&punctuate=true&diarize=true&smart_format=true"

    # Use this to get subtitles in the same language as the audio/video
    # url = "https://api.deepgram.com/v1/listen?model=whisper-large&detect_language=true"

    payload = {
        "url": p_url
    }

    headers = {
        "Authorization": 'Token ' + DEEPGRAM_API_KEY,
        "content-type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    output = response.json()
    return output

p_url = 'https://db9c2d0e80dc9774067d0f439aa504a7.cdn.bubble.io/f1692677290753x434684319755118660/RPReplay_Final1692675241.MP4'
# p_url = 'https://s3.amazonaws.com/appforest_uf/f1678940868271x564994871606250500/aistorytelling.py%20-%20Untitled%20%28Workspace%29%20-%20Visual%20Studio%20Code%202023-01-02%2011-12-25.mp4'
output = getDeepgramTranscription(p_url)

def convert_to_srt(data, output_filename):
    def format_time(seconds):
        # Convert seconds to hours, minutes, seconds, milliseconds format
        hours, remainder = divmod(seconds, 3600)
        minutes, remainder = divmod(remainder, 60)
        seconds, milliseconds = divmod(remainder, 1)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(milliseconds*1000):03d}"

    with open(output_filename, 'w') as f:
        for i, entry in enumerate(data, start=1):
            start_time = format_time(entry['start'])
            end_time = format_time(entry['end'])
            subtitle_text = entry['punctuated_word']
            f.write(f"{i}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{subtitle_text}\n\n")
    with open('test.txt', 'w') as f:
        for i, entry in enumerate(data, start=1):
            subtitle_text = entry['punctuated_word']
            f.write(f"{subtitle_text} ")

import os
subtitle_data = output['results']['channels'][0]['alternatives'][0]['words']

# Extract the filename from the URL
filename = os.path.basename(p_url)
name, extension = os.path.splitext(filename)
output_filename = 'test' + ".srt"

# write a subtitle (.srt) file with word-level timestamps
convert_to_srt(subtitle_data,output_filename)