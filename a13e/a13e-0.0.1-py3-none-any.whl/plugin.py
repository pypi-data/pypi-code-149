import importlib
import pkgutil
from types import ModuleType
from typing import Type, TYPE_CHECKING, Optional, Dict, List

# from a13e import plugins

if TYPE_CHECKING:
    from a13e.recognizer import BaseRecognizer


class PluginRegister:
    """Plugin Registrar.

    It is used to extend more recognizers, and automatically imports all plugins in the plugins
    directory of the package path when instantiated. The class attribute dictionary named recognizers is used to
    store the recognizer, the key is the name of the recognizer, and the value is the instance of the recognizer.
    """
    recognizers: Dict[str, 'BaseRecognizer'] = {}

    def __init__(self, pkg: ModuleType):
        self.load_plugins(pkg)

    @classmethod
    def register(cls, recognizer: Type['BaseRecognizer']):
        """Register and instantiate a recognizer."""
        instance = recognizer()
        cls.recognizers[instance.name] = instance
        return instance

    @staticmethod
    def load_plugins(pkg: ModuleType):
        plugins: List[ModuleType] = []
        for module_finder, name, ispkg in pkgutil.iter_modules([pkg.__path__[0]]):
            if not (module_spec := module_finder.find_spec(name, None)):
                continue
            if not module_spec.origin:
                continue

            module_name = f"{pkg.__name__}.{name}"
            module = importlib.import_module(module_name)
            if ispkg:
                PluginRegister.load_plugins(module)
                continue
            if module in plugins:
                continue
            plugins.append(module)

        return plugins


def get_recognizer(name: str) -> Optional['BaseRecognizer']:
    """Get a registered recognizer by name."""
    return plugin_manager.recognizers.get(name)


plugin_manager = PluginRegister(importlib.import_module('a13e.plugins'))
