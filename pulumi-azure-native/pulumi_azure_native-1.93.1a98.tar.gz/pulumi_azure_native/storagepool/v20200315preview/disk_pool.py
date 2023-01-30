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
from ._enums import *
from ._inputs import *

__all__ = ['DiskPoolArgs', 'DiskPool']

@pulumi.input_type
class DiskPoolArgs:
    def __init__(__self__, *,
                 availability_zones: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resource_group_name: pulumi.Input[str],
                 subnet_id: pulumi.Input[str],
                 tier: pulumi.Input[Union[str, 'DiskPoolTier']],
                 additional_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DiskPool resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: Logical zone for Disk pool resource; example: ["1"].
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] subnet_id: Azure Resource ID of a Subnet for the Disk pool.
        :param pulumi.Input[Union[str, 'DiskPoolTier']] tier: Determines the SKU of VM deployed for Disk pool
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_capabilities: List of additional capabilities for a Disk pool.
        :param pulumi.Input[str] disk_pool_name: The name of the Disk pool.
        :param pulumi.Input[Sequence[pulumi.Input['DiskArgs']]] disks: List of Azure Managed Disks to attach to a Disk pool. Can attach 8 disks at most.
        :param pulumi.Input[str] location: The geo-location where the resource lives.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "availability_zones", availability_zones)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "tier", tier)
        if additional_capabilities is not None:
            pulumi.set(__self__, "additional_capabilities", additional_capabilities)
        if disk_pool_name is not None:
            pulumi.set(__self__, "disk_pool_name", disk_pool_name)
        if disks is not None:
            pulumi.set(__self__, "disks", disks)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Logical zone for Disk pool resource; example: ["1"].
        """
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "availability_zones", value)

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
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        Azure Resource ID of a Subnet for the Disk pool.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[str, 'DiskPoolTier']]:
        """
        Determines the SKU of VM deployed for Disk pool
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input[Union[str, 'DiskPoolTier']]):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of additional capabilities for a Disk pool.
        """
        return pulumi.get(self, "additional_capabilities")

    @additional_capabilities.setter
    def additional_capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "additional_capabilities", value)

    @property
    @pulumi.getter(name="diskPoolName")
    def disk_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Disk pool.
        """
        return pulumi.get(self, "disk_pool_name")

    @disk_pool_name.setter
    def disk_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_pool_name", value)

    @property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]:
        """
        List of Azure Managed Disks to attach to a Disk pool. Can attach 8 disks at most.
        """
        return pulumi.get(self, "disks")

    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]):
        pulumi.set(self, "disks", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DiskPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[Union[str, 'DiskPoolTier']]] = None,
                 __props__=None):
        """
        Response for Disk pool request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_capabilities: List of additional capabilities for a Disk pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: Logical zone for Disk pool resource; example: ["1"].
        :param pulumi.Input[str] disk_pool_name: The name of the Disk pool.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]] disks: List of Azure Managed Disks to attach to a Disk pool. Can attach 8 disks at most.
        :param pulumi.Input[str] location: The geo-location where the resource lives.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] subnet_id: Azure Resource ID of a Subnet for the Disk pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'DiskPoolTier']] tier: Determines the SKU of VM deployed for Disk pool
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DiskPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response for Disk pool request.

        :param str resource_name: The name of the resource.
        :param DiskPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiskPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[Union[str, 'DiskPoolTier']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DiskPoolArgs.__new__(DiskPoolArgs)

            __props__.__dict__["additional_capabilities"] = additional_capabilities
            if availability_zones is None and not opts.urn:
                raise TypeError("Missing required property 'availability_zones'")
            __props__.__dict__["availability_zones"] = availability_zones
            __props__.__dict__["disk_pool_name"] = disk_pool_name
            __props__.__dict__["disks"] = disks
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            if tier is None and not opts.urn:
                raise TypeError("Missing required property 'tier'")
            __props__.__dict__["tier"] = tier
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storagepool:DiskPool"), pulumi.Alias(type_="azure-native:storagepool/v20210401preview:DiskPool"), pulumi.Alias(type_="azure-native:storagepool/v20210801:DiskPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DiskPool, __self__).__init__(
            'azure-native:storagepool/v20200315preview:DiskPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DiskPool':
        """
        Get an existing DiskPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DiskPoolArgs.__new__(DiskPoolArgs)

        __props__.__dict__["additional_capabilities"] = None
        __props__.__dict__["availability_zones"] = None
        __props__.__dict__["disks"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tier"] = None
        __props__.__dict__["type"] = None
        return DiskPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of additional capabilities for Disk pool.
        """
        return pulumi.get(self, "additional_capabilities")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[str]]:
        """
        Logical zone for Disk pool resource; example: ["1"].
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter
    def disks(self) -> pulumi.Output[Optional[Sequence['outputs.DiskResponse']]]:
        """
        List of Azure Managed Disks to attach to a Disk pool. Can attach 8 disks at most.
        """
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Operational status of the Disk pool.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        Azure Resource ID of a Subnet for the Disk pool.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemMetadataResponse']:
        """
        Resource metadata required by ARM RPC
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[str]:
        """
        Determines the SKU of VM deployed for Disk pool
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

