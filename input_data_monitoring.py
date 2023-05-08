import queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define a custom event handler that watches for new files with a specified file extension
class CVHandler(FileSystemEventHandler):
    def __init__(self, cv_queue):
        super().__init__()
        self.cv_queue = cv_queue

    def on_created(self, event):
        # Check if the event is a file creation and if it has the desired file extension
        if not event.is_directory and event.src_path.endswith('.pdf'):
            print(f"New file created: {event.src_path}")
            # Add the path of the new file to a queue for processing
            self.cv_queue.put(event.src_path)

class Parser:
    def __init__(self):
        # Create a queue to hold the paths of new files
        self.cv_queue = queue.Queue()
        # Create an instance of the custom event handler and attach it to an observer
        self.cv_handler = CVHandler(self.cv_queue)
        self.observer = Observer()
        # Set the directory to watch and set recursive to False to only watch the specified directory
        self.observer.schedule(self.cv_handler, 'C:/Users/LAP-10/Documents/input_data', recursive=False)

    def start(self):
        # Start the observer
        self.observer.start()
        # Continuously loop and process new files added to the queue
        while True:
            try:
                # Get the path of a new file from the queue
                cv_filepath = self.cv_queue.get(timeout=1)
                # Process the file here
                print(f'Processing {cv_filepath}')
            except queue.Empty:
                pass

    def stop(self):
        # Stop the observer and wait for it to finish
        self.observer.stop()
        self.observer.join()


# Create an instance of the parser and start it
if __name__ == '__main__':
    parser = Parser()
    parser.start()

   

    # Stop the parser when done
    parser.stop()
