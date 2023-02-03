'''
# freyraim-spider-loadbalancer-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::Spider::LoadBalancer::MODULE` v1.1.0.

## Description

Schema for Module Fragment of type FreyrAIM::Spider::LoadBalancer::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::Spider::LoadBalancer::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-Spider-LoadBalancer-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::Spider::LoadBalancer::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-spider-loadbalancer-module+v1.1.0).
* Issues related to `FreyrAIM::Spider::LoadBalancer::MODULE` should be reported to the [publisher](undefined).

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


class CfnLoadBalancerModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModule",
):
    '''A CloudFormation ``FreyrAIM::Spider::LoadBalancer::MODULE``.

    :cloudformationResource: FreyrAIM::Spider::LoadBalancer::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::Spider::LoadBalancer::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4df6c32e5f7e46b6b7fc00c2e6056450b6b69946224e0763afd98f7fa5b19ed9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoadBalancerModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnLoadBalancerModuleProps":
        '''Resource props.'''
        return typing.cast("CfnLoadBalancerModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnLoadBalancerModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::Spider::LoadBalancer::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnLoadBalancerModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnLoadBalancerModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnLoadBalancerModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10098038d0e93b581ee2aab3e3a042fb8edb9db21f083d8e13c9f26318ef9d72)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnLoadBalancerModulePropsParameters"]:
        '''
        :schema: CfnLoadBalancerModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnLoadBalancerModulePropsResources"]:
        '''
        :schema: CfnLoadBalancerModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "elb_bucket_name": "elbBucketName",
        "env_name": "envName",
        "image_digest": "imageDigest",
        "run_time": "runTime",
        "vpc_id": "vpcId",
    },
)
class CfnLoadBalancerModulePropsParameters:
    def __init__(
        self,
        *,
        elb_bucket_name: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersElbBucketName", typing.Dict[builtins.str, typing.Any]]] = None,
        env_name: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
        image_digest: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersImageDigest", typing.Dict[builtins.str, typing.Any]]] = None,
        run_time: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersRunTime", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_id: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersVpcId", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_bucket_name: The ELB logs bucket name.
        :param env_name: The environment name.
        :param image_digest: The ImageDigest.
        :param run_time: The RunTime.
        :param vpc_id: Vpc-ID.

        :schema: CfnLoadBalancerModulePropsParameters
        '''
        if isinstance(elb_bucket_name, dict):
            elb_bucket_name = CfnLoadBalancerModulePropsParametersElbBucketName(**elb_bucket_name)
        if isinstance(env_name, dict):
            env_name = CfnLoadBalancerModulePropsParametersEnvName(**env_name)
        if isinstance(image_digest, dict):
            image_digest = CfnLoadBalancerModulePropsParametersImageDigest(**image_digest)
        if isinstance(run_time, dict):
            run_time = CfnLoadBalancerModulePropsParametersRunTime(**run_time)
        if isinstance(vpc_id, dict):
            vpc_id = CfnLoadBalancerModulePropsParametersVpcId(**vpc_id)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf28e4d818ae30e84fe1df258303f860817916754d15de600be8bf07e0e0380)
            check_type(argname="argument elb_bucket_name", value=elb_bucket_name, expected_type=type_hints["elb_bucket_name"])
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
            check_type(argname="argument image_digest", value=image_digest, expected_type=type_hints["image_digest"])
            check_type(argname="argument run_time", value=run_time, expected_type=type_hints["run_time"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if elb_bucket_name is not None:
            self._values["elb_bucket_name"] = elb_bucket_name
        if env_name is not None:
            self._values["env_name"] = env_name
        if image_digest is not None:
            self._values["image_digest"] = image_digest
        if run_time is not None:
            self._values["run_time"] = run_time
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def elb_bucket_name(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsParametersElbBucketName"]:
        '''The ELB logs bucket name.

        :schema: CfnLoadBalancerModulePropsParameters#ELBBucketName
        '''
        result = self._values.get("elb_bucket_name")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsParametersElbBucketName"], result)

    @builtins.property
    def env_name(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnLoadBalancerModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsParametersEnvName"], result)

    @builtins.property
    def image_digest(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsParametersImageDigest"]:
        '''The ImageDigest.

        :schema: CfnLoadBalancerModulePropsParameters#ImageDigest
        '''
        result = self._values.get("image_digest")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsParametersImageDigest"], result)

    @builtins.property
    def run_time(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsParametersRunTime"]:
        '''The RunTime.

        :schema: CfnLoadBalancerModulePropsParameters#RunTime
        '''
        result = self._values.get("run_time")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsParametersRunTime"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnLoadBalancerModulePropsParametersVpcId"]:
        '''Vpc-ID.

        :schema: CfnLoadBalancerModulePropsParameters#VpcID
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsParametersVpcId"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsParametersElbBucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLoadBalancerModulePropsParametersElbBucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The ELB logs bucket name.

        :param description: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsParametersElbBucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aac4e0d272b56192dfe08d4b8e883f0045ab3e5827f06682796888c00e24231)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersElbBucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersElbBucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsParametersElbBucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLoadBalancerModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4c8c75f7c9d4b602973edf5203f0e07d582e3ad4b58877c5f45be26da2e758a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsParametersImageDigest",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLoadBalancerModulePropsParametersImageDigest:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The ImageDigest.

        :param description: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsParametersImageDigest
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be38980966d9ab1fa784f5e97dadd2ff4adcb3b7c71fdbf8dbdc9b7f2338969)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersImageDigest#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersImageDigest#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsParametersImageDigest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsParametersRunTime",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLoadBalancerModulePropsParametersRunTime:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The RunTime.

        :param description: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsParametersRunTime
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__147c62555af9b7a3c288beec90a07b62d763d99ffc6928e8c6ffef0bf339beb8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersRunTime#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersRunTime#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsParametersRunTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLoadBalancerModulePropsParametersVpcId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Vpc-ID.

        :param description: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsParametersVpcId
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211b1c05ab34b76ac7a17eee6879c1b7d5202d451569195349be6ae92723d41e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersVpcId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLoadBalancerModulePropsParametersVpcId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsParametersVpcId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "elb_bucket": "elbBucket",
        "elb_bucket_policy": "elbBucketPolicy",
        "listener1": "listener1",
        "listener_rule1": "listenerRule1",
        "load_balancer1": "loadBalancer1",
        "spider_ec2_instance": "spiderEc2Instance",
        "target_group1": "targetGroup1",
        "target_group2": "targetGroup2",
    },
)
class CfnLoadBalancerModulePropsResources:
    def __init__(
        self,
        *,
        elb_bucket: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesElbBucket", typing.Dict[builtins.str, typing.Any]]] = None,
        elb_bucket_policy: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesElbBucketPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        listener1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListener1", typing.Dict[builtins.str, typing.Any]]] = None,
        listener_rule1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListenerRule1", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancer1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesLoadBalancer1", typing.Dict[builtins.str, typing.Any]]] = None,
        spider_ec2_instance: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesSpiderEc2Instance", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesTargetGroup1", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group2: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesTargetGroup2", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_bucket: 
        :param elb_bucket_policy: 
        :param listener1: 
        :param listener_rule1: 
        :param load_balancer1: 
        :param spider_ec2_instance: 
        :param target_group1: 
        :param target_group2: 

        :schema: CfnLoadBalancerModulePropsResources
        '''
        if isinstance(elb_bucket, dict):
            elb_bucket = CfnLoadBalancerModulePropsResourcesElbBucket(**elb_bucket)
        if isinstance(elb_bucket_policy, dict):
            elb_bucket_policy = CfnLoadBalancerModulePropsResourcesElbBucketPolicy(**elb_bucket_policy)
        if isinstance(listener1, dict):
            listener1 = CfnLoadBalancerModulePropsResourcesListener1(**listener1)
        if isinstance(listener_rule1, dict):
            listener_rule1 = CfnLoadBalancerModulePropsResourcesListenerRule1(**listener_rule1)
        if isinstance(load_balancer1, dict):
            load_balancer1 = CfnLoadBalancerModulePropsResourcesLoadBalancer1(**load_balancer1)
        if isinstance(spider_ec2_instance, dict):
            spider_ec2_instance = CfnLoadBalancerModulePropsResourcesSpiderEc2Instance(**spider_ec2_instance)
        if isinstance(target_group1, dict):
            target_group1 = CfnLoadBalancerModulePropsResourcesTargetGroup1(**target_group1)
        if isinstance(target_group2, dict):
            target_group2 = CfnLoadBalancerModulePropsResourcesTargetGroup2(**target_group2)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0051745d8738630841c0a8061edfdb4c4d33e6043c5319eb8031b6458f8ef8)
            check_type(argname="argument elb_bucket", value=elb_bucket, expected_type=type_hints["elb_bucket"])
            check_type(argname="argument elb_bucket_policy", value=elb_bucket_policy, expected_type=type_hints["elb_bucket_policy"])
            check_type(argname="argument listener1", value=listener1, expected_type=type_hints["listener1"])
            check_type(argname="argument listener_rule1", value=listener_rule1, expected_type=type_hints["listener_rule1"])
            check_type(argname="argument load_balancer1", value=load_balancer1, expected_type=type_hints["load_balancer1"])
            check_type(argname="argument spider_ec2_instance", value=spider_ec2_instance, expected_type=type_hints["spider_ec2_instance"])
            check_type(argname="argument target_group1", value=target_group1, expected_type=type_hints["target_group1"])
            check_type(argname="argument target_group2", value=target_group2, expected_type=type_hints["target_group2"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if elb_bucket is not None:
            self._values["elb_bucket"] = elb_bucket
        if elb_bucket_policy is not None:
            self._values["elb_bucket_policy"] = elb_bucket_policy
        if listener1 is not None:
            self._values["listener1"] = listener1
        if listener_rule1 is not None:
            self._values["listener_rule1"] = listener_rule1
        if load_balancer1 is not None:
            self._values["load_balancer1"] = load_balancer1
        if spider_ec2_instance is not None:
            self._values["spider_ec2_instance"] = spider_ec2_instance
        if target_group1 is not None:
            self._values["target_group1"] = target_group1
        if target_group2 is not None:
            self._values["target_group2"] = target_group2

    @builtins.property
    def elb_bucket(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesElbBucket"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#ELBBucket
        '''
        result = self._values.get("elb_bucket")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesElbBucket"], result)

    @builtins.property
    def elb_bucket_policy(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesElbBucketPolicy"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#ELBBucketPolicy
        '''
        result = self._values.get("elb_bucket_policy")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesElbBucketPolicy"], result)

    @builtins.property
    def listener1(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesListener1"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#Listener1
        '''
        result = self._values.get("listener1")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesListener1"], result)

    @builtins.property
    def listener_rule1(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesListenerRule1"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#ListenerRule1
        '''
        result = self._values.get("listener_rule1")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesListenerRule1"], result)

    @builtins.property
    def load_balancer1(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesLoadBalancer1"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#LoadBalancer1
        '''
        result = self._values.get("load_balancer1")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesLoadBalancer1"], result)

    @builtins.property
    def spider_ec2_instance(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesSpiderEc2Instance"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#SpiderEC2Instance
        '''
        result = self._values.get("spider_ec2_instance")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesSpiderEc2Instance"], result)

    @builtins.property
    def target_group1(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesTargetGroup1"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#TargetGroup1
        '''
        result = self._values.get("target_group1")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesTargetGroup1"], result)

    @builtins.property
    def target_group2(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesTargetGroup2"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#TargetGroup2
        '''
        result = self._values.get("target_group2")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesTargetGroup2"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesElbBucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesElbBucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesElbBucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e7ab56fbf3610c842a89b37de5d85ace82961f8bab63aa65b5cbd3aacf1e421)
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
        :schema: CfnLoadBalancerModulePropsResourcesElbBucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesElbBucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesElbBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesElbBucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesElbBucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesElbBucketPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38415afb2cc24033e7d4e2ac20cfc9b1881ed1f428b08b50dd930e7cb1ebf26c)
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
        :schema: CfnLoadBalancerModulePropsResourcesElbBucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesElbBucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesElbBucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListener1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesListener1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesListener1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bf2c5a540737e659eea082a48ff7ea03e2ee92bf05f78694239dbfe690d7482)
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
        :schema: CfnLoadBalancerModulePropsResourcesListener1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesListener1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesListener1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListenerRule1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesListenerRule1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesListenerRule1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a790c558cf22dd6055c08d10323290b629e222a39018d5f3e0403c496b66e771)
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
        :schema: CfnLoadBalancerModulePropsResourcesListenerRule1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesListenerRule1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesListenerRule1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesLoadBalancer1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesLoadBalancer1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesLoadBalancer1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__587d24953e75b4be91bb7e0e2c63afea1f799a82e95107116a86ae32d74de183)
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
        :schema: CfnLoadBalancerModulePropsResourcesLoadBalancer1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesLoadBalancer1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesLoadBalancer1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesSpiderEc2Instance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesSpiderEc2Instance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesSpiderEc2Instance
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79196a4adb9a86aa48eec324e918ec9673527982d31ff72f65bb11025e4f271b)
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
        :schema: CfnLoadBalancerModulePropsResourcesSpiderEc2Instance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesSpiderEc2Instance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesSpiderEc2Instance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesTargetGroup1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesTargetGroup1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32938ce6a263fe93c01994d1113213482661898cf8d518eab76102a6ac63ec4b)
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
        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesTargetGroup1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-loadbalancer-module.CfnLoadBalancerModulePropsResourcesTargetGroup2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesTargetGroup2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28913ec877c17a6692604ec624ae82a6b9fe363d24e71449628af4f0eab1b43f)
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
        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesTargetGroup2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLoadBalancerModule",
    "CfnLoadBalancerModuleProps",
    "CfnLoadBalancerModulePropsParameters",
    "CfnLoadBalancerModulePropsParametersElbBucketName",
    "CfnLoadBalancerModulePropsParametersEnvName",
    "CfnLoadBalancerModulePropsParametersImageDigest",
    "CfnLoadBalancerModulePropsParametersRunTime",
    "CfnLoadBalancerModulePropsParametersVpcId",
    "CfnLoadBalancerModulePropsResources",
    "CfnLoadBalancerModulePropsResourcesElbBucket",
    "CfnLoadBalancerModulePropsResourcesElbBucketPolicy",
    "CfnLoadBalancerModulePropsResourcesListener1",
    "CfnLoadBalancerModulePropsResourcesListenerRule1",
    "CfnLoadBalancerModulePropsResourcesLoadBalancer1",
    "CfnLoadBalancerModulePropsResourcesSpiderEc2Instance",
    "CfnLoadBalancerModulePropsResourcesTargetGroup1",
    "CfnLoadBalancerModulePropsResourcesTargetGroup2",
]

publication.publish()

def _typecheckingstub__4df6c32e5f7e46b6b7fc00c2e6056450b6b69946224e0763afd98f7fa5b19ed9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10098038d0e93b581ee2aab3e3a042fb8edb9db21f083d8e13c9f26318ef9d72(
    *,
    parameters: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf28e4d818ae30e84fe1df258303f860817916754d15de600be8bf07e0e0380(
    *,
    elb_bucket_name: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersElbBucketName, typing.Dict[builtins.str, typing.Any]]] = None,
    env_name: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
    image_digest: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersImageDigest, typing.Dict[builtins.str, typing.Any]]] = None,
    run_time: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersRunTime, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_id: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersVpcId, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aac4e0d272b56192dfe08d4b8e883f0045ab3e5827f06682796888c00e24231(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c8c75f7c9d4b602973edf5203f0e07d582e3ad4b58877c5f45be26da2e758a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be38980966d9ab1fa784f5e97dadd2ff4adcb3b7c71fdbf8dbdc9b7f2338969(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147c62555af9b7a3c288beec90a07b62d763d99ffc6928e8c6ffef0bf339beb8(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211b1c05ab34b76ac7a17eee6879c1b7d5202d451569195349be6ae92723d41e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0051745d8738630841c0a8061edfdb4c4d33e6043c5319eb8031b6458f8ef8(
    *,
    elb_bucket: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesElbBucket, typing.Dict[builtins.str, typing.Any]]] = None,
    elb_bucket_policy: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesElbBucketPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    listener1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListener1, typing.Dict[builtins.str, typing.Any]]] = None,
    listener_rule1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListenerRule1, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancer1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesLoadBalancer1, typing.Dict[builtins.str, typing.Any]]] = None,
    spider_ec2_instance: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesSpiderEc2Instance, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesTargetGroup1, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group2: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesTargetGroup2, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e7ab56fbf3610c842a89b37de5d85ace82961f8bab63aa65b5cbd3aacf1e421(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38415afb2cc24033e7d4e2ac20cfc9b1881ed1f428b08b50dd930e7cb1ebf26c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bf2c5a540737e659eea082a48ff7ea03e2ee92bf05f78694239dbfe690d7482(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a790c558cf22dd6055c08d10323290b629e222a39018d5f3e0403c496b66e771(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__587d24953e75b4be91bb7e0e2c63afea1f799a82e95107116a86ae32d74de183(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79196a4adb9a86aa48eec324e918ec9673527982d31ff72f65bb11025e4f271b(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32938ce6a263fe93c01994d1113213482661898cf8d518eab76102a6ac63ec4b(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28913ec877c17a6692604ec624ae82a6b9fe363d24e71449628af4f0eab1b43f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
