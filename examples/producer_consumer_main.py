"""
This Main script will act as a producer,
and it will spawn consumer processes as well
"""
import queue
import time
from multiprocessing import Process, Queue


def process_task(name, inp_queue, res_queue):
    keep_running = True
    while keep_running:
        try:
            print(f"Consumer {name} process waiting....")
            curr_word = inp_queue.get(timeout=10)
            print("Got a word", curr_word)
            result = curr_word.lower()
            res_queue.put(result)
        except queue.Empty:
            print("Queue is still empty!.")

        if inp_queue.empty():
            keep_running = False


if __name__ == "__main__":
    task_queue = Queue()
    result_queue = Queue()

    consumer_process_1 = Process(target=process_task, args=("c1", task_queue, result_queue))
    consumer_process_2 = Process(target=process_task, args=("c2", task_queue, result_queue))
    consumer_process_3 = Process(target=process_task, args=("c3", task_queue, result_queue))

    consumer_process_1.start()
    consumer_process_2.start()
    consumer_process_3.start()

    # Creating (Producing) Tasks
    print("Producing tasks in 3 seconds")
    time.sleep(3)
    list_of_words = ["HeLlO", "woRLd", "THIS", "iS", "A", "TeST"]
    for word in list_of_words:
        task_queue.put(word)

    consumer_process_1.join()
    consumer_process_2.join()
    consumer_process_3.join()
    print("Exiting the Main (Process) Application")
