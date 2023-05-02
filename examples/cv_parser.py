import time
from pyresparser import ResumeParser


def get_skills_from_cv():
    return ResumeParser('./data/m_ibad_khan.pdf').get_extracted_data().get("skills")


if __name__ == "__main__":
    start_time = time.time()
    print(get_skills_from_cv())
    print(f"Finished in {time.time() - start_time} seconds")
