import os
import time
import redis
from rq import Queue
from selenium import webdriver

# Connect to the Redis server
redis_conn = redis.Redis(host='localhost', port=6379)
q = Queue(connection=redis_conn)

# Define the Selenium task
def scrape_task(url):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()
    driver.get(url)

    # Scrape the data from the page
    data = driver.find_elements_by_css_selector("#data")

    # Close the driver and return the data
    driver.quit()
    return data

# Enqueue the task in RQ
task = q.enqueue(scrape_task, 'https://www.example.com')

# Wait for the task to complete
while not task.is_finished:
    time.sleep(1)

# Get the results from the task
result = task.result

# Print the results
print(result)
