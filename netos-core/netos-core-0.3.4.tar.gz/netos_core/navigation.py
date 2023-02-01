from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

hardware_buttons = [
    PluginMenuButton(
        link='plugins:netos_core:netoshardware_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
]

report_buttons = [
    PluginMenuButton(
        link='plugins:netos_core:netoseolreportdevice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
]

software_buttons = [
    PluginMenuButton(
        link='plugins:netos_core:netossoftware_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
]


menu_items = (
    PluginMenuItem(
        link='plugins:netos_core:netoshardware_list',
        link_text='Netos Hardware',
        buttons=hardware_buttons
    ),
    PluginMenuItem(
        link='plugins:netos_core:netossoftware_list',
        link_text='Netos Software',
        buttons=software_buttons
    ),
    PluginMenuItem(
        link='plugins:netos_core:netoseolreportdevice_list',
        link_text='Netos Report',
        buttons=report_buttons
    ),

)
