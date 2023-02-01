from extras.plugins import PluginConfig


class NetosCoreConfig(PluginConfig):
    name = 'netos_core'
    verbose_name = ' Netos Core'
    description = 'Enrich netbox models'
    version = '0.3.4'
    default_settings = {
        'warning_threshold': '0',
        'danger_threshold': '-1'
    }
    base_url = 'netos_core'


config = NetosCoreConfig
