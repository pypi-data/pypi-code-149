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
    'GetJobCredentialResult',
    'AwaitableGetJobCredentialResult',
    'get_job_credential',
    'get_job_credential_output',
]

@pulumi.output_type
class GetJobCredentialResult:
    """
    A stored credential that can be used by a job to connect to target databases.
    """
    def __init__(__self__, id=None, name=None, type=None, username=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The credential user name.
        """
        return pulumi.get(self, "username")


class AwaitableGetJobCredentialResult(GetJobCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobCredentialResult(
            id=self.id,
            name=self.name,
            type=self.type,
            username=self.username)


def get_job_credential(credential_name: Optional[str] = None,
                       job_agent_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       server_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobCredentialResult:
    """
    A stored credential that can be used by a job to connect to target databases.


    :param str credential_name: The name of the credential.
    :param str job_agent_name: The name of the job agent.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['credentialName'] = credential_name
    __args__['jobAgentName'] = job_agent_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20210201preview:getJobCredential', __args__, opts=opts, typ=GetJobCredentialResult).value

    return AwaitableGetJobCredentialResult(
        id=__ret__.id,
        name=__ret__.name,
        type=__ret__.type,
        username=__ret__.username)


@_utilities.lift_output_func(get_job_credential)
def get_job_credential_output(credential_name: Optional[pulumi.Input[str]] = None,
                              job_agent_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              server_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobCredentialResult]:
    """
    A stored credential that can be used by a job to connect to target databases.


    :param str credential_name: The name of the credential.
    :param str job_agent_name: The name of the job agent.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
