from dataclasses import dataclass

from extras.choices import CustomFieldTypeChoices


@dataclass
class InitCustomField:
    name: str
    field_type: CustomFieldTypeChoices
    default_value: str = ""
    object_type: str = ""

    @property
    def label(self) -> str:
        return " ".join(self.name.split("_")[1:])

DEVICE_CF = (

    InitCustomField(
        name="Netos_Detected_Serial_Number",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Detected_Software_Kickstart_Version",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Software_Version",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Detected_Software_Version",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Detected_Type",
        field_type=CustomFieldTypeChoices.TYPE_OBJECT,
        object_type="device type",
        default_value=None,
    ),
    InitCustomField(
        name="Netos_Hostname",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Detected_Hostname",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Software_Kickstart_Version",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Detected_Type",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
)

MODULE_CF = (
    InitCustomField(
        name="Netos_Detected_Serial_Number",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
)

INVENTORY_CF = (
    InitCustomField(
        name="Netos_Detected_Serial_Number",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Detected_Software_Kickstart_Version",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
    InitCustomField(
        name="Netos_Software_Kickstart_Version",
        field_type=CustomFieldTypeChoices.TYPE_TEXT
    ),
)
