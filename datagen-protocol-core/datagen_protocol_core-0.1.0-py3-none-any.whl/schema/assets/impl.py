from enum import Enum
from typing import Union, List, TypeVar, Generic

from pydantic import BaseModel
from pydantic.fields import ModelField, Field


class AssetAttr(str, Enum):
    pass


A = TypeVar("A")


class AttributesList(list, Generic[A]):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Union[A, List[A]], field: ModelField) -> List[A]:
        if not isinstance(v, list):
            v = [v]
        return [field.type_(v_) for v_ in v]


class AssetAttributes(BaseModel):
    class Config:
        frozen = True


class Asset(BaseModel):
    attributes: AssetAttributes = Field(default=None)

    def dict(self, *args, **kwargs):
        return super().dict(*args, exclude={"attributes"}, **kwargs)

    def copy(self, *args, **kwargs):
        return super().dict(*args, deep=True, **kwargs)
