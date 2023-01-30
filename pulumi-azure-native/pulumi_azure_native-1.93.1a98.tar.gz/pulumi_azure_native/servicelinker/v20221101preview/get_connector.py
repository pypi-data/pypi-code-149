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
    'GetConnectorResult',
    'AwaitableGetConnectorResult',
    'get_connector',
    'get_connector_output',
]

@pulumi.output_type
class GetConnectorResult:
    """
    Linker of source and target resource
    """
    def __init__(__self__, auth_info=None, client_type=None, configuration_info=None, id=None, name=None, provisioning_state=None, public_network_solution=None, scope=None, secret_store=None, system_data=None, target_service=None, type=None, v_net_solution=None):
        if auth_info and not isinstance(auth_info, dict):
            raise TypeError("Expected argument 'auth_info' to be a dict")
        pulumi.set(__self__, "auth_info", auth_info)
        if client_type and not isinstance(client_type, str):
            raise TypeError("Expected argument 'client_type' to be a str")
        pulumi.set(__self__, "client_type", client_type)
        if configuration_info and not isinstance(configuration_info, dict):
            raise TypeError("Expected argument 'configuration_info' to be a dict")
        pulumi.set(__self__, "configuration_info", configuration_info)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_solution and not isinstance(public_network_solution, dict):
            raise TypeError("Expected argument 'public_network_solution' to be a dict")
        pulumi.set(__self__, "public_network_solution", public_network_solution)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if secret_store and not isinstance(secret_store, dict):
            raise TypeError("Expected argument 'secret_store' to be a dict")
        pulumi.set(__self__, "secret_store", secret_store)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if target_service and not isinstance(target_service, dict):
            raise TypeError("Expected argument 'target_service' to be a dict")
        pulumi.set(__self__, "target_service", target_service)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if v_net_solution and not isinstance(v_net_solution, dict):
            raise TypeError("Expected argument 'v_net_solution' to be a dict")
        pulumi.set(__self__, "v_net_solution", v_net_solution)

    @property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> Optional[Any]:
        """
        The authentication type.
        """
        return pulumi.get(self, "auth_info")

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[str]:
        """
        The application client type
        """
        return pulumi.get(self, "client_type")

    @property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> Optional['outputs.ConfigurationInfoResponse']:
        """
        The connection information consumed by applications, including secrets, connection strings.
        """
        return pulumi.get(self, "configuration_info")

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
        The provisioning state. 
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkSolution")
    def public_network_solution(self) -> Optional['outputs.PublicNetworkSolutionResponse']:
        """
        The network solution.
        """
        return pulumi.get(self, "public_network_solution")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        connection scope in source service.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional['outputs.SecretStoreResponse']:
        """
        An option to store secret value in secure place
        """
        return pulumi.get(self, "secret_store")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetService")
    def target_service(self) -> Optional[Any]:
        """
        The target service properties
        """
        return pulumi.get(self, "target_service")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(self) -> Optional['outputs.VNetSolutionResponse']:
        """
        The VNet solution.
        """
        return pulumi.get(self, "v_net_solution")


class AwaitableGetConnectorResult(GetConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectorResult(
            auth_info=self.auth_info,
            client_type=self.client_type,
            configuration_info=self.configuration_info,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            public_network_solution=self.public_network_solution,
            scope=self.scope,
            secret_store=self.secret_store,
            system_data=self.system_data,
            target_service=self.target_service,
            type=self.type,
            v_net_solution=self.v_net_solution)


def get_connector(connector_name: Optional[str] = None,
                  location: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  subscription_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectorResult:
    """
    Linker of source and target resource


    :param str connector_name: The name of resource.
    :param str location: The name of Azure region.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str subscription_id: The ID of the target subscription.
    """
    __args__ = dict()
    __args__['connectorName'] = connector_name
    __args__['location'] = location
    __args__['resourceGroupName'] = resource_group_name
    __args__['subscriptionId'] = subscription_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicelinker/v20221101preview:getConnector', __args__, opts=opts, typ=GetConnectorResult).value

    return AwaitableGetConnectorResult(
        auth_info=__ret__.auth_info,
        client_type=__ret__.client_type,
        configuration_info=__ret__.configuration_info,
        id=__ret__.id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        public_network_solution=__ret__.public_network_solution,
        scope=__ret__.scope,
        secret_store=__ret__.secret_store,
        system_data=__ret__.system_data,
        target_service=__ret__.target_service,
        type=__ret__.type,
        v_net_solution=__ret__.v_net_solution)


@_utilities.lift_output_func(get_connector)
def get_connector_output(connector_name: Optional[pulumi.Input[str]] = None,
                         location: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         subscription_id: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectorResult]:
    """
    Linker of source and target resource


    :param str connector_name: The name of resource.
    :param str location: The name of Azure region.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str subscription_id: The ID of the target subscription.
    """
    ...
