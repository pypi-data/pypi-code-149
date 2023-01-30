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
from ._enums import *
from ._inputs import *

__all__ = ['TaskRunArgs', 'TaskRun']

@pulumi.input_type
class TaskRunArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityPropertiesArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 run_request: Optional[pulumi.Input[Union['DockerBuildRequestArgs', 'EncodedTaskRunRequestArgs', 'FileTaskRunRequestArgs', 'TaskRunRequestArgs']]] = None,
                 task_run_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TaskRun resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[str] force_update_tag: How the run should be forced to rerun even if the run request configuration has not changed
        :param pulumi.Input['IdentityPropertiesArgs'] identity: Identity for the resource.
        :param pulumi.Input[str] location: The location of the resource
        :param pulumi.Input[Union['DockerBuildRequestArgs', 'EncodedTaskRunRequestArgs', 'FileTaskRunRequestArgs', 'TaskRunRequestArgs']] run_request: The request (parameters) for the run
        :param pulumi.Input[str] task_run_name: The name of the task run.
        """
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if force_update_tag is not None:
            pulumi.set(__self__, "force_update_tag", force_update_tag)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if run_request is not None:
            pulumi.set(__self__, "run_request", run_request)
        if task_run_name is not None:
            pulumi.set(__self__, "task_run_name", task_run_name)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the container registry belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[str]]:
        """
        How the run should be forced to rerun even if the run request configuration has not changed
        """
        return pulumi.get(self, "force_update_tag")

    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "force_update_tag", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityPropertiesArgs']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityPropertiesArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="runRequest")
    def run_request(self) -> Optional[pulumi.Input[Union['DockerBuildRequestArgs', 'EncodedTaskRunRequestArgs', 'FileTaskRunRequestArgs', 'TaskRunRequestArgs']]]:
        """
        The request (parameters) for the run
        """
        return pulumi.get(self, "run_request")

    @run_request.setter
    def run_request(self, value: Optional[pulumi.Input[Union['DockerBuildRequestArgs', 'EncodedTaskRunRequestArgs', 'FileTaskRunRequestArgs', 'TaskRunRequestArgs']]]):
        pulumi.set(self, "run_request", value)

    @property
    @pulumi.getter(name="taskRunName")
    def task_run_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the task run.
        """
        return pulumi.get(self, "task_run_name")

    @task_run_name.setter
    def task_run_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "task_run_name", value)


class TaskRun(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_request: Optional[pulumi.Input[Union[pulumi.InputType['DockerBuildRequestArgs'], pulumi.InputType['EncodedTaskRunRequestArgs'], pulumi.InputType['FileTaskRunRequestArgs'], pulumi.InputType['TaskRunRequestArgs']]]] = None,
                 task_run_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The task run that has the ARM resource and properties.
        The task run will have the information of request and result of a run.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] force_update_tag: How the run should be forced to rerun even if the run request configuration has not changed
        :param pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']] identity: Identity for the resource.
        :param pulumi.Input[str] location: The location of the resource
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[Union[pulumi.InputType['DockerBuildRequestArgs'], pulumi.InputType['EncodedTaskRunRequestArgs'], pulumi.InputType['FileTaskRunRequestArgs'], pulumi.InputType['TaskRunRequestArgs']]] run_request: The request (parameters) for the run
        :param pulumi.Input[str] task_run_name: The name of the task run.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TaskRunArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The task run that has the ARM resource and properties.
        The task run will have the information of request and result of a run.

        :param str resource_name: The name of the resource.
        :param TaskRunArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TaskRunArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_request: Optional[pulumi.Input[Union[pulumi.InputType['DockerBuildRequestArgs'], pulumi.InputType['EncodedTaskRunRequestArgs'], pulumi.InputType['FileTaskRunRequestArgs'], pulumi.InputType['TaskRunRequestArgs']]]] = None,
                 task_run_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TaskRunArgs.__new__(TaskRunArgs)

            __props__.__dict__["force_update_tag"] = force_update_tag
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["run_request"] = run_request
            __props__.__dict__["task_run_name"] = task_run_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["run_result"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry:TaskRun")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TaskRun, __self__).__init__(
            'azure-native:containerregistry/v20190601preview:TaskRun',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TaskRun':
        """
        Get an existing TaskRun resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TaskRunArgs.__new__(TaskRunArgs)

        __props__.__dict__["force_update_tag"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["run_request"] = None
        __props__.__dict__["run_result"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return TaskRun(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[str]]:
        """
        How the run should be forced to rerun even if the run request configuration has not changed
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityPropertiesResponse']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of this task run
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runRequest")
    def run_request(self) -> pulumi.Output[Optional[Any]]:
        """
        The request (parameters) for the run
        """
        return pulumi.get(self, "run_request")

    @property
    @pulumi.getter(name="runResult")
    def run_result(self) -> pulumi.Output['outputs.RunResponse']:
        """
        The result of this task run
        """
        return pulumi.get(self, "run_result")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

