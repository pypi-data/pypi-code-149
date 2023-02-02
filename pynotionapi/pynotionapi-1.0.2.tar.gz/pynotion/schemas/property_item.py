from marshmallow import fields, validate

from pynotion.enums import PropertyType
from pynotion.schemas.base import BaseNotionSchema


class PropertyItemSchema(BaseNotionSchema):
    object = fields.String(validate=validate.Equal("property_item"))
    id = fields.String()
    type = fields.Enum(PropertyType, by_value=True)
    next_url = fields.Url()
