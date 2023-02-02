from marshmallow import fields, validate

from pynotion.enums import UserType
from pynotion.schemas.base import BaseNotionSchema


class PersonSchema(BaseNotionSchema):
    email = fields.Email()


class BotSchema(BaseNotionSchema):
    owner = fields.Dict()
    workspace_name = fields.String()


class UserSchema(BaseNotionSchema):
    object = fields.String(validate=validate.Equal("user"))
    id = fields.UUID()

    type = fields.Enum(UserType, by_value=True)
    name = fields.String()
    avatar_url = fields.Url()

    person = fields.Nested(PersonSchema)
    bot = fields.Nested(BotSchema)
