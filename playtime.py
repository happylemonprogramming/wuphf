import datetime
import time

target_date = datetime.datetime(2023, 3, 14, 21, 9)

while datetime.datetime.now() < target_date:
    time.sleep(60)  # Wait for 1 minute
else:
    print("yay!")
