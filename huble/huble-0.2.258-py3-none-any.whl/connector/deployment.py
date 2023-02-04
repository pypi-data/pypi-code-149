import requests
from .experiment import Experiment

class Deployment:

    def generate_code(self, experiment_id: str):
        experiment = Experiment(experiment_id=experiment_id)
        with open("deployment.py", "w") as f:
            f.write("import requests")
            f.write("\nimport os")
            f.write("\nfrom pydantic import BaseModel")
            f.write("\nfrom huble import Experiment")
            f.write("\nfrom typing import Union")
            f.write("\nexperiment_id = os.getenv(\"EXPERIMENT_ID\")")
            f.write(f"\nexperiment = Experiment(experiment_id)")
            f.write("\n")
            f.write("\nclass RequestBody(BaseModel):")
            for column in experiment.input_format["columns"]:
                f.write(f"\n\t{column['name']}: Union[int, float]")
            f.write("\n")
            f.write(f"\nmodel_url = experiment.modelURL")
            f.write('model = requests.get(f"https://ipfs.filebase.io/ipfs/{model_url}")')
            f.write("\n")
            f.write("\ndef predict(request_body: RequestBody):")
            f.write("\n\treturn model.predict(request_body.dict())")



