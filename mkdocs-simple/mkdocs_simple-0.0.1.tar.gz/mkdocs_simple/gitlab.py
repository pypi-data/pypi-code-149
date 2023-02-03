import os

from .site_config import SiteConfig

CI_PROJECT_TITLE = "CI_PROJECT_TITLE"
CI_PROJECT_DESCRIPTION = "CI_PROJECT_DESCRIPTION"
CI_PROJECT_URL = "CI_PROJECT_URL"
CI_PROJECT_NAME = "CI_PROJECT_NAME"
CI_PROJECT_PATH = "CI_PROJECT_PATH"
CI_DEFAULT_BRANCH = "CI_DEFAULT_BRANCH"


def make_gitlab_settings() -> SiteConfig:
    project_title = os.getenv(CI_PROJECT_TITLE, "Documentation")
    project_description = os.getenv(CI_PROJECT_DESCRIPTION, "")
    project_url = os.getenv(CI_PROJECT_URL)
    project_name = os.getenv(CI_PROJECT_NAME)
    # .project_path = os.getenv(CI_PROJECT_PATH)

    return SiteConfig(
        site_name=project_title,
        site_url=project_url,
        site_description=project_description,
        repo_name=project_name,
        copyright=None,
        repo_url=None,
        edit_url=None,
    )
