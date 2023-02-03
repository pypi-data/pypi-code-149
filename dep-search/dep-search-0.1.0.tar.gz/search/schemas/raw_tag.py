"""Tag raw model definition."""

from typing import Optional

from ..internals.builtins import TypeRaw
# from .types import TypeRaw


class Tag(TypeRaw):
    """Raw tag."""

    name: str
    slug: str

    category_pk: Optional[int]
