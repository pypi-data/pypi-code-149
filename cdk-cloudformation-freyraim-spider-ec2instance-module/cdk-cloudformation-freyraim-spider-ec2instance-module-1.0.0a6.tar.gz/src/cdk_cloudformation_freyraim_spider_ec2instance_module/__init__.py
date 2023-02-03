'''
# freyraim-spider-ec2instance-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::Spider::EC2Instance::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type FreyrAIM::Spider::EC2Instance::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::Spider::EC2Instance::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-Spider-EC2Instance-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::Spider::EC2Instance::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-spider-ec2instance-module+v1.0.0).
* Issues related to `FreyrAIM::Spider::EC2Instance::MODULE` should be reported to the [publisher](undefined).

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


class CfnEc2InstanceModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-spider-ec2instance-module.CfnEc2InstanceModule",
):
    '''A CloudFormation ``FreyrAIM::Spider::EC2Instance::MODULE``.

    :cloudformationResource: FreyrAIM::Spider::EC2Instance::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnEc2InstanceModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::Spider::EC2Instance::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ee732eb9db6125bdead844d2ce658b12c4a34b4e3c8cd7d9b4d50713e60aee)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEc2InstanceModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnEc2InstanceModuleProps":
        '''Resource props.'''
        return typing.cast("CfnEc2InstanceModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ec2instance-module.CfnEc2InstanceModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnEc2InstanceModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnEc2InstanceModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::Spider::EC2Instance::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnEc2InstanceModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnEc2InstanceModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnEc2InstanceModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e9d02cff3cc75709491968a7c1d8ddf2f60c82645b0b3ba46aa25800a1d2912)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnEc2InstanceModulePropsParameters"]:
        '''
        :schema: CfnEc2InstanceModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnEc2InstanceModulePropsResources"]:
        '''
        :schema: CfnEc2InstanceModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ec2instance-module.CfnEc2InstanceModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"env_name": "envName"},
)
class CfnEc2InstanceModulePropsParameters:
    def __init__(
        self,
        *,
        env_name: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param env_name: The environment name.

        :schema: CfnEc2InstanceModulePropsParameters
        '''
        if isinstance(env_name, dict):
            env_name = CfnEc2InstanceModulePropsParametersEnvName(**env_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b5c7e85acb7af40ff016f5d83f7be21a0fbc25cd6f23107832acf22632a062e)
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if env_name is not None:
            self._values["env_name"] = env_name

    @builtins.property
    def env_name(self) -> typing.Optional["CfnEc2InstanceModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnEc2InstanceModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersEnvName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ec2instance-module.CfnEc2InstanceModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__136318fbcabb58a5b91baf1422530fba8dc1faaed566748f2181793fa12c4d45)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ec2instance-module.CfnEc2InstanceModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"spider_ec2_instance": "spiderEc2Instance"},
)
class CfnEc2InstanceModulePropsResources:
    def __init__(
        self,
        *,
        spider_ec2_instance: typing.Optional[typing.Union["CfnEc2InstanceModulePropsResourcesSpiderEc2Instance", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param spider_ec2_instance: 

        :schema: CfnEc2InstanceModulePropsResources
        '''
        if isinstance(spider_ec2_instance, dict):
            spider_ec2_instance = CfnEc2InstanceModulePropsResourcesSpiderEc2Instance(**spider_ec2_instance)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d5507e30df6bdf1169c815cb74ee5f598b27732a23ea6ff77ccd09d0844b64e)
            check_type(argname="argument spider_ec2_instance", value=spider_ec2_instance, expected_type=type_hints["spider_ec2_instance"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if spider_ec2_instance is not None:
            self._values["spider_ec2_instance"] = spider_ec2_instance

    @builtins.property
    def spider_ec2_instance(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsResourcesSpiderEc2Instance"]:
        '''
        :schema: CfnEc2InstanceModulePropsResources#SpiderEC2Instance
        '''
        result = self._values.get("spider_ec2_instance")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResourcesSpiderEc2Instance"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-ec2instance-module.CfnEc2InstanceModulePropsResourcesSpiderEc2Instance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEc2InstanceModulePropsResourcesSpiderEc2Instance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsResourcesSpiderEc2Instance
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff864750227c607a192aa268d7cd1b06cdbaa69dc0b353185f994cc5c1557d8)
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
        :schema: CfnEc2InstanceModulePropsResourcesSpiderEc2Instance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesSpiderEc2Instance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResourcesSpiderEc2Instance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEc2InstanceModule",
    "CfnEc2InstanceModuleProps",
    "CfnEc2InstanceModulePropsParameters",
    "CfnEc2InstanceModulePropsParametersEnvName",
    "CfnEc2InstanceModulePropsResources",
    "CfnEc2InstanceModulePropsResourcesSpiderEc2Instance",
]

publication.publish()

def _typecheckingstub__a7ee732eb9db6125bdead844d2ce658b12c4a34b4e3c8cd7d9b4d50713e60aee(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e9d02cff3cc75709491968a7c1d8ddf2f60c82645b0b3ba46aa25800a1d2912(
    *,
    parameters: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b5c7e85acb7af40ff016f5d83f7be21a0fbc25cd6f23107832acf22632a062e(
    *,
    env_name: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136318fbcabb58a5b91baf1422530fba8dc1faaed566748f2181793fa12c4d45(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d5507e30df6bdf1169c815cb74ee5f598b27732a23ea6ff77ccd09d0844b64e(
    *,
    spider_ec2_instance: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResourcesSpiderEc2Instance, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff864750227c607a192aa268d7cd1b06cdbaa69dc0b353185f994cc5c1557d8(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
