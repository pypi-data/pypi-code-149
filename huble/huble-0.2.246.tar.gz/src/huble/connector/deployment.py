import requests


class Deployment:
    def __init__(self, deployment_id: str) -> None:
        self.deployment_id = deployment_id
        self.model_url = self.__get_deployment_details()

    def __get_deployment_details(self):
        try:
            response = requests.get(
                f"http://localhost:8000/deployments/sdk/{self.deployment_id}",
            )
            response = response.json()
        except:
            raise Exception("Unable to connect to the server")
        try:
            model_url = response["modelURL"]
        except:
            raise Exception("Invalid Deployment ID")
        return model_url

    def generate_code(self):
        with open("deployment.py", "w") as f:
            f.write("from pydantic import BaseModel")
            f.write("\nclass RequestBody(BaseModel):")
            f.write("\n\tdata: dict")
            f.write("\n")
            f.write("\ndef make_inference():")
            f.write("\n\t# TODO: Implement your inference logic here")