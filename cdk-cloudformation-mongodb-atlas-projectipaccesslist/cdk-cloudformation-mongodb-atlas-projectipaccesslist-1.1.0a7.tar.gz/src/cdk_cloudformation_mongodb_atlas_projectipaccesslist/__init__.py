'''
# mongodb-atlas-projectipaccesslist

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `MongoDB::Atlas::ProjectIpAccessList` v1.1.0.

---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This package is deprecated. Please use the respective `@mongodbatlas-awscdk/*` scoped package instead

---


## Description

An example resource schema demonstrating some basic constructs and validation rules.

## References

* [Source](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name MongoDB::Atlas::ProjectIpAccessList \
  --publisher-id bb989456c78c398a858fef18f2ca1bfc1fbba082 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/bb989456c78c398a858fef18f2ca1bfc1fbba082/MongoDB-Atlas-ProjectIpAccessList \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `MongoDB::Atlas::ProjectIpAccessList`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fmongodb-atlas-projectipaccesslist+v1.1.0).
* Issues related to `MongoDB::Atlas::ProjectIpAccessList` should be reported to the [publisher](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git).

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
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.AccessListDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "aws_security_group": "awsSecurityGroup",
        "cidr_block": "cidrBlock",
        "comment": "comment",
        "ip_address": "ipAddress",
        "project_id": "projectId",
    },
)
class AccessListDefinition:
    def __init__(
        self,
        *,
        aws_security_group: typing.Optional[builtins.str] = None,
        cidr_block: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        ip_address: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_security_group: (deprecated) ID of the AWS security group to allow access. Mutually exclusive with CIDRBlock and IPAddress.
        :param cidr_block: (deprecated) Accessable entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with ipAddress and AwsSecurityGroup.
        :param comment: (deprecated) Comment associated with the ip access list entry.
        :param ip_address: (deprecated) Accessable IP address. Mutually exclusive with CIDRBlock and AwsSecurityGroup.
        :param project_id: (deprecated) The unique identifier for the project to which you want to add one or more ip access list entries.

        :stability: deprecated
        :schema: accessListDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2c98c1bbe3547d75d5ee59382b34f7f8d886adb6d54962be3a7e22bcd1e5a6e)
            check_type(argname="argument aws_security_group", value=aws_security_group, expected_type=type_hints["aws_security_group"])
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_security_group is not None:
            self._values["aws_security_group"] = aws_security_group
        if cidr_block is not None:
            self._values["cidr_block"] = cidr_block
        if comment is not None:
            self._values["comment"] = comment
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def aws_security_group(self) -> typing.Optional[builtins.str]:
        '''(deprecated) ID of the AWS security group to allow access.

        Mutually exclusive with CIDRBlock and IPAddress.

        :stability: deprecated
        :schema: accessListDefinition#AwsSecurityGroup
        '''
        result = self._values.get("aws_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cidr_block(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Accessable entry in Classless Inter-Domain Routing (CIDR) notation.

        Mutually exclusive with ipAddress and AwsSecurityGroup.

        :stability: deprecated
        :schema: accessListDefinition#CIDRBlock
        '''
        result = self._values.get("cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Comment associated with the ip access list entry.

        :stability: deprecated
        :schema: accessListDefinition#Comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Accessable IP address.

        Mutually exclusive with CIDRBlock and AwsSecurityGroup.

        :stability: deprecated
        :schema: accessListDefinition#IPAddress
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The unique identifier for the project to which you want to add one or more ip access list entries.

        :stability: deprecated
        :schema: accessListDefinition#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessListDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.ApiKeyDefinition",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bb9fe97ec2d634209d318bed0ad5e1a818ad20c3d4274eacd0aab769a37c33a)
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


class CfnProjectIpAccessList(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.CfnProjectIpAccessList",
):
    '''A CloudFormation ``MongoDB::Atlas::ProjectIpAccessList``.

    :cloudformationResource: MongoDB::Atlas::ProjectIpAccessList
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_list: typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]],
        api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::ProjectIpAccessList``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param access_list: 
        :param api_keys: 
        :param project_id: (deprecated) The unique identifier for the project to which you want to add one or more ip access list entries.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22dddf0c9a0645a9b02d55c836504a1114020122d69b1c8d338f93726a6dee2b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectIpAccessListProps(
            access_list=access_list, api_keys=api_keys, project_id=project_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ProjectIpAccessList.Id``.

        :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrTotalCount")
    def attr_total_count(self) -> jsii.Number:
        '''Attribute ``MongoDB::Atlas::ProjectIpAccessList.TotalCount``.

        :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrTotalCount"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnProjectIpAccessListProps":
        '''Resource props.'''
        return typing.cast("CfnProjectIpAccessListProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.CfnProjectIpAccessListProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_list": "accessList",
        "api_keys": "apiKeys",
        "project_id": "projectId",
    },
)
class CfnProjectIpAccessListProps:
    def __init__(
        self,
        *,
        access_list: typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]],
        api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
        project_id: builtins.str,
    ) -> None:
        '''(deprecated) An example resource schema demonstrating some basic constructs and validation rules.

        :param access_list: 
        :param api_keys: 
        :param project_id: (deprecated) The unique identifier for the project to which you want to add one or more ip access list entries.

        :stability: deprecated
        :schema: CfnProjectIpAccessListProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef976fb08cb2bc9827e0c6bf05935bf6881ccd8e8435ee590ed382bda3886a4)
            check_type(argname="argument access_list", value=access_list, expected_type=type_hints["access_list"])
            check_type(argname="argument api_keys", value=api_keys, expected_type=type_hints["api_keys"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_list": access_list,
            "api_keys": api_keys,
            "project_id": project_id,
        }

    @builtins.property
    def access_list(self) -> typing.List[AccessListDefinition]:
        '''
        :stability: deprecated
        :schema: CfnProjectIpAccessListProps#AccessList
        '''
        result = self._values.get("access_list")
        assert result is not None, "Required property 'access_list' is missing"
        return typing.cast(typing.List[AccessListDefinition], result)

    @builtins.property
    def api_keys(self) -> ApiKeyDefinition:
        '''
        :stability: deprecated
        :schema: CfnProjectIpAccessListProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        assert result is not None, "Required property 'api_keys' is missing"
        return typing.cast(ApiKeyDefinition, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''(deprecated) The unique identifier for the project to which you want to add one or more ip access list entries.

        :stability: deprecated
        :schema: CfnProjectIpAccessListProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectIpAccessListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessListDefinition",
    "ApiKeyDefinition",
    "CfnProjectIpAccessList",
    "CfnProjectIpAccessListProps",
]

publication.publish()

def _typecheckingstub__a2c98c1bbe3547d75d5ee59382b34f7f8d886adb6d54962be3a7e22bcd1e5a6e(
    *,
    aws_security_group: typing.Optional[builtins.str] = None,
    cidr_block: typing.Optional[builtins.str] = None,
    comment: typing.Optional[builtins.str] = None,
    ip_address: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bb9fe97ec2d634209d318bed0ad5e1a818ad20c3d4274eacd0aab769a37c33a(
    *,
    private_key: typing.Optional[builtins.str] = None,
    public_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22dddf0c9a0645a9b02d55c836504a1114020122d69b1c8d338f93726a6dee2b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_list: typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]],
    api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef976fb08cb2bc9827e0c6bf05935bf6881ccd8e8435ee590ed382bda3886a4(
    *,
    access_list: typing.Sequence[typing.Union[AccessListDefinition, typing.Dict[builtins.str, typing.Any]]],
    api_keys: typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]],
    project_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
