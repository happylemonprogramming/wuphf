from deeptranscribe import *
from aivoicecreator import *
from audiofunctions import *
from pytube import YouTube
from cloud import *
import time

messi = 'https://www.youtube.com/watch?v=UCQiwICqINc'
maru = 'https://db9c2d0e80dc9774067d0f439aa504a7.cdn.bubble.io/f1692677290753x434684319755118660/RPReplay_Final1692675241.MP4'
maru = 'https://www.youtube.com/watch?v=taZ3STb5yak'
putin = 'https://www.youtube.com/watch?v=EkDwRJqcHSI'

def translatevideo(video,voice='Bella'):
	start = time.time()

	# If youtube
	if 'youtube' in video or 'youtu.be' in video:
		file = YouTube(video).streams.filter(progressive=True).order_by('resolution').last()
		file.download(filename='video.mp4')
		time.sleep(2) # Wait on save
		video = serverlink('video.mp4')

	# Transcribe video to text
	text = getDeepgramTranscription(video)
	raw_text = text['results']['channels'][0]['alternatives'][0]['transcript']
	subtitle_data = text['results']['channels'][0]['alternatives'][0]['words']
	paragraphs = text['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']

	# intialize lists
	sentences = []
	texts = []
	starts = []
	ends = []
	i = 0

	# gather all paragraphs into unified list
	for paragraph in paragraphs:
		sentences.append(paragraph['sentences'])

	# create text list, start list and end list
	for sentence in sentences:
		for text in sentence:
			texts.append(text['text'])
			starts.append(text['start'])
			ends.append(text['end'])

	# extract video audio
	extract_audio('video.mp4', audio_filename='videovoice.wav')

	# use speaker voice if elected
	if voice == 'Speaker':
		voice = addvoice('videovoice.wav', 'Speaker')
		voice = json.loads(voice)['voice_id']

	# make ai voice for text
	i = 0
	for text in texts:
		# Create voice from text
		aispeech(text=text, voice=voice, output = f'{i}.wav')
		i += 1
	print('Speech Files Created')
		
	# then add silence in front
	i = 0
	for start in starts:
		duration = int(float(start)*1000)
		addsilence(f'{i}.wav',f'{i}.wav', duration = duration)
		i += 1
	print('Files Prepended with Silence')

	# then overlay audio 
	i = 0
	for text in range(len(texts)):
		if i+1 >= len(texts):
			break
		try:
			overlay_audio(f'{i+1}.wav', f'{i}.wav', f'{i+1}.wav')
			i += 1
		except FileNotFoundError as e:
			print(f'Error: {e}')
			break  # Break the loop if a file is not found
	print('Speech Files Combined')

	# reduce video audio volume
	reduceaudiovolume('videovoice.wav', 'lowvolume.wav', 0.60)
	# combine final audio
	overlay_audio(f'lowvolume.wav', f'{len(texts)}.wav', f'donezo.wav')
	# add new audio to video file
	output_video = 'superdonezo.mp4'
	add_new_audio('video.mp4', 'donezo.wav', output_video=output_video)

	print(time.time()-start)
	return output_video, raw_text

if __name__ == '__main__':  
	import streamlit as st
	st.title("Video Translator")

	video_url = st.text_input('Paste video url:')
	local_file = st.file_uploader('Or upload your own:')
	voice = st.selectbox('Select AI generated voice:', ['Speaker','Rachel', 'Domi', 'Bella', 'Antoni', ' Elli', 'Josh', 'Arnold', 'Adam', 'Sam'])

	if st.button('Launch!'):
		if video_url:
			video = video_url
		if local_file:
			video = local_file

		st.success('Here is the original video:')
		st.video(video)

		# translatevideo(video)

		st.success('Here is the updated video:')
		st.video('superdonezo.mp4')

		# # Remove unnecessary files
		# if len(silence_blocks)>0:
		#     os.remove(background_audio)
		# if final_audio != aivoice_file:
		#     os.remove(final_audio)
		# os.remove(subtitle_file)
		# os.remove(aivoice_file)
		# st.success('Files removed')