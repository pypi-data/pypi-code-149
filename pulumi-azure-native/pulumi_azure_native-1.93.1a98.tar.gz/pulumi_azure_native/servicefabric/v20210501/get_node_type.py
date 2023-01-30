# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetNodeTypeResult',
    'AwaitableGetNodeTypeResult',
    'get_node_type',
    'get_node_type_output',
]

@pulumi.output_type
class GetNodeTypeResult:
    """
    Describes a node type in the cluster, each node type represents sub set of nodes in the cluster.
    """
    def __init__(__self__, application_ports=None, capacities=None, data_disk_size_gb=None, data_disk_type=None, ephemeral_ports=None, id=None, is_primary=None, is_stateless=None, multiple_placement_groups=None, name=None, placement_properties=None, provisioning_state=None, system_data=None, tags=None, type=None, vm_extensions=None, vm_image_offer=None, vm_image_publisher=None, vm_image_sku=None, vm_image_version=None, vm_instance_count=None, vm_managed_identity=None, vm_secrets=None, vm_size=None):
        if application_ports and not isinstance(application_ports, dict):
            raise TypeError("Expected argument 'application_ports' to be a dict")
        pulumi.set(__self__, "application_ports", application_ports)
        if capacities and not isinstance(capacities, dict):
            raise TypeError("Expected argument 'capacities' to be a dict")
        pulumi.set(__self__, "capacities", capacities)
        if data_disk_size_gb and not isinstance(data_disk_size_gb, int):
            raise TypeError("Expected argument 'data_disk_size_gb' to be a int")
        pulumi.set(__self__, "data_disk_size_gb", data_disk_size_gb)
        if data_disk_type and not isinstance(data_disk_type, str):
            raise TypeError("Expected argument 'data_disk_type' to be a str")
        pulumi.set(__self__, "data_disk_type", data_disk_type)
        if ephemeral_ports and not isinstance(ephemeral_ports, dict):
            raise TypeError("Expected argument 'ephemeral_ports' to be a dict")
        pulumi.set(__self__, "ephemeral_ports", ephemeral_ports)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_primary and not isinstance(is_primary, bool):
            raise TypeError("Expected argument 'is_primary' to be a bool")
        pulumi.set(__self__, "is_primary", is_primary)
        if is_stateless and not isinstance(is_stateless, bool):
            raise TypeError("Expected argument 'is_stateless' to be a bool")
        pulumi.set(__self__, "is_stateless", is_stateless)
        if multiple_placement_groups and not isinstance(multiple_placement_groups, bool):
            raise TypeError("Expected argument 'multiple_placement_groups' to be a bool")
        pulumi.set(__self__, "multiple_placement_groups", multiple_placement_groups)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if placement_properties and not isinstance(placement_properties, dict):
            raise TypeError("Expected argument 'placement_properties' to be a dict")
        pulumi.set(__self__, "placement_properties", placement_properties)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_extensions and not isinstance(vm_extensions, list):
            raise TypeError("Expected argument 'vm_extensions' to be a list")
        pulumi.set(__self__, "vm_extensions", vm_extensions)
        if vm_image_offer and not isinstance(vm_image_offer, str):
            raise TypeError("Expected argument 'vm_image_offer' to be a str")
        pulumi.set(__self__, "vm_image_offer", vm_image_offer)
        if vm_image_publisher and not isinstance(vm_image_publisher, str):
            raise TypeError("Expected argument 'vm_image_publisher' to be a str")
        pulumi.set(__self__, "vm_image_publisher", vm_image_publisher)
        if vm_image_sku and not isinstance(vm_image_sku, str):
            raise TypeError("Expected argument 'vm_image_sku' to be a str")
        pulumi.set(__self__, "vm_image_sku", vm_image_sku)
        if vm_image_version and not isinstance(vm_image_version, str):
            raise TypeError("Expected argument 'vm_image_version' to be a str")
        pulumi.set(__self__, "vm_image_version", vm_image_version)
        if vm_instance_count and not isinstance(vm_instance_count, int):
            raise TypeError("Expected argument 'vm_instance_count' to be a int")
        pulumi.set(__self__, "vm_instance_count", vm_instance_count)
        if vm_managed_identity and not isinstance(vm_managed_identity, dict):
            raise TypeError("Expected argument 'vm_managed_identity' to be a dict")
        pulumi.set(__self__, "vm_managed_identity", vm_managed_identity)
        if vm_secrets and not isinstance(vm_secrets, list):
            raise TypeError("Expected argument 'vm_secrets' to be a list")
        pulumi.set(__self__, "vm_secrets", vm_secrets)
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter(name="applicationPorts")
    def application_ports(self) -> Optional['outputs.EndpointRangeDescriptionResponse']:
        """
        The range of ports from which cluster assigned port to Service Fabric applications.
        """
        return pulumi.get(self, "application_ports")

    @property
    @pulumi.getter
    def capacities(self) -> Optional[Mapping[str, str]]:
        """
        The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter(name="dataDiskSizeGB")
    def data_disk_size_gb(self) -> int:
        """
        Disk size for each vm in the node type in GBs.
        """
        return pulumi.get(self, "data_disk_size_gb")

    @property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> Optional[str]:
        """
        Managed data disk type. IOPS and throughput are given by the disk size, to see more information go to https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types.
        """
        return pulumi.get(self, "data_disk_type")

    @property
    @pulumi.getter(name="ephemeralPorts")
    def ephemeral_ports(self) -> Optional['outputs.EndpointRangeDescriptionResponse']:
        """
        The range of ephemeral ports that nodes in this node type should be configured with.
        """
        return pulumi.get(self, "ephemeral_ports")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> bool:
        """
        The node type on which system services will run. Only one node type should be marked as primary. Primary node type cannot be deleted or changed for existing clusters.
        """
        return pulumi.get(self, "is_primary")

    @property
    @pulumi.getter(name="isStateless")
    def is_stateless(self) -> Optional[bool]:
        """
        Indicates if the node type can only host Stateless workloads.
        """
        return pulumi.get(self, "is_stateless")

    @property
    @pulumi.getter(name="multiplePlacementGroups")
    def multiple_placement_groups(self) -> Optional[bool]:
        """
        Indicates if scale set associated with the node type can be composed of multiple placement groups.
        """
        return pulumi.get(self, "multiple_placement_groups")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="placementProperties")
    def placement_properties(self) -> Optional[Mapping[str, str]]:
        """
        The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.
        """
        return pulumi.get(self, "placement_properties")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the managed cluster resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmExtensions")
    def vm_extensions(self) -> Optional[Sequence['outputs.VMSSExtensionResponse']]:
        """
        Set of extensions that should be installed onto the virtual machines.
        """
        return pulumi.get(self, "vm_extensions")

    @property
    @pulumi.getter(name="vmImageOffer")
    def vm_image_offer(self) -> Optional[str]:
        """
        The offer type of the Azure Virtual Machines Marketplace image. For example, UbuntuServer or WindowsServer.
        """
        return pulumi.get(self, "vm_image_offer")

    @property
    @pulumi.getter(name="vmImagePublisher")
    def vm_image_publisher(self) -> Optional[str]:
        """
        The publisher of the Azure Virtual Machines Marketplace image. For example, Canonical or MicrosoftWindowsServer.
        """
        return pulumi.get(self, "vm_image_publisher")

    @property
    @pulumi.getter(name="vmImageSku")
    def vm_image_sku(self) -> Optional[str]:
        """
        The SKU of the Azure Virtual Machines Marketplace image. For example, 14.04.0-LTS or 2012-R2-Datacenter.
        """
        return pulumi.get(self, "vm_image_sku")

    @property
    @pulumi.getter(name="vmImageVersion")
    def vm_image_version(self) -> Optional[str]:
        """
        The version of the Azure Virtual Machines Marketplace image. A value of 'latest' can be specified to select the latest version of an image. If omitted, the default is 'latest'.
        """
        return pulumi.get(self, "vm_image_version")

    @property
    @pulumi.getter(name="vmInstanceCount")
    def vm_instance_count(self) -> int:
        """
        The number of nodes in the node type.
        """
        return pulumi.get(self, "vm_instance_count")

    @property
    @pulumi.getter(name="vmManagedIdentity")
    def vm_managed_identity(self) -> Optional['outputs.VmManagedIdentityResponse']:
        """
        Identities for the virtual machine scale set under the node type.
        """
        return pulumi.get(self, "vm_managed_identity")

    @property
    @pulumi.getter(name="vmSecrets")
    def vm_secrets(self) -> Optional[Sequence['outputs.VaultSecretGroupResponse']]:
        """
        The secrets to install in the virtual machines.
        """
        return pulumi.get(self, "vm_secrets")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        The size of virtual machines in the pool. All virtual machines in a pool are the same size. For example, Standard_D3.
        """
        return pulumi.get(self, "vm_size")


