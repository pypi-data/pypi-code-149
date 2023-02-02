import logging
from typing import Optional

from requests import PreparedRequest, Request, Response, Session

from pynotion.endpoints import (
    BlocksEndpoint,
    CommentsEndpoint,
    DatabasesEndpoint,
    PagesEndpoint,
    SearchEndpoint,
    UsersEndpoint,
)
from pynotion.exceptions import ERRORS_MAP
from pynotion.schemas import SCHEMAS_MAP


# pylint: disable-next=too-many-instance-attributes
class PyNotionClient:
    def __init__(
        self,
        integration_token: str,
        notion_version: str,
        timeout: int = 15,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self.integration_token = integration_token
        self.notion_version = notion_version

        self.timeout = timeout
        self.logger = logger or logging.getLogger("pynotion")

        self.blocks = BlocksEndpoint(self)
        self.comments = CommentsEndpoint(self)
        self.databases = DatabasesEndpoint(self)
        self.pages = PagesEndpoint(self)
        self.search = SearchEndpoint(self)
        self.users = UsersEndpoint(self)

    def request(self, **kwargs) -> dict:
        prepared_request = self.prepare_request(**kwargs)

        response = Session().send(
            request=prepared_request, timeout=self.timeout
        )
        self.logger.debug("Response text: %s", response.text)

        return self.check_response(response)

    def prepare_request(
        self, method: str, endpoint: str, **kwargs
    ) -> PreparedRequest:
        request_args = {
            "method": method.upper(),
            "url": self.make_url(endpoint),
            "headers": self.headers,
            **kwargs,
        }
        request = Request(**request_args).prepare()

        self.logger.debug("Prepared a request: %s", request_args)
        return request

    def make_url(self, endpoint: str) -> str:
        return f"https://api.notion.com/v1/{endpoint}"

    @property
    def headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.integration_token}",
            "Notion-Version": self.notion_version,
        }

    def check_response(self, response: Response) -> dict:
        data = response.json()

        if not response.ok:
            code = data["code"]
            message = data["message"]

            raise ERRORS_MAP[code](message, response)

        return SCHEMAS_MAP[data["object"]]().load(data)
