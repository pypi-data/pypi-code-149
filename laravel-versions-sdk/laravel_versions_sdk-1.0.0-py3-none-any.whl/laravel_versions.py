from typing import Optional, cast, Union

import requests

from laravel_versions.types import LaravelVersionsCollection, LaravelVersionsSingular

TIMEOUT = 3
API_BASE_URI = "https://laravelversions.com/api"


class LaravelVersionsException(RuntimeError):
    """Unknown error"""


class NotFoundException(LaravelVersionsException):
    """Not Found"""


class LaravelVersions:
    def __init__(self, base_uri: str = API_BASE_URI) -> None:
        self.base_uri: str = base_uri

    def versions(self) -> LaravelVersionsCollection:
        return cast(LaravelVersionsCollection, self.get("/versions"))

    def version(self, version: Union[str, int]) -> LaravelVersionsSingular:
        return cast(LaravelVersionsSingular, self.get("/versions/{}".format(version)))

    def get(self, url: str):
        return self.__request("GET", url)

    def post(self, url: str, data: Optional[dict] = None):
        if data is None:
            data = {}
        return self.__request("POST", url, data)

    def __request(self, method: str, url: str, params: Optional[dict] = None):
        if params is None:
            params = {}

        if method == "GET":
            response = requests.get(self.base_uri + url, params=params)
        elif method == "POST":
            response = requests.post(self.base_uri + url, json=params)
        else:
            raise RuntimeError("Invalid request method provided")

        if response.status_code == 404:
            raise NotFoundException(response.json().get("error"))
        if response.status_code >= 400:
            raise LaravelVersionsException(
                response.json().get("error") or "Unknown error"
            )
        return response.json()
