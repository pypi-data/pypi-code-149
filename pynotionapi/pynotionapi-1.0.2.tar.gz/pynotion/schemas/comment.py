from marshmallow import fields, validate

from pynotion.schemas.base import BaseNotionSchema
from pynotion.schemas.common import ParentSchema, RichTextSchema
from pynotion.schemas.user import UserSchema


class CommentSchema(BaseNotionSchema):
    object = fields.String(validate=validate.Equal("comment"))
    id = fields.UUID()

    parent = fields.Nested(ParentSchema)
    discussion_id = fields.UUID()

    created_time = fields.DateTime()
    last_edited_time = fields.DateTime()
    created_by = fields.Nested(UserSchema)

    rich_text = fields.List(fields.Nested(RichTextSchema))
