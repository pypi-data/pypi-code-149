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
    'GetOpenIdConnectProviderResult',
    'AwaitableGetOpenIdConnectProviderResult',
    'get_open_id_connect_provider',
    'get_open_id_connect_provider_output',
]

@pulumi.output_type
class GetOpenIdConnectProviderResult:
    """
    OpenId Connect Provider details.
    """
    def __init__(__self__, client_id=None, client_secret=None, description=None, display_name=None, id=None, metadata_endpoint=None, name=None, type=None, use_in_api_documentation=None, use_in_test_console=None):
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata_endpoint and not isinstance(metadata_endpoint, str):
            raise TypeError("Expected argument 'metadata_endpoint' to be a str")
        pulumi.set(__self__, "metadata_endpoint", metadata_endpoint)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if use_in_api_documentation and not isinstance(use_in_api_documentation, bool):
            raise TypeError("Expected argument 'use_in_api_documentation' to be a bool")
        pulumi.set(__self__, "use_in_api_documentation", use_in_api_documentation)
        if use_in_test_console and not isinstance(use_in_test_console, bool):
            raise TypeError("Expected argument 'use_in_test_console' to be a bool")
        pulumi.set(__self__, "use_in_test_console", use_in_test_console)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Client ID of developer console which is the client application.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[str]:
        """
        Client Secret of developer console which is the client application.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        User-friendly description of OpenID Connect Provider.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        User-friendly OpenID Connect Provider name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="metadataEndpoint")
    def metadata_endpoint(self) -> str:
        """
        Metadata endpoint URI.
        """
        return pulumi.get(self, "metadata_endpoint")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useInApiDocumentation")
    def use_in_api_documentation(self) -> Optional[bool]:
        """
        If true, the Open ID Connect provider will be used in the API documentation in the developer portal. False by default if no value is provided.
        """
        return pulumi.get(self, "use_in_api_documentation")

    @property
    @pulumi.getter(name="useInTestConsole")
    def use_in_test_console(self) -> Optional[bool]:
        """
        If true, the Open ID Connect provider may be used in the developer portal test console. True by default if no value is provided.
        """
        return pulumi.get(self, "use_in_test_console")


class AwaitableGetOpenIdConnectProviderResult(GetOpenIdConnectProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOpenIdConnectProviderResult(
            client_id=self.client_id,
            client_secret=self.client_secret,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            metadata_endpoint=self.metadata_endpoint,
            name=self.name,
            type=self.type,
            use_in_api_documentation=self.use_in_api_documentation,
            use_in_test_console=self.use_in_test_console)


def get_open_id_connect_provider(opid: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 service_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOpenIdConnectProviderResult:
    """
    OpenId Connect Provider details.


    :param str opid: Identifier of the OpenID Connect Provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['opid'] = opid
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220401preview:getOpenIdConnectProvider', __args__, opts=opts, typ=GetOpenIdConnectProviderResult).value

    return AwaitableGetOpenIdConnectProviderResult(
        client_id=__ret__.client_id,
        client_secret=__ret__.client_secret,
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        metadata_endpoint=__ret__.metadata_endpoint,
        name=__ret__.name,
        type=__ret__.type,
        use_in_api_documentation=__ret__.use_in_api_documentation,
        use_in_test_console=__ret__.use_in_test_console)


@_utilities.lift_output_func(get_open_id_connect_provider)
def get_open_id_connect_provider_output(opid: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        service_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOpenIdConnectProviderResult]:
    """
    OpenId Connect Provider details.


    :param str opid: Identifier of the OpenID Connect Provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
