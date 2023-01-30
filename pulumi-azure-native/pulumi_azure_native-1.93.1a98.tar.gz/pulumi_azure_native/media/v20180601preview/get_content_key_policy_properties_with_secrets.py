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
    'GetContentKeyPolicyPropertiesWithSecretsResult',
    'AwaitableGetContentKeyPolicyPropertiesWithSecretsResult',
    'get_content_key_policy_properties_with_secrets',
    'get_content_key_policy_properties_with_secrets_output',
]

@pulumi.output_type
class GetContentKeyPolicyPropertiesWithSecretsResult:
    """
    The properties of the Content Key Policy.
    """
    def __init__(__self__, created=None, description=None, last_modified=None, options=None, policy_id=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if options and not isinstance(options, list):
            raise TypeError("Expected argument 'options' to be a list")
        pulumi.set(__self__, "options", options)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The creation date of the Policy
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The last modified date of the Policy
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def options(self) -> Sequence['outputs.ContentKeyPolicyOptionResponse']:
        """
        The Key Policy options.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> str:
        """
        The legacy Policy ID.
        """
        return pulumi.get(self, "policy_id")


class AwaitableGetContentKeyPolicyPropertiesWithSecretsResult(GetContentKeyPolicyPropertiesWithSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContentKeyPolicyPropertiesWithSecretsResult(
            created=self.created,
            description=self.description,
            last_modified=self.last_modified,
            options=self.options,
            policy_id=self.policy_id)


def get_content_key_policy_properties_with_secrets(account_name: Optional[str] = None,
                                                   content_key_policy_name: Optional[str] = None,
                                                   resource_group_name: Optional[str] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContentKeyPolicyPropertiesWithSecretsResult:
    """
    The properties of the Content Key Policy.


    :param str account_name: The Media Services account name.
    :param str content_key_policy_name: The Content Key Policy name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['contentKeyPolicyName'] = content_key_policy_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20180601preview:getContentKeyPolicyPropertiesWithSecrets', __args__, opts=opts, typ=GetContentKeyPolicyPropertiesWithSecretsResult).value

    return AwaitableGetContentKeyPolicyPropertiesWithSecretsResult(
        created=__ret__.created,
        description=__ret__.description,
        last_modified=__ret__.last_modified,
        options=__ret__.options,
        policy_id=__ret__.policy_id)


@_utilities.lift_output_func(get_content_key_policy_properties_with_secrets)
def get_content_key_policy_properties_with_secrets_output(account_name: Optional[pulumi.Input[str]] = None,
                                                          content_key_policy_name: Optional[pulumi.Input[str]] = None,
                                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContentKeyPolicyPropertiesWithSecretsResult]:
    """
    The properties of the Content Key Policy.


    :param str account_name: The Media Services account name.
    :param str content_key_policy_name: The Content Key Policy name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    ...
