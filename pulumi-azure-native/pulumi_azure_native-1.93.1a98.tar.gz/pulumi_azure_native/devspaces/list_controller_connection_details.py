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
    'ListControllerConnectionDetailsResult',
    'AwaitableListControllerConnectionDetailsResult',
    'list_controller_connection_details',
    'list_controller_connection_details_output',
]

@pulumi.output_type
class ListControllerConnectionDetailsResult:
    def __init__(__self__, connection_details_list=None):
        if connection_details_list and not isinstance(connection_details_list, list):
            raise TypeError("Expected argument 'connection_details_list' to be a list")
        pulumi.set(__self__, "connection_details_list", connection_details_list)

    @property
    @pulumi.getter(name="connectionDetailsList")
    def connection_details_list(self) -> Optional[Sequence['outputs.ControllerConnectionDetailsResponse']]:
        """
        List of Azure Dev Spaces Controller connection details.
        """
        return pulumi.get(self, "connection_details_list")


class AwaitableListControllerConnectionDetailsResult(ListControllerConnectionDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListControllerConnectionDetailsResult(
            connection_details_list=self.connection_details_list)


def list_controller_connection_details(name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       target_container_host_resource_id: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListControllerConnectionDetailsResult:
    """
    API Version: 2019-04-01.


    :param str name: Name of the resource.
    :param str resource_group_name: Resource group to which the resource belongs.
    :param str target_container_host_resource_id: Resource ID of the target container host mapped to the Azure Dev Spaces Controller.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['targetContainerHostResourceId'] = target_container_host_resource_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devspaces:listControllerConnectionDetails', __args__, opts=opts, typ=ListControllerConnectionDetailsResult).value

    return AwaitableListControllerConnectionDetailsResult(
        connection_details_list=__ret__.connection_details_list)


@_utilities.lift_output_func(list_controller_connection_details)
def list_controller_connection_details_output(name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              target_container_host_resource_id: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListControllerConnectionDetailsResult]:
    """
    API Version: 2019-04-01.


    :param str name: Name of the resource.
    :param str resource_group_name: Resource group to which the resource belongs.
    :param str target_container_host_resource_id: Resource ID of the target container host mapped to the Azure Dev Spaces Controller.
    """
    ...
