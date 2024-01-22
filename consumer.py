import redis
from rq import Queue, Connection
from rq_win import WindowsWorker

redis_connection = redis.Redis(host="localhost", port="6379")

if __name__ == "__main__":
    with Connection(redis_connection):
        curr_worker = WindowsWorker(map(Queue, ['default']))
        curr_worker.work()
