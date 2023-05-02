import queue
import time


def write_result_to_file(name, res_queue):
    keep_running = True
    while keep_running:
        try:
            print(f"Result Producer {name} process waiting....")
            curr_file_content = res_queue.get(timeout=20)
            print("Got content", curr_file_content)

            # Write file content
            out_file_path = "./data/output_files/" + str(time.time()) + ".txt"
            with open(out_file_path, "w") as res_file:
                res_file.write(curr_file_content)
        except queue.Empty:
            print("Result Queue is still empty!.")

        if res_queue.empty():
            keep_running = False