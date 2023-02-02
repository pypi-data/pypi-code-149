from marshmallow import fields, validate

from pynotion.schemas.base import BaseNotionSchema
from pynotion.schemas.common import (
    FileSchema,
    EmojiSchema,
    ParentSchema,
    RichTextSchema,
    PropertySchema,
)
from pynotion.schemas.user import UserSchema


class DatabaseSchema(BaseNotionSchema):
    object = fields.String(validate=validate.Equal("database"))
    id = fields.UUID()

    created_time = fields.DateTime()
    created_by = fields.Nested(UserSchema)

    last_edited_time = fields.DateTime()
    last_edited_by = fields.Nested(UserSchema)

    title = fields.List(fields.Nested(RichTextSchema))
    description = fields.List(fields.Nested(RichTextSchema))

    icon = fields.Nested(EmojiSchema)
    cover = fields.Nested(FileSchema)

    properties = fields.Dict(
        keys=fields.String(), values=fields.Nested(PropertySchema)
    )

    parent = fields.Nested(ParentSchema)
    url = fields.Url()
    archived = fields.Boolean()
    is_inline = fields.Boolean()
