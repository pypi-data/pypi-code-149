from datetime import datetime
from datetime import date
import json
from cnd_event_logger.cnd_base import CndBase


class CndEvent(CndBase):
    types = {
        'host': {
            'fields': ['tiers', 'deployment_id', 'source', 'hostname', 'domain', 'success', 'start_at', 'end_at'],
            'key': 'host_id'
        },
        'deployment': {
            'fields': ['service', 'deployment_name', 'source', 'project', 'success', 'owner', 'start_at', 'end_at'],
            'key': 'deployment_id'
        },
        'deployment_workflow': {
            'fields': ['source', 'application', 'name', 'deployment_id', 'success', 'start_at', 'end_at'],
            'key': 'workflow_id'
        },
        'host_workflow': {
            'fields': ['application', 'name', 'hostname', 'domain', 'success', 'start_at', 'end_at'],
            'key': 'workflow_id'
        },
    }
    def __init__(self, host, port, token, scheme, print, key_base="iaas_inventory/events"):
        super().__init__(host, port, token, scheme, print)
        self.key_base = key_base
        for type_name in CndEvent.types:
            for step in ['start', 'end']:
                setattr(CndEvent, f"{type_name}_{step}", self.make_method(type_name, step))

    def make_method(self, type_name, step):
        def _method(self, **kwargs):
            key_name = self.types[type_name]['key']
            key_value = kwargs[key_name]
            del(kwargs[key_name])
            path, values = self.prepare_event(type_name, key_value, step, **kwargs)
            return self.push_event(path, values)
        return _method

    def prepare_event(self, type_name, key, step, **kwargs):
        path = f"{self.key_base}/{type_name}/{key}/{step}"
        content = {'raw': {}}
        if f"{step}_at" not in kwargs:
            content[f"{step}_at"] = datetime.now()
        for data_key in kwargs:
            if data_key in self.types[type_name]['fields']:
                content[data_key] = kwargs[data_key]
            else:
                content['raw'][data_key] = kwargs[data_key]

        return [path, content]
