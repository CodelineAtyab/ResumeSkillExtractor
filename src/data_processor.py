def process_cv(cv_file_content):
    # TODO use pyresparser which is already intalled to get the list of skills and then return it as a dict
    return cv_file_content


if __name__ == "__main__":
    import json
    from pyresparser import ResumeParser
    extracted_data = ResumeParser("../cv_store/java-developer-resume-example.pdf").get_extracted_data()
    print(json.dumps(extracted_data, indent=2))
