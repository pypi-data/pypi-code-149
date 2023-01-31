# ****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# ****************************************************************#
"""Common serialization interfaces that are generally helpful for saving out models that
are not necessarily specific to any domain's 3rd party libraries.
"""
import abc

from . import fileio


class ObjectSerializer(abc.ABC):
    """Abstract class for serializing an object to disk."""

    @abc.abstractmethod
    def serialize(self, obj, file_path):
        """Serialize the provided object to the specified file path.

        Args:
            obj:  object
                The object to serialize
            file_path:  str
                Absolute path to which the object should be serialized
        """


class JSONSerializer(ObjectSerializer):
    """An ObjectSerializer for serializing to a JSON file."""

    def serialize(self, obj, file_path):
        """Serialize the provided object to a JSON file.

        Args:
            obj:  object
                The object to serialize
            file_path:  str
                Absolute path to which the object should be serialized
        """
        fileio.save_json(obj, file_path)


class TextSerializer(ObjectSerializer):
    """An ObjectSerializer for serializing a python list to a text file."""

    def serialize(self, data, file_path):
        """Serialize the provided python list to a text file.

        Args:
            data:  list(str)
                The list to serialize
            file_path:  str
                Absolute path to which the object should be serialized
        """
        lines = "\n".join(data)
        fileio.save_txt(lines, file_path)


class YAMLSerializer(ObjectSerializer):
    """An ObjectSerializer for serializing to a YAML file."""

    def serialize(self, obj, file_path):
        """Serialize the provided object to a YAML file.

        Args:
            obj:  object
                The object to serialize
            file_path:  str
                Absolute path to which the object should be serialized
        """
        fileio.save_yaml(obj, file_path)


class CSVSerializer(ObjectSerializer):
    """An ObjectSerializer for serializing to a CSV file."""

    def serialize(self, obj, file_path):
        """Serialize the provided object to a CSV file.

        Args:
            obj:  object
                The object to serialize
            file_path:  str
                Absolute path to which the object should be serialized
        """
        fileio.save_csv(obj, file_path)


class PickleSerializer(ObjectSerializer):
    """An ObjectSerializer for pickling arbitrary Python objects."""

    def serialize(self, obj, file_path):
        """Serialize the provided object to a CSV file.

        Args:
            obj: any
                The object to serialize
            file_path:  str
                Absolute path to which the object should be serialized
        """
        fileio.save_pickle(obj, file_path)
