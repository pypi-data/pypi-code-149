from importlib.metadata import version

__version__ = version("dls-mainiac")
del version

__all__ = ["__version__"]
