import pkg_resources


path = pkg_resources.resource_filename("cnd_event_logger", "VERSION")
__version__ = open(path).read()
