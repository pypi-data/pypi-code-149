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
    'GetCodelessApiPollingDataConnectorResult',
    'AwaitableGetCodelessApiPollingDataConnectorResult',
    'get_codeless_api_polling_data_connector',
    'get_codeless_api_polling_data_connector_output',
]

@pulumi.output_type
class GetCodelessApiPollingDataConnectorResult:
    """
    Represents Codeless API Polling data connector.
    """
    def __init__(__self__, connector_ui_config=None, etag=None, id=None, kind=None, name=None, polling_config=None, system_data=None, type=None):
        if connector_ui_config and not isinstance(connector_ui_config, dict):
            raise TypeError("Expected argument 'connector_ui_config' to be a dict")
        pulumi.set(__self__, "connector_ui_config", connector_ui_config)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if polling_config and not isinstance(polling_config, dict):
            raise TypeError("Expected argument 'polling_config' to be a dict")
        pulumi.set(__self__, "polling_config", polling_config)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> Optional['outputs.CodelessUiConnectorConfigPropertiesResponse']:
        """
        Config to describe the instructions blade
        """
        return pulumi.get(self, "connector_ui_config")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the data connector
        Expected value is 'APIPolling'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pollingConfig")
    def polling_config(self) -> Optional['outputs.CodelessConnectorPollingConfigPropertiesResponse']:
        """
        Config to describe the polling instructions
        """
        return pulumi.get(self, "polling_config")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetCodelessApiPollingDataConnectorResult(GetCodelessApiPollingDataConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCodelessApiPollingDataConnectorResult(
            connector_ui_config=self.connector_ui_config,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            name=self.name,
            polling_config=self.polling_config,
            system_data=self.system_data,
            type=self.type)


def get_codeless_api_polling_data_connector(data_connector_id: Optional[str] = None,
                                            resource_group_name: Optional[str] = None,
                                            workspace_name: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCodelessApiPollingDataConnectorResult:
    """
    Represents Codeless API Polling data connector.


    :param str data_connector_id: Connector ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['dataConnectorId'] = data_connector_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20220601preview:getCodelessApiPollingDataConnector', __args__, opts=opts, typ=GetCodelessApiPollingDataConnectorResult).value

    return AwaitableGetCodelessApiPollingDataConnectorResult(
        connector_ui_config=__ret__.connector_ui_config,
        etag=__ret__.etag,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        polling_config=__ret__.polling_config,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_codeless_api_polling_data_connector)
def get_codeless_api_polling_data_connector_output(data_connector_id: Optional[pulumi.Input[str]] = None,
                                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                                   workspace_name: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCodelessApiPollingDataConnectorResult]:
    """
    Represents Codeless API Polling data connector.


    :param str data_connector_id: Connector ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
