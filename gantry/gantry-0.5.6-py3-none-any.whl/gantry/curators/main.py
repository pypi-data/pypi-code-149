import logging
import inspect
import os
from typing import Optional
from urllib.parse import urlparse

from gantry.api_client import APIClient
from gantry.const import PROD_API_URL
from gantry.curators.curators import CuratorClient
from gantry.curators import globals
from gantry.curators.globals import validate_init

logger_obj = logging.getLogger(__name__)


def _init(
    api_key: Optional[str] = None,
):
    backend = os.environ.get("GANTRY_LOGS_LOCATION", PROD_API_URL)
    parsed_origin = urlparse(backend)
    if parsed_origin.scheme not in ("http", "https"):
        raise ValueError(
            "Invalid backend. http or https backends " + "supported. Got {}".format(backend)
        )

    api_key = os.environ.get("GANTRY_API_KEY") if api_key is None else api_key

    if not api_key:
        raise ValueError(
            """
            No API key provided. Please pass the api_key parameter or set the GANTRY_API_KEY
            environment variable.
            """
        )

    api_client = APIClient(backend, api_key)
    # instantiated curators need a client, too
    globals._API_CLIENT = api_client  # type: ignore
    # this client has special methods for querying all curators
    globals._CURATOR_CLIENT = CuratorClient(api_client)  # type: ignore


def _curators_alias(func):
    """Decorator for GantryAlerts functions, exposed in main.py"""
    doc: str = ""
    orig_doc: Optional[str] = None
    if hasattr(CuratorClient, func.__name__):
        doc = "Alias for :meth:`gantry.curators.curators.CuratorClient.{}`".format(func.__name__)
        orig_doc = inspect.getdoc(getattr(CuratorClient, func.__name__))

    if orig_doc:
        doc += "\n\n{}".format(orig_doc)
    func.__doc__ = doc

    return func


@_curators_alias
def get_all_curators(application_name: Optional[str] = None):
    validate_init()
    return globals._CURATOR_CLIENT.get_all_curators(**locals())  # type: ignore


@_curators_alias
def get_curator(name: str):
    validate_init()
    return globals._CURATOR_CLIENT.get_curator(name)  # type: ignore


@_curators_alias
def list_curators(application_name: Optional[str] = None):
    validate_init()
    return globals._CURATOR_CLIENT.list_curators(application_name)  # type: ignore
