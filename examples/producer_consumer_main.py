"""
This Main script will act as a producer,
and it will spawn consumer processes as well
"""
import time
from multiprocessing import Process, Queue

from task_consumer import process_task
from file_parser import get_list_of_text_files
from result_producer import write_result_to_file


def create_tasks(task_queue):
    list_of_files = get_list_of_text_files("./data/input_files/", "txt")
    for curr_file in list_of_files:
        with open(curr_file, "r") as curr_file_ptr:
            task_queue.put(curr_file_ptr.read())


if __name__ == "__main__":
    task_queue = Queue()
    result_queue = Queue()

    num_of_consumer_processes = 3
    list_of_consumer_processes = []

    for num in range(num_of_consumer_processes):
        curr_process = Process(target=process_task, args=("c"+str(num+1), task_queue, result_queue))
        list_of_consumer_processes.append(curr_process)
        curr_process.start()

    result_producer_process_1 = Process(target=write_result_to_file, args=("res1", result_queue))
    result_producer_process_1.start()

    # Creating (Producing) Tasks
    print("Producing tasks in 3 seconds")
    time.sleep(3)
    create_tasks(task_queue)

    # Wait for consumers to finish
    for con_process in list_of_consumer_processes:
        con_process.join()

    # Wait for result producer to finish
    result_producer_process_1.join()

    print("Exiting the Main (Process) Application")
