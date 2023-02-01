from extras.plugins import PluginTemplateExtension


class NetosHardwareDeviceType(PluginTemplateExtension):
    model = 'dcim.devicetype'

    def right_page(self):

        return self.render('netos_core/inc/eol_report.html', extra_context={"device_type_id": self.context["object"].pk})


class NetosHardwareDevice(PluginTemplateExtension):
    model = 'dcim.device'

    def right_page(self):

        return self.render('netos_core/inc/eol_report.html', extra_context={"device_type_id": self.context["object"].device_type.pk})


template_extensions = [NetosHardwareDeviceType, NetosHardwareDevice]
