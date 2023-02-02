from marshmallow import fields, validate

from pynotion.enums import BlockType
from pynotion.schemas.base import BaseNotionSchema
from pynotion.schemas.common import ParentSchema
from pynotion.schemas.user import UserSchema


class BlockSchema(BaseNotionSchema):
    object = fields.String(validate=validate.Equal("block"))
    id = fields.UUID()
    parent = fields.Nested(ParentSchema)
    type = fields.Enum(BlockType, by_value=True)

    created_time = fields.DateTime()
    created_by = fields.Nested(UserSchema)

    last_edited_time = fields.DateTime()
    last_edited_by = fields.Nested(UserSchema)

    archived = fields.Boolean()
    has_children = fields.Boolean()
