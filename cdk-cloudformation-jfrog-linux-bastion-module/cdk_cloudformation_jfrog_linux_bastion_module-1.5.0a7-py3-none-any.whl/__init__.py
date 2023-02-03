'''
# jfrog-linux-bastion-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Linux::Bastion::MODULE` v1.5.0.

## Description

Schema for Module Fragment of type JFrog::Linux::Bastion::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Linux::Bastion::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Linux-Bastion-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Linux::Bastion::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-linux-bastion-module+v1.5.0).
* Issues related to `JFrog::Linux::Bastion::MODULE` should be reported to the [publisher](undefined).

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
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModule",
):
    '''A CloudFormation ``JFrog::Linux::Bastion::MODULE``.

    :cloudformationResource: JFrog::Linux::Bastion::MODULE
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
        '''Create a new ``JFrog::Linux::Bastion::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c7ea32ed00c47eab16c3cc9bc4e9867577fd53e6d68977d1696551378fe2fd5)
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
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Linux::Bastion::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnBastionModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnBastionModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnBastionModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73460fb68f726f53b663e0d59321a2150f678863ec32df8bdb00f829e0a200b)
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
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "alternative_initialization_script": "alternativeInitializationScript",
        "bastion_amios": "bastionAmios",
        "bastion_banner": "bastionBanner",
        "bastion_host_name": "bastionHostName",
        "bastion_instance_type": "bastionInstanceType",
        "bastion_tenancy": "bastionTenancy",
        "enable_banner": "enableBanner",
        "enable_tcp_forwarding": "enableTcpForwarding",
        "enable_x11_forwarding": "enableX11Forwarding",
        "environment_variables": "environmentVariables",
        "key_pair_name": "keyPairName",
        "logical_id": "logicalId",
        "num_bastion_hosts": "numBastionHosts",
        "os_image_override": "osImageOverride",
        "public_subnet1_id": "publicSubnet1Id",
        "public_subnet2_id": "publicSubnet2Id",
        "qss3_bucket_name": "qss3BucketName",
        "qss3_bucket_region": "qss3BucketRegion",
        "qss3_key_prefix": "qss3KeyPrefix",
        "remote_access_cidr": "remoteAccessCidr",
        "root_volume_size": "rootVolumeSize",
        "vpcid": "vpcid",
    },
)
class CfnBastionModulePropsParameters:
    def __init__(
        self,
        *,
        alternative_initialization_script: typing.Optional[typing.Union["CfnBastionModulePropsParametersAlternativeInitializationScript", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_amios: typing.Optional[typing.Union["CfnBastionModulePropsParametersBastionAmios", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_banner: typing.Optional[typing.Union["CfnBastionModulePropsParametersBastionBanner", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_name: typing.Optional[typing.Union["CfnBastionModulePropsParametersBastionHostName", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_instance_type: typing.Optional[typing.Union["CfnBastionModulePropsParametersBastionInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_tenancy: typing.Optional[typing.Union["CfnBastionModulePropsParametersBastionTenancy", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_banner: typing.Optional[typing.Union["CfnBastionModulePropsParametersEnableBanner", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_tcp_forwarding: typing.Optional[typing.Union["CfnBastionModulePropsParametersEnableTcpForwarding", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_x11_forwarding: typing.Optional[typing.Union["CfnBastionModulePropsParametersEnableX11Forwarding", typing.Dict[builtins.str, typing.Any]]] = None,
        environment_variables: typing.Optional[typing.Union["CfnBastionModulePropsParametersEnvironmentVariables", typing.Dict[builtins.str, typing.Any]]] = None,
        key_pair_name: typing.Optional[typing.Union["CfnBastionModulePropsParametersKeyPairName", typing.Dict[builtins.str, typing.Any]]] = None,
        logical_id: typing.Optional[typing.Union["CfnBastionModulePropsParametersLogicalId", typing.Dict[builtins.str, typing.Any]]] = None,
        num_bastion_hosts: typing.Optional[typing.Union["CfnBastionModulePropsParametersNumBastionHosts", typing.Dict[builtins.str, typing.Any]]] = None,
        os_image_override: typing.Optional[typing.Union["CfnBastionModulePropsParametersOsImageOverride", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1_id: typing.Optional[typing.Union["CfnBastionModulePropsParametersPublicSubnet1Id", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2_id: typing.Optional[typing.Union["CfnBastionModulePropsParametersPublicSubnet2Id", typing.Dict[builtins.str, typing.Any]]] = None,
        qss3_bucket_name: typing.Optional[typing.Union["CfnBastionModulePropsParametersQss3BucketName", typing.Dict[builtins.str, typing.Any]]] = None,
        qss3_bucket_region: typing.Optional[typing.Union["CfnBastionModulePropsParametersQss3BucketRegion", typing.Dict[builtins.str, typing.Any]]] = None,
        qss3_key_prefix: typing.Optional[typing.Union["CfnBastionModulePropsParametersQss3KeyPrefix", typing.Dict[builtins.str, typing.Any]]] = None,
        remote_access_cidr: typing.Optional[typing.Union["CfnBastionModulePropsParametersRemoteAccessCidr", typing.Dict[builtins.str, typing.Any]]] = None,
        root_volume_size: typing.Optional[typing.Union["CfnBastionModulePropsParametersRootVolumeSize", typing.Dict[builtins.str, typing.Any]]] = None,
        vpcid: typing.Optional[typing.Union["CfnBastionModulePropsParametersVpcid", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param alternative_initialization_script: An alternative initialization script to run during setup.
        :param bastion_amios: The Linux distribution for the AMI to be used for the bastion instances.
        :param bastion_banner: Banner text to display upon login.
        :param bastion_host_name: The value used for the name tag of the bastion host.
        :param bastion_instance_type: Amazon EC2 instance type for the bastion instances.
        :param bastion_tenancy: VPC tenancy to launch the bastion in. Options: 'dedicated' or 'default'
        :param enable_banner: To include a banner to be displayed when connecting via SSH to the bastion, choose true.
        :param enable_tcp_forwarding: To enable TCP forwarding, choose true.
        :param enable_x11_forwarding: To enable X11 forwarding, choose true.
        :param environment_variables: A comma-separated list of environment variables for use in bootstrapping. Variables must be in the format KEY=VALUE. VALUE cannot contain commas.
        :param key_pair_name: Name of an existing public/private key pair. If you do not have one in this AWS Region, please create it before continuing.
        :param logical_id: Logical Id of the MODULE.
        :param num_bastion_hosts: The number of bastion hosts to create. The maximum number is four.
        :param os_image_override: The Region-specific image to use for the instance.
        :param public_subnet1_id: ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param public_subnet2_id: ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param qss3_bucket_name: S3 bucket name for the Quick Start assets. Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).
        :param qss3_bucket_region: The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. When using your own bucket, you must specify this value.
        :param qss3_key_prefix: S3 key prefix for the Quick Start assets. Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), dots (.) and forward slash (/) and it should end with a forward slash (/).
        :param remote_access_cidr: Allowed CIDR block for external SSH access to the bastions.
        :param root_volume_size: The size in GB for the root EBS volume.
        :param vpcid: ID of the VPC (e.g., vpc-0343606e).

        :schema: CfnBastionModulePropsParameters
        '''
        if isinstance(alternative_initialization_script, dict):
            alternative_initialization_script = CfnBastionModulePropsParametersAlternativeInitializationScript(**alternative_initialization_script)
        if isinstance(bastion_amios, dict):
            bastion_amios = CfnBastionModulePropsParametersBastionAmios(**bastion_amios)
        if isinstance(bastion_banner, dict):
            bastion_banner = CfnBastionModulePropsParametersBastionBanner(**bastion_banner)
        if isinstance(bastion_host_name, dict):
            bastion_host_name = CfnBastionModulePropsParametersBastionHostName(**bastion_host_name)
        if isinstance(bastion_instance_type, dict):
            bastion_instance_type = CfnBastionModulePropsParametersBastionInstanceType(**bastion_instance_type)
        if isinstance(bastion_tenancy, dict):
            bastion_tenancy = CfnBastionModulePropsParametersBastionTenancy(**bastion_tenancy)
        if isinstance(enable_banner, dict):
            enable_banner = CfnBastionModulePropsParametersEnableBanner(**enable_banner)
        if isinstance(enable_tcp_forwarding, dict):
            enable_tcp_forwarding = CfnBastionModulePropsParametersEnableTcpForwarding(**enable_tcp_forwarding)
        if isinstance(enable_x11_forwarding, dict):
            enable_x11_forwarding = CfnBastionModulePropsParametersEnableX11Forwarding(**enable_x11_forwarding)
        if isinstance(environment_variables, dict):
            environment_variables = CfnBastionModulePropsParametersEnvironmentVariables(**environment_variables)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnBastionModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnBastionModulePropsParametersLogicalId(**logical_id)
        if isinstance(num_bastion_hosts, dict):
            num_bastion_hosts = CfnBastionModulePropsParametersNumBastionHosts(**num_bastion_hosts)
        if isinstance(os_image_override, dict):
            os_image_override = CfnBastionModulePropsParametersOsImageOverride(**os_image_override)
        if isinstance(public_subnet1_id, dict):
            public_subnet1_id = CfnBastionModulePropsParametersPublicSubnet1Id(**public_subnet1_id)
        if isinstance(public_subnet2_id, dict):
            public_subnet2_id = CfnBastionModulePropsParametersPublicSubnet2Id(**public_subnet2_id)
        if isinstance(qss3_bucket_name, dict):
            qss3_bucket_name = CfnBastionModulePropsParametersQss3BucketName(**qss3_bucket_name)
        if isinstance(qss3_bucket_region, dict):
            qss3_bucket_region = CfnBastionModulePropsParametersQss3BucketRegion(**qss3_bucket_region)
        if isinstance(qss3_key_prefix, dict):
            qss3_key_prefix = CfnBastionModulePropsParametersQss3KeyPrefix(**qss3_key_prefix)
        if isinstance(remote_access_cidr, dict):
            remote_access_cidr = CfnBastionModulePropsParametersRemoteAccessCidr(**remote_access_cidr)
        if isinstance(root_volume_size, dict):
            root_volume_size = CfnBastionModulePropsParametersRootVolumeSize(**root_volume_size)
        if isinstance(vpcid, dict):
            vpcid = CfnBastionModulePropsParametersVpcid(**vpcid)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2178de716aa9ff7c3d509330b95a0799a0cf9aa832781a65be8f76dded58cde3)
            check_type(argname="argument alternative_initialization_script", value=alternative_initialization_script, expected_type=type_hints["alternative_initialization_script"])
            check_type(argname="argument bastion_amios", value=bastion_amios, expected_type=type_hints["bastion_amios"])
            check_type(argname="argument bastion_banner", value=bastion_banner, expected_type=type_hints["bastion_banner"])
            check_type(argname="argument bastion_host_name", value=bastion_host_name, expected_type=type_hints["bastion_host_name"])
            check_type(argname="argument bastion_instance_type", value=bastion_instance_type, expected_type=type_hints["bastion_instance_type"])
            check_type(argname="argument bastion_tenancy", value=bastion_tenancy, expected_type=type_hints["bastion_tenancy"])
            check_type(argname="argument enable_banner", value=enable_banner, expected_type=type_hints["enable_banner"])
            check_type(argname="argument enable_tcp_forwarding", value=enable_tcp_forwarding, expected_type=type_hints["enable_tcp_forwarding"])
            check_type(argname="argument enable_x11_forwarding", value=enable_x11_forwarding, expected_type=type_hints["enable_x11_forwarding"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument key_pair_name", value=key_pair_name, expected_type=type_hints["key_pair_name"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument num_bastion_hosts", value=num_bastion_hosts, expected_type=type_hints["num_bastion_hosts"])
            check_type(argname="argument os_image_override", value=os_image_override, expected_type=type_hints["os_image_override"])
            check_type(argname="argument public_subnet1_id", value=public_subnet1_id, expected_type=type_hints["public_subnet1_id"])
            check_type(argname="argument public_subnet2_id", value=public_subnet2_id, expected_type=type_hints["public_subnet2_id"])
            check_type(argname="argument qss3_bucket_name", value=qss3_bucket_name, expected_type=type_hints["qss3_bucket_name"])
            check_type(argname="argument qss3_bucket_region", value=qss3_bucket_region, expected_type=type_hints["qss3_bucket_region"])
            check_type(argname="argument qss3_key_prefix", value=qss3_key_prefix, expected_type=type_hints["qss3_key_prefix"])
            check_type(argname="argument remote_access_cidr", value=remote_access_cidr, expected_type=type_hints["remote_access_cidr"])
            check_type(argname="argument root_volume_size", value=root_volume_size, expected_type=type_hints["root_volume_size"])
            check_type(argname="argument vpcid", value=vpcid, expected_type=type_hints["vpcid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alternative_initialization_script is not None:
            self._values["alternative_initialization_script"] = alternative_initialization_script
        if bastion_amios is not None:
            self._values["bastion_amios"] = bastion_amios
        if bastion_banner is not None:
            self._values["bastion_banner"] = bastion_banner
        if bastion_host_name is not None:
            self._values["bastion_host_name"] = bastion_host_name
        if bastion_instance_type is not None:
            self._values["bastion_instance_type"] = bastion_instance_type
        if bastion_tenancy is not None:
            self._values["bastion_tenancy"] = bastion_tenancy
        if enable_banner is not None:
            self._values["enable_banner"] = enable_banner
        if enable_tcp_forwarding is not None:
            self._values["enable_tcp_forwarding"] = enable_tcp_forwarding
        if enable_x11_forwarding is not None:
            self._values["enable_x11_forwarding"] = enable_x11_forwarding
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if logical_id is not None:
            self._values["logical_id"] = logical_id
        if num_bastion_hosts is not None:
            self._values["num_bastion_hosts"] = num_bastion_hosts
        if os_image_override is not None:
            self._values["os_image_override"] = os_image_override
        if public_subnet1_id is not None:
            self._values["public_subnet1_id"] = public_subnet1_id
        if public_subnet2_id is not None:
            self._values["public_subnet2_id"] = public_subnet2_id
        if qss3_bucket_name is not None:
            self._values["qss3_bucket_name"] = qss3_bucket_name
        if qss3_bucket_region is not None:
            self._values["qss3_bucket_region"] = qss3_bucket_region
        if qss3_key_prefix is not None:
            self._values["qss3_key_prefix"] = qss3_key_prefix
        if remote_access_cidr is not None:
            self._values["remote_access_cidr"] = remote_access_cidr
        if root_volume_size is not None:
            self._values["root_volume_size"] = root_volume_size
        if vpcid is not None:
            self._values["vpcid"] = vpcid

    @builtins.property
    def alternative_initialization_script(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersAlternativeInitializationScript"]:
        '''An alternative initialization script to run during setup.

        :schema: CfnBastionModulePropsParameters#AlternativeInitializationScript
        '''
        result = self._values.get("alternative_initialization_script")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersAlternativeInitializationScript"], result)

    @builtins.property
    def bastion_amios(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersBastionAmios"]:
        '''The Linux distribution for the AMI to be used for the bastion instances.

        :schema: CfnBastionModulePropsParameters#BastionAMIOS
        '''
        result = self._values.get("bastion_amios")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersBastionAmios"], result)

    @builtins.property
    def bastion_banner(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersBastionBanner"]:
        '''Banner text to display upon login.

        :schema: CfnBastionModulePropsParameters#BastionBanner
        '''
        result = self._values.get("bastion_banner")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersBastionBanner"], result)

    @builtins.property
    def bastion_host_name(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersBastionHostName"]:
        '''The value used for the name tag of the bastion host.

        :schema: CfnBastionModulePropsParameters#BastionHostName
        '''
        result = self._values.get("bastion_host_name")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersBastionHostName"], result)

    @builtins.property
    def bastion_instance_type(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersBastionInstanceType"]:
        '''Amazon EC2 instance type for the bastion instances.

        :schema: CfnBastionModulePropsParameters#BastionInstanceType
        '''
        result = self._values.get("bastion_instance_type")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersBastionInstanceType"], result)

    @builtins.property
    def bastion_tenancy(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersBastionTenancy"]:
        '''VPC tenancy to launch the bastion in.

        Options: 'dedicated' or 'default'

        :schema: CfnBastionModulePropsParameters#BastionTenancy
        '''
        result = self._values.get("bastion_tenancy")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersBastionTenancy"], result)

    @builtins.property
    def enable_banner(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersEnableBanner"]:
        '''To include a banner to be displayed when connecting via SSH to the bastion, choose true.

        :schema: CfnBastionModulePropsParameters#EnableBanner
        '''
        result = self._values.get("enable_banner")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersEnableBanner"], result)

    @builtins.property
    def enable_tcp_forwarding(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersEnableTcpForwarding"]:
        '''To enable TCP forwarding, choose true.

        :schema: CfnBastionModulePropsParameters#EnableTCPForwarding
        '''
        result = self._values.get("enable_tcp_forwarding")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersEnableTcpForwarding"], result)

    @builtins.property
    def enable_x11_forwarding(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersEnableX11Forwarding"]:
        '''To enable X11 forwarding, choose true.

        :schema: CfnBastionModulePropsParameters#EnableX11Forwarding
        '''
        result = self._values.get("enable_x11_forwarding")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersEnableX11Forwarding"], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersEnvironmentVariables"]:
        '''A comma-separated list of environment variables for use in bootstrapping.

        Variables must be in the format KEY=VALUE. VALUE cannot contain commas.

        :schema: CfnBastionModulePropsParameters#EnvironmentVariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersEnvironmentVariables"], result)

    @builtins.property
    def key_pair_name(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersKeyPairName"]:
        '''Name of an existing public/private key pair.

        If you do not have one in this AWS Region, please create it before continuing.

        :schema: CfnBastionModulePropsParameters#KeyPairName
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersKeyPairName"], result)

    @builtins.property
    def logical_id(self) -> typing.Optional["CfnBastionModulePropsParametersLogicalId"]:
        '''Logical Id of the MODULE.

        :schema: CfnBastionModulePropsParameters#LogicalId
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersLogicalId"], result)

    @builtins.property
    def num_bastion_hosts(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersNumBastionHosts"]:
        '''The number of bastion hosts to create.

        The maximum number is four.

        :schema: CfnBastionModulePropsParameters#NumBastionHosts
        '''
        result = self._values.get("num_bastion_hosts")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersNumBastionHosts"], result)

    @builtins.property
    def os_image_override(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersOsImageOverride"]:
        '''The Region-specific image to use for the instance.

        :schema: CfnBastionModulePropsParameters#OSImageOverride
        '''
        result = self._values.get("os_image_override")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersOsImageOverride"], result)

    @builtins.property
    def public_subnet1_id(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersPublicSubnet1Id"]:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnBastionModulePropsParameters#PublicSubnet1Id
        '''
        result = self._values.get("public_subnet1_id")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersPublicSubnet1Id"], result)

    @builtins.property
    def public_subnet2_id(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersPublicSubnet2Id"]:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnBastionModulePropsParameters#PublicSubnet2Id
        '''
        result = self._values.get("public_subnet2_id")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersPublicSubnet2Id"], result)

    @builtins.property
    def qss3_bucket_name(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersQss3BucketName"]:
        '''S3 bucket name for the Quick Start assets.

        Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :schema: CfnBastionModulePropsParameters#QSS3BucketName
        '''
        result = self._values.get("qss3_bucket_name")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersQss3BucketName"], result)

    @builtins.property
    def qss3_bucket_region(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersQss3BucketRegion"]:
        '''The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        When using your own bucket, you must specify this value.

        :schema: CfnBastionModulePropsParameters#QSS3BucketRegion
        '''
        result = self._values.get("qss3_bucket_region")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersQss3BucketRegion"], result)

    @builtins.property
    def qss3_key_prefix(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersQss3KeyPrefix"]:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), dots (.) and forward slash (/) and it should end with a forward slash (/).

        :schema: CfnBastionModulePropsParameters#QSS3KeyPrefix
        '''
        result = self._values.get("qss3_key_prefix")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersQss3KeyPrefix"], result)

    @builtins.property
    def remote_access_cidr(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersRemoteAccessCidr"]:
        '''Allowed CIDR block for external SSH access to the bastions.

        :schema: CfnBastionModulePropsParameters#RemoteAccessCIDR
        '''
        result = self._values.get("remote_access_cidr")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersRemoteAccessCidr"], result)

    @builtins.property
    def root_volume_size(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersRootVolumeSize"]:
        '''The size in GB for the root EBS volume.

        :schema: CfnBastionModulePropsParameters#RootVolumeSize
        '''
        result = self._values.get("root_volume_size")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersRootVolumeSize"], result)

    @builtins.property
    def vpcid(self) -> typing.Optional["CfnBastionModulePropsParametersVpcid"]:
        '''ID of the VPC (e.g., vpc-0343606e).

        :schema: CfnBastionModulePropsParameters#VPCID
        '''
        result = self._values.get("vpcid")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersVpcid"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersAlternativeInitializationScript",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersAlternativeInitializationScript:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''An alternative initialization script to run during setup.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersAlternativeInitializationScript
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8825edd46b8411303b47381886b95e8c347ac030606891bb03df0d0de267a92d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersAlternativeInitializationScript#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersAlternativeInitializationScript#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersAlternativeInitializationScript(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersBastionAmios",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersBastionAmios:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Linux distribution for the AMI to be used for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersBastionAmios
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__160d7bdefbb97d59862fc7ab70428e17beb524096143a867a038bd48e7a4ab9e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionAmios#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionAmios#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersBastionAmios(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersBastionBanner",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersBastionBanner:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Banner text to display upon login.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersBastionBanner
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae19deec2302d9031f581ef80b6c6636be232835d0f42b088f54d65426dc7804)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionBanner#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionBanner#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersBastionBanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersBastionHostName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersBastionHostName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The value used for the name tag of the bastion host.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersBastionHostName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c75449b54c609446ef3053487f8b881b87644bbae3ed7558e4ddd162524beb8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionHostName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionHostName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersBastionHostName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersBastionInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersBastionInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon EC2 instance type for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersBastionInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3eb6f80d46170436f105cb0e17fb1ceca0432c2677ba5593a017421c38b15f4)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersBastionInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersBastionTenancy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersBastionTenancy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''VPC tenancy to launch the bastion in.

        Options: 'dedicated' or 'default'

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersBastionTenancy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e72a633bfebd52ecdbc9680977d9c32daca7ef16f29065354645c32d41dfec5)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionTenancy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersBastionTenancy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersBastionTenancy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersEnableBanner",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersEnableBanner:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To include a banner to be displayed when connecting via SSH to the bastion, choose true.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersEnableBanner
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae7891be01a20de468cbf407d2791645d44978ed0da6e2843c7c5a8498df5421)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnableBanner#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnableBanner#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersEnableBanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersEnableTcpForwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersEnableTcpForwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To enable TCP forwarding, choose true.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersEnableTcpForwarding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__613905ce5372c20baa11750df2790057cf5c4ea1e059b958f68eca6dd0712e57)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnableTcpForwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnableTcpForwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersEnableTcpForwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersEnableX11Forwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersEnableX11Forwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To enable X11 forwarding, choose true.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersEnableX11Forwarding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87236a6d7a84c24e0ad5cbed16392daa39e5754ef51f4fd66173e52500ac1a8c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnableX11Forwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnableX11Forwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersEnableX11Forwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersEnvironmentVariables",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersEnvironmentVariables:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A comma-separated list of environment variables for use in bootstrapping.

        Variables must be in the format KEY=VALUE. VALUE cannot contain commas.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersEnvironmentVariables
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a3cd41ddc625a2e303959ca00d02aed826a03c5867df1d7b6cc9b453d6e2a63)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnvironmentVariables#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersEnvironmentVariables#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersEnvironmentVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersKeyPairName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of an existing public/private key pair.

        If you do not have one in this AWS Region, please create it before continuing.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersKeyPairName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5f251f17608fbe668194d3549e329a839cacd8a49110e076534ae82190a65c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersKeyPairName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersKeyPairName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersKeyPairName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersLogicalId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersLogicalId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logical Id of the MODULE.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersLogicalId
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdde1d696eaa751afe4aa092b07d30181ecbfc73384e3ae42ab1457b6a335d98)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersLogicalId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersLogicalId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersLogicalId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersNumBastionHosts",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersNumBastionHosts:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The number of bastion hosts to create.

        The maximum number is four.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersNumBastionHosts
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5de978bf10b892ff296bd53a4fca0a1155c224cd8e9f34ede4109861e2f045ed)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersNumBastionHosts#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersNumBastionHosts#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersNumBastionHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersOsImageOverride",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersOsImageOverride:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Region-specific image to use for the instance.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersOsImageOverride
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b24d1eeb6ca8049db7f9468a15e067488a9d7bb049c3c058a5f1e11d4e4302)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersOsImageOverride#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersOsImageOverride#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersOsImageOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersPublicSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersPublicSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersPublicSubnet1Id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecaad410b3779f120ffd42e4862890b1f91dedd807424239e5808403a079c06f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersPublicSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersPublicSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersPublicSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersPublicSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersPublicSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersPublicSubnet2Id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeb5798fa9167777d847154eb8131d8fc549af58f272843dfddea4e9add70954)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersPublicSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersPublicSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersPublicSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersQss3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersQss3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 bucket name for the Quick Start assets.

        Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersQss3BucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__420cf33afa339afe94bc94b9c65c6ed22ee70e96192b3a378146727186a97b07)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersQss3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersQss3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersQss3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersQss3BucketRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersQss3BucketRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        When using your own bucket, you must specify this value.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersQss3BucketRegion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df232e8b7da09663ade277cf9a000e42c8ba5dcd43b24c725d58c126930d13a6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersQss3BucketRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersQss3BucketRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersQss3BucketRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersQss3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersQss3KeyPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), dots (.) and forward slash (/) and it should end with a forward slash (/).

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersQss3KeyPrefix
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104e5172398c46355c8bbd0660500cc21c8e63515b336bf50c74e1c3f3352212)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersQss3KeyPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersQss3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersQss3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersRemoteAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersRemoteAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allowed CIDR block for external SSH access to the bastions.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersRemoteAccessCidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab088750be2644fceaa00860086d8d20ced8712945d85d5cade0ce69c19c4942)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersRemoteAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersRemoteAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersRemoteAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersRootVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersRootVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The size in GB for the root EBS volume.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersRootVolumeSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1883951dcfba08e5411d3cba67a96171e340395aa8379aacfa00522ff469959b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersRootVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersRootVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersRootVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsParametersVpcid",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersVpcid:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the VPC (e.g., vpc-0343606e).

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersVpcid
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e9995f33569d5076d2f71ce470205513255b3fff5ea213e8445188a3b9a9056)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcid#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcid#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersVpcid(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "bastion_auto_scaling_group": "bastionAutoScalingGroup",
        "bastion_host_policy": "bastionHostPolicy",
        "bastion_host_profile": "bastionHostProfile",
        "bastion_host_role": "bastionHostRole",
        "bastion_launch_configuration": "bastionLaunchConfiguration",
        "bastion_main_log_group": "bastionMainLogGroup",
        "bastion_security_group": "bastionSecurityGroup",
        "eip1": "eip1",
        "eip2": "eip2",
        "eip3": "eip3",
        "eip4": "eip4",
        "ssh_metric_filter": "sshMetricFilter",
    },
)
class CfnBastionModulePropsResources:
    def __init__(
        self,
        *,
        bastion_auto_scaling_group: typing.Optional[typing.Union["CfnBastionModulePropsResourcesBastionAutoScalingGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_policy: typing.Optional[typing.Union["CfnBastionModulePropsResourcesBastionHostPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_profile: typing.Optional[typing.Union["CfnBastionModulePropsResourcesBastionHostProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_role: typing.Optional[typing.Union["CfnBastionModulePropsResourcesBastionHostRole", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_launch_configuration: typing.Optional[typing.Union["CfnBastionModulePropsResourcesBastionLaunchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_main_log_group: typing.Optional[typing.Union["CfnBastionModulePropsResourcesBastionMainLogGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_security_group: typing.Optional[typing.Union["CfnBastionModulePropsResourcesBastionSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        eip1: typing.Optional[typing.Union["CfnBastionModulePropsResourcesEip1", typing.Dict[builtins.str, typing.Any]]] = None,
        eip2: typing.Optional[typing.Union["CfnBastionModulePropsResourcesEip2", typing.Dict[builtins.str, typing.Any]]] = None,
        eip3: typing.Optional[typing.Union["CfnBastionModulePropsResourcesEip3", typing.Dict[builtins.str, typing.Any]]] = None,
        eip4: typing.Optional[typing.Union["CfnBastionModulePropsResourcesEip4", typing.Dict[builtins.str, typing.Any]]] = None,
        ssh_metric_filter: typing.Optional[typing.Union["CfnBastionModulePropsResourcesSshMetricFilter", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bastion_auto_scaling_group: 
        :param bastion_host_policy: 
        :param bastion_host_profile: 
        :param bastion_host_role: 
        :param bastion_launch_configuration: 
        :param bastion_main_log_group: 
        :param bastion_security_group: 
        :param eip1: 
        :param eip2: 
        :param eip3: 
        :param eip4: 
        :param ssh_metric_filter: 

        :schema: CfnBastionModulePropsResources
        '''
        if isinstance(bastion_auto_scaling_group, dict):
            bastion_auto_scaling_group = CfnBastionModulePropsResourcesBastionAutoScalingGroup(**bastion_auto_scaling_group)
        if isinstance(bastion_host_policy, dict):
            bastion_host_policy = CfnBastionModulePropsResourcesBastionHostPolicy(**bastion_host_policy)
        if isinstance(bastion_host_profile, dict):
            bastion_host_profile = CfnBastionModulePropsResourcesBastionHostProfile(**bastion_host_profile)
        if isinstance(bastion_host_role, dict):
            bastion_host_role = CfnBastionModulePropsResourcesBastionHostRole(**bastion_host_role)
        if isinstance(bastion_launch_configuration, dict):
            bastion_launch_configuration = CfnBastionModulePropsResourcesBastionLaunchConfiguration(**bastion_launch_configuration)
        if isinstance(bastion_main_log_group, dict):
            bastion_main_log_group = CfnBastionModulePropsResourcesBastionMainLogGroup(**bastion_main_log_group)
        if isinstance(bastion_security_group, dict):
            bastion_security_group = CfnBastionModulePropsResourcesBastionSecurityGroup(**bastion_security_group)
        if isinstance(eip1, dict):
            eip1 = CfnBastionModulePropsResourcesEip1(**eip1)
        if isinstance(eip2, dict):
            eip2 = CfnBastionModulePropsResourcesEip2(**eip2)
        if isinstance(eip3, dict):
            eip3 = CfnBastionModulePropsResourcesEip3(**eip3)
        if isinstance(eip4, dict):
            eip4 = CfnBastionModulePropsResourcesEip4(**eip4)
        if isinstance(ssh_metric_filter, dict):
            ssh_metric_filter = CfnBastionModulePropsResourcesSshMetricFilter(**ssh_metric_filter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071730c2dda59c3dc05e7febee9071f99e90f541d837a03bfd0cad1ca09b150b)
            check_type(argname="argument bastion_auto_scaling_group", value=bastion_auto_scaling_group, expected_type=type_hints["bastion_auto_scaling_group"])
            check_type(argname="argument bastion_host_policy", value=bastion_host_policy, expected_type=type_hints["bastion_host_policy"])
            check_type(argname="argument bastion_host_profile", value=bastion_host_profile, expected_type=type_hints["bastion_host_profile"])
            check_type(argname="argument bastion_host_role", value=bastion_host_role, expected_type=type_hints["bastion_host_role"])
            check_type(argname="argument bastion_launch_configuration", value=bastion_launch_configuration, expected_type=type_hints["bastion_launch_configuration"])
            check_type(argname="argument bastion_main_log_group", value=bastion_main_log_group, expected_type=type_hints["bastion_main_log_group"])
            check_type(argname="argument bastion_security_group", value=bastion_security_group, expected_type=type_hints["bastion_security_group"])
            check_type(argname="argument eip1", value=eip1, expected_type=type_hints["eip1"])
            check_type(argname="argument eip2", value=eip2, expected_type=type_hints["eip2"])
            check_type(argname="argument eip3", value=eip3, expected_type=type_hints["eip3"])
            check_type(argname="argument eip4", value=eip4, expected_type=type_hints["eip4"])
            check_type(argname="argument ssh_metric_filter", value=ssh_metric_filter, expected_type=type_hints["ssh_metric_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bastion_auto_scaling_group is not None:
            self._values["bastion_auto_scaling_group"] = bastion_auto_scaling_group
        if bastion_host_policy is not None:
            self._values["bastion_host_policy"] = bastion_host_policy
        if bastion_host_profile is not None:
            self._values["bastion_host_profile"] = bastion_host_profile
        if bastion_host_role is not None:
            self._values["bastion_host_role"] = bastion_host_role
        if bastion_launch_configuration is not None:
            self._values["bastion_launch_configuration"] = bastion_launch_configuration
        if bastion_main_log_group is not None:
            self._values["bastion_main_log_group"] = bastion_main_log_group
        if bastion_security_group is not None:
            self._values["bastion_security_group"] = bastion_security_group
        if eip1 is not None:
            self._values["eip1"] = eip1
        if eip2 is not None:
            self._values["eip2"] = eip2
        if eip3 is not None:
            self._values["eip3"] = eip3
        if eip4 is not None:
            self._values["eip4"] = eip4
        if ssh_metric_filter is not None:
            self._values["ssh_metric_filter"] = ssh_metric_filter

    @builtins.property
    def bastion_auto_scaling_group(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesBastionAutoScalingGroup"]:
        '''
        :schema: CfnBastionModulePropsResources#BastionAutoScalingGroup
        '''
        result = self._values.get("bastion_auto_scaling_group")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesBastionAutoScalingGroup"], result)

    @builtins.property
    def bastion_host_policy(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesBastionHostPolicy"]:
        '''
        :schema: CfnBastionModulePropsResources#BastionHostPolicy
        '''
        result = self._values.get("bastion_host_policy")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesBastionHostPolicy"], result)

    @builtins.property
    def bastion_host_profile(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesBastionHostProfile"]:
        '''
        :schema: CfnBastionModulePropsResources#BastionHostProfile
        '''
        result = self._values.get("bastion_host_profile")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesBastionHostProfile"], result)

    @builtins.property
    def bastion_host_role(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesBastionHostRole"]:
        '''
        :schema: CfnBastionModulePropsResources#BastionHostRole
        '''
        result = self._values.get("bastion_host_role")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesBastionHostRole"], result)

    @builtins.property
    def bastion_launch_configuration(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesBastionLaunchConfiguration"]:
        '''
        :schema: CfnBastionModulePropsResources#BastionLaunchConfiguration
        '''
        result = self._values.get("bastion_launch_configuration")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesBastionLaunchConfiguration"], result)

    @builtins.property
    def bastion_main_log_group(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesBastionMainLogGroup"]:
        '''
        :schema: CfnBastionModulePropsResources#BastionMainLogGroup
        '''
        result = self._values.get("bastion_main_log_group")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesBastionMainLogGroup"], result)

    @builtins.property
    def bastion_security_group(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesBastionSecurityGroup"]:
        '''
        :schema: CfnBastionModulePropsResources#BastionSecurityGroup
        '''
        result = self._values.get("bastion_security_group")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesBastionSecurityGroup"], result)

    @builtins.property
    def eip1(self) -> typing.Optional["CfnBastionModulePropsResourcesEip1"]:
        '''
        :schema: CfnBastionModulePropsResources#EIP1
        '''
        result = self._values.get("eip1")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesEip1"], result)

    @builtins.property
    def eip2(self) -> typing.Optional["CfnBastionModulePropsResourcesEip2"]:
        '''
        :schema: CfnBastionModulePropsResources#EIP2
        '''
        result = self._values.get("eip2")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesEip2"], result)

    @builtins.property
    def eip3(self) -> typing.Optional["CfnBastionModulePropsResourcesEip3"]:
        '''
        :schema: CfnBastionModulePropsResources#EIP3
        '''
        result = self._values.get("eip3")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesEip3"], result)

    @builtins.property
    def eip4(self) -> typing.Optional["CfnBastionModulePropsResourcesEip4"]:
        '''
        :schema: CfnBastionModulePropsResources#EIP4
        '''
        result = self._values.get("eip4")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesEip4"], result)

    @builtins.property
    def ssh_metric_filter(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesSshMetricFilter"]:
        '''
        :schema: CfnBastionModulePropsResources#SSHMetricFilter
        '''
        result = self._values.get("ssh_metric_filter")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesSshMetricFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesBastionAutoScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesBastionAutoScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesBastionAutoScalingGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e27b8bd4ba160bc68f6000a156ee07b816d93515fdb6d4fe524e61b0de7fea4a)
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
        :schema: CfnBastionModulePropsResourcesBastionAutoScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesBastionAutoScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesBastionAutoScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesBastionHostPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesBastionHostPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesBastionHostPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e4556b2b00c84a62fdd81b701462d2d6485f7b36fbaf4bbb6544c81975e1bc)
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
        :schema: CfnBastionModulePropsResourcesBastionHostPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesBastionHostPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesBastionHostPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesBastionHostProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesBastionHostProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesBastionHostProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b18397c361212bf8c401f72f22b41bf51d5ff83cac395d3806d14235770e17)
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
        :schema: CfnBastionModulePropsResourcesBastionHostProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesBastionHostProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesBastionHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesBastionHostRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesBastionHostRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesBastionHostRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e3805c3ee8e64cdea3d8f8412472c34eef1cde2ccd34f2c03a721726ecf7d6)
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
        :schema: CfnBastionModulePropsResourcesBastionHostRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesBastionHostRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesBastionHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesBastionLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesBastionLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesBastionLaunchConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753a2394cca83eaa1c4d62c1f75b40fa657389dbb22c9c65c4a519b9dfedca5b)
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
        :schema: CfnBastionModulePropsResourcesBastionLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesBastionLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesBastionLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesBastionMainLogGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesBastionMainLogGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesBastionMainLogGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092e5db24cf95a24a9b0ed36d15e621e7646653b9bb1331f820ea13867df7634)
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
        :schema: CfnBastionModulePropsResourcesBastionMainLogGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesBastionMainLogGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesBastionMainLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesBastionSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesBastionSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesBastionSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d729a0d20b990c9c1e84d9fb5917e22ac19df8bd1942e7d7f5799c72a80992)
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
        :schema: CfnBastionModulePropsResourcesBastionSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesBastionSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesBastionSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesEip1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesEip1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesEip1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7160e003cea121a9910d799e599d0efd594b4449d24913e778bc56b5bb2ee9be)
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
        :schema: CfnBastionModulePropsResourcesEip1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesEip1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesEip1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesEip2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesEip2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesEip2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01fc0456c52053b569bc717b0e9d7b9084cf24688a052b2c5bdec863f421146f)
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
        :schema: CfnBastionModulePropsResourcesEip2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesEip2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesEip2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesEip3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesEip3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesEip3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e95fdfa336d705a970472403af91a526d7387772bb610b9abcc2a55768b2233)
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
        :schema: CfnBastionModulePropsResourcesEip3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesEip3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesEip3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesEip4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesEip4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesEip4
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4688dc1151970b0a9f20407ec11e80ee8d7c958fd67c5436889033a50cec41c)
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
        :schema: CfnBastionModulePropsResourcesEip4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesEip4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesEip4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnBastionModulePropsResourcesSshMetricFilter",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesSshMetricFilter:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesSshMetricFilter
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e08e8cea74a2e59ae405cc3c56a41b590216208d785bf16b06a26281aeaf6393)
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
        :schema: CfnBastionModulePropsResourcesSshMetricFilter#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesSshMetricFilter#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesSshMetricFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBastionModule",
    "CfnBastionModuleProps",
    "CfnBastionModulePropsParameters",
    "CfnBastionModulePropsParametersAlternativeInitializationScript",
    "CfnBastionModulePropsParametersBastionAmios",
    "CfnBastionModulePropsParametersBastionBanner",
    "CfnBastionModulePropsParametersBastionHostName",
    "CfnBastionModulePropsParametersBastionInstanceType",
    "CfnBastionModulePropsParametersBastionTenancy",
    "CfnBastionModulePropsParametersEnableBanner",
    "CfnBastionModulePropsParametersEnableTcpForwarding",
    "CfnBastionModulePropsParametersEnableX11Forwarding",
    "CfnBastionModulePropsParametersEnvironmentVariables",
    "CfnBastionModulePropsParametersKeyPairName",
    "CfnBastionModulePropsParametersLogicalId",
    "CfnBastionModulePropsParametersNumBastionHosts",
    "CfnBastionModulePropsParametersOsImageOverride",
    "CfnBastionModulePropsParametersPublicSubnet1Id",
    "CfnBastionModulePropsParametersPublicSubnet2Id",
    "CfnBastionModulePropsParametersQss3BucketName",
    "CfnBastionModulePropsParametersQss3BucketRegion",
    "CfnBastionModulePropsParametersQss3KeyPrefix",
    "CfnBastionModulePropsParametersRemoteAccessCidr",
    "CfnBastionModulePropsParametersRootVolumeSize",
    "CfnBastionModulePropsParametersVpcid",
    "CfnBastionModulePropsResources",
    "CfnBastionModulePropsResourcesBastionAutoScalingGroup",
    "CfnBastionModulePropsResourcesBastionHostPolicy",
    "CfnBastionModulePropsResourcesBastionHostProfile",
    "CfnBastionModulePropsResourcesBastionHostRole",
    "CfnBastionModulePropsResourcesBastionLaunchConfiguration",
    "CfnBastionModulePropsResourcesBastionMainLogGroup",
    "CfnBastionModulePropsResourcesBastionSecurityGroup",
    "CfnBastionModulePropsResourcesEip1",
    "CfnBastionModulePropsResourcesEip2",
    "CfnBastionModulePropsResourcesEip3",
    "CfnBastionModulePropsResourcesEip4",
    "CfnBastionModulePropsResourcesSshMetricFilter",
]

publication.publish()

def _typecheckingstub__3c7ea32ed00c47eab16c3cc9bc4e9867577fd53e6d68977d1696551378fe2fd5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnBastionModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnBastionModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73460fb68f726f53b663e0d59321a2150f678863ec32df8bdb00f829e0a200b(
    *,
    parameters: typing.Optional[typing.Union[CfnBastionModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnBastionModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2178de716aa9ff7c3d509330b95a0799a0cf9aa832781a65be8f76dded58cde3(
    *,
    alternative_initialization_script: typing.Optional[typing.Union[CfnBastionModulePropsParametersAlternativeInitializationScript, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_amios: typing.Optional[typing.Union[CfnBastionModulePropsParametersBastionAmios, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_banner: typing.Optional[typing.Union[CfnBastionModulePropsParametersBastionBanner, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_name: typing.Optional[typing.Union[CfnBastionModulePropsParametersBastionHostName, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_instance_type: typing.Optional[typing.Union[CfnBastionModulePropsParametersBastionInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_tenancy: typing.Optional[typing.Union[CfnBastionModulePropsParametersBastionTenancy, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_banner: typing.Optional[typing.Union[CfnBastionModulePropsParametersEnableBanner, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_tcp_forwarding: typing.Optional[typing.Union[CfnBastionModulePropsParametersEnableTcpForwarding, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_x11_forwarding: typing.Optional[typing.Union[CfnBastionModulePropsParametersEnableX11Forwarding, typing.Dict[builtins.str, typing.Any]]] = None,
    environment_variables: typing.Optional[typing.Union[CfnBastionModulePropsParametersEnvironmentVariables, typing.Dict[builtins.str, typing.Any]]] = None,
    key_pair_name: typing.Optional[typing.Union[CfnBastionModulePropsParametersKeyPairName, typing.Dict[builtins.str, typing.Any]]] = None,
    logical_id: typing.Optional[typing.Union[CfnBastionModulePropsParametersLogicalId, typing.Dict[builtins.str, typing.Any]]] = None,
    num_bastion_hosts: typing.Optional[typing.Union[CfnBastionModulePropsParametersNumBastionHosts, typing.Dict[builtins.str, typing.Any]]] = None,
    os_image_override: typing.Optional[typing.Union[CfnBastionModulePropsParametersOsImageOverride, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1_id: typing.Optional[typing.Union[CfnBastionModulePropsParametersPublicSubnet1Id, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2_id: typing.Optional[typing.Union[CfnBastionModulePropsParametersPublicSubnet2Id, typing.Dict[builtins.str, typing.Any]]] = None,
    qss3_bucket_name: typing.Optional[typing.Union[CfnBastionModulePropsParametersQss3BucketName, typing.Dict[builtins.str, typing.Any]]] = None,
    qss3_bucket_region: typing.Optional[typing.Union[CfnBastionModulePropsParametersQss3BucketRegion, typing.Dict[builtins.str, typing.Any]]] = None,
    qss3_key_prefix: typing.Optional[typing.Union[CfnBastionModulePropsParametersQss3KeyPrefix, typing.Dict[builtins.str, typing.Any]]] = None,
    remote_access_cidr: typing.Optional[typing.Union[CfnBastionModulePropsParametersRemoteAccessCidr, typing.Dict[builtins.str, typing.Any]]] = None,
    root_volume_size: typing.Optional[typing.Union[CfnBastionModulePropsParametersRootVolumeSize, typing.Dict[builtins.str, typing.Any]]] = None,
    vpcid: typing.Optional[typing.Union[CfnBastionModulePropsParametersVpcid, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8825edd46b8411303b47381886b95e8c347ac030606891bb03df0d0de267a92d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__160d7bdefbb97d59862fc7ab70428e17beb524096143a867a038bd48e7a4ab9e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae19deec2302d9031f581ef80b6c6636be232835d0f42b088f54d65426dc7804(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c75449b54c609446ef3053487f8b881b87644bbae3ed7558e4ddd162524beb8(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3eb6f80d46170436f105cb0e17fb1ceca0432c2677ba5593a017421c38b15f4(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e72a633bfebd52ecdbc9680977d9c32daca7ef16f29065354645c32d41dfec5(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7891be01a20de468cbf407d2791645d44978ed0da6e2843c7c5a8498df5421(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__613905ce5372c20baa11750df2790057cf5c4ea1e059b958f68eca6dd0712e57(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87236a6d7a84c24e0ad5cbed16392daa39e5754ef51f4fd66173e52500ac1a8c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3cd41ddc625a2e303959ca00d02aed826a03c5867df1d7b6cc9b453d6e2a63(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5f251f17608fbe668194d3549e329a839cacd8a49110e076534ae82190a65c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdde1d696eaa751afe4aa092b07d30181ecbfc73384e3ae42ab1457b6a335d98(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de978bf10b892ff296bd53a4fca0a1155c224cd8e9f34ede4109861e2f045ed(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b24d1eeb6ca8049db7f9468a15e067488a9d7bb049c3c058a5f1e11d4e4302(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecaad410b3779f120ffd42e4862890b1f91dedd807424239e5808403a079c06f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb5798fa9167777d847154eb8131d8fc549af58f272843dfddea4e9add70954(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420cf33afa339afe94bc94b9c65c6ed22ee70e96192b3a378146727186a97b07(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df232e8b7da09663ade277cf9a000e42c8ba5dcd43b24c725d58c126930d13a6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104e5172398c46355c8bbd0660500cc21c8e63515b336bf50c74e1c3f3352212(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab088750be2644fceaa00860086d8d20ced8712945d85d5cade0ce69c19c4942(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1883951dcfba08e5411d3cba67a96171e340395aa8379aacfa00522ff469959b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e9995f33569d5076d2f71ce470205513255b3fff5ea213e8445188a3b9a9056(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071730c2dda59c3dc05e7febee9071f99e90f541d837a03bfd0cad1ca09b150b(
    *,
    bastion_auto_scaling_group: typing.Optional[typing.Union[CfnBastionModulePropsResourcesBastionAutoScalingGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_policy: typing.Optional[typing.Union[CfnBastionModulePropsResourcesBastionHostPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_profile: typing.Optional[typing.Union[CfnBastionModulePropsResourcesBastionHostProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_role: typing.Optional[typing.Union[CfnBastionModulePropsResourcesBastionHostRole, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_launch_configuration: typing.Optional[typing.Union[CfnBastionModulePropsResourcesBastionLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_main_log_group: typing.Optional[typing.Union[CfnBastionModulePropsResourcesBastionMainLogGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_security_group: typing.Optional[typing.Union[CfnBastionModulePropsResourcesBastionSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    eip1: typing.Optional[typing.Union[CfnBastionModulePropsResourcesEip1, typing.Dict[builtins.str, typing.Any]]] = None,
    eip2: typing.Optional[typing.Union[CfnBastionModulePropsResourcesEip2, typing.Dict[builtins.str, typing.Any]]] = None,
    eip3: typing.Optional[typing.Union[CfnBastionModulePropsResourcesEip3, typing.Dict[builtins.str, typing.Any]]] = None,
    eip4: typing.Optional[typing.Union[CfnBastionModulePropsResourcesEip4, typing.Dict[builtins.str, typing.Any]]] = None,
    ssh_metric_filter: typing.Optional[typing.Union[CfnBastionModulePropsResourcesSshMetricFilter, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27b8bd4ba160bc68f6000a156ee07b816d93515fdb6d4fe524e61b0de7fea4a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e4556b2b00c84a62fdd81b701462d2d6485f7b36fbaf4bbb6544c81975e1bc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b18397c361212bf8c401f72f22b41bf51d5ff83cac395d3806d14235770e17(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e3805c3ee8e64cdea3d8f8412472c34eef1cde2ccd34f2c03a721726ecf7d6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753a2394cca83eaa1c4d62c1f75b40fa657389dbb22c9c65c4a519b9dfedca5b(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092e5db24cf95a24a9b0ed36d15e621e7646653b9bb1331f820ea13867df7634(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d729a0d20b990c9c1e84d9fb5917e22ac19df8bd1942e7d7f5799c72a80992(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7160e003cea121a9910d799e599d0efd594b4449d24913e778bc56b5bb2ee9be(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01fc0456c52053b569bc717b0e9d7b9084cf24688a052b2c5bdec863f421146f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e95fdfa336d705a970472403af91a526d7387772bb610b9abcc2a55768b2233(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4688dc1151970b0a9f20407ec11e80ee8d7c958fd67c5436889033a50cec41c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08e8cea74a2e59ae405cc3c56a41b590216208d785bf16b06a26281aeaf6393(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
