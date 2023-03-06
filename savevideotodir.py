# Saving Videos
import urllib.request

url = 'https:'+ '//s3.amazonaws.com/appforest_uf/f1677830552804x218224468465226800/father%20son%20travel%20to%20mars%20on%20rocketship.mp4' # Replace with the URL of the video you want to download
filename = 'video.mp4' # Replace with the desired filename for the saved file

urllib.request.urlretrieve(url, filename)


# # Saving Images
# import urllib.request

# url = 'https:'+'//s3.amazonaws.com/appforest_uf/f1677830733775x854822226006835200/4.png'  # Replace with the URL of the image you want to download
# filename = 'image.jpg'  # Replace with the desired filename for the saved file

# urllib.request.urlretrieve(url, filename)
