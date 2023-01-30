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
    'GetAvailabilitySetResult',
    'AwaitableGetAvailabilitySetResult',
    'get_availability_set',
    'get_availability_set_output',
]

@pulumi.output_type
class GetAvailabilitySetResult:
    """
    Specifies information about the availability set that the virtual machine should be assigned to. Virtual machines specified in the same availability set are allocated to different nodes to maximize availability. For more information about availability sets, see [Availability sets overview](https://docs.microsoft.com/azure/virtual-machines/availability-set-overview). <br><br> For more information on Azure planned maintenance, see [Maintenance and updates for Virtual Machines in Azure](https://docs.microsoft.com/azure/virtual-machines/maintenance-and-updates) <br><br> Currently, a VM can only be added to availability set at creation time. An existing VM cannot be added to an availability set.
    """
    def __init__(__self__, id=None, location=None, name=None, platform_fault_domain_count=None, platform_update_domain_count=None, proximity_placement_group=None, sku=None, statuses=None, tags=None, type=None, virtual_machines=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform_fault_domain_count and not isinstance(platform_fault_domain_count, int):
            raise TypeError("Expected argument 'platform_fault_domain_count' to be a int")
        pulumi.set(__self__, "platform_fault_domain_count", platform_fault_domain_count)
        if platform_update_domain_count and not isinstance(platform_update_domain_count, int):
            raise TypeError("Expected argument 'platform_update_domain_count' to be a int")
        pulumi.set(__self__, "platform_update_domain_count", platform_update_domain_count)
        if proximity_placement_group and not isinstance(proximity_placement_group, dict):
            raise TypeError("Expected argument 'proximity_placement_group' to be a dict")
        pulumi.set(__self__, "proximity_placement_group", proximity_placement_group)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        pulumi.set(__self__, "statuses", statuses)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machines and not isinstance(virtual_machines, list):
            raise TypeError("Expected argument 'virtual_machines' to be a list")
        pulumi.set(__self__, "virtual_machines", virtual_machines)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> Optional[int]:
        """
        Fault Domain count.
        """
        return pulumi.get(self, "platform_fault_domain_count")

    @property
    @pulumi.getter(name="platformUpdateDomainCount")
    def platform_update_domain_count(self) -> Optional[int]:
        """
        Update Domain count.
        """
        return pulumi.get(self, "platform_update_domain_count")

    @property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional['outputs.SubResourceResponse']:
        """
        Specifies information about the proximity placement group that the availability set should be assigned to. <br><br>Minimum api-version: 2018-04-01.
        """
        return pulumi.get(self, "proximity_placement_group")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        Sku of the availability set, only name is required to be set. See AvailabilitySetSkuTypes for possible set of values. Use 'Aligned' for virtual machines with managed disks and 'Classic' for virtual machines with unmanaged disks. Default value is 'Classic'.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def statuses(self) -> Sequence['outputs.InstanceViewStatusResponse']:
        """
        The resource status information.
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(self) -> Optional[Sequence['outputs.SubResourceResponse']]:
        """
        A list of references to all virtual machines in the availability set.
        """
        return pulumi.get(self, "virtual_machines")


class AwaitableGetAvailabilitySetResult(GetAvailabilitySetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailabilitySetResult(
            id=self.id,
            location=self.location,
            name=self.name,
            platform_fault_domain_count=self.platform_fault_domain_count,
            platform_update_domain_count=self.platform_update_domain_count,
            proximity_placement_group=self.proximity_placement_group,
            sku=self.sku,
            statuses=self.statuses,
            tags=self.tags,
            type=self.type,
            virtual_machines=self.virtual_machines)


def get_availability_set(availability_set_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAvailabilitySetResult:
    """
    Specifies information about the availability set that the virtual machine should be assigned to. Virtual machines specified in the same availability set are allocated to different nodes to maximize availability. For more information about availability sets, see [Availability sets overview](https://docs.microsoft.com/azure/virtual-machines/availability-set-overview). <br><br> For more information on Azure planned maintenance, see [Maintenance and updates for Virtual Machines in Azure](https://docs.microsoft.com/azure/virtual-machines/maintenance-and-updates) <br><br> Currently, a VM can only be added to availability set at creation time. An existing VM cannot be added to an availability set.


    :param str availability_set_name: The name of the availability set.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['availabilitySetName'] = availability_set_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20211101:getAvailabilitySet', __args__, opts=opts, typ=GetAvailabilitySetResult).value

    return AwaitableGetAvailabilitySetResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        platform_fault_domain_count=__ret__.platform_fault_domain_count,
        platform_update_domain_count=__ret__.platform_update_domain_count,
        proximity_placement_group=__ret__.proximity_placement_group,
        sku=__ret__.sku,
        statuses=__ret__.statuses,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_machines=__ret__.virtual_machines)


@_utilities.lift_output_func(get_availability_set)
def get_availability_set_output(availability_set_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAvailabilitySetResult]:
    """
    Specifies information about the availability set that the virtual machine should be assigned to. Virtual machines specified in the same availability set are allocated to different nodes to maximize availability. For more information about availability sets, see [Availability sets overview](https://docs.microsoft.com/azure/virtual-machines/availability-set-overview). <br><br> For more information on Azure planned maintenance, see [Maintenance and updates for Virtual Machines in Azure](https://docs.microsoft.com/azure/virtual-machines/maintenance-and-updates) <br><br> Currently, a VM can only be added to availability set at creation time. An existing VM cannot be added to an availability set.


    :param str availability_set_name: The name of the availability set.
    :param str resource_group_name: The name of the resource group.
    """
    ...
