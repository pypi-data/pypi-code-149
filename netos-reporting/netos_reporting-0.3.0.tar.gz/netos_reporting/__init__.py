from extras.plugins import PluginConfig


class NetosReportingConfig(PluginConfig):
    name = 'netos_reporting'
    verbose_name = 'Netos Reporting'
    description = 'Add reports charts'
    version = '0.3.0'
    default_settings = {
        "software_fields": {'detected_software': 'Netos_Detected_Software_Version',
                            'current_software': 'Netos_Software_Version',
                            'standard_software': 'Netos_Standard_Software_Version'}
    }

    base_url = 'netos_reporting'

config = NetosReportingConfig