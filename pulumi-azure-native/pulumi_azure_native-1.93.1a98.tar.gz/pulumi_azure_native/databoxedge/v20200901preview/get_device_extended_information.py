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
    'GetDeviceExtendedInformationResult',
    'AwaitableGetDeviceExtendedInformationResult',
    'get_device_extended_information',
    'get_device_extended_information_output',
]

@pulumi.output_type
class GetDeviceExtendedInformationResult:
    """
    The extended Info of the Data Box Edge/Gateway device.
    """
    def __init__(__self__, channel_integrity_key_name=None, channel_integrity_key_version=None, client_secret_store_id=None, client_secret_store_url=None, encryption_key=None, encryption_key_thumbprint=None, id=None, name=None, resource_key=None, type=None):
        if channel_integrity_key_name and not isinstance(channel_integrity_key_name, str):
            raise TypeError("Expected argument 'channel_integrity_key_name' to be a str")
        pulumi.set(__self__, "channel_integrity_key_name", channel_integrity_key_name)
        if channel_integrity_key_version and not isinstance(channel_integrity_key_version, str):
            raise TypeError("Expected argument 'channel_integrity_key_version' to be a str")
        pulumi.set(__self__, "channel_integrity_key_version", channel_integrity_key_version)
        if client_secret_store_id and not isinstance(client_secret_store_id, str):
            raise TypeError("Expected argument 'client_secret_store_id' to be a str")
        pulumi.set(__self__, "client_secret_store_id", client_secret_store_id)
        if client_secret_store_url and not isinstance(client_secret_store_url, str):
            raise TypeError("Expected argument 'client_secret_store_url' to be a str")
        pulumi.set(__self__, "client_secret_store_url", client_secret_store_url)
        if encryption_key and not isinstance(encryption_key, str):
            raise TypeError("Expected argument 'encryption_key' to be a str")
        pulumi.set(__self__, "encryption_key", encryption_key)
        if encryption_key_thumbprint and not isinstance(encryption_key_thumbprint, str):
            raise TypeError("Expected argument 'encryption_key_thumbprint' to be a str")
        pulumi.set(__self__, "encryption_key_thumbprint", encryption_key_thumbprint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_key and not isinstance(resource_key, str):
            raise TypeError("Expected argument 'resource_key' to be a str")
        pulumi.set(__self__, "resource_key", resource_key)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="channelIntegrityKeyName")
    def channel_integrity_key_name(self) -> Optional[str]:
        """
        The name of Channel Integrity Key stored in the Client Key Vault
        """
        return pulumi.get(self, "channel_integrity_key_name")

    @property
    @pulumi.getter(name="channelIntegrityKeyVersion")
    def channel_integrity_key_version(self) -> Optional[str]:
        """
        The version of Channel Integrity Key stored in the Client Key Vault
        """
        return pulumi.get(self, "channel_integrity_key_version")

    @property
    @pulumi.getter(name="clientSecretStoreId")
    def client_secret_store_id(self) -> Optional[str]:
        """
        The Key Vault ARM Id for client secrets
        """
        return pulumi.get(self, "client_secret_store_id")

    @property
    @pulumi.getter(name="clientSecretStoreUrl")
    def client_secret_store_url(self) -> Optional[str]:
        """
        The url to access the Client Key Vault
        """
        return pulumi.get(self, "client_secret_store_url")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[str]:
        """
        The public part of the encryption certificate. Client uses this to encrypt any secret.
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter(name="encryptionKeyThumbprint")
    def encryption_key_thumbprint(self) -> Optional[str]:
        """
        The digital signature of encrypted certificate.
        """
        return pulumi.get(self, "encryption_key_thumbprint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceKey")
    def resource_key(self) -> str:
        """
        The Resource ID of the Resource.
        """
        return pulumi.get(self, "resource_key")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetDeviceExtendedInformationResult(GetDeviceExtendedInformationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceExtendedInformationResult(
            channel_integrity_key_name=self.channel_integrity_key_name,
            channel_integrity_key_version=self.channel_integrity_key_version,
            client_secret_store_id=self.client_secret_store_id,
            client_secret_store_url=self.client_secret_store_url,
            encryption_key=self.encryption_key,
            encryption_key_thumbprint=self.encryption_key_thumbprint,
            id=self.id,
            name=self.name,
            resource_key=self.resource_key,
            type=self.type)


def get_device_extended_information(device_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceExtendedInformationResult:
    """
    The extended Info of the Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20200901preview:getDeviceExtendedInformation', __args__, opts=opts, typ=GetDeviceExtendedInformationResult).value

    return AwaitableGetDeviceExtendedInformationResult(
        channel_integrity_key_name=__ret__.channel_integrity_key_name,
        channel_integrity_key_version=__ret__.channel_integrity_key_version,
        client_secret_store_id=__ret__.client_secret_store_id,
        client_secret_store_url=__ret__.client_secret_store_url,
        encryption_key=__ret__.encryption_key,
        encryption_key_thumbprint=__ret__.encryption_key_thumbprint,
        id=__ret__.id,
        name=__ret__.name,
        resource_key=__ret__.resource_key,
        type=__ret__.type)


@_utilities.lift_output_func(get_device_extended_information)
def get_device_extended_information_output(device_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceExtendedInformationResult]:
    """
    The extended Info of the Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    """
    ...
