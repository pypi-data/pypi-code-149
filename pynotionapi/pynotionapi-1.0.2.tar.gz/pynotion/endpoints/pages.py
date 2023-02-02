from typing import Mapping, Optional

from pynotion.endpoints.base import BaseEndpoint
from pynotion.types import Block, PageDecoration, Pagination, Parent, Property


class PagesEndpoint(BaseEndpoint):
    def retrieve(self, page_id: str) -> dict:
        return self.request(method="get", endpoint=f"pages/{page_id}")

    def create(
        self,
        parent: Parent,
        properties: Mapping[str, Property],
        children: Optional[list[Block]] = None,
        decoration: Optional[PageDecoration] = None,
    ) -> dict:
        return self.request(
            method="post",
            endpoint="pages",
            json={
                "parent": parent,
                "properties": properties,
                "children": children,
                **(decoration or {}),
            },
        )

    def update(
        self,
        page_id: str,
        properties: Optional[Mapping[str, Property]] = None,
        archived: Optional[bool] = None,
        decoration: Optional[PageDecoration] = None,
    ) -> dict:
        return self.request(
            method="patch",
            endpoint=f"pages/{page_id}",
            json={
                "properties": properties,
                "archived": archived,
                **(decoration or {}),
            },
        )

    def delete(self, page_id: str) -> dict:
        return self.update(page_id=page_id, archived=True)

    def archive(self, page_id: str) -> dict:
        return self.delete(page_id=page_id)

    def retrieve_property_item(
        self,
        page_id: str,
        property_id: str,
        pagination: Optional[Pagination] = None,
    ) -> dict:
        return self.request(
            method="get",
            endpoint=f"pages/{page_id}/properties/{property_id}",
            json=(pagination or {}),
        )
