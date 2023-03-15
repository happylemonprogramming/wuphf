import datetime
import time

# Parse the input string into a datetime object
target_date_str = "Mar 14, 2023 9:25 pm"
target_date = datetime.datetime.strptime(target_date_str, "%b %d, %Y %I:%M %p")

while datetime.datetime.now() < target_date:
    time.sleep(60)  # Wait for 1 minute
else:
    print("yay!")
