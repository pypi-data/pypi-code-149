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
    'GetSimGroupResult',
    'AwaitableGetSimGroupResult',
    'get_sim_group',
    'get_sim_group_output',
]

@pulumi.output_type
class GetSimGroupResult:
    """
    SIM group resource.
    """
    def __init__(__self__, encryption_key=None, id=None, identity=None, location=None, mobile_network=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if encryption_key and not isinstance(encryption_key, dict):
            raise TypeError("Expected argument 'encryption_key' to be a dict")
        pulumi.set(__self__, "encryption_key", encryption_key)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mobile_network and not isinstance(mobile_network, dict):
            raise TypeError("Expected argument 'mobile_network' to be a dict")
        pulumi.set(__self__, "mobile_network", mobile_network)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional['outputs.KeyVaultKeyResponse']:
        """
        A key to encrypt the SIM data that belongs to this SIM group.
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        The identity used to retrieve the encryption key from Azure key vault.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileNetwork")
    def mobile_network(self) -> Optional['outputs.MobileNetworkResourceIdResponse']:
        """
        Mobile network that this SIM group belongs to. The mobile network must be in the same location as the SIM group.
        """
        return pulumi.get(self, "mobile_network")

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
        The provisioning state of the SIM group resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSimGroupResult(GetSimGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSimGroupResult(
            encryption_key=self.encryption_key,
            id=self.id,
            identity=self.identity,
            location=self.location,
            mobile_network=self.mobile_network,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_sim_group(resource_group_name: Optional[str] = None,
                  sim_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSimGroupResult:
    """
    SIM group resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sim_group_name: The name of the SIM Group.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['simGroupName'] = sim_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilenetwork/v20221101:getSimGroup', __args__, opts=opts, typ=GetSimGroupResult).value

    return AwaitableGetSimGroupResult(
        encryption_key=__ret__.encryption_key,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        mobile_network=__ret__.mobile_network,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_sim_group)
def get_sim_group_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                         sim_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSimGroupResult]:
    """
    SIM group resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sim_group_name: The name of the SIM Group.
    """
    ...
