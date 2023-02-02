from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pynotion.client import PyNotionClient


class BaseEndpoint:
    def __init__(self, client: "PyNotionClient") -> None:
        self.client: "PyNotionClient" = client

    def request(self, *args, **kwargs) -> dict:
        if request_data := kwargs.get("json"):
            kwargs["json"] = self.clean_request_data(request_data)

        return self.client.request(*args, **kwargs)

    @staticmethod
    def clean_request_data(request_data: dict) -> dict:
        return {k: v for k, v in request_data.items() if v is not None}
