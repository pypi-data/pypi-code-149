from datetime import datetime
from datetime import date
import json
from cnd_event_logger.cnd_base import CndBase


class CndInventory(CndBase):
    types = {
        'vra': {
            'fields': [
                'deployment_id',
                'uuid',
                'deleted',
                'datacenter',
                'cloud_account',
                'cpu',
                'memory',
                'os_type',
                'software_name',
                'power_state',
                'item_created_at',
                'item_updated_at',
                'tags',
                'tiers',
                'source',
                'hostname',
                'domain'
            ],
            'key': 'uuid'
        },
        'app': {
            'fields': [
                'hostname',
                'domain',
                'deleted',
                'source'
            ],
            'key': 'uuid'
        }
    }

    def __init__(self, host, port, token, scheme, print, key_base="iaas_inventory/inventory"):
        super().__init__(host, port, token, scheme, print)
        self.key_base = key_base
        for type_name in CndInventory.types:
            setattr(CndInventory, f"{type_name}", self.make_method(type_name))

    def make_method(self, type_name,):
        def _method(self, **kwargs):
            key_name = self.types[type_name]['key']
            key_value = kwargs[key_name]
            del(kwargs[key_name])
            path, values = self.prepare_event(type_name, key_value, **kwargs)
            return self.push_event(path, values)
        return _method

    def prepare_event(self, type_name, key, **kwargs):
        path = f"{self.key_base}/{type_name}/{kwargs['source']}/{key}"
        content = {'raw': {}}
        for data_key in kwargs:
            if data_key == 'source':
                continue
            if data_key in self.types[type_name]['fields']:
                content[data_key] = kwargs[data_key]
            else:
                content['raw'][data_key] = kwargs[data_key]

        return [path, content]
