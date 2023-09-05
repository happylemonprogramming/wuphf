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

def downloadvideo(url, local_filename):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for any errors in the response

        # Open a local file for writing in binary mode
        with open(local_filename, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive new chunks
                    local_file.write(chunk)

        print(f"Downloaded {local_filename} successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def translatevideo(video, voice='Bella', captions=False, filepath='files/'):
	start = time.time()

	if 'http' not in video:
		if '"' in video:
			video = video.strip('"')
		print(video)
		video = serverlink(video)
		downloadvideo(video, filepath+'video.mp4')

	elif 'youtube' in video or 'youtu.be' in video:
		# If youtube
		print('YouTube video detected')
		file = YouTube(video).streams.filter(progressive=True).order_by('resolution').last()
		file.download(filename=filepath+'video.mp4')
		print('Video saved locally')
		time.sleep(2) # Wait on save
		video = serverlink('video.mp4')
		print('Video saved in the cloud')

	else:
		downloadvideo(video, filepath+'video.mp4')

	# Transcribe video to text
	text = getDeepgramTranscription(video)
	print('Video transcribed')
	raw_text = text['results']['channels'][0]['alternatives'][0]['transcript']
	subtitle_data = text['results']['channels'][0]['alternatives'][0]
	# subtitle_data = text['results']['channels'][0]['alternatives'][0]['words']
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
			# TODO: Add sentence subtitles
			texts.append(text['text'])
			starts.append(text['start'])
			ends.append(text['end'])

	if captions:
		# Create word-level subtitle file
		subtitles = convert_to_srt(subtitle_data, path=filepath)
		print('Subtitles created')
	else:
		subtitles = None

	if voice != 'None':
		print('New audio requested')

		# extract video audio
		extract_audio(filepath+'video.mp4', audio_filename=filepath+'videovoice.wav')

		# use speaker voice if elected
		if voice == 'Speaker':
			file_size = os.path.getsize(filepath+'video.mp4')

			if file_size > 10*1024*1024:
				audio = AudioSegment.from_file(filepath+'videovoice.wav', format="wav")

				# Trim the audio to the desired duration
				trimmed_audio = audio[:61 * 1000]

				# Export the trimmed audio as a WAV file
				learningpath = filepath+'voicelearning.wav'
				trimmed_audio.export(learningpath, format="wav")
			else:
				learningpath = filepath+'videovoice.wav'

			voice = addvoice(learningpath, 'Speaker')
			# TODO: ERROR {"detail":{"status":"upload_file_size_exceeded",
			# "message":"A uploaded file is too large, please upload files with a maximum of 11MB."}}
			voice = json.loads(voice)['voice_id']
			print('Voice creation successful')

		# make ai voice for text
		# TODO: compare sentence length against .wav file length (speed up as needed?)
		i = 0
		for text in texts:
			# Create voice from text
			aispeech(text=text, voice=voice, output = filepath+f'{i}.wav')
			i += 1
		print('Speech Files Created')
			
		# then add silence in front
		i = 0
		for start in starts:
			duration = int(float(start)*1000)
			addsilence(filepath+f'{i}.wav',filepath+f'{i}.wav', duration = duration)
			i += 1
		print('Files Prepended with Silence')

		# then overlay audio 
		i = 0
		for text in range(len(texts)):
			if i+1 >= len(texts):
				break
			try:
				overlay_audio(filepath+f'{i+1}.wav', filepath+f'{i}.wav', filepath+f'{i+1}.wav')
				i += 1
			except FileNotFoundError as e:
				print(f'Error: {e}')
				break  # Break the loop if a file is not found
		print('Speech Files Combined')

		# reduce video audio volume
		reduceaudiovolume(filepath+'videovoice.wav', filepath+'lowvolume.wav', 0.90)
		# combine final audio
		new_audio = overlay_audio(filepath+f'lowvolume.wav', filepath+f'{len(texts)-1}.wav', filepath+f'donezo.wav')
	else:
		new_audio = None
		print('No new audio requested')

	# add new audio to video file
	output_video = filepath+'superdonezo.mp4'
	add_new_audio(filepath+'video.mp4', new_audio, subtitles, output_video)
	print('New video file creation attempted')

	print(time.time()-start)
	return output_video, raw_text

if __name__ == '__main__':  
	import streamlit as st
	st.title("Video Translator")

	video_url = st.text_input('Paste video url or file path:')
	voice = st.selectbox('AI generated voice:', ['None','Speaker','Bella','Josh'])
	cc = st.toggle('Subtitles')
	
	if st.button('Launch!'):
		if video_url:
			video = video_url

		translatevideo(video, voice=voice,captions=cc)

		st.success('Here is the original video:')
		st.video(r'files\video.mp4')



		st.success('Here is the updated video:')
		st.video(r'files\superdonezo.mp4')