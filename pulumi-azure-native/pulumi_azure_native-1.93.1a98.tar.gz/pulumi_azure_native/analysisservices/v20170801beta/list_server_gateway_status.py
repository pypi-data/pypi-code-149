# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListServerGatewayStatusResult',
    'AwaitableListServerGatewayStatusResult',
    'list_server_gateway_status',
    'list_server_gateway_status_output',
]

@pulumi.output_type
class ListServerGatewayStatusResult:
    """
    Status of gateway is live.
    """
    def __init__(__self__, status=None):
        if status and not isinstance(status, int):
            raise TypeError("Expected argument 'status' to be a int")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> Optional[int]:
        """
        Live message of list gateway. Status: 0 - Live
        """
        return pulumi.get(self, "status")


class AwaitableListServerGatewayStatusResult(ListServerGatewayStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListServerGatewayStatusResult(
            status=self.status)


def list_server_gateway_status(resource_group_name: Optional[str] = None,
                               server_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListServerGatewayStatusResult:
    """
    Status of gateway is live.


    :param str resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :param str server_name: The name of the Analysis Services server.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:analysisservices/v20170801beta:listServerGatewayStatus', __args__, opts=opts, typ=ListServerGatewayStatusResult).value

    return AwaitableListServerGatewayStatusResult(
        status=__ret__.status)


@_utilities.lift_output_func(list_server_gateway_status)
def list_server_gateway_status_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                      server_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListServerGatewayStatusResult]:
    """
    Status of gateway is live.


    :param str resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :param str server_name: The name of the Analysis Services server.
    """
    ...
