import time
from threading import Thread
from cv_parser import get_skills_from_cv


def do_something(task_name):
    print(f"Started doing the task {task_name}")
    extracted_skills = get_skills_from_cv()
    print(f"Task {task_name} done! Response: {extracted_skills}")
    print("")


if __name__ == "__main__":
    print("STARTING THE MAIN APP!")
    test_start_time = time.time()
    thread_1 = Thread(target=do_something, args=("task1",), daemon=True)
    thread_2 = Thread(target=do_something, args=("task2",), daemon=True)
    thread_3 = Thread(target=do_something, args=("task3",), daemon=True)

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()

    test_end_time = time.time() - test_start_time

    print(f"Completed in {test_end_time} seconds.")
    print("EXITING THE MAIN APP!")
