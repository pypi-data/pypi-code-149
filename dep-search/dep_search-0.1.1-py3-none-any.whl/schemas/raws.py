"""Tag raw model definition."""

from typing import Optional

from ..internals.builtins import TypeRaw


class TypeTag(TypeRaw):
    """Raw type tag."""

    name: str
    slug: str

    category_pk: Optional[int]
