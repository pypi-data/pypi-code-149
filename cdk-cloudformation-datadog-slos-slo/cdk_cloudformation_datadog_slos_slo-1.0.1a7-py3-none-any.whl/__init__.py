'''
# datadog-slos-slo

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Datadog::SLOs::SLO` v1.0.1.

## Description

Datadog SLO 1.0.1

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Datadog::SLOs::SLO \
  --publisher-id 7171b96e5d207b947eb72ca9ce05247c246de623 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/7171b96e5d207b947eb72ca9ce05247c246de623/Datadog-SLOs-SLO \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Datadog::SLOs::SLO`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fdatadog-slos-slo+v1.0.1).
* Issues related to `Datadog::SLOs::SLO` should be reported to the [publisher](undefined).

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


class CfnSlo(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-slos-slo.CfnSlo",
):
    '''A CloudFormation ``Datadog::SLOs::SLO``.

    :cloudformationResource: Datadog::SLOs::SLO
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        thresholds: typing.Sequence[typing.Union["Threshold", typing.Dict[builtins.str, typing.Any]]],
        type: "CfnSloPropsType",
        creator: typing.Optional[typing.Union["Creator", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        query: typing.Optional[typing.Union["Query", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``Datadog::SLOs::SLO``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Name of the slo.
        :param thresholds: 
        :param type: The type of the slo.
        :param creator: 
        :param description: Description of the slo.
        :param groups: A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.
        :param monitor_ids: A list of monitor ids that defines the scope of a monitor service level objective. Required if type is monitor.
        :param query: 
        :param tags: Tags associated with the slo.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f02aecf56346194619959eeb642dd0cedce3f2340febf08bfde7c407d50c703)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSloProps(
            name=name,
            thresholds=thresholds,
            type=type,
            creator=creator,
            description=description,
            groups=groups,
            monitor_ids=monitor_ids,
            query=query,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreated")
    def attr_created(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Created``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreated"))

    @builtins.property
    @jsii.member(jsii_name="attrDeleted")
    def attr_deleted(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Deleted``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeleted"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrModified")
    def attr_modified(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Modified``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModified"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnSloProps":
        '''Resource props.'''
        return typing.cast("CfnSloProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.CfnSloProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "thresholds": "thresholds",
        "type": "type",
        "creator": "creator",
        "description": "description",
        "groups": "groups",
        "monitor_ids": "monitorIds",
        "query": "query",
        "tags": "tags",
    },
)
class CfnSloProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        thresholds: typing.Sequence[typing.Union["Threshold", typing.Dict[builtins.str, typing.Any]]],
        type: "CfnSloPropsType",
        creator: typing.Optional[typing.Union["Creator", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        query: typing.Optional[typing.Union["Query", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Datadog SLO 1.0.1.

        :param name: Name of the slo.
        :param thresholds: 
        :param type: The type of the slo.
        :param creator: 
        :param description: Description of the slo.
        :param groups: A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.
        :param monitor_ids: A list of monitor ids that defines the scope of a monitor service level objective. Required if type is monitor.
        :param query: 
        :param tags: Tags associated with the slo.

        :schema: CfnSloProps
        '''
        if isinstance(creator, dict):
            creator = Creator(**creator)
        if isinstance(query, dict):
            query = Query(**query)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2654aba5ca9c9d80f79bdd82ea42ecd7472e5405aec8abd2c59b93f3a4408cd5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thresholds", value=thresholds, expected_type=type_hints["thresholds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument creator", value=creator, expected_type=type_hints["creator"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument monitor_ids", value=monitor_ids, expected_type=type_hints["monitor_ids"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "thresholds": thresholds,
            "type": type,
        }
        if creator is not None:
            self._values["creator"] = creator
        if description is not None:
            self._values["description"] = description
        if groups is not None:
            self._values["groups"] = groups
        if monitor_ids is not None:
            self._values["monitor_ids"] = monitor_ids
        if query is not None:
            self._values["query"] = query
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the slo.

        :schema: CfnSloProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thresholds(self) -> typing.List["Threshold"]:
        '''
        :schema: CfnSloProps#Thresholds
        '''
        result = self._values.get("thresholds")
        assert result is not None, "Required property 'thresholds' is missing"
        return typing.cast(typing.List["Threshold"], result)

    @builtins.property
    def type(self) -> "CfnSloPropsType":
        '''The type of the slo.

        :schema: CfnSloProps#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("CfnSloPropsType", result)

    @builtins.property
    def creator(self) -> typing.Optional["Creator"]:
        '''
        :schema: CfnSloProps#Creator
        '''
        result = self._values.get("creator")
        return typing.cast(typing.Optional["Creator"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the slo.

        :schema: CfnSloProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.

        :schema: CfnSloProps#Groups
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def monitor_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of monitor ids that defines the scope of a monitor service level objective.

        Required if type is monitor.

        :schema: CfnSloProps#MonitorIds
        '''
        result = self._values.get("monitor_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def query(self) -> typing.Optional["Query"]:
        '''
        :schema: CfnSloProps#Query
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional["Query"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags associated with the slo.

        :schema: CfnSloProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSloProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/datadog-slos-slo.CfnSloPropsType")
class CfnSloPropsType(enum.Enum):
    '''The type of the slo.

    :schema: CfnSloPropsType
    '''

    MONITOR = "MONITOR"
    '''monitor.'''
    METRIC = "METRIC"
    '''metric.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.Creator",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "handle": "handle", "name": "name"},
)
class Creator:
    def __init__(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
        handle: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Email of the creator of the slo.
        :param handle: Handle of the creator of the slo.
        :param name: Name of the creator of the slo.

        :schema: Creator
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e864eaf705eb5254cc1f399ea9ee013f01b8b7b4b50323ef3cc370ca48f95add)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument handle", value=handle, expected_type=type_hints["handle"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if handle is not None:
            self._values["handle"] = handle
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Email of the creator of the slo.

        :schema: Creator#Email
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def handle(self) -> typing.Optional[builtins.str]:
        '''Handle of the creator of the slo.

        :schema: Creator#Handle
        '''
        result = self._values.get("handle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the creator of the slo.

        :schema: Creator#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Creator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.Query",
    jsii_struct_bases=[],
    name_mapping={"denominator": "denominator", "numerator": "numerator"},
)
class Query:
    def __init__(
        self,
        *,
        denominator: typing.Optional[builtins.str] = None,
        numerator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param denominator: A Datadog metric query for good events.
        :param numerator: A Datadog metric query for total (valid) events.

        :schema: Query
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a548b00c201b816ae18ae30aa7896c96f2f7655c322e74f5b9206820d815f25)
            check_type(argname="argument denominator", value=denominator, expected_type=type_hints["denominator"])
            check_type(argname="argument numerator", value=numerator, expected_type=type_hints["numerator"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if denominator is not None:
            self._values["denominator"] = denominator
        if numerator is not None:
            self._values["numerator"] = numerator

    @builtins.property
    def denominator(self) -> typing.Optional[builtins.str]:
        '''A Datadog metric query for good events.

        :schema: Query#Denominator
        '''
        result = self._values.get("denominator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def numerator(self) -> typing.Optional[builtins.str]:
        '''A Datadog metric query for total (valid) events.

        :schema: Query#Numerator
        '''
        result = self._values.get("numerator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Query(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.Threshold",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "target_display": "targetDisplay",
        "timeframe": "timeframe",
        "warning": "warning",
        "warning_display": "warningDisplay",
    },
)
class Threshold:
    def __init__(
        self,
        *,
        target: typing.Optional[jsii.Number] = None,
        target_display: typing.Optional[builtins.str] = None,
        timeframe: typing.Optional["ThresholdTimeframe"] = None,
        warning: typing.Optional[jsii.Number] = None,
        warning_display: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The target value for the service level indicator within the corresponding timeframe.
        :param target_display: A string representation of the target that indicates its precision.(e.g. 98.00).
        :param timeframe: The SLO time window options. Allowed enum values: 7d,30d,90d
        :param warning: The warning value for the service level objective.
        :param warning_display: A string representation of the warning target.(e.g. 98.00).

        :schema: Threshold
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4610483d1183c8c0284f69fea7495cd6d10b38da3c640528dac5be79f9847f)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument target_display", value=target_display, expected_type=type_hints["target_display"])
            check_type(argname="argument timeframe", value=timeframe, expected_type=type_hints["timeframe"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
            check_type(argname="argument warning_display", value=warning_display, expected_type=type_hints["warning_display"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if target is not None:
            self._values["target"] = target
        if target_display is not None:
            self._values["target_display"] = target_display
        if timeframe is not None:
            self._values["timeframe"] = timeframe
        if warning is not None:
            self._values["warning"] = warning
        if warning_display is not None:
            self._values["warning_display"] = warning_display

    @builtins.property
    def target(self) -> typing.Optional[jsii.Number]:
        '''The target value for the service level indicator within the corresponding timeframe.

        :schema: Threshold#Target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_display(self) -> typing.Optional[builtins.str]:
        '''A string representation of the target that indicates its precision.(e.g. 98.00).

        :schema: Threshold#TargetDisplay
        '''
        result = self._values.get("target_display")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeframe(self) -> typing.Optional["ThresholdTimeframe"]:
        '''The SLO time window options.

        Allowed enum values: 7d,30d,90d

        :schema: Threshold#Timeframe
        '''
        result = self._values.get("timeframe")
        return typing.cast(typing.Optional["ThresholdTimeframe"], result)

    @builtins.property
    def warning(self) -> typing.Optional[jsii.Number]:
        '''The warning value for the service level objective.

        :schema: Threshold#Warning
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warning_display(self) -> typing.Optional[builtins.str]:
        '''A string representation of the warning target.(e.g. 98.00).

        :schema: Threshold#WarningDisplay
        '''
        result = self._values.get("warning_display")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Threshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/datadog-slos-slo.ThresholdTimeframe")
class ThresholdTimeframe(enum.Enum):
    '''The SLO time window options.

    Allowed enum values: 7d,30d,90d

    :schema: ThresholdTimeframe
    '''

    VALUE_7D = "VALUE_7D"
    '''7d.'''
    VALUE_30D = "VALUE_30D"
    '''30d.'''
    VALUE_90D = "VALUE_90D"
    '''90d.'''


__all__ = [
    "CfnSlo",
    "CfnSloProps",
    "CfnSloPropsType",
    "Creator",
    "Query",
    "Threshold",
    "ThresholdTimeframe",
]

publication.publish()

def _typecheckingstub__8f02aecf56346194619959eeb642dd0cedce3f2340febf08bfde7c407d50c703(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    thresholds: typing.Sequence[typing.Union[Threshold, typing.Dict[builtins.str, typing.Any]]],
    type: CfnSloPropsType,
    creator: typing.Optional[typing.Union[Creator, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    query: typing.Optional[typing.Union[Query, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2654aba5ca9c9d80f79bdd82ea42ecd7472e5405aec8abd2c59b93f3a4408cd5(
    *,
    name: builtins.str,
    thresholds: typing.Sequence[typing.Union[Threshold, typing.Dict[builtins.str, typing.Any]]],
    type: CfnSloPropsType,
    creator: typing.Optional[typing.Union[Creator, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    query: typing.Optional[typing.Union[Query, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e864eaf705eb5254cc1f399ea9ee013f01b8b7b4b50323ef3cc370ca48f95add(
    *,
    email: typing.Optional[builtins.str] = None,
    handle: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a548b00c201b816ae18ae30aa7896c96f2f7655c322e74f5b9206820d815f25(
    *,
    denominator: typing.Optional[builtins.str] = None,
    numerator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4610483d1183c8c0284f69fea7495cd6d10b38da3c640528dac5be79f9847f(
    *,
    target: typing.Optional[jsii.Number] = None,
    target_display: typing.Optional[builtins.str] = None,
    timeframe: typing.Optional[ThresholdTimeframe] = None,
    warning: typing.Optional[jsii.Number] = None,
    warning_display: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
