from typing import Optional

from pynotion.endpoints.base import BaseEndpoint
from pynotion.types import Pagination, Parent


class CommentsEndpoint(BaseEndpoint):
    def retrieve(
        self, block_id: str, pagination: Optional[Pagination] = None
    ) -> dict:
        return self.request(
            method="get",
            endpoint="comments",
            params={"block_id": block_id, **(pagination or {})},
        )

    def create(
        self,
        rich_text: dict,
        parent: Optional[Parent] = None,
        discussion_id: Optional[str] = None,
    ) -> dict:
        return self.request(
            method="post",
            endpoint="comments",
            json={
                "rich_text": rich_text,
                "parent": parent,
                "discussion_id": discussion_id,
            },
        )
