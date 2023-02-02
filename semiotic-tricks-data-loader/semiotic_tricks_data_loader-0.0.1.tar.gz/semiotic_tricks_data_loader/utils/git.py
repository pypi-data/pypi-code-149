"""
Module with git worker
"""
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from logging import Logger
from pathlib import Path
from typing import Any, List, Optional, Union

from ..config import DEFAULT_LOGGER
from .exc import GitCommandError, GitFolderError, GitWorkerFileError, IncorrectGitUrl

REGEX_GIT_REPOS_URL = r"(\w+://)(.+@)*([\w\d\.]+)(:[\d]+){0,1}/*(.*)"


class GitWorker:
    """
    Class for working with git
    """

    _logger: Logger = None
    __git_repos: str = None
    __git_folder: Path = None
    __folder_name = os.getenv("clone_to_folder")

    __is_delete_folder_with_same_name: bool = False

    @property
    def folder_name(self):
        return self.__folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        if not self.__folder_name:
            self.__folder_name = folder_name

    @property
    def git_folder(self) -> Optional[Path]:
        return self.__git_folder

    def __init__(
        self,
        path_to_git_repository: str,
        path_to_save: Optional[str] = "../",
        logger: Optional[Logger] = None,
        is_delete_folder_with_same_name: Optional[bool] = False,
    ):
        """

        :param path_to_git_repository:
        :param path_to_save:
        :param logger:
        :param is_delete_folder_with_same_name:
        """
        self._logger = logger or DEFAULT_LOGGER
        self.__check_is_existing_lfs()
        self.__git_repos = path_to_git_repository

        folder_name = path_to_git_repository.split("/")[-1]
        if folder_name[-4:] == ".git":
            folder_name = folder_name[:-4]
        self.folder_name = folder_name

        if not re.match(REGEX_GIT_REPOS_URL, self.__git_repos):
            raise IncorrectGitUrl()

        # just in case someone sets the parameters wrong :)
        self.__is_delete_folder_with_same_name = is_delete_folder_with_same_name
        self.__path_to_save = path_to_save

        self.__git_folder = Path(self.__path_to_save).resolve() / self.folder_name
        self.__git_folder.mkdir(exist_ok=True, parents=True)

        self.current_main_folder = Path().resolve()

        self._git_checker()

    def __check_is_existing_lfs(self):
        """
        Method to check is installed git lfs
        :return:
        """
        "git lfs --version"
        try:
            self.__execute_command(command="lfs", args="--version")
        except GitCommandError:
            self._logger.warning(
                "Please install LFS on your device. Look a https://git-lfs.com/"
            )
            sys.exit(1)

    def _git_checker(self):
        """
        Method for check infrastructure git repository
        """

        if self.is_exist_clone_repository():
            if self.is_exist_clone_repository(check_git_repos=True):
                self._git_pool_command_executor()
            else:
                if self.__is_delete_folder_with_same_name:
                    shutil.rmtree(self.__git_folder)
                    self._git_clone_command_executor()
                else:
                    raise GitFolderError()
        else:
            self._git_clone_command_executor()

    def is_exist_clone_repository(self, check_git_repos: bool = False) -> bool:
        """
        Check for folder existence
        :param bool check_git_repos: check git folder in base_folder
        :return: is exist folder or not
        """
        path = os.path.join(self.__path_to_save, self.folder_name)
        if check_git_repos:
            path = os.path.join(path, ".git")
        return os.path.exists(path)

    def __execute_command(
        self, command: str, args: Optional[Any] = None, run_from_folder: Path = None
    ):
        if not run_from_folder:
            run_from_folder = self.__git_folder
        args_command = list(("git", command))
        if args:
            if not isinstance(args, (list, tuple)):
                args = list((args,))
        else:
            args = list()
        args_command.extend(args)
        cmd = subprocess.Popen(args_command, cwd=run_from_folder)
        cmd.wait()
        if cmd.poll():
            raise GitCommandError(command, *args)

    def _git_pool_command_executor(self):
        self.__execute_command(command="pull")

    def _git_clone_command_executor(self):
        """
        Execute `git clone` command.
        """
        self.__execute_command(
            command="clone", args=self.__git_repos, run_from_folder=self.__path_to_save
        )

    def _git_add_command_executor(self, path_to_added_file: Path) -> None:
        """
        Execute `git add` command
        :param path_to_added_file:
        """
        self.__execute_command(command="add", args=path_to_added_file)

    def _git_push_command_executor(self) -> None:
        """
        Execute `git push` command
        """
        self.__execute_command(command="push", args=self.__git_repos)

    def _git_commit_command_executor(self, comment: str = "") -> None:
        """
        Execute `git commit` command
        :param str comment: comment to commit
        """
        self.__execute_command(command="commit", args=("-m", f'"{comment}"'))

    def push_new_files(
        self, files_to_add: Union[Path, List[Path]], comment: Optional[str] = None
    ) -> None:
        if not isinstance(files_to_add, list):
            files_to_add = [files_to_add]

        for file in files_to_add:
            if not isinstance(file, Path):
                try:
                    file = Path(file)
                except TypeError:
                    self._logger.error(
                        "GitWorkerPushError wrong value in files_to_add variable",
                        exc_info=True,
                    )
                    raise GitWorkerFileError()
                except Exception as exc:
                    self._logger.error("GitWorkerError", exc_info=True)
                    raise exc
            if not file.is_file():
                raise FileNotFoundError(f"File to push not exists. File {file}")

            self._git_add_command_executor(file)

        if not comment:
            comment = f"New commit from {datetime.now().isoformat()}"

        self._git_commit_command_executor(comment=comment)
        self._git_pool_command_executor()
        self._git_push_command_executor()

    def pull_repository(self) -> None:
        """
        Call pull command
        """
        self._git_pool_command_executor()
