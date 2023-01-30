# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetLSSConfigControllerResult',
    'AwaitableGetLSSConfigControllerResult',
    'get_lss_config_controller',
    'get_lss_config_controller_output',
]

@pulumi.output_type
class GetLSSConfigControllerResult:
    """
    A collection of values returned by getLSSConfigController.
    """
    def __init__(__self__, configs=None, connector_groups=None, id=None, policy_rules=None):
        if configs and not isinstance(configs, list):
            raise TypeError("Expected argument 'configs' to be a list")
        pulumi.set(__self__, "configs", configs)
        if connector_groups and not isinstance(connector_groups, list):
            raise TypeError("Expected argument 'connector_groups' to be a list")
        pulumi.set(__self__, "connector_groups", connector_groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_rules and not isinstance(policy_rules, list):
            raise TypeError("Expected argument 'policy_rules' to be a list")
        pulumi.set(__self__, "policy_rules", policy_rules)

    @property
    @pulumi.getter
    def configs(self) -> Sequence['outputs.GetLSSConfigControllerConfigResult']:
        """
        (Computed)
        """
        return pulumi.get(self, "configs")

    @property
    @pulumi.getter(name="connectorGroups")
    def connector_groups(self) -> Sequence['outputs.GetLSSConfigControllerConnectorGroupResult']:
        """
        (Computed)
        """
        return pulumi.get(self, "connector_groups")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        (string)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyRules")
    def policy_rules(self) -> Sequence['outputs.GetLSSConfigControllerPolicyRuleResult']:
        return pulumi.get(self, "policy_rules")


class AwaitableGetLSSConfigControllerResult(GetLSSConfigControllerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLSSConfigControllerResult(
            configs=self.configs,
            connector_groups=self.connector_groups,
            id=self.id,
            policy_rules=self.policy_rules)


def get_lss_config_controller(configs: Optional[Sequence[pulumi.InputType['GetLSSConfigControllerConfigArgs']]] = None,
                              id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLSSConfigControllerResult:
    """
    Use the **zpa_lss_config_controller** data source to get information about a Log Streaming (LSS) configuration resource created in the Zscaler Private Access.


    :param Sequence[pulumi.InputType['GetLSSConfigControllerConfigArgs']] configs: (Computed)
    :param str id: This field defines the name of the log streaming resource.
    """
    __args__ = dict()
    __args__['configs'] = configs
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('zpa:LSSConfig/getLSSConfigController:getLSSConfigController', __args__, opts=opts, typ=GetLSSConfigControllerResult).value

    return AwaitableGetLSSConfigControllerResult(
        configs=__ret__.configs,
        connector_groups=__ret__.connector_groups,
        id=__ret__.id,
        policy_rules=__ret__.policy_rules)


@_utilities.lift_output_func(get_lss_config_controller)
def get_lss_config_controller_output(configs: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetLSSConfigControllerConfigArgs']]]]] = None,
                                     id: Optional[pulumi.Input[Optional[str]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLSSConfigControllerResult]:
    """
    Use the **zpa_lss_config_controller** data source to get information about a Log Streaming (LSS) configuration resource created in the Zscaler Private Access.


    :param Sequence[pulumi.InputType['GetLSSConfigControllerConfigArgs']] configs: (Computed)
    :param str id: This field defines the name of the log streaming resource.
    """
    ...
