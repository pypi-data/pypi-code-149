from extras.plugins import PluginConfig

__version__ = "0.0.0.0.19"


class OCPProjectConfig(PluginConfig):
    name = "ocp_project_plugin"
    verbose_name = "OCP Project Plugin"
    description = "The netbox ocp project plugin, for creating ocp projects"
    min_version = "3.4.0"
    version = __version__
    author = "Tim Rhomberg"
    author_email = "timrhomberg@hotmail.com"
    required_settings = []
    base_url = "ocp-project-plugin"


config = OCPProjectConfig
