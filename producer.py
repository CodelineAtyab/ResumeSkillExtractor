import redis
from rq import Queue

from data_processor import process_cv

redis_connection = redis.Redis(host="localhost", port="6379")
storage_queue = Queue(connection=redis_connection)

# TODO: Read CVs and put the content on the remote Queue, so it can be processed by the consumers
cv_content_to_process = ["Javascript Developer", "Java Developer", "Python Developer", "C# Developer"]
for curr_content in cv_content_to_process:
    storage_queue.enqueue(process_cv, curr_content)

print("Closing the producer")
