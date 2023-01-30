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
    'GetScriptResult',
    'AwaitableGetScriptResult',
    'get_script',
    'get_script_output',
]

@pulumi.output_type
class GetScriptResult:
    """
    Class representing a database script.
    """
    def __init__(__self__, continue_on_errors=None, force_update_tag=None, id=None, name=None, provisioning_state=None, script_url=None, system_data=None, type=None):
        if continue_on_errors and not isinstance(continue_on_errors, bool):
            raise TypeError("Expected argument 'continue_on_errors' to be a bool")
        pulumi.set(__self__, "continue_on_errors", continue_on_errors)
        if force_update_tag and not isinstance(force_update_tag, str):
            raise TypeError("Expected argument 'force_update_tag' to be a str")
        pulumi.set(__self__, "force_update_tag", force_update_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if script_url and not isinstance(script_url, str):
            raise TypeError("Expected argument 'script_url' to be a str")
        pulumi.set(__self__, "script_url", script_url)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="continueOnErrors")
    def continue_on_errors(self) -> Optional[bool]:
        """
        Flag that indicates whether to continue if one of the command fails.
        """
        return pulumi.get(self, "continue_on_errors")

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[str]:
        """
        A unique string. If changed the script will be applied again.
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scriptUrl")
    def script_url(self) -> str:
        """
        The url to the KQL script blob file.
        """
        return pulumi.get(self, "script_url")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetScriptResult(GetScriptResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScriptResult(
            continue_on_errors=self.continue_on_errors,
            force_update_tag=self.force_update_tag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            script_url=self.script_url,
            system_data=self.system_data,
            type=self.type)


def get_script(cluster_name: Optional[str] = None,
               database_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               script_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScriptResult:
    """
    Class representing a database script.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    :param str script_name: The name of the Kusto database script.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['scriptName'] = script_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20210827:getScript', __args__, opts=opts, typ=GetScriptResult).value

    return AwaitableGetScriptResult(
        continue_on_errors=__ret__.continue_on_errors,
        force_update_tag=__ret__.force_update_tag,
        id=__ret__.id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        script_url=__ret__.script_url,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_script)
def get_script_output(cluster_name: Optional[pulumi.Input[str]] = None,
                      database_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      script_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScriptResult]:
    """
    Class representing a database script.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    :param str script_name: The name of the Kusto database script.
    """
    ...
