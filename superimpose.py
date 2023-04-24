import requests
from PIL import Image
import PIL.Image
from io import BytesIO
from removebg import removebgurl

# Local Files
# # Open the first image and convert it to RGBA format
# image1 = Image.open(r"C:\Users\clayt\Downloads\forjulie.png").convert("RGBA")

# # Open the second image and convert it to RGBA format
# image2 = Image.open(r"C:\Users\clayt\Downloads\julie background.png").convert("RGBA")

# URL Files
# Open the first image and convert it to RGBA format
# url1 = 'https://cdn.discordapp.com/attachments/939751705732599818/1097033144592498859/70311012317__AA955D4D-C90E-4125-A087-F5928DDE53D1.jpeg'
# response1 = requests.get(url1)
# print(response1.headers.get('content-type'))
# PIL.Image.register_mime("PNG", "png")
# image1 = Image.open(BytesIO(response1.content)).convert("RGBA")

# removebgurl(url1, "daric.png")
image1 = Image.open(r"C:\Users\clayt\Downloads\piperagain-removebg-preview (1).png").convert("RGBA")

# Open the second image from URL and convert it to RGBA format
# url2 = 'https://cdn-images-1.medium.com/max/721/1*XIiHVgiHXm8G6tX_aLjOqw.jpeg'
# response2 = requests.get(url2)
# print(response2.headers.get('content-type'))
# PIL.Image.register_mime("PNG", "png")
# image2 = Image.open(BytesIO(response2.content)).convert("RGBA")
image2 = Image.open(r"C:\Users\clayt\Downloads\moon.jpg").convert("RGBA")

# Resize the second image to the same size as the first image
# image2 = image2.resize(image1.size)
width, height = image1.size
print(width, height)
image2 = image2.crop((0,0,width, height))
image2.save("moononly.png")
        # # Crop and resize the first image to a square shape with the minimum dimension, focusing on the center
        # imgcrop = imgdload.crop((crop_left, crop_upper, crop_right, crop_lower)).resize((min_dim, min_dim))

# # Create a new image by blending the two images together
# blend = Image.blend(image1, image2, 0.5)

# Create a new image by alpha-compositing the two images together
composite = Image.alpha_composite(image2, image1)

# Save the blended image to a file
composite.save("superimposed.png")
