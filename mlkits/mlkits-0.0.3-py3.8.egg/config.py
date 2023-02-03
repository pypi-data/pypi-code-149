from __future__ import annotations

import os
import re
import copy
import logging
import platform
import multiprocessing
from pathlib import Path
from typing import Callable, Optional, Union


class Config:
    def __init__(self, default_conf):
        self.__dict__["_default_config"] = copy.deepcopy(default_conf)  # avoiding conflicts with __getattr__
        self.reset()

    def __getitem__(self, key):
        return self.__dict__["_config"][key]

    def __getattr__(self, attr):
        if attr in self.__dict__["_config"]:
            return self.__dict__["_config"][attr]

        raise AttributeError(f"No such `{attr}` in self._config")

    def get(self, key, default=None):
        return self.__dict__["_config"].get(key, default)

    def __setitem__(self, key, value):
        self.__dict__["_config"][key] = value

    def __setattr__(self, attr, value):
        self.__dict__["_config"][attr] = value

    def __contains__(self, item):
        return item in self.__dict__["_config"]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __str__(self):
        return str(self.__dict__["_config"])

    def __repr__(self):
        return str(self.__dict__["_config"])

    def reset(self):
        self.__dict__["_config"] = copy.deepcopy(self._default_config)

    def update(self, *args, **kwargs):
        self.__dict__["_config"].update(*args, **kwargs)

    def set_conf_from_C(self, config_c):
        self.update(**config_c.__dict__["_config"])

    def register_from_C(self, config):
        from .utils import set_log_with_config  # pylint: disable=C0415

        C.set_conf_from_C(config)
        if C.logging_config:
            set_log_with_config(C.logging_config)


_default_config = {
    "logging_level": logging.INFO,
    # logging_level can control the logging level more finely
    "logging_config": {
        "version": 1,
        "formatters": {
            "logger_format": {
                "format": "[%(process)s:%(threadName)s](%(asctime)s) %(levelname)s - %(name)s - [%(filename)s:%(lineno)d] - %(message)s"
            }
        },
        "filters": {
            "field_not_found": {
                "()": "mlkits.log.LogFilter",
                "param": [".*?WARN: data not found for.*?"],
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": logging.DEBUG,
                "formatter": "logger_format",
                "filters": ["field_not_found"],
            }
        },
        "loggers": {"mlkits": {"level": logging.DEBUG, "handlers": ["console"]}},
        "disable_existing_loggers": False,
    },
}

class MLKitsConfig(Config):
    def __init__(self, default_conf):
        super().__init__(default_conf)
        self._registered = False


    def set(self, **kwargs):
        from .log import set_log_with_config, get_module_logger  # pylint: disable=C0415

        self.reset()

        _logging_config = kwargs.get("logging_config", self.logging_config)

        # set global config
        if _logging_config:
            set_log_with_config(_logging_config)

        logger = get_module_logger("Initialization", kwargs.get("logging_level", self.logging_level))




# global config
C = MLKitsConfig(_default_config)


