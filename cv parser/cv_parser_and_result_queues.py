import hashlib
from extract_skills import get_skills_from_cv
from multiprocessing import Process, Queue
from queue import Empty


def parse_resume(file_queue, result_queue):
    """
    This function takes two queues as arguments, file_queue and result_queue. It reads the file path from the file queue,
    extracts skills from the corresponding file using the get_skills_from_cv function, and adds the extracted skills and
    the input CV filename to the result queue.
    """
    processing = True
    while processing:
        try:
            file_path = file_queue.get(timeout=1)
            extracted_skills = get_skills_from_cv(file_path)
            # read the content to gen sha256 hash and use that as filename
            with open(file_path, 'rb') as pdf_file:
                content = pdf_file.read()
                file_hash = hashlib.sha256(content).hexdigest()
            file_name = f"{file_hash}.pdf"
            result = {'input_cv_filename': file_name, 'result': {'extracted_skills': extracted_skills}}
            result_queue.put((result, file_name))
            print(f"Extracted skills from {file_path}: {extracted_skills}")
        except Empty:
            processing = False


if __name__ == "__main__":
    print("Starting the MAIN APP")

    # create file queue and result queue
    file_queue = Queue()
    result_queue = Queue()

    # add file paths to file queue
    file_queue.put('./Najlacv.pdf')

    # create and start resume parser process
    resume_parser_process = Process(target=parse_resume, args=(file_queue, result_queue), daemon=True)
    print("Parsing resumes...")
    resume_parser_process.start()

    # wait for all files to be parsed
    resume_parser_process.join()

    # process results from result queue
    # Testing the result queue
    while not result_queue.empty():
        extracted_skills, file_name = result_queue.get()
        print(f"Extracted skills: {extracted_skills}")

    print("Exiting the Main app")
