# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['StaticSiteUserProvidedFunctionAppForStaticSiteArgs', 'StaticSiteUserProvidedFunctionAppForStaticSite']

@pulumi.input_type
class StaticSiteUserProvidedFunctionAppForStaticSiteArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 function_app_name: Optional[pulumi.Input[str]] = None,
                 function_app_region: Optional[pulumi.Input[str]] = None,
                 function_app_resource_id: Optional[pulumi.Input[str]] = None,
                 is_forced: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StaticSiteUserProvidedFunctionAppForStaticSite resource.
        :param pulumi.Input[str] name: Name of the static site.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] function_app_name: Name of the function app to register with the static site.
        :param pulumi.Input[str] function_app_region: The region of the function app registered with the static site
        :param pulumi.Input[str] function_app_resource_id: The resource id of the function app registered with the static site
        :param pulumi.Input[bool] is_forced: Specify <code>true</code> to force the update of the auth configuration on the function app even if an AzureStaticWebApps provider is already configured on the function app. The default is <code>false</code>.
        :param pulumi.Input[str] kind: Kind of resource.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if function_app_name is not None:
            pulumi.set(__self__, "function_app_name", function_app_name)
        if function_app_region is not None:
            pulumi.set(__self__, "function_app_region", function_app_region)
        if function_app_resource_id is not None:
            pulumi.set(__self__, "function_app_resource_id", function_app_resource_id)
        if is_forced is not None:
            pulumi.set(__self__, "is_forced", is_forced)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the static site.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="functionAppName")
    def function_app_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the function app to register with the static site.
        """
        return pulumi.get(self, "function_app_name")

    @function_app_name.setter
    def function_app_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_app_name", value)

    @property
    @pulumi.getter(name="functionAppRegion")
    def function_app_region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the function app registered with the static site
        """
        return pulumi.get(self, "function_app_region")

    @function_app_region.setter
    def function_app_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_app_region", value)

    @property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the function app registered with the static site
        """
        return pulumi.get(self, "function_app_resource_id")

    @function_app_resource_id.setter
    def function_app_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_app_resource_id", value)

    @property
    @pulumi.getter(name="isForced")
    def is_forced(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify <code>true</code> to force the update of the auth configuration on the function app even if an AzureStaticWebApps provider is already configured on the function app. The default is <code>false</code>.
        """
        return pulumi.get(self, "is_forced")

    @is_forced.setter
    def is_forced(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_forced", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)


class StaticSiteUserProvidedFunctionAppForStaticSite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 function_app_name: Optional[pulumi.Input[str]] = None,
                 function_app_region: Optional[pulumi.Input[str]] = None,
                 function_app_resource_id: Optional[pulumi.Input[str]] = None,
                 is_forced: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Static Site User Provided Function App ARM resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] function_app_name: Name of the function app to register with the static site.
        :param pulumi.Input[str] function_app_region: The region of the function app registered with the static site
        :param pulumi.Input[str] function_app_resource_id: The resource id of the function app registered with the static site
        :param pulumi.Input[bool] is_forced: Specify <code>true</code> to force the update of the auth configuration on the function app even if an AzureStaticWebApps provider is already configured on the function app. The default is <code>false</code>.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the static site.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StaticSiteUserProvidedFunctionAppForStaticSiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Static Site User Provided Function App ARM resource.

        :param str resource_name: The name of the resource.
        :param StaticSiteUserProvidedFunctionAppForStaticSiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticSiteUserProvidedFunctionAppForStaticSiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 function_app_name: Optional[pulumi.Input[str]] = None,
                 function_app_region: Optional[pulumi.Input[str]] = None,
                 function_app_resource_id: Optional[pulumi.Input[str]] = None,
                 is_forced: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StaticSiteUserProvidedFunctionAppForStaticSiteArgs.__new__(StaticSiteUserProvidedFunctionAppForStaticSiteArgs)

            __props__.__dict__["function_app_name"] = function_app_name
            __props__.__dict__["function_app_region"] = function_app_region
            __props__.__dict__["function_app_resource_id"] = function_app_resource_id
            __props__.__dict__["is_forced"] = is_forced
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["created_on"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:StaticSiteUserProvidedFunctionAppForStaticSite"), pulumi.Alias(type_="azure-native:web/v20201201:StaticSiteUserProvidedFunctionAppForStaticSite"), pulumi.Alias(type_="azure-native:web/v20210101:StaticSiteUserProvidedFunctionAppForStaticSite"), pulumi.Alias(type_="azure-native:web/v20210115:StaticSiteUserProvidedFunctionAppForStaticSite"), pulumi.Alias(type_="azure-native:web/v20210201:StaticSiteUserProvidedFunctionAppForStaticSite"), pulumi.Alias(type_="azure-native:web/v20210301:StaticSiteUserProvidedFunctionAppForStaticSite")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StaticSiteUserProvidedFunctionAppForStaticSite, __self__).__init__(
            'azure-native:web/v20220301:StaticSiteUserProvidedFunctionAppForStaticSite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StaticSiteUserProvidedFunctionAppForStaticSite':
        """
        Get an existing StaticSiteUserProvidedFunctionAppForStaticSite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StaticSiteUserProvidedFunctionAppForStaticSiteArgs.__new__(StaticSiteUserProvidedFunctionAppForStaticSiteArgs)

        __props__.__dict__["created_on"] = None
        __props__.__dict__["function_app_region"] = None
        __props__.__dict__["function_app_resource_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return StaticSiteUserProvidedFunctionAppForStaticSite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        The date and time on which the function app was registered with the static site.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="functionAppRegion")
    def function_app_region(self) -> pulumi.Output[Optional[str]]:
        """
        The region of the function app registered with the static site
        """
        return pulumi.get(self, "function_app_region")

    @property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource id of the function app registered with the static site
        """
        return pulumi.get(self, "function_app_resource_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

