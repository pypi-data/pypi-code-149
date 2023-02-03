'''
# jfrog-artifactory-newvpc-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Artifactory::NewVpc::MODULE` v1.9.0.

## Description

Schema for Module Fragment of type JFrog::Artifactory::NewVpc::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Artifactory::NewVpc::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Artifactory-NewVpc-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Artifactory::NewVpc::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-artifactory-newvpc-module+v1.9.0).
* Issues related to `JFrog::Artifactory::NewVpc::MODULE` should be reported to the [publisher](undefined).

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


class CfnNewVpcModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModule",
):
    '''A CloudFormation ``JFrog::Artifactory::NewVpc::MODULE``.

    :cloudformationResource: JFrog::Artifactory::NewVpc::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnNewVpcModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnNewVpcModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``JFrog::Artifactory::NewVpc::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0741222943298226354605fa004cceb01685aba4157cf2a306fa3caa36ef194)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNewVpcModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnNewVpcModuleProps":
        '''Resource props.'''
        return typing.cast("CfnNewVpcModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnNewVpcModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnNewVpcModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnNewVpcModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type JFrog::Artifactory::NewVpc::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnNewVpcModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnNewVpcModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnNewVpcModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a65017efcac0082bd85da2045e430f771375df8d16207369ffa7b321ed314d4)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnNewVpcModulePropsParameters"]:
        '''
        :schema: CfnNewVpcModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnNewVpcModulePropsResources"]:
        '''
        :schema: CfnNewVpcModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "access_cidr": "accessCidr",
        "artifactory_product": "artifactoryProduct",
        "artifactory_server_name": "artifactoryServerName",
        "artifactory_version": "artifactoryVersion",
        "availability_zone1": "availabilityZone1",
        "availability_zone2": "availabilityZone2",
        "bastion_enable_tcp_forwarding": "bastionEnableTcpForwarding",
        "bastion_enable_x11_forwarding": "bastionEnableX11Forwarding",
        "bastion_instance_type": "bastionInstanceType",
        "bastion_os": "bastionOs",
        "bastion_root_volume_size": "bastionRootVolumeSize",
        "database_allocated_storage": "databaseAllocatedStorage",
        "database_engine": "databaseEngine",
        "database_instance": "databaseInstance",
        "database_name": "databaseName",
        "database_password": "databasePassword",
        "database_preferred_az": "databasePreferredAz",
        "database_user": "databaseUser",
        "default_java_mem_settings": "defaultJavaMemSettings",
        "enable_bastion": "enableBastion",
        "extra_java_options": "extraJavaOptions",
        "install_xray": "installXray",
        "instance_type": "instanceType",
        "key_pair_name": "keyPairName",
        "logical_id": "logicalId",
        "master_key": "masterKey",
        "multi_az_database": "multiAzDatabase",
        "num_bastion_hosts": "numBastionHosts",
        "number_of_secondary": "numberOfSecondary",
        "private_subnet1_cidr": "privateSubnet1Cidr",
        "private_subnet2_cidr": "privateSubnet2Cidr",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "qs_s3_bucket_name": "qsS3BucketName",
        "qs_s3_bucket_region": "qsS3BucketRegion",
        "qs_s3_key_prefix": "qsS3KeyPrefix",
        "remote_access_cidr": "remoteAccessCidr",
        "sm_cert_name": "smCertName",
        "sm_license_name": "smLicenseName",
        "volume_size": "volumeSize",
        "vpc_cidr": "vpcCidr",
        "xray_database_password": "xrayDatabasePassword",
        "xray_database_user": "xrayDatabaseUser",
        "xray_instance_type": "xrayInstanceType",
        "xray_number_of_instances": "xrayNumberOfInstances",
        "xray_version": "xrayVersion",
    },
)
class CfnNewVpcModulePropsParameters:
    def __init__(
        self,
        *,
        access_cidr: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersAccessCidr", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_product: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersArtifactoryProduct", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_server_name: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersArtifactoryServerName", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_version: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersArtifactoryVersion", typing.Dict[builtins.str, typing.Any]]] = None,
        availability_zone1: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersAvailabilityZone1", typing.Dict[builtins.str, typing.Any]]] = None,
        availability_zone2: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersAvailabilityZone2", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_enable_tcp_forwarding: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersBastionEnableTcpForwarding", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_enable_x11_forwarding: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersBastionEnableX11Forwarding", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_instance_type: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersBastionInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_os: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersBastionOs", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_root_volume_size: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersBastionRootVolumeSize", typing.Dict[builtins.str, typing.Any]]] = None,
        database_allocated_storage: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDatabaseAllocatedStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        database_engine: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDatabaseEngine", typing.Dict[builtins.str, typing.Any]]] = None,
        database_instance: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDatabaseInstance", typing.Dict[builtins.str, typing.Any]]] = None,
        database_name: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDatabaseName", typing.Dict[builtins.str, typing.Any]]] = None,
        database_password: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDatabasePassword", typing.Dict[builtins.str, typing.Any]]] = None,
        database_preferred_az: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDatabasePreferredAz", typing.Dict[builtins.str, typing.Any]]] = None,
        database_user: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDatabaseUser", typing.Dict[builtins.str, typing.Any]]] = None,
        default_java_mem_settings: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersDefaultJavaMemSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_bastion: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersEnableBastion", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_java_options: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersExtraJavaOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        install_xray: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersInstallXray", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_type: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        key_pair_name: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersKeyPairName", typing.Dict[builtins.str, typing.Any]]] = None,
        logical_id: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersLogicalId", typing.Dict[builtins.str, typing.Any]]] = None,
        master_key: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersMasterKey", typing.Dict[builtins.str, typing.Any]]] = None,
        multi_az_database: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersMultiAzDatabase", typing.Dict[builtins.str, typing.Any]]] = None,
        num_bastion_hosts: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersNumBastionHosts", typing.Dict[builtins.str, typing.Any]]] = None,
        number_of_secondary: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersNumberOfSecondary", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_cidr: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersPrivateSubnet1Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_cidr: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersPrivateSubnet2Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1_cidr: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersPublicSubnet1Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2_cidr: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersPublicSubnet2Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        qs_s3_bucket_name: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersQsS3BucketName", typing.Dict[builtins.str, typing.Any]]] = None,
        qs_s3_bucket_region: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersQsS3BucketRegion", typing.Dict[builtins.str, typing.Any]]] = None,
        qs_s3_key_prefix: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersQsS3KeyPrefix", typing.Dict[builtins.str, typing.Any]]] = None,
        remote_access_cidr: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersRemoteAccessCidr", typing.Dict[builtins.str, typing.Any]]] = None,
        sm_cert_name: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersSmCertName", typing.Dict[builtins.str, typing.Any]]] = None,
        sm_license_name: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersSmLicenseName", typing.Dict[builtins.str, typing.Any]]] = None,
        volume_size: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersVolumeSize", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_cidr: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersVpcCidr", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_database_password: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersXrayDatabasePassword", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_database_user: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersXrayDatabaseUser", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_instance_type: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersXrayInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_number_of_instances: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersXrayNumberOfInstances", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_version: typing.Optional[typing.Union["CfnNewVpcModulePropsParametersXrayVersion", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_cidr: CIDR IP range permitted to access Artifactory. It is recommended that you set this value to a trusted IP range. For example, you may want to limit software access to your corporate network.
        :param artifactory_product: JFrog Artifactory product you want to install into an AMI.
        :param artifactory_server_name: Name of your Artifactory server. Ensure that this matches your certificate.
        :param artifactory_version: Version of Artifactory that you want to deploy into the Quick Start. To select the correct version, see the release notes at https://www.jfrog.com/confluence/display/RTF/Release+Notes.
        :param availability_zone1: Availability Zone 1 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param availability_zone2: Availability Zone 2 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param bastion_enable_tcp_forwarding: Choose whether to enable TCP forwarding via bootstrapping of the bastion instance.
        :param bastion_enable_x11_forwarding: Choose true to enable X11 via bootstrapping of the bastion host. Setting this value to true enables X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.
        :param bastion_instance_type: Size of the bastion instances.
        :param bastion_os: Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.
        :param bastion_root_volume_size: Size of the root volume in the bastion instances.
        :param database_allocated_storage: Size in gigabytes of available storage for the database instance.
        :param database_engine: Database engine that you want to run.
        :param database_instance: Size of the database to be deployed as part of the Quick Start.
        :param database_name: Name of your database instance. The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").
        :param database_password: Password for the Artifactory database user.
        :param database_preferred_az: Preferred availability zone for Amazon RDS primary instance.
        :param database_user: Login ID for the master user of your database instance.
        :param default_java_mem_settings: Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM. If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.
        :param enable_bastion: If set to true, a bastion host will be created.
        :param extra_java_options: Set Java options to pass to the JVM for Artifactory. For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.
        :param install_xray: Choose true to install JFrog Xray instance(s).
        :param instance_type: EC2 instance type for the Artifactory instances.
        :param key_pair_name: Name of an existing key pair, which allows you to connect securely to your instance after it launches. This is the key pair you created in your preferred Region.
        :param logical_id: Logical Id of the MODULE.
        :param master_key: Master key for the Artifactory cluster. Generate a master key by using the command '$openssl rand -hex 16'.
        :param multi_az_database: Choose false to create an Amazon RDS instance in a single Availability Zone.
        :param num_bastion_hosts: Number of bastion instances to create.
        :param number_of_secondary: Number of secondary Artifactory servers to complete your HA deployment. To align with Artifactory best practices, the minimum number is two, and the maximum is seven. Do not select more instances than you have licenses for.
        :param private_subnet1_cidr: CIDR block for private subnet 1 located in Availability Zone 1.
        :param private_subnet2_cidr: CIDR block for private subnet 2 located in Availability Zone 2.
        :param public_subnet1_cidr: CIDR block for the public (DMZ) subnet 1 located in Availability Zone 1.
        :param public_subnet2_cidr: CIDR block for the public (DMZ) subnet 2 located in Availability Zone 2.
        :param qs_s3_bucket_name: S3 bucket name for the Quick Start assets. This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).
        :param qs_s3_bucket_region: AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. If you use your own bucket, you must specify your own value.
        :param qs_s3_key_prefix: S3 key prefix for the Quick Start assets. Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).
        :param remote_access_cidr: Remote CIDR range that allows you to connect to the bastion instance by using SSH. It is recommended that you set this value to a trusted IP range. For example, you may want to grant specific ranges from within your corporate network that use the SSH protocol.
        :param sm_cert_name: Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.
        :param sm_license_name: Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.
        :param volume_size: Size in gigabytes of available storage (min 10GB). The Quick Start creates an Amazon Elastic Block Store (Amazon EBS) volumes of this size.
        :param vpc_cidr: CIDR block for the VPC.
        :param xray_database_password: The password for the Xray database user.
        :param xray_database_user: The login ID for the Xray database user.
        :param xray_instance_type: The EC2 instance type for the Xray instances.
        :param xray_number_of_instances: The number of Xray instances servers to complete your HA deployment. The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.
        :param xray_version: The version of Xray that you want to deploy into the Quick Start.

        :schema: CfnNewVpcModulePropsParameters
        '''
        if isinstance(access_cidr, dict):
            access_cidr = CfnNewVpcModulePropsParametersAccessCidr(**access_cidr)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnNewVpcModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(artifactory_server_name, dict):
            artifactory_server_name = CfnNewVpcModulePropsParametersArtifactoryServerName(**artifactory_server_name)
        if isinstance(artifactory_version, dict):
            artifactory_version = CfnNewVpcModulePropsParametersArtifactoryVersion(**artifactory_version)
        if isinstance(availability_zone1, dict):
            availability_zone1 = CfnNewVpcModulePropsParametersAvailabilityZone1(**availability_zone1)
        if isinstance(availability_zone2, dict):
            availability_zone2 = CfnNewVpcModulePropsParametersAvailabilityZone2(**availability_zone2)
        if isinstance(bastion_enable_tcp_forwarding, dict):
            bastion_enable_tcp_forwarding = CfnNewVpcModulePropsParametersBastionEnableTcpForwarding(**bastion_enable_tcp_forwarding)
        if isinstance(bastion_enable_x11_forwarding, dict):
            bastion_enable_x11_forwarding = CfnNewVpcModulePropsParametersBastionEnableX11Forwarding(**bastion_enable_x11_forwarding)
        if isinstance(bastion_instance_type, dict):
            bastion_instance_type = CfnNewVpcModulePropsParametersBastionInstanceType(**bastion_instance_type)
        if isinstance(bastion_os, dict):
            bastion_os = CfnNewVpcModulePropsParametersBastionOs(**bastion_os)
        if isinstance(bastion_root_volume_size, dict):
            bastion_root_volume_size = CfnNewVpcModulePropsParametersBastionRootVolumeSize(**bastion_root_volume_size)
        if isinstance(database_allocated_storage, dict):
            database_allocated_storage = CfnNewVpcModulePropsParametersDatabaseAllocatedStorage(**database_allocated_storage)
        if isinstance(database_engine, dict):
            database_engine = CfnNewVpcModulePropsParametersDatabaseEngine(**database_engine)
        if isinstance(database_instance, dict):
            database_instance = CfnNewVpcModulePropsParametersDatabaseInstance(**database_instance)
        if isinstance(database_name, dict):
            database_name = CfnNewVpcModulePropsParametersDatabaseName(**database_name)
        if isinstance(database_password, dict):
            database_password = CfnNewVpcModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_preferred_az, dict):
            database_preferred_az = CfnNewVpcModulePropsParametersDatabasePreferredAz(**database_preferred_az)
        if isinstance(database_user, dict):
            database_user = CfnNewVpcModulePropsParametersDatabaseUser(**database_user)
        if isinstance(default_java_mem_settings, dict):
            default_java_mem_settings = CfnNewVpcModulePropsParametersDefaultJavaMemSettings(**default_java_mem_settings)
        if isinstance(enable_bastion, dict):
            enable_bastion = CfnNewVpcModulePropsParametersEnableBastion(**enable_bastion)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnNewVpcModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(install_xray, dict):
            install_xray = CfnNewVpcModulePropsParametersInstallXray(**install_xray)
        if isinstance(instance_type, dict):
            instance_type = CfnNewVpcModulePropsParametersInstanceType(**instance_type)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnNewVpcModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnNewVpcModulePropsParametersLogicalId(**logical_id)
        if isinstance(master_key, dict):
            master_key = CfnNewVpcModulePropsParametersMasterKey(**master_key)
        if isinstance(multi_az_database, dict):
            multi_az_database = CfnNewVpcModulePropsParametersMultiAzDatabase(**multi_az_database)
        if isinstance(num_bastion_hosts, dict):
            num_bastion_hosts = CfnNewVpcModulePropsParametersNumBastionHosts(**num_bastion_hosts)
        if isinstance(number_of_secondary, dict):
            number_of_secondary = CfnNewVpcModulePropsParametersNumberOfSecondary(**number_of_secondary)
        if isinstance(private_subnet1_cidr, dict):
            private_subnet1_cidr = CfnNewVpcModulePropsParametersPrivateSubnet1Cidr(**private_subnet1_cidr)
        if isinstance(private_subnet2_cidr, dict):
            private_subnet2_cidr = CfnNewVpcModulePropsParametersPrivateSubnet2Cidr(**private_subnet2_cidr)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnNewVpcModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnNewVpcModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(qs_s3_bucket_name, dict):
            qs_s3_bucket_name = CfnNewVpcModulePropsParametersQsS3BucketName(**qs_s3_bucket_name)
        if isinstance(qs_s3_bucket_region, dict):
            qs_s3_bucket_region = CfnNewVpcModulePropsParametersQsS3BucketRegion(**qs_s3_bucket_region)
        if isinstance(qs_s3_key_prefix, dict):
            qs_s3_key_prefix = CfnNewVpcModulePropsParametersQsS3KeyPrefix(**qs_s3_key_prefix)
        if isinstance(remote_access_cidr, dict):
            remote_access_cidr = CfnNewVpcModulePropsParametersRemoteAccessCidr(**remote_access_cidr)
        if isinstance(sm_cert_name, dict):
            sm_cert_name = CfnNewVpcModulePropsParametersSmCertName(**sm_cert_name)
        if isinstance(sm_license_name, dict):
            sm_license_name = CfnNewVpcModulePropsParametersSmLicenseName(**sm_license_name)
        if isinstance(volume_size, dict):
            volume_size = CfnNewVpcModulePropsParametersVolumeSize(**volume_size)
        if isinstance(vpc_cidr, dict):
            vpc_cidr = CfnNewVpcModulePropsParametersVpcCidr(**vpc_cidr)
        if isinstance(xray_database_password, dict):
            xray_database_password = CfnNewVpcModulePropsParametersXrayDatabasePassword(**xray_database_password)
        if isinstance(xray_database_user, dict):
            xray_database_user = CfnNewVpcModulePropsParametersXrayDatabaseUser(**xray_database_user)
        if isinstance(xray_instance_type, dict):
            xray_instance_type = CfnNewVpcModulePropsParametersXrayInstanceType(**xray_instance_type)
        if isinstance(xray_number_of_instances, dict):
            xray_number_of_instances = CfnNewVpcModulePropsParametersXrayNumberOfInstances(**xray_number_of_instances)
        if isinstance(xray_version, dict):
            xray_version = CfnNewVpcModulePropsParametersXrayVersion(**xray_version)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7d6df41560099ee081a8d2f0cc1c9eed8fb689af85488c5ee16233ece74036c)
            check_type(argname="argument access_cidr", value=access_cidr, expected_type=type_hints["access_cidr"])
            check_type(argname="argument artifactory_product", value=artifactory_product, expected_type=type_hints["artifactory_product"])
            check_type(argname="argument artifactory_server_name", value=artifactory_server_name, expected_type=type_hints["artifactory_server_name"])
            check_type(argname="argument artifactory_version", value=artifactory_version, expected_type=type_hints["artifactory_version"])
            check_type(argname="argument availability_zone1", value=availability_zone1, expected_type=type_hints["availability_zone1"])
            check_type(argname="argument availability_zone2", value=availability_zone2, expected_type=type_hints["availability_zone2"])
            check_type(argname="argument bastion_enable_tcp_forwarding", value=bastion_enable_tcp_forwarding, expected_type=type_hints["bastion_enable_tcp_forwarding"])
            check_type(argname="argument bastion_enable_x11_forwarding", value=bastion_enable_x11_forwarding, expected_type=type_hints["bastion_enable_x11_forwarding"])
            check_type(argname="argument bastion_instance_type", value=bastion_instance_type, expected_type=type_hints["bastion_instance_type"])
            check_type(argname="argument bastion_os", value=bastion_os, expected_type=type_hints["bastion_os"])
            check_type(argname="argument bastion_root_volume_size", value=bastion_root_volume_size, expected_type=type_hints["bastion_root_volume_size"])
            check_type(argname="argument database_allocated_storage", value=database_allocated_storage, expected_type=type_hints["database_allocated_storage"])
            check_type(argname="argument database_engine", value=database_engine, expected_type=type_hints["database_engine"])
            check_type(argname="argument database_instance", value=database_instance, expected_type=type_hints["database_instance"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument database_password", value=database_password, expected_type=type_hints["database_password"])
            check_type(argname="argument database_preferred_az", value=database_preferred_az, expected_type=type_hints["database_preferred_az"])
            check_type(argname="argument database_user", value=database_user, expected_type=type_hints["database_user"])
            check_type(argname="argument default_java_mem_settings", value=default_java_mem_settings, expected_type=type_hints["default_java_mem_settings"])
            check_type(argname="argument enable_bastion", value=enable_bastion, expected_type=type_hints["enable_bastion"])
            check_type(argname="argument extra_java_options", value=extra_java_options, expected_type=type_hints["extra_java_options"])
            check_type(argname="argument install_xray", value=install_xray, expected_type=type_hints["install_xray"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument key_pair_name", value=key_pair_name, expected_type=type_hints["key_pair_name"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument master_key", value=master_key, expected_type=type_hints["master_key"])
            check_type(argname="argument multi_az_database", value=multi_az_database, expected_type=type_hints["multi_az_database"])
            check_type(argname="argument num_bastion_hosts", value=num_bastion_hosts, expected_type=type_hints["num_bastion_hosts"])
            check_type(argname="argument number_of_secondary", value=number_of_secondary, expected_type=type_hints["number_of_secondary"])
            check_type(argname="argument private_subnet1_cidr", value=private_subnet1_cidr, expected_type=type_hints["private_subnet1_cidr"])
            check_type(argname="argument private_subnet2_cidr", value=private_subnet2_cidr, expected_type=type_hints["private_subnet2_cidr"])
            check_type(argname="argument public_subnet1_cidr", value=public_subnet1_cidr, expected_type=type_hints["public_subnet1_cidr"])
            check_type(argname="argument public_subnet2_cidr", value=public_subnet2_cidr, expected_type=type_hints["public_subnet2_cidr"])
            check_type(argname="argument qs_s3_bucket_name", value=qs_s3_bucket_name, expected_type=type_hints["qs_s3_bucket_name"])
            check_type(argname="argument qs_s3_bucket_region", value=qs_s3_bucket_region, expected_type=type_hints["qs_s3_bucket_region"])
            check_type(argname="argument qs_s3_key_prefix", value=qs_s3_key_prefix, expected_type=type_hints["qs_s3_key_prefix"])
            check_type(argname="argument remote_access_cidr", value=remote_access_cidr, expected_type=type_hints["remote_access_cidr"])
            check_type(argname="argument sm_cert_name", value=sm_cert_name, expected_type=type_hints["sm_cert_name"])
            check_type(argname="argument sm_license_name", value=sm_license_name, expected_type=type_hints["sm_license_name"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument vpc_cidr", value=vpc_cidr, expected_type=type_hints["vpc_cidr"])
            check_type(argname="argument xray_database_password", value=xray_database_password, expected_type=type_hints["xray_database_password"])
            check_type(argname="argument xray_database_user", value=xray_database_user, expected_type=type_hints["xray_database_user"])
            check_type(argname="argument xray_instance_type", value=xray_instance_type, expected_type=type_hints["xray_instance_type"])
            check_type(argname="argument xray_number_of_instances", value=xray_number_of_instances, expected_type=type_hints["xray_number_of_instances"])
            check_type(argname="argument xray_version", value=xray_version, expected_type=type_hints["xray_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_cidr is not None:
            self._values["access_cidr"] = access_cidr
        if artifactory_product is not None:
            self._values["artifactory_product"] = artifactory_product
        if artifactory_server_name is not None:
            self._values["artifactory_server_name"] = artifactory_server_name
        if artifactory_version is not None:
            self._values["artifactory_version"] = artifactory_version
        if availability_zone1 is not None:
            self._values["availability_zone1"] = availability_zone1
        if availability_zone2 is not None:
            self._values["availability_zone2"] = availability_zone2
        if bastion_enable_tcp_forwarding is not None:
            self._values["bastion_enable_tcp_forwarding"] = bastion_enable_tcp_forwarding
        if bastion_enable_x11_forwarding is not None:
            self._values["bastion_enable_x11_forwarding"] = bastion_enable_x11_forwarding
        if bastion_instance_type is not None:
            self._values["bastion_instance_type"] = bastion_instance_type
        if bastion_os is not None:
            self._values["bastion_os"] = bastion_os
        if bastion_root_volume_size is not None:
            self._values["bastion_root_volume_size"] = bastion_root_volume_size
        if database_allocated_storage is not None:
            self._values["database_allocated_storage"] = database_allocated_storage
        if database_engine is not None:
            self._values["database_engine"] = database_engine
        if database_instance is not None:
            self._values["database_instance"] = database_instance
        if database_name is not None:
            self._values["database_name"] = database_name
        if database_password is not None:
            self._values["database_password"] = database_password
        if database_preferred_az is not None:
            self._values["database_preferred_az"] = database_preferred_az
        if database_user is not None:
            self._values["database_user"] = database_user
        if default_java_mem_settings is not None:
            self._values["default_java_mem_settings"] = default_java_mem_settings
        if enable_bastion is not None:
            self._values["enable_bastion"] = enable_bastion
        if extra_java_options is not None:
            self._values["extra_java_options"] = extra_java_options
        if install_xray is not None:
            self._values["install_xray"] = install_xray
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if logical_id is not None:
            self._values["logical_id"] = logical_id
        if master_key is not None:
            self._values["master_key"] = master_key
        if multi_az_database is not None:
            self._values["multi_az_database"] = multi_az_database
        if num_bastion_hosts is not None:
            self._values["num_bastion_hosts"] = num_bastion_hosts
        if number_of_secondary is not None:
            self._values["number_of_secondary"] = number_of_secondary
        if private_subnet1_cidr is not None:
            self._values["private_subnet1_cidr"] = private_subnet1_cidr
        if private_subnet2_cidr is not None:
            self._values["private_subnet2_cidr"] = private_subnet2_cidr
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
        if qs_s3_bucket_name is not None:
            self._values["qs_s3_bucket_name"] = qs_s3_bucket_name
        if qs_s3_bucket_region is not None:
            self._values["qs_s3_bucket_region"] = qs_s3_bucket_region
        if qs_s3_key_prefix is not None:
            self._values["qs_s3_key_prefix"] = qs_s3_key_prefix
        if remote_access_cidr is not None:
            self._values["remote_access_cidr"] = remote_access_cidr
        if sm_cert_name is not None:
            self._values["sm_cert_name"] = sm_cert_name
        if sm_license_name is not None:
            self._values["sm_license_name"] = sm_license_name
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if vpc_cidr is not None:
            self._values["vpc_cidr"] = vpc_cidr
        if xray_database_password is not None:
            self._values["xray_database_password"] = xray_database_password
        if xray_database_user is not None:
            self._values["xray_database_user"] = xray_database_user
        if xray_instance_type is not None:
            self._values["xray_instance_type"] = xray_instance_type
        if xray_number_of_instances is not None:
            self._values["xray_number_of_instances"] = xray_number_of_instances
        if xray_version is not None:
            self._values["xray_version"] = xray_version

    @builtins.property
    def access_cidr(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersAccessCidr"]:
        '''CIDR IP range permitted to access Artifactory.

        It is recommended that you set this value to a trusted IP range. For example, you may want to limit software access to your corporate network.

        :schema: CfnNewVpcModulePropsParameters#AccessCidr
        '''
        result = self._values.get("access_cidr")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersAccessCidr"], result)

    @builtins.property
    def artifactory_product(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersArtifactoryProduct"]:
        '''JFrog Artifactory product you want to install into an AMI.

        :schema: CfnNewVpcModulePropsParameters#ArtifactoryProduct
        '''
        result = self._values.get("artifactory_product")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersArtifactoryProduct"], result)

    @builtins.property
    def artifactory_server_name(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersArtifactoryServerName"]:
        '''Name of your Artifactory server.

        Ensure that this matches your certificate.

        :schema: CfnNewVpcModulePropsParameters#ArtifactoryServerName
        '''
        result = self._values.get("artifactory_server_name")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersArtifactoryServerName"], result)

    @builtins.property
    def artifactory_version(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersArtifactoryVersion"]:
        '''Version of Artifactory that you want to deploy into the Quick Start.

        To select the correct version, see the release notes at https://www.jfrog.com/confluence/display/RTF/Release+Notes.

        :schema: CfnNewVpcModulePropsParameters#ArtifactoryVersion
        '''
        result = self._values.get("artifactory_version")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersArtifactoryVersion"], result)

    @builtins.property
    def availability_zone1(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersAvailabilityZone1"]:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnNewVpcModulePropsParameters#AvailabilityZone1
        '''
        result = self._values.get("availability_zone1")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersAvailabilityZone1"], result)

    @builtins.property
    def availability_zone2(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersAvailabilityZone2"]:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnNewVpcModulePropsParameters#AvailabilityZone2
        '''
        result = self._values.get("availability_zone2")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersAvailabilityZone2"], result)

    @builtins.property
    def bastion_enable_tcp_forwarding(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersBastionEnableTcpForwarding"]:
        '''Choose whether to enable TCP forwarding via bootstrapping of the bastion instance.

        :schema: CfnNewVpcModulePropsParameters#BastionEnableTcpForwarding
        '''
        result = self._values.get("bastion_enable_tcp_forwarding")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersBastionEnableTcpForwarding"], result)

    @builtins.property
    def bastion_enable_x11_forwarding(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersBastionEnableX11Forwarding"]:
        '''Choose true to enable X11 via bootstrapping of the bastion host.

        Setting this value to true enables X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.

        :schema: CfnNewVpcModulePropsParameters#BastionEnableX11Forwarding
        '''
        result = self._values.get("bastion_enable_x11_forwarding")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersBastionEnableX11Forwarding"], result)

    @builtins.property
    def bastion_instance_type(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersBastionInstanceType"]:
        '''Size of the bastion instances.

        :schema: CfnNewVpcModulePropsParameters#BastionInstanceType
        '''
        result = self._values.get("bastion_instance_type")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersBastionInstanceType"], result)

    @builtins.property
    def bastion_os(self) -> typing.Optional["CfnNewVpcModulePropsParametersBastionOs"]:
        '''Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.

        :schema: CfnNewVpcModulePropsParameters#BastionOs
        '''
        result = self._values.get("bastion_os")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersBastionOs"], result)

    @builtins.property
    def bastion_root_volume_size(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersBastionRootVolumeSize"]:
        '''Size of the root volume in the bastion instances.

        :schema: CfnNewVpcModulePropsParameters#BastionRootVolumeSize
        '''
        result = self._values.get("bastion_root_volume_size")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersBastionRootVolumeSize"], result)

    @builtins.property
    def database_allocated_storage(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDatabaseAllocatedStorage"]:
        '''Size in gigabytes of available storage for the database instance.

        :schema: CfnNewVpcModulePropsParameters#DatabaseAllocatedStorage
        '''
        result = self._values.get("database_allocated_storage")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDatabaseAllocatedStorage"], result)

    @builtins.property
    def database_engine(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDatabaseEngine"]:
        '''Database engine that you want to run.

        :schema: CfnNewVpcModulePropsParameters#DatabaseEngine
        '''
        result = self._values.get("database_engine")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDatabaseEngine"], result)

    @builtins.property
    def database_instance(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDatabaseInstance"]:
        '''Size of the database to be deployed as part of the Quick Start.

        :schema: CfnNewVpcModulePropsParameters#DatabaseInstance
        '''
        result = self._values.get("database_instance")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDatabaseInstance"], result)

    @builtins.property
    def database_name(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDatabaseName"]:
        '''Name of your database instance.

        The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").

        :schema: CfnNewVpcModulePropsParameters#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDatabaseName"], result)

    @builtins.property
    def database_password(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDatabasePassword"]:
        '''Password for the Artifactory database user.

        :schema: CfnNewVpcModulePropsParameters#DatabasePassword
        '''
        result = self._values.get("database_password")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDatabasePassword"], result)

    @builtins.property
    def database_preferred_az(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDatabasePreferredAz"]:
        '''Preferred availability zone for Amazon RDS primary instance.

        :schema: CfnNewVpcModulePropsParameters#DatabasePreferredAz
        '''
        result = self._values.get("database_preferred_az")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDatabasePreferredAz"], result)

    @builtins.property
    def database_user(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDatabaseUser"]:
        '''Login ID for the master user of your database instance.

        :schema: CfnNewVpcModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def default_java_mem_settings(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersDefaultJavaMemSettings"]:
        '''Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM.

        If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.

        :schema: CfnNewVpcModulePropsParameters#DefaultJavaMemSettings
        '''
        result = self._values.get("default_java_mem_settings")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersDefaultJavaMemSettings"], result)

    @builtins.property
    def enable_bastion(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersEnableBastion"]:
        '''If set to true, a bastion host will be created.

        :schema: CfnNewVpcModulePropsParameters#EnableBastion
        '''
        result = self._values.get("enable_bastion")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersEnableBastion"], result)

    @builtins.property
    def extra_java_options(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersExtraJavaOptions"]:
        '''Set Java options to pass to the JVM for Artifactory.

        For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.

        :schema: CfnNewVpcModulePropsParameters#ExtraJavaOptions
        '''
        result = self._values.get("extra_java_options")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersExtraJavaOptions"], result)

    @builtins.property
    def install_xray(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersInstallXray"]:
        '''Choose true to install JFrog Xray instance(s).

        :schema: CfnNewVpcModulePropsParameters#InstallXray
        '''
        result = self._values.get("install_xray")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersInstallXray"], result)

    @builtins.property
    def instance_type(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersInstanceType"]:
        '''EC2 instance type for the Artifactory instances.

        :schema: CfnNewVpcModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersInstanceType"], result)

    @builtins.property
    def key_pair_name(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersKeyPairName"]:
        '''Name of an existing key pair, which allows you to connect securely to your instance after it launches.

        This is the key pair you created in your preferred Region.

        :schema: CfnNewVpcModulePropsParameters#KeyPairName
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersKeyPairName"], result)

    @builtins.property
    def logical_id(self) -> typing.Optional["CfnNewVpcModulePropsParametersLogicalId"]:
        '''Logical Id of the MODULE.

        :schema: CfnNewVpcModulePropsParameters#LogicalId
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersLogicalId"], result)

    @builtins.property
    def master_key(self) -> typing.Optional["CfnNewVpcModulePropsParametersMasterKey"]:
        '''Master key for the Artifactory cluster.

        Generate a master key by using the command '$openssl rand -hex 16'.

        :schema: CfnNewVpcModulePropsParameters#MasterKey
        '''
        result = self._values.get("master_key")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersMasterKey"], result)

    @builtins.property
    def multi_az_database(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersMultiAzDatabase"]:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :schema: CfnNewVpcModulePropsParameters#MultiAzDatabase
        '''
        result = self._values.get("multi_az_database")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersMultiAzDatabase"], result)

    @builtins.property
    def num_bastion_hosts(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersNumBastionHosts"]:
        '''Number of bastion instances to create.

        :schema: CfnNewVpcModulePropsParameters#NumBastionHosts
        '''
        result = self._values.get("num_bastion_hosts")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersNumBastionHosts"], result)

    @builtins.property
    def number_of_secondary(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersNumberOfSecondary"]:
        '''Number of secondary Artifactory servers to complete your HA deployment.

        To align with Artifactory best practices, the minimum number is two, and the maximum is seven. Do not select more instances than you have licenses for.

        :schema: CfnNewVpcModulePropsParameters#NumberOfSecondary
        '''
        result = self._values.get("number_of_secondary")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersNumberOfSecondary"], result)

    @builtins.property
    def private_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersPrivateSubnet1Cidr"]:
        '''CIDR block for private subnet 1 located in Availability Zone 1.

        :schema: CfnNewVpcModulePropsParameters#PrivateSubnet1Cidr
        '''
        result = self._values.get("private_subnet1_cidr")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersPrivateSubnet1Cidr"], result)

    @builtins.property
    def private_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersPrivateSubnet2Cidr"]:
        '''CIDR block for private subnet 2 located in Availability Zone 2.

        :schema: CfnNewVpcModulePropsParameters#PrivateSubnet2Cidr
        '''
        result = self._values.get("private_subnet2_cidr")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersPrivateSubnet2Cidr"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersPublicSubnet1Cidr"]:
        '''CIDR block for the public (DMZ) subnet 1 located in Availability Zone 1.

        :schema: CfnNewVpcModulePropsParameters#PublicSubnet1Cidr
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersPublicSubnet2Cidr"]:
        '''CIDR block for the public (DMZ) subnet 2 located in Availability Zone 2.

        :schema: CfnNewVpcModulePropsParameters#PublicSubnet2Cidr
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def qs_s3_bucket_name(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersQsS3BucketName"]:
        '''S3 bucket name for the Quick Start assets.

        This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :schema: CfnNewVpcModulePropsParameters#QsS3BucketName
        '''
        result = self._values.get("qs_s3_bucket_name")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersQsS3BucketName"], result)

    @builtins.property
    def qs_s3_bucket_region(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersQsS3BucketRegion"]:
        '''AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        If you use your own bucket, you must specify your own value.

        :schema: CfnNewVpcModulePropsParameters#QsS3BucketRegion
        '''
        result = self._values.get("qs_s3_bucket_region")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersQsS3BucketRegion"], result)

    @builtins.property
    def qs_s3_key_prefix(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersQsS3KeyPrefix"]:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).

        :schema: CfnNewVpcModulePropsParameters#QsS3KeyPrefix
        '''
        result = self._values.get("qs_s3_key_prefix")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersQsS3KeyPrefix"], result)

    @builtins.property
    def remote_access_cidr(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersRemoteAccessCidr"]:
        '''Remote CIDR range that allows you to connect to the bastion instance by using SSH.

        It is recommended that you set this value to a trusted IP range. For example, you may want to grant specific ranges from within your corporate network that use the SSH protocol.

        :schema: CfnNewVpcModulePropsParameters#RemoteAccessCidr
        '''
        result = self._values.get("remote_access_cidr")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersRemoteAccessCidr"], result)

    @builtins.property
    def sm_cert_name(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersSmCertName"]:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :schema: CfnNewVpcModulePropsParameters#SmCertName
        '''
        result = self._values.get("sm_cert_name")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersSmCertName"], result)

    @builtins.property
    def sm_license_name(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersSmLicenseName"]:
        '''Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.

        :schema: CfnNewVpcModulePropsParameters#SmLicenseName
        '''
        result = self._values.get("sm_license_name")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersSmLicenseName"], result)

    @builtins.property
    def volume_size(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersVolumeSize"]:
        '''Size in gigabytes of available storage (min 10GB).

        The Quick Start creates an Amazon Elastic Block Store (Amazon EBS) volumes of this size.

        :schema: CfnNewVpcModulePropsParameters#VolumeSize
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersVolumeSize"], result)

    @builtins.property
    def vpc_cidr(self) -> typing.Optional["CfnNewVpcModulePropsParametersVpcCidr"]:
        '''CIDR block for the VPC.

        :schema: CfnNewVpcModulePropsParameters#VpcCidr
        '''
        result = self._values.get("vpc_cidr")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersVpcCidr"], result)

    @builtins.property
    def xray_database_password(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersXrayDatabasePassword"]:
        '''The password for the Xray database user.

        :schema: CfnNewVpcModulePropsParameters#XrayDatabasePassword
        '''
        result = self._values.get("xray_database_password")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersXrayDatabasePassword"], result)

    @builtins.property
    def xray_database_user(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersXrayDatabaseUser"]:
        '''The login ID for the Xray database user.

        :schema: CfnNewVpcModulePropsParameters#XrayDatabaseUser
        '''
        result = self._values.get("xray_database_user")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersXrayDatabaseUser"], result)

    @builtins.property
    def xray_instance_type(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersXrayInstanceType"]:
        '''The EC2 instance type for the Xray instances.

        :schema: CfnNewVpcModulePropsParameters#XrayInstanceType
        '''
        result = self._values.get("xray_instance_type")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersXrayInstanceType"], result)

    @builtins.property
    def xray_number_of_instances(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersXrayNumberOfInstances"]:
        '''The number of Xray instances servers to complete your HA deployment.

        The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.

        :schema: CfnNewVpcModulePropsParameters#XrayNumberOfInstances
        '''
        result = self._values.get("xray_number_of_instances")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersXrayNumberOfInstances"], result)

    @builtins.property
    def xray_version(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsParametersXrayVersion"]:
        '''The version of Xray that you want to deploy into the Quick Start.

        :schema: CfnNewVpcModulePropsParameters#XrayVersion
        '''
        result = self._values.get("xray_version")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsParametersXrayVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR IP range permitted to access Artifactory.

        It is recommended that you set this value to a trusted IP range. For example, you may want to limit software access to your corporate network.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersAccessCidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f4cadef85efbd379bdf17aef584b351abe0775d67262fbbf3e6ffb1c3650f73)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersArtifactoryProduct",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersArtifactoryProduct:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JFrog Artifactory product you want to install into an AMI.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersArtifactoryProduct
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e948f8ccf9dd3b45597c3836d1af62db60d0203fa209a3318496a3e4c2d45d7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersArtifactoryProduct#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersArtifactoryProduct#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersArtifactoryProduct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersArtifactoryServerName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersArtifactoryServerName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of your Artifactory server.

        Ensure that this matches your certificate.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersArtifactoryServerName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f555fa045b011debf1f56129eb9104c1b6f44941cd55b572d08ddb3b4a320825)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersArtifactoryServerName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersArtifactoryServerName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersArtifactoryServerName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersArtifactoryVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersArtifactoryVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Version of Artifactory that you want to deploy into the Quick Start.

        To select the correct version, see the release notes at https://www.jfrog.com/confluence/display/RTF/Release+Notes.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersArtifactoryVersion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00511406890732e5d987d774c987946cf27339031f242f4bf73de27cfc7f73ac)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersArtifactoryVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersArtifactoryVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersArtifactoryVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersAvailabilityZone1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersAvailabilityZone1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersAvailabilityZone1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4dc50654d2f13210d433cf789db723ce5d865fa52b8afd58afb1748e68682ee)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersAvailabilityZone1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersAvailabilityZone1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersAvailabilityZone1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersAvailabilityZone2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersAvailabilityZone2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersAvailabilityZone2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd9949755fe9abb8a0d1dd20e8facc19595125e4f23d3cb570e5102474fa5e68)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersAvailabilityZone2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersAvailabilityZone2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersAvailabilityZone2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersBastionEnableTcpForwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersBastionEnableTcpForwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose whether to enable TCP forwarding via bootstrapping of the bastion instance.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersBastionEnableTcpForwarding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61cce5b0063840a0c9ca83f4ff83f9cf68335e00923ff3c8494f7438fb7fbd9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionEnableTcpForwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionEnableTcpForwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersBastionEnableTcpForwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersBastionEnableX11Forwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersBastionEnableX11Forwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose true to enable X11 via bootstrapping of the bastion host.

        Setting this value to true enables X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersBastionEnableX11Forwarding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d9754144119bf9e1f1555be15927dddab740cae491b1f2588db93467b6ef95e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionEnableX11Forwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionEnableX11Forwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersBastionEnableX11Forwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersBastionInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersBastionInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersBastionInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5ebe2c00ef0c93614379d91a7e7d03d9b48ec665f90facbf5a91fcc286311f8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersBastionInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersBastionOs",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersBastionOs:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersBastionOs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d5c11bc60b89dc3136de100505bc048fbe3fafe3bf9bce00fa820a0eb4547e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionOs#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionOs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersBastionOs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersBastionRootVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersBastionRootVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the root volume in the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersBastionRootVolumeSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddfec493d398ade8d41d2313f63b1e47d7692311a7514263665c292b6b8cfba3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionRootVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersBastionRootVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersBastionRootVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDatabaseAllocatedStorage",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDatabaseAllocatedStorage:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size in gigabytes of available storage for the database instance.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDatabaseAllocatedStorage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473d776a140f7cb9c56e1ab0e829995f237bc26961f419b66c119d74d2b34336)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseAllocatedStorage#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseAllocatedStorage#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDatabaseAllocatedStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDatabaseEngine",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDatabaseEngine:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Database engine that you want to run.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDatabaseEngine
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e65cf573bb11d96d772709295e34dddc331a815ab4d927421eb09260b17684a1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseEngine#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseEngine#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDatabaseEngine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDatabaseInstance",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDatabaseInstance:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the database to be deployed as part of the Quick Start.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDatabaseInstance
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e228006d8266416b63dd71f1b012cce2b905e7edeac73717e498cf71360fabe)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseInstance#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseInstance#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDatabaseInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDatabaseName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDatabaseName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of your database instance.

        The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDatabaseName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe10fc80b09eb85cffc43b12fc36849d38650c0e1d77d844c17e6222684e8bd3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDatabaseName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDatabasePassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Password for the Artifactory database user.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDatabasePassword
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e71fe4bc6910fc4e722660e87ecb3551233e045a4d42d6e47f2f278e39c6f5a1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabasePassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDatabasePreferredAz",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDatabasePreferredAz:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Preferred availability zone for Amazon RDS primary instance.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDatabasePreferredAz
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e94f229bfd18d29a0de5c2c06fdcb41cd10c0def2e87d0147e3ca62d7ab9d5b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabasePreferredAz#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabasePreferredAz#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDatabasePreferredAz(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDatabaseUser:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Login ID for the master user of your database instance.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDatabaseUser
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3538c38b054b8ac09ce4be0ce3a9b312e63371c89a236467e44064aa93b205f9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseUser#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersDefaultJavaMemSettings",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersDefaultJavaMemSettings:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM.

        If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersDefaultJavaMemSettings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f244d32dbd597e763c5a3a15daea3ef34b17cfd4e77bc2d7f8e658ea892a878c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDefaultJavaMemSettings#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersDefaultJavaMemSettings#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersDefaultJavaMemSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersEnableBastion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersEnableBastion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If set to true, a bastion host will be created.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersEnableBastion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__060d4ec1caa58c702af1b0d81dd77ca3c9f0d792e0ad0f5b3916497cf2308e48)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersEnableBastion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersEnableBastion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersEnableBastion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersExtraJavaOptions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersExtraJavaOptions:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set Java options to pass to the JVM for Artifactory.

        For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersExtraJavaOptions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee485b9f0a75ef397bdd274e4355d8c5b72091a04c5836d764822072bac2a767)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersExtraJavaOptions#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersExtraJavaOptions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersExtraJavaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersInstallXray",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersInstallXray:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose true to install JFrog Xray instance(s).

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersInstallXray
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333ef299ddd159d846039d12552cc981aa0c783fdee947789693ceef3bec868b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersInstallXray#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersInstallXray#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersInstallXray(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EC2 instance type for the Artifactory instances.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22593281d815b41e333b8fbec0f0d497a4c891624655de1d5d22ea62a98f0840)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersKeyPairName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of an existing key pair, which allows you to connect securely to your instance after it launches.

        This is the key pair you created in your preferred Region.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersKeyPairName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ee47689fbd4401cf7a9625827ed96b93793e0d636d03b00e48480ddc08a63a1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersKeyPairName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersKeyPairName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersKeyPairName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersLogicalId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersLogicalId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logical Id of the MODULE.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersLogicalId
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca11277ad047dee3d3dcf72fdb825c8986ec784725ce2ccea57490e5492a28a8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersLogicalId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersLogicalId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersLogicalId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersMasterKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersMasterKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Master key for the Artifactory cluster.

        Generate a master key by using the command '$openssl rand -hex 16'.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersMasterKey
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec30eef77ba33b22837f604feef42204ad6852c14f2afadd2237fe2e00e58bf)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersMasterKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersMasterKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersMasterKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersMultiAzDatabase",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersMultiAzDatabase:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersMultiAzDatabase
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bef8053287ba3fcd497d0f21459f7ffa97a9b155bcb6ea1e2017be0f8e59da6f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersMultiAzDatabase#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersMultiAzDatabase#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersMultiAzDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersNumBastionHosts",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersNumBastionHosts:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of bastion instances to create.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersNumBastionHosts
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9053526b7352be5b0ead9982e3b09c1c304b421e114c5fbf229768d9afb4d104)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersNumBastionHosts#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersNumBastionHosts#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersNumBastionHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersNumberOfSecondary",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersNumberOfSecondary:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of secondary Artifactory servers to complete your HA deployment.

        To align with Artifactory best practices, the minimum number is two, and the maximum is seven. Do not select more instances than you have licenses for.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersNumberOfSecondary
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__555bb726c952f4efa11cfd31e65216293b27e3bbaadd5ce265e1c2a828dac900)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersNumberOfSecondary#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersNumberOfSecondary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersNumberOfSecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersPrivateSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersPrivateSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1 located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersPrivateSubnet1Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20d5b3726d33f5a39331c855d0c34a2865bffb98c8b0c97e749c826d38f895d5)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPrivateSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPrivateSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersPrivateSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersPrivateSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersPrivateSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2 located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersPrivateSubnet2Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d560bbb2cb3925768b9f969ea3d2346e9f4786ae9e70f983cfe25a727c7f683d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPrivateSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPrivateSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersPrivateSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public (DMZ) subnet 1 located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersPublicSubnet1Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__052090ae56da3a00dd9fd9f6a9e8ce83de766f48687f32510849615769f04ae5)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPublicSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPublicSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersPublicSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public (DMZ) subnet 2 located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersPublicSubnet2Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9e347009626622080626543941a7ecd9ed98fd919d7f91298bdec22ac2df2a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPublicSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersPublicSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersPublicSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersQsS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersQsS3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 bucket name for the Quick Start assets.

        This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersQsS3BucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90d6a1efd3b811ca76cd73ca896197500afd015a4d7f4100f17d7faf052b90de)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersQsS3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersQsS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersQsS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersQsS3BucketRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersQsS3BucketRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        If you use your own bucket, you must specify your own value.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersQsS3BucketRegion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce91a331c9eabab8c5ed887bc7c0b228ecf5b2bb6a05f6b14abea19ee28a82a8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersQsS3BucketRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersQsS3BucketRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersQsS3BucketRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersQsS3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersQsS3KeyPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersQsS3KeyPrefix
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50aae96537c0a10deccbbad3713da8973f1e906e201900dc74436c3d1e0d95d6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersQsS3KeyPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersQsS3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersQsS3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersRemoteAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersRemoteAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Remote CIDR range that allows you to connect to the bastion instance by using SSH.

        It is recommended that you set this value to a trusted IP range. For example, you may want to grant specific ranges from within your corporate network that use the SSH protocol.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersRemoteAccessCidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f73c41228d95a89384ee3f0f746f30d9db30f6537088a8c18b68bfccce4aec3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersRemoteAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersRemoteAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersRemoteAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersSmCertName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersSmCertName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersSmCertName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7895b0193ef504898f05c2139a93e0f4c4cc03189f30bfa05949c59aef382cf9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersSmCertName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersSmCertName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersSmCertName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersSmLicenseName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersSmLicenseName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersSmLicenseName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07d79b468b0dfac11b04127a4da911ce5ac246f8f9632b516614cdfe12496c3c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersSmLicenseName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersSmLicenseName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersSmLicenseName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size in gigabytes of available storage (min 10GB).

        The Quick Start creates an Amazon Elastic Block Store (Amazon EBS) volumes of this size.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersVolumeSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__427ce10f570a9072bee5a24b82a61afe2feda1909829d60568061bd9f9589e74)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersVpcCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersVpcCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersVpcCidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20b4f22a89d1ff9bb143a8498b83c100be57043933936a8f5391a1020c64c763)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersVpcCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersVpcCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersVpcCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersXrayDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersXrayDatabasePassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The password for the Xray database user.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersXrayDatabasePassword
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e86a9226d3e7a839c1e1ddb61ba08efd4a01b14865b40c2acbafff7a169987)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayDatabasePassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersXrayDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersXrayDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersXrayDatabaseUser:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The login ID for the Xray database user.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersXrayDatabaseUser
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba40eed96288eba5c34d980524d0c4dbdc04d24b1d3f7207ef2cb9b393fc2647)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayDatabaseUser#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersXrayDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersXrayInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersXrayInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type for the Xray instances.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersXrayInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff62b09d55d7057dfd7dd5fda70cf9b7c9cafeaea844031f7bbab0f23c6bbc4)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersXrayInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersXrayNumberOfInstances",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersXrayNumberOfInstances:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The number of Xray instances servers to complete your HA deployment.

        The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersXrayNumberOfInstances
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ecaf6856b934807d51025ca125c39a109a9c2aefbca4b942c673082ef0604c6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayNumberOfInstances#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayNumberOfInstances#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersXrayNumberOfInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsParametersXrayVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnNewVpcModulePropsParametersXrayVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The version of Xray that you want to deploy into the Quick Start.

        :param description: 
        :param type: 

        :schema: CfnNewVpcModulePropsParametersXrayVersion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efcccbbeb3587ec8e6e67e5bdf1709fbd601c85bca1aca2af2726b1cbbabd743)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnNewVpcModulePropsParametersXrayVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsParametersXrayVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_existing_vpc_stack": "artifactoryExistingVpcStack",
        "artifactory_vpc_stack": "artifactoryVpcStack",
    },
)
class CfnNewVpcModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_existing_vpc_stack: typing.Optional[typing.Union["CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack", typing.Dict[builtins.str, typing.Any]]] = None,
        artifactory_vpc_stack: typing.Optional[typing.Union["CfnNewVpcModulePropsResourcesArtifactoryVpcStack", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param artifactory_existing_vpc_stack: 
        :param artifactory_vpc_stack: 

        :schema: CfnNewVpcModulePropsResources
        '''
        if isinstance(artifactory_existing_vpc_stack, dict):
            artifactory_existing_vpc_stack = CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack(**artifactory_existing_vpc_stack)
        if isinstance(artifactory_vpc_stack, dict):
            artifactory_vpc_stack = CfnNewVpcModulePropsResourcesArtifactoryVpcStack(**artifactory_vpc_stack)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63ca17e125f1da3a5613f0b12b85b4a1fb3a8c5b81b63510e36785a276287377)
            check_type(argname="argument artifactory_existing_vpc_stack", value=artifactory_existing_vpc_stack, expected_type=type_hints["artifactory_existing_vpc_stack"])
            check_type(argname="argument artifactory_vpc_stack", value=artifactory_vpc_stack, expected_type=type_hints["artifactory_vpc_stack"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if artifactory_existing_vpc_stack is not None:
            self._values["artifactory_existing_vpc_stack"] = artifactory_existing_vpc_stack
        if artifactory_vpc_stack is not None:
            self._values["artifactory_vpc_stack"] = artifactory_vpc_stack

    @builtins.property
    def artifactory_existing_vpc_stack(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack"]:
        '''
        :schema: CfnNewVpcModulePropsResources#ArtifactoryExistingVpcStack
        '''
        result = self._values.get("artifactory_existing_vpc_stack")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack"], result)

    @builtins.property
    def artifactory_vpc_stack(
        self,
    ) -> typing.Optional["CfnNewVpcModulePropsResourcesArtifactoryVpcStack"]:
        '''
        :schema: CfnNewVpcModulePropsResources#ArtifactoryVpcStack
        '''
        result = self._values.get("artifactory_vpc_stack")
        return typing.cast(typing.Optional["CfnNewVpcModulePropsResourcesArtifactoryVpcStack"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70b1434380439e4679910add222246e1e24fbc5676d43dd214d68f50c4678233)
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
        :schema: CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnNewVpcModulePropsResourcesArtifactoryVpcStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnNewVpcModulePropsResourcesArtifactoryVpcStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnNewVpcModulePropsResourcesArtifactoryVpcStack
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b2b96512ef71d2c4b2f847b949046e1e5f8d851ff8249932fddf0e48de65293)
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
        :schema: CfnNewVpcModulePropsResourcesArtifactoryVpcStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnNewVpcModulePropsResourcesArtifactoryVpcStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNewVpcModulePropsResourcesArtifactoryVpcStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNewVpcModule",
    "CfnNewVpcModuleProps",
    "CfnNewVpcModulePropsParameters",
    "CfnNewVpcModulePropsParametersAccessCidr",
    "CfnNewVpcModulePropsParametersArtifactoryProduct",
    "CfnNewVpcModulePropsParametersArtifactoryServerName",
    "CfnNewVpcModulePropsParametersArtifactoryVersion",
    "CfnNewVpcModulePropsParametersAvailabilityZone1",
    "CfnNewVpcModulePropsParametersAvailabilityZone2",
    "CfnNewVpcModulePropsParametersBastionEnableTcpForwarding",
    "CfnNewVpcModulePropsParametersBastionEnableX11Forwarding",
    "CfnNewVpcModulePropsParametersBastionInstanceType",
    "CfnNewVpcModulePropsParametersBastionOs",
    "CfnNewVpcModulePropsParametersBastionRootVolumeSize",
    "CfnNewVpcModulePropsParametersDatabaseAllocatedStorage",
    "CfnNewVpcModulePropsParametersDatabaseEngine",
    "CfnNewVpcModulePropsParametersDatabaseInstance",
    "CfnNewVpcModulePropsParametersDatabaseName",
    "CfnNewVpcModulePropsParametersDatabasePassword",
    "CfnNewVpcModulePropsParametersDatabasePreferredAz",
    "CfnNewVpcModulePropsParametersDatabaseUser",
    "CfnNewVpcModulePropsParametersDefaultJavaMemSettings",
    "CfnNewVpcModulePropsParametersEnableBastion",
    "CfnNewVpcModulePropsParametersExtraJavaOptions",
    "CfnNewVpcModulePropsParametersInstallXray",
    "CfnNewVpcModulePropsParametersInstanceType",
    "CfnNewVpcModulePropsParametersKeyPairName",
    "CfnNewVpcModulePropsParametersLogicalId",
    "CfnNewVpcModulePropsParametersMasterKey",
    "CfnNewVpcModulePropsParametersMultiAzDatabase",
    "CfnNewVpcModulePropsParametersNumBastionHosts",
    "CfnNewVpcModulePropsParametersNumberOfSecondary",
    "CfnNewVpcModulePropsParametersPrivateSubnet1Cidr",
    "CfnNewVpcModulePropsParametersPrivateSubnet2Cidr",
    "CfnNewVpcModulePropsParametersPublicSubnet1Cidr",
    "CfnNewVpcModulePropsParametersPublicSubnet2Cidr",
    "CfnNewVpcModulePropsParametersQsS3BucketName",
    "CfnNewVpcModulePropsParametersQsS3BucketRegion",
    "CfnNewVpcModulePropsParametersQsS3KeyPrefix",
    "CfnNewVpcModulePropsParametersRemoteAccessCidr",
    "CfnNewVpcModulePropsParametersSmCertName",
    "CfnNewVpcModulePropsParametersSmLicenseName",
    "CfnNewVpcModulePropsParametersVolumeSize",
    "CfnNewVpcModulePropsParametersVpcCidr",
    "CfnNewVpcModulePropsParametersXrayDatabasePassword",
    "CfnNewVpcModulePropsParametersXrayDatabaseUser",
    "CfnNewVpcModulePropsParametersXrayInstanceType",
    "CfnNewVpcModulePropsParametersXrayNumberOfInstances",
    "CfnNewVpcModulePropsParametersXrayVersion",
    "CfnNewVpcModulePropsResources",
    "CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack",
    "CfnNewVpcModulePropsResourcesArtifactoryVpcStack",
]

publication.publish()

def _typecheckingstub__a0741222943298226354605fa004cceb01685aba4157cf2a306fa3caa36ef194(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnNewVpcModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnNewVpcModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a65017efcac0082bd85da2045e430f771375df8d16207369ffa7b321ed314d4(
    *,
    parameters: typing.Optional[typing.Union[CfnNewVpcModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnNewVpcModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d6df41560099ee081a8d2f0cc1c9eed8fb689af85488c5ee16233ece74036c(
    *,
    access_cidr: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersAccessCidr, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_product: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersArtifactoryProduct, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_server_name: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersArtifactoryServerName, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_version: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersArtifactoryVersion, typing.Dict[builtins.str, typing.Any]]] = None,
    availability_zone1: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersAvailabilityZone1, typing.Dict[builtins.str, typing.Any]]] = None,
    availability_zone2: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersAvailabilityZone2, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_enable_tcp_forwarding: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersBastionEnableTcpForwarding, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_enable_x11_forwarding: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersBastionEnableX11Forwarding, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_instance_type: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersBastionInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_os: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersBastionOs, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_root_volume_size: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersBastionRootVolumeSize, typing.Dict[builtins.str, typing.Any]]] = None,
    database_allocated_storage: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDatabaseAllocatedStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    database_engine: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDatabaseEngine, typing.Dict[builtins.str, typing.Any]]] = None,
    database_instance: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDatabaseInstance, typing.Dict[builtins.str, typing.Any]]] = None,
    database_name: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDatabaseName, typing.Dict[builtins.str, typing.Any]]] = None,
    database_password: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDatabasePassword, typing.Dict[builtins.str, typing.Any]]] = None,
    database_preferred_az: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDatabasePreferredAz, typing.Dict[builtins.str, typing.Any]]] = None,
    database_user: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDatabaseUser, typing.Dict[builtins.str, typing.Any]]] = None,
    default_java_mem_settings: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersDefaultJavaMemSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_bastion: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersEnableBastion, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_java_options: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersExtraJavaOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    install_xray: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersInstallXray, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_type: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    key_pair_name: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersKeyPairName, typing.Dict[builtins.str, typing.Any]]] = None,
    logical_id: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersLogicalId, typing.Dict[builtins.str, typing.Any]]] = None,
    master_key: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersMasterKey, typing.Dict[builtins.str, typing.Any]]] = None,
    multi_az_database: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersMultiAzDatabase, typing.Dict[builtins.str, typing.Any]]] = None,
    num_bastion_hosts: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersNumBastionHosts, typing.Dict[builtins.str, typing.Any]]] = None,
    number_of_secondary: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersNumberOfSecondary, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_cidr: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersPrivateSubnet1Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_cidr: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersPrivateSubnet2Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1_cidr: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersPublicSubnet1Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2_cidr: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersPublicSubnet2Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    qs_s3_bucket_name: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersQsS3BucketName, typing.Dict[builtins.str, typing.Any]]] = None,
    qs_s3_bucket_region: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersQsS3BucketRegion, typing.Dict[builtins.str, typing.Any]]] = None,
    qs_s3_key_prefix: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersQsS3KeyPrefix, typing.Dict[builtins.str, typing.Any]]] = None,
    remote_access_cidr: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersRemoteAccessCidr, typing.Dict[builtins.str, typing.Any]]] = None,
    sm_cert_name: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersSmCertName, typing.Dict[builtins.str, typing.Any]]] = None,
    sm_license_name: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersSmLicenseName, typing.Dict[builtins.str, typing.Any]]] = None,
    volume_size: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersVolumeSize, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_cidr: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersVpcCidr, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_database_password: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersXrayDatabasePassword, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_database_user: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersXrayDatabaseUser, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_instance_type: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersXrayInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_number_of_instances: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersXrayNumberOfInstances, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_version: typing.Optional[typing.Union[CfnNewVpcModulePropsParametersXrayVersion, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f4cadef85efbd379bdf17aef584b351abe0775d67262fbbf3e6ffb1c3650f73(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e948f8ccf9dd3b45597c3836d1af62db60d0203fa209a3318496a3e4c2d45d7(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f555fa045b011debf1f56129eb9104c1b6f44941cd55b572d08ddb3b4a320825(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00511406890732e5d987d774c987946cf27339031f242f4bf73de27cfc7f73ac(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4dc50654d2f13210d433cf789db723ce5d865fa52b8afd58afb1748e68682ee(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd9949755fe9abb8a0d1dd20e8facc19595125e4f23d3cb570e5102474fa5e68(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61cce5b0063840a0c9ca83f4ff83f9cf68335e00923ff3c8494f7438fb7fbd9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d9754144119bf9e1f1555be15927dddab740cae491b1f2588db93467b6ef95e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5ebe2c00ef0c93614379d91a7e7d03d9b48ec665f90facbf5a91fcc286311f8(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d5c11bc60b89dc3136de100505bc048fbe3fafe3bf9bce00fa820a0eb4547e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddfec493d398ade8d41d2313f63b1e47d7692311a7514263665c292b6b8cfba3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473d776a140f7cb9c56e1ab0e829995f237bc26961f419b66c119d74d2b34336(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e65cf573bb11d96d772709295e34dddc331a815ab4d927421eb09260b17684a1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e228006d8266416b63dd71f1b012cce2b905e7edeac73717e498cf71360fabe(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe10fc80b09eb85cffc43b12fc36849d38650c0e1d77d844c17e6222684e8bd3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71fe4bc6910fc4e722660e87ecb3551233e045a4d42d6e47f2f278e39c6f5a1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e94f229bfd18d29a0de5c2c06fdcb41cd10c0def2e87d0147e3ca62d7ab9d5b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3538c38b054b8ac09ce4be0ce3a9b312e63371c89a236467e44064aa93b205f9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f244d32dbd597e763c5a3a15daea3ef34b17cfd4e77bc2d7f8e658ea892a878c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__060d4ec1caa58c702af1b0d81dd77ca3c9f0d792e0ad0f5b3916497cf2308e48(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee485b9f0a75ef397bdd274e4355d8c5b72091a04c5836d764822072bac2a767(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333ef299ddd159d846039d12552cc981aa0c783fdee947789693ceef3bec868b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22593281d815b41e333b8fbec0f0d497a4c891624655de1d5d22ea62a98f0840(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee47689fbd4401cf7a9625827ed96b93793e0d636d03b00e48480ddc08a63a1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca11277ad047dee3d3dcf72fdb825c8986ec784725ce2ccea57490e5492a28a8(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec30eef77ba33b22837f604feef42204ad6852c14f2afadd2237fe2e00e58bf(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef8053287ba3fcd497d0f21459f7ffa97a9b155bcb6ea1e2017be0f8e59da6f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9053526b7352be5b0ead9982e3b09c1c304b421e114c5fbf229768d9afb4d104(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__555bb726c952f4efa11cfd31e65216293b27e3bbaadd5ce265e1c2a828dac900(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20d5b3726d33f5a39331c855d0c34a2865bffb98c8b0c97e749c826d38f895d5(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d560bbb2cb3925768b9f969ea3d2346e9f4786ae9e70f983cfe25a727c7f683d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__052090ae56da3a00dd9fd9f6a9e8ce83de766f48687f32510849615769f04ae5(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9e347009626622080626543941a7ecd9ed98fd919d7f91298bdec22ac2df2a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90d6a1efd3b811ca76cd73ca896197500afd015a4d7f4100f17d7faf052b90de(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce91a331c9eabab8c5ed887bc7c0b228ecf5b2bb6a05f6b14abea19ee28a82a8(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50aae96537c0a10deccbbad3713da8973f1e906e201900dc74436c3d1e0d95d6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f73c41228d95a89384ee3f0f746f30d9db30f6537088a8c18b68bfccce4aec3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7895b0193ef504898f05c2139a93e0f4c4cc03189f30bfa05949c59aef382cf9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07d79b468b0dfac11b04127a4da911ce5ac246f8f9632b516614cdfe12496c3c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427ce10f570a9072bee5a24b82a61afe2feda1909829d60568061bd9f9589e74(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20b4f22a89d1ff9bb143a8498b83c100be57043933936a8f5391a1020c64c763(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e86a9226d3e7a839c1e1ddb61ba08efd4a01b14865b40c2acbafff7a169987(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba40eed96288eba5c34d980524d0c4dbdc04d24b1d3f7207ef2cb9b393fc2647(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff62b09d55d7057dfd7dd5fda70cf9b7c9cafeaea844031f7bbab0f23c6bbc4(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ecaf6856b934807d51025ca125c39a109a9c2aefbca4b942c673082ef0604c6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efcccbbeb3587ec8e6e67e5bdf1709fbd601c85bca1aca2af2726b1cbbabd743(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63ca17e125f1da3a5613f0b12b85b4a1fb3a8c5b81b63510e36785a276287377(
    *,
    artifactory_existing_vpc_stack: typing.Optional[typing.Union[CfnNewVpcModulePropsResourcesArtifactoryExistingVpcStack, typing.Dict[builtins.str, typing.Any]]] = None,
    artifactory_vpc_stack: typing.Optional[typing.Union[CfnNewVpcModulePropsResourcesArtifactoryVpcStack, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b1434380439e4679910add222246e1e24fbc5676d43dd214d68f50c4678233(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b2b96512ef71d2c4b2f847b949046e1e5f8d851ff8249932fddf0e48de65293(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
