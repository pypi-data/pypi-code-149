# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""This contains factory methods for building artifact catalogs"""
import os
from typing import Optional

from autoai_ts_libs.deps.watson_core.beta.catalog import ArtifactCatalog, Repository
from autoai_ts_libs.deps.watson_core.beta.remotes import NoOpRemote, ArtifactoryRemote, S3Remote
from autoai_ts_libs.deps.watson_core.toolkit import alog, error_handler

log = alog.use_channel("FACTORY")
error = error_handler.get(log)


def build_catalog_from_config(config: object) -> Optional[ArtifactCatalog]:
    """Build an ArtifactCatalog from a config object

    Args:
        config: Config
            Config file with catalog and repo info

    Returns:
        A catalog built with the repositories configured in beta.catalog
    """
    if not (config.beta and config.beta.catalog and config.beta.catalog.repos):
        log.error("<COR77850052E>", "Configuration does not have catalog or repos")
        return None
    repo_configs = config.beta.catalog.repos

    repos = []
    for repo_config in repo_configs:
        remote_type = repo_config["remote"]["type"]

        remote_client = None
        if remote_type == "local":
            remote_client = NoOpRemote()
        elif remote_type == "artifactory":
            remote_client = ArtifactoryRemote(
                repo_config["remote"]["url"],
                repo_config["remote"]["path"],
                os.getenv("ARTIFACTORY_USERNAME"),
                os.getenv("ARTIFACTORY_API_KEY"),
            )
        elif remote_type == "s3":
            remote_client = S3Remote(
                repo_config["remote"]["bucket"],
                os.getenv("AWS_ACCESS_KEY_ID"),
                os.getenv("AWS_SECRET_ACCESS_KEY"),
                repo_config["remote"]["endpoints"],
            )
        try:
            repo = Repository(
                local_repo_root=repo_config["path"],
                remote_client=remote_client,
                nickname=repo_config["nickname"],
                read_only=repo_config["readonly"],
                default_repository=repo_config["default"],
            )
            repos.append(repo)
        except PermissionError as exc:
            message = "Error creating repository with permission error {}".format(exc)
            log.error("<COR77850053E>", message)
        except NotADirectoryError as exc:
            message = "A repo is not a directory {}".format(exc)
            log.error("<COR77850054E>", message)
        except Exception as exc:
            message = "Unknown error while creating a repo {}".format(exc)
            log.error("<COR77850055E>", message)

    try:
        return ArtifactCatalog(repos)
    except Exception as exc:
        message = "Error creating catalog {}".format(exc)
        log.error("<COR77850056E>", message)
