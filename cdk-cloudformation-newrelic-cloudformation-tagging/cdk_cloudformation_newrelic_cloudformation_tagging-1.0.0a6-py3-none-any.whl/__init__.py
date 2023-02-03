'''
# newrelic-cloudformation-tagging

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `newrelic::cloudformation::tagging` v1.0.0.

## Description

CRUD operations for New Relic Tags via the NerdGraph API

## References

* [Source](https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-tagging.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name newrelic::cloudformation::tagging \
  --publisher-id 759f81f13de188bad7cafc8a2d50910f7d5e2bcc \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/759f81f13de188bad7cafc8a2d50910f7d5e2bcc/newrelic-cloudformation-tagging \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `newrelic::cloudformation::tagging`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fnewrelic-cloudformation-tagging+v1.0.0).
* Issues related to `newrelic::cloudformation::tagging` should be reported to the [publisher](https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-tagging.git).

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


class CfnTagging(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/newrelic-cloudformation-tagging.CfnTagging",
):
    '''A CloudFormation ``newrelic::cloudformation::tagging``.

    :cloudformationResource: newrelic::cloudformation::tagging
    :link: https://github.com/newrelic-experimental/newrelic-cloudformation-resource-providers-tagging.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        entity_guid: builtins.str,
        tags: typing.Sequence[typing.Union["TagObject", typing.Dict[builtins.str, typing.Any]]],
        endpoint: typing.Optional[builtins.str] = None,
        guid: typing.Optional[builtins.str] = None,
        list_query_filter: typing.Optional[builtins.str] = None,
        semantics: typing.Optional[builtins.str] = None,
        variables: typing.Any = None,
    ) -> None:
        '''Create a new ``newrelic::cloudformation::tagging``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_key: 
        :param entity_guid: 
        :param tags: 
        :param endpoint: 
        :param guid: 
        :param list_query_filter: 
        :param semantics: 
        :param variables: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a1da37fd8597ee84b5a5750dbf93fe2c17ae76d0d36f10e00b7d2b9779ccdd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTaggingProps(
            api_key=api_key,
            entity_guid=entity_guid,
            tags=tags,
            endpoint=endpoint,
            guid=guid,
            list_query_filter=list_query_filter,
            semantics=semantics,
            variables=variables,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnTaggingProps":
        '''Resource props.'''
        return typing.cast("CfnTaggingProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/newrelic-cloudformation-tagging.CfnTaggingProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "entity_guid": "entityGuid",
        "tags": "tags",
        "endpoint": "endpoint",
        "guid": "guid",
        "list_query_filter": "listQueryFilter",
        "semantics": "semantics",
        "variables": "variables",
    },
)
class CfnTaggingProps:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        entity_guid: builtins.str,
        tags: typing.Sequence[typing.Union["TagObject", typing.Dict[builtins.str, typing.Any]]],
        endpoint: typing.Optional[builtins.str] = None,
        guid: typing.Optional[builtins.str] = None,
        list_query_filter: typing.Optional[builtins.str] = None,
        semantics: typing.Optional[builtins.str] = None,
        variables: typing.Any = None,
    ) -> None:
        '''CRUD operations for New Relic Tags via the NerdGraph API.

        :param api_key: 
        :param entity_guid: 
        :param tags: 
        :param endpoint: 
        :param guid: 
        :param list_query_filter: 
        :param semantics: 
        :param variables: 

        :schema: CfnTaggingProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8db12f4a240e14aaaee37bc25f0237e96e7b59ae927f09c48503103fbaec945f)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument entity_guid", value=entity_guid, expected_type=type_hints["entity_guid"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument guid", value=guid, expected_type=type_hints["guid"])
            check_type(argname="argument list_query_filter", value=list_query_filter, expected_type=type_hints["list_query_filter"])
            check_type(argname="argument semantics", value=semantics, expected_type=type_hints["semantics"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "entity_guid": entity_guid,
            "tags": tags,
        }
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if guid is not None:
            self._values["guid"] = guid
        if list_query_filter is not None:
            self._values["list_query_filter"] = list_query_filter
        if semantics is not None:
            self._values["semantics"] = semantics
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def api_key(self) -> builtins.str:
        '''
        :schema: CfnTaggingProps#APIKey
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_guid(self) -> builtins.str:
        '''
        :schema: CfnTaggingProps#EntityGuid
        '''
        result = self._values.get("entity_guid")
        assert result is not None, "Required property 'entity_guid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.List["TagObject"]:
        '''
        :schema: CfnTaggingProps#Tags
        '''
        result = self._values.get("tags")
        assert result is not None, "Required property 'tags' is missing"
        return typing.cast(typing.List["TagObject"], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTaggingProps#Endpoint
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def guid(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTaggingProps#Guid
        '''
        result = self._values.get("guid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def list_query_filter(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTaggingProps#ListQueryFilter
        '''
        result = self._values.get("list_query_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def semantics(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnTaggingProps#Semantics
        '''
        result = self._values.get("semantics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variables(self) -> typing.Any:
        '''
        :schema: CfnTaggingProps#Variables
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaggingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/newrelic-cloudformation-tagging.TagObject",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class TagObject:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: 
        :param values: 

        :schema: TagObject
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cfbc9d75d7bb512ef7e1527b9bfea137345b904c166ebfbbdc22e2830f71249)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :schema: TagObject#Key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''
        :schema: TagObject#Values
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTagging",
    "CfnTaggingProps",
    "TagObject",
]

publication.publish()

def _typecheckingstub__f8a1da37fd8597ee84b5a5750dbf93fe2c17ae76d0d36f10e00b7d2b9779ccdd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key: builtins.str,
    entity_guid: builtins.str,
    tags: typing.Sequence[typing.Union[TagObject, typing.Dict[builtins.str, typing.Any]]],
    endpoint: typing.Optional[builtins.str] = None,
    guid: typing.Optional[builtins.str] = None,
    list_query_filter: typing.Optional[builtins.str] = None,
    semantics: typing.Optional[builtins.str] = None,
    variables: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db12f4a240e14aaaee37bc25f0237e96e7b59ae927f09c48503103fbaec945f(
    *,
    api_key: builtins.str,
    entity_guid: builtins.str,
    tags: typing.Sequence[typing.Union[TagObject, typing.Dict[builtins.str, typing.Any]]],
    endpoint: typing.Optional[builtins.str] = None,
    guid: typing.Optional[builtins.str] = None,
    list_query_filter: typing.Optional[builtins.str] = None,
    semantics: typing.Optional[builtins.str] = None,
    variables: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfbc9d75d7bb512ef7e1527b9bfea137345b904c166ebfbbdc22e2830f71249(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass
