from typing import Mapping, Optional

from pynotion.endpoints.base import BaseEndpoint
from pynotion.types import Block, Pagination


class BlocksEndpoint(BaseEndpoint):
    def retrieve(self, block_id: str) -> dict:
        return self.request(method="get", endpoint=f"blocks/{block_id}")

    def update(
        self, block_id: str, archived: Optional[bool] = None, **kwargs: Mapping
    ) -> dict:
        return self.request(
            method="patch",
            endpoint=f"blocks/{block_id}",
            json={"archived": archived, **kwargs},
        )

    def retrieve_children(
        self, block_id: str, pagination: Optional[Pagination] = None
    ) -> dict:
        return self.request(
            method="get",
            endpoint=f"blocks/{block_id}/children",
            json=(pagination or {}),
        )

    def append_children(self, block_id: str, children: list[Block]) -> dict:
        return self.request(
            method="patch",
            endpoint=f"blocks/{block_id}/children",
            json={"children": children},
        )

    def delete(self, block_id: str) -> dict:
        return self.request(method="delete", endpoint=f"blocks/{block_id}")
