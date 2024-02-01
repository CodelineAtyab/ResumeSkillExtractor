from rq.job import Job
from rq.queue import Queue
from rq.registry import StartedJobRegistry
from rq_win import WindowsWorker
from rq.exceptions import NoSuchJobError


class CustomWindowsWorker(WindowsWorker):
    def handle_job_success(self, job: 'Job', queue: 'Queue', started_job_registry: StartedJobRegistry):
        super().handle_job_success(job, queue, started_job_registry)

        try:
            job.refresh()
            print(f">>>>>>> Job {job.id} is completed. The result is: {job.return_value()}")
        except NoSuchJobError:
            print(f">>>>>>> No Job found with ID: {job.id}")

