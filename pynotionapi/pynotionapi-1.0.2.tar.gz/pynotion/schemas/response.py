from typing import Callable

from marshmallow import fields, validate

from pynotion.enums import ResponseType
from pynotion.schemas.base import BaseNotionSchema
from pynotion.schemas.block import BlockSchema
from pynotion.schemas.comment import CommentSchema
from pynotion.schemas.database import DatabaseSchema
from pynotion.schemas.page import PageSchema
from pynotion.schemas.property_item import PropertyItemSchema
from pynotion.schemas.user import UserSchema


class ReponseSchema(BaseNotionSchema):
    has_more = fields.Boolean()
    next_cursor = fields.String()

    results = fields.Method(deserialize="parse_results")
    object = fields.String(validate=validate.Equal("list"))
    type = fields.Enum(ResponseType, by_value=True)

    def parse_results(self, value: list) -> list[dict]:
        return [SCHEMAS_MAP[v["object"]]().load(v) for v in value]


SCHEMAS_MAP: dict[str, Callable] = {
    "block": BlockSchema,
    "comment": CommentSchema,
    "database": DatabaseSchema,
    "page": PageSchema,
    "property_item": PropertyItemSchema,
    "list": ReponseSchema,
    "user": UserSchema,
}
