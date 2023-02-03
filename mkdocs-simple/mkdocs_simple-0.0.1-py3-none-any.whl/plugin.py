from typing import TYPE_CHECKING

from mkdocs.plugins import BasePlugin

from .gitlab import make_gitlab_settings

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig

    from .site_config import SiteConfig


class MkDocsSettingsPlugin(BasePlugin):
    # def __init__(self):
    #     pass

    # def on_startup(self, command, dirty) -> None:
    #     pass

    def on_config(self, config: "MkDocsConfig") -> "MkDocsConfig":
        site_config = make_gitlab_settings()
        _site_config_to_mkdocs(config, site_config)
        # TODO make github_settings

        # TODO
        # if bellow files there aren't in docs than copy them to there
        # copy README to docs
        # copy CONTRIBUTING to docs
        # copy CHANGELOG to docs
        # copy CODE_OF_CONDUCT to docs

        return config


def _site_config_to_mkdocs(
    config: "MkDocsConfig",
    site_config: "SiteConfig",
) -> "MkDocsConfig":
    config["site_name"] = site_config.site_name
    config["site_description"] = site_config.site_description
    config["site_url"] = site_config.site_url
    config["repo_name"] = site_config.repo_name
    return config
