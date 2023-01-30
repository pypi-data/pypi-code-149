# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetStorageAccountCredentialResult',
    'AwaitableGetStorageAccountCredentialResult',
    'get_storage_account_credential',
    'get_storage_account_credential_output',
]

@pulumi.output_type
class GetStorageAccountCredentialResult:
    """
    The storage account credential.
    """
    def __init__(__self__, access_key=None, end_point=None, id=None, kind=None, name=None, ssl_status=None, type=None, volumes_count=None):
        if access_key and not isinstance(access_key, dict):
            raise TypeError("Expected argument 'access_key' to be a dict")
        pulumi.set(__self__, "access_key", access_key)
        if end_point and not isinstance(end_point, str):
            raise TypeError("Expected argument 'end_point' to be a str")
        pulumi.set(__self__, "end_point", end_point)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if ssl_status and not isinstance(ssl_status, str):
            raise TypeError("Expected argument 'ssl_status' to be a str")
        pulumi.set(__self__, "ssl_status", ssl_status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volumes_count and not isinstance(volumes_count, int):
            raise TypeError("Expected argument 'volumes_count' to be a int")
        pulumi.set(__self__, "volumes_count", volumes_count)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional['outputs.AsymmetricEncryptedSecretResponse']:
        """
        The details of the storage account password.
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="endPoint")
    def end_point(self) -> str:
        """
        The storage endpoint
        """
        return pulumi.get(self, "end_point")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sslStatus")
    def ssl_status(self) -> str:
        """
        Signifies whether SSL needs to be enabled or not.
        """
        return pulumi.get(self, "ssl_status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumesCount")
    def volumes_count(self) -> int:
        """
        The count of volumes using this storage account credential.
        """
        return pulumi.get(self, "volumes_count")


class AwaitableGetStorageAccountCredentialResult(GetStorageAccountCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageAccountCredentialResult(
            access_key=self.access_key,
            end_point=self.end_point,
            id=self.id,
            kind=self.kind,
            name=self.name,
            ssl_status=self.ssl_status,
            type=self.type,
            volumes_count=self.volumes_count)


def get_storage_account_credential(manager_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   storage_account_credential_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageAccountCredentialResult:
    """
    The storage account credential.
    API Version: 2017-06-01.


    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str storage_account_credential_name: The name of storage account credential to be fetched.
    """
    __args__ = dict()
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageAccountCredentialName'] = storage_account_credential_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple:getStorageAccountCredential', __args__, opts=opts, typ=GetStorageAccountCredentialResult).value

    return AwaitableGetStorageAccountCredentialResult(
        access_key=__ret__.access_key,
        end_point=__ret__.end_point,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        ssl_status=__ret__.ssl_status,
        type=__ret__.type,
        volumes_count=__ret__.volumes_count)


@_utilities.lift_output_func(get_storage_account_credential)
def get_storage_account_credential_output(manager_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          storage_account_credential_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageAccountCredentialResult]:
    """
    The storage account credential.
    API Version: 2017-06-01.


    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str storage_account_credential_name: The name of storage account credential to be fetched.
    """
    ...
