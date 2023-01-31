# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Top-level configuration for the `watson_core` library.  Mainly used for model management and
version.
"""

import os

from autoai_ts_libs.deps.watson_core import ModelManager

from ..toolkit.errors import error_handler
from .config import *
from . import catalog

lib_config = Config.get_config(
    "watson_core",
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.yml"),
)

# Update the global error configurations
error_handler.ENABLE_ERROR_CHECKS = lib_config.enable_error_checks
error_handler.MAX_EXCEPTION_LOG_MESSAGES = lib_config.max_exception_log_messages

MODEL_CATALOG = ModelCatalog(
    {}, lib_config.library_version, lib_config.artifactory_base_path
)
RESOURCE_CATALOG = ResourceCatalog(
    {}, lib_config.library_version, lib_config.artifactory_base_path
)
WORKFLOW_CATALOG = WorkflowCatalog(
    {}, lib_config.library_version, lib_config.artifactory_base_path
)

# aliases helpers for users
get_models = MODEL_CATALOG.get_models
get_alias_models = MODEL_CATALOG.get_alias_models
get_latest_models = MODEL_CATALOG.get_latest_models
get_resources = RESOURCE_CATALOG.get_resources
get_alias_resources = RESOURCE_CATALOG.get_alias_resources
get_latest_resources = RESOURCE_CATALOG.get_latest_resources
get_workflows = WORKFLOW_CATALOG.get_workflows
get_alias_workflows = WORKFLOW_CATALOG.get_alias_models
get_latest_workflows = WORKFLOW_CATALOG.get_latest_models

MODEL_MANAGER = ModelManager(
    lib_config.artifactory_base_path, MODEL_CATALOG, RESOURCE_CATALOG, WORKFLOW_CATALOG
)

download = MODEL_MANAGER.download
extract = MODEL_MANAGER.extract
fetch = MODEL_MANAGER.fetch
load = MODEL_MANAGER.load
download_and_load = MODEL_MANAGER.download_and_load
resolve_and_load = MODEL_MANAGER.resolve_and_load
