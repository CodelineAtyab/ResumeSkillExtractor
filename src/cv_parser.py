import traceback

from pyresparser import ResumeParser

import nltk


# Download necessary NLTK resources if they haven't been downloaded already downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')


def parse_cv(path_to_cv):
    """
    Extracts data from a PDF resume file.

    Parameters:
    path_to_cv (str): The path to the PDF resume file.

    Returns:
    dict: A dictionary containing extracted data, including name, email, phone number, skills, work experience, education, and more.
        or None if there is an Exception

    Raises:
    FileNotFoundError: If the provided file path is invalid or the file does not exist.
    ValueError: If the provided file is not a valid PDF.
    Exception: If any other error occurs while parsing the resume file.
    """
    try:
        # Create a ResumeParser object with the path to the PDF CV
        parser = ResumeParser(path_to_cv)

        # Use the get_extracted_data() method of the parser object to extract data from the CV
        extracted_data = parser.get_extracted_data()

        return extracted_data
    except FileNotFoundError:
        print("Invalid file path. Please provide a valid path to a PDF file.")
    except ValueError:
        print("Invalid PDF file. Please provide a valid PDF file.")
    except Exception:
        print(f"An error occurred:{traceback.format_exc()}")


# For unit tests
if __name__ == "__main__":
    cv_data = parse_cv('C:\\Users\\LAP-8\\Documents\\ResumeSkillExtractor\\src\\cv2.pdf')
    print(cv_data)