class AwaitableGetNodeTypeResult(GetNodeTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNodeTypeResult(
            application_ports=self.application_ports,
            capacities=self.capacities,
            data_disk_size_gb=self.data_disk_size_gb,
            data_disk_type=self.data_disk_type,
            ephemeral_ports=self.ephemeral_ports,
            id=self.id,
            is_primary=self.is_primary,
            is_stateless=self.is_stateless,
            multiple_placement_groups=self.multiple_placement_groups,
            name=self.name,
            placement_properties=self.placement_properties,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_extensions=self.vm_extensions,
            vm_image_offer=self.vm_image_offer,
            vm_image_publisher=self.vm_image_publisher,
            vm_image_sku=self.vm_image_sku,
            vm_image_version=self.vm_image_version,
            vm_instance_count=self.vm_instance_count,
            vm_managed_identity=self.vm_managed_identity,
            vm_secrets=self.vm_secrets,
            vm_size=self.vm_size)


def get_node_type(cluster_name: Optional[str] = None,
                  node_type_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNodeTypeResult:
    """
    Describes a node type in the cluster, each node type represents sub set of nodes in the cluster.


    :param str cluster_name: The name of the cluster resource.
    :param str node_type_name: The name of the node type.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['nodeTypeName'] = node_type_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20210501:getNodeType', __args__, opts=opts, typ=GetNodeTypeResult).value

    return AwaitableGetNodeTypeResult(
        application_ports=__ret__.application_ports,
        capacities=__ret__.capacities,
        data_disk_size_gb=__ret__.data_disk_size_gb,
        data_disk_type=__ret__.data_disk_type,
        ephemeral_ports=__ret__.ephemeral_ports,
        id=__ret__.id,
        is_primary=__ret__.is_primary,
        is_stateless=__ret__.is_stateless,
        multiple_placement_groups=__ret__.multiple_placement_groups,
        name=__ret__.name,
        placement_properties=__ret__.placement_properties,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        vm_extensions=__ret__.vm_extensions,
        vm_image_offer=__ret__.vm_image_offer,
        vm_image_publisher=__ret__.vm_image_publisher,
        vm_image_sku=__ret__.vm_image_sku,
        vm_image_version=__ret__.vm_image_version,
        vm_instance_count=__ret__.vm_instance_count,
        vm_managed_identity=__ret__.vm_managed_identity,
        vm_secrets=__ret__.vm_secrets,
        vm_size=__ret__.vm_size)


@_utilities.lift_output_func(get_node_type)
def get_node_type_output(cluster_name: Optional[pulumi.Input[str]] = None,
                         node_type_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNodeTypeResult]:
    """
    Describes a node type in the cluster, each node type represents sub set of nodes in the cluster.


    :param str cluster_name: The name of the cluster resource.
    :param str node_type_name: The name of the node type.
    :param str resource_group_name: The name of the resource group.
    """
    ...
