r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["AggrSpaceEfficiency", "AggrSpaceEfficiencySchema"]
__pdoc__ = {
    "AggrSpaceEfficiencySchema.resource": False,
    "AggrSpaceEfficiencySchema.opts": False,
    "AggrSpaceEfficiency": False,
}


class AggrSpaceEfficiencySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AggrSpaceEfficiency object"""

    auto_adaptive_compression_savings = fields.Boolean(data_key="auto_adaptive_compression_savings")
    r""" Indicates whether or not aggregate has auto adaptive compression savings. """

    cross_volume_background_dedupe = fields.Boolean(data_key="cross_volume_background_dedupe")
    r""" Indicates whether or not cross volume background deduplication is enabled. """

    cross_volume_dedupe_savings = fields.Boolean(data_key="cross_volume_dedupe_savings")
    r""" Indicates whether or not aggregate has cross volume deduplication savings. """

    cross_volume_inline_dedupe = fields.Boolean(data_key="cross_volume_inline_dedupe")
    r""" Indicates whether or not cross volume inline deduplication is enabled. """

    logical_used = Size(data_key="logical_used")
    r""" Logical used """

    ratio = fields.Number(data_key="ratio")
    r""" Data reduction ratio (logical_used / used) """

    savings = Size(data_key="savings")
    r""" Space saved by storage efficiencies (logical_used - used) """

    @property
    def resource(self):
        return AggrSpaceEfficiency

    gettable_fields = [
        "auto_adaptive_compression_savings",
        "cross_volume_background_dedupe",
        "cross_volume_dedupe_savings",
        "cross_volume_inline_dedupe",
        "logical_used",
        "ratio",
        "savings",
    ]
    """auto_adaptive_compression_savings,cross_volume_background_dedupe,cross_volume_dedupe_savings,cross_volume_inline_dedupe,logical_used,ratio,savings,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class AggrSpaceEfficiency(Resource):

    _schema = AggrSpaceEfficiencySchema
