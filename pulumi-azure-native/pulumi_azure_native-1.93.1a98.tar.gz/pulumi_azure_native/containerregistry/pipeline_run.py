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
from ._enums import *
from ._inputs import *

__all__ = ['PipelineRunArgs', 'PipelineRun']

@pulumi.input_type
class PipelineRunArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 pipeline_run_name: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input['PipelineRunRequestArgs']] = None):
        """
        The set of arguments for constructing a PipelineRun resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[str] force_update_tag: How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.
        :param pulumi.Input[str] pipeline_run_name: The name of the pipeline run.
        :param pulumi.Input['PipelineRunRequestArgs'] request: The request parameters for a pipeline run.
        """
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if force_update_tag is not None:
            pulumi.set(__self__, "force_update_tag", force_update_tag)
        if pipeline_run_name is not None:
            pulumi.set(__self__, "pipeline_run_name", pipeline_run_name)
        if request is not None:
            pulumi.set(__self__, "request", request)

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
        How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "force_update_tag", value)

    @property
    @pulumi.getter(name="pipelineRunName")
    def pipeline_run_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the pipeline run.
        """
        return pulumi.get(self, "pipeline_run_name")

    @pipeline_run_name.setter
    def pipeline_run_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_run_name", value)

    @property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input['PipelineRunRequestArgs']]:
        """
        The request parameters for a pipeline run.
        """
        return pulumi.get(self, "request")

    @request.setter
    def request(self, value: Optional[pulumi.Input['PipelineRunRequestArgs']]):
        pulumi.set(self, "request", value)


class PipelineRun(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 pipeline_run_name: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input[pulumi.InputType['PipelineRunRequestArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents a pipeline run for a container registry.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] force_update_tag: How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.
        :param pulumi.Input[str] pipeline_run_name: The name of the pipeline run.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[pulumi.InputType['PipelineRunRequestArgs']] request: The request parameters for a pipeline run.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineRunArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents a pipeline run for a container registry.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param PipelineRunArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineRunArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 pipeline_run_name: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input[pulumi.InputType['PipelineRunRequestArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineRunArgs.__new__(PipelineRunArgs)

            __props__.__dict__["force_update_tag"] = force_update_tag
            __props__.__dict__["pipeline_run_name"] = pipeline_run_name
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            __props__.__dict__["request"] = request
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["response"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry/v20191201preview:PipelineRun"), pulumi.Alias(type_="azure-native:containerregistry/v20201101preview:PipelineRun"), pulumi.Alias(type_="azure-native:containerregistry/v20210601preview:PipelineRun"), pulumi.Alias(type_="azure-native:containerregistry/v20210801preview:PipelineRun"), pulumi.Alias(type_="azure-native:containerregistry/v20211201preview:PipelineRun"), pulumi.Alias(type_="azure-native:containerregistry/v20220201preview:PipelineRun"), pulumi.Alias(type_="azure-native:containerregistry/v20230101preview:PipelineRun")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PipelineRun, __self__).__init__(
            'azure-native:containerregistry:PipelineRun',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PipelineRun':
        """
        Get an existing PipelineRun resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineRunArgs.__new__(PipelineRunArgs)

        __props__.__dict__["force_update_tag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["request"] = None
        __props__.__dict__["response"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PipelineRun(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[str]]:
        """
        How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

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
        The provisioning state of a pipeline run.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def request(self) -> pulumi.Output[Optional['outputs.PipelineRunRequestResponse']]:
        """
        The request parameters for a pipeline run.
        """
        return pulumi.get(self, "request")

    @property
    @pulumi.getter
    def response(self) -> pulumi.Output['outputs.PipelineRunResponseResponse']:
        """
        The response of a pipeline run.
        """
        return pulumi.get(self, "response")

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

