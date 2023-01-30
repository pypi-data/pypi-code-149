# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ManagedClusterSnapshotArgs', 'ManagedClusterSnapshot']

@pulumi.input_type
class ManagedClusterSnapshotArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 creation_data: Optional[pulumi.Input['CreationDataArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 snapshot_type: Optional[pulumi.Input[Union[str, 'SnapshotType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ManagedClusterSnapshot resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['CreationDataArgs'] creation_data: CreationData to be used to specify the source resource ID to create this snapshot.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_name: The name of the managed cluster resource.
        :param pulumi.Input[Union[str, 'SnapshotType']] snapshot_type: The type of a snapshot. The default is NodePool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if creation_data is not None:
            pulumi.set(__self__, "creation_data", creation_data)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if snapshot_type is not None:
            pulumi.set(__self__, "snapshot_type", snapshot_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[pulumi.Input['CreationDataArgs']]:
        """
        CreationData to be used to specify the source resource ID to create this snapshot.
        """
        return pulumi.get(self, "creation_data")

    @creation_data.setter
    def creation_data(self, value: Optional[pulumi.Input['CreationDataArgs']]):
        pulumi.set(self, "creation_data", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[pulumi.Input[Union[str, 'SnapshotType']]]:
        """
        The type of a snapshot. The default is NodePool.
        """
        return pulumi.get(self, "snapshot_type")

    @snapshot_type.setter
    def snapshot_type(self, value: Optional[pulumi.Input[Union[str, 'SnapshotType']]]):
        pulumi.set(self, "snapshot_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ManagedClusterSnapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_data: Optional[pulumi.Input[pulumi.InputType['CreationDataArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 snapshot_type: Optional[pulumi.Input[Union[str, 'SnapshotType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A managed cluster snapshot resource.
        API Version: 2022-02-02-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CreationDataArgs']] creation_data: CreationData to be used to specify the source resource ID to create this snapshot.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the managed cluster resource.
        :param pulumi.Input[Union[str, 'SnapshotType']] snapshot_type: The type of a snapshot. The default is NodePool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedClusterSnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A managed cluster snapshot resource.
        API Version: 2022-02-02-preview.

        :param str resource_name: The name of the resource.
        :param ManagedClusterSnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedClusterSnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_data: Optional[pulumi.Input[pulumi.InputType['CreationDataArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 snapshot_type: Optional[pulumi.Input[Union[str, 'SnapshotType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedClusterSnapshotArgs.__new__(ManagedClusterSnapshotArgs)

            __props__.__dict__["creation_data"] = creation_data
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["snapshot_type"] = snapshot_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["managed_cluster_properties_read_only"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice/v20220202preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220302preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220402preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220502preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220602preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220702preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220802preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220803preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220902preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20221002preview:ManagedClusterSnapshot"), pulumi.Alias(type_="azure-native:containerservice/v20221102preview:ManagedClusterSnapshot")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedClusterSnapshot, __self__).__init__(
            'azure-native:containerservice:ManagedClusterSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedClusterSnapshot':
        """
        Get an existing ManagedClusterSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedClusterSnapshotArgs.__new__(ManagedClusterSnapshotArgs)

        __props__.__dict__["creation_data"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_cluster_properties_read_only"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["snapshot_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ManagedClusterSnapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output[Optional['outputs.CreationDataResponse']]:
        """
        CreationData to be used to specify the source resource ID to create this snapshot.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedClusterPropertiesReadOnly")
    def managed_cluster_properties_read_only(self) -> pulumi.Output['outputs.ManagedClusterPropertiesForSnapshotResponse']:
        """
        What the properties will be showed when getting managed cluster snapshot. Those properties are read-only.
        """
        return pulumi.get(self, "managed_cluster_properties_read_only")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of a snapshot. The default is NodePool.
        """
        return pulumi.get(self, "snapshot_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

