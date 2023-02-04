from typing import Optional, List, Dict, Any

from vellum.api_resources.types import GenerateResult
from vellum.api_resources.abstract.predict_api_resource import PredictAPIResource


class Generate(PredictAPIResource):
    api_path = "v1/generate"

    @classmethod
    def run(
        cls,
        deployment_id: Optional[str] = None,
        deployment_name: Optional[str] = None,
        input_values: List[Dict[str, Any]] = None,
    ) -> GenerateResult:
        """Run a generation request against Vellum's predict API.

        Args:
            deployment_id: The ID of the deployment to use for generating predictions. You must provide either this
                or deployment_name.
            deployment_name: The name of the deployment to use for generating predictions. You must provide either
                this or deployment_id.
            input_values: A list of input values to generate predictions for. Provide a list of length one
                to make a single prediction, or provide multiple items to perform a batch prediction.
                Each item in the list should be a dictionary of input variable names to values.

        Returns:
            The result of the generation request.
        """

        if deployment_id is None and deployment_name is None:
            raise ValueError("Must provide either deployment_id or deployment_name")
        elif deployment_id is not None and deployment_name is not None:
            raise ValueError("Must provide only one of deployment_id or deployment_name")

        raw_result = super().run(
            deployment_id=deployment_id, deployment_name=deployment_name, input_values=input_values
        )

        return GenerateResult.from_raw(raw_result)
