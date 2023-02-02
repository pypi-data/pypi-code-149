from extras.plugins import PluginConfig

__version__ = "0.0.0.0.2"


class OCPProjectConfig(PluginConfig):
    name = "ocp_project_plugin"
    verbose_name = "Netbox Storage"
    description = "Netbox Storage"
    min_version = "3.4.0"
    version = __version__
    author = "Tim Rhomberg"
    author_email = "timrhomberg@hotmail.com"
    required_settings = []
    base_url = "ocp-project-plugin"


config = OCPProjectConfig
