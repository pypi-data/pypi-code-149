'''
# mongodb-atlas-databaseuser

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `MongoDB::Atlas::DatabaseUser` v1.3.0.

---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This package is deprecated. Please use the respective `@mongodbatlas-awscdk/*` scoped package instead

---


## Description

The databaseUsers resource lets you retrieve, create and modify the MongoDB users in your cluster. Each user has a set of roles that provide access to the project?s databases. A user?s roles apply to all the clusters in the project: if two clusters have a products database and a user has a role granting read access on the products database, the user has that access on both clusters.

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name MongoDB::Atlas::DatabaseUser \
  --publisher-id bb989456c78c398a858fef18f2ca1bfc1fbba082 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/bb989456c78c398a858fef18f2ca1bfc1fbba082/MongoDB-Atlas-DatabaseUser \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `MongoDB::Atlas::DatabaseUser`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fmongodb-atlas-databaseuser+v1.3.0).
* Issues related to `MongoDB::Atlas::DatabaseUser` should be reported to the [publisher](undefined).

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
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.ApiKeyDefinition",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab1f7a1f27aab19339dcc821c84e1792a4ebccc0d5efbfbfac537db2355668cf)
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


class CfnDatabaseUser(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUser",
):
    '''A CloudFormation ``MongoDB::Atlas::DatabaseUser``.

    :cloudformationResource: MongoDB::Atlas::DatabaseUser
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        database_name: builtins.str,
        project_id: builtins.str,
        roles: typing.Sequence[typing.Union["RoleDefinition", typing.Dict[builtins.str, typing.Any]]],
        username: builtins.str,
        api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
        awsiam_type: typing.Optional["CfnDatabaseUserPropsAwsiamType"] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["LabelDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        ldap_auth_type: typing.Optional["CfnDatabaseUserPropsLdapAuthType"] = None,
        password: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence[typing.Union["ScopeDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::DatabaseUser``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database_name: (deprecated) The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
        :param project_id: (deprecated) Unique identifier of the Atlas project to which the user belongs.
        :param roles: (deprecated) Array of this user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well.
        :param username: (deprecated) Username for authenticating to MongoDB.
        :param api_keys: 
        :param awsiam_type: (deprecated) If this value is set, the new database user authenticates with AWS IAM credentials.
        :param labels: (deprecated) Array containing key-value pairs that tag and categorize the database user.
        :param ldap_auth_type: (deprecated) Method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE.
        :param password: (deprecated) The user’s password. This field is not included in the entity returned from the server.
        :param scopes: (deprecated) Array of clusters and Atlas Data Lakes that this user has access to. If omitted, Atlas grants the user access to all the clusters and Atlas Data Lakes in the project by default.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2938047f6540ee3ed9bfbf1285f590f977c150399a93bf08f8eb10ee8921f7e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatabaseUserProps(
            database_name=database_name,
            project_id=project_id,
            roles=roles,
            username=username,
            api_keys=api_keys,
            awsiam_type=awsiam_type,
            labels=labels,
            ldap_auth_type=ldap_auth_type,
            password=password,
            scopes=scopes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrUserCFNIdentifier")
    def attr_user_cfn_identifier(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::DatabaseUser.UserCFNIdentifier``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserCFNIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDatabaseUserProps":
        '''Resource props.'''
        return typing.cast("CfnDatabaseUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "project_id": "projectId",
        "roles": "roles",
        "username": "username",
        "api_keys": "apiKeys",
        "awsiam_type": "awsiamType",
        "labels": "labels",
        "ldap_auth_type": "ldapAuthType",
        "password": "password",
        "scopes": "scopes",
    },
)
class CfnDatabaseUserProps:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        project_id: builtins.str,
        roles: typing.Sequence[typing.Union["RoleDefinition", typing.Dict[builtins.str, typing.Any]]],
        username: builtins.str,
        api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
        awsiam_type: typing.Optional["CfnDatabaseUserPropsAwsiamType"] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["LabelDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        ldap_auth_type: typing.Optional["CfnDatabaseUserPropsLdapAuthType"] = None,
        password: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence[typing.Union["ScopeDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''(deprecated) The databaseUsers resource lets you retrieve, create and modify the MongoDB users in your cluster.

        Each user has a set of roles that provide access to the project’s databases. A user’s roles apply to all the clusters in the project: if two clusters have a products database and a user has a role granting read access on the products database, the user has that access on both clusters.

        :param database_name: (deprecated) The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
        :param project_id: (deprecated) Unique identifier of the Atlas project to which the user belongs.
        :param roles: (deprecated) Array of this user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well.
        :param username: (deprecated) Username for authenticating to MongoDB.
        :param api_keys: 
        :param awsiam_type: (deprecated) If this value is set, the new database user authenticates with AWS IAM credentials.
        :param labels: (deprecated) Array containing key-value pairs that tag and categorize the database user.
        :param ldap_auth_type: (deprecated) Method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE.
        :param password: (deprecated) The user’s password. This field is not included in the entity returned from the server.
        :param scopes: (deprecated) Array of clusters and Atlas Data Lakes that this user has access to. If omitted, Atlas grants the user access to all the clusters and Atlas Data Lakes in the project by default.

        :stability: deprecated
        :schema: CfnDatabaseUserProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e3c7db7aaa555b2362fba0d76209942460cc8f817291c56e0ba41b6a34c0925)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument api_keys", value=api_keys, expected_type=type_hints["api_keys"])
            check_type(argname="argument awsiam_type", value=awsiam_type, expected_type=type_hints["awsiam_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument ldap_auth_type", value=ldap_auth_type, expected_type=type_hints["ldap_auth_type"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "project_id": project_id,
            "roles": roles,
            "username": username,
        }
        if api_keys is not None:
            self._values["api_keys"] = api_keys
        if awsiam_type is not None:
            self._values["awsiam_type"] = awsiam_type
        if labels is not None:
            self._values["labels"] = labels
        if ldap_auth_type is not None:
            self._values["ldap_auth_type"] = ldap_auth_type
        if password is not None:
            self._values["password"] = password
        if scopes is not None:
            self._values["scopes"] = scopes

    @builtins.property
    def database_name(self) -> builtins.str:
        '''(deprecated) The user’s authentication database.

        A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#DatabaseName
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''(deprecated) Unique identifier of the Atlas project to which the user belongs.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List["RoleDefinition"]:
        '''(deprecated) Array of this user’s roles and the databases / collections on which the roles apply.

        A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#Roles
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List["RoleDefinition"], result)

    @builtins.property
    def username(self) -> builtins.str:
        '''(deprecated) Username for authenticating to MongoDB.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#Username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_keys(self) -> typing.Optional[ApiKeyDefinition]:
        '''
        :stability: deprecated
        :schema: CfnDatabaseUserProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        return typing.cast(typing.Optional[ApiKeyDefinition], result)

    @builtins.property
    def awsiam_type(self) -> typing.Optional["CfnDatabaseUserPropsAwsiamType"]:
        '''(deprecated) If this value is set, the new database user authenticates with AWS IAM credentials.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#AWSIAMType
        '''
        result = self._values.get("awsiam_type")
        return typing.cast(typing.Optional["CfnDatabaseUserPropsAwsiamType"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["LabelDefinition"]]:
        '''(deprecated) Array containing key-value pairs that tag and categorize the database user.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#Labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["LabelDefinition"]], result)

    @builtins.property
    def ldap_auth_type(self) -> typing.Optional["CfnDatabaseUserPropsLdapAuthType"]:
        '''(deprecated) Method by which the provided username is authenticated.

        If no value is given, Atlas uses the default value of NONE.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#LdapAuthType
        '''
        result = self._values.get("ldap_auth_type")
        return typing.cast(typing.Optional["CfnDatabaseUserPropsLdapAuthType"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The user’s password.

        This field is not included in the entity returned from the server.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#Password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scopes(self) -> typing.Optional[typing.List["ScopeDefinition"]]:
        '''(deprecated) Array of clusters and Atlas Data Lakes that this user has access to.

        If omitted, Atlas grants the user access to all the clusters and Atlas Data Lakes in the project by default.

        :stability: deprecated
        :schema: CfnDatabaseUserProps#Scopes
        '''
        result = self._values.get("scopes")
        return typing.cast(typing.Optional[typing.List["ScopeDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUserPropsAwsiamType"
)
class CfnDatabaseUserPropsAwsiamType(enum.Enum):
    '''(deprecated) If this value is set, the new database user authenticates with AWS IAM credentials.

    :stability: deprecated
    :schema: CfnDatabaseUserPropsAwsiamType
    '''

    NONE = "NONE"
    '''(deprecated) NONE.

    :stability: deprecated
    '''
    USER = "USER"
    '''(deprecated) USER.

    :stability: deprecated
    '''
    ROLE = "ROLE"
    '''(deprecated) ROLE.

    :stability: deprecated
    '''


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUserPropsLdapAuthType"
)
class CfnDatabaseUserPropsLdapAuthType(enum.Enum):
    '''(deprecated) Method by which the provided username is authenticated.

    If no value is given, Atlas uses the default value of NONE.

    :stability: deprecated
    :schema: CfnDatabaseUserPropsLdapAuthType
    '''

    NONE = "NONE"
    '''(deprecated) NONE.

    :stability: deprecated
    '''
    USER = "USER"
    '''(deprecated) USER.

    :stability: deprecated
    '''
    GROUP = "GROUP"
    '''(deprecated) GROUP.

    :stability: deprecated
    '''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.LabelDefinition",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class LabelDefinition:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :stability: deprecated
        :schema: labelDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f813538b9817d3c23a4fc084a3a3a525e1a6ead2f02216d1e939f4a7c98bcb)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: labelDefinition#Key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: labelDefinition#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LabelDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.RoleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "collection_name": "collectionName",
        "database_name": "databaseName",
        "role_name": "roleName",
    },
)
class RoleDefinition:
    def __init__(
        self,
        *,
        collection_name: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param collection_name: 
        :param database_name: 
        :param role_name: 

        :stability: deprecated
        :schema: roleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac2ce09265336b515cbb1cb3dc5fb1cea7aac5981fdcda2835d4b3d72427d900)
            check_type(argname="argument collection_name", value=collection_name, expected_type=type_hints["collection_name"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collection_name is not None:
            self._values["collection_name"] = collection_name
        if database_name is not None:
            self._values["database_name"] = database_name
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def collection_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: roleDefinition#CollectionName
        '''
        result = self._values.get("collection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: roleDefinition#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: roleDefinition#RoleName
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.ScopeDefinition",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class ScopeDefinition:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["ScopeDefinitionType"] = None,
    ) -> None:
        '''
        :param name: 
        :param type: 

        :stability: deprecated
        :schema: scopeDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18589cb59f7df204782c329223bb6520be21007bdd94886172add2409a439a4e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: scopeDefinition#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ScopeDefinitionType"]:
        '''
        :stability: deprecated
        :schema: scopeDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ScopeDefinitionType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScopeDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.ScopeDefinitionType"
)
class ScopeDefinitionType(enum.Enum):
    '''
    :stability: deprecated
    :schema: ScopeDefinitionType
    '''

    CLUSTER = "CLUSTER"
    '''(deprecated) CLUSTER.

    :stability: deprecated
    '''
    DATA_LAKE = "DATA_LAKE"
    '''(deprecated) DATA_LAKE.

    :stability: deprecated
    '''


__all__ = [
    "ApiKeyDefinition",
    "CfnDatabaseUser",
    "CfnDatabaseUserProps",
    "CfnDatabaseUserPropsAwsiamType",
    "CfnDatabaseUserPropsLdapAuthType",
    "LabelDefinition",
    "RoleDefinition",
    "ScopeDefinition",
    "ScopeDefinitionType",
]

publication.publish()

def _typecheckingstub__ab1f7a1f27aab19339dcc821c84e1792a4ebccc0d5efbfbfac537db2355668cf(
    *,
    private_key: typing.Optional[builtins.str] = None,
    public_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2938047f6540ee3ed9bfbf1285f590f977c150399a93bf08f8eb10ee8921f7e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    database_name: builtins.str,
    project_id: builtins.str,
    roles: typing.Sequence[typing.Union[RoleDefinition, typing.Dict[builtins.str, typing.Any]]],
    username: builtins.str,
    api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    awsiam_type: typing.Optional[CfnDatabaseUserPropsAwsiamType] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[LabelDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ldap_auth_type: typing.Optional[CfnDatabaseUserPropsLdapAuthType] = None,
    password: typing.Optional[builtins.str] = None,
    scopes: typing.Optional[typing.Sequence[typing.Union[ScopeDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3c7db7aaa555b2362fba0d76209942460cc8f817291c56e0ba41b6a34c0925(
    *,
    database_name: builtins.str,
    project_id: builtins.str,
    roles: typing.Sequence[typing.Union[RoleDefinition, typing.Dict[builtins.str, typing.Any]]],
    username: builtins.str,
    api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    awsiam_type: typing.Optional[CfnDatabaseUserPropsAwsiamType] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[LabelDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ldap_auth_type: typing.Optional[CfnDatabaseUserPropsLdapAuthType] = None,
    password: typing.Optional[builtins.str] = None,
    scopes: typing.Optional[typing.Sequence[typing.Union[ScopeDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f813538b9817d3c23a4fc084a3a3a525e1a6ead2f02216d1e939f4a7c98bcb(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2ce09265336b515cbb1cb3dc5fb1cea7aac5981fdcda2835d4b3d72427d900(
    *,
    collection_name: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18589cb59f7df204782c329223bb6520be21007bdd94886172add2409a439a4e(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ScopeDefinitionType] = None,
) -> None:
    """Type checking stubs"""
    pass
