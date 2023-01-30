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
    'GetSqlServerResult',
    'AwaitableGetSqlServerResult',
    'get_sql_server',
    'get_sql_server_output',
]

warnings.warn("""Version 2017-03-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetSqlServerResult:
    """
    A SQL server.
    """
    def __init__(__self__, edition=None, id=None, name=None, property_bag=None, registration_id=None, type=None, version=None):
        if edition and not isinstance(edition, str):
            raise TypeError("Expected argument 'edition' to be a str")
        pulumi.set(__self__, "edition", edition)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if property_bag and not isinstance(property_bag, str):
            raise TypeError("Expected argument 'property_bag' to be a str")
        pulumi.set(__self__, "property_bag", property_bag)
        if registration_id and not isinstance(registration_id, str):
            raise TypeError("Expected argument 'registration_id' to be a str")
        pulumi.set(__self__, "registration_id", registration_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def edition(self) -> Optional[str]:
        """
        Sql Server Edition.
        """
        return pulumi.get(self, "edition")

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
    @pulumi.getter(name="propertyBag")
    def property_bag(self) -> Optional[str]:
        """
        Sql Server Json Property Bag.
        """
        return pulumi.get(self, "property_bag")

    @property
    @pulumi.getter(name="registrationID")
    def registration_id(self) -> Optional[str]:
        """
        ID for Parent Sql Server Registration.
        """
        return pulumi.get(self, "registration_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Version of the Sql Server.
        """
        return pulumi.get(self, "version")


class AwaitableGetSqlServerResult(GetSqlServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlServerResult(
            edition=self.edition,
            id=self.id,
            name=self.name,
            property_bag=self.property_bag,
            registration_id=self.registration_id,
            type=self.type,
            version=self.version)


def get_sql_server(expand: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   sql_server_name: Optional[str] = None,
                   sql_server_registration_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlServerResult:
    """
    A SQL server.


    :param str expand: The child resources to include in the response.
    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_server_name: Name of the SQL Server.
    :param str sql_server_registration_name: Name of the SQL Server registration.
    """
    pulumi.log.warn("""get_sql_server is deprecated: Version 2017-03-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlServerName'] = sql_server_name
    __args__['sqlServerRegistrationName'] = sql_server_registration_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azuredata/v20170301preview:getSqlServer', __args__, opts=opts, typ=GetSqlServerResult).value

    return AwaitableGetSqlServerResult(
        edition=__ret__.edition,
        id=__ret__.id,
        name=__ret__.name,
        property_bag=__ret__.property_bag,
        registration_id=__ret__.registration_id,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_sql_server)
def get_sql_server_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          sql_server_name: Optional[pulumi.Input[str]] = None,
                          sql_server_registration_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlServerResult]:
    """
    A SQL server.


    :param str expand: The child resources to include in the response.
    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_server_name: Name of the SQL Server.
    :param str sql_server_registration_name: Name of the SQL Server registration.
    """
    pulumi.log.warn("""get_sql_server is deprecated: Version 2017-03-01-preview will be removed in v2 of the provider.""")
    ...
