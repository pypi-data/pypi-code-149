'''
# freyraim-impactapi-loadbalancer-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::ImpactApi::LoadBalancer::MODULE` v1.2.0.

## Description

Schema for Module Fragment of type FreyrAIM::ImpactApi::LoadBalancer::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::ImpactApi::LoadBalancer::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-ImpactApi-LoadBalancer-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::ImpactApi::LoadBalancer::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-impactapi-loadbalancer-module+v1.2.0).
* Issues related to `FreyrAIM::ImpactApi::LoadBalancer::MODULE` should be reported to the [publisher](undefined).

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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModule",
):
    '''A CloudFormation ``FreyrAIM::ImpactApi::LoadBalancer::MODULE``.

    :cloudformationResource: FreyrAIM::ImpactApi::LoadBalancer::MODULE
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
        '''Create a new ``FreyrAIM::ImpactApi::LoadBalancer::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4ae2d1dc93e2a11e366d72e5ba0d1cc7f7d44f78d9842a00f8cd512323cff3)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModuleProps",
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
        '''Schema for Module Fragment of type FreyrAIM::ImpactApi::LoadBalancer::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnLoadBalancerModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnLoadBalancerModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnLoadBalancerModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3333221018c0e56b3988453ec2942cb7c67abbdb4fb8e559490a636b8489d845)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "elb_bucket_name": "elbBucketName",
        "env_name": "envName",
        "image_digest": "imageDigest",
    },
)
class CfnLoadBalancerModulePropsParameters:
    def __init__(
        self,
        *,
        elb_bucket_name: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersElbBucketName", typing.Dict[builtins.str, typing.Any]]] = None,
        env_name: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
        image_digest: typing.Optional[typing.Union["CfnLoadBalancerModulePropsParametersImageDigest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_bucket_name: The ELB logs bucket name.
        :param env_name: The environment name.
        :param image_digest: The ImageDigest.

        :schema: CfnLoadBalancerModulePropsParameters
        '''
        if isinstance(elb_bucket_name, dict):
            elb_bucket_name = CfnLoadBalancerModulePropsParametersElbBucketName(**elb_bucket_name)
        if isinstance(env_name, dict):
            env_name = CfnLoadBalancerModulePropsParametersEnvName(**env_name)
        if isinstance(image_digest, dict):
            image_digest = CfnLoadBalancerModulePropsParametersImageDigest(**image_digest)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__269bde64111a7e9fffe5fe2cf16e1869d9bd230fd3eef69ebadd3af946e2c838)
            check_type(argname="argument elb_bucket_name", value=elb_bucket_name, expected_type=type_hints["elb_bucket_name"])
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
            check_type(argname="argument image_digest", value=image_digest, expected_type=type_hints["image_digest"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if elb_bucket_name is not None:
            self._values["elb_bucket_name"] = elb_bucket_name
        if env_name is not None:
            self._values["env_name"] = env_name
        if image_digest is not None:
            self._values["image_digest"] = image_digest

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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsParametersElbBucketName",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af9b37d70943353449b6a5be3fc26100da156440eee88f73d3e084c831cd7f69)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsParametersEnvName",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b7a65de2dee6d0fd7290dc49e7c66b854e27e6d47f9aa4e056bc58f3dbccf19)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsParametersImageDigest",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b23afa2c121d681b756cf3ea97ea1c6a84ed3bb72f343b636dc02fd8ebe58d6f)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "elb_bucket": "elbBucket",
        "elb_bucket_policy": "elbBucketPolicy",
        "impact_classify_ec2_instance": "impactClassifyEc2Instance",
        "listener1": "listener1",
        "listener2": "listener2",
        "listener3": "listener3",
        "listener_rule1": "listenerRule1",
        "listener_rule2": "listenerRule2",
        "listener_rule3": "listenerRule3",
        "load_balancer1": "loadBalancer1",
        "target_group1": "targetGroup1",
        "target_group2": "targetGroup2",
        "target_group3": "targetGroup3",
    },
)
class CfnLoadBalancerModulePropsResources:
    def __init__(
        self,
        *,
        elb_bucket: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesElbBucket", typing.Dict[builtins.str, typing.Any]]] = None,
        elb_bucket_policy: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesElbBucketPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        impact_classify_ec2_instance: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance", typing.Dict[builtins.str, typing.Any]]] = None,
        listener1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListener1", typing.Dict[builtins.str, typing.Any]]] = None,
        listener2: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListener2", typing.Dict[builtins.str, typing.Any]]] = None,
        listener3: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListener3", typing.Dict[builtins.str, typing.Any]]] = None,
        listener_rule1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListenerRule1", typing.Dict[builtins.str, typing.Any]]] = None,
        listener_rule2: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListenerRule2", typing.Dict[builtins.str, typing.Any]]] = None,
        listener_rule3: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesListenerRule3", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancer1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesLoadBalancer1", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group1: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesTargetGroup1", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group2: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesTargetGroup2", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group3: typing.Optional[typing.Union["CfnLoadBalancerModulePropsResourcesTargetGroup3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_bucket: 
        :param elb_bucket_policy: 
        :param impact_classify_ec2_instance: 
        :param listener1: 
        :param listener2: 
        :param listener3: 
        :param listener_rule1: 
        :param listener_rule2: 
        :param listener_rule3: 
        :param load_balancer1: 
        :param target_group1: 
        :param target_group2: 
        :param target_group3: 

        :schema: CfnLoadBalancerModulePropsResources
        '''
        if isinstance(elb_bucket, dict):
            elb_bucket = CfnLoadBalancerModulePropsResourcesElbBucket(**elb_bucket)
        if isinstance(elb_bucket_policy, dict):
            elb_bucket_policy = CfnLoadBalancerModulePropsResourcesElbBucketPolicy(**elb_bucket_policy)
        if isinstance(impact_classify_ec2_instance, dict):
            impact_classify_ec2_instance = CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance(**impact_classify_ec2_instance)
        if isinstance(listener1, dict):
            listener1 = CfnLoadBalancerModulePropsResourcesListener1(**listener1)
        if isinstance(listener2, dict):
            listener2 = CfnLoadBalancerModulePropsResourcesListener2(**listener2)
        if isinstance(listener3, dict):
            listener3 = CfnLoadBalancerModulePropsResourcesListener3(**listener3)
        if isinstance(listener_rule1, dict):
            listener_rule1 = CfnLoadBalancerModulePropsResourcesListenerRule1(**listener_rule1)
        if isinstance(listener_rule2, dict):
            listener_rule2 = CfnLoadBalancerModulePropsResourcesListenerRule2(**listener_rule2)
        if isinstance(listener_rule3, dict):
            listener_rule3 = CfnLoadBalancerModulePropsResourcesListenerRule3(**listener_rule3)
        if isinstance(load_balancer1, dict):
            load_balancer1 = CfnLoadBalancerModulePropsResourcesLoadBalancer1(**load_balancer1)
        if isinstance(target_group1, dict):
            target_group1 = CfnLoadBalancerModulePropsResourcesTargetGroup1(**target_group1)
        if isinstance(target_group2, dict):
            target_group2 = CfnLoadBalancerModulePropsResourcesTargetGroup2(**target_group2)
        if isinstance(target_group3, dict):
            target_group3 = CfnLoadBalancerModulePropsResourcesTargetGroup3(**target_group3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df97f77266fc37d7bb6f7ad0630f50d23bb24cc976beea7b317f5432004a040c)
            check_type(argname="argument elb_bucket", value=elb_bucket, expected_type=type_hints["elb_bucket"])
            check_type(argname="argument elb_bucket_policy", value=elb_bucket_policy, expected_type=type_hints["elb_bucket_policy"])
            check_type(argname="argument impact_classify_ec2_instance", value=impact_classify_ec2_instance, expected_type=type_hints["impact_classify_ec2_instance"])
            check_type(argname="argument listener1", value=listener1, expected_type=type_hints["listener1"])
            check_type(argname="argument listener2", value=listener2, expected_type=type_hints["listener2"])
            check_type(argname="argument listener3", value=listener3, expected_type=type_hints["listener3"])
            check_type(argname="argument listener_rule1", value=listener_rule1, expected_type=type_hints["listener_rule1"])
            check_type(argname="argument listener_rule2", value=listener_rule2, expected_type=type_hints["listener_rule2"])
            check_type(argname="argument listener_rule3", value=listener_rule3, expected_type=type_hints["listener_rule3"])
            check_type(argname="argument load_balancer1", value=load_balancer1, expected_type=type_hints["load_balancer1"])
            check_type(argname="argument target_group1", value=target_group1, expected_type=type_hints["target_group1"])
            check_type(argname="argument target_group2", value=target_group2, expected_type=type_hints["target_group2"])
            check_type(argname="argument target_group3", value=target_group3, expected_type=type_hints["target_group3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if elb_bucket is not None:
            self._values["elb_bucket"] = elb_bucket
        if elb_bucket_policy is not None:
            self._values["elb_bucket_policy"] = elb_bucket_policy
        if impact_classify_ec2_instance is not None:
            self._values["impact_classify_ec2_instance"] = impact_classify_ec2_instance
        if listener1 is not None:
            self._values["listener1"] = listener1
        if listener2 is not None:
            self._values["listener2"] = listener2
        if listener3 is not None:
            self._values["listener3"] = listener3
        if listener_rule1 is not None:
            self._values["listener_rule1"] = listener_rule1
        if listener_rule2 is not None:
            self._values["listener_rule2"] = listener_rule2
        if listener_rule3 is not None:
            self._values["listener_rule3"] = listener_rule3
        if load_balancer1 is not None:
            self._values["load_balancer1"] = load_balancer1
        if target_group1 is not None:
            self._values["target_group1"] = target_group1
        if target_group2 is not None:
            self._values["target_group2"] = target_group2
        if target_group3 is not None:
            self._values["target_group3"] = target_group3

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
    def impact_classify_ec2_instance(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#ImpactClassifyEC2Instance
        '''
        result = self._values.get("impact_classify_ec2_instance")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance"], result)

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
    def listener2(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesListener2"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#Listener2
        '''
        result = self._values.get("listener2")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesListener2"], result)

    @builtins.property
    def listener3(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesListener3"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#Listener3
        '''
        result = self._values.get("listener3")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesListener3"], result)

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
    def listener_rule2(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesListenerRule2"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#ListenerRule2
        '''
        result = self._values.get("listener_rule2")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesListenerRule2"], result)

    @builtins.property
    def listener_rule3(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesListenerRule3"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#ListenerRule3
        '''
        result = self._values.get("listener_rule3")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesListenerRule3"], result)

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

    @builtins.property
    def target_group3(
        self,
    ) -> typing.Optional["CfnLoadBalancerModulePropsResourcesTargetGroup3"]:
        '''
        :schema: CfnLoadBalancerModulePropsResources#TargetGroup3
        '''
        result = self._values.get("target_group3")
        return typing.cast(typing.Optional["CfnLoadBalancerModulePropsResourcesTargetGroup3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesElbBucket",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea845836670adc29dac9fba362b80806ced97821aa63f42910ad89d3d709600a)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesElbBucketPolicy",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e63780ea666c217d91338139a84ef8c5772594a5b9d1cb4919175051ee3f6409)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b5aeb2156a04e482e57b7962280a7295c63c452d304260f2fdaf0282b74187)
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
        :schema: CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListener1",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d4be15938ed3d6525e44d07f3fb9eb6bfbadd9559061d4619b604bf20aa4e04)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListener2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesListener2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesListener2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dd8eeb0af0789eeb249672734adcaab1144809c4217591b5caca543f952f80)
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
        :schema: CfnLoadBalancerModulePropsResourcesListener2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesListener2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesListener2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListener3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesListener3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesListener3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd194803f40cf9085ae6d831a426c0f98e5f9b68bf976ee3b5ec7f8c12ca3ee)
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
        :schema: CfnLoadBalancerModulePropsResourcesListener3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesListener3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesListener3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListenerRule1",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1426cac9480cf1eff50dec0e2f63752a3edfd218989a21963b3f647a139dae3)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListenerRule2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesListenerRule2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesListenerRule2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31f3a30dc68553788e1bc91b8e29da3ca1e7989cf9f1a902261b983d39f5c223)
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
        :schema: CfnLoadBalancerModulePropsResourcesListenerRule2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesListenerRule2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesListenerRule2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesListenerRule3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesListenerRule3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesListenerRule3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376981dff1abc9478b16a955870d06afbc02c3c28094ae2bbdba15ffbf35692f)
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
        :schema: CfnLoadBalancerModulePropsResourcesListenerRule3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesListenerRule3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesListenerRule3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesLoadBalancer1",
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
            type_hints = typing.get_type_hints(_typecheckingstub__139142fe0ffa09dfdabf0bd060da4bb39d4d9299da13a7721fd670b8d7f63f59)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesTargetGroup1",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f00aa2769a669dd1b6b29620032ed673cc9a79519e2ab75f2c315d8d952af82)
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
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesTargetGroup2",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3352e45715b0171ac565d78c52e565ef439332bccbe9e9e3fed7cc880543a920)
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


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-loadbalancer-module.CfnLoadBalancerModulePropsResourcesTargetGroup3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLoadBalancerModulePropsResourcesTargetGroup3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dc8be5181e72b2692e64cdd50d32c0db5a8b8e27d49f2930d053ff8337485f)
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
        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLoadBalancerModulePropsResourcesTargetGroup3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerModulePropsResourcesTargetGroup3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLoadBalancerModule",
    "CfnLoadBalancerModuleProps",
    "CfnLoadBalancerModulePropsParameters",
    "CfnLoadBalancerModulePropsParametersElbBucketName",
    "CfnLoadBalancerModulePropsParametersEnvName",
    "CfnLoadBalancerModulePropsParametersImageDigest",
    "CfnLoadBalancerModulePropsResources",
    "CfnLoadBalancerModulePropsResourcesElbBucket",
    "CfnLoadBalancerModulePropsResourcesElbBucketPolicy",
    "CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance",
    "CfnLoadBalancerModulePropsResourcesListener1",
    "CfnLoadBalancerModulePropsResourcesListener2",
    "CfnLoadBalancerModulePropsResourcesListener3",
    "CfnLoadBalancerModulePropsResourcesListenerRule1",
    "CfnLoadBalancerModulePropsResourcesListenerRule2",
    "CfnLoadBalancerModulePropsResourcesListenerRule3",
    "CfnLoadBalancerModulePropsResourcesLoadBalancer1",
    "CfnLoadBalancerModulePropsResourcesTargetGroup1",
    "CfnLoadBalancerModulePropsResourcesTargetGroup2",
    "CfnLoadBalancerModulePropsResourcesTargetGroup3",
]

publication.publish()

def _typecheckingstub__6e4ae2d1dc93e2a11e366d72e5ba0d1cc7f7d44f78d9842a00f8cd512323cff3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3333221018c0e56b3988453ec2942cb7c67abbdb4fb8e559490a636b8489d845(
    *,
    parameters: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269bde64111a7e9fffe5fe2cf16e1869d9bd230fd3eef69ebadd3af946e2c838(
    *,
    elb_bucket_name: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersElbBucketName, typing.Dict[builtins.str, typing.Any]]] = None,
    env_name: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
    image_digest: typing.Optional[typing.Union[CfnLoadBalancerModulePropsParametersImageDigest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9b37d70943353449b6a5be3fc26100da156440eee88f73d3e084c831cd7f69(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7a65de2dee6d0fd7290dc49e7c66b854e27e6d47f9aa4e056bc58f3dbccf19(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23afa2c121d681b756cf3ea97ea1c6a84ed3bb72f343b636dc02fd8ebe58d6f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df97f77266fc37d7bb6f7ad0630f50d23bb24cc976beea7b317f5432004a040c(
    *,
    elb_bucket: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesElbBucket, typing.Dict[builtins.str, typing.Any]]] = None,
    elb_bucket_policy: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesElbBucketPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    impact_classify_ec2_instance: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesImpactClassifyEc2Instance, typing.Dict[builtins.str, typing.Any]]] = None,
    listener1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListener1, typing.Dict[builtins.str, typing.Any]]] = None,
    listener2: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListener2, typing.Dict[builtins.str, typing.Any]]] = None,
    listener3: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListener3, typing.Dict[builtins.str, typing.Any]]] = None,
    listener_rule1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListenerRule1, typing.Dict[builtins.str, typing.Any]]] = None,
    listener_rule2: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListenerRule2, typing.Dict[builtins.str, typing.Any]]] = None,
    listener_rule3: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesListenerRule3, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancer1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesLoadBalancer1, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group1: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesTargetGroup1, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group2: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesTargetGroup2, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group3: typing.Optional[typing.Union[CfnLoadBalancerModulePropsResourcesTargetGroup3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea845836670adc29dac9fba362b80806ced97821aa63f42910ad89d3d709600a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63780ea666c217d91338139a84ef8c5772594a5b9d1cb4919175051ee3f6409(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b5aeb2156a04e482e57b7962280a7295c63c452d304260f2fdaf0282b74187(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4be15938ed3d6525e44d07f3fb9eb6bfbadd9559061d4619b604bf20aa4e04(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dd8eeb0af0789eeb249672734adcaab1144809c4217591b5caca543f952f80(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd194803f40cf9085ae6d831a426c0f98e5f9b68bf976ee3b5ec7f8c12ca3ee(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1426cac9480cf1eff50dec0e2f63752a3edfd218989a21963b3f647a139dae3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31f3a30dc68553788e1bc91b8e29da3ca1e7989cf9f1a902261b983d39f5c223(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__376981dff1abc9478b16a955870d06afbc02c3c28094ae2bbdba15ffbf35692f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__139142fe0ffa09dfdabf0bd060da4bb39d4d9299da13a7721fd670b8d7f63f59(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f00aa2769a669dd1b6b29620032ed673cc9a79519e2ab75f2c315d8d952af82(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3352e45715b0171ac565d78c52e565ef439332bccbe9e9e3fed7cc880543a920(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dc8be5181e72b2692e64cdd50d32c0db5a8b8e27d49f2930d053ff8337485f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
