from typing import Optional

from pynotion.endpoints.base import BaseEndpoint
from pynotion.types import Filter, Pagination, Sort


class SearchEndpoint(BaseEndpoint):
    def __call__(
        self,
        query: Optional[str] = None,
        sort: Optional[Sort] = None,
        _filter: Optional[Filter] = None,
        pagination: Optional[Pagination] = None,
    ) -> dict:
        return self.request(
            method="post",
            endpoint="search",
            json={
                "query": query,
                "sort": sort,
                "filter": _filter,
                **(pagination or {}),
            },
        )
