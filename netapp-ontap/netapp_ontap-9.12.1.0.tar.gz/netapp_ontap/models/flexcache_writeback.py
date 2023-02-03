r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["FlexcacheWriteback", "FlexcacheWritebackSchema"]
__pdoc__ = {
    "FlexcacheWritebackSchema.resource": False,
    "FlexcacheWritebackSchema.opts": False,
    "FlexcacheWriteback": False,
}


class FlexcacheWritebackSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the FlexcacheWriteback object"""

    enabled = fields.Boolean(data_key="enabled")
    r""" Indicates whether or not writeback is enabled for the FlexCache volume. Writeback is a storage method where data is first written to the FlexCache volume and then written to the origin of a FlexCache volume. """

    per_inode_dirty_limit = Size(data_key="per_inode_dirty_limit")
    r""" Specifies the amount of data in 4KB blocks that the system can write per inode in a FlexCache volume before a writeback is initiated for that inode. This property is only relevant to a FlexCache Volume with the writeback property enabled. """

    scrub_threshold = Size(data_key="scrub_threshold")
    r""" Specifies the threshold value in 4KB data blocks which when hit will trigger a scrub that will initiate writeback for all dirty inodes on the FlexCache volume. This property is only relevant to a FlexCache Volume with the writeback property enabled. """

    transfer_limit = Size(data_key="transfer_limit")
    r""" Specifies the maximum number of 4KB data blocks the system can transfer, at one time, from the cache to the origin. This process will keep on recurring until all the dirty blocks for the inode are transferred to the origin volume. This property is only relevant to a FlexCache Volume with the writeback property enabled. """

    @property
    def resource(self):
        return FlexcacheWriteback

    gettable_fields = [
        "enabled",
        "per_inode_dirty_limit",
        "scrub_threshold",
        "transfer_limit",
    ]
    """enabled,per_inode_dirty_limit,scrub_threshold,transfer_limit,"""

    patchable_fields = [
        "enabled",
        "per_inode_dirty_limit",
        "scrub_threshold",
        "transfer_limit",
    ]
    """enabled,per_inode_dirty_limit,scrub_threshold,transfer_limit,"""

    postable_fields = [
        "enabled",
        "per_inode_dirty_limit",
        "scrub_threshold",
        "transfer_limit",
    ]
    """enabled,per_inode_dirty_limit,scrub_threshold,transfer_limit,"""


class FlexcacheWriteback(Resource):

    _schema = FlexcacheWritebackSchema
