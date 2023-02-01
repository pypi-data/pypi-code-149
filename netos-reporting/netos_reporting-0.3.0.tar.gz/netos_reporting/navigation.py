from extras.plugins import PluginMenuItem, PluginMenu, PluginMenuButton
from utilities.choices import ButtonColorChoices

report_buttons = [
    PluginMenuButton(
        link='plugins:netos_reporting:netoseolreportdevice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
]


menu = PluginMenu(
    label='Reporting',
    groups=(
        ('Infrastructure', (
            PluginMenuItem(
                link='plugins:netos_reporting:netossoftwarereport_list',
                link_text='Software',
            ),
            PluginMenuItem(
                link='plugins:netos_reporting:netoseolreportdevice_list',
                link_text='Hardware',
                buttons=report_buttons
            ),
        )),

    ),
    icon_class='mdi mdi-chart-bar'
)
