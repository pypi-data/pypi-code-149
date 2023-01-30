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
from ._inputs import *

__all__ = ['ServerFarmArgs', 'ServerFarm']

@pulumi.input_type
class ServerFarmArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 admin_site_name: Optional[pulumi.Input[str]] = None,
                 allow_pending_state: Optional[pulumi.Input[bool]] = None,
                 hosting_environment_profile: Optional[pulumi.Input['HostingEnvironmentProfileArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_number_of_workers: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 per_site_scaling: Optional[pulumi.Input[bool]] = None,
                 reserved: Optional[pulumi.Input[bool]] = None,
                 sku: Optional[pulumi.Input['SkuDescriptionArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 worker_tier_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerFarm resource.
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[str] admin_site_name: App Service Plan administration site
        :param pulumi.Input[bool] allow_pending_state: OBSOLETE: If true, allow pending state for App Service Plan
        :param pulumi.Input['HostingEnvironmentProfileArgs'] hosting_environment_profile: Specification for the hosting environment (App Service Environment) to use for the App Service Plan
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[int] maximum_number_of_workers: Maximum number of instances that can be assigned to this App Service Plan
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[bool] per_site_scaling: If True apps assigned to this App Service Plan can be scaled independently
                           If False apps assigned to this App Service Plan will scale to all instances of the plan
        :param pulumi.Input[bool] reserved: Enables creation of a Linux App Service Plan
        :param pulumi.Input['SkuDescriptionArgs'] sku: Describes a sku for a scalable resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        :param pulumi.Input[str] worker_tier_name: Target worker tier assigned to the App Service Plan
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if admin_site_name is not None:
            pulumi.set(__self__, "admin_site_name", admin_site_name)
        if allow_pending_state is not None:
            pulumi.set(__self__, "allow_pending_state", allow_pending_state)
        if hosting_environment_profile is not None:
            pulumi.set(__self__, "hosting_environment_profile", hosting_environment_profile)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if maximum_number_of_workers is not None:
            pulumi.set(__self__, "maximum_number_of_workers", maximum_number_of_workers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if per_site_scaling is not None:
            pulumi.set(__self__, "per_site_scaling", per_site_scaling)
        if reserved is not None:
            pulumi.set(__self__, "reserved", reserved)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if worker_tier_name is not None:
            pulumi.set(__self__, "worker_tier_name", worker_tier_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="adminSiteName")
    def admin_site_name(self) -> Optional[pulumi.Input[str]]:
        """
        App Service Plan administration site
        """
        return pulumi.get(self, "admin_site_name")

    @admin_site_name.setter
    def admin_site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_site_name", value)

    @property
    @pulumi.getter(name="allowPendingState")
    def allow_pending_state(self) -> Optional[pulumi.Input[bool]]:
        """
        OBSOLETE: If true, allow pending state for App Service Plan
        """
        return pulumi.get(self, "allow_pending_state")

    @allow_pending_state.setter
    def allow_pending_state(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_pending_state", value)

    @property
    @pulumi.getter(name="hostingEnvironmentProfile")
    def hosting_environment_profile(self) -> Optional[pulumi.Input['HostingEnvironmentProfileArgs']]:
        """
        Specification for the hosting environment (App Service Environment) to use for the App Service Plan
        """
        return pulumi.get(self, "hosting_environment_profile")

    @hosting_environment_profile.setter
    def hosting_environment_profile(self, value: Optional[pulumi.Input['HostingEnvironmentProfileArgs']]):
        pulumi.set(self, "hosting_environment_profile", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maximumNumberOfWorkers")
    def maximum_number_of_workers(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of instances that can be assigned to this App Service Plan
        """
        return pulumi.get(self, "maximum_number_of_workers")

    @maximum_number_of_workers.setter
    def maximum_number_of_workers(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_number_of_workers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="perSiteScaling")
    def per_site_scaling(self) -> Optional[pulumi.Input[bool]]:
        """
        If True apps assigned to this App Service Plan can be scaled independently
                    If False apps assigned to this App Service Plan will scale to all instances of the plan
        """
        return pulumi.get(self, "per_site_scaling")

    @per_site_scaling.setter
    def per_site_scaling(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "per_site_scaling", value)

    @property
    @pulumi.getter
    def reserved(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables creation of a Linux App Service Plan
        """
        return pulumi.get(self, "reserved")

    @reserved.setter
    def reserved(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reserved", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuDescriptionArgs']]:
        """
        Describes a sku for a scalable resource
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuDescriptionArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="workerTierName")
    def worker_tier_name(self) -> Optional[pulumi.Input[str]]:
        """
        Target worker tier assigned to the App Service Plan
        """
        return pulumi.get(self, "worker_tier_name")

    @worker_tier_name.setter
    def worker_tier_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "worker_tier_name", value)


warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)


class ServerFarm(pulumi.CustomResource):
    warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_site_name: Optional[pulumi.Input[str]] = None,
                 allow_pending_state: Optional[pulumi.Input[bool]] = None,
                 hosting_environment_profile: Optional[pulumi.Input[pulumi.InputType['HostingEnvironmentProfileArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_number_of_workers: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 per_site_scaling: Optional[pulumi.Input[bool]] = None,
                 reserved: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuDescriptionArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 worker_tier_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        App Service Plan Model

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_site_name: App Service Plan administration site
        :param pulumi.Input[bool] allow_pending_state: OBSOLETE: If true, allow pending state for App Service Plan
        :param pulumi.Input[pulumi.InputType['HostingEnvironmentProfileArgs']] hosting_environment_profile: Specification for the hosting environment (App Service Environment) to use for the App Service Plan
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[int] maximum_number_of_workers: Maximum number of instances that can be assigned to this App Service Plan
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[bool] per_site_scaling: If True apps assigned to this App Service Plan can be scaled independently
                           If False apps assigned to this App Service Plan will scale to all instances of the plan
        :param pulumi.Input[bool] reserved: Enables creation of a Linux App Service Plan
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[pulumi.InputType['SkuDescriptionArgs']] sku: Describes a sku for a scalable resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        :param pulumi.Input[str] worker_tier_name: Target worker tier assigned to the App Service Plan
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerFarmArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        App Service Plan Model

        :param str resource_name: The name of the resource.
        :param ServerFarmArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerFarmArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_site_name: Optional[pulumi.Input[str]] = None,
                 allow_pending_state: Optional[pulumi.Input[bool]] = None,
                 hosting_environment_profile: Optional[pulumi.Input[pulumi.InputType['HostingEnvironmentProfileArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_number_of_workers: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 per_site_scaling: Optional[pulumi.Input[bool]] = None,
                 reserved: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuDescriptionArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 worker_tier_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ServerFarm is deprecated: Version 2015-08-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerFarmArgs.__new__(ServerFarmArgs)

            __props__.__dict__["admin_site_name"] = admin_site_name
            __props__.__dict__["allow_pending_state"] = allow_pending_state
            __props__.__dict__["hosting_environment_profile"] = hosting_environment_profile
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["maximum_number_of_workers"] = maximum_number_of_workers
            __props__.__dict__["name"] = name
            __props__.__dict__["per_site_scaling"] = per_site_scaling
            __props__.__dict__["reserved"] = reserved
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["worker_tier_name"] = worker_tier_name
            __props__.__dict__["geo_region"] = None
            __props__.__dict__["number_of_sites"] = None
            __props__.__dict__["resource_group"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["subscription"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20160901:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20180201:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20190801:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20200601:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20200901:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20201001:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20201201:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20210101:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20210115:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20210201:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20210301:ServerFarm"), pulumi.Alias(type_="azure-native:web/v20220301:ServerFarm")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerFarm, __self__).__init__(
            'azure-native:web/v20150801:ServerFarm',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerFarm':
        """
        Get an existing ServerFarm resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerFarmArgs.__new__(ServerFarmArgs)

        __props__.__dict__["admin_site_name"] = None
        __props__.__dict__["geo_region"] = None
        __props__.__dict__["hosting_environment_profile"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maximum_number_of_workers"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["number_of_sites"] = None
        __props__.__dict__["per_site_scaling"] = None
        __props__.__dict__["reserved"] = None
        __props__.__dict__["resource_group"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subscription"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["worker_tier_name"] = None
        return ServerFarm(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminSiteName")
    def admin_site_name(self) -> pulumi.Output[Optional[str]]:
        """
        App Service Plan administration site
        """
        return pulumi.get(self, "admin_site_name")

    @property
    @pulumi.getter(name="geoRegion")
    def geo_region(self) -> pulumi.Output[str]:
        """
        Geographical location for the App Service Plan
        """
        return pulumi.get(self, "geo_region")

    @property
    @pulumi.getter(name="hostingEnvironmentProfile")
    def hosting_environment_profile(self) -> pulumi.Output[Optional['outputs.HostingEnvironmentProfileResponse']]:
        """
        Specification for the hosting environment (App Service Environment) to use for the App Service Plan
        """
        return pulumi.get(self, "hosting_environment_profile")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumNumberOfWorkers")
    def maximum_number_of_workers(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum number of instances that can be assigned to this App Service Plan
        """
        return pulumi.get(self, "maximum_number_of_workers")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfSites")
    def number_of_sites(self) -> pulumi.Output[int]:
        """
        Number of web apps assigned to this App Service Plan
        """
        return pulumi.get(self, "number_of_sites")

    @property
    @pulumi.getter(name="perSiteScaling")
    def per_site_scaling(self) -> pulumi.Output[Optional[bool]]:
        """
        If True apps assigned to this App Service Plan can be scaled independently
                    If False apps assigned to this App Service Plan will scale to all instances of the plan
        """
        return pulumi.get(self, "per_site_scaling")

    @property
    @pulumi.getter
    def reserved(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables creation of a Linux App Service Plan
        """
        return pulumi.get(self, "reserved")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[str]:
        """
        Resource group of the server farm
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuDescriptionResponse']]:
        """
        Describes a sku for a scalable resource
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        App Service Plan Status
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subscription(self) -> pulumi.Output[str]:
        """
        App Service Plan Subscription
        """
        return pulumi.get(self, "subscription")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workerTierName")
    def worker_tier_name(self) -> pulumi.Output[Optional[str]]:
        """
        Target worker tier assigned to the App Service Plan
        """
        return pulumi.get(self, "worker_tier_name")

