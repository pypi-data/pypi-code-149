r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorPolicyRule", "SnapmirrorPolicyRuleSchema"]
__pdoc__ = {
    "SnapmirrorPolicyRuleSchema.resource": False,
    "SnapmirrorPolicyRuleSchema.opts": False,
    "SnapmirrorPolicyRule": False,
}


class SnapmirrorPolicyRuleSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorPolicyRule object"""

    count = Size(data_key="count")
    r""" Number of Snapshot copies to be kept for retention.

Example: 7 """

    creation_schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", unknown=EXCLUDE, data_key="creation_schedule")
    r""" The creation_schedule field of the snapmirror_policy_rule. """

    label = fields.Str(data_key="label")
    r""" Snapshot copy label

Example: hourly """

    period = fields.Str(data_key="period")
    r""" Specifies the duration for which the Snapshot copies are locked. The retention period value represents a duration and must be in the ISO-8601 duration format. Years, months, days, hours, minutes, and seconds are represented as "P<num>Y","P<num>M","P<num>D","PT<num>H","PT<num>M" and "PT<num>S". Value "infinite" is also a valid input for Flexvol volumes and FlexGroup volumes. A duration which combines different periods is not supported, for example "P1Y10M" is not supported. The range of supported retention period values is between 1 second to infinite.

Example: P30D """

    prefix = fields.Str(data_key="prefix")
    r""" Specifies the prefix for the Snapshot copy name to be created as per the schedule. If no value is specified, then the label is used as the prefix. """

    @property
    def resource(self):
        return SnapmirrorPolicyRule

    gettable_fields = [
        "count",
        "creation_schedule.links",
        "creation_schedule.name",
        "creation_schedule.uuid",
        "label",
        "period",
        "prefix",
    ]
    """count,creation_schedule.links,creation_schedule.name,creation_schedule.uuid,label,period,prefix,"""

    patchable_fields = [
        "count",
        "creation_schedule.name",
        "creation_schedule.uuid",
        "label",
        "period",
        "prefix",
    ]
    """count,creation_schedule.name,creation_schedule.uuid,label,period,prefix,"""

    postable_fields = [
        "count",
        "creation_schedule.name",
        "creation_schedule.uuid",
        "label",
        "period",
        "prefix",
    ]
    """count,creation_schedule.name,creation_schedule.uuid,label,period,prefix,"""


class SnapmirrorPolicyRule(Resource):

    _schema = SnapmirrorPolicyRuleSchema
