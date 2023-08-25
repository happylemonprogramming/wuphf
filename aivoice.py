from elevenlabs import generate, play, voices, set_api_key, stream, save
import time
import os

set_api_key(os.environ.get('elevenlabsapikey'))

start = time.time()
voiceList = ['Rachel', 'Domi', 'Bella', 'Antoni', ' Elli', 'Josh', 'Arnold', 'Adam', 'Sam']
'''
rachel is meh
domi is female
bella best story teller
elli is kiddish
josh is rugged
arnold is like a car salesman, energetic
adam is more news anchor
sam is teenager (male)
'''

def aispeech(text,voice_index=2,output='speechoutput.wav',text_file=None):
    if text_file != None:
        # Open the text file in read mode
        with open(text_file, 'r') as file:
            # Read the entire contents of the file into a variable
            text = file.read()

    # for voice in voiceList:
    audio = generate(
    text=text,
    voice=voiceList[voice_index],
    model="eleven_monolingual_v1"
    )

    save(audio, output)
    print(time.time()-start)


'''
POTENTIAL NEXT STEPS:
Take video_url input
identify talking blocks and silence gaps
    look at .srt, if >5 seconds between words consider silence gap, else: talking block TODO: create function
    block 1 35 seconds of silence
    block 2 23 seconds of talking
    block 3 10 seonds of silence
    block 4 ...
split all silence blocks from url and name them by order (1,3,...)
use aispeech to create text to speech for talking blocks
    save files as order (2,...)
take all .wav files and stitch together
take original video file and overlay new stitched audio using ffmpeg
DONE
'''


from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import make_chunks
from moviepy.video.io.VideoFileClip import VideoFileClip

def audioslicing(video_url):
    # Load the video clip
    video_clip = VideoFileClip('input.mp4')

    # Extract audio from the video clip
    audio = video_clip.audio

    # Convert audio to AudioSegment for slicing
    audio_segment = AudioSegment.from_file(audio)

    start_time = 10000  # Start time in milliseconds
    end_time = 30000    # End time in milliseconds

    # Slice the audio segment
    sliced_audio = audio_segment[start_time:end_time]

    # Export sliced audio to a new .wav file
    sliced_audio.export('sliced_audio.wav', format='wav')


from pydub import AudioSegment

def audiocombine(folder_path):
    segment1 = AudioSegment.from_wav('segment1.wav')
    segment2 = AudioSegment.from_wav('segment2.wav')

    combined_audio = segment1 + segment2
    combined_audio.export('combined_audio.wav', format='wav')




if __name__ == '__main__':
    from datetime import datetime, timedelta

    # Save subtitle lines in variable
    with open("test.srt", 'r') as file:
        subtitles = file.readlines()

    # Convert the timestamp to a timedelta object at start
    start = "00:00:00"
    hours, minutes, seconds = map(int, start.split(':'))
    start = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    # Initialize lists
    timestamps = [start]
    silence_blocks = []
    talking_blocks = []
    # Sort through all timestamps
    for timestamp in subtitles:
        if ":" in timestamp:
            # Convert the time string to a timedelta object
            hours, minutes, seconds = map(int, timestamp[:8].split(':'))
            stamp = timedelta(hours=hours, minutes=minutes, seconds=seconds)

            # Look for silence by measuring the time difference between lines
            if stamp > timestamps[-1]+timedelta(seconds=3):
                # Logic if silence at start of video
                if timestamps[-1] == '\n':
                    silence_blocks.append([start,stamp])
                # Logic for silence anywhere else
                else:
                    silence_blocks.append([timestamps[-1],stamp])

            # # If there's no silence break, capture talking blocks
            # else:
            #     if len(talking_blocks)==0:
            #         first_word = stamp
            #         talking_blocks.append([first_word,stamp])
            #         last_word= talking_blocks[0][1]
            #     if stamp>talking_blocks[0][1]:
            #         talking_blocks = [first_word,stamp]
            
            # times = [34, 34, 35, 36, 37, 38, 40, 50, 52, 53, 54, 60, 61, 63]

            # talking_range = [stamp, stamp]

            # if stamp - talking_range[1] >= timedelta(seconds=3):
            #     talking_blocks.append(talking_range)
            #     talking_range = [stamp, stamp]
            # else:
            #     talking_range[1] = stamp

            # talking_blocks.append(talking_range)  # Add the last range



            timestamps.append(stamp)

    print(talking_blocks) #TODO: figure this out
    print(silence_blocks)



    # aispeech('yo yo yo, sweet baby thang! How you doin?', -1)