import os
import json
from queue import Queue


# Define a dummy function for parsing resumes and adding results to the queue
def _parse_resume(input_cv_filename, result_queue):
    """
    this function is only for test
    :param input_cv_filename:
    :param result_queue:
    :return:
    """
    # Parse the resume and extract relevant information
    extracted_skills = ['C++', 'Java', 'Python']

    # Add the results to the queue
    result_queue.put({'input_cv_filename': input_cv_filename, 'result': {'extracted_skills': extracted_skills}})


# Define a function for writing the results to a file
def write_results_to_file(result_queue):
    # Create the output file path
    output_file_path = os.path.join("output_data", "results.json")

    # Create the output_data directory if it does not exist
    os.makedirs("output_data", exist_ok=True)

    # Open the output file for writing
    with open(output_file_path, "w") as output_file:
        # Write each result from the queue to the file
        while not result_queue.empty():
            result = result_queue.get()
            output_file.write(json.dumps(result.get('result')) + "\n")


if __name__ == "__main__":
    # Define the result queue
    result_queue = Queue()

    # Example usage
    _parse_resume("say_cv.pdf", result_queue)
    write_results_to_file(result_queue)
