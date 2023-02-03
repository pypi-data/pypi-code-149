from extras.plugins import PluginConfig

__version__ = "0.0.0.0.95"


class OCPProjectConfig(PluginConfig):
    name = "ocp_project_plugin"
    verbose_name = "OCP Project Plugin"
    description = "The netbox ocp project plugin, for creating ocp projects"
    min_version = "3.4.0"
    version = __version__
    author = "Tim Rhomberg"
    author_email = "timrhomberg@hotmail.com"
    required_settings = [
        "gitlab_project_url",
        "values_path",
        "default_access_token",
        'jira_browse_url',
        'ocp_tst_url',
        'ocp_dev_url',
        'ocp_int_url',
        'ocp_prd_url',
        'cpu_cost',
        'memory_cost',
        'storage_cost'
    ]
    base_url = "ocp-project-plugin"


config = OCPProjectConfig
