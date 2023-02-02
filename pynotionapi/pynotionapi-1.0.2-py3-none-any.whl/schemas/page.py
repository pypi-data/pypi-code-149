from marshmallow import fields, validate

from pynotion.schemas.base import BaseNotionSchema
from pynotion.schemas.common import (
    FileSchema,
    EmojiSchema,
    ParentSchema,
    PropertySchema,
)
from pynotion.schemas.user import UserSchema


class PageSchema(BaseNotionSchema):
    object = fields.String(validate=validate.Equal("page"))
    id = fields.UUID()

    created_time = fields.DateTime()
    created_by = fields.Nested(UserSchema)

    last_edited_time = fields.DateTime()
    last_edited_by = fields.Nested(UserSchema)

    archived = fields.Boolean()

    icon = fields.Nested(EmojiSchema)
    cover = fields.Nested(FileSchema)

    properties = fields.Dict(
        keys=fields.String(), values=fields.Nested(PropertySchema)
    )

    parent = fields.Nested(ParentSchema)
    url = fields.Url()
