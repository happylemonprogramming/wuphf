import imageio
import numpy as np
import os

# path = r"C:\Users\<user>\Pictures\AI Images/" # For testing purposes only
# path = r"C:\Users\<user>\Documents\Programming\AI Twitter Bot/"

# Function to see if image is light or dark based on 0-255 mean grayscale of image in path
def imagereadlightdark(path):
    # Identify folder path and create list of image descriptions to review
    filenames = os.listdir(path)
    i = 0
    decision = []
    iterate = []
    filtered = [item for item in filenames if '.png' in item or '.jpg' in item]
    
    # Sort through the directory "filenames"
    for filename in filtered:
        file = imageio.imread(path+filename, as_gray=True)
        is_light = np.mean(file) > 127 #Between 0-255
        # Small function to count files
        i = i+1
        iterate.append(i)
        # Make decision on grayscale and add it to the list
        if is_light == False:
            is_light = 'Dark'
            decision.append(is_light)
        else:
            is_light = 'Light'
            decision.append(is_light)

    # create a dictionary in the schema {1:[aliens.png, dark]}
    lightdarkdict = dict(zip(iterate, zip(filtered, decision)))
    return lightdarkdict