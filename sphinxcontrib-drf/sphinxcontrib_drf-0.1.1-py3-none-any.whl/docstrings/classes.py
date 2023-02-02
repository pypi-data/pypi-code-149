"""
This module contains all functions which are used to improve the documentation of classes.
"""
from rest_framework import serializers
from sphinx.application import Sphinx


def improve_class_docstring(app: Sphinx, cls: type, lines: list[str]):
    """
    Improve the documentation of a class if it's a Django model or form

    :param app: The Sphinx application object
    :type app: ~sphinx.application.Sphinx

    :param cls: The instance of the class to document
    :type cls: object

    :param lines: The docstring lines
    :type lines: list [ str ]
    """
    if issubclass(cls, serializers.Serializer):
        improve_serializer_docstring(app, cls, lines)


def improve_serializer_docstring(app: Sphinx, serializer: type[serializers.Serializer], lines: list[str]) -> None:
    """
    Improve the documentation of a Django :class:`~rest_framework.serializer.Serializer` subclass.

    This adds all model fields as parameters to the ``__init__()`` method.

    :param app: The Sphinx application object
    :type app: ~sphinx.application.Sphinx

    :param model: The instance of the model to document
    :type model: ~django.db.models.Model

    :param lines: The docstring lines
    :type lines: list [ str ]
    """

    lines.append("**Fields:**")
    lines.append("")
    for field_name, field in serializer._declared_fields.items():
        required_prefix = "\\* " if field.required else ""

        field_type = f"{field.__class__.__module__}.{field.__class__.__name__}"
        lines.append(f"* {required_prefix}``{field_name}``: (:class:`~{field_type}`)")

        if hasattr(field, "allow_blank"):
            lines.append("")
            lines.append(f"  * ``allow_blank``: {field.allow_blank}")

        lines.append("")
        lines.append(f"  * ``allow_null``: {field.allow_null}")

        if not issubclass(field.__class__, serializers.PrimaryKeyRelatedField) and hasattr(field, "choices") and field.choices:
            choices = [value for _, value in field.choices.items()]
            lines.append("")
            lines.append(f"  * ``choices``: {choices}")

        lines.append("")
