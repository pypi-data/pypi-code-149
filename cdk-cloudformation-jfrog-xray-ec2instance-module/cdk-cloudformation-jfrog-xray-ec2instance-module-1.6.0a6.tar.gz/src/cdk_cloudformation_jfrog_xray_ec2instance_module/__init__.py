'''
# jfrog-xray-ec2instance-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Xray::EC2Instance::MODULE` v1.6.0.

## Description

Schema for Module Fragment of type JFrog::Xray::EC2Instance::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Xray::EC2Instance::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Xray-EC2Instance-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Xray::EC2Instance::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-xray-ec2instance-module+v1.6.0).
* Issues related to `JFrog::Xray::EC2Instance::MODULE` should be reported to the [publisher](undefined).

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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModule",
):
    '''A CloudFormation ``JFrog::Xray::EC2Instance::MODULE``.

    :cloudformationResource: JFrog::Xray::EC2Instance::MODULE
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
        '''Create a new ``JFrog::Xray::EC2Instance::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a05ef70d4ee1972d08a528a9b2f4a12918341c6376ade8907597f609da1a72e3)
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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Xray::EC2Instance::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnEc2InstanceModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnEc2InstanceModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnEc2InstanceModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df9ab534ea4a18e48256b3304ef67118e1889f07213e313caf1b857f82f45fb2)
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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_product": "artifactoryProduct",
        "database_driver": "databaseDriver",
        "database_password": "databasePassword",
        "database_type": "databaseType",
        "database_user": "databaseUser",
        "deployment_tag": "deploymentTag",
        "extra_java_options": "extraJavaOptions",
        "jfrog_internal_url": "jfrogInternalUrl",
        "key_pair_name": "keyPairName",
        "logical_id": "logicalId",
        "master_key": "masterKey",
        "max_scaling_nodes": "maxScalingNodes",
        "min_scaling_nodes": "minScalingNodes",
        "private_subnet1_id": "privateSubnet1Id",
        "private_subnet2_id": "privateSubnet2Id",
        "qs_s3_bucket_name": "qsS3BucketName",
        "qs_s3_key_prefix": "qsS3KeyPrefix",
        "qs_s3_uri": "qsS3Uri",
        "security_groups": "securityGroups",
        "user_data_directory": "userDataDirectory",
        "volume_size": "volumeSize",
        "xray_database_password": "xrayDatabasePassword",
        "xray_database_url": "xrayDatabaseUrl",
        "xray_database_user": "xrayDatabaseUser",
        "xray_host_profile": "xrayHostProfile",
        "xray_host_role": "xrayHostRole",
        "xray_instance_type": "xrayInstanceType",
        "xray_master_database_url": "xrayMasterDatabaseUrl",
        "xray_version": "xrayVersion",
    },
)
class CfnEc2InstanceModulePropsParameters:
    def __init__(
        self,
        *,
        artifactory_product: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryProduct", typing.Dict[builtins.str, typing.Any]]] = None,
        database_driver: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabaseDriver", typing.Dict[builtins.str, typing.Any]]] = None,
        database_password: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabasePassword", typing.Dict[builtins.str, typing.Any]]] = None,
        database_type: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabaseType", typing.Dict[builtins.str, typing.Any]]] = None,
        database_user: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabaseUser", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_tag: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDeploymentTag", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_java_options: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersExtraJavaOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        jfrog_internal_url: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersJfrogInternalUrl", typing.Dict[builtins.str, typing.Any]]] = None,
        key_pair_name: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersKeyPairName", typing.Dict[builtins.str, typing.Any]]] = None,
        logical_id: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersLogicalId", typing.Dict[builtins.str, typing.Any]]] = None,
        master_key: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersMasterKey", typing.Dict[builtins.str, typing.Any]]] = None,
        max_scaling_nodes: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersMaxScalingNodes", typing.Dict[builtins.str, typing.Any]]] = None,
        min_scaling_nodes: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersMinScalingNodes", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_id: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersPrivateSubnet1Id", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_id: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersPrivateSubnet2Id", typing.Dict[builtins.str, typing.Any]]] = None,
        qs_s3_bucket_name: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersQsS3BucketName", typing.Dict[builtins.str, typing.Any]]] = None,
        qs_s3_key_prefix: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersQsS3KeyPrefix", typing.Dict[builtins.str, typing.Any]]] = None,
        qs_s3_uri: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersQsS3Uri", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersSecurityGroups", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data_directory: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersUserDataDirectory", typing.Dict[builtins.str, typing.Any]]] = None,
        volume_size: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersVolumeSize", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_database_password: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayDatabasePassword", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_database_url: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayDatabaseUrl", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_database_user: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayDatabaseUser", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_host_profile: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayHostProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_host_role: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayHostRole", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_instance_type: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_master_database_url: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_version: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersXrayVersion", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param artifactory_product: JFrog Artifactory product you want to install into an AMI.
        :param database_driver: 
        :param database_password: 
        :param database_type: 
        :param database_user: 
        :param deployment_tag: 
        :param extra_java_options: 
        :param jfrog_internal_url: 
        :param key_pair_name: 
        :param logical_id: Logical Id of the MODULE.
        :param master_key: 
        :param max_scaling_nodes: 
        :param min_scaling_nodes: 
        :param private_subnet1_id: ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param private_subnet2_id: ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).
        :param qs_s3_bucket_name: 
        :param qs_s3_key_prefix: 
        :param qs_s3_uri: 
        :param security_groups: 
        :param user_data_directory: Directory to store Artifactory data. Can be used to store data (via symlink) in detachable volume
        :param volume_size: 
        :param xray_database_password: 
        :param xray_database_url: 
        :param xray_database_user: 
        :param xray_host_profile: 
        :param xray_host_role: 
        :param xray_instance_type: 
        :param xray_master_database_url: 
        :param xray_version: 

        :schema: CfnEc2InstanceModulePropsParameters
        '''
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnEc2InstanceModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(database_driver, dict):
            database_driver = CfnEc2InstanceModulePropsParametersDatabaseDriver(**database_driver)
        if isinstance(database_password, dict):
            database_password = CfnEc2InstanceModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_type, dict):
            database_type = CfnEc2InstanceModulePropsParametersDatabaseType(**database_type)
        if isinstance(database_user, dict):
            database_user = CfnEc2InstanceModulePropsParametersDatabaseUser(**database_user)
        if isinstance(deployment_tag, dict):
            deployment_tag = CfnEc2InstanceModulePropsParametersDeploymentTag(**deployment_tag)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnEc2InstanceModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(jfrog_internal_url, dict):
            jfrog_internal_url = CfnEc2InstanceModulePropsParametersJfrogInternalUrl(**jfrog_internal_url)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnEc2InstanceModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnEc2InstanceModulePropsParametersLogicalId(**logical_id)
        if isinstance(master_key, dict):
            master_key = CfnEc2InstanceModulePropsParametersMasterKey(**master_key)
        if isinstance(max_scaling_nodes, dict):
            max_scaling_nodes = CfnEc2InstanceModulePropsParametersMaxScalingNodes(**max_scaling_nodes)
        if isinstance(min_scaling_nodes, dict):
            min_scaling_nodes = CfnEc2InstanceModulePropsParametersMinScalingNodes(**min_scaling_nodes)
        if isinstance(private_subnet1_id, dict):
            private_subnet1_id = CfnEc2InstanceModulePropsParametersPrivateSubnet1Id(**private_subnet1_id)
        if isinstance(private_subnet2_id, dict):
            private_subnet2_id = CfnEc2InstanceModulePropsParametersPrivateSubnet2Id(**private_subnet2_id)
        if isinstance(qs_s3_bucket_name, dict):
            qs_s3_bucket_name = CfnEc2InstanceModulePropsParametersQsS3BucketName(**qs_s3_bucket_name)
        if isinstance(qs_s3_key_prefix, dict):
            qs_s3_key_prefix = CfnEc2InstanceModulePropsParametersQsS3KeyPrefix(**qs_s3_key_prefix)
        if isinstance(qs_s3_uri, dict):
            qs_s3_uri = CfnEc2InstanceModulePropsParametersQsS3Uri(**qs_s3_uri)
        if isinstance(security_groups, dict):
            security_groups = CfnEc2InstanceModulePropsParametersSecurityGroups(**security_groups)
        if isinstance(user_data_directory, dict):
            user_data_directory = CfnEc2InstanceModulePropsParametersUserDataDirectory(**user_data_directory)
        if isinstance(volume_size, dict):
            volume_size = CfnEc2InstanceModulePropsParametersVolumeSize(**volume_size)
        if isinstance(xray_database_password, dict):
            xray_database_password = CfnEc2InstanceModulePropsParametersXrayDatabasePassword(**xray_database_password)
        if isinstance(xray_database_url, dict):
            xray_database_url = CfnEc2InstanceModulePropsParametersXrayDatabaseUrl(**xray_database_url)
        if isinstance(xray_database_user, dict):
            xray_database_user = CfnEc2InstanceModulePropsParametersXrayDatabaseUser(**xray_database_user)
        if isinstance(xray_host_profile, dict):
            xray_host_profile = CfnEc2InstanceModulePropsParametersXrayHostProfile(**xray_host_profile)
        if isinstance(xray_host_role, dict):
            xray_host_role = CfnEc2InstanceModulePropsParametersXrayHostRole(**xray_host_role)
        if isinstance(xray_instance_type, dict):
            xray_instance_type = CfnEc2InstanceModulePropsParametersXrayInstanceType(**xray_instance_type)
        if isinstance(xray_master_database_url, dict):
            xray_master_database_url = CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl(**xray_master_database_url)
        if isinstance(xray_version, dict):
            xray_version = CfnEc2InstanceModulePropsParametersXrayVersion(**xray_version)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc54c6ce038153b831dbacac25d4e8ecc779b126f6d42546c1e10256c03896a1)
            check_type(argname="argument artifactory_product", value=artifactory_product, expected_type=type_hints["artifactory_product"])
            check_type(argname="argument database_driver", value=database_driver, expected_type=type_hints["database_driver"])
            check_type(argname="argument database_password", value=database_password, expected_type=type_hints["database_password"])
            check_type(argname="argument database_type", value=database_type, expected_type=type_hints["database_type"])
            check_type(argname="argument database_user", value=database_user, expected_type=type_hints["database_user"])
            check_type(argname="argument deployment_tag", value=deployment_tag, expected_type=type_hints["deployment_tag"])
            check_type(argname="argument extra_java_options", value=extra_java_options, expected_type=type_hints["extra_java_options"])
            check_type(argname="argument jfrog_internal_url", value=jfrog_internal_url, expected_type=type_hints["jfrog_internal_url"])
            check_type(argname="argument key_pair_name", value=key_pair_name, expected_type=type_hints["key_pair_name"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument master_key", value=master_key, expected_type=type_hints["master_key"])
            check_type(argname="argument max_scaling_nodes", value=max_scaling_nodes, expected_type=type_hints["max_scaling_nodes"])
            check_type(argname="argument min_scaling_nodes", value=min_scaling_nodes, expected_type=type_hints["min_scaling_nodes"])
            check_type(argname="argument private_subnet1_id", value=private_subnet1_id, expected_type=type_hints["private_subnet1_id"])
            check_type(argname="argument private_subnet2_id", value=private_subnet2_id, expected_type=type_hints["private_subnet2_id"])
            check_type(argname="argument qs_s3_bucket_name", value=qs_s3_bucket_name, expected_type=type_hints["qs_s3_bucket_name"])
            check_type(argname="argument qs_s3_key_prefix", value=qs_s3_key_prefix, expected_type=type_hints["qs_s3_key_prefix"])
            check_type(argname="argument qs_s3_uri", value=qs_s3_uri, expected_type=type_hints["qs_s3_uri"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument user_data_directory", value=user_data_directory, expected_type=type_hints["user_data_directory"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument xray_database_password", value=xray_database_password, expected_type=type_hints["xray_database_password"])
            check_type(argname="argument xray_database_url", value=xray_database_url, expected_type=type_hints["xray_database_url"])
            check_type(argname="argument xray_database_user", value=xray_database_user, expected_type=type_hints["xray_database_user"])
            check_type(argname="argument xray_host_profile", value=xray_host_profile, expected_type=type_hints["xray_host_profile"])
            check_type(argname="argument xray_host_role", value=xray_host_role, expected_type=type_hints["xray_host_role"])
            check_type(argname="argument xray_instance_type", value=xray_instance_type, expected_type=type_hints["xray_instance_type"])
            check_type(argname="argument xray_master_database_url", value=xray_master_database_url, expected_type=type_hints["xray_master_database_url"])
            check_type(argname="argument xray_version", value=xray_version, expected_type=type_hints["xray_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if artifactory_product is not None:
            self._values["artifactory_product"] = artifactory_product
        if database_driver is not None:
            self._values["database_driver"] = database_driver
        if database_password is not None:
            self._values["database_password"] = database_password
        if database_type is not None:
            self._values["database_type"] = database_type
        if database_user is not None:
            self._values["database_user"] = database_user
        if deployment_tag is not None:
            self._values["deployment_tag"] = deployment_tag
        if extra_java_options is not None:
            self._values["extra_java_options"] = extra_java_options
        if jfrog_internal_url is not None:
            self._values["jfrog_internal_url"] = jfrog_internal_url
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if logical_id is not None:
            self._values["logical_id"] = logical_id
        if master_key is not None:
            self._values["master_key"] = master_key
        if max_scaling_nodes is not None:
            self._values["max_scaling_nodes"] = max_scaling_nodes
        if min_scaling_nodes is not None:
            self._values["min_scaling_nodes"] = min_scaling_nodes
        if private_subnet1_id is not None:
            self._values["private_subnet1_id"] = private_subnet1_id
        if private_subnet2_id is not None:
            self._values["private_subnet2_id"] = private_subnet2_id
        if qs_s3_bucket_name is not None:
            self._values["qs_s3_bucket_name"] = qs_s3_bucket_name
        if qs_s3_key_prefix is not None:
            self._values["qs_s3_key_prefix"] = qs_s3_key_prefix
        if qs_s3_uri is not None:
            self._values["qs_s3_uri"] = qs_s3_uri
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if user_data_directory is not None:
            self._values["user_data_directory"] = user_data_directory
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if xray_database_password is not None:
            self._values["xray_database_password"] = xray_database_password
        if xray_database_url is not None:
            self._values["xray_database_url"] = xray_database_url
        if xray_database_user is not None:
            self._values["xray_database_user"] = xray_database_user
        if xray_host_profile is not None:
            self._values["xray_host_profile"] = xray_host_profile
        if xray_host_role is not None:
            self._values["xray_host_role"] = xray_host_role
        if xray_instance_type is not None:
            self._values["xray_instance_type"] = xray_instance_type
        if xray_master_database_url is not None:
            self._values["xray_master_database_url"] = xray_master_database_url
        if xray_version is not None:
            self._values["xray_version"] = xray_version

    @builtins.property
    def artifactory_product(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryProduct"]:
        '''JFrog Artifactory product you want to install into an AMI.

        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryProduct
        '''
        result = self._values.get("artifactory_product")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryProduct"], result)

    @builtins.property
    def database_driver(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseDriver"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseDriver
        '''
        result = self._values.get("database_driver")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseDriver"], result)

    @builtins.property
    def database_password(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePassword"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabasePassword
        '''
        result = self._values.get("database_password")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePassword"], result)

    @builtins.property
    def database_type(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseType"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseType
        '''
        result = self._values.get("database_type")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseType"], result)

    @builtins.property
    def database_user(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUser"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def deployment_tag(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDeploymentTag"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DeploymentTag
        '''
        result = self._values.get("deployment_tag")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDeploymentTag"], result)

    @builtins.property
    def extra_java_options(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersExtraJavaOptions"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ExtraJavaOptions
        '''
        result = self._values.get("extra_java_options")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersExtraJavaOptions"], result)

    @builtins.property
    def jfrog_internal_url(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersJfrogInternalUrl"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#JfrogInternalUrl
        '''
        result = self._values.get("jfrog_internal_url")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersJfrogInternalUrl"], result)

    @builtins.property
    def key_pair_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersKeyPairName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#KeyPairName
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersKeyPairName"], result)

    @builtins.property
    def logical_id(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersLogicalId"]:
        '''Logical Id of the MODULE.

        :schema: CfnEc2InstanceModulePropsParameters#LogicalId
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersLogicalId"], result)

    @builtins.property
    def master_key(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersMasterKey"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#MasterKey
        '''
        result = self._values.get("master_key")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersMasterKey"], result)

    @builtins.property
    def max_scaling_nodes(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersMaxScalingNodes"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#MaxScalingNodes
        '''
        result = self._values.get("max_scaling_nodes")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersMaxScalingNodes"], result)

    @builtins.property
    def min_scaling_nodes(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersMinScalingNodes"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#MinScalingNodes
        '''
        result = self._values.get("min_scaling_nodes")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersMinScalingNodes"], result)

    @builtins.property
    def private_subnet1_id(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet1Id"]:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnEc2InstanceModulePropsParameters#PrivateSubnet1Id
        '''
        result = self._values.get("private_subnet1_id")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet1Id"], result)

    @builtins.property
    def private_subnet2_id(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet2Id"]:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnEc2InstanceModulePropsParameters#PrivateSubnet2Id
        '''
        result = self._values.get("private_subnet2_id")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet2Id"], result)

    @builtins.property
    def qs_s3_bucket_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersQsS3BucketName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#QsS3BucketName
        '''
        result = self._values.get("qs_s3_bucket_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersQsS3BucketName"], result)

    @builtins.property
    def qs_s3_key_prefix(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersQsS3KeyPrefix"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#QsS3KeyPrefix
        '''
        result = self._values.get("qs_s3_key_prefix")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersQsS3KeyPrefix"], result)

    @builtins.property
    def qs_s3_uri(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersQsS3Uri"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#QsS3Uri
        '''
        result = self._values.get("qs_s3_uri")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersQsS3Uri"], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersSecurityGroups"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#SecurityGroups
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersSecurityGroups"], result)

    @builtins.property
    def user_data_directory(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersUserDataDirectory"]:
        '''Directory to store Artifactory data.

        Can be used to store data (via symlink) in detachable volume

        :schema: CfnEc2InstanceModulePropsParameters#UserDataDirectory
        '''
        result = self._values.get("user_data_directory")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersUserDataDirectory"], result)

    @builtins.property
    def volume_size(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersVolumeSize"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#VolumeSize
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersVolumeSize"], result)

    @builtins.property
    def xray_database_password(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayDatabasePassword"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayDatabasePassword
        '''
        result = self._values.get("xray_database_password")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayDatabasePassword"], result)

    @builtins.property
    def xray_database_url(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayDatabaseUrl"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayDatabaseUrl
        '''
        result = self._values.get("xray_database_url")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayDatabaseUrl"], result)

    @builtins.property
    def xray_database_user(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayDatabaseUser"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayDatabaseUser
        '''
        result = self._values.get("xray_database_user")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayDatabaseUser"], result)

    @builtins.property
    def xray_host_profile(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayHostProfile"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayHostProfile
        '''
        result = self._values.get("xray_host_profile")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayHostProfile"], result)

    @builtins.property
    def xray_host_role(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayHostRole"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayHostRole
        '''
        result = self._values.get("xray_host_role")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayHostRole"], result)

    @builtins.property
    def xray_instance_type(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayInstanceType"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayInstanceType
        '''
        result = self._values.get("xray_instance_type")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayInstanceType"], result)

    @builtins.property
    def xray_master_database_url(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayMasterDatabaseUrl
        '''
        result = self._values.get("xray_master_database_url")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl"], result)

    @builtins.property
    def xray_version(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersXrayVersion"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#XrayVersion
        '''
        result = self._values.get("xray_version")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersXrayVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryProduct",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryProduct:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JFrog Artifactory product you want to install into an AMI.

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryProduct
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534b6f5151ba2f9a938bfca95b178ea281b07bcb94f4129fb41efa21e1646fcc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryProduct#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryProduct#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryProduct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseDriver",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseDriver:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseDriver
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9515f8008db12ab85d038514be09d8c3471a55fa0c8dac547ac6f2b8e9baa35e)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseDriver#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseDriver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabasePassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabasePassword
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c71e95cbe5fa0f40f9cfca0d8f13f4d1a61f99af61b1e36042fd02cd466ab0b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32cf6f06c2e8ec997661c4afd4230d018d6308b69df239548dba768adee58e5d)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseUser:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseUser
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f20d941922db591f160ef5a22731206e4bf28ba2a825ad64efaa293e82f2ff40)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersDeploymentTag",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDeploymentTag:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDeploymentTag
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89220959b3cec4ffc43988814588daebb464a2489a42cd55e49d8317d44eb6c9)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDeploymentTag#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDeploymentTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersExtraJavaOptions",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersExtraJavaOptions:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersExtraJavaOptions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59d2f6cdd9a909a3362356f38e019aa24175ce3b8b76e4be0faf691f47aa110)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersExtraJavaOptions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersExtraJavaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersJfrogInternalUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersJfrogInternalUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersJfrogInternalUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56841e51c1319e6277eaeb0b387a48941f44c5628ddebb86cf526346635c968)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersJfrogInternalUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersJfrogInternalUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersKeyPairName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersKeyPairName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6343987a26c21b1d39336bc14efdbeb993017d20d0e26f6f630d0fd89dbdb1)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersKeyPairName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersKeyPairName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersLogicalId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersLogicalId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logical Id of the MODULE.

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersLogicalId
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f25c9d63f123c75a6e0e43ca54a8a59a45699ee71269be747417fcc78c309ba4)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersLogicalId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersLogicalId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersLogicalId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersMasterKey",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersMasterKey:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersMasterKey
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__007da8b060232e4bbd80c6951fa7c609c352a35d425a53e9c143129ef531ac14)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersMasterKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersMasterKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersMaxScalingNodes",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersMaxScalingNodes:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersMaxScalingNodes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed3e8e47bba0ad9b3d70f5cedcd1424e61e970f86c4d6d1d2dfef18b3b0fceea)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersMaxScalingNodes#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersMaxScalingNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersMinScalingNodes",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersMinScalingNodes:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersMinScalingNodes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bec9cb2cecdc44f4f6aacc863ed6c32ef9ee86537c11ea95dc38aa7013767dc9)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersMinScalingNodes#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersMinScalingNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersPrivateSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersPrivateSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet1Id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f24b1433f77380dc22dcba4f457d442dd2c9503e229d90fac3afb0ebcb2bb4)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersPrivateSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersPrivateSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersPrivateSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet2Id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec56006cad0db4f99fc5228844b4a341546ea8c45e72d71ed31944832abad92d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersPrivateSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersQsS3BucketName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersQsS3BucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__744b3729184b8a3d8e786c8be9cce04c63edf54f58193faa2a0c4e36abda5456)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersQsS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersQsS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersQsS3KeyPrefix:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersQsS3KeyPrefix
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e509a2ac8cfef095f32f8bf6b483cae156f4d4adb833823d6b52c1cfd45507)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersQsS3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersQsS3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3Uri",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersQsS3Uri:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersQsS3Uri
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37fc531f78252c4e0d5f4effb8cdff5ecfe41ce824a7e502232fd893a322289)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersQsS3Uri#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersQsS3Uri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersSecurityGroups",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersSecurityGroups:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersSecurityGroups
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a015e3babfa11bedffe2af75ad9f4b4341f4517b2879e0d0b484b8c0e1e74b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSecurityGroups#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersSecurityGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersUserDataDirectory",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersUserDataDirectory:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Directory to store Artifactory data.

        Can be used to store data (via symlink) in detachable volume

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersUserDataDirectory
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4523275189b276772b2d7741087ca3db9d6e2fba042a88bade5c6c490fe22bc7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersUserDataDirectory#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersUserDataDirectory#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersUserDataDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersVolumeSize:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersVolumeSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b94d0a555102474569730c5ec990f8e584c398b1bace61083df76c9bba51e69)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayDatabasePassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayDatabasePassword
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da74c95484ced72224548426669e2873eac67561ae65e25b451c0a0770a6c01e)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayDatabaseUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayDatabaseUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayDatabaseUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b839a0db7ef1c802876f7c1ab06749fcbdc68e0c3fc281f02a1afb71479848b7)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayDatabaseUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayDatabaseUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayDatabaseUser:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayDatabaseUser
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b2ffb33c44eee839ab1eab13a653fe29c077bd256716e9bb2bc3d0158ec59a8)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayHostProfile",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayHostProfile:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayHostProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fd90651eaa6be9046817e7dd2a4982bbc6f2a7a3ebce9999a6204013a46cd1a)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayHostProfile#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayHostRole",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayHostRole:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayHostRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bda0faf3ce411a7ae8543c23cdbeaf2973e5ddf0f12e7896a7f162d8bfafc107)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayHostRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b8b928b3bb776e67967da2b0329d5e29c2aab9c34eab188a773188ee51b528d)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d76e4a2e802e6e91b69605c41b0488cf6931183542b7dbcaeeb370eb7436b799)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsParametersXrayVersion",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersXrayVersion:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersXrayVersion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6da149f71fafc5a47a5ecaee76654de0896eb960f72a51a7ed4b6cfa6b4e16)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersXrayVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersXrayVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "xray_launch_configuration": "xrayLaunchConfiguration",
        "xray_scaling_group": "xrayScalingGroup",
    },
)
class CfnEc2InstanceModulePropsResources:
    def __init__(
        self,
        *,
        xray_launch_configuration: typing.Optional[typing.Union["CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_scaling_group: typing.Optional[typing.Union["CfnEc2InstanceModulePropsResourcesXrayScalingGroup", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param xray_launch_configuration: 
        :param xray_scaling_group: 

        :schema: CfnEc2InstanceModulePropsResources
        '''
        if isinstance(xray_launch_configuration, dict):
            xray_launch_configuration = CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration(**xray_launch_configuration)
        if isinstance(xray_scaling_group, dict):
            xray_scaling_group = CfnEc2InstanceModulePropsResourcesXrayScalingGroup(**xray_scaling_group)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad91a108fd9d067dea3b931f190ac125bbe428f6f33f4d906022fa3e571f590)
            check_type(argname="argument xray_launch_configuration", value=xray_launch_configuration, expected_type=type_hints["xray_launch_configuration"])
            check_type(argname="argument xray_scaling_group", value=xray_scaling_group, expected_type=type_hints["xray_scaling_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if xray_launch_configuration is not None:
            self._values["xray_launch_configuration"] = xray_launch_configuration
        if xray_scaling_group is not None:
            self._values["xray_scaling_group"] = xray_scaling_group

    @builtins.property
    def xray_launch_configuration(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration"]:
        '''
        :schema: CfnEc2InstanceModulePropsResources#XrayLaunchConfiguration
        '''
        result = self._values.get("xray_launch_configuration")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration"], result)

    @builtins.property
    def xray_scaling_group(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsResourcesXrayScalingGroup"]:
        '''
        :schema: CfnEc2InstanceModulePropsResources#XrayScalingGroup
        '''
        result = self._values.get("xray_scaling_group")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResourcesXrayScalingGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d65c3dfd576a202197fa9f4f28a631dd0bf403ffdc8ad2339d5b2dea5ffae64)
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
        :schema: CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnEc2InstanceModulePropsResourcesXrayScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEc2InstanceModulePropsResourcesXrayScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsResourcesXrayScalingGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c958a7004ca34e5d3425a9b577840e21264adf8637840b64cb17e2db25a52e9)
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
        :schema: CfnEc2InstanceModulePropsResourcesXrayScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesXrayScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResourcesXrayScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEc2InstanceModule",
    "CfnEc2InstanceModuleProps",
    "CfnEc2InstanceModulePropsParameters",
    "CfnEc2InstanceModulePropsParametersArtifactoryProduct",
    "CfnEc2InstanceModulePropsParametersDatabaseDriver",
    "CfnEc2InstanceModulePropsParametersDatabasePassword",
    "CfnEc2InstanceModulePropsParametersDatabaseType",
    "CfnEc2InstanceModulePropsParametersDatabaseUser",
    "CfnEc2InstanceModulePropsParametersDeploymentTag",
    "CfnEc2InstanceModulePropsParametersExtraJavaOptions",
    "CfnEc2InstanceModulePropsParametersJfrogInternalUrl",
    "CfnEc2InstanceModulePropsParametersKeyPairName",
    "CfnEc2InstanceModulePropsParametersLogicalId",
    "CfnEc2InstanceModulePropsParametersMasterKey",
    "CfnEc2InstanceModulePropsParametersMaxScalingNodes",
    "CfnEc2InstanceModulePropsParametersMinScalingNodes",
    "CfnEc2InstanceModulePropsParametersPrivateSubnet1Id",
    "CfnEc2InstanceModulePropsParametersPrivateSubnet2Id",
    "CfnEc2InstanceModulePropsParametersQsS3BucketName",
    "CfnEc2InstanceModulePropsParametersQsS3KeyPrefix",
    "CfnEc2InstanceModulePropsParametersQsS3Uri",
    "CfnEc2InstanceModulePropsParametersSecurityGroups",
    "CfnEc2InstanceModulePropsParametersUserDataDirectory",
    "CfnEc2InstanceModulePropsParametersVolumeSize",
    "CfnEc2InstanceModulePropsParametersXrayDatabasePassword",
    "CfnEc2InstanceModulePropsParametersXrayDatabaseUrl",
    "CfnEc2InstanceModulePropsParametersXrayDatabaseUser",
    "CfnEc2InstanceModulePropsParametersXrayHostProfile",
    "CfnEc2InstanceModulePropsParametersXrayHostRole",
    "CfnEc2InstanceModulePropsParametersXrayInstanceType",
    "CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl",
    "CfnEc2InstanceModulePropsParametersXrayVersion",
    "CfnEc2InstanceModulePropsResources",
    "CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration",
    "CfnEc2InstanceModulePropsResourcesXrayScalingGroup",
]

publication.publish()

def _typecheckingstub__a05ef70d4ee1972d08a528a9b2f4a12918341c6376ade8907597f609da1a72e3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df9ab534ea4a18e48256b3304ef67118e1889f07213e313caf1b857f82f45fb2(
    *,
    parameters: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc54c6ce038153b831dbacac25d4e8ecc779b126f6d42546c1e10256c03896a1(
    *,
    artifactory_product: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryProduct, typing.Dict[builtins.str, typing.Any]]] = None,
    database_driver: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabaseDriver, typing.Dict[builtins.str, typing.Any]]] = None,
    database_password: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabasePassword, typing.Dict[builtins.str, typing.Any]]] = None,
    database_type: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabaseType, typing.Dict[builtins.str, typing.Any]]] = None,
    database_user: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabaseUser, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_tag: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDeploymentTag, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_java_options: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersExtraJavaOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    jfrog_internal_url: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersJfrogInternalUrl, typing.Dict[builtins.str, typing.Any]]] = None,
    key_pair_name: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersKeyPairName, typing.Dict[builtins.str, typing.Any]]] = None,
    logical_id: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersLogicalId, typing.Dict[builtins.str, typing.Any]]] = None,
    master_key: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersMasterKey, typing.Dict[builtins.str, typing.Any]]] = None,
    max_scaling_nodes: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersMaxScalingNodes, typing.Dict[builtins.str, typing.Any]]] = None,
    min_scaling_nodes: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersMinScalingNodes, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_id: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersPrivateSubnet1Id, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_id: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersPrivateSubnet2Id, typing.Dict[builtins.str, typing.Any]]] = None,
    qs_s3_bucket_name: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersQsS3BucketName, typing.Dict[builtins.str, typing.Any]]] = None,
    qs_s3_key_prefix: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersQsS3KeyPrefix, typing.Dict[builtins.str, typing.Any]]] = None,
    qs_s3_uri: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersQsS3Uri, typing.Dict[builtins.str, typing.Any]]] = None,
    security_groups: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersSecurityGroups, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data_directory: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersUserDataDirectory, typing.Dict[builtins.str, typing.Any]]] = None,
    volume_size: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersVolumeSize, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_database_password: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayDatabasePassword, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_database_url: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayDatabaseUrl, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_database_user: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayDatabaseUser, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_host_profile: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayHostProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_host_role: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayHostRole, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_instance_type: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_master_database_url: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayMasterDatabaseUrl, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_version: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersXrayVersion, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534b6f5151ba2f9a938bfca95b178ea281b07bcb94f4129fb41efa21e1646fcc(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9515f8008db12ab85d038514be09d8c3471a55fa0c8dac547ac6f2b8e9baa35e(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c71e95cbe5fa0f40f9cfca0d8f13f4d1a61f99af61b1e36042fd02cd466ab0b(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32cf6f06c2e8ec997661c4afd4230d018d6308b69df239548dba768adee58e5d(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20d941922db591f160ef5a22731206e4bf28ba2a825ad64efaa293e82f2ff40(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89220959b3cec4ffc43988814588daebb464a2489a42cd55e49d8317d44eb6c9(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59d2f6cdd9a909a3362356f38e019aa24175ce3b8b76e4be0faf691f47aa110(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56841e51c1319e6277eaeb0b387a48941f44c5628ddebb86cf526346635c968(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6343987a26c21b1d39336bc14efdbeb993017d20d0e26f6f630d0fd89dbdb1(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f25c9d63f123c75a6e0e43ca54a8a59a45699ee71269be747417fcc78c309ba4(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__007da8b060232e4bbd80c6951fa7c609c352a35d425a53e9c143129ef531ac14(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed3e8e47bba0ad9b3d70f5cedcd1424e61e970f86c4d6d1d2dfef18b3b0fceea(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bec9cb2cecdc44f4f6aacc863ed6c32ef9ee86537c11ea95dc38aa7013767dc9(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11f24b1433f77380dc22dcba4f457d442dd2c9503e229d90fac3afb0ebcb2bb4(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec56006cad0db4f99fc5228844b4a341546ea8c45e72d71ed31944832abad92d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__744b3729184b8a3d8e786c8be9cce04c63edf54f58193faa2a0c4e36abda5456(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e509a2ac8cfef095f32f8bf6b483cae156f4d4adb833823d6b52c1cfd45507(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37fc531f78252c4e0d5f4effb8cdff5ecfe41ce824a7e502232fd893a322289(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a015e3babfa11bedffe2af75ad9f4b4341f4517b2879e0d0b484b8c0e1e74b(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4523275189b276772b2d7741087ca3db9d6e2fba042a88bade5c6c490fe22bc7(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b94d0a555102474569730c5ec990f8e584c398b1bace61083df76c9bba51e69(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da74c95484ced72224548426669e2873eac67561ae65e25b451c0a0770a6c01e(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b839a0db7ef1c802876f7c1ab06749fcbdc68e0c3fc281f02a1afb71479848b7(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2ffb33c44eee839ab1eab13a653fe29c077bd256716e9bb2bc3d0158ec59a8(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd90651eaa6be9046817e7dd2a4982bbc6f2a7a3ebce9999a6204013a46cd1a(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda0faf3ce411a7ae8543c23cdbeaf2973e5ddf0f12e7896a7f162d8bfafc107(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b8b928b3bb776e67967da2b0329d5e29c2aab9c34eab188a773188ee51b528d(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76e4a2e802e6e91b69605c41b0488cf6931183542b7dbcaeeb370eb7436b799(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6da149f71fafc5a47a5ecaee76654de0896eb960f72a51a7ed4b6cfa6b4e16(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad91a108fd9d067dea3b931f190ac125bbe428f6f33f4d906022fa3e571f590(
    *,
    xray_launch_configuration: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResourcesXrayLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_scaling_group: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResourcesXrayScalingGroup, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d65c3dfd576a202197fa9f4f28a631dd0bf403ffdc8ad2339d5b2dea5ffae64(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c958a7004ca34e5d3425a9b577840e21264adf8637840b64cb17e2db25a52e9(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
