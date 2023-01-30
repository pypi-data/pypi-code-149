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

__all__ = ['AutomationRuleArgs', 'AutomationRule']

@pulumi.input_type
class AutomationRuleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input[Union['AutomationRuleModifyPropertiesActionArgs', 'AutomationRuleRunPlaybookActionArgs']]]],
                 display_name: pulumi.Input[str],
                 order: pulumi.Input[int],
                 resource_group_name: pulumi.Input[str],
                 triggering_logic: pulumi.Input['AutomationRuleTriggeringLogicArgs'],
                 workspace_name: pulumi.Input[str],
                 automation_rule_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AutomationRule resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['AutomationRuleModifyPropertiesActionArgs', 'AutomationRuleRunPlaybookActionArgs']]]] actions: The actions to execute when the automation rule is triggered
        :param pulumi.Input[str] display_name: The display name of the automation rule
        :param pulumi.Input[int] order: The order of execution of the automation rule
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['AutomationRuleTriggeringLogicArgs'] triggering_logic: Describes automation rule triggering logic
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] automation_rule_id: Automation rule ID
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "triggering_logic", triggering_logic)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if automation_rule_id is not None:
            pulumi.set(__self__, "automation_rule_id", automation_rule_id)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[Union['AutomationRuleModifyPropertiesActionArgs', 'AutomationRuleRunPlaybookActionArgs']]]]:
        """
        The actions to execute when the automation rule is triggered
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[Union['AutomationRuleModifyPropertiesActionArgs', 'AutomationRuleRunPlaybookActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the automation rule
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        The order of execution of the automation rule
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="triggeringLogic")
    def triggering_logic(self) -> pulumi.Input['AutomationRuleTriggeringLogicArgs']:
        """
        Describes automation rule triggering logic
        """
        return pulumi.get(self, "triggering_logic")

    @triggering_logic.setter
    def triggering_logic(self, value: pulumi.Input['AutomationRuleTriggeringLogicArgs']):
        pulumi.set(self, "triggering_logic", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="automationRuleId")
    def automation_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        Automation rule ID
        """
        return pulumi.get(self, "automation_rule_id")

    @automation_rule_id.setter
    def automation_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "automation_rule_id", value)


class AutomationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AutomationRuleModifyPropertiesActionArgs'], pulumi.InputType['AutomationRuleRunPlaybookActionArgs']]]]]] = None,
                 automation_rule_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 triggering_logic: Optional[pulumi.Input[pulumi.InputType['AutomationRuleTriggeringLogicArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AutomationRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AutomationRuleModifyPropertiesActionArgs'], pulumi.InputType['AutomationRuleRunPlaybookActionArgs']]]]] actions: The actions to execute when the automation rule is triggered
        :param pulumi.Input[str] automation_rule_id: Automation rule ID
        :param pulumi.Input[str] display_name: The display name of the automation rule
        :param pulumi.Input[int] order: The order of execution of the automation rule
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['AutomationRuleTriggeringLogicArgs']] triggering_logic: Describes automation rule triggering logic
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutomationRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AutomationRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AutomationRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutomationRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AutomationRuleModifyPropertiesActionArgs'], pulumi.InputType['AutomationRuleRunPlaybookActionArgs']]]]]] = None,
                 automation_rule_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 triggering_logic: Optional[pulumi.Input[pulumi.InputType['AutomationRuleTriggeringLogicArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AutomationRuleArgs.__new__(AutomationRuleArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["automation_rule_id"] = automation_rule_id
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if order is None and not opts.urn:
                raise TypeError("Missing required property 'order'")
            __props__.__dict__["order"] = order
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if triggering_logic is None and not opts.urn:
                raise TypeError("Missing required property 'triggering_logic'")
            __props__.__dict__["triggering_logic"] = triggering_logic
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["created_by"] = None
            __props__.__dict__["created_time_utc"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_modified_by"] = None
            __props__.__dict__["last_modified_time_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:AutomationRule"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:AutomationRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AutomationRule, __self__).__init__(
            'azure-native:securityinsights/v20220801:AutomationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AutomationRule':
        """
        Get an existing AutomationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AutomationRuleArgs.__new__(AutomationRuleArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_time_utc"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_time_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["order"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["triggering_logic"] = None
        __props__.__dict__["type"] = None
        return AutomationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[Any]]:
        """
        The actions to execute when the automation rule is triggered
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output['outputs.ClientInfoResponse']:
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[str]:
        """
        The time the automation rule was created
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the automation rule
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output['outputs.ClientInfoResponse']:
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[str]:
        """
        The last time the automation rule was updated
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[int]:
        """
        The order of execution of the automation rule
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="triggeringLogic")
    def triggering_logic(self) -> pulumi.Output['outputs.AutomationRuleTriggeringLogicResponse']:
        """
        Describes automation rule triggering logic
        """
        return pulumi.get(self, "triggering_logic")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

