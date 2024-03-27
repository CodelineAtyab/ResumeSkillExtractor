import time
import redis
from rq import Queue
from rq.job import Job

from data_processor import process_cv


# Make a connection to the Redis server and grab the reference of the default queue.
REDIS_CONNECTION = redis.Redis(host="localhost", port="6379")
STORAGE_QUEUE = Queue(connection=REDIS_CONNECTION)


def all_jobs_done(list_of_jobs: list[Job]) -> bool:
    """
    :param list_of_jobs: List of Job objects that are referring to the scheduled jobs.
    :return: False if any of the scheduled job is not finished. True if all jobs are complete.
    """
    for job in list_of_jobs:
        if not job.is_finished:
            return False
    return True


# TODO: Read CVs and put their filepath on the remote Queue, so it can be downloaded and processed by the consumers
cv_content_to_process = ["https://aws_s3/sqa_cv_1.pdf", "https://aws_s3/dev_cv_1.pdf", "https://aws_s3/admin_cv_2.pdf"]

list_of_scheduled_jobs = []
for curr_content in cv_content_to_process:
    list_of_scheduled_jobs.append(STORAGE_QUEUE.enqueue(process_cv, curr_content))

time_slept_in_secs = 0
while not all_jobs_done(list_of_scheduled_jobs):
    print(f"Waited {time_slept_in_secs} seconds for all jobs to finish ...")
    time.sleep(1)
    time_slept_in_secs += 1

for curr_job in list_of_scheduled_jobs:
    print(f">>>>>>>>>>>> {curr_job.result}")

print("Closing the producer")
