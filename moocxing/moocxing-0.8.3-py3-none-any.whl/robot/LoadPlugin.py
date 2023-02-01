import pkgutil
from moocxing.robot import Constants

import logging

log = logging.getLogger(__name__)


def loadPlugin():
    plugins = {}
    locations = [
        Constants.PATH_CUSTOM_PLUGIN,
        Constants.PATH_PLUGIN
    ]

    for finder, name, ispkg in pkgutil.walk_packages(locations):
        loader = finder.find_module(name)

        mod = loader.load_module(name)

        if not hasattr(mod, 'Plugin'):
            continue

        plugin = mod.Plugin()

        plugins[plugin.SLUG] = plugin

        log.info("-" * 35)
        log.info(f">>> 插件加载成功 {plugin.SLUG}")

    log.info("-" * 35)
    log.info(">>> 插件加载完成\n\n")

    return plugins
