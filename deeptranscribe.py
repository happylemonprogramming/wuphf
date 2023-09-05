from deepgram import Deepgram
import asyncio
import json
import os
import requests

DEEPGRAM_API_KEY = os.environ["deepgramapikey"]

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

def extract_sentences_from_srt(srt):
    # Save subtitle lines in variable
    with open(srt, 'r') as file:
        subtitles = file.readlines()
    
    # Initialize list and sort through subtitle lines
    words = []
    for word in subtitles:
        try:
            int(word)
        except:
            if ':' in word:
                pass
            elif word.strip() == '':
                pass
            else:
                words.append(word.strip())

    # Convert the list of words into a single string
    text = ' '.join(words)
    return text

def convert_to_srt(data, path, level='sentence'):
    print('Data input type: ', type(data))
    word_level = data['words']
    sentence_level = data['paragraphs']['paragraphs']

    def format_time(seconds):
        # Convert seconds to hours, minutes, seconds, milliseconds format
        hours, remainder = divmod(seconds, 3600)
        minutes, remainder = divmod(remainder, 60)
        seconds, milliseconds = divmod(remainder, 1)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(milliseconds*1000):03d}"

    if level == 'word':
        # Word-Level
        data = word_level
        output_filename = path + 'word_level.srt'
        with open(output_filename, 'w') as f:
            for i, entry in enumerate(data, start=1):
                start_time = format_time(entry['start'])
                end_time = format_time(entry['end'])
                subtitle_text = entry['punctuated_word']
                f.write(f"{i}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{subtitle_text}\n\n")

    elif level == 'sentence':
        # Sentence-Level
        output_filename = path + 'sentence_level.srt'

        # intialize lists
        sentences = []
        texts = []
        starts = []
        ends = []
        i = 0

        # gather all paragraphs into unified list
        for paragraph in sentence_level:
            sentences.append(paragraph['sentences'])

        # create text list, start list and end list
        for sentence in sentences:
            for text in sentence:
                # TODO: Add sentence subtitles
                texts.append(text['text'])
                starts.append(text['start'])
                ends.append(text['end'])

        with open(output_filename, 'w') as f:
            for i, entry in enumerate(texts, start=1):
                start_time = format_time(starts[i-1])
                end_time = format_time(ends[i-1])
                subtitle_text = texts[i-1]
                f.write(f"{i}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{subtitle_text}\n\n")
            
    return output_filename

# async def DeepgramWait(file):

#     # Initialize the Deepgram SDK
#     deepgram = Deepgram(DEEPGRAM_API_KEY)

#     # FILE = 'https://s3.amazonaws.com/appforest_uf/f1678940868271x564994871606250500/aistorytelling.py%20-%20Untitled%20%28Workspace%29%20-%20Visual%20Studio%20Code%202023-01-02%2011-12-25.mp4'
#     if 'http' in file:
#         source = {'url': file}
#         response = await asyncio.create_task(
#             deepgram.transcription.prerecorded(
#                 source, {'model': 'whisper-large','language': 'en', 'punctuate': 'true','diarize': 'true', 'smart_format': 'true'}
#                 # model=whisper-large&language=en&punctuate=true&diarize=true&smart_format=true
#             )
#         )

#     else:
#         with open(file, 'rb') as video:
#             # ...or replace mimetype as appropriate
#             source = {'buffer': video, 'mimetype': 'video/mp4'}

#             response = await asyncio.create_task(
#                 deepgram.transcription.prerecorded(
#                     source, {'model': 'whisper-large','language': 'en', 'punctuate': 'true','diarize': 'true', 'smart_format': 'true'}
#                     # model=whisper-large&language=en&punctuate=true&diarize=true&smart_format=true
#                 )
#             )

#     output = json.dumps(response)
#     return output

# async def DeepgramTranscribe(filepath):
#     # Initializes the Deepgram SDK
#     deepgram = Deepgram(DEEPGRAM_API_KEY)
    
#     if 'http' in filepath:
#         source = {'url': filepath}
#         response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
#     else:
#         with open(filepath, 'rb') as video:
#             # ...or replace mimetype as appropriate
#             source = {'buffer': video, 'mimetype': 'video/mp4'}
#             response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
    
#     return json.dumps(response)

# if __name__ == '__main__':
    # p_url = 'https://db9c2d0e80dc9774067d0f439aa504a7.cdn.bubble.io/f1692677290753x434684319755118660/RPReplay_Final1692675241.MP4'
    # # p_url = 'https://s3.amazonaws.com/appforest_uf/f1678940868271x564994871606250500/aistorytelling.py%20-%20Untitled%20%28Workspace%29%20-%20Visual%20Studio%20Code%202023-01-02%2011-12-25.mp4'
    # output = getDeepgramTranscription(p_url)
    # subtitle_data = output['results']['channels'][0]['alternatives'][0]['words']

    # # Extract the filename from the URL
    # filename = os.path.basename(p_url)
    # name, extension = os.path.splitext(filename)
    # output_filename = 'test' + ".srt"

    # # write a subtitle (.srt) file with word-level timestamps
    # convert_to_srt(subtitle_data,output_filename)
    # Create an event loop and await the coroutine
    # loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(DeepgramTranscribe('video.mp4'))
    # loop.close()
    # print(result)
    # result = asyncio.run(DeepgramWait('video.mp4'))
    # print(result)
    # print(DeepgramTranscribe('video.mp4'))