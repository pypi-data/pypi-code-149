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

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 is_auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
                 kafka_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_throughput_units: Optional[pulumi.Input[int]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input[bool] is_auto_inflate_enabled: Value that indicates whether AutoInflate is enabled for eventhub namespace.
        :param pulumi.Input[bool] kafka_enabled: Value that indicates whether Kafka is enabled for eventhub namespace.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[int] maximum_throughput_units: Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input['SkuArgs'] sku: Properties of sku resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if is_auto_inflate_enabled is not None:
            pulumi.set(__self__, "is_auto_inflate_enabled", is_auto_inflate_enabled)
        if kafka_enabled is not None:
            pulumi.set(__self__, "kafka_enabled", kafka_enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if maximum_throughput_units is not None:
            pulumi.set(__self__, "maximum_throughput_units", maximum_throughput_units)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="isAutoInflateEnabled")
    def is_auto_inflate_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether AutoInflate is enabled for eventhub namespace.
        """
        return pulumi.get(self, "is_auto_inflate_enabled")

    @is_auto_inflate_enabled.setter
    def is_auto_inflate_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_auto_inflate_enabled", value)

    @property
    @pulumi.getter(name="kafkaEnabled")
    def kafka_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether Kafka is enabled for eventhub namespace.
        """
        return pulumi.get(self, "kafka_enabled")

    @kafka_enabled.setter
    def kafka_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "kafka_enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maximumThroughputUnits")
    def maximum_throughput_units(self) -> Optional[pulumi.Input[int]]:
        """
        Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        """
        return pulumi.get(self, "maximum_throughput_units")

    @maximum_throughput_units.setter
    def maximum_throughput_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_throughput_units", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        Properties of sku resource
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
                 kafka_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_throughput_units: Optional[pulumi.Input[int]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Single Namespace item in List or Get Operation
        API Version: 2017-04-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_auto_inflate_enabled: Value that indicates whether AutoInflate is enabled for eventhub namespace.
        :param pulumi.Input[bool] kafka_enabled: Value that indicates whether Kafka is enabled for eventhub namespace.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[int] maximum_throughput_units: Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: Properties of sku resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Single Namespace item in List or Get Operation
        API Version: 2017-04-01.

        :param str resource_name: The name of the resource.
        :param NamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
                 kafka_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_throughput_units: Optional[pulumi.Input[int]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["is_auto_inflate_enabled"] = is_auto_inflate_enabled
            __props__.__dict__["kafka_enabled"] = kafka_enabled
            __props__.__dict__["location"] = location
            __props__.__dict__["maximum_throughput_units"] = maximum_throughput_units
            __props__.__dict__["namespace_name"] = namespace_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_at"] = None
            __props__.__dict__["metric_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["service_bus_endpoint"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventhub/v20140901:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20150801:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20170401:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20180101preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20210101preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20210601preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20211101:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20220101preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20221001preview:Namespace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Namespace, __self__).__init__(
            'azure-native:eventhub:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceArgs.__new__(NamespaceArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["is_auto_inflate_enabled"] = None
        __props__.__dict__["kafka_enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maximum_throughput_units"] = None
        __props__.__dict__["metric_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_bus_endpoint"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time the Namespace was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="isAutoInflateEnabled")
    def is_auto_inflate_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether AutoInflate is enabled for eventhub namespace.
        """
        return pulumi.get(self, "is_auto_inflate_enabled")

    @property
    @pulumi.getter(name="kafkaEnabled")
    def kafka_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether Kafka is enabled for eventhub namespace.
        """
        return pulumi.get(self, "kafka_enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumThroughputUnits")
    def maximum_throughput_units(self) -> pulumi.Output[Optional[int]]:
        """
        Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        """
        return pulumi.get(self, "maximum_throughput_units")

    @property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> pulumi.Output[str]:
        """
        Identifier for Azure Insights metrics.
        """
        return pulumi.get(self, "metric_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint you can use to perform Service Bus operations.
        """
        return pulumi.get(self, "service_bus_endpoint")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        Properties of sku resource
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The time the Namespace was updated.
        """
        return pulumi.get(self, "updated_at")

