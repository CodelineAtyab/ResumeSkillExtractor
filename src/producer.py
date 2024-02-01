import time
import redis
from rq import Queue

from data_processor import process_cv


def report_success(job, connection, result, *args, **kwargs):
    print(f">>>>>>> Job {job.id} is completed. The result is: {result}")


redis_connection = redis.Redis(host="localhost", port="6379")
storage_queue = Queue(connection=redis_connection)

# TODO: Read CVs and put the content on the remote Queue, so it can be processed by the consumers
cv_content_to_process = ["Javascript Developer", "Java Developer", "Python Developer", "C# Developer"]

list_of_scheduled_jobs = []
for curr_content in cv_content_to_process:
    list_of_scheduled_jobs.append(storage_queue.enqueue(process_cv, curr_content))

time.sleep(3)

for curr_job in list_of_scheduled_jobs:
    print(f">>>>>>>>>>>> {curr_job.result}")

print("Closing the producer")
