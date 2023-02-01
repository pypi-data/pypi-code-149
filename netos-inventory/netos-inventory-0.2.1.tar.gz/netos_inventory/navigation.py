from extras.plugins import PluginMenuItem, PluginMenu


menu = PluginMenu(
    label='Inventory',
    groups=(
        ('Reconciliation', (
            PluginMenuItem(
                link='plugins:netos_inventory:recondevice_list',
                link_text='Reconcile devices'
            ),
            PluginMenuItem(
                link='plugins:netos_inventory:reconmodule_list',
                link_text='Reconcile modules'
            ),
            PluginMenuItem(
                link='plugins:netos_inventory:reconinventoryitem_list',
                link_text='Reconcile inventory items'
            ),
            PluginMenuItem(
                link='plugins:netos_inventory:lanconsolidationreport_list',
                link_text='LAN Consolidation Report'
            ))),
        ('Last Detected', (
            PluginMenuItem(
                link='plugins:netos_inventory:vrfdetected_list',
                link_text='Logical Last Detected'
            ),
            PluginMenuItem(
                link='plugins:netos_inventory:devicedetected_list',
                link_text='Hardware Last Detected'
            ),
        )),
    ),
    icon_class='mdi mdi-list-box-outline'
)
