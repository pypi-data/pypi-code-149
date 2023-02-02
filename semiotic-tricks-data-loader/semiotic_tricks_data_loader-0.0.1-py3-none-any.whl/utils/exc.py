"""
Module with exceptions git worker
"""
# pylint: disable=super-init-not-called


class GitWorkerException(Exception):
    """
    Base class for errors lib
    """

    pass


class ConfigKeyError(GitWorkerException):
    """
    Error if not exists section or key in config
    """

    def __init__(self, section_name: str):
        self.message = f'Not exist key "{section_name}" in config'
        Exception.__init__(self, self.message)


class GitFolderError(GitWorkerException):
    """
    If exists folder with name repository but don't have .git folder
    and `is_delete_folder_with_same_name` = False
    """

    def __init__(self):
        self.message = (
            "The folder where you want to clone the repository exists. "
            "Make sure there is no required data there and delete it "
            "or add a `is_delete_folder_with_same_name` field to the "
            "config file with the value `True`"
        )
        Exception.__init__(self, self.message)


class GitCommandError(GitWorkerException):
    """
    If execute command return code not equal 0 raise this error
    """

    def __init__(self, command: str, *args):
        additional_row = ""
        if args:
            additional_row = f"with param(s): {list(map(str, args))}"
        self.message = (
            f"Git command `{command}` {additional_row} not executable."
            f" Please look git log."
        )
        Exception.__init__(self, self.message)


class GitWorkerFileError(GitWorkerException):
    """
    If in list files  add to commit wrong type(not str or Path)
    """

    def __init__(self):
        self.message = "Wrong file value to push."
        Exception.__init__(self, self.message)


class IncorrectGitUrl(GitWorkerException):
    """
    If in config wrong url to repository
    """

    def __init__(self):
        self.message = "Wrong git url."
        Exception.__init__(self, self.message)
