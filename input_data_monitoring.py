import glob
import queue

class Parser:
    def __init__(self):
        # Create a set to hold the paths of existing files
        self.existing_files = set()
        # Create a queue to hold the paths of new files
        self.cv_queue = queue.Queue()

    def start(self):
        while True:
            # Get a list of paths of all files with the desired file extension
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

    def stop(self):
        # Clear the queue
        while not self.cv_queue.empty():
            self.cv_queue.get()

# Create an instance of the parser and start it
if __name__ == '__main__':
    parser = Parser()
    parser.start()

    # Stop the parser when done
    parser.stop()
