from importlib.metadata import version

__version__ = version("setuptools_openapi_generator")
del version

__all__ = ["__version__"]
