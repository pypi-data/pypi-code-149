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

__all__ = ['ReportByBillingAccountArgs', 'ReportByBillingAccount']

@pulumi.input_type
class ReportByBillingAccountArgs:
    def __init__(__self__, *,
                 billing_account_id: pulumi.Input[str],
                 definition: pulumi.Input['ReportDefinitionArgs'],
                 delivery_info: pulumi.Input['ReportDeliveryInfoArgs'],
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input['ReportScheduleArgs']] = None):
        """
        The set of arguments for constructing a ReportByBillingAccount resource.
        :param pulumi.Input[str] billing_account_id: BillingAccount ID
        :param pulumi.Input['ReportDefinitionArgs'] definition: Has definition for the report.
        :param pulumi.Input['ReportDeliveryInfoArgs'] delivery_info: Has delivery information for the report.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the report being delivered.
        :param pulumi.Input[str] report_name: Report Name.
        :param pulumi.Input['ReportScheduleArgs'] schedule: Has schedule information for the report.
        """
        pulumi.set(__self__, "billing_account_id", billing_account_id)
        pulumi.set(__self__, "definition", definition)
        pulumi.set(__self__, "delivery_info", delivery_info)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if report_name is not None:
            pulumi.set(__self__, "report_name", report_name)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)

    @property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[str]:
        """
        BillingAccount ID
        """
        return pulumi.get(self, "billing_account_id")

    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account_id", value)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Input['ReportDefinitionArgs']:
        """
        Has definition for the report.
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: pulumi.Input['ReportDefinitionArgs']):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Input['ReportDeliveryInfoArgs']:
        """
        Has delivery information for the report.
        """
        return pulumi.get(self, "delivery_info")

    @delivery_info.setter
    def delivery_info(self, value: pulumi.Input['ReportDeliveryInfoArgs']):
        pulumi.set(self, "delivery_info", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[str, 'FormatType']]]:
        """
        The format of the report being delivered.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[str, 'FormatType']]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter(name="reportName")
    def report_name(self) -> Optional[pulumi.Input[str]]:
        """
        Report Name.
        """
        return pulumi.get(self, "report_name")

    @report_name.setter
    def report_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "report_name", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['ReportScheduleArgs']]:
        """
        Has schedule information for the report.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['ReportScheduleArgs']]):
        pulumi.set(self, "schedule", value)


class ReportByBillingAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ReportDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ReportDeliveryInfoArgs']]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ReportScheduleArgs']]] = None,
                 __props__=None):
        """
        A report resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_account_id: BillingAccount ID
        :param pulumi.Input[pulumi.InputType['ReportDefinitionArgs']] definition: Has definition for the report.
        :param pulumi.Input[pulumi.InputType['ReportDeliveryInfoArgs']] delivery_info: Has delivery information for the report.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the report being delivered.
        :param pulumi.Input[str] report_name: Report Name.
        :param pulumi.Input[pulumi.InputType['ReportScheduleArgs']] schedule: Has schedule information for the report.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReportByBillingAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A report resource.

        :param str resource_name: The name of the resource.
        :param ReportByBillingAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReportByBillingAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ReportDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ReportDeliveryInfoArgs']]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ReportScheduleArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReportByBillingAccountArgs.__new__(ReportByBillingAccountArgs)

            if billing_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account_id'")
            __props__.__dict__["billing_account_id"] = billing_account_id
            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__.__dict__["definition"] = definition
            if delivery_info is None and not opts.urn:
                raise TypeError("Missing required property 'delivery_info'")
            __props__.__dict__["delivery_info"] = delivery_info
            __props__.__dict__["format"] = format
            __props__.__dict__["report_name"] = report_name
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["name"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:ReportByBillingAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ReportByBillingAccount, __self__).__init__(
            'azure-native:costmanagement/v20180801preview:ReportByBillingAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReportByBillingAccount':
        """
        Get an existing ReportByBillingAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReportByBillingAccountArgs.__new__(ReportByBillingAccountArgs)

        __props__.__dict__["definition"] = None
        __props__.__dict__["delivery_info"] = None
        __props__.__dict__["format"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ReportByBillingAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.ReportDefinitionResponse']:
        """
        Has definition for the report.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output['outputs.ReportDeliveryInfoResponse']:
        """
        Has delivery information for the report.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        The format of the report being delivered.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.ReportScheduleResponse']]:
        """
        Has schedule information for the report.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, str]]:
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

