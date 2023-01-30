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

__all__ = [
    'GetHyperVSiteResult',
    'AwaitableGetHyperVSiteResult',
    'get_hyper_v_site',
    'get_hyper_v_site_output',
]

@pulumi.output_type
class GetHyperVSiteResult:
    """
    Site REST Resource.
    """
    def __init__(__self__, e_tag=None, id=None, location=None, name=None, properties=None, tags=None, type=None):
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        eTag for concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Azure location in which Sites is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the Hyper-V site.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.SitePropertiesResponse':
        """
        Nested properties of Hyper-V site.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of resource. Type = Microsoft.OffAzure/HyperVSites.
        """
        return pulumi.get(self, "type")


class AwaitableGetHyperVSiteResult(GetHyperVSiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHyperVSiteResult(
            e_tag=self.e_tag,
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            tags=self.tags,
            type=self.type)


def get_hyper_v_site(resource_group_name: Optional[str] = None,
                     site_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHyperVSiteResult:
    """
    Site REST Resource.
    API Version: 2020-01-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['siteName'] = site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:offazure:getHyperVSite', __args__, opts=opts, typ=GetHyperVSiteResult).value

    return AwaitableGetHyperVSiteResult(
        e_tag=__ret__.e_tag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        properties=__ret__.properties,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_hyper_v_site)
def get_hyper_v_site_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            site_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHyperVSiteResult]:
    """
    Site REST Resource.
    API Version: 2020-01-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name.
    """
    ...
