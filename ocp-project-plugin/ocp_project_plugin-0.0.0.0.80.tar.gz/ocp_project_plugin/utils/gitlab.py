from django.conf import settings
from git import Repo, Git

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get('ocp_project_plugin', dict())
GITLAB_PROJECT_URL = PLUGIN_SETTINGS.get('gitlab_project_url', '')
VALUES_PATH = PLUGIN_SETTINGS.get('values_path', '')


def clone_repo():
    repo_instance = Repo.clone_from(
        GITLAB_PROJECT_URL, '/repo/project_repo')


def pull_repo(git_dir):
    repo_instance = Git(git_dir)
    result = repo_instance.pull()
    print(f'{result}')


def add_ocp_project():
    print()


class GitlabProjectManager:
    def __init__(self, context):
        super().__init__(context)
