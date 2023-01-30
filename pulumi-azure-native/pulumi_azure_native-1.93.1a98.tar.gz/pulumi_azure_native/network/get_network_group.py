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

__all__ = [
    'GetNetworkGroupResult',
    'AwaitableGetNetworkGroupResult',
    'get_network_group',
    'get_network_group_output',
]

@pulumi.output_type
class GetNetworkGroupResult:
    """
    The network group resource
    """
    def __init__(__self__, conditional_membership=None, description=None, display_name=None, etag=None, group_members=None, id=None, member_type=None, name=None, provisioning_state=None, system_data=None, type=None):
        if conditional_membership and not isinstance(conditional_membership, str):
            raise TypeError("Expected argument 'conditional_membership' to be a str")
        pulumi.set(__self__, "conditional_membership", conditional_membership)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if group_members and not isinstance(group_members, list):
            raise TypeError("Expected argument 'group_members' to be a list")
        pulumi.set(__self__, "group_members", group_members)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_type and not isinstance(member_type, str):
            raise TypeError("Expected argument 'member_type' to be a str")
        pulumi.set(__self__, "member_type", member_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="conditionalMembership")
    def conditional_membership(self) -> Optional[str]:
        """
        Network group conditional filter.
        """
        return pulumi.get(self, "conditional_membership")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the network group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A friendly name for the network group.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="groupMembers")
    def group_members(self) -> Optional[Sequence['outputs.GroupMembersItemResponse']]:
        """
        Group members of network group.
        """
        return pulumi.get(self, "group_members")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> Optional[str]:
        """
        Group member type.
        """
        return pulumi.get(self, "member_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the scope assignment resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetNetworkGroupResult(GetNetworkGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkGroupResult(
            conditional_membership=self.conditional_membership,
            description=self.description,
            display_name=self.display_name,
            etag=self.etag,
            group_members=self.group_members,
            id=self.id,
            member_type=self.member_type,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_network_group(network_group_name: Optional[str] = None,
                      network_manager_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkGroupResult:
    """
    The network group resource
    API Version: 2021-02-01-preview.


    :param str network_group_name: The name of the network group to get.
    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['networkGroupName'] = network_group_name
    __args__['networkManagerName'] = network_manager_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getNetworkGroup', __args__, opts=opts, typ=GetNetworkGroupResult).value

    return AwaitableGetNetworkGroupResult(
        conditional_membership=__ret__.conditional_membership,
        description=__ret__.description,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        group_members=__ret__.group_members,
        id=__ret__.id,
        member_type=__ret__.member_type,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_network_group)
def get_network_group_output(network_group_name: Optional[pulumi.Input[str]] = None,
                             network_manager_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkGroupResult]:
    """
    The network group resource
    API Version: 2021-02-01-preview.


    :param str network_group_name: The name of the network group to get.
    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    """
    ...
