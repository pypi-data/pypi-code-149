
#
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor

# DataType {FLOAT, INT, BOOLEAN, STRING}
from muphyn.packages.interface.properties_pages.data_property_widgets.basic_type_property_widgets import \
    BooleanPropertyWidget, DoublePropertyWidget, IntegerPropertyWidget, StringPropertyWidget, UnknownTypePropertyWidget, PropertyLineEdit

# Datatype {ANYFILE, DIRECTORY, EXISTINGFILE, EXISTINGFILES}
from muphyn.packages.interface.properties_pages.data_property_widgets.path_property_widgets import \
    AnyFilePropertyWidget, DirectoryPropertyWidget, ExistingFilePropertyWidget, ExistingFilesPropertyWidget

from muphyn.packages.interface.properties_pages.data_property_widgets.choice_property_widget import ChoicePropertyWidget

def property_widget_factory(parameter_to_edit: dict) -> AbstractPropertiesEditor:
    # Get parameter type name
    param_type_name = parameter_to_edit["type"].__str__().lower()


    if param_type_name == str(DataType.BOOLEAN):
        return BooleanPropertyWidget()

    elif param_type_name == str(DataType.FLOAT):
        return PropertyLineEdit(parameter_to_edit, DataType.FLOAT)
        # return DoublePropertyWidget(parameter_to_edit)

    elif param_type_name == str(DataType.INT):
        return PropertyLineEdit(parameter_to_edit, DataType.INT)
        # return IntegerPropertyWidget(parameter_to_edit)

    elif param_type_name == str(DataType.STRING):
        # return  PropertyLineEdit(parameter_to_edit, DataType.STRING)
        return  StringPropertyWidget(parameter_to_edit)

    elif param_type_name == str(DataType.ANYFILE):
        return AnyFilePropertyWidget()

    elif param_type_name == str(DataType.DIRECTORY):
        return DirectoryPropertyWidget()

    elif param_type_name == str(DataType.EXISTINGFILE):
        return ExistingFilePropertyWidget()

    elif param_type_name == str(DataType.EXISTINGFILES):
        return ExistingFilesPropertyWidget()

    elif param_type_name == str(DataType.CHOICE):
        return ChoicePropertyWidget(parameter_to_edit)
    else:
        LogManager().error(f"Unsupported parameter type for : {param_type_name}")
        return UnknownTypePropertyWidget(param_type_name.__str__())
