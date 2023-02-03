"""Tag raw model definition."""

from typing import Optional

from .types import TypeRaw


class Tag(TypeRaw):
    """Raw tag."""

    name: str
    slug: str

    category_pk: Optional[int]
