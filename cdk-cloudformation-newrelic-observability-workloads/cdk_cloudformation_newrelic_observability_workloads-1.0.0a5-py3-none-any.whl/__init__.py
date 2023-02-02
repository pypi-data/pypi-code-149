'''
# newrelic-observability-workloads

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `NewRelic::Observability::Workloads` v1.0.0.

## Description

CRUD operations for New Relic Workloads via the NerdGraph API

## References

* [Source](https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-workloads)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name NewRelic::Observability::Workloads \
  --publisher-id 759f81f13de188bad7cafc8a2d50910f7d5e2bcc \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/759f81f13de188bad7cafc8a2d50910f7d5e2bcc/NewRelic-Observability-Workloads \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `NewRelic::Observability::Workloads`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fnewrelic-observability-workloads+v1.0.0).
* Issues related to `NewRelic::Observability::Workloads` should be reported to the [publisher](https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-workloads).

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


class CfnWorkloads(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/newrelic-observability-workloads.CfnWorkloads",
):
    '''A CloudFormation ``NewRelic::Observability::Workloads``.

    :cloudformationResource: NewRelic::Observability::Workloads
    :link: https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-workloads
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        duplicate_name: typing.Optional[builtins.str] = None,
        list_query_filter: typing.Optional[builtins.str] = None,
        source_guid: typing.Optional[builtins.str] = None,
        variables: typing.Any = None,
        workload: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``NewRelic::Observability::Workloads``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param duplicate_name: 
        :param list_query_filter: 
        :param source_guid: 
        :param variables: 
        :param workload: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84822ac3c31b0d667a407c07951ba064e049dc2d6db5015d05df2378f09702df)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkloadsProps(
            duplicate_name=duplicate_name,
            list_query_filter=list_query_filter,
            source_guid=source_guid,
            variables=variables,
            workload=workload,
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
        '''Attribute ``NewRelic::Observability::Workloads.Guid``.

        :link: https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-workloads
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGuid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnWorkloadsProps":
        '''Resource props.'''
        return typing.cast("CfnWorkloadsProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/newrelic-observability-workloads.CfnWorkloadsProps",
    jsii_struct_bases=[],
    name_mapping={
        "duplicate_name": "duplicateName",
        "list_query_filter": "listQueryFilter",
        "source_guid": "sourceGuid",
        "variables": "variables",
        "workload": "workload",
    },
)
class CfnWorkloadsProps:
    def __init__(
        self,
        *,
        duplicate_name: typing.Optional[builtins.str] = None,
        list_query_filter: typing.Optional[builtins.str] = None,
        source_guid: typing.Optional[builtins.str] = None,
        variables: typing.Any = None,
        workload: typing.Optional[builtins.str] = None,
    ) -> None:
        '''CRUD operations for New Relic Workloads via the NerdGraph API.

        :param duplicate_name: 
        :param list_query_filter: 
        :param source_guid: 
        :param variables: 
        :param workload: 

        :schema: CfnWorkloadsProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__282ab5bf2b30c52830b65bfbbec7234cd95397e6f378010a0ab8fbffca622624)
            check_type(argname="argument duplicate_name", value=duplicate_name, expected_type=type_hints["duplicate_name"])
            check_type(argname="argument list_query_filter", value=list_query_filter, expected_type=type_hints["list_query_filter"])
            check_type(argname="argument source_guid", value=source_guid, expected_type=type_hints["source_guid"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            check_type(argname="argument workload", value=workload, expected_type=type_hints["workload"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if duplicate_name is not None:
            self._values["duplicate_name"] = duplicate_name
        if list_query_filter is not None:
            self._values["list_query_filter"] = list_query_filter
        if source_guid is not None:
            self._values["source_guid"] = source_guid
        if variables is not None:
            self._values["variables"] = variables
        if workload is not None:
            self._values["workload"] = workload

    @builtins.property
    def duplicate_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnWorkloadsProps#DuplicateName
        '''
        result = self._values.get("duplicate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def list_query_filter(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnWorkloadsProps#ListQueryFilter
        '''
        result = self._values.get("list_query_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_guid(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnWorkloadsProps#SourceGuid
        '''
        result = self._values.get("source_guid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variables(self) -> typing.Any:
        '''
        :schema: CfnWorkloadsProps#Variables
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Any, result)

    @builtins.property
    def workload(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnWorkloadsProps#Workload
        '''
        result = self._values.get("workload")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkloadsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnWorkloads",
    "CfnWorkloadsProps",
]

publication.publish()

def _typecheckingstub__84822ac3c31b0d667a407c07951ba064e049dc2d6db5015d05df2378f09702df(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    duplicate_name: typing.Optional[builtins.str] = None,
    list_query_filter: typing.Optional[builtins.str] = None,
    source_guid: typing.Optional[builtins.str] = None,
    variables: typing.Any = None,
    workload: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282ab5bf2b30c52830b65bfbbec7234cd95397e6f378010a0ab8fbffca622624(
    *,
    duplicate_name: typing.Optional[builtins.str] = None,
    list_query_filter: typing.Optional[builtins.str] = None,
    source_guid: typing.Optional[builtins.str] = None,
    variables: typing.Any = None,
    workload: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
