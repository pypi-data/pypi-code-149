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
    'GetProjectEnvironmentTypeResult',
    'AwaitableGetProjectEnvironmentTypeResult',
    'get_project_environment_type',
    'get_project_environment_type_output',
]

@pulumi.output_type
class GetProjectEnvironmentTypeResult:
    """
    Represents an environment type.
    """
    def __init__(__self__, creator_role_assignment=None, deployment_target_id=None, id=None, identity=None, location=None, name=None, provisioning_state=None, status=None, system_data=None, tags=None, type=None, user_role_assignments=None):
        if creator_role_assignment and not isinstance(creator_role_assignment, dict):
            raise TypeError("Expected argument 'creator_role_assignment' to be a dict")
        pulumi.set(__self__, "creator_role_assignment", creator_role_assignment)
        if deployment_target_id and not isinstance(deployment_target_id, str):
            raise TypeError("Expected argument 'deployment_target_id' to be a str")
        pulumi.set(__self__, "deployment_target_id", deployment_target_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_role_assignments and not isinstance(user_role_assignments, dict):
            raise TypeError("Expected argument 'user_role_assignments' to be a dict")
        pulumi.set(__self__, "user_role_assignments", user_role_assignments)

    @property
    @pulumi.getter(name="creatorRoleAssignment")
    def creator_role_assignment(self) -> Optional['outputs.ProjectEnvironmentTypeUpdatePropertiesResponseCreatorRoleAssignment']:
        """
        The role definition assigned to the environment creator on backing resources.
        """
        return pulumi.get(self, "creator_role_assignment")

    @property
    @pulumi.getter(name="deploymentTargetId")
    def deployment_target_id(self) -> Optional[str]:
        """
        Id of a subscription that the environment type will be mapped to. The environment's resources will be deployed into this subscription.
        """
        return pulumi.get(self, "deployment_target_id")

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
        Managed identity properties
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The geo-location for the environment type
        """
        return pulumi.get(self, "location")

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
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Defines whether this Environment Type can be used in this Project.
        """
        return pulumi.get(self, "status")

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

    @property
    @pulumi.getter(name="userRoleAssignments")
    def user_role_assignments(self) -> Optional[Mapping[str, 'outputs.UserRoleAssignmentResponse']]:
        """
        Role Assignments created on environment backing resources. This is a mapping from a user object ID to an object of role definition IDs.
        """
        return pulumi.get(self, "user_role_assignments")


class AwaitableGetProjectEnvironmentTypeResult(GetProjectEnvironmentTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectEnvironmentTypeResult(
            creator_role_assignment=self.creator_role_assignment,
            deployment_target_id=self.deployment_target_id,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            user_role_assignments=self.user_role_assignments)


def get_project_environment_type(environment_type_name: Optional[str] = None,
                                 project_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectEnvironmentTypeResult:
    """
    Represents an environment type.


    :param str environment_type_name: The name of the environment type.
    :param str project_name: The name of the project.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['environmentTypeName'] = environment_type_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20220801preview:getProjectEnvironmentType', __args__, opts=opts, typ=GetProjectEnvironmentTypeResult).value

    return AwaitableGetProjectEnvironmentTypeResult(
        creator_role_assignment=__ret__.creator_role_assignment,
        deployment_target_id=__ret__.deployment_target_id,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        status=__ret__.status,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        user_role_assignments=__ret__.user_role_assignments)


@_utilities.lift_output_func(get_project_environment_type)
def get_project_environment_type_output(environment_type_name: Optional[pulumi.Input[str]] = None,
                                        project_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectEnvironmentTypeResult]:
    """
    Represents an environment type.


    :param str environment_type_name: The name of the environment type.
    :param str project_name: The name of the project.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    ...
