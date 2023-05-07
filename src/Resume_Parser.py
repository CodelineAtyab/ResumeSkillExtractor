from pyresparser import ResumeParser
import nltk

nltk.download('words')
nltk.download('stopwords')


def parse_cv(path_to_cv):
    # Create a ResumeParser object with the path to the PDF CV
    parser = ResumeParser(path_to_cv)

    # Use the get_extracted_data() method of the parser object to extract data from the CV
    extracted_data = parser.get_extracted_data()

    # Return the extracted data as a dictionary
    return extracted_data


# For unit tests
if __name__ == "__main__":
    cv_data = parse_cv('C:\\Users\\LAP-8\\Documents\\ResumeSkillExtractor\\src\\cv2.pdf')
    print(cv_data)
