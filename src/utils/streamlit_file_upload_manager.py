import hashlib
import os
import traceback

from utils.streamlit_task_dict import task_dict


# Constants
UPLOAD_FILE_DIRECTORY_NAME = "data/streamit_uploaded_files"

# Create directories if they don't exist.
os.makedirs(UPLOAD_FILE_DIRECTORY_NAME, exist_ok=True)


def upload_files_to_a_dir(list_of_files_to_upload, streamlit_instance):
    """
    Saves all user's uploaded files to UPLOAD_FILE_DIRECTORY_NAME for later processing.
    :param list_of_files_to_upload: List of file pointers, pointing to a collection of uploaded files.
    :param streamlit_instance: Used to render necessary widgets on the UI.
    :return:
    """
    for curr_cv in list_of_files_to_upload:
        if curr_cv is not None:
            # Write the data to a file, so it can be later used by cv processor (resume parser)
            with streamlit_instance.spinner(f"Uploading: {curr_cv.name}"):
                try:
                    with open(f"./{UPLOAD_FILE_DIRECTORY_NAME}/{curr_cv.name}", 'wb') as new_cv_file:
                        curr_cv_content = curr_cv.read()
                        curr_cv_content_hash = hashlib.sha256(curr_cv_content).hexdigest()
                        new_cv_file.write(curr_cv_content)
                    task_dict.update({
                        curr_cv_content_hash: {
                            "original_name": curr_cv.name,
                            "sha256_content_hash": curr_cv_content_hash
                        }
                    })
                    streamlit_instance.success(f"Uploaded {curr_cv.name} Successfully!")
                except Exception:
                    streamlit_instance.error(f"Unable to save {curr_cv.name}")
                    print(traceback.format_exc())
