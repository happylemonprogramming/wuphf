import imageio
import numpy as np
import os
import requests
# path = r"C:\Users\<user>\Pictures\AI Images/" # For testing purposes only
# path = r"C:\Users\<user>\Documents\Programming\AI Twitter Bot/"


# FRANK QUESTION: SHOULD IMAGE RANKING ALLOW DUPLICATE PHOTO UPLOADS?
# Function to see if image is light or dark based on 0-255 mean grayscale of image in path
def imagereadlightdark(listofimageurls):
    # Identify folder path and create list of image descriptions to review

    # First step is to download all of the images from bubble
    # Initialize variables and lists
    i = 0
    grayscale_list = []
    define_mean_light = []
    sorted_light_dict = {}

    # Iterate through the list of image urls and download them
    for image in listofimageurls:
        image = "https:" + image
        response = requests.get(image)
        # Download content to server
        with open(f'{i}.png', 'wb') as f:
            f.write(response.content)
        # Read the image and append it to the grayscale_list
        grayscale_list.append(imageio.imread(f'{i}.png', as_gray=True))

        # Append the mean of the grayscale image to the define_light list
        define_mean_light.append(np.mean(grayscale_list[i]))
        print(define_mean_light)
        print(image)
        sorted_light_dict[define_mean_light[i]] = image
        i = i+1
        print(i)
    print(sorted_light_dict, len(sorted_light_dict), len(define_mean_light),len(grayscale_list), len(listofimageurls))
    # filenames = os.listdir(path)
    # i = 0
    # decision = []
    # iterate = []
    # filtered = [item for item in filenames if '.png' in item or '.jpg' in item]
    
    # # Sort through the directory "filenames"
    # for filename in filtered:
    #     file = imageio.imread(path+filename, as_gray=True)
    #     is_light = np.mean(file) > 127 #Between 0-255
    #     # Small function to count files
    #     i = i+1
    #     iterate.append(i)
    #     # Make decision on grayscale and add it to the list
    #     if is_light == False:
    #         is_light = 'Dark'
    #         decision.append(is_light)
    #     else:
    #         is_light = 'Light'
    #         decision.append(is_light)

    # # create a dictionary in the schema {1:[aliens.png, dark]}
    # lightdarkdict = dict(zip(iterate, zip(filtered, decision)))
    # return lightdarkdict
    return None

# listofimageurls = ['//s3.amazonaws.com/appforest_uf/f1677559888855x607469259013140400/example.PNG', 
#                    '//s3.amazonaws.com/appforest_uf/f1677559889650x369774974835638700/warzone%202.png', 
#                    '//s3.amazonaws.com/appforest_uf/f1677559953479x124276868361050900/jean-estrella-yqaTqfoetTY-unsplash.jpg',
#                    '//s3.amazonaws.com/appforest_uf/f1677559888855x607469259013140400/example.PNG']

# imagereadlightdark(listofimageurls)