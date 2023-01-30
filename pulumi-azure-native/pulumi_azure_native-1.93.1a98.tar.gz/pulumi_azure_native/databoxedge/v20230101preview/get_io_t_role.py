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
    'GetIoTRoleResult',
    'AwaitableGetIoTRoleResult',
    'get_io_t_role',
    'get_io_t_role_output',
]

@pulumi.output_type
class GetIoTRoleResult:
    """
    Compute role.
    """
    def __init__(__self__, compute_resource=None, host_platform=None, host_platform_type=None, id=None, io_t_device_details=None, io_t_edge_agent_info=None, io_t_edge_device_details=None, kind=None, name=None, role_status=None, share_mappings=None, system_data=None, type=None):
        if compute_resource and not isinstance(compute_resource, dict):
            raise TypeError("Expected argument 'compute_resource' to be a dict")
        pulumi.set(__self__, "compute_resource", compute_resource)
        if host_platform and not isinstance(host_platform, str):
            raise TypeError("Expected argument 'host_platform' to be a str")
        pulumi.set(__self__, "host_platform", host_platform)
        if host_platform_type and not isinstance(host_platform_type, str):
            raise TypeError("Expected argument 'host_platform_type' to be a str")
        pulumi.set(__self__, "host_platform_type", host_platform_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if io_t_device_details and not isinstance(io_t_device_details, dict):
            raise TypeError("Expected argument 'io_t_device_details' to be a dict")
        pulumi.set(__self__, "io_t_device_details", io_t_device_details)
        if io_t_edge_agent_info and not isinstance(io_t_edge_agent_info, dict):
            raise TypeError("Expected argument 'io_t_edge_agent_info' to be a dict")
        pulumi.set(__self__, "io_t_edge_agent_info", io_t_edge_agent_info)
        if io_t_edge_device_details and not isinstance(io_t_edge_device_details, dict):
            raise TypeError("Expected argument 'io_t_edge_device_details' to be a dict")
        pulumi.set(__self__, "io_t_edge_device_details", io_t_edge_device_details)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_status and not isinstance(role_status, str):
            raise TypeError("Expected argument 'role_status' to be a str")
        pulumi.set(__self__, "role_status", role_status)
        if share_mappings and not isinstance(share_mappings, list):
            raise TypeError("Expected argument 'share_mappings' to be a list")
        pulumi.set(__self__, "share_mappings", share_mappings)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="computeResource")
    def compute_resource(self) -> Optional['outputs.ComputeResourceResponse']:
        """
        Resource allocation
        """
        return pulumi.get(self, "compute_resource")

    @property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> str:
        """
        Host OS supported by the IoT role.
        """
        return pulumi.get(self, "host_platform")

    @property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> str:
        """
        Platform where the Iot runtime is hosted.
        """
        return pulumi.get(self, "host_platform_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> 'outputs.IoTDeviceInfoResponse':
        """
        IoT device metadata to which data box edge device needs to be connected.
        """
        return pulumi.get(self, "io_t_device_details")

    @property
    @pulumi.getter(name="ioTEdgeAgentInfo")
    def io_t_edge_agent_info(self) -> Optional['outputs.IoTEdgeAgentInfoResponse']:
        """
        Iot edge agent details to download the agent and bootstrap iot runtime.
        """
        return pulumi.get(self, "io_t_edge_agent_info")

    @property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> 'outputs.IoTDeviceInfoResponse':
        """
        IoT edge device to which the IoT role needs to be configured.
        """
        return pulumi.get(self, "io_t_edge_device_details")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Role type.
        Expected value is 'IOT'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> str:
        """
        Role status.
        """
        return pulumi.get(self, "role_status")

    @property
    @pulumi.getter(name="shareMappings")
    def share_mappings(self) -> Optional[Sequence['outputs.MountPointMapResponse']]:
        """
        Mount points of shares in role(s).
        """
        return pulumi.get(self, "share_mappings")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of Role
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetIoTRoleResult(GetIoTRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIoTRoleResult(
            compute_resource=self.compute_resource,
            host_platform=self.host_platform,
            host_platform_type=self.host_platform_type,
            id=self.id,
            io_t_device_details=self.io_t_device_details,
            io_t_edge_agent_info=self.io_t_edge_agent_info,
            io_t_edge_device_details=self.io_t_edge_device_details,
            kind=self.kind,
            name=self.name,
            role_status=self.role_status,
            share_mappings=self.share_mappings,
            system_data=self.system_data,
            type=self.type)


def get_io_t_role(device_name: Optional[str] = None,
                  name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIoTRoleResult:
    """
    Compute role.


    :param str device_name: The device name.
    :param str name: The role name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20230101preview:getIoTRole', __args__, opts=opts, typ=GetIoTRoleResult).value

    return AwaitableGetIoTRoleResult(
        compute_resource=__ret__.compute_resource,
        host_platform=__ret__.host_platform,
        host_platform_type=__ret__.host_platform_type,
        id=__ret__.id,
        io_t_device_details=__ret__.io_t_device_details,
        io_t_edge_agent_info=__ret__.io_t_edge_agent_info,
        io_t_edge_device_details=__ret__.io_t_edge_device_details,
        kind=__ret__.kind,
        name=__ret__.name,
        role_status=__ret__.role_status,
        share_mappings=__ret__.share_mappings,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_io_t_role)
def get_io_t_role_output(device_name: Optional[pulumi.Input[str]] = None,
                         name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIoTRoleResult]:
    """
    Compute role.


    :param str device_name: The device name.
    :param str name: The role name.
    :param str resource_group_name: The resource group name.
    """
    ...
