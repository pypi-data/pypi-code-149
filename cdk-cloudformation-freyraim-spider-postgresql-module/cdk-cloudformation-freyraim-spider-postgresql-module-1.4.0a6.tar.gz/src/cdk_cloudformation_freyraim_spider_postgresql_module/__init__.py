'''
# freyraim-spider-postgresql-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::Spider::PostgreSQL::MODULE` v1.4.0.

## Description

Schema for Module Fragment of type FreyrAIM::Spider::PostgreSQL::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::Spider::PostgreSQL::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-Spider-PostgreSQL-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::Spider::PostgreSQL::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-spider-postgresql-module+v1.4.0).
* Issues related to `FreyrAIM::Spider::PostgreSQL::MODULE` should be reported to the [publisher](undefined).

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


class CfnPostgreSqlModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModule",
):
    '''A CloudFormation ``FreyrAIM::Spider::PostgreSQL::MODULE``.

    :cloudformationResource: FreyrAIM::Spider::PostgreSQL::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnPostgreSqlModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnPostgreSqlModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::Spider::PostgreSQL::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93b829300d3a46b7503f5f9a43adc000cdea40997a2f928d2ef0b91d4c4d2822)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPostgreSqlModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnPostgreSqlModuleProps":
        '''Resource props.'''
        return typing.cast("CfnPostgreSqlModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnPostgreSqlModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnPostgreSqlModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnPostgreSqlModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::Spider::PostgreSQL::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnPostgreSqlModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnPostgreSqlModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnPostgreSqlModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f89f96278bdfc6d222d44cece2bb3c80de06ca2f25cde46bfe951e4717cf8d2)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnPostgreSqlModulePropsParameters"]:
        '''
        :schema: CfnPostgreSqlModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnPostgreSqlModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnPostgreSqlModulePropsResources"]:
        '''
        :schema: CfnPostgreSqlModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnPostgreSqlModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "db_password": "dbPassword",
        "db_username": "dbUsername",
        "env_name": "envName",
        "test": "test",
    },
)
class CfnPostgreSqlModulePropsParameters:
    def __init__(
        self,
        *,
        db_password: typing.Optional[typing.Union["CfnPostgreSqlModulePropsParametersDbPassword", typing.Dict[builtins.str, typing.Any]]] = None,
        db_username: typing.Optional[typing.Union["CfnPostgreSqlModulePropsParametersDbUsername", typing.Dict[builtins.str, typing.Any]]] = None,
        env_name: typing.Optional[typing.Union["CfnPostgreSqlModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
        test: typing.Optional[typing.Union["CfnPostgreSqlModulePropsParametersTest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param db_password: Password database access.
        :param db_username: Username for database access.
        :param env_name: The environment name.
        :param test: The environment name.

        :schema: CfnPostgreSqlModulePropsParameters
        '''
        if isinstance(db_password, dict):
            db_password = CfnPostgreSqlModulePropsParametersDbPassword(**db_password)
        if isinstance(db_username, dict):
            db_username = CfnPostgreSqlModulePropsParametersDbUsername(**db_username)
        if isinstance(env_name, dict):
            env_name = CfnPostgreSqlModulePropsParametersEnvName(**env_name)
        if isinstance(test, dict):
            test = CfnPostgreSqlModulePropsParametersTest(**test)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89d9b4efe8bf5dcbaa6d681e830e2ce261253cb9123054cbf6877d210c8f891)
            check_type(argname="argument db_password", value=db_password, expected_type=type_hints["db_password"])
            check_type(argname="argument db_username", value=db_username, expected_type=type_hints["db_username"])
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
            check_type(argname="argument test", value=test, expected_type=type_hints["test"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if db_password is not None:
            self._values["db_password"] = db_password
        if db_username is not None:
            self._values["db_username"] = db_username
        if env_name is not None:
            self._values["env_name"] = env_name
        if test is not None:
            self._values["test"] = test

    @builtins.property
    def db_password(
        self,
    ) -> typing.Optional["CfnPostgreSqlModulePropsParametersDbPassword"]:
        '''Password database access.

        :schema: CfnPostgreSqlModulePropsParameters#DBPassword
        '''
        result = self._values.get("db_password")
        return typing.cast(typing.Optional["CfnPostgreSqlModulePropsParametersDbPassword"], result)

    @builtins.property
    def db_username(
        self,
    ) -> typing.Optional["CfnPostgreSqlModulePropsParametersDbUsername"]:
        '''Username for database access.

        :schema: CfnPostgreSqlModulePropsParameters#DBUsername
        '''
        result = self._values.get("db_username")
        return typing.cast(typing.Optional["CfnPostgreSqlModulePropsParametersDbUsername"], result)

    @builtins.property
    def env_name(self) -> typing.Optional["CfnPostgreSqlModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnPostgreSqlModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnPostgreSqlModulePropsParametersEnvName"], result)

    @builtins.property
    def test(self) -> typing.Optional["CfnPostgreSqlModulePropsParametersTest"]:
        '''The environment name.

        :schema: CfnPostgreSqlModulePropsParameters#Test
        '''
        result = self._values.get("test")
        return typing.cast(typing.Optional["CfnPostgreSqlModulePropsParametersTest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModulePropsParametersDbPassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnPostgreSqlModulePropsParametersDbPassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Password database access.

        :param description: 
        :param type: 

        :schema: CfnPostgreSqlModulePropsParametersDbPassword
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5912112825bc2dd3aff7d514f5c9d98cff1b37f47f1c5059fe41f94945c2a195)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersDbPassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersDbPassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModulePropsParametersDbPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModulePropsParametersDbUsername",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnPostgreSqlModulePropsParametersDbUsername:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Username for database access.

        :param description: 
        :param type: 

        :schema: CfnPostgreSqlModulePropsParametersDbUsername
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec7584d288e8b3d805994e60e09785c13e07b37b90970a8f8c7358fa75d38643)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersDbUsername#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersDbUsername#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModulePropsParametersDbUsername(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnPostgreSqlModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnPostgreSqlModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc6871fb5c7f07ae0c7723b236cf8087e29b57b61794d88fd35e0f384c9f5d27)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModulePropsParametersTest",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnPostgreSqlModulePropsParametersTest:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnPostgreSqlModulePropsParametersTest
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b8c42f1cd691fb0d4d11d64896321060c30cb1af64321c596519bc8175b247)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersTest#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnPostgreSqlModulePropsParametersTest#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModulePropsParametersTest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"postgre_sql": "postgreSql"},
)
class CfnPostgreSqlModulePropsResources:
    def __init__(
        self,
        *,
        postgre_sql: typing.Optional[typing.Union["CfnPostgreSqlModulePropsResourcesPostgreSql", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param postgre_sql: 

        :schema: CfnPostgreSqlModulePropsResources
        '''
        if isinstance(postgre_sql, dict):
            postgre_sql = CfnPostgreSqlModulePropsResourcesPostgreSql(**postgre_sql)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e62ed949255a2f2e87071b395cff5a7839f64b716c82b5c0d72b67b3950a82b2)
            check_type(argname="argument postgre_sql", value=postgre_sql, expected_type=type_hints["postgre_sql"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if postgre_sql is not None:
            self._values["postgre_sql"] = postgre_sql

    @builtins.property
    def postgre_sql(
        self,
    ) -> typing.Optional["CfnPostgreSqlModulePropsResourcesPostgreSql"]:
        '''
        :schema: CfnPostgreSqlModulePropsResources#PostgreSQL
        '''
        result = self._values.get("postgre_sql")
        return typing.cast(typing.Optional["CfnPostgreSqlModulePropsResourcesPostgreSql"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-postgresql-module.CfnPostgreSqlModulePropsResourcesPostgreSql",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnPostgreSqlModulePropsResourcesPostgreSql:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnPostgreSqlModulePropsResourcesPostgreSql
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc2bd6d2ee460c9035d0a89ba704ccd90b494f08d08509a9f1873f269e80adb6)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnPostgreSqlModulePropsResourcesPostgreSql#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnPostgreSqlModulePropsResourcesPostgreSql#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPostgreSqlModulePropsResourcesPostgreSql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPostgreSqlModule",
    "CfnPostgreSqlModuleProps",
    "CfnPostgreSqlModulePropsParameters",
    "CfnPostgreSqlModulePropsParametersDbPassword",
    "CfnPostgreSqlModulePropsParametersDbUsername",
    "CfnPostgreSqlModulePropsParametersEnvName",
    "CfnPostgreSqlModulePropsParametersTest",
    "CfnPostgreSqlModulePropsResources",
    "CfnPostgreSqlModulePropsResourcesPostgreSql",
]

publication.publish()

def _typecheckingstub__93b829300d3a46b7503f5f9a43adc000cdea40997a2f928d2ef0b91d4c4d2822(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnPostgreSqlModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnPostgreSqlModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f89f96278bdfc6d222d44cece2bb3c80de06ca2f25cde46bfe951e4717cf8d2(
    *,
    parameters: typing.Optional[typing.Union[CfnPostgreSqlModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnPostgreSqlModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89d9b4efe8bf5dcbaa6d681e830e2ce261253cb9123054cbf6877d210c8f891(
    *,
    db_password: typing.Optional[typing.Union[CfnPostgreSqlModulePropsParametersDbPassword, typing.Dict[builtins.str, typing.Any]]] = None,
    db_username: typing.Optional[typing.Union[CfnPostgreSqlModulePropsParametersDbUsername, typing.Dict[builtins.str, typing.Any]]] = None,
    env_name: typing.Optional[typing.Union[CfnPostgreSqlModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
    test: typing.Optional[typing.Union[CfnPostgreSqlModulePropsParametersTest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5912112825bc2dd3aff7d514f5c9d98cff1b37f47f1c5059fe41f94945c2a195(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec7584d288e8b3d805994e60e09785c13e07b37b90970a8f8c7358fa75d38643(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6871fb5c7f07ae0c7723b236cf8087e29b57b61794d88fd35e0f384c9f5d27(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b8c42f1cd691fb0d4d11d64896321060c30cb1af64321c596519bc8175b247(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e62ed949255a2f2e87071b395cff5a7839f64b716c82b5c0d72b67b3950a82b2(
    *,
    postgre_sql: typing.Optional[typing.Union[CfnPostgreSqlModulePropsResourcesPostgreSql, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc2bd6d2ee460c9035d0a89ba704ccd90b494f08d08509a9f1873f269e80adb6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
