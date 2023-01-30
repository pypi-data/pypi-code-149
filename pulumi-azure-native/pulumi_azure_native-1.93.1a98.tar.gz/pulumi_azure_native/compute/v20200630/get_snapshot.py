# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetSnapshotResult',
    'AwaitableGetSnapshotResult',
    'get_snapshot',
    'get_snapshot_output',
]

warnings.warn("""Version 2020-06-30 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetSnapshotResult:
    """
    Snapshot resource.
    """
    def __init__(__self__, creation_data=None, disk_access_id=None, disk_size_bytes=None, disk_size_gb=None, disk_state=None, encryption=None, encryption_settings_collection=None, hyper_v_generation=None, id=None, incremental=None, location=None, managed_by=None, name=None, network_access_policy=None, os_type=None, provisioning_state=None, sku=None, tags=None, time_created=None, type=None, unique_id=None):
        if creation_data and not isinstance(creation_data, dict):
            raise TypeError("Expected argument 'creation_data' to be a dict")
        pulumi.set(__self__, "creation_data", creation_data)
        if disk_access_id and not isinstance(disk_access_id, str):
            raise TypeError("Expected argument 'disk_access_id' to be a str")
        pulumi.set(__self__, "disk_access_id", disk_access_id)
        if disk_size_bytes and not isinstance(disk_size_bytes, float):
            raise TypeError("Expected argument 'disk_size_bytes' to be a float")
        pulumi.set(__self__, "disk_size_bytes", disk_size_bytes)
        if disk_size_gb and not isinstance(disk_size_gb, int):
            raise TypeError("Expected argument 'disk_size_gb' to be a int")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if disk_state and not isinstance(disk_state, str):
            raise TypeError("Expected argument 'disk_state' to be a str")
        pulumi.set(__self__, "disk_state", disk_state)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if encryption_settings_collection and not isinstance(encryption_settings_collection, dict):
            raise TypeError("Expected argument 'encryption_settings_collection' to be a dict")
        pulumi.set(__self__, "encryption_settings_collection", encryption_settings_collection)
        if hyper_v_generation and not isinstance(hyper_v_generation, str):
            raise TypeError("Expected argument 'hyper_v_generation' to be a str")
        pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if incremental and not isinstance(incremental, bool):
            raise TypeError("Expected argument 'incremental' to be a bool")
        pulumi.set(__self__, "incremental", incremental)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_access_policy and not isinstance(network_access_policy, str):
            raise TypeError("Expected argument 'network_access_policy' to be a str")
        pulumi.set(__self__, "network_access_policy", network_access_policy)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> 'outputs.CreationDataResponse':
        """
        Disk source information. CreationData information cannot be changed after the disk has been created.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="diskAccessId")
    def disk_access_id(self) -> Optional[str]:
        """
        ARM id of the DiskAccess resource for using private endpoints on disks.
        """
        return pulumi.get(self, "disk_access_id")

    @property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> float:
        """
        The size of the disk in bytes. This field is read only.
        """
        return pulumi.get(self, "disk_size_bytes")

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[int]:
        """
        If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> str:
        """
        The state of the snapshot.
        """
        return pulumi.get(self, "disk_state")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionResponse']:
        """
        Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(self) -> Optional['outputs.EncryptionSettingsCollectionResponse']:
        """
        Encryption settings collection used be Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.
        """
        return pulumi.get(self, "encryption_settings_collection")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[str]:
        """
        The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def incremental(self) -> Optional[bool]:
        """
        Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed.
        """
        return pulumi.get(self, "incremental")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> str:
        """
        Unused. Always Null.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAccessPolicy")
    def network_access_policy(self) -> Optional[str]:
        """
        Policy for accessing the disk via network.
        """
        return pulumi.get(self, "network_access_policy")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        The Operating System type.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The disk provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SnapshotSkuResponse']:
        """
        The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time when the snapshot was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Unique Guid identifying the resource.
        """
        return pulumi.get(self, "unique_id")


class AwaitableGetSnapshotResult(GetSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotResult(
            creation_data=self.creation_data,
            disk_access_id=self.disk_access_id,
            disk_size_bytes=self.disk_size_bytes,
            disk_size_gb=self.disk_size_gb,
            disk_state=self.disk_state,
            encryption=self.encryption,
            encryption_settings_collection=self.encryption_settings_collection,
            hyper_v_generation=self.hyper_v_generation,
            id=self.id,
            incremental=self.incremental,
            location=self.location,
            managed_by=self.managed_by,
            name=self.name,
            network_access_policy=self.network_access_policy,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            tags=self.tags,
            time_created=self.time_created,
            type=self.type,
            unique_id=self.unique_id)


def get_snapshot(resource_group_name: Optional[str] = None,
                 snapshot_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotResult:
    """
    Snapshot resource.


    :param str resource_group_name: The name of the resource group.
    :param str snapshot_name: The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
    """
    pulumi.log.warn("""get_snapshot is deprecated: Version 2020-06-30 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['snapshotName'] = snapshot_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20200630:getSnapshot', __args__, opts=opts, typ=GetSnapshotResult).value

    return AwaitableGetSnapshotResult(
        creation_data=__ret__.creation_data,
        disk_access_id=__ret__.disk_access_id,
        disk_size_bytes=__ret__.disk_size_bytes,
        disk_size_gb=__ret__.disk_size_gb,
        disk_state=__ret__.disk_state,
        encryption=__ret__.encryption,
        encryption_settings_collection=__ret__.encryption_settings_collection,
        hyper_v_generation=__ret__.hyper_v_generation,
        id=__ret__.id,
        incremental=__ret__.incremental,
        location=__ret__.location,
        managed_by=__ret__.managed_by,
        name=__ret__.name,
        network_access_policy=__ret__.network_access_policy,
        os_type=__ret__.os_type,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        tags=__ret__.tags,
        time_created=__ret__.time_created,
        type=__ret__.type,
        unique_id=__ret__.unique_id)


@_utilities.lift_output_func(get_snapshot)
def get_snapshot_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        snapshot_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSnapshotResult]:
    """
    Snapshot resource.


    :param str resource_group_name: The name of the resource group.
    :param str snapshot_name: The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
    """
    pulumi.log.warn("""get_snapshot is deprecated: Version 2020-06-30 will be removed in v2 of the provider.""")
    ...
