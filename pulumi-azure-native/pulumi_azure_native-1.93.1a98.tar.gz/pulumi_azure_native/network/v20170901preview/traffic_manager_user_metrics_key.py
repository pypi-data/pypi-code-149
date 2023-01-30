# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['TrafficManagerUserMetricsKeyArgs', 'TrafficManagerUserMetricsKey']

@pulumi.input_type
class TrafficManagerUserMetricsKeyArgs:
    def __init__(__self__):
        """
        The set of arguments for constructing a TrafficManagerUserMetricsKey resource.
        """
        pass


warnings.warn("""Version 2017-09-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class TrafficManagerUserMetricsKey(pulumi.CustomResource):
    warnings.warn("""Version 2017-09-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        """
        Class representing a Traffic Manager Real User Metrics key response.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TrafficManagerUserMetricsKeyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a Traffic Manager Real User Metrics key response.

        :param str resource_name: The name of the resource.
        :param TrafficManagerUserMetricsKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrafficManagerUserMetricsKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        pulumi.log.warn("""TrafficManagerUserMetricsKey is deprecated: Version 2017-09-01-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrafficManagerUserMetricsKeyArgs.__new__(TrafficManagerUserMetricsKeyArgs)

            __props__.__dict__["key"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        super(TrafficManagerUserMetricsKey, __self__).__init__(
            'azure-native:network/v20170901preview:TrafficManagerUserMetricsKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TrafficManagerUserMetricsKey':
        """
        Get an existing TrafficManagerUserMetricsKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TrafficManagerUserMetricsKeyArgs.__new__(TrafficManagerUserMetricsKeyArgs)

        __props__.__dict__["key"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return TrafficManagerUserMetricsKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        The key returned by the Real User Metrics operation.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
        """
        return pulumi.get(self, "type")

