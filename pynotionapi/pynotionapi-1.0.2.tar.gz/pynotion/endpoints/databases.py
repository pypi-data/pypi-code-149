from typing import Mapping, Optional

from pynotion.endpoints.base import BaseEndpoint
from pynotion.types import Pagination, Parent, Property, RichText, Sort


class DatabasesEndpoint(BaseEndpoint):
    def query(
        self,
        database_id: str,
        _filter: Optional[Mapping] = None,
        sorts: Optional[list[Sort]] = None,
        pagination: Optional[Pagination] = None,
    ) -> dict:
        return self.request(
            method="post",
            endpoint=f"databases/{database_id}/query",
            json={"filter": _filter, "sorts": sorts, **(pagination or {})},
        )

    def retrieve(self, database_id: str) -> dict:
        return self.request(method="get", endpoint=f"databases/{database_id}")

    def create(
        self,
        parent: Parent,
        properties: Mapping[str, Property],
        title: Optional[list[RichText]] = None,
    ) -> dict:
        return self.request(
            method="post",
            endpoint="databases",
            json={"parent": parent, "properties": properties, "title": title},
        )

    def update(
        self,
        database_id: str,
        properties: Optional[Mapping[str, Property]] = None,
        title: Optional[list[RichText]] = None,
    ) -> dict:
        return self.request(
            method="patch",
            endpoint=f"databases/{database_id}",
            json={"properties": properties, "title": title},
        )
