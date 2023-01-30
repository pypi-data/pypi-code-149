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
    'GetVirtualMachineScaleSetResult',
    'AwaitableGetVirtualMachineScaleSetResult',
    'get_virtual_machine_scale_set',
    'get_virtual_machine_scale_set_output',
]

warnings.warn("""Version 2017-03-30 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetVirtualMachineScaleSetResult:
    """
    Describes a Virtual Machine Scale Set.
    """
    def __init__(__self__, id=None, identity=None, location=None, name=None, overprovision=None, plan=None, provisioning_state=None, single_placement_group=None, sku=None, tags=None, type=None, unique_id=None, upgrade_policy=None, virtual_machine_profile=None, zones=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if overprovision and not isinstance(overprovision, bool):
            raise TypeError("Expected argument 'overprovision' to be a bool")
        pulumi.set(__self__, "overprovision", overprovision)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if single_placement_group and not isinstance(single_placement_group, bool):
            raise TypeError("Expected argument 'single_placement_group' to be a bool")
        pulumi.set(__self__, "single_placement_group", single_placement_group)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)
        if upgrade_policy and not isinstance(upgrade_policy, dict):
            raise TypeError("Expected argument 'upgrade_policy' to be a dict")
        pulumi.set(__self__, "upgrade_policy", upgrade_policy)
        if virtual_machine_profile and not isinstance(virtual_machine_profile, dict):
            raise TypeError("Expected argument 'virtual_machine_profile' to be a dict")
        pulumi.set(__self__, "virtual_machine_profile", virtual_machine_profile)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.VirtualMachineScaleSetIdentityResponse']:
        """
        The identity of the virtual machine scale set, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def overprovision(self) -> Optional[bool]:
        """
        Specifies whether the Virtual Machine Scale Set should be overprovisioned.
        """
        return pulumi.get(self, "overprovision")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.PlanResponse']:
        """
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="singlePlacementGroup")
    def single_placement_group(self) -> Optional[bool]:
        """
        When true this limits the scale set to a single placement group, of max size 100 virtual machines.
        """
        return pulumi.get(self, "single_placement_group")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The virtual machine scale set sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Specifies the ID which uniquely identifies a Virtual Machine Scale Set.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional['outputs.UpgradePolicyResponse']:
        """
        The upgrade policy.
        """
        return pulumi.get(self, "upgrade_policy")

    @property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> Optional['outputs.VirtualMachineScaleSetVMProfileResponse']:
        """
        The virtual machine profile.
        """
        return pulumi.get(self, "virtual_machine_profile")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set.
        """
        return pulumi.get(self, "zones")


class AwaitableGetVirtualMachineScaleSetResult(GetVirtualMachineScaleSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineScaleSetResult(
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            overprovision=self.overprovision,
            plan=self.plan,
            provisioning_state=self.provisioning_state,
            single_placement_group=self.single_placement_group,
            sku=self.sku,
            tags=self.tags,
            type=self.type,
            unique_id=self.unique_id,
            upgrade_policy=self.upgrade_policy,
            virtual_machine_profile=self.virtual_machine_profile,
            zones=self.zones)


def get_virtual_machine_scale_set(resource_group_name: Optional[str] = None,
                                  vm_scale_set_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineScaleSetResult:
    """
    Describes a Virtual Machine Scale Set.


    :param str resource_group_name: The name of the resource group.
    :param str vm_scale_set_name: The name of the VM scale set.
    """
    pulumi.log.warn("""get_virtual_machine_scale_set is deprecated: Version 2017-03-30 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['vmScaleSetName'] = vm_scale_set_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20170330:getVirtualMachineScaleSet', __args__, opts=opts, typ=GetVirtualMachineScaleSetResult).value

    return AwaitableGetVirtualMachineScaleSetResult(
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        overprovision=__ret__.overprovision,
        plan=__ret__.plan,
        provisioning_state=__ret__.provisioning_state,
        single_placement_group=__ret__.single_placement_group,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type,
        unique_id=__ret__.unique_id,
        upgrade_policy=__ret__.upgrade_policy,
        virtual_machine_profile=__ret__.virtual_machine_profile,
        zones=__ret__.zones)


@_utilities.lift_output_func(get_virtual_machine_scale_set)
def get_virtual_machine_scale_set_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                         vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineScaleSetResult]:
    """
    Describes a Virtual Machine Scale Set.


    :param str resource_group_name: The name of the resource group.
    :param str vm_scale_set_name: The name of the VM scale set.
    """
    pulumi.log.warn("""get_virtual_machine_scale_set is deprecated: Version 2017-03-30 will be removed in v2 of the provider.""")
    ...
