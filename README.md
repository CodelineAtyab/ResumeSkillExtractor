# CV Processing System Using Redis Queue

## Overview
This project implements a distributed task processing system using Redis Queue (RQ) in Python. It's designed to process Curriculum Vitae (CV) data efficiently by utilizing a producer-consumer model. The system allows for multiple consumer workers to process CVs concurrently, improving throughput and scalability.

## Features
- **Asynchronous Task Processing**: Utilizes Redis Queue for managing asynchronous tasks.
- **Scalable Architecture**: Easily scale by increasing the number of consumer workers.
- **Concurrent CV Processing**: Multiple CVs can be processed simultaneously by different workers.
- **Simple and Extensible**: Easy to modify and extend for various CV processing requirements.

## Installation

### Prerequisites
- Python 3.x
- Redis server

### Setup
1. Clone the repository:
2. Install required Python packages from requirements.txt

## Usage

### Starting Redis Server
Ensure that the Redis server is running. Use docker to run the container:  
`docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest`

### Running the Producer
Run the producer script to enqueue CV processing tasks: python producer.py

### Running the Consumers
Start one or more consumer scripts to process the queued tasks: python consumer.py

## Project Structure

- `producer.py`: Script to enqueue CV processing tasks.
- `consumer.py`: Worker script to process tasks from the queue.
- `cv_processor.py`: Module containing the business logic for CV processing.

## Contributing
Contributions to this project are welcome. Please ensure to follow the guidelines below:
- Fork the repository and create your branch from `develop`.
- Write clear and concise commit messages.
- Ensure code style and quality compliance.
- Create a pull request with a comprehensive description of changes.

## License
GPL

## Contact
For any queries or contributions, please contact syed.atyab.hussain@gmail.com

## Acknowledgements
- Redis and RQ for providing the task queueing mechanisms.
- Contributors and maintainers of this project.
