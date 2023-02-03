'''
# mongodb-atlas-project

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `MongoDB::Atlas::Project` v1.6.0.

---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This package is deprecated. Please use the respective `@mongodbatlas-awscdk/*` scoped package instead

---


## Description

Retrieves or creates projects in any given Atlas organization.

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name MongoDB::Atlas::Project \
  --publisher-id bb989456c78c398a858fef18f2ca1bfc1fbba082 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/bb989456c78c398a858fef18f2ca1bfc1fbba082/MongoDB-Atlas-Project \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `MongoDB::Atlas::Project`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fmongodb-atlas-project+v1.6.0).
* Issues related to `MongoDB::Atlas::Project` should be reported to the [publisher](undefined).

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


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-project.ApiKeyDefinition",
    jsii_struct_bases=[],
    name_mapping={"private_key": "privateKey", "public_key": "publicKey"},
)
class ApiKeyDefinition:
    def __init__(
        self,
        *,
        private_key: typing.Optional[builtins.str] = None,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private_key: 
        :param public_key: 

        :stability: deprecated
        :schema: apiKeyDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51e09e6ad9e1a4c964c155f93c52a7a6fe4d6cc57e091e73d742ba4afd84dc53)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if private_key is not None:
            self._values["private_key"] = private_key
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: apiKeyDefinition#PrivateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: apiKeyDefinition#PublicKey
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnProject(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-project.CfnProject",
):
    '''A CloudFormation ``MongoDB::Atlas::Project``.

    :cloudformationResource: MongoDB::Atlas::Project
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        org_id: builtins.str,
        api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: (deprecated) Name of the project to create.
        :param org_id: (deprecated) Unique identifier of the organization within which to create the project.
        :param api_keys: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd51843eaf2658107616ab9cbb7d566ef79744f24a8bbab654ec0048719e17a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(name=name, org_id=org_id, api_keys=api_keys)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterCount")
    def attr_cluster_count(self) -> jsii.Number:
        '''Attribute ``MongoDB::Atlas::Project.ClusterCount``.

        :link: http://unknown-url
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrClusterCount"))

    @builtins.property
    @jsii.member(jsii_name="attrCreated")
    def attr_created(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Project.Created``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreated"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Project.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnProjectProps":
        '''Resource props.'''
        return typing.cast("CfnProjectProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-project.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "org_id": "orgId", "api_keys": "apiKeys"},
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        org_id: builtins.str,
        api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(deprecated) Retrieves or creates projects in any given Atlas organization.

        :param name: (deprecated) Name of the project to create.
        :param org_id: (deprecated) Unique identifier of the organization within which to create the project.
        :param api_keys: 

        :stability: deprecated
        :schema: CfnProjectProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e5d7f8b8284a84034a33d8ca6dea5275b2bfccc4d78f95b97c3dfefd2b13254)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument api_keys", value=api_keys, expected_type=type_hints["api_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "org_id": org_id,
        }
        if api_keys is not None:
            self._values["api_keys"] = api_keys

    @builtins.property
    def name(self) -> builtins.str:
        '''(deprecated) Name of the project to create.

        :stability: deprecated
        :schema: CfnProjectProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def org_id(self) -> builtins.str:
        '''(deprecated) Unique identifier of the organization within which to create the project.

        :stability: deprecated
        :schema: CfnProjectProps#OrgId
        '''
        result = self._values.get("org_id")
        assert result is not None, "Required property 'org_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_keys(self) -> typing.Optional[ApiKeyDefinition]:
        '''
        :stability: deprecated
        :schema: CfnProjectProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        return typing.cast(typing.Optional[ApiKeyDefinition], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiKeyDefinition",
    "CfnProject",
    "CfnProjectProps",
]

publication.publish()

def _typecheckingstub__51e09e6ad9e1a4c964c155f93c52a7a6fe4d6cc57e091e73d742ba4afd84dc53(
    *,
    private_key: typing.Optional[builtins.str] = None,
    public_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd51843eaf2658107616ab9cbb7d566ef79744f24a8bbab654ec0048719e17a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    org_id: builtins.str,
    api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e5d7f8b8284a84034a33d8ca6dea5275b2bfccc4d78f95b97c3dfefd2b13254(
    *,
    name: builtins.str,
    org_id: builtins.str,
    api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
