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
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

warnings.warn("""Version 2017-01-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetApplicationResult:
    """
    Contains information about an application in a Batch account.
    """
    def __init__(__self__, allow_updates=None, default_version=None, display_name=None, id=None, packages=None):
        if allow_updates and not isinstance(allow_updates, bool):
            raise TypeError("Expected argument 'allow_updates' to be a bool")
        pulumi.set(__self__, "allow_updates", allow_updates)
        if default_version and not isinstance(default_version, str):
            raise TypeError("Expected argument 'default_version' to be a str")
        pulumi.set(__self__, "default_version", default_version)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if packages and not isinstance(packages, list):
            raise TypeError("Expected argument 'packages' to be a list")
        pulumi.set(__self__, "packages", packages)

    @property
    @pulumi.getter(name="allowUpdates")
    def allow_updates(self) -> Optional[bool]:
        """
        A value indicating whether packages within the application may be overwritten using the same version string.
        """
        return pulumi.get(self, "allow_updates")

    @property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[str]:
        """
        The package to use if a client requests the application but does not specify a version.
        """
        return pulumi.get(self, "default_version")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name for the application.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        A string that uniquely identifies the application within the account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def packages(self) -> Optional[Sequence['outputs.ApplicationPackageResponse']]:
        """
        The list of packages under this application.
        """
        return pulumi.get(self, "packages")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            allow_updates=self.allow_updates,
            default_version=self.default_version,
            display_name=self.display_name,
            id=self.id,
            packages=self.packages)


def get_application(account_name: Optional[str] = None,
                    application_id: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Contains information about an application in a Batch account.


    :param str account_name: The name of the Batch account.
    :param str application_id: The ID of the application.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    """
    pulumi.log.warn("""get_application is deprecated: Version 2017-01-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['applicationId'] = application_id
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:batch/v20170101:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        allow_updates=__ret__.allow_updates,
        default_version=__ret__.default_version,
        display_name=__ret__.display_name,
        id=__ret__.id,
        packages=__ret__.packages)


@_utilities.lift_output_func(get_application)
def get_application_output(account_name: Optional[pulumi.Input[str]] = None,
                           application_id: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    Contains information about an application in a Batch account.


    :param str account_name: The name of the Batch account.
    :param str application_id: The ID of the application.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    """
    pulumi.log.warn("""get_application is deprecated: Version 2017-01-01 will be removed in v2 of the provider.""")
    ...
