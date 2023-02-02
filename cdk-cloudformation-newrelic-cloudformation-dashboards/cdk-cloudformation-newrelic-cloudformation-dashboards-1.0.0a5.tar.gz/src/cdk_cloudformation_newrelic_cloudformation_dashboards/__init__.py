'''
# newrelic-cloudformation-dashboards

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `newrelic::cloudformation::dashboards` v1.0.0.

## Description

CRUDL operations for New Relic Dashboards via the NerdGraph API

## References

* [Source](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name newrelic::cloudformation::dashboards \
  --publisher-id 759f81f13de188bad7cafc8a2d50910f7d5e2bcc \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/759f81f13de188bad7cafc8a2d50910f7d5e2bcc/newrelic-cloudformation-dashboards \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `newrelic::cloudformation::dashboards`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fnewrelic-cloudformation-dashboards+v1.0.0).
* Issues related to `newrelic::cloudformation::dashboards` should be reported to the [publisher](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnDashboards(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/newrelic-cloudformation-dashboards.CfnDashboards",
):
    '''A CloudFormation ``newrelic::cloudformation::dashboards``.

    :cloudformationResource: newrelic::cloudformation::dashboards
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        dashboard_input: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        list_query_filter: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        variables: typing.Any = None,
    ) -> None:
        '''Create a new ``newrelic::cloudformation::dashboards``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_key: 
        :param dashboard_input: 
        :param account_id: 
        :param endpoint: 
        :param list_query_filter: 
        :param tags: 
        :param variables: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21cb6797e49e1137fa0ebcb49086f9fd553b47d10763ee4ac8d8ffcb03a934ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDashboardsProps(
            api_key=api_key,
            dashboard_input=dashboard_input,
            account_id=account_id,
            endpoint=endpoint,
            list_query_filter=list_query_filter,
            tags=tags,
            variables=variables,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGuid")
    def attr_guid(self) -> builtins.str:
        '''Attribute ``newrelic::cloudformation::dashboards.Guid``.

        :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGuid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDashboardsProps":
        '''Resource props.'''
        return typing.cast("CfnDashboardsProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/newrelic-cloudformation-dashboards.CfnDashboardsProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "dashboard_input": "dashboardInput",
        "account_id": "accountId",
        "endpoint": "endpoint",
        "list_query_filter": "listQueryFilter",
        "tags": "tags",
        "variables": "variables",
    },
)
class CfnDashboardsProps:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        dashboard_input: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        list_query_filter: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        variables: typing.Any = None,
    ) -> None:
        '''CRUDL operations for New Relic Dashboards via the NerdGraph API.

        :param api_key: 
        :param dashboard_input: 
        :param account_id: 
        :param endpoint: 
        :param list_query_filter: 
        :param tags: 
        :param variables: 

        :schema: CfnDashboardsProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94219d4b7d0cf977025ee4c2524686712142f4b2ac40c09046fd54da1f828294)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument dashboard_input", value=dashboard_input, expected_type=type_hints["dashboard_input"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument list_query_filter", value=list_query_filter, expected_type=type_hints["list_query_filter"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "dashboard_input": dashboard_input,
        }
        if account_id is not None:
            self._values["account_id"] = account_id
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if list_query_filter is not None:
            self._values["list_query_filter"] = list_query_filter
        if tags is not None:
            self._values["tags"] = tags
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def api_key(self) -> builtins.str:
        '''
        :schema: CfnDashboardsProps#APIKey
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_input(self) -> builtins.str:
        '''
        :schema: CfnDashboardsProps#DashboardInput
        '''
        result = self._values.get("dashboard_input")
        assert result is not None, "Required property 'dashboard_input' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDashboardsProps#AccountID
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDashboardsProps#Endpoint
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def list_query_filter(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDashboardsProps#ListQueryFilter
        '''
        result = self._values.get("list_query_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''
        :schema: CfnDashboardsProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def variables(self) -> typing.Any:
        '''
        :schema: CfnDashboardsProps#Variables
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDashboards",
    "CfnDashboardsProps",
]

publication.publish()

def _typecheckingstub__21cb6797e49e1137fa0ebcb49086f9fd553b47d10763ee4ac8d8ffcb03a934ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key: builtins.str,
    dashboard_input: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    list_query_filter: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    variables: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94219d4b7d0cf977025ee4c2524686712142f4b2ac40c09046fd54da1f828294(
    *,
    api_key: builtins.str,
    dashboard_input: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    list_query_filter: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    variables: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass
