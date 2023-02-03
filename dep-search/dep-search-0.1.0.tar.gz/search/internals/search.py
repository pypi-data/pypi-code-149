"""Search types."""

from typing import Any, Dict, List, Union

from dataclasses import dataclass
from httpx import AsyncClient
from collections import namedtuple
from pydantic import BaseModel

from .types import Expression
from ..schemas.raw_tag import Tag
from ..shared.shared_definitions import branch_digest

TypeTags = Union[None, List[Tag]]

TypeProxyResult = namedtuple('TypeProxyResult', ['items', 'count', 'total'])
TypeProxyIndex = namedtuple('TypeProxyIndex', ['method', 'serializer'])


@dataclass(frozen=True)
class TagResults:
    """Tag results."""

    items: TypeTags
    exists: bool
    count: int
    total: int

    details: Union[None, str]


IndexTag = 'tag'

_fallback_items = []
_fallback_count = 0
_fallback_total = 0
_default_lang = 'ru'
_default_limit = 25


@dataclass
class Search:
    """Async search."""

    url: str
    token: str
    client: AsyncClient

    __config__ = {
        IndexTag: TypeProxyIndex(method='raw_tags', serializer=Tag),
    }

    # Internals ---------------------------------------------------------------

    def _create_message(
        self,
        method: str,
        expression: Dict[str, Any],
        sorting: Dict[str, int],
        lang: str,
        page: int,
        limit: int,
    ) -> Dict:
        """Create message payload."""

        return {
            'jsonrpc': '2.0',
            'id': 0,
            'method': method,
            'params': {
                'query': {
                    'token': str(self.token),
                    'version': branch_digest,
                    'lang': str(lang),
                    'sorting': sorting,
                    'expression': expression,
                    'page': page,
                    'limit': limit,
                },
            },
        }

    def _read_items(self, response: Dict) -> List[Dict]:  # noqa
        """Read items from response."""
        try:
            return response['result']['data']['results']
        except Exception as _any:
            print(f'Error read response items: {_any}')
            return _fallback_items

    def _read_count(self, response: Dict) -> int:  # noqa
        """Read count from response."""
        try:
            return int(response['result']['data']['count'])
        except Exception as _any:
            print(f'Error read response count: {_any}')
            return _fallback_count

    def _read_total(self, response: Dict) -> int:  # noqa
        """Read total from response."""
        try:
            return int(response['result']['data']['total'])
        except Exception as _any:
            print(f'Error read response total: {_any}')
            return _fallback_total

    async def _lookup(
        self,
        name: str,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = _default_lang,
        limit: int = _default_limit,
        page: int = 1,
    ) -> TypeProxyResult:

        items, count, total, raw_expr = (
            _fallback_items,
            _fallback_count,
            _fallback_total,
            None,
        )

        if expression:
            raw_expr = expression.eval()

        message = self._create_message(
            method=self.__config__[name].method,
            expression=raw_expr,
            sorting=sorting,
            lang=lang,
            limit=limit,
            page=page,
        )

        response = await self.client.post(url=self.url, json=message)

        if response.status_code == 200:

            body = response.json()

            total = self._read_total(body)
            count = self._read_count(body)

            raw_items = self._read_items(body)
            if len(raw_items) >= 1:
                items = self._serialize(name=name, items=raw_items)

        return TypeProxyResult(items=items, count=count, total=total)

    def _serialize(self, name: str, items: List[Union[BaseModel, Any]]):
        """Serialize items."""

        try:
            raw_class = self.__config__[name].serializer
            return [raw_class(**item) for item in items]
        except Exception as _any_exc:
            print(f'Error in serialize: {_any_exc}')
            return _fallback_items

    # Exports -----------------------------------------------------------------

    async def tags(
        self,
        expression: Expression = None,
        sorting: Dict[str, int] = None,
        lang: str = 'ru',
        limit: int = 25,
        page: int = 1,
    ) -> TagResults:
        """Search tags."""

        items, details, exists, count, total = (
            _fallback_items,
            None,
            False,
            _fallback_count,
            _fallback_total,
        )

        try:
            result = await self._lookup(
                name=IndexTag,
                expression=expression,
                sorting=sorting,
                lang=lang,
                limit=limit,
                page=page,
            )

            if all([
                bool(result),
                bool(result.count),
                result.count >= 1,  # noqa
            ]):
                items, count, total = (
                    result.items,
                    result.count,
                    result.total,
                )

        except Exception as _any_exc:  # noqa
            details = f'Error: {_any_exc}'
        finally:
            return TagResults(
                items=items,
                details=details,
                exists=bool(count >= 1),
                count=count,
                total=total,
            )
