"""
This is a sphinx extension which improves the documentation of Django apps.
"""
__version__ = "0.1.1"

from sphinx.application import Sphinx

from . import docstrings


def setup(app: Sphinx):
    """
    Allow this module to be used as sphinx extension.

    Setup the two sub-extensions :mod:`~sphinxcontrib_django.docstrings` and
    :mod:`~sphinxcontrib_django.roles` which can also be imported separately.

    :param app: The Sphinx application object
    :type app: ~sphinx.application.Sphinx
    """
    docstrings.setup(app)

    return {
        "version:": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
