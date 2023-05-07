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
                    new_cv_file.write(curr_cv.read())
                st.success(f"Uploaded {curr_cv.name} Successfully!")
            except Exception:
                st.error(f"Unable to save {curr_cv.name}")
                print(traceback.format_exc())

st.divider()

if len(list_of_uploaded_cvs) > 0:
    # Download and display results for the previously selected files
    with st.spinner(f"Waiting for results!"):
        while True:
            time.sleep(1)

        # for curr_cv in list_of_uploaded_cvs:
        #     if curr_cv is not None:
        #         pass