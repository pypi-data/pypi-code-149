from marshmallow import fields

from pynotion.enums import (
    FileType,
    EmojiType,
    ParentType,
    PropertyType,
    RichTextType,
)
from pynotion.schemas.base import BaseNotionSchema


class FileSchema(BaseNotionSchema):
    type = fields.Enum(FileType, by_value=True)
    url = fields.Url()
    expiry_time = fields.DateTime()


class EmojiSchema(FileSchema):
    type = fields.Enum(EmojiType, by_value=True)
    emoji = fields.String()


class ParentSchema(BaseNotionSchema):
    type = fields.Enum(ParentType, by_value=True)

    database_id = fields.UUID()
    page_id = fields.UUID()
    workspace = fields.Boolean()
    block_id = fields.UUID()


class PropertySchema(BaseNotionSchema):
    id = fields.String()
    type = fields.Enum(PropertyType, by_value=True)
    name = fields.String()


class RichTextSchema(BaseNotionSchema):
    type = fields.Enum(RichTextType, by_value=True)
    annotations = fields.Dict()
    plain_text = fields.String()
    href = fields.String()
