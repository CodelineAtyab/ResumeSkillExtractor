import hashlib
import os
import time
import traceback

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
task_dict = dict()


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
                task_dict.update({
                    curr_cv_content_hash: {
                        "original_name": curr_cv.name,
                        "sha256_content_hash": curr_cv_content_hash,
                    }
                })
                st.success(f"Uploaded {curr_cv.name} Successfully!")
            except Exception:
                st.error(f"Unable to save {curr_cv.name}")
                print(traceback.format_exc())

st.divider()

if task_dict and os.path.exists(RESULT_FILE_DIRECTORY_NAME):
    st.header("This is what I found:")

    # Download and display results for the previously selected files
    wait_message = "Waiting for results!"

    while task_dict:
        with st.spinner(wait_message):
            # Wait, so the user can see the message.
            time.sleep(3)

            # Copy task dict and then iterate it, so we can delete the processed elements from the original dict.
            for curr_file_content_hash, task_desc_dict in dict(task_dict).items():
                curr_res_file_path = os.path.join(RESULT_FILE_DIRECTORY_NAME, curr_file_content_hash+".txt")
                try:
                    with open(curr_res_file_path, "r") as curr_res_file:
                        st.divider()
                        st.write(f"Results for: {curr_file_content_hash}")
                        st.info(curr_res_file.read())

                        # Remove the processed element
                        task_dict.pop(curr_file_content_hash)
                except FileNotFoundError:
                    wait_message = f"Waiting for {curr_file_content_hash}.txt file"
