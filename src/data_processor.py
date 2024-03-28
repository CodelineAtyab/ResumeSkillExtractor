import json
from pyresparser import ResumeParser


def process_cv(cv_file_path):
    extracted_data = ResumeParser(cv_file_path).get_extracted_data()
    return json.dumps(extracted_data, indent=2)


if __name__ == "__main__":
    import json
    from pyresparser import ResumeParser
    extracted_data = ResumeParser("../cv_store/java-developer-resume-example.pdf").get_extracted_data()
    print(json.dumps(extracted_data, indent=2))
