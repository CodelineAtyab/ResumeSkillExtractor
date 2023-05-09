import hashlib
import os
import time
import traceback
from queue import Queue

import streamlit as st


# Hiding the Menu and the footer
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("CV Skill Parser")
st.header("Developed by TheDynamicDoers")

# Constants
RESULT_FILE_DIRECTORY_NAME = "output_files"

# Global Storage
task_queue = Queue()


# Thread Targets
def get_result_content(res_queue, res_filename):
    while not os.path.exists(res_filename):
        time.sleep(3)


# Create if the directory doesn't exist.
UPLOAD_FILE_DIRECTORY_NAME = "streamit_uploaded_files"
if not os.path.exists(UPLOAD_FILE_DIRECTORY_NAME):
    os.mkdir(UPLOAD_FILE_DIRECTORY_NAME)

# Display a file uploader widget that accepts multiple pdf files
list_of_uploaded_cvs = st.file_uploader(label="Upload Your CVs in pdf format.",
                                        type="pdf",
                                        accept_multiple_files=True)

# Upload all selected files
for curr_cv in list_of_uploaded_cvs:
    if curr_cv is not None:
        # Write the data to a file, so it can be later used by cv processor (resume parser)
        with st.spinner(f"Uploading: {curr_cv.name}"):
            try:
                with open(f"./{UPLOAD_FILE_DIRECTORY_NAME}/{curr_cv.name}", 'wb') as new_cv_file:
                    curr_cv_content = curr_cv.read()
                    curr_cv_content_hash = hashlib.sha256(curr_cv_content).hexdigest()
                    new_cv_file.write(curr_cv_content)
                task_queue.put({"original_name": curr_cv.name, "sha256_content_hash": curr_cv_content_hash})
                st.success(f"Uploaded {curr_cv.name} Successfully!")
            except Exception:
                st.error(f"Unable to save {curr_cv.name}")
                print(traceback.format_exc())

st.divider()

if len(list_of_uploaded_cvs) > 0 and os.path.exists(RESULT_FILE_DIRECTORY_NAME):
    st.header("This is what I found:")
    # Start new threads to look for the available CVs in the result directory
    # result_reader_threads = []
    # while not task_queue.empty():
    #     new_reader_thread = Thread(target=get_result_content, args=(result_queue, task_queue.get()))
    #     result_reader_threads.append(new_reader_thread)

    # wait_for_results = True
    # # Download and display results for the previously selected files
    # with st.spinner(f"Waiting for results!"):
    #     while wait_for_results:
    #         list_of_available_result_files = glob.glob(os.path.join(RESULT_FILE_DIRECTORY_NAME, "*.txt"))
    #         if list_of_available_result_files:
    #             for curr_res_file in list_of_available_result_files:
    #                 with open(curr_res_file, "r") as curr_res_file_ptr:
    #                     st.divider()
    #                     st.write(f"Results for: {curr_res_file}")
    #                     st.info(curr_res_file_ptr.read())
    #
    #         time.sleep(3)
