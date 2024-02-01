import redis
from rq import Queue, Connection

from custom_windows_worker import CustomWindowsWorker

redis_connection = redis.Redis(host="localhost", port="6379")

if __name__ == "__main__":
    with Connection(redis_connection):
        curr_worker = CustomWindowsWorker(map(Queue, ['default']))
        curr_worker.work()
