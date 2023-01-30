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
    'GetDeploymentAtScopeResult',
    'AwaitableGetDeploymentAtScopeResult',
    'get_deployment_at_scope',
    'get_deployment_at_scope_output',
]

@pulumi.output_type
class GetDeploymentAtScopeResult:
    """
    Deployment information.
    """
    def __init__(__self__, id=None, location=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the deployment.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        the location of the deployment.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the deployment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.DeploymentPropertiesExtendedResponse':
        """
        Deployment properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the deployment.
        """
        return pulumi.get(self, "type")


class AwaitableGetDeploymentAtScopeResult(GetDeploymentAtScopeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentAtScopeResult(
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_deployment_at_scope(deployment_name: Optional[str] = None,
                            scope: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentAtScopeResult:
    """
    Deployment information.


    :param str deployment_name: The name of the deployment.
    :param str scope: The scope of a deployment.
    """
    __args__ = dict()
    __args__['deploymentName'] = deployment_name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:resources/v20190801:getDeploymentAtScope', __args__, opts=opts, typ=GetDeploymentAtScopeResult).value

    return AwaitableGetDeploymentAtScopeResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_deployment_at_scope)
def get_deployment_at_scope_output(deployment_name: Optional[pulumi.Input[str]] = None,
                                   scope: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentAtScopeResult]:
    """
    Deployment information.


    :param str deployment_name: The name of the deployment.
    :param str scope: The scope of a deployment.
    """
    ...
