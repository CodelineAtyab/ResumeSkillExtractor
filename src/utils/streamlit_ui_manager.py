def _hide_non_essential_elements_from_ui(streamlit_instance):
    """
    This method hides un-necessary widgets and labels from the UI rendered by Streamlit.
    :param streamlit_instance: Used to configure and render necessary widgets on the UI.
    """
    updated_streamlit_css_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """
    streamlit_instance.markdown(updated_streamlit_css_style, unsafe_allow_html=True)


def initialize_user_interface(streamlit_instance):
    """
    Sets up the UI when the server is accessed from any client.
    :param streamlit_instance: Used to configure and render necessary widgets on the UI.
    """
    _hide_non_essential_elements_from_ui(streamlit_instance)
    streamlit_instance.title("CV Skill Parser")
    streamlit_instance.header("Developed by TheDynamicDoers")
