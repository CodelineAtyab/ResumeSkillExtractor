import glob
import queue


class QueuePopulater:
    """
    A class to populate a directory for new files with a specified file extension
    and add their file paths to a queue.

    Attributes:
    - existing_files (set): A set to hold the paths of existing files.
    - cv_queue (queue.Queue): A queue to hold the paths of new files.

    Methods:
    - populate(): populates the directory for new files and calls add_file_to_queue for each new file.
    - add_file_to_queue(filepath): Adds a file path to the queue.
    """

    def __init__(self, queue_to_populate):
        """
        Initializes a new instance of the FileScanner class.

        Args:
        - cv_queue (queue.Queue): A queue to hold the paths of new files.
        """
        # Create a set to hold the paths of existing files

        self.existing_files = set()
        # Create a queue to hold the paths of new files
        self.cv_queue = queue_to_populate
        self.populate()

    def add_to_queue(self, filepath):
        """
        Adds a file path to the queue.

        Args:
        - filepath (str): The path of the file to be added to the queue.
        """
        print(f'Processing {filepath}')
        print(f'Adding {filepath} to queue')
        self.cv_queue.put(filepath)

    def populate(self):
        """
        Scans the directory for new files and calls add_file_to_queue for each new file.
        """
        # Get a list of paths of all files with the desired file extension
        try:
            filepaths = set(glob.glob('./input_data/*.pdf'))
            # Get the set difference between the existing files and the new files
            new_files = filepaths - self.existing_files

            # Process each new file
            for filepath in new_files:
                self.add_to_queue(filepath)

            # Update the set of existing files
            self.existing_files = filepaths
        except FileNotFoundError:
            # Handle the exception if the specified directory was not found
            print('The specified directory was not found.')


# Create an instance of the FileScanner and start it
if __name__ == '__main__':
    # Create a queue to hold the paths of new files
    incoming_cv_queue = queue.Queue()
    # Create an instance of the FileScanner class
    populater = QueuePopulater(queue_to_populate=incoming_cv_queue)
    # Call the populater method to start populating the directory for new files
    populater.populate()
