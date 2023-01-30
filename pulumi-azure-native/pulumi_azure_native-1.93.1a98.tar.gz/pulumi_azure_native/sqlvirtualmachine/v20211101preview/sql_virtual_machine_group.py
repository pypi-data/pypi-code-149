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

__all__ = ['SqlVirtualMachineGroupArgs', 'SqlVirtualMachineGroup']

@pulumi.input_type
class SqlVirtualMachineGroupArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 sql_image_offer: Optional[pulumi.Input[str]] = None,
                 sql_image_sku: Optional[pulumi.Input[Union[str, 'SqlVmGroupImageSku']]] = None,
                 sql_virtual_machine_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 wsfc_domain_profile: Optional[pulumi.Input['WsfcDomainProfileArgs']] = None):
        """
        The set of arguments for constructing a SqlVirtualMachineGroup resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] sql_image_offer: SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.
        :param pulumi.Input[Union[str, 'SqlVmGroupImageSku']] sql_image_sku: SQL image sku.
        :param pulumi.Input[str] sql_virtual_machine_group_name: Name of the SQL virtual machine group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['WsfcDomainProfileArgs'] wsfc_domain_profile: Cluster Active Directory domain profile.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sql_image_offer is not None:
            pulumi.set(__self__, "sql_image_offer", sql_image_offer)
        if sql_image_sku is not None:
            pulumi.set(__self__, "sql_image_sku", sql_image_sku)
        if sql_virtual_machine_group_name is not None:
            pulumi.set(__self__, "sql_virtual_machine_group_name", sql_virtual_machine_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if wsfc_domain_profile is not None:
            pulumi.set(__self__, "wsfc_domain_profile", wsfc_domain_profile)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

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
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> Optional[pulumi.Input[str]]:
        """
        SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.
        """
        return pulumi.get(self, "sql_image_offer")

    @sql_image_offer.setter
    def sql_image_offer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_image_offer", value)

    @property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> Optional[pulumi.Input[Union[str, 'SqlVmGroupImageSku']]]:
        """
        SQL image sku.
        """
        return pulumi.get(self, "sql_image_sku")

    @sql_image_sku.setter
    def sql_image_sku(self, value: Optional[pulumi.Input[Union[str, 'SqlVmGroupImageSku']]]):
        pulumi.set(self, "sql_image_sku", value)

    @property
    @pulumi.getter(name="sqlVirtualMachineGroupName")
    def sql_virtual_machine_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SQL virtual machine group.
        """
        return pulumi.get(self, "sql_virtual_machine_group_name")

    @sql_virtual_machine_group_name.setter
    def sql_virtual_machine_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_virtual_machine_group_name", value)

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

    @property
    @pulumi.getter(name="wsfcDomainProfile")
    def wsfc_domain_profile(self) -> Optional[pulumi.Input['WsfcDomainProfileArgs']]:
        """
        Cluster Active Directory domain profile.
        """
        return pulumi.get(self, "wsfc_domain_profile")

    @wsfc_domain_profile.setter
    def wsfc_domain_profile(self, value: Optional[pulumi.Input['WsfcDomainProfileArgs']]):
        pulumi.set(self, "wsfc_domain_profile", value)


class SqlVirtualMachineGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_image_offer: Optional[pulumi.Input[str]] = None,
                 sql_image_sku: Optional[pulumi.Input[Union[str, 'SqlVmGroupImageSku']]] = None,
                 sql_virtual_machine_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 wsfc_domain_profile: Optional[pulumi.Input[pulumi.InputType['WsfcDomainProfileArgs']]] = None,
                 __props__=None):
        """
        A SQL virtual machine group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] sql_image_offer: SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.
        :param pulumi.Input[Union[str, 'SqlVmGroupImageSku']] sql_image_sku: SQL image sku.
        :param pulumi.Input[str] sql_virtual_machine_group_name: Name of the SQL virtual machine group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['WsfcDomainProfileArgs']] wsfc_domain_profile: Cluster Active Directory domain profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlVirtualMachineGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A SQL virtual machine group.

        :param str resource_name: The name of the resource.
        :param SqlVirtualMachineGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlVirtualMachineGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_image_offer: Optional[pulumi.Input[str]] = None,
                 sql_image_sku: Optional[pulumi.Input[Union[str, 'SqlVmGroupImageSku']]] = None,
                 sql_virtual_machine_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 wsfc_domain_profile: Optional[pulumi.Input[pulumi.InputType['WsfcDomainProfileArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlVirtualMachineGroupArgs.__new__(SqlVirtualMachineGroupArgs)

            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sql_image_offer"] = sql_image_offer
            __props__.__dict__["sql_image_sku"] = sql_image_sku
            __props__.__dict__["sql_virtual_machine_group_name"] = sql_virtual_machine_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["wsfc_domain_profile"] = wsfc_domain_profile
            __props__.__dict__["cluster_configuration"] = None
            __props__.__dict__["cluster_manager_type"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["scale_type"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sqlvirtualmachine:SqlVirtualMachineGroup"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20170301preview:SqlVirtualMachineGroup"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20220201:SqlVirtualMachineGroup"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20220201preview:SqlVirtualMachineGroup"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20220701preview:SqlVirtualMachineGroup"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20220801preview:SqlVirtualMachineGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlVirtualMachineGroup, __self__).__init__(
            'azure-native:sqlvirtualmachine/v20211101preview:SqlVirtualMachineGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlVirtualMachineGroup':
        """
        Get an existing SqlVirtualMachineGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlVirtualMachineGroupArgs.__new__(SqlVirtualMachineGroupArgs)

        __props__.__dict__["cluster_configuration"] = None
        __props__.__dict__["cluster_manager_type"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["scale_type"] = None
        __props__.__dict__["sql_image_offer"] = None
        __props__.__dict__["sql_image_sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["wsfc_domain_profile"] = None
        return SqlVirtualMachineGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterConfiguration")
    def cluster_configuration(self) -> pulumi.Output[str]:
        """
        Cluster type.
        """
        return pulumi.get(self, "cluster_configuration")

    @property
    @pulumi.getter(name="clusterManagerType")
    def cluster_manager_type(self) -> pulumi.Output[str]:
        """
        Type of cluster manager: Windows Server Failover Cluster (WSFC), implied by the scale type of the group and the OS type.
        """
        return pulumi.get(self, "cluster_manager_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state to track the async operation status.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> pulumi.Output[str]:
        """
        Scale type.
        """
        return pulumi.get(self, "scale_type")

    @property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> pulumi.Output[Optional[str]]:
        """
        SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.
        """
        return pulumi.get(self, "sql_image_offer")

    @property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> pulumi.Output[Optional[str]]:
        """
        SQL image sku.
        """
        return pulumi.get(self, "sql_image_sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="wsfcDomainProfile")
    def wsfc_domain_profile(self) -> pulumi.Output[Optional['outputs.WsfcDomainProfileResponse']]:
        """
        Cluster Active Directory domain profile.
        """
        return pulumi.get(self, "wsfc_domain_profile")

