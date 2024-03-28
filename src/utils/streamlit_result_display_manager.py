import os
import time

from utils.streamlit_task_dict import task_dict


RESULT_FILE_DIRECTORY_NAME = "output_files"


def wait_for_results_and_display_when_available(streamlit_instance):
    """
    This is the main application loop. This method will keep on waiting for the result files
    to be made available in RESULT_FILE_DIRECTORY_NAME so the results can be displayed on the UI.
    :param streamlit_instance: Used to render necessary widgets on the UI.
    """
    if task_dict:
        streamlit_instance.header("Listing my findings here:")

        # Download and display results for the previously selected files
        wait_message = "Waiting for results!"

        while task_dict:
            with streamlit_instance.spinner(wait_message):
                # Wait, so the user can see the message.
                time.sleep(3)

                # Copy task dict and then iterate it, so we can delete the processed elements from the original dict.
                for curr_file_content_hash, task_desc_dict in dict(task_dict).items():
                    curr_res_file_path = os.path.join(RESULT_FILE_DIRECTORY_NAME, curr_file_content_hash+".txt")
                    try:
                        with open(curr_res_file_path, "r") as curr_res_file:
                            streamlit_instance.divider()
                            streamlit_instance.write(f"Results for: {curr_file_content_hash}")
                            streamlit_instance.info(curr_res_file.read())

                            # Remove the processed element
                            task_dict.pop(curr_file_content_hash)
                    except FileNotFoundError:
                        wait_message = f"Waiting for {curr_file_content_hash}.txt file"
