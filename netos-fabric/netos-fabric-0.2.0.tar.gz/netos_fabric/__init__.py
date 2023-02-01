from extras.plugins import PluginConfig


class NetosFabricConfig(PluginConfig):
    name = 'netos_fabric'
    verbose_name = 'Netos Fabric'
    description = 'Add fabric models'
    version = '0.2.0'
    base_url = 'netos-fabric'

config = NetosFabricConfig

