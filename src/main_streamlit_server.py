"""
This is a main script that can be used to run the application and use CV parsing services through a UI
which is rendered by Streamlit framework. The script will fist ask the user to upload CVs then it will
save those CVs on the server in a specific directory.

There would be another main process that will run at specific intervals to process the available CVs
and then generate the results in form of file which will be picked up by this script and all the
results will be displayed on the UI.
"""

import streamlit as st

from utils.streamlit_ui_manager import initialize_user_interface
from utils.streamlit_file_upload_manager import upload_files_to_a_dir
from utils.streamlit_result_display_manager import wait_for_results_and_display_when_available


# Customize the UI for better user experience.
initialize_user_interface(st)

# Display a file upload widget that accepts multiple pdf files.
list_of_uploaded_cvs = st.file_uploader(label="Upload Your CVs in pdf format.",
                                        type="pdf",
                                        accept_multiple_files=True)

# Save all the selected files for later processing.
upload_files_to_a_dir(list_of_files_to_upload=list_of_uploaded_cvs, streamlit_instance=st)

# A separator that will appear on the UI, so we can display the results next.
st.divider()

# Keep waiting for the results, and once results are available then display them.
wait_for_results_and_display_when_available(st)
