import consul
from datetime import datetime
from datetime import date
import json
from cnd_event_logger.__version__ import __version__


class CndBase:
    def __init__(self, host, port, token, scheme, print):
        self._print = print
        self._print.info_c(f"CndEventLogger {__version__}")
        self._host = host
        self._port = port
        self._token = token
        self._scheme = scheme
        self._consul = consul.Consul(host=self._host, port=self._port, scheme=self._scheme, token=self._token)

    def push_event(self, key, values):
        self._print.trace_v("Pushing event")
        result = self._consul.kv.put(key, json.dumps(values, default=str))
        return result
