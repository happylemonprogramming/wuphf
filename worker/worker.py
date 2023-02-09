# Work needed

# Background app running
from rq import Queue, Worker, Connection
import redis
import os

listen = ["default"]
# Redis server from Heroku Add-on
# conn = redis.Redis(
#   host='redis-15847.c258.us-east-1-4.ec2.cloud.redislabs.com',
#   port=15847,
#   password = os.environ["redisapikey"])


conn = redis.Redis(
  host='redis-16832.c265.us-east-1-2.ec2.cloud.redislabs.com',
  port=16832,
  password='7Q48qw1QfSEOWEujhzIiTMxDwjuoKDWD')

# # Localhost Redis server using wsl
# conn = redis.Redis(host='localhost', port=6379, db=0)
# listen = ['high','default','low']
# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
# conn = redis.from_url(redis_url)
# q = Queue(connection=conn)

# Variable 'prompt' passed from webapp (user input on index.html)
# import sys
# prompt = sys.argv[1]
# print(prompt)

# # How to retrieve data from redis per Chat GPT
# import redis

# # Connect to Redis server
# r = redis.Redis(host='localhost', port=6379, db=0)

# # Retrieve a string value
# string_value = r.get('string_key')
# if string_value is not None:
#     print(f"String value: {string_value.decode()}")

# # Retrieve a list value
# list_values = r.lrange('list_key', 0, -1)
# if list_values:
#     print(f"List values: {[value.decode() for value in list_values]}")


# Worker doin' work
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(listen)
        # worker = Worker(map(Queue, listen))
        worker.work()