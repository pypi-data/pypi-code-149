"""
Improve the docstrings of Django apps.

For example:

* List all model and form fields as parameters
  (see:mod:`~sphinxcontrib_django.docstrings.classes`)
"""
from .. import __version__
from .classes import improve_class_docstring
from .config import EXCLUDE_MEMBERS, INCLUDE_MEMBERS


def setup(app):
    """
    Allow this package to be used as Sphinx extension.

    This is also called from the top-level :meth:`~sphinxcontrib_django.setup`.

    It connects to the sphinx events :event:`autodoc-skip-member` and
    :event:`autodoc-process-docstring`.

    Additionally, the sphinx config value ``django_settings`` is added via
    :meth:`~sphinx.application.Sphinx.add_config_value` and
    :meth:`~sphinxcontrib_django.docstrings.setup_django` is called on the
    :event:`config-inited` event.

    :param app: The Sphinx application object
    :type app: ~sphinx.application.Sphinx
    """
    # Load sphinx.ext.autodoc extension before registering events
    app.setup_extension("sphinx.ext.autodoc")

    # Generate docstrings for Django model fields
    # Register the docstring processor with sphinx
    app.connect("autodoc-process-docstring", improve_docstring)

    # influence skip rules
    app.connect("autodoc-skip-member", autodoc_skip)

    return {
        "version:": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def autodoc_skip(app, what, name, obj, skip, options):
    """
    Hook to tell autodoc to include or exclude certain fields (see :event:`autodoc-skip-member`).

    Sadly, it doesn't give a reference to the parent object,
    so only the ``name`` can be used for referencing.

    :param app: The Sphinx application object
    :type app: ~sphinx.application.Sphinx

    :param what: The parent type, ``class`` or ``module``
    :type what: str

    :param name: The name of the child method/attribute.
    :type name: str

    :param obj: The child value (e.g. a method, dict, or module reference)
    :type obj: object

    :param options: The current autodoc settings.
    :type options: dict
    """
    if name in EXCLUDE_MEMBERS:
        return True

    if name in INCLUDE_MEMBERS:
        return False

    return skip


def improve_docstring(app, what, name, obj, options, lines):
    """
    Hook to improve the autodoc docstrings for Django models
    (see :event:`autodoc-process-docstring`).

    :param what: The type of the object which the docstring belongs to (one of ``module``,
                 ``class``, ``exception``, ``function``, ``method`` and ``attribute``)
    :type what: str

    :param name: The fully qualified name of the object
    :type name: str

    :param obj: The documented object
    :type obj: object

    :param options: The options given to the directive: an object with attributes
                    ``inherited_members``, ``undoc_members``, ``show_inheritance`` and ``noindex``
                    that are ``True`` if the flag option of same name was given to the auto
                    directive
    :type options: object

    :param lines: A list of strings – the lines of the processed docstring – that the event
                  handler can modify in place to change what Sphinx puts into the output.
    :type lines: list [ str ]

    :return: The modified list of lines
    :rtype: list [ str ]
    """
    if what == "class":
        improve_class_docstring(app, obj, lines)

    return lines
