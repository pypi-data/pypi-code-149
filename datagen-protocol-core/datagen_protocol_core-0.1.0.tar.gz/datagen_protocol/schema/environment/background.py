from pydantic import BaseModel

from datagen_protocol.config import conf
from datagen_protocol.schema import fields


class Background(BaseModel):
    id: str
    rotation: float = fields.numeric(conf.background.rotation)
    transparent: bool = fields.bool(conf.background.transparency)
