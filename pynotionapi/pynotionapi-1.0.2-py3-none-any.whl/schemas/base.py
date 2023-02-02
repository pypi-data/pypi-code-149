from typing import Any

from marshmallow import INCLUDE, Schema, pre_load


# pylint: disable-next=too-few-public-methods
class BaseNotionSchema(Schema):
    # pylint: disable-next=too-few-public-methods
    class Meta:
        datetimeformat = "iso"
        unknown = INCLUDE

    @pre_load
    def process_response(self, data: dict, **_: Any) -> dict[Any, Any]:
        return {k: v for k, v in data.items() if v is not None}
