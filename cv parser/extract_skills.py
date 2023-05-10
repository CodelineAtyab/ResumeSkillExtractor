from pyresparser import ResumeParser


def get_skills_from_cv(file_path):
    """
        This function uses the Pyresparser library to extract skills from the input resume file.

        Parameters:
        - file_path: A string representing the file path of the resume.

        Returns:
        - A list of skills extracted from the resume using Pyresparser library.
        """
    return ResumeParser(file_path).get_extracted_data().get("skills")
