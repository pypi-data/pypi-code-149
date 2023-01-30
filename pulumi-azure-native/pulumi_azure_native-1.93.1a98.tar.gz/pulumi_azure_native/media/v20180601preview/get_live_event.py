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
    'GetLiveEventResult',
    'AwaitableGetLiveEventResult',
    'get_live_event',
    'get_live_event_output',
]

@pulumi.output_type
class GetLiveEventResult:
    """
    The Live Event.
    """
    def __init__(__self__, created=None, cross_site_access_policies=None, description=None, encoding=None, id=None, input=None, last_modified=None, location=None, name=None, preview=None, provisioning_state=None, resource_state=None, stream_options=None, tags=None, type=None, vanity_url=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if cross_site_access_policies and not isinstance(cross_site_access_policies, dict):
            raise TypeError("Expected argument 'cross_site_access_policies' to be a dict")
        pulumi.set(__self__, "cross_site_access_policies", cross_site_access_policies)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encoding and not isinstance(encoding, dict):
            raise TypeError("Expected argument 'encoding' to be a dict")
        pulumi.set(__self__, "encoding", encoding)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if input and not isinstance(input, dict):
            raise TypeError("Expected argument 'input' to be a dict")
        pulumi.set(__self__, "input", input)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if preview and not isinstance(preview, dict):
            raise TypeError("Expected argument 'preview' to be a dict")
        pulumi.set(__self__, "preview", preview)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if stream_options and not isinstance(stream_options, list):
            raise TypeError("Expected argument 'stream_options' to be a list")
        pulumi.set(__self__, "stream_options", stream_options)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vanity_url and not isinstance(vanity_url, bool):
            raise TypeError("Expected argument 'vanity_url' to be a bool")
        pulumi.set(__self__, "vanity_url", vanity_url)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The exact time the Live Event was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="crossSiteAccessPolicies")
    def cross_site_access_policies(self) -> Optional['outputs.CrossSiteAccessPoliciesResponse']:
        """
        The Live Event access policies.
        """
        return pulumi.get(self, "cross_site_access_policies")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The Live Event description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encoding(self) -> Optional['outputs.LiveEventEncodingResponse']:
        """
        The Live Event encoding.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def input(self) -> 'outputs.LiveEventInputResponse':
        """
        The Live Event input.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The exact time the Live Event was last modified.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The Azure Region of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def preview(self) -> Optional['outputs.LiveEventPreviewResponse']:
        """
        The Live Event preview.
        """
        return pulumi.get(self, "preview")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the Live Event.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        The resource state of the Live Event.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="streamOptions")
    def stream_options(self) -> Optional[Sequence[str]]:
        """
        The stream options.
        """
        return pulumi.get(self, "stream_options")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vanityUrl")
    def vanity_url(self) -> Optional[bool]:
        """
        The Live Event vanity URL flag.
        """
        return pulumi.get(self, "vanity_url")


class AwaitableGetLiveEventResult(GetLiveEventResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLiveEventResult(
            created=self.created,
            cross_site_access_policies=self.cross_site_access_policies,
            description=self.description,
            encoding=self.encoding,
            id=self.id,
            input=self.input,
            last_modified=self.last_modified,
            location=self.location,
            name=self.name,
            preview=self.preview,
            provisioning_state=self.provisioning_state,
            resource_state=self.resource_state,
            stream_options=self.stream_options,
            tags=self.tags,
            type=self.type,
            vanity_url=self.vanity_url)


def get_live_event(account_name: Optional[str] = None,
                   live_event_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLiveEventResult:
    """
    The Live Event.


    :param str account_name: The Media Services account name.
    :param str live_event_name: The name of the Live Event.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['liveEventName'] = live_event_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20180601preview:getLiveEvent', __args__, opts=opts, typ=GetLiveEventResult).value

    return AwaitableGetLiveEventResult(
        created=__ret__.created,
        cross_site_access_policies=__ret__.cross_site_access_policies,
        description=__ret__.description,
        encoding=__ret__.encoding,
        id=__ret__.id,
        input=__ret__.input,
        last_modified=__ret__.last_modified,
        location=__ret__.location,
        name=__ret__.name,
        preview=__ret__.preview,
        provisioning_state=__ret__.provisioning_state,
        resource_state=__ret__.resource_state,
        stream_options=__ret__.stream_options,
        tags=__ret__.tags,
        type=__ret__.type,
        vanity_url=__ret__.vanity_url)


@_utilities.lift_output_func(get_live_event)
def get_live_event_output(account_name: Optional[pulumi.Input[str]] = None,
                          live_event_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLiveEventResult]:
    """
    The Live Event.


    :param str account_name: The Media Services account name.
    :param str live_event_name: The name of the Live Event.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    ...
