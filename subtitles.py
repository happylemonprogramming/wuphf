from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

# video_clip = VideoFileClip("video_file.mp4")
# subtitles = SubtitlesClip("subtitles_file.srt", video_clip.size)

# result = CompositeVideoClip([video_clip, subtitles.set_position(("center", "bottom"))])

# result.write_videofile("result_file.mp4")


# import requests
# from io import BytesIO

# # Load the video file from URL
# response = requests.get("https://s3.amazonaws.com/appforest_uf/f1678940868271x564994871606250500/aistorytelling.py%20-%20Untitled%20%28Workspace%29%20-%20Visual%20Studio%20Code%202023-01-02%2011-12-25.mp4")
# video_file = BytesIO(response.content)
# video_clip = VideoFileClip(video_file)

# # Create subtitles clip from SRT file
# subtitles = SubtitlesClip("test.srt", video_clip.size, 
#                           font="Arial", fontsize=24, color="white")

# # Combine the video clip and subtitles clip using CompositeVideoClip
# result = CompositeVideoClip([video_clip, subtitles.set_position(("center", "bottom"))])

# # Write the result to a new video file
# result.write_videofile("result_file.mp4")

# import requests
# from io import BytesIO

# # Load the video file from URL
# response = requests.get("https://s3.amazonaws.com/appforest_uf/f1678940868271x564994871606250500/aistorytelling.py%20-%20Untitled%20%28Workspace%29%20-%20Visual%20Studio%20Code%202023-01-02%2011-12-25.mp4")
# video_file = BytesIO(response.content)

# # Save the video file to disk
# with open("video.mp4", "wb") as f:
#     f.write(video_file.getbuffer())

# # Load the video file from disk
# video_clip = VideoFileClip("video.mp4")

# # Create subtitles clip from SRT file
# subtitles = SubtitlesClip("test.srt", video_clip.size)

# # Combine the video clip and subtitles clip using CompositeVideoClip
# result = CompositeVideoClip([video_clip, subtitles.set_position(("center", "bottom"))])

# # Write the result to a new video file
# result.write_videofile("result_file.mp4")

import subprocess

input_video = 'video.mp4'
subtitle_file = 'test.srt'

def add_subtitle(input_video, subtitle_file):
    ffmpeg_cmd = ['ffmpeg', '-i', f'{input_video}', '-vf', f'subtitles={subtitle_file}', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'copy', '-y', 'captioned.mp4']

    subprocess.run(ffmpeg_cmd)

# Test
if __name__ == '__main__':
    add_subtitle(input_video, subtitle_file)