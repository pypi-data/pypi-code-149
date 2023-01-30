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
    'GetDeploymentLogFileUrlResult',
    'AwaitableGetDeploymentLogFileUrlResult',
    'get_deployment_log_file_url',
    'get_deployment_log_file_url_output',
]

@pulumi.output_type
class GetDeploymentLogFileUrlResult:
    """
    Log file URL payload
    """
    def __init__(__self__, url=None):
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        URL of the log file
        """
        return pulumi.get(self, "url")


class AwaitableGetDeploymentLogFileUrlResult(GetDeploymentLogFileUrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentLogFileUrlResult(
            url=self.url)


def get_deployment_log_file_url(app_name: Optional[str] = None,
                                deployment_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                service_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentLogFileUrlResult:
    """
    Log file URL payload


    :param str app_name: The name of the App resource.
    :param str deployment_name: The name of the Deployment resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['appName'] = app_name
    __args__['deploymentName'] = deployment_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appplatform/v20221101preview:getDeploymentLogFileUrl', __args__, opts=opts, typ=GetDeploymentLogFileUrlResult).value

    return AwaitableGetDeploymentLogFileUrlResult(
        url=__ret__.url)


@_utilities.lift_output_func(get_deployment_log_file_url)
def get_deployment_log_file_url_output(app_name: Optional[pulumi.Input[str]] = None,
                                       deployment_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       service_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentLogFileUrlResult]:
    """
    Log file URL payload


    :param str app_name: The name of the App resource.
    :param str deployment_name: The name of the Deployment resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    ...
