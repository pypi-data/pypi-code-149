import logging
from extras.plugins import PluginConfig
from netos_inventory.constants import DEVICE_CF, MODULE_CF, INVENTORY_CF


class NetosInventoryConfig(PluginConfig):
    name = 'netos_inventory'
    verbose_name = 'Netos Inventory'
    description = 'Reconcile infrastructure inventory'
    version = '0.2.1'
    default_settings = {
        "device_recon_fields": {
        'device_type': 'Netos_Detected_Type',
        'serial': 'Netos_Detected_Serial_Number',
        'Netos_Software_Kickstart_Version': 'Netos_Detected_Software_Kickstart_Version',
        'Netos_Software_Version': 'Netos_Detected_Software_Version',
        'Netos_Hostname': 'Netos_Detected_Hostname'
        },
        "module_recon_fields": {
            'serial': 'Netos_Detected_Serial_Number', 
        },
        "inventory_recon_fields": {
            'serial': 'Netos_Detected_Serial_Number', 

        },
        "min_lan_switch_utilization": 30
    }

    base_url = 'netos_inventory'

    def ready(self):
        from dcim.models.device_components import Interface, InventoryItem
        from dcim.models.devices import Device, Module
        from extras.models.customfields import CustomField
        from ipam.models.fhrp import FHRPGroup
        from ipam.models.ip import ASN, IPAddress, Prefix
        from ipam.models.vlans import VLAN
        from ipam.models.vrfs import VRF
        from dcim.models.cables import Cable
        from wireless.models import WirelessLAN
        from extras.choices import CustomFieldTypeChoices, CustomFieldVisibilityChoices
        from django.contrib.contenttypes.models import ContentType

        logger = logging.getLogger(__name__)
        detected_models = [
            Device,
            Interface,
            InventoryItem,
            Module,
            Cable,
            VRF,
            VLAN,
            FHRPGroup,
            ASN,
            IPAddress,
            Prefix,
            WirelessLAN,
        ]
        cf = CustomField.objects.filter(name="Netos_Last_Polled").count()
        if cf == 0:
            logger.info("Creating 'Netos_Last_Polled' custom field")
            cf = CustomField.objects.create(
                type=CustomFieldTypeChoices.TYPE_DATE,
                name="Netos_Last_Polled",
                label="Last Polled",
                description="Last polled date marks when model was last time updated",
                ui_visibility=CustomFieldVisibilityChoices.VISIBILITY_READ_WRITE
            )

            cts = [ContentType.objects.get_for_model(
                dm) for dm in detected_models]
            cf.content_types.set(cts)
            cf.save()
        else:
            logger.info("Skipping creating 'Netos_Last_Polled' custom field")

        # polled_status
        cf = CustomField.objects.filter(name="polled_status").count()
        if cf == 0:
            logger.info("Creating 'polled_status' custom field")
            cf = CustomField.objects.create(
                type=CustomFieldTypeChoices.TYPE_SELECT,
                name="polled_status",
                label="Polled Status",
                default="Active",
                description="Status of device set by user",
                ui_visibility=CustomFieldVisibilityChoices.VISIBILITY_READ_WRITE,
                choices=["Active", "Decommissioning"]
            )

            cts = [ContentType.objects.get_for_model(
                dm) for dm in detected_models]
            cf.content_types.set(cts)
            cf.save()
        else:
            logger.info("Skipping creating 'polled_status' custom field")

        cf_fields = {
            Device: DEVICE_CF,
            Module: MODULE_CF,
            InventoryItem: INVENTORY_CF
        }

        for model, model_cf in cf_fields.items():
            ct = ContentType.objects.get_for_model(model)
            for cf_data in model_cf:
                cf_exists = CustomField.objects.filter(name=cf_data.name).count()
                cf = CustomField.objects.filter(
                    name=cf_data.name, content_types__model__contains=ct.name).count()
                if not cf_exists:
                    logger.info(f"Creating {cf_data.name} custom field")
                    if cf_data.field_type == CustomFieldTypeChoices.TYPE_OBJECT:
                        cf = CustomField.objects.create(
                            type=cf_data.field_type,
                            name=cf_data.name,
                            label=cf_data.label,
                            default=cf_data.default_value,
                            description=cf_data.label,
                            # TODO: Hardcoded change if new model will come, 
                            # not working with 'device type' name
                            object_type=ContentType.objects.filter(model__icontains='type').filter(model__icontains='device')[0],
                            ui_visibility=CustomFieldVisibilityChoices.VISIBILITY_READ_WRITE,
                        )
                    else:
                        cf = CustomField.objects.create(
                            type=cf_data.field_type,
                            name=cf_data.name,
                            label=cf_data.label,
                            default=cf_data.default_value,
                            description=cf_data.label,
                            ui_visibility=CustomFieldVisibilityChoices.VISIBILITY_READ_WRITE,
                        )
                    cf.content_types.add(ct)
                    cf.save()
                elif cf == 0:
                    logger.info(f"Updating content types for {cf_data.name}")
                    cf = CustomField.objects.get(name=cf_data.name)
                    cf.content_types.add(ct)
                    cf.save()
                else:
                    logger.info(f"Skipping creating {cf_data.name}")

        return super().ready()


config = NetosInventoryConfig
