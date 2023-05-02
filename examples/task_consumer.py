import queue


def process_task(name, inp_queue, res_queue):
    keep_running = True
    while keep_running:
        try:
            print(f"Consumer {name} process waiting....")
            curr_file_content = inp_queue.get(timeout=10)
            print("Got content", curr_file_content)

            # Processing file content
            list_of_words = curr_file_content.split()
            result_str = "\n".join([word.strip().lower() for word in list_of_words])
            res_queue.put(result_str)
        except queue.Empty:
            print("Queue is still empty!.")

        if inp_queue.empty():
            keep_running = False