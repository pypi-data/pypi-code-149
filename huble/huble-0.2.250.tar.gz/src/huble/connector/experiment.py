import requests
from boto3.session import Session


class Experiment:
    def __init__(self, experiment_id: str) -> None:
        self.experiment_id = experiment_id
        self.graph, self.task_type, self.target_column = self.__get_experiment_details(experiment_id=experiment_id)

    def __get_experiment_details(self, experiment_id: str):
        try:
            response = requests.get(
                f"http://localhost:8000/experiments/{experiment_id}",
            )
            response = response.json()
        except:
            raise Exception("Unable to connect to the server")
        try:
            graph = response["pipelineJSON"]
            project = response["project"]
            target_column = project["targetColumn"]
            task_type = project["taskType"]
        except:
            raise Exception("Invalid Experiment ID")
        return graph, task_type, target_column

    def upload_metrics(self, metrics, input_format):
        requests.put(
            f"http://localhost:8000/experiments/results/{self.experiment_id}",
            data={"metrics": metrics, "input_format": input_format},
        )

    def upload_model(self, file_name):
        session = Session()
        client = session.client(
            "s3",
            region_name="us-east-1",
            endpoint_url="https://s3.filebase.com",
            aws_access_key_id="709B6E02413B7282AC93",
            aws_secret_access_key="EyByFcqsBwTe4bWq6PwnoUJ9e2BqzShztJ48efVH",
        )

        bucket_name = "testsesaetsatast"
        with open(file_name, "rb") as data:
            client.upload_fileobj(data, bucket_name, file_name)
