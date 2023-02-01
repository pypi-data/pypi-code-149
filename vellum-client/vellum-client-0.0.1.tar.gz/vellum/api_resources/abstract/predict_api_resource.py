from abc import abstractmethod
from typing import Any

from openai.util import convert_to_openai_object

from vellum.api_resources.abstract.api_resource import APIResource


class PredictAPIResource(APIResource):
    @property
    @abstractmethod
    def api_path(self) -> str:
        pass

    api_base = "https://predict.vellum.ai"

    @classmethod
    def run(cls, **kwargs: Any) -> dict:
        result = cls._make_request("POST", cls.api_path, json=kwargs).json()

        if result.get("provider") == "OPENAI":
            result["provider_object"] = convert_to_openai_object(result["raw"])

        return result
