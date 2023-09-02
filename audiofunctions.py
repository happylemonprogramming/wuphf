from pydub import AudioSegment
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import AudioFileClip, concatenate_audioclips
import subprocess
import os

# Add silence to a given 
def addsilence(input_mp3,output_mp3, duration):
    # Load the original MP3 file
    # input_mp3 = "input.mp3"
    # output_mp3 = "output_with_silence.mp3"
    audio = AudioSegment.from_file(input_mp3, format="mp3")

    # Duration of silence in milliseconds
    # duration = 3000  # Adjust as needed

    # Generate a silence audio segment
    silence = AudioSegment.silent(duration=duration)

    # Add silence before or after the audio
    audio_with_silence_before = silence + audio
    # Alternatively, to add silence after the audio: audio_with_silence_after = audio + silence

    # Export the audio with added silence as an MP3 file
    audio_with_silence_before.export(output_mp3, format="mp3")

# Multimedia overlay ___________________________________________________________________


def overlay_audio(file1, file2, output_path):
    audio1 = AudioSegment.from_file(file1)
    audio2 = AudioSegment.from_file(file2)
    combined = audio1.overlay(audio2)
    combined.export(output_path, format="wav")


# Reduce volume __________________________________________________________________________


def reduceaudiovolume(input_file, output_file, volume):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Reduce the volume by X% (adjust as needed)
    reduced_volume_audio = audio + (audio.dBFS * volume)
    print(reduced_volume_audio)
    # Export the adjusted audio
    reduced_volume_audio.export(output_file, format="wav")

def extract_audio(mp4_filename, audio_filename='videovoice.wav'):
    video_clip = VideoFileClip(mp4_filename)
    audio_clip = video_clip.audio

    audio_clip.write_audiofile(audio_filename)
    audio_clip.close()


def audioslicing(video_url, start, end):
    # Load the video clip
    video_clip = VideoFileClip(video_url)

    # Extract audio from the video clip
    audio = video_clip.audio

    # Export the audio to a temporary WAV file
    temp_audio_file = "temp_audio.wav"
    audio.write_audiofile(temp_audio_file)

    try:
        # Convert audio to AudioSegment for slicing
        audio_segment = AudioSegment.from_file(temp_audio_file)

        # Slice the audio segment
        sliced_audio = audio_segment[start:end]

        # Export sliced audio to the specified output filename
        output = 'audioslice.wav'
        sliced_audio.export(output, format='wav')
    finally:
        # Clean up: delete the temporary audio file
        os.remove(temp_audio_file)
    return output


def audiocombine(path1,path2):
    # Load audio clips
    clip1 = AudioFileClip(path1)
    clip2 = AudioFileClip(path2)

    # Concatenate audio clips
    concatenated_clip = concatenate_audioclips([clip1, clip2])

    # Export the concatenated clip
    output = 'concatenated_audio.wav'
    concatenated_clip.write_audiofile(output)
    return output

def add_new_audio(input_video, new_audio, subtitles=None, output_video='output.mp4'):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_video,
        '-i', new_audio,
        # '-vf', f'subtitles={subtitles}',
        '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
        '-c:a', 'aac', '-b:a', '192k',  # You can adjust the audio codec and bitrate as needed
        '-map', '0:v', '-map', '1:a',
        '-y', output_video
    ]
    subprocess.run(ffmpeg_cmd)

# def audioblocks(subtitles):
    # from datetime import timedelta
#     # Save subtitle lines in variable
#     with open(subtitles, 'r') as file:
#         subtitles = file.readlines()

#     # Convert the timestamp to a timedelta object at start
#     start = "00:00:00"
#     hours, minutes, seconds = map(int, start.split(':'))
#     start = timedelta(hours=hours, minutes=minutes, seconds=seconds)

#     # Initialize lists
#     timestamps = [start]
#     silence_blocks = []
#     talking_blocks = []
#     i = 0
#     # Sort through all timestamps
#     for timestamp in subtitles:
#         if ":" in timestamp:
#             # Convert the time string to a timedelta object
#             hours, minutes, seconds = map(int, timestamp[:8].split(':'))
#             stamp = timedelta(hours=hours, minutes=minutes, seconds=seconds)

#             # Look for silence by measuring the time difference between lines
#             if stamp > timestamps[-1]+timedelta(seconds=3):
#                 # Logic if silence at start of video
#                 if timestamps[-1] == '\n':
#                     first_stamp = stamp
#                     silence_blocks.append([start,first_stamp])
#                 # Logic for silence anywhere else
#                 else:
#                     silence_blocks.append([timestamps[-1],stamp])

#             # # If there's no silence break, capture talking blocks
#             else:
#                 if i==0 and len(silence_blocks)==1:
#                     talking_blocks.append([stamp,stamp])
#                 elif i>0 and len(silence_blocks)==1:
#                     talking_blocks[0][1] = stamp
#                 i+=1

#             timestamps.append(stamp)

#     print(talking_blocks) #TODO: figure this out
#     print(silence_blocks)
#     return silence_blocks,talking_blocks

# # Slow down audio:__________________________________________________________________________
# import numpy as np
# from scipy.io import wavfile
# from pydub import AudioSegment

# # Load the MP3 file
# input_mp3 = "input.mp3"
# output_mp3 = "output_slowed.mp3"
# audio = AudioSegment.from_file(input_mp3, format="mp3")

# # Slow down factor
# slow_down_factor = 0.8  # Adjust as needed (0.5 for half speed, 0.8 for 80% speed, etc.)

# # Convert AudioSegment to NumPy array
# samples = np.array(audio.get_array_of_samples())

# # Calculate new sample rate
# new_sample_rate = int(audio.frame_rate * slow_down_factor)

# # Resample the audio
# resampled_samples = np.interp(
#     np.arange(0, len(samples), 1.0 / slow_down_factor),
#     np.arange(0, len(samples)),
#     samples,
# )

# # Convert the resampled samples back to AudioSegment
# resampled_audio = AudioSegment(
#     data=resampled_samples.tobytes(),
#     sample_width=audio.sample_width,
#     frame_rate=new_sample_rate,
#     channels=audio.channels,
# )

# # Export the slowed down audio as an MP3 file
# resampled_audio.export(output_mp3, format="mp3")

# # Overlay clips__________________________________________________________________
# from pydub import AudioSegment


# # Load the audio clips
# clip1 = AudioSegment.from_file("clip1.mp3", format="mp3")
# clip2 = AudioSegment.from_file("clip2.mp3", format="mp3")

# # Determine the maximum length between the two clips
# max_length = max(len(clip1), len(clip2))

# # Adjust the length of the shorter clip
# clip1 = clip1.set_frame_rate(max_length)
# clip2 = clip2.set_frame_rate(max_length)

# # Overlay the clips
# overlayed_clip = clip1.overlay(clip2)

# # Export the overlayed clip
# overlayed_clip.export("overlayed_output.mp3", format="mp3")




# if __name__ == "__main__":
#     audio_files_to_overlay = [
#     ("input1.wav", "input2.wav", "output1.wav"),
#     ("input3.wav", "input4.wav", "output2.wav")
#     # Add more pairs as needed
#     ]

#     with Pool() as pool:
#         for file1, file2, output_file in audio_files_to_overlay:
#             pool.apply_async(overlay_audio, (file1, file2, output_file))

#         pool.close()
#         pool.join()

#     print("All audio files have been overlaid in parallel.")
