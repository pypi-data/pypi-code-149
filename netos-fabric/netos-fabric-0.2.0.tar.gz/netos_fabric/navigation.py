from utilities.choices import ButtonColorChoices
from extras.plugins import PluginMenuItem, PluginMenu, PluginMenuButton


networkfabric_buttons = [
    PluginMenuButton(
        link='plugins:netos_fabric:networkfabric_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


menu = PluginMenu(
    label='Fabric',
    groups=(
        ('Network Fabric', (
            PluginMenuItem(
                link='plugins:netos_fabric:networkfabric_list',
                link_text='Network Fabric',
                buttons=networkfabric_buttons
            ),
        )),
    ),
    icon_class='mdi mdi-lan'
)
