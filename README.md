"# ResumeSkillExtractor"

here are the steps to use the parse_cv() function to extract data from a PDF CV:

1- Make sure you have Python 3.x installed on your system.
2- Install the required packages by running the following command in your terminal or command prompt:
     pip install -r requirements.txt
     python -m nltk.downloader words
     python -m nltk.downloader stopwords
3- Once the packages are installed, you can import the parse_cv() function in your Python code using the following statement:
     from Resume_Parser import parse_cv
4- Call the parse_cv() function with the path to your PDF CV file as an argument:
   data = parse_cv('/path/to/your/cv.pdf')

