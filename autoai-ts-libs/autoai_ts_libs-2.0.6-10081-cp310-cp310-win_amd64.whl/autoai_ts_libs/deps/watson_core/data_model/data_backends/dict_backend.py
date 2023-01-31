# *****************************************************************#
# (C) Copyright IBM Corporation 2022.                              #
#                                                                  #
# The source code for this program is not published or otherwise   #
# divested of its trade secrets, irrespective of what has been     #
# deposited with the U.S. Copyright Office.                        #
# *****************************************************************#
"""The dict-based backend implementation
"""

# Standard
from typing import Any, Iterable, Type

# First Party
import alog

# Local
from ...toolkit.errors import error_handler
from ..base import DataBase
from .base import DataModelBackendBase


log = alog.use_channel("DATAB")
error = error_handler.get(log)


# DictBackend ##################################################################


class DictBackend(DataModelBackendBase):
    """Data model backend for a raw dict"""

    def __init__(self, data_dict: dict):
        """Construct with the dict"""
        error.type_check("<COR85037210E>", dict, data_dict=data_dict)
        self._data_dict = data_dict

    def get_attribute(self, data_model_class: Type[DataBase], name: str) -> Any:
        """Fetch the attribute out of the internal dict and validate it against
        the target data model class. If the target attribute is a nested data
        model type, wrap the corresponding nested dict in an instance of this
        same backend.

        Args:
            data_model_class:  Type[DataBase]
                The frontend data model class that is accessing this attribute
            name:  str
                The name of the attribute to access

        Returns:
            value:  Any
                The extracted attribute value
        """

        # NOTE: We do not type-check the args here for efficiency. This method
        #   should only be called by the DataBase class, so we can assume it's
        #   being used correctly.

        # Make sure the name is a valid field on the given class
        if name not in data_model_class.fields:
            error(
                "<COR85037211E>",
                AttributeError(
                    f"No such attribute [{name}] on [{data_model_class.__name__}]"
                ),
            )

        # Get the value from the internal dict
        raw_value = self._data_dict.get(name)

        # If the target attribute is itself a message, make sure the value is a
        # dict, then wrap it in the corresponding data model object with the a
        # new backend instance.
        if name in data_model_class._fields_message and raw_value is not None:
            error.type_check("<COR85037212E>", dict, **{name: raw_value})
            field_backend = self.__class__(raw_value)
            proto_class = data_model_class._proto_class
            field_dm_class = DataBase.class_registry[
                proto_class.DESCRIPTOR.fields_by_name[name].message_type.name
            ]
            return field_dm_class.from_backend(self.__class__(raw_value))

        # If the target attribute is a repeated message, convert it to a list of
        # nested messages with dict backends
        #
        # TODO: It may be better to do this lazily, but that would come at the
        #   expense of being able to re-iterate or randomly-index into the
        #   object. We could consider writing a lazily constructed list to avoid
        #   costruction of the messages that aren't used.
        if name in data_model_class._fields_message_repeated and raw_value is not None:
            error.type_check("<COR85037213E>", Iterable, **{name: raw_value})
            field_dm_class = data_model_class.get_field_message_type(name)
            return [
                field_dm_class.from_backend(self.__class__(entry))
                for entry in raw_value
            ]

        return raw_value
