import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb

from . import interactive_console
from .config import ConfigUtils


class JobInfo:
    def __init__(self, stub, job_id):
        self._stub = stub
        self._job_id = job_id
        self._next_index = 0

    def show_progress(self):
        """Displays job progress in console."""
        if ConfigUtils.is_interactive_print_enabled():
            request = pb.JobProgressInput(job_id=self._job_id.job_id, next_index=self._next_index)
            response = self._stub.GetJobProgress(request)
            if response.progress:
                self._next_index += len(response.progress)
                for progress in response.progress:
                    interactive_console.log(f"Job ID: {self._job_id.job_id}, Status: {progress.message}")

    def get_metrics(self):
        """Obtain the completed metrics of a job.

        Returns:
            dict: A dictionary which consists of completed job progress.

            For example:

            {'Finished setting up spark session.': '6s',
            'Finished reading data from source location to extract schema.': '7s',
            'Schema generation completed.': '0s'}

        Typical example:
            job.get_metrics()

        For more details:
            https://docs.h2o.ai/feature-store/latest-stable/docs/api/jobs_api.html?highlight=get_metrics#checking-job-metrics
        """
        if self._stub.GetJob(self._job_id).done:
            request = pb.JobProgressInput(job_id=self._job_id.job_id, next_index=0)
            response = self._stub.GetJobProgress(request)
            if response.progress:
                return {progress.message: f"{progress.duration_in_seconds}s" for progress in response.progress}
        else:
            interactive_console.log("Job is still running. Please wait until the job finishes.")
