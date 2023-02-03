r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["EmsEventAction", "EmsEventActionSchema"]
__pdoc__ = {
    "EmsEventActionSchema.resource": False,
    "EmsEventActionSchema.opts": False,
    "EmsEventAction": False,
}


class EmsEventActionSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the EmsEventAction object"""

    confirmation_message = fields.Nested("netapp_ontap.models.ems_ui_message.EmsUiMessageSchema", unknown=EXCLUDE, data_key="confirmation_message")
    r""" The confirmation_message field of the ems_event_action. """

    description = fields.Nested("netapp_ontap.models.ems_ui_message.EmsUiMessageSchema", unknown=EXCLUDE, data_key="description")
    r""" The description field of the ems_event_action. """

    href = fields.Str(data_key="href")
    r""" URI on which to perform the action, using the HTTP method specified in the method property.

Example: /api/resourcelink """

    method = fields.Str(data_key="method")
    r""" HTTP verb, such as PATCH, POST, used to perform the action.

Example: PATCH """

    name = fields.Str(data_key="name")
    r""" Name of the action.

Example: schedule """

    parameters = fields.List(fields.Nested("netapp_ontap.models.ems_action_parameter.EmsActionParameterSchema", unknown=EXCLUDE), data_key="parameters")
    r""" Parameter list for the action. """

    title = fields.Nested("netapp_ontap.models.ems_ui_message.EmsUiMessageSchema", unknown=EXCLUDE, data_key="title")
    r""" The title field of the ems_event_action. """

    @property
    def resource(self):
        return EmsEventAction

    gettable_fields = [
        "confirmation_message",
        "description",
        "href",
        "method",
        "name",
        "parameters",
        "title",
    ]
    """confirmation_message,description,href,method,name,parameters,title,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class EmsEventAction(Resource):

    _schema = EmsEventActionSchema
