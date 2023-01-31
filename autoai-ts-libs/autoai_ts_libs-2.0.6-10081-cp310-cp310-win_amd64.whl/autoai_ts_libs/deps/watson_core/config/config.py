# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Config methods for the `watson_core` library. Mainly interacts with `config.yml`.
"""

import os

import semver

from importlib import metadata

from autoai_ts_libs.deps.watson_core.toolkit import aconfig
from autoai_ts_libs.deps.watson_core.toolkit import alog
from ..toolkit.errors import error_handler

from .catalog import ModelCatalog, ResourceCatalog, WorkflowCatalog


log = alog.use_channel("CONFIG")
error = error_handler.get(log)


# restrict functions that are imported so we don't pollute the base module namespce
__all__ = [
    "Config",
    "compare_versions",
    "get_credentials_or_default",
    "ModelCatalog",
    "WorkflowCatalog",
    "ResourceCatalog",
]

log = alog.use_channel("WCAICNFG")
error = error_handler.get(log)


class Config(aconfig.Config):
    @classmethod
    def get_config(cls, library_name, config_path, use_legacy_versioning=False):
        """Get top-level configuration for `watson_core` library and extensions. Generally only
        used by internal functions.
        """
        out_config = cls.from_yaml(config_path)
        # useful variables to have
        out_config.library_name = library_name
        # If we enable legacy versioning, use <libname>_version from the config
        if use_legacy_versioning:
            out_config.library_version_key = "{0}_version".format(
                out_config.library_name
            )
            out_config.library_version = out_config[out_config.library_version_key]
        else:
            try:
                out_config.library_version = metadata.version(library_name)
            except metadata.PackageNotFoundError:
                log.warning("<COR25991305W>", "No library version found")
                out_config.library_version = "0.0.0"

        out_config.artifact_path = out_config.artifactory_base_path
        return out_config


def compare_versions(v1, v2):
    """Compare a given version against the other. Used for comparing model and library versions.

    Args:
        v1:  str
            SemVer version to compare.
        v2:  str
            SemVer version to compare.

    Returns:
        int
            -1 if `v1` version is less than `v2`, 0 if equal and 1 if greater
    """
    return semver.VersionInfo.parse(v1).compare(v2)


def get_credentials_or_default(username=None, password=None):
    """Get credentials as passed or default (picking up environment variables
    ARTIFACTORY_USERNAME, ARTIFACTORY_API_KEY)

    Returns: (username, password)
    """
    if not username:
        username = os.environ.get("ARTIFACTORY_USERNAME")

    if not password:
        password = os.environ.get("ARTIFACTORY_API_KEY")

    if username is None or password is None:
        error(
            "<COR25111305E>",
            ValueError(
                "No artifactory credentials passed, please pass in username/password as arguments"
            ),
        )

    return username, password
