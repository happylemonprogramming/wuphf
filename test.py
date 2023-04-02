# # Suppose to take in 3 lists of data and sort them by date


# #Example JSON
# # JSON Body = {"post_time": ['2022-01-01', '2021-12-31', '2022-01-02'],
#     # "image_urls": ['url1', 'url2', 'url3'],
#     # "final_captions": ['string1', 'string2', 'string3']}

# # # Variable loading for JSON
# # json_data = request.get_json()
# # post_time = json_data['Post Time']
# # image_urls = json_data['Post Time Image List']
# # final_captions = json_data['Post Time Captions']


# # Sample input data
# post_time = ['2022-01-01', '2021-12-31', '2022-01-02']
# image_urls = ['url1', 'url2', 'url3']
# final_captions = ['string1', 'string2', 'string3']

# def sort_posts_by_date(dates, image_urls, strings):
#     # Combine the lists into a list of tuples
#     combined_data = list(zip(dates, image_urls, strings))

#     # Sort the list of tuples by date
#     sorted_data = sorted(combined_data)

#     # Extract the sorted image urls and strings into new lists
#     sorted_image_urls = [t[1] for t in sorted_data]
#     sorted_strings = [t[2] for t in sorted_data]

#     # Print the sorted data for verification
#     # print(sorted_data[0][1])
#     # print(sorted_image_urls)
#     # print(sorted_strings)
#     return sorted_data



# if __name__ == "__main__":
#     test = sort_posts_by_date(post_time, image_urls, final_captions)
#     # Retrieve the sorted list of tuples
#     print(test)
#     # Post the sorted list of tuples
#     for i in test:
#         print(i[0]) # Post time, which is currently used as YouTube key
#         print(i[1]) # Image URL
#         print(i[2]) # Caption

# Input string
# string = 'Apr 1, 2023 7:00 pm Apr 1, 2023 8:30 pm'

# Input string
# string = 'Apr 1, 2023 7:00 pm Apr 1, 2023 8:30 pm May 1, 2023 9:00 am May 2, 2023 2:30 pm'



# # Input string
# string = 'Apr 1, 2023 9:30 pm, Apr 1, 2023 10:00 pm'
# print(len(string))
# # Group the input string into a list of substrings of 19 characters each, skipping the 20th character
# substrings = [string[i:i+20] for i in range(0, len(string), 21)]

# # Print the list of substrings
# print(substrings)

# # Input string
string = 'Apr 1, 2023 9:30 pm, Apr 1, 2023 10:00 pm'

# Split the string into a list of substrings, using ", " as the delimiter
substrings = string.split(", ")
# Combine every two elements together in the list
result = []
for i in range(0, len(substrings), 2):
    result.append(substrings[i] + " " + substrings[i+1])
    # print(result)


captions = ["\n\nJust when I thought I've seen it all, my buddy calls me to come over and watch a dinosaur and lemon battle. This ain't no ordinary fight club! #DaveChappelle", "\n\nI just got struck by lightning while making a lemonade... oh well, at least the drink will be extra strong this time! #LightningLemon #DaveChappelle"]
imgurls = ['//s3.amazonaws.com/appforest_uf/f1675978942446x792425085319267600/Lemon%20%26%20T-Rex.png', '//s3.amazonaws.com/appforest_uf/f1675978976428x846564285372801800/Lightning%20%26%20Lemon%202.png']

listOfPosts = len(captions)
i=0
# Loop through all posts
for item in range(listOfPosts): #TODO: can probably change 'item' for 'i' and then delete i = 0
    imgurl = imgurls[i]
    caption = captions[i]
    post_time = result[i]
    # print('API Print Time 2:', post_time)
    # print(item, imgurl, caption, post_time)
    i += 1
import datetime
target_date_list = result
print(target_date_list)
print(range(len(target_date_list)))
for i in range(len(target_date_list)):
    print(target_date_list[i])
    target_date = datetime.datetime.strptime(target_date_list[i], "%b %d %Y %I:%M %p")
    print(target_date)