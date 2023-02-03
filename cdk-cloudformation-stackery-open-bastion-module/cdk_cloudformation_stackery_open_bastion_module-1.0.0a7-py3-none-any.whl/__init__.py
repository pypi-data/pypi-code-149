'''
# stackery-open-bastion-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Stackery::Open::Bastion::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Stackery::Open::Bastion::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Stackery::Open::Bastion::MODULE \
  --publisher-id c7a1566696d21e673a0e14208c79edfc9dd639e3 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/c7a1566696d21e673a0e14208c79edfc9dd639e3/Stackery-Open-Bastion-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Stackery::Open::Bastion::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fstackery-open-bastion-module+v1.0.0).
* Issues related to `Stackery::Open::Bastion::MODULE` should be reported to the [publisher](undefined).

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


class CfnBastionModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModule",
):
    '''A CloudFormation ``Stackery::Open::Bastion::MODULE``.

    :cloudformationResource: Stackery::Open::Bastion::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnBastionModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnBastionModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Stackery::Open::Bastion::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8544524a56a42708391226c10e406bcd71eea010fe66732b88c08cb98cad3131)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBastionModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnBastionModuleProps":
        '''Resource props.'''
        return typing.cast("CfnBastionModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnBastionModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnBastionModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnBastionModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type Stackery::Open::Bastion::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnBastionModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnBastionModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnBastionModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__618e3797321160b7b0e9d5989f92b164f67052477818382472b91ac6aa688135)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnBastionModulePropsParameters"]:
        '''
        :schema: CfnBastionModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnBastionModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnBastionModulePropsResources"]:
        '''
        :schema: CfnBastionModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnBastionModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "instance_class": "instanceClass",
        "vpc_id": "vpcId",
        "vpc_subnets": "vpcSubnets",
    },
)
class CfnBastionModulePropsParameters:
    def __init__(
        self,
        *,
        instance_class: typing.Optional[typing.Union["CfnBastionModulePropsParametersInstanceClass", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_id: typing.Optional[typing.Union["CfnBastionModulePropsParametersVpcId", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_subnets: typing.Optional[typing.Union["CfnBastionModulePropsParametersVpcSubnets", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param instance_class: EC2 instance class to provision.
        :param vpc_id: VPC to run bastion server in.
        :param vpc_subnets: Subnets to pick from to run a bastion server in.

        :schema: CfnBastionModulePropsParameters
        '''
        if isinstance(instance_class, dict):
            instance_class = CfnBastionModulePropsParametersInstanceClass(**instance_class)
        if isinstance(vpc_id, dict):
            vpc_id = CfnBastionModulePropsParametersVpcId(**vpc_id)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = CfnBastionModulePropsParametersVpcSubnets(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a8f3ce570b2fd646f6d2fde528e81e4a1b78f1e9fe1851dd47769811714d98)
            check_type(argname="argument instance_class", value=instance_class, expected_type=type_hints["instance_class"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_class is not None:
            self._values["instance_class"] = instance_class
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def instance_class(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersInstanceClass"]:
        '''EC2 instance class to provision.

        :schema: CfnBastionModulePropsParameters#InstanceClass
        '''
        result = self._values.get("instance_class")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersInstanceClass"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnBastionModulePropsParametersVpcId"]:
        '''VPC to run bastion server in.

        :schema: CfnBastionModulePropsParameters#VPCId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersVpcId"], result)

    @builtins.property
    def vpc_subnets(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersVpcSubnets"]:
        '''Subnets to pick from to run a bastion server in.

        :schema: CfnBastionModulePropsParameters#VPCSubnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersVpcSubnets"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParametersInstanceClass",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersInstanceClass:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EC2 instance class to provision.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersInstanceClass
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41bf5ec10e70ccd01524323dc31b1693f82f9a7f9ab494581be75a6c32dd818d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersInstanceClass#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersInstanceClass#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersInstanceClass(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersVpcId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''VPC to run bastion server in.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersVpcId
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d3d56fd14b524a55fc08fc7be50039db15300d27613cb8e08afb38325bdc834)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersVpcId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParametersVpcSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersVpcSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Subnets to pick from to run a bastion server in.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersVpcSubnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee644f13baeb984955fae7095d429bc9efb44a70f9f5e662c04d23b1f8ece286)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersVpcSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_group": "autoScalingGroup",
        "cloud_watch_agent_auto_update": "cloudWatchAgentAutoUpdate",
        "cloud_watch_agent_update_and_start": "cloudWatchAgentUpdateAndStart",
        "iam_instance_profile": "iamInstanceProfile",
        "iam_role": "iamRole",
        "instances_security_group": "instancesSecurityGroup",
        "launch_configuration": "launchConfiguration",
        "ssm_agent_auto_update": "ssmAgentAutoUpdate",
    },
)
class CfnBastionModulePropsResources:
    def __init__(
        self,
        *,
        auto_scaling_group: typing.Optional[typing.Union["CfnBastionModulePropsResourcesAutoScalingGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_watch_agent_auto_update: typing.Optional[typing.Union["CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate", typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_watch_agent_update_and_start: typing.Optional[typing.Union["CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart", typing.Dict[builtins.str, typing.Any]]] = None,
        iam_instance_profile: typing.Optional[typing.Union["CfnBastionModulePropsResourcesIamInstanceProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        iam_role: typing.Optional[typing.Union["CfnBastionModulePropsResourcesIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        instances_security_group: typing.Optional[typing.Union["CfnBastionModulePropsResourcesInstancesSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        launch_configuration: typing.Optional[typing.Union["CfnBastionModulePropsResourcesLaunchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        ssm_agent_auto_update: typing.Optional[typing.Union["CfnBastionModulePropsResourcesSsmAgentAutoUpdate", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_scaling_group: 
        :param cloud_watch_agent_auto_update: 
        :param cloud_watch_agent_update_and_start: 
        :param iam_instance_profile: 
        :param iam_role: 
        :param instances_security_group: 
        :param launch_configuration: 
        :param ssm_agent_auto_update: 

        :schema: CfnBastionModulePropsResources
        '''
        if isinstance(auto_scaling_group, dict):
            auto_scaling_group = CfnBastionModulePropsResourcesAutoScalingGroup(**auto_scaling_group)
        if isinstance(cloud_watch_agent_auto_update, dict):
            cloud_watch_agent_auto_update = CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate(**cloud_watch_agent_auto_update)
        if isinstance(cloud_watch_agent_update_and_start, dict):
            cloud_watch_agent_update_and_start = CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart(**cloud_watch_agent_update_and_start)
        if isinstance(iam_instance_profile, dict):
            iam_instance_profile = CfnBastionModulePropsResourcesIamInstanceProfile(**iam_instance_profile)
        if isinstance(iam_role, dict):
            iam_role = CfnBastionModulePropsResourcesIamRole(**iam_role)
        if isinstance(instances_security_group, dict):
            instances_security_group = CfnBastionModulePropsResourcesInstancesSecurityGroup(**instances_security_group)
        if isinstance(launch_configuration, dict):
            launch_configuration = CfnBastionModulePropsResourcesLaunchConfiguration(**launch_configuration)
        if isinstance(ssm_agent_auto_update, dict):
            ssm_agent_auto_update = CfnBastionModulePropsResourcesSsmAgentAutoUpdate(**ssm_agent_auto_update)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6bd5e86647dbc121e82a524853f89c10ab3f4637d1698c3c0eb5bce022f8786)
            check_type(argname="argument auto_scaling_group", value=auto_scaling_group, expected_type=type_hints["auto_scaling_group"])
            check_type(argname="argument cloud_watch_agent_auto_update", value=cloud_watch_agent_auto_update, expected_type=type_hints["cloud_watch_agent_auto_update"])
            check_type(argname="argument cloud_watch_agent_update_and_start", value=cloud_watch_agent_update_and_start, expected_type=type_hints["cloud_watch_agent_update_and_start"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument instances_security_group", value=instances_security_group, expected_type=type_hints["instances_security_group"])
            check_type(argname="argument launch_configuration", value=launch_configuration, expected_type=type_hints["launch_configuration"])
            check_type(argname="argument ssm_agent_auto_update", value=ssm_agent_auto_update, expected_type=type_hints["ssm_agent_auto_update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_scaling_group is not None:
            self._values["auto_scaling_group"] = auto_scaling_group
        if cloud_watch_agent_auto_update is not None:
            self._values["cloud_watch_agent_auto_update"] = cloud_watch_agent_auto_update
        if cloud_watch_agent_update_and_start is not None:
            self._values["cloud_watch_agent_update_and_start"] = cloud_watch_agent_update_and_start
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if instances_security_group is not None:
            self._values["instances_security_group"] = instances_security_group
        if launch_configuration is not None:
            self._values["launch_configuration"] = launch_configuration
        if ssm_agent_auto_update is not None:
            self._values["ssm_agent_auto_update"] = ssm_agent_auto_update

    @builtins.property
    def auto_scaling_group(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesAutoScalingGroup"]:
        '''
        :schema: CfnBastionModulePropsResources#AutoScalingGroup
        '''
        result = self._values.get("auto_scaling_group")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesAutoScalingGroup"], result)

    @builtins.property
    def cloud_watch_agent_auto_update(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate"]:
        '''
        :schema: CfnBastionModulePropsResources#CloudWatchAgentAutoUpdate
        '''
        result = self._values.get("cloud_watch_agent_auto_update")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate"], result)

    @builtins.property
    def cloud_watch_agent_update_and_start(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart"]:
        '''
        :schema: CfnBastionModulePropsResources#CloudWatchAgentUpdateAndStart
        '''
        result = self._values.get("cloud_watch_agent_update_and_start")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart"], result)

    @builtins.property
    def iam_instance_profile(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesIamInstanceProfile"]:
        '''
        :schema: CfnBastionModulePropsResources#IAMInstanceProfile
        '''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesIamInstanceProfile"], result)

    @builtins.property
    def iam_role(self) -> typing.Optional["CfnBastionModulePropsResourcesIamRole"]:
        '''
        :schema: CfnBastionModulePropsResources#IAMRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesIamRole"], result)

    @builtins.property
    def instances_security_group(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesInstancesSecurityGroup"]:
        '''
        :schema: CfnBastionModulePropsResources#InstancesSecurityGroup
        '''
        result = self._values.get("instances_security_group")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesInstancesSecurityGroup"], result)

    @builtins.property
    def launch_configuration(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesLaunchConfiguration"]:
        '''
        :schema: CfnBastionModulePropsResources#LaunchConfiguration
        '''
        result = self._values.get("launch_configuration")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesLaunchConfiguration"], result)

    @builtins.property
    def ssm_agent_auto_update(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesSsmAgentAutoUpdate"]:
        '''
        :schema: CfnBastionModulePropsResources#SSMAgentAutoUpdate
        '''
        result = self._values.get("ssm_agent_auto_update")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesSsmAgentAutoUpdate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesAutoScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesAutoScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesAutoScalingGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d5e33146c62423ecf8ce56108ad6df529cea67a63daa4d5ad4157eb61afc58)
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
        :schema: CfnBastionModulePropsResourcesAutoScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesAutoScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesAutoScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414dac0d228a8f957e5a006b1a467206d5b9b8985e58221128ea067da7568108)
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
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79e1449a77436f393d95106700f2738e99dc7a0a3d10ada0fb97422710a79b88)
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
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesIamInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesIamInstanceProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesIamInstanceProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8676be576da4dbd981d0131916e49ad591f76592286cb62526ed5321bd3e21)
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
        :schema: CfnBastionModulePropsResourcesIamInstanceProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesIamInstanceProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesIamInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesIamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__321ab99ae221b58374a6e73b153647e3d2c3d892812e590349287fa50f94bd6e)
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
        :schema: CfnBastionModulePropsResourcesIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesInstancesSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesInstancesSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesInstancesSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a45e2300458882b03dd5267e58a9b85304e1c0bb606ed4c975135107fc8069d4)
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
        :schema: CfnBastionModulePropsResourcesInstancesSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesInstancesSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesInstancesSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesLaunchConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf43ec8b8ce572ecf131a5274a6c7e26277ad4553ee541ef9560f0389e3587a5)
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
        :schema: CfnBastionModulePropsResourcesLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesSsmAgentAutoUpdate",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesSsmAgentAutoUpdate:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesSsmAgentAutoUpdate
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ae92b2d03f9812557be5c853eb5c789c77938b902e2ff91c3914d1f2beb08e0)
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
        :schema: CfnBastionModulePropsResourcesSsmAgentAutoUpdate#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesSsmAgentAutoUpdate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesSsmAgentAutoUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBastionModule",
    "CfnBastionModuleProps",
    "CfnBastionModulePropsParameters",
    "CfnBastionModulePropsParametersInstanceClass",
    "CfnBastionModulePropsParametersVpcId",
    "CfnBastionModulePropsParametersVpcSubnets",
    "CfnBastionModulePropsResources",
    "CfnBastionModulePropsResourcesAutoScalingGroup",
    "CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate",
    "CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart",
    "CfnBastionModulePropsResourcesIamInstanceProfile",
    "CfnBastionModulePropsResourcesIamRole",
    "CfnBastionModulePropsResourcesInstancesSecurityGroup",
    "CfnBastionModulePropsResourcesLaunchConfiguration",
    "CfnBastionModulePropsResourcesSsmAgentAutoUpdate",
]

publication.publish()

def _typecheckingstub__8544524a56a42708391226c10e406bcd71eea010fe66732b88c08cb98cad3131(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnBastionModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnBastionModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618e3797321160b7b0e9d5989f92b164f67052477818382472b91ac6aa688135(
    *,
    parameters: typing.Optional[typing.Union[CfnBastionModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnBastionModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a8f3ce570b2fd646f6d2fde528e81e4a1b78f1e9fe1851dd47769811714d98(
    *,
    instance_class: typing.Optional[typing.Union[CfnBastionModulePropsParametersInstanceClass, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_id: typing.Optional[typing.Union[CfnBastionModulePropsParametersVpcId, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_subnets: typing.Optional[typing.Union[CfnBastionModulePropsParametersVpcSubnets, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41bf5ec10e70ccd01524323dc31b1693f82f9a7f9ab494581be75a6c32dd818d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d3d56fd14b524a55fc08fc7be50039db15300d27613cb8e08afb38325bdc834(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee644f13baeb984955fae7095d429bc9efb44a70f9f5e662c04d23b1f8ece286(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6bd5e86647dbc121e82a524853f89c10ab3f4637d1698c3c0eb5bce022f8786(
    *,
    auto_scaling_group: typing.Optional[typing.Union[CfnBastionModulePropsResourcesAutoScalingGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_watch_agent_auto_update: typing.Optional[typing.Union[CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_watch_agent_update_and_start: typing.Optional[typing.Union[CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart, typing.Dict[builtins.str, typing.Any]]] = None,
    iam_instance_profile: typing.Optional[typing.Union[CfnBastionModulePropsResourcesIamInstanceProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    iam_role: typing.Optional[typing.Union[CfnBastionModulePropsResourcesIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    instances_security_group: typing.Optional[typing.Union[CfnBastionModulePropsResourcesInstancesSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    launch_configuration: typing.Optional[typing.Union[CfnBastionModulePropsResourcesLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    ssm_agent_auto_update: typing.Optional[typing.Union[CfnBastionModulePropsResourcesSsmAgentAutoUpdate, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d5e33146c62423ecf8ce56108ad6df529cea67a63daa4d5ad4157eb61afc58(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414dac0d228a8f957e5a006b1a467206d5b9b8985e58221128ea067da7568108(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79e1449a77436f393d95106700f2738e99dc7a0a3d10ada0fb97422710a79b88(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8676be576da4dbd981d0131916e49ad591f76592286cb62526ed5321bd3e21(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__321ab99ae221b58374a6e73b153647e3d2c3d892812e590349287fa50f94bd6e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a45e2300458882b03dd5267e58a9b85304e1c0bb606ed4c975135107fc8069d4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf43ec8b8ce572ecf131a5274a6c7e26277ad4553ee541ef9560f0389e3587a5(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae92b2d03f9812557be5c853eb5c789c77938b902e2ff91c3914d1f2beb08e0(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
