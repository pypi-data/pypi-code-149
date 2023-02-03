'''
# jfrog-artifactory-ec2instance-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Artifactory::EC2Instance::MODULE` v1.7.0.

## Description

Schema for Module Fragment of type JFrog::Artifactory::EC2Instance::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Artifactory::EC2Instance::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Artifactory-EC2Instance-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Artifactory::EC2Instance::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-artifactory-ec2instance-module+v1.7.0).
* Issues related to `JFrog::Artifactory::EC2Instance::MODULE` should be reported to the [publisher](undefined).

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModule",
):
    '''A CloudFormation ``JFrog::Artifactory::EC2Instance::MODULE``.

    :cloudformationResource: JFrog::Artifactory::EC2Instance::MODULE
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
        '''Create a new ``JFrog::Artifactory::EC2Instance::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88fca067515fe4abbe12dba935e582f23fffff965e4f0b1ccffe4e9be342dac2)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Artifactory::EC2Instance::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnEc2InstanceModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnEc2InstanceModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnEc2InstanceModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9da1ac93a152420f41e6cd031f8ed85b5768e4bc598109668fdc93b95cf76c12)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_efs_file_system": "artifactoryEfsFileSystem",
        "artifactory_licenses_secret_name": "artifactoryLicensesSecretName",
        "artifactory_primary": "artifactoryPrimary",
        "artifactory_product": "artifactoryProduct",
        "artifactory_s3_bucket": "artifactoryS3Bucket",
        "artifactory_server_name": "artifactoryServerName",
        "artifactory_version": "artifactoryVersion",
        "database_driver": "databaseDriver",
        "database_password": "databasePassword",
        "database_plugin": "databasePlugin",
        "database_plugin_url": "databasePluginUrl",
        "database_type": "databaseType",
        "database_url": "databaseUrl",
        "database_user": "databaseUser",
        "deployment_tag": "deploymentTag",
        "extra_java_options": "extraJavaOptions",
        "host_profile": "hostProfile",
        "host_role": "hostRole",
        "instance_type": "instanceType",
        "internal_target_group_arn": "internalTargetGroupArn",
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
        "sm_cert_name": "smCertName",
        "ssl_target_group_arn": "sslTargetGroupArn",
        "target_group_arn": "targetGroupArn",
        "user_data_directory": "userDataDirectory",
    },
)
class CfnEc2InstanceModulePropsParameters:
    def __init__(
        self,
        *,
        artifactory_efs_file_system: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_licenses_secret_name: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_primary: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryPrimary", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_product: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryProduct", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_s3_bucket: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_server_name: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryServerName", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_version: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersArtifactoryVersion", typing.Dict[builtins.str, typing.Any]]] = None,
        database_driver: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabaseDriver", typing.Dict[builtins.str, typing.Any]]] = None,
        database_password: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabasePassword", typing.Dict[builtins.str, typing.Any]]] = None,
        database_plugin: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabasePlugin", typing.Dict[builtins.str, typing.Any]]] = None,
        database_plugin_url: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabasePluginUrl", typing.Dict[builtins.str, typing.Any]]] = None,
        database_type: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabaseType", typing.Dict[builtins.str, typing.Any]]] = None,
        database_url: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabaseUrl", typing.Dict[builtins.str, typing.Any]]] = None,
        database_user: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDatabaseUser", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_tag: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersDeploymentTag", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_java_options: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersExtraJavaOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        host_profile: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersHostProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        host_role: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersHostRole", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_type: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        internal_target_group_arn: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersInternalTargetGroupArn", typing.Dict[builtins.str, typing.Any]]] = None,
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
        sm_cert_name: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersSmCertName", typing.Dict[builtins.str, typing.Any]]] = None,
        ssl_target_group_arn: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersSslTargetGroupArn", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group_arn: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersTargetGroupArn", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data_directory: typing.Optional[typing.Union["CfnEc2InstanceModulePropsParametersUserDataDirectory", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param artifactory_efs_file_system: 
        :param artifactory_licenses_secret_name: 
        :param artifactory_primary: 
        :param artifactory_product: JFrog Artifactory product you want to install into an AMI.
        :param artifactory_s3_bucket: 
        :param artifactory_server_name: 
        :param artifactory_version: 
        :param database_driver: 
        :param database_password: 
        :param database_plugin: 
        :param database_plugin_url: 
        :param database_type: 
        :param database_url: 
        :param database_user: 
        :param deployment_tag: 
        :param extra_java_options: 
        :param host_profile: 
        :param host_role: 
        :param instance_type: 
        :param internal_target_group_arn: 
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
        :param sm_cert_name: Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.
        :param ssl_target_group_arn: 
        :param target_group_arn: 
        :param user_data_directory: Directory to store Artifactory data. Can be used to store data (via symlink) in detachable volume

        :schema: CfnEc2InstanceModulePropsParameters
        '''
        if isinstance(artifactory_efs_file_system, dict):
            artifactory_efs_file_system = CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem(**artifactory_efs_file_system)
        if isinstance(artifactory_licenses_secret_name, dict):
            artifactory_licenses_secret_name = CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName(**artifactory_licenses_secret_name)
        if isinstance(artifactory_primary, dict):
            artifactory_primary = CfnEc2InstanceModulePropsParametersArtifactoryPrimary(**artifactory_primary)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnEc2InstanceModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(artifactory_s3_bucket, dict):
            artifactory_s3_bucket = CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket(**artifactory_s3_bucket)
        if isinstance(artifactory_server_name, dict):
            artifactory_server_name = CfnEc2InstanceModulePropsParametersArtifactoryServerName(**artifactory_server_name)
        if isinstance(artifactory_version, dict):
            artifactory_version = CfnEc2InstanceModulePropsParametersArtifactoryVersion(**artifactory_version)
        if isinstance(database_driver, dict):
            database_driver = CfnEc2InstanceModulePropsParametersDatabaseDriver(**database_driver)
        if isinstance(database_password, dict):
            database_password = CfnEc2InstanceModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_plugin, dict):
            database_plugin = CfnEc2InstanceModulePropsParametersDatabasePlugin(**database_plugin)
        if isinstance(database_plugin_url, dict):
            database_plugin_url = CfnEc2InstanceModulePropsParametersDatabasePluginUrl(**database_plugin_url)
        if isinstance(database_type, dict):
            database_type = CfnEc2InstanceModulePropsParametersDatabaseType(**database_type)
        if isinstance(database_url, dict):
            database_url = CfnEc2InstanceModulePropsParametersDatabaseUrl(**database_url)
        if isinstance(database_user, dict):
            database_user = CfnEc2InstanceModulePropsParametersDatabaseUser(**database_user)
        if isinstance(deployment_tag, dict):
            deployment_tag = CfnEc2InstanceModulePropsParametersDeploymentTag(**deployment_tag)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnEc2InstanceModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(host_profile, dict):
            host_profile = CfnEc2InstanceModulePropsParametersHostProfile(**host_profile)
        if isinstance(host_role, dict):
            host_role = CfnEc2InstanceModulePropsParametersHostRole(**host_role)
        if isinstance(instance_type, dict):
            instance_type = CfnEc2InstanceModulePropsParametersInstanceType(**instance_type)
        if isinstance(internal_target_group_arn, dict):
            internal_target_group_arn = CfnEc2InstanceModulePropsParametersInternalTargetGroupArn(**internal_target_group_arn)
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
        if isinstance(sm_cert_name, dict):
            sm_cert_name = CfnEc2InstanceModulePropsParametersSmCertName(**sm_cert_name)
        if isinstance(ssl_target_group_arn, dict):
            ssl_target_group_arn = CfnEc2InstanceModulePropsParametersSslTargetGroupArn(**ssl_target_group_arn)
        if isinstance(target_group_arn, dict):
            target_group_arn = CfnEc2InstanceModulePropsParametersTargetGroupArn(**target_group_arn)
        if isinstance(user_data_directory, dict):
            user_data_directory = CfnEc2InstanceModulePropsParametersUserDataDirectory(**user_data_directory)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__259db37424b1c9395758e09af0737955305cf5ab40a492f99b61b25d7b5dcc05)
            check_type(argname="argument artifactory_efs_file_system", value=artifactory_efs_file_system, expected_type=type_hints["artifactory_efs_file_system"])
            check_type(argname="argument artifactory_licenses_secret_name", value=artifactory_licenses_secret_name, expected_type=type_hints["artifactory_licenses_secret_name"])
            check_type(argname="argument artifactory_primary", value=artifactory_primary, expected_type=type_hints["artifactory_primary"])
            check_type(argname="argument artifactory_product", value=artifactory_product, expected_type=type_hints["artifactory_product"])
            check_type(argname="argument artifactory_s3_bucket", value=artifactory_s3_bucket, expected_type=type_hints["artifactory_s3_bucket"])
            check_type(argname="argument artifactory_server_name", value=artifactory_server_name, expected_type=type_hints["artifactory_server_name"])
            check_type(argname="argument artifactory_version", value=artifactory_version, expected_type=type_hints["artifactory_version"])
            check_type(argname="argument database_driver", value=database_driver, expected_type=type_hints["database_driver"])
            check_type(argname="argument database_password", value=database_password, expected_type=type_hints["database_password"])
            check_type(argname="argument database_plugin", value=database_plugin, expected_type=type_hints["database_plugin"])
            check_type(argname="argument database_plugin_url", value=database_plugin_url, expected_type=type_hints["database_plugin_url"])
            check_type(argname="argument database_type", value=database_type, expected_type=type_hints["database_type"])
            check_type(argname="argument database_url", value=database_url, expected_type=type_hints["database_url"])
            check_type(argname="argument database_user", value=database_user, expected_type=type_hints["database_user"])
            check_type(argname="argument deployment_tag", value=deployment_tag, expected_type=type_hints["deployment_tag"])
            check_type(argname="argument extra_java_options", value=extra_java_options, expected_type=type_hints["extra_java_options"])
            check_type(argname="argument host_profile", value=host_profile, expected_type=type_hints["host_profile"])
            check_type(argname="argument host_role", value=host_role, expected_type=type_hints["host_role"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument internal_target_group_arn", value=internal_target_group_arn, expected_type=type_hints["internal_target_group_arn"])
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
            check_type(argname="argument sm_cert_name", value=sm_cert_name, expected_type=type_hints["sm_cert_name"])
            check_type(argname="argument ssl_target_group_arn", value=ssl_target_group_arn, expected_type=type_hints["ssl_target_group_arn"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
            check_type(argname="argument user_data_directory", value=user_data_directory, expected_type=type_hints["user_data_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if artifactory_efs_file_system is not None:
            self._values["artifactory_efs_file_system"] = artifactory_efs_file_system
        if artifactory_licenses_secret_name is not None:
            self._values["artifactory_licenses_secret_name"] = artifactory_licenses_secret_name
        if artifactory_primary is not None:
            self._values["artifactory_primary"] = artifactory_primary
        if artifactory_product is not None:
            self._values["artifactory_product"] = artifactory_product
        if artifactory_s3_bucket is not None:
            self._values["artifactory_s3_bucket"] = artifactory_s3_bucket
        if artifactory_server_name is not None:
            self._values["artifactory_server_name"] = artifactory_server_name
        if artifactory_version is not None:
            self._values["artifactory_version"] = artifactory_version
        if database_driver is not None:
            self._values["database_driver"] = database_driver
        if database_password is not None:
            self._values["database_password"] = database_password
        if database_plugin is not None:
            self._values["database_plugin"] = database_plugin
        if database_plugin_url is not None:
            self._values["database_plugin_url"] = database_plugin_url
        if database_type is not None:
            self._values["database_type"] = database_type
        if database_url is not None:
            self._values["database_url"] = database_url
        if database_user is not None:
            self._values["database_user"] = database_user
        if deployment_tag is not None:
            self._values["deployment_tag"] = deployment_tag
        if extra_java_options is not None:
            self._values["extra_java_options"] = extra_java_options
        if host_profile is not None:
            self._values["host_profile"] = host_profile
        if host_role is not None:
            self._values["host_role"] = host_role
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if internal_target_group_arn is not None:
            self._values["internal_target_group_arn"] = internal_target_group_arn
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
        if sm_cert_name is not None:
            self._values["sm_cert_name"] = sm_cert_name
        if ssl_target_group_arn is not None:
            self._values["ssl_target_group_arn"] = ssl_target_group_arn
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn
        if user_data_directory is not None:
            self._values["user_data_directory"] = user_data_directory

    @builtins.property
    def artifactory_efs_file_system(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryEfsFileSystem
        '''
        result = self._values.get("artifactory_efs_file_system")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem"], result)

    @builtins.property
    def artifactory_licenses_secret_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryLicensesSecretName
        '''
        result = self._values.get("artifactory_licenses_secret_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName"], result)

    @builtins.property
    def artifactory_primary(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryPrimary"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryPrimary
        '''
        result = self._values.get("artifactory_primary")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryPrimary"], result)

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
    def artifactory_s3_bucket(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryS3Bucket
        '''
        result = self._values.get("artifactory_s3_bucket")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket"], result)

    @builtins.property
    def artifactory_server_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryServerName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryServerName
        '''
        result = self._values.get("artifactory_server_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryServerName"], result)

    @builtins.property
    def artifactory_version(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryVersion"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryVersion
        '''
        result = self._values.get("artifactory_version")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryVersion"], result)

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
    def database_plugin(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePlugin"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabasePlugin
        '''
        result = self._values.get("database_plugin")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePlugin"], result)

    @builtins.property
    def database_plugin_url(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePluginUrl"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabasePluginUrl
        '''
        result = self._values.get("database_plugin_url")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePluginUrl"], result)

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
    def database_url(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUrl"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseUrl
        '''
        result = self._values.get("database_url")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUrl"], result)

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
    def host_profile(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersHostProfile"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#HostProfile
        '''
        result = self._values.get("host_profile")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersHostProfile"], result)

    @builtins.property
    def host_role(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersHostRole"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#HostRole
        '''
        result = self._values.get("host_role")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersHostRole"], result)

    @builtins.property
    def instance_type(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersInstanceType"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersInstanceType"], result)

    @builtins.property
    def internal_target_group_arn(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersInternalTargetGroupArn"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#InternalTargetGroupARN
        '''
        result = self._values.get("internal_target_group_arn")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersInternalTargetGroupArn"], result)

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
    def sm_cert_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersSmCertName"]:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :schema: CfnEc2InstanceModulePropsParameters#SmCertName
        '''
        result = self._values.get("sm_cert_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersSmCertName"], result)

    @builtins.property
    def ssl_target_group_arn(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersSslTargetGroupArn"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#SSLTargetGroupARN
        '''
        result = self._values.get("ssl_target_group_arn")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersSslTargetGroupArn"], result)

    @builtins.property
    def target_group_arn(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersTargetGroupArn"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#TargetGroupARN
        '''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersTargetGroupArn"], result)

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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d212b938d6d27d871dede72ce6a4e6ca24555f36775ce8347ef43ecd4550416)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b88bdddc31c3d1310ec2e5dd097806cacb3cd0f5d718e98abaf2af295714b12a)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryPrimary",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryPrimary:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryPrimary
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69695b8736a2fa51e3c081f2619dd4788eefd2da50bc79ece52e0545910163ab)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryPrimary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryPrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryProduct",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a704bbeb67cfb16c8644ca48f0690baf741bacadb1202f7cd9395b2904a1cfa1)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a31d8d6e99892e21a575e5191773ba9e026a49bda2e4ca7f889b2082965bbd9e)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryServerName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryServerName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryServerName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f70d172ce26a93bef94d093da63dc01d49bfa10c7d500e6f17693d93b8455e15)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryServerName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryServerName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryVersion",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryVersion:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryVersion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad49aa2da4c44f28f1750e71377ab133616c905e89e232aed22a4913862f519e)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseDriver",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6541d2e86e31cc6352a99457e4f10c80a45615b3c09557593e2095f627785a4d)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabasePassword",
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
            type_hints = typing.get_type_hints(_typecheckingstub__028221ab4f9ded6a79328e0a70c81e8512255595576ba054d2ab8f1e3fdfc63b)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabasePlugin",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabasePlugin:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabasePlugin
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22caab021a4f1474208d29bc50de2cafae969cd7305a37e9d5c9b97987f2a96)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabasePlugin#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabasePlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabasePluginUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabasePluginUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabasePluginUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e91f84f342224f5a8f69b1ff85d94c304d82f3c5ea9de094b3b8de152edcab7)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabasePluginUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabasePluginUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseType",
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
            type_hints = typing.get_type_hints(_typecheckingstub__678577d5aab389a7af1f8d3ccd8267fd60a82413683109ab5624fd192937d7f1)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99e662dac89d8a1aa9fa5fc7f75da4602f09b6d3d335f433eea35c6de7267f9)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseUser",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80ad90900ce662598b204e06222af0768d8695d0977cf1b76fbb09b2a48535f7)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDeploymentTag",
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
            type_hints = typing.get_type_hints(_typecheckingstub__59ea3868ed07c04f851fe7266a53c452819eaa3763d0d7cc9159293b2451e0c2)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersExtraJavaOptions",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56015ce9d3263c22f53a1bead1d17f844a962a63d5e2d9218a7b599681a0120b)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersHostProfile",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersHostProfile:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersHostProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f233c0851779c967b3d860edde9ac3079f2c9e0a81fe03ea3080227e94af3912)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersHostProfile#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersHostRole",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersHostRole:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersHostRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c6b634ae4c48981fd51e8f28610b333808f194d312e42f6c6abb729a843f6c)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersHostRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb0396c1387d43b0e1fe5c87a5f13831760ca5b5a70e98dacaec3d4c32699baf)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersInternalTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersInternalTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersInternalTargetGroupArn
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9bf3210e286cd85065258c843c7f59e3a8d0c1809403822dc9e8a62e0a3179f)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersInternalTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersInternalTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersKeyPairName",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a711d4f1b3a78a3d19dd359ea300f80de04f68b7c0de4efaf69ea07c223d1073)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersLogicalId",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86c83249bb515ae882a4936e3f8563cef951b0d95e57974c9a0de70239a1aef7)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersMasterKey",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8122b864df1e59dda5f28939368a63fc0452534b81adf83b8edcc6f4490187af)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersMaxScalingNodes",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e406bc9a972947271245240ed0b4d1172488f3181832d7ec89b9bca9e5140f52)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersMinScalingNodes",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36e8eb87790f989a6a6040ad2161439c685622e9a286a30a7b3a04d4f9754515)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersPrivateSubnet1Id",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f39c0578ae94bad4892e375359728ea87f3faa3ab0a8965db12af95a572d5f00)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersPrivateSubnet2Id",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbbd2989177658927fb55940934793d2f742d20892325dfab6c00663190782d0)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3BucketName",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57f7d1e15f1d4dbb1ad0a57be70edb0734e07603c95b37098a0e4da46646b7d6)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3KeyPrefix",
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
            type_hints = typing.get_type_hints(_typecheckingstub__df83e6d020f7233d24ac9d351cf858be7803017adffd014685a12eac2acfefcc)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3Uri",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d94e014fda2edd7acb3ac51d3b305e0949d33ebfcc8676b8e3428ba8b6aeb541)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersSecurityGroups",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c71dccc16498d89e43bdb89c5e794e79dbfd287df7fbb621bf7b37c41dd972bc)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersSmCertName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersSmCertName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersSmCertName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__018c08b49729a8ade2b9d8119cc938a3767ef3d6941c52802f883ace7c2497ae)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSmCertName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSmCertName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersSmCertName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersSslTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersSslTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersSslTargetGroupArn
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb1f6c7ed88117d3eddf3cf68202afec46cb7b34a340ea4cd7d91cf8a08a7d1)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSslTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersSslTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersTargetGroupArn
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a25860d9b754ca1f4778cf9fbdfee71a04b8e68e7c16a97810b05c3e8529ed11)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersUserDataDirectory",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac8b1cf62b66e91e438bea7ae578be5bd12c806f34872a162fd7aab3c1b2ca2a)
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_launch_configuration": "artifactoryLaunchConfiguration",
        "artifactory_scaling_group": "artifactoryScalingGroup",
    },
)
class CfnEc2InstanceModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_launch_configuration: typing.Optional[typing.Union["CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_scaling_group: typing.Optional[typing.Union["CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param artifactory_launch_configuration: 
        :param artifactory_scaling_group: 

        :schema: CfnEc2InstanceModulePropsResources
        '''
        if isinstance(artifactory_launch_configuration, dict):
            artifactory_launch_configuration = CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration(**artifactory_launch_configuration)
        if isinstance(artifactory_scaling_group, dict):
            artifactory_scaling_group = CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup(**artifactory_scaling_group)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75123da85339ee8bc5aff6af4117dff68295615e9041ed75251791e22d4d88fd)
            check_type(argname="argument artifactory_launch_configuration", value=artifactory_launch_configuration, expected_type=type_hints["artifactory_launch_configuration"])
            check_type(argname="argument artifactory_scaling_group", value=artifactory_scaling_group, expected_type=type_hints["artifactory_scaling_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if artifactory_launch_configuration is not None:
            self._values["artifactory_launch_configuration"] = artifactory_launch_configuration
        if artifactory_scaling_group is not None:
            self._values["artifactory_scaling_group"] = artifactory_scaling_group

    @builtins.property
    def artifactory_launch_configuration(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration"]:
        '''
        :schema: CfnEc2InstanceModulePropsResources#ArtifactoryLaunchConfiguration
        '''
        result = self._values.get("artifactory_launch_configuration")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration"], result)

    @builtins.property
    def artifactory_scaling_group(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup"]:
        '''
        :schema: CfnEc2InstanceModulePropsResources#ArtifactoryScalingGroup
        '''
        result = self._values.get("artifactory_scaling_group")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fadecf093c58b835022d0659a0e3ba69affad834c70d3bbbadbe94d28e4b2eb)
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
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea0dc7c450793915d675fe02ac9f6706a68f1e63d6f0526ce2562f2f637959cc)
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
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEc2InstanceModule",
    "CfnEc2InstanceModuleProps",
    "CfnEc2InstanceModulePropsParameters",
    "CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem",
    "CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName",
    "CfnEc2InstanceModulePropsParametersArtifactoryPrimary",
    "CfnEc2InstanceModulePropsParametersArtifactoryProduct",
    "CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket",
    "CfnEc2InstanceModulePropsParametersArtifactoryServerName",
    "CfnEc2InstanceModulePropsParametersArtifactoryVersion",
    "CfnEc2InstanceModulePropsParametersDatabaseDriver",
    "CfnEc2InstanceModulePropsParametersDatabasePassword",
    "CfnEc2InstanceModulePropsParametersDatabasePlugin",
    "CfnEc2InstanceModulePropsParametersDatabasePluginUrl",
    "CfnEc2InstanceModulePropsParametersDatabaseType",
    "CfnEc2InstanceModulePropsParametersDatabaseUrl",
    "CfnEc2InstanceModulePropsParametersDatabaseUser",
    "CfnEc2InstanceModulePropsParametersDeploymentTag",
    "CfnEc2InstanceModulePropsParametersExtraJavaOptions",
    "CfnEc2InstanceModulePropsParametersHostProfile",
    "CfnEc2InstanceModulePropsParametersHostRole",
    "CfnEc2InstanceModulePropsParametersInstanceType",
    "CfnEc2InstanceModulePropsParametersInternalTargetGroupArn",
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
    "CfnEc2InstanceModulePropsParametersSmCertName",
    "CfnEc2InstanceModulePropsParametersSslTargetGroupArn",
    "CfnEc2InstanceModulePropsParametersTargetGroupArn",
    "CfnEc2InstanceModulePropsParametersUserDataDirectory",
    "CfnEc2InstanceModulePropsResources",
    "CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration",
    "CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup",
]

publication.publish()

def _typecheckingstub__88fca067515fe4abbe12dba935e582f23fffff965e4f0b1ccffe4e9be342dac2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9da1ac93a152420f41e6cd031f8ed85b5768e4bc598109668fdc93b95cf76c12(
    *,
    parameters: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__259db37424b1c9395758e09af0737955305cf5ab40a492f99b61b25d7b5dcc05(
    *,
    artifactory_efs_file_system: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_licenses_secret_name: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_primary: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryPrimary, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_product: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryProduct, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_s3_bucket: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_server_name: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryServerName, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_version: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersArtifactoryVersion, typing.Dict[builtins.str, typing.Any]]] = None,
    database_driver: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabaseDriver, typing.Dict[builtins.str, typing.Any]]] = None,
    database_password: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabasePassword, typing.Dict[builtins.str, typing.Any]]] = None,
    database_plugin: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabasePlugin, typing.Dict[builtins.str, typing.Any]]] = None,
    database_plugin_url: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabasePluginUrl, typing.Dict[builtins.str, typing.Any]]] = None,
    database_type: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabaseType, typing.Dict[builtins.str, typing.Any]]] = None,
    database_url: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabaseUrl, typing.Dict[builtins.str, typing.Any]]] = None,
    database_user: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDatabaseUser, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_tag: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersDeploymentTag, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_java_options: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersExtraJavaOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    host_profile: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersHostProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    host_role: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersHostRole, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_type: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    internal_target_group_arn: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersInternalTargetGroupArn, typing.Dict[builtins.str, typing.Any]]] = None,
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
    sm_cert_name: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersSmCertName, typing.Dict[builtins.str, typing.Any]]] = None,
    ssl_target_group_arn: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersSslTargetGroupArn, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group_arn: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersTargetGroupArn, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data_directory: typing.Optional[typing.Union[CfnEc2InstanceModulePropsParametersUserDataDirectory, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d212b938d6d27d871dede72ce6a4e6ca24555f36775ce8347ef43ecd4550416(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88bdddc31c3d1310ec2e5dd097806cacb3cd0f5d718e98abaf2af295714b12a(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69695b8736a2fa51e3c081f2619dd4788eefd2da50bc79ece52e0545910163ab(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a704bbeb67cfb16c8644ca48f0690baf741bacadb1202f7cd9395b2904a1cfa1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a31d8d6e99892e21a575e5191773ba9e026a49bda2e4ca7f889b2082965bbd9e(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f70d172ce26a93bef94d093da63dc01d49bfa10c7d500e6f17693d93b8455e15(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad49aa2da4c44f28f1750e71377ab133616c905e89e232aed22a4913862f519e(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6541d2e86e31cc6352a99457e4f10c80a45615b3c09557593e2095f627785a4d(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028221ab4f9ded6a79328e0a70c81e8512255595576ba054d2ab8f1e3fdfc63b(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22caab021a4f1474208d29bc50de2cafae969cd7305a37e9d5c9b97987f2a96(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e91f84f342224f5a8f69b1ff85d94c304d82f3c5ea9de094b3b8de152edcab7(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678577d5aab389a7af1f8d3ccd8267fd60a82413683109ab5624fd192937d7f1(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99e662dac89d8a1aa9fa5fc7f75da4602f09b6d3d335f433eea35c6de7267f9(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ad90900ce662598b204e06222af0768d8695d0977cf1b76fbb09b2a48535f7(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59ea3868ed07c04f851fe7266a53c452819eaa3763d0d7cc9159293b2451e0c2(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56015ce9d3263c22f53a1bead1d17f844a962a63d5e2d9218a7b599681a0120b(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f233c0851779c967b3d860edde9ac3079f2c9e0a81fe03ea3080227e94af3912(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c6b634ae4c48981fd51e8f28610b333808f194d312e42f6c6abb729a843f6c(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb0396c1387d43b0e1fe5c87a5f13831760ca5b5a70e98dacaec3d4c32699baf(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9bf3210e286cd85065258c843c7f59e3a8d0c1809403822dc9e8a62e0a3179f(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a711d4f1b3a78a3d19dd359ea300f80de04f68b7c0de4efaf69ea07c223d1073(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86c83249bb515ae882a4936e3f8563cef951b0d95e57974c9a0de70239a1aef7(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8122b864df1e59dda5f28939368a63fc0452534b81adf83b8edcc6f4490187af(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e406bc9a972947271245240ed0b4d1172488f3181832d7ec89b9bca9e5140f52(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36e8eb87790f989a6a6040ad2161439c685622e9a286a30a7b3a04d4f9754515(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f39c0578ae94bad4892e375359728ea87f3faa3ab0a8965db12af95a572d5f00(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbbd2989177658927fb55940934793d2f742d20892325dfab6c00663190782d0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f7d1e15f1d4dbb1ad0a57be70edb0734e07603c95b37098a0e4da46646b7d6(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df83e6d020f7233d24ac9d351cf858be7803017adffd014685a12eac2acfefcc(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94e014fda2edd7acb3ac51d3b305e0949d33ebfcc8676b8e3428ba8b6aeb541(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c71dccc16498d89e43bdb89c5e794e79dbfd287df7fbb621bf7b37c41dd972bc(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018c08b49729a8ade2b9d8119cc938a3767ef3d6941c52802f883ace7c2497ae(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb1f6c7ed88117d3eddf3cf68202afec46cb7b34a340ea4cd7d91cf8a08a7d1(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25860d9b754ca1f4778cf9fbdfee71a04b8e68e7c16a97810b05c3e8529ed11(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8b1cf62b66e91e438bea7ae578be5bd12c806f34872a162fd7aab3c1b2ca2a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75123da85339ee8bc5aff6af4117dff68295615e9041ed75251791e22d4d88fd(
    *,
    artifactory_launch_configuration: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_scaling_group: typing.Optional[typing.Union[CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fadecf093c58b835022d0659a0e3ba69affad834c70d3bbbadbe94d28e4b2eb(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea0dc7c450793915d675fe02ac9f6706a68f1e63d6f0526ce2562f2f637959cc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
