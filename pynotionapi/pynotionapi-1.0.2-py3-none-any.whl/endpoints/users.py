from typing import Optional

from pynotion.endpoints.base import BaseEndpoint
from pynotion.types import Pagination


class UsersEndpoint(BaseEndpoint):
    def retrieve(self, user_id: str) -> dict:
        return self.request(method="get", endpoint=f"users/{user_id}")

    def list_all(self, pagination: Optional[Pagination] = None) -> dict:
        return self.request(
            method="get", endpoint="users", params=(pagination or {})
        )

    def retrieve_bot(self) -> dict:
        return self.request(method="get", endpoint="users/me")
