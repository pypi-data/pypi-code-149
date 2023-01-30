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
    'GetSyncMemberResult',
    'AwaitableGetSyncMemberResult',
    'get_sync_member',
    'get_sync_member_output',
]

@pulumi.output_type
class GetSyncMemberResult:
    """
    An Azure SQL Database sync member.
    """
    def __init__(__self__, database_name=None, database_type=None, id=None, name=None, private_endpoint_name=None, server_name=None, sql_server_database_id=None, sync_agent_id=None, sync_direction=None, sync_member_azure_database_resource_id=None, sync_state=None, type=None, use_private_link_connection=None, user_name=None):
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if database_type and not isinstance(database_type, str):
            raise TypeError("Expected argument 'database_type' to be a str")
        pulumi.set(__self__, "database_type", database_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_name and not isinstance(private_endpoint_name, str):
            raise TypeError("Expected argument 'private_endpoint_name' to be a str")
        pulumi.set(__self__, "private_endpoint_name", private_endpoint_name)
        if server_name and not isinstance(server_name, str):
            raise TypeError("Expected argument 'server_name' to be a str")
        pulumi.set(__self__, "server_name", server_name)
        if sql_server_database_id and not isinstance(sql_server_database_id, str):
            raise TypeError("Expected argument 'sql_server_database_id' to be a str")
        pulumi.set(__self__, "sql_server_database_id", sql_server_database_id)
        if sync_agent_id and not isinstance(sync_agent_id, str):
            raise TypeError("Expected argument 'sync_agent_id' to be a str")
        pulumi.set(__self__, "sync_agent_id", sync_agent_id)
        if sync_direction and not isinstance(sync_direction, str):
            raise TypeError("Expected argument 'sync_direction' to be a str")
        pulumi.set(__self__, "sync_direction", sync_direction)
        if sync_member_azure_database_resource_id and not isinstance(sync_member_azure_database_resource_id, str):
            raise TypeError("Expected argument 'sync_member_azure_database_resource_id' to be a str")
        pulumi.set(__self__, "sync_member_azure_database_resource_id", sync_member_azure_database_resource_id)
        if sync_state and not isinstance(sync_state, str):
            raise TypeError("Expected argument 'sync_state' to be a str")
        pulumi.set(__self__, "sync_state", sync_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if use_private_link_connection and not isinstance(use_private_link_connection, bool):
            raise TypeError("Expected argument 'use_private_link_connection' to be a bool")
        pulumi.set(__self__, "use_private_link_connection", use_private_link_connection)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[str]:
        """
        Database name of the member database in the sync member.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[str]:
        """
        Database type of the sync member.
        """
        return pulumi.get(self, "database_type")

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
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> str:
        """
        Private endpoint name of the sync member if use private link connection is enabled, for sync members in Azure.
        """
        return pulumi.get(self, "private_endpoint_name")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[str]:
        """
        Server name of the member database in the sync member
        """
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter(name="sqlServerDatabaseId")
    def sql_server_database_id(self) -> Optional[str]:
        """
        SQL Server database id of the sync member.
        """
        return pulumi.get(self, "sql_server_database_id")

    @property
    @pulumi.getter(name="syncAgentId")
    def sync_agent_id(self) -> Optional[str]:
        """
        ARM resource id of the sync agent in the sync member.
        """
        return pulumi.get(self, "sync_agent_id")

    @property
    @pulumi.getter(name="syncDirection")
    def sync_direction(self) -> Optional[str]:
        """
        Sync direction of the sync member.
        """
        return pulumi.get(self, "sync_direction")

    @property
    @pulumi.getter(name="syncMemberAzureDatabaseResourceId")
    def sync_member_azure_database_resource_id(self) -> Optional[str]:
        """
        ARM resource id of the sync member logical database, for sync members in Azure.
        """
        return pulumi.get(self, "sync_member_azure_database_resource_id")

    @property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> str:
        """
        Sync state of the sync member.
        """
        return pulumi.get(self, "sync_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usePrivateLinkConnection")
    def use_private_link_connection(self) -> Optional[bool]:
        """
        Whether to use private link connection.
        """
        return pulumi.get(self, "use_private_link_connection")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[str]:
        """
        User name of the member database in the sync member.
        """
        return pulumi.get(self, "user_name")


class AwaitableGetSyncMemberResult(GetSyncMemberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSyncMemberResult(
            database_name=self.database_name,
            database_type=self.database_type,
            id=self.id,
            name=self.name,
            private_endpoint_name=self.private_endpoint_name,
            server_name=self.server_name,
            sql_server_database_id=self.sql_server_database_id,
            sync_agent_id=self.sync_agent_id,
            sync_direction=self.sync_direction,
            sync_member_azure_database_resource_id=self.sync_member_azure_database_resource_id,
            sync_state=self.sync_state,
            type=self.type,
            use_private_link_connection=self.use_private_link_connection,
            user_name=self.user_name)


def get_sync_member(database_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    server_name: Optional[str] = None,
                    sync_group_name: Optional[str] = None,
                    sync_member_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSyncMemberResult:
    """
    An Azure SQL Database sync member.


    :param str database_name: The name of the database on which the sync group is hosted.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    :param str sync_group_name: The name of the sync group on which the sync member is hosted.
    :param str sync_member_name: The name of the sync member.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    __args__['syncGroupName'] = sync_group_name
    __args__['syncMemberName'] = sync_member_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20211101:getSyncMember', __args__, opts=opts, typ=GetSyncMemberResult).value

    return AwaitableGetSyncMemberResult(
        database_name=__ret__.database_name,
        database_type=__ret__.database_type,
        id=__ret__.id,
        name=__ret__.name,
        private_endpoint_name=__ret__.private_endpoint_name,
        server_name=__ret__.server_name,
        sql_server_database_id=__ret__.sql_server_database_id,
        sync_agent_id=__ret__.sync_agent_id,
        sync_direction=__ret__.sync_direction,
        sync_member_azure_database_resource_id=__ret__.sync_member_azure_database_resource_id,
        sync_state=__ret__.sync_state,
        type=__ret__.type,
        use_private_link_connection=__ret__.use_private_link_connection,
        user_name=__ret__.user_name)


@_utilities.lift_output_func(get_sync_member)
def get_sync_member_output(database_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           server_name: Optional[pulumi.Input[str]] = None,
                           sync_group_name: Optional[pulumi.Input[str]] = None,
                           sync_member_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSyncMemberResult]:
    """
    An Azure SQL Database sync member.


    :param str database_name: The name of the database on which the sync group is hosted.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    :param str sync_group_name: The name of the sync group on which the sync member is hosted.
    :param str sync_member_name: The name of the sync member.
    """
    ...
