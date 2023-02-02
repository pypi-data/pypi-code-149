'''
# freyraim-spider-ecs-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::Spider::ECS::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type FreyrAIM::Spider::ECS::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::Spider::ECS::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-Spider-ECS-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::Spider::ECS::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-spider-ecs-module+v1.0.0).
* Issues related to `FreyrAIM::Spider::ECS::MODULE` should be reported to the [publisher](undefined).

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


class CfnEcsModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-spider-ecs-module.CfnEcsModule",
):
    '''A CloudFormation ``FreyrAIM::Spider::ECS::MODULE``.

    :cloudformationResource: FreyrAIM::Spider::ECS::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnEcsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnEcsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::Spider::ECS::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d43886cc899109ff029fe19b604952c1ff50fa5648220ac1b3183c1bc2f33cf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEcsModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnEcsModuleProps":
        '''Resource props.'''
        return typing.cast("CfnEcsModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ecs-module.CfnEcsModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnEcsModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnEcsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnEcsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::Spider::ECS::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnEcsModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnEcsModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnEcsModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56912f5a6a778a898ceaa98f8db56bcc757f8fb2aa2dec75bbf5980f6fdb8ff7)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnEcsModulePropsParameters"]:
        '''
        :schema: CfnEcsModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnEcsModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnEcsModulePropsResources"]:
        '''
        :schema: CfnEcsModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnEcsModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEcsModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ecs-module.CfnEcsModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"env_name": "envName"},
)
class CfnEcsModulePropsParameters:
    def __init__(
        self,
        *,
        env_name: typing.Optional[typing.Union["CfnEcsModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param env_name: The environment name.

        :schema: CfnEcsModulePropsParameters
        '''
        if isinstance(env_name, dict):
            env_name = CfnEcsModulePropsParametersEnvName(**env_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39200b54ea45eb438c85fadda5ed0d4c5be6b88f581fd22058e0e11ea2f0cd15)
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if env_name is not None:
            self._values["env_name"] = env_name

    @builtins.property
    def env_name(self) -> typing.Optional["CfnEcsModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnEcsModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnEcsModulePropsParametersEnvName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEcsModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ecs-module.CfnEcsModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEcsModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnEcsModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d65a8deb23eca54b6f296bbe60ed93fee3536eb6189e8a93b70f3fc655654c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEcsModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEcsModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEcsModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ecs-module.CfnEcsModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"cluster": "cluster", "task_definition": "taskDefinition"},
)
class CfnEcsModulePropsResources:
    def __init__(
        self,
        *,
        cluster: typing.Optional[typing.Union["CfnEcsModulePropsResourcesCluster", typing.Dict[builtins.str, typing.Any]]] = None,
        task_definition: typing.Optional[typing.Union["CfnEcsModulePropsResourcesTaskDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cluster: 
        :param task_definition: 

        :schema: CfnEcsModulePropsResources
        '''
        if isinstance(cluster, dict):
            cluster = CfnEcsModulePropsResourcesCluster(**cluster)
        if isinstance(task_definition, dict):
            task_definition = CfnEcsModulePropsResourcesTaskDefinition(**task_definition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6afd44649d9dc9f877087b208ec39493704b1ae4019109b44cf87f74771c256b)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cluster is not None:
            self._values["cluster"] = cluster
        if task_definition is not None:
            self._values["task_definition"] = task_definition

    @builtins.property
    def cluster(self) -> typing.Optional["CfnEcsModulePropsResourcesCluster"]:
        '''
        :schema: CfnEcsModulePropsResources#Cluster
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional["CfnEcsModulePropsResourcesCluster"], result)

    @builtins.property
    def task_definition(
        self,
    ) -> typing.Optional["CfnEcsModulePropsResourcesTaskDefinition"]:
        '''
        :schema: CfnEcsModulePropsResources#TaskDefinition
        '''
        result = self._values.get("task_definition")
        return typing.cast(typing.Optional["CfnEcsModulePropsResourcesTaskDefinition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEcsModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ecs-module.CfnEcsModulePropsResourcesCluster",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEcsModulePropsResourcesCluster:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEcsModulePropsResourcesCluster
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddc6af91abcfde26dd052244e08f4830c3053de6c064bd2786bfa9747b82a486)
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
        :schema: CfnEcsModulePropsResourcesCluster#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEcsModulePropsResourcesCluster#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEcsModulePropsResourcesCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ecs-module.CfnEcsModulePropsResourcesTaskDefinition",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEcsModulePropsResourcesTaskDefinition:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEcsModulePropsResourcesTaskDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b752ad6339a963c7bd9ad169e04963737db7f10269ab2742c613d9f5d03eb6)
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
        :schema: CfnEcsModulePropsResourcesTaskDefinition#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEcsModulePropsResourcesTaskDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEcsModulePropsResourcesTaskDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEcsModule",
    "CfnEcsModuleProps",
    "CfnEcsModulePropsParameters",
    "CfnEcsModulePropsParametersEnvName",
    "CfnEcsModulePropsResources",
    "CfnEcsModulePropsResourcesCluster",
    "CfnEcsModulePropsResourcesTaskDefinition",
]

publication.publish()

def _typecheckingstub__9d43886cc899109ff029fe19b604952c1ff50fa5648220ac1b3183c1bc2f33cf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnEcsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEcsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56912f5a6a778a898ceaa98f8db56bcc757f8fb2aa2dec75bbf5980f6fdb8ff7(
    *,
    parameters: typing.Optional[typing.Union[CfnEcsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEcsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39200b54ea45eb438c85fadda5ed0d4c5be6b88f581fd22058e0e11ea2f0cd15(
    *,
    env_name: typing.Optional[typing.Union[CfnEcsModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d65a8deb23eca54b6f296bbe60ed93fee3536eb6189e8a93b70f3fc655654c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6afd44649d9dc9f877087b208ec39493704b1ae4019109b44cf87f74771c256b(
    *,
    cluster: typing.Optional[typing.Union[CfnEcsModulePropsResourcesCluster, typing.Dict[builtins.str, typing.Any]]] = None,
    task_definition: typing.Optional[typing.Union[CfnEcsModulePropsResourcesTaskDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc6af91abcfde26dd052244e08f4830c3053de6c064bd2786bfa9747b82a486(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b752ad6339a963c7bd9ad169e04963737db7f10269ab2742c613d9f5d03eb6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
