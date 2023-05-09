import glob
import queue

class FileScanner:
    """
      A class to scan a directory for new files with a specified file extension
      and add their file paths to a queue.

      Attributes:
      - existing_files (set): A set to hold the paths of existing files.
      - cv_queue (queue.Queue): A queue to hold the paths of new files.

      Methods:
      - scan(): Scans the directory for new files and adds their file paths to the queue.
      """
    def __init__(self,cv_queue):
        """
               Initializes a new instance of the FileScanner class.

               Args:
               - cv_queue (queue.Queue): A queue to hold the paths of new files.
        """
        # Create a set to hold the paths of existing files
        self.existing_files = set()
        # Create a queue to hold the paths of new files
        self.cv_queue = queue.Queue()

    def scan(self):
        """
              Scans the directory for new files and adds their file paths to the queue.
        """
        # Get a list of paths of all files with the desired file extension
        try:
            filepaths = set(glob.glob('C:/Users/LAP-10/Documents/input_data/*.pdf'))
            # Get the set difference between the existing files and the new files
            new_files = filepaths - self.existing_files

            # Process each new file
            for filepath in new_files:
                print(f'Processing {filepath}')
                print(f'Adding {filepath} to queue')
                self.cv_queue.put(filepath)

            # Update the set of existing files
            self.existing_files = filepaths
        except FileNotFoundError:
            # Handle the exception if the specified directory was not found
            print('The specified directory was not found.')


# Create an instance of the FileScanner and start it
if __name__ == '__main__':
    # Create a queue to hold the paths of new files
    cv_queue = queue.Queue()
    # Create an instance of the FileScanner class
    scanner = FileScanner(cv_queue)
    # Call the scan method to start scanning the directory for new files
    scanner.scan()
