import git
from django.conf import settings

from commons.python import formatter


def build_info(request):
    repository = git.Repo(settings.BASE_DIR)
    try:
        branch = repository.active_branch.name
        commit = repository.active_branch.commit.hexsha
        date = formatter.date_time(repository.active_branch.commit.committed_datetime)
        version_info = {'version_key': 'branch', 'version': branch, 'commit': commit, 'date': date}
        return version_info
    except Exception as error:
        print(f'An error was occurred: {error}')
        tag = repository.tags[0]
        tag_name = tag.name
        tag_commit = tag.commit.hexsha
        tag_commit_date = formatter.date_time(tag.commit.committed_datetime)

        version = (val for val in tag_name if val.isdigit() or val == '.')
        version = ''.join(version)
        version_info = {'version_key': 'version', 'version': version, 'commit': tag_commit, 'date': tag_commit_date}
        return version_info
