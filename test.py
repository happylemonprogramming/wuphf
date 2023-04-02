# Suppose to take in 3 lists of data and sort them by date


#Example JSON
# JSON Body = {"post_time": ['2022-01-01', '2021-12-31', '2022-01-02'],
    # "image_urls": ['url1', 'url2', 'url3'],
    # "final_captions": ['string1', 'string2', 'string3']}

# # Variable loading for JSON
# json_data = request.get_json()
# post_time = json_data['Post Time']
# image_urls = json_data['Post Time Image List']
# final_captions = json_data['Post Time Captions']


# Sample input data
post_time = ['2022-01-01', '2021-12-31', '2022-01-02']
image_urls = ['url1', 'url2', 'url3']
final_captions = ['string1', 'string2', 'string3']

def sort_posts_by_date(dates, image_urls, strings):
    # Combine the lists into a list of tuples
    combined_data = list(zip(dates, image_urls, strings))

    # Sort the list of tuples by date
    sorted_data = sorted(combined_data)

    # Extract the sorted image urls and strings into new lists
    sorted_image_urls = [t[1] for t in sorted_data]
    sorted_strings = [t[2] for t in sorted_data]

    # Print the sorted data for verification
    # print(sorted_data[0][1])
    # print(sorted_image_urls)
    # print(sorted_strings)
    return sorted_data



if __name__ == "__main__":
    test = sort_posts_by_date(post_time, image_urls, final_captions)
    # Retrieve the sorted list of tuples
    print(test)
    # Post the sorted list of tuples
    for i in test:
        print(i[0]) # Post time, which is currently used as YouTube key
        print(i[1]) # Image URL
        print(i[2]) # Caption

