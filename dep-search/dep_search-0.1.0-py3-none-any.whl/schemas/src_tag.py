"""Tag source schema definition."""

from typing import Dict, List, Optional
from pydantic import BaseModel

# from shared.dep_search.shared_types import TypeSource
from ..internals.builtins import TypeSource


class TagEventCategory(BaseModel):
    """Tag event category."""

    id: int
    name: str
    breadcrumbs: List[Dict]


class SourceTag(TypeSource):
    """Source tag."""

    id: int
    name: str
    slug: str
    event_category: Optional[TagEventCategory]

    @classmethod
    def __normalize__(cls, source: BaseModel) -> Dict:
        """Overrides."""

        normalized = source.dict(exclude=cls.exclude_fields())

        try:
            normalized['category_pk'] = cls.event_category.id
        except (AttributeError, KeyError, TypeError, ValueError):
            normalized['category_pk'] = None

        return normalized
