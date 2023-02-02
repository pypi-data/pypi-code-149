import os
from logging import Logger
from pathlib import Path
from typing import List, Optional, Tuple, Union

from .config import DEFAULT_LOGGER, NAMES_TO_IGNORE, PATH_TO_GIT_REPOSITORY
from .utils.file_extractor import FileExtractor
from .utils.git import GitWorker


class DataLoader:
    """
    Main class for loads data from lfs
    """

    def __init__(
        self,
        path_to_git_repository: Optional[str] = None,
        path_to_save: Optional[str] = "../",
        logger: Optional[Logger] = None,
        is_delete_folder_with_same_name: Optional[bool] = False,
    ):
        self.__logger = logger or DEFAULT_LOGGER
        self.__git_worker = GitWorker(
            path_to_git_repository=path_to_git_repository or PATH_TO_GIT_REPOSITORY,
            path_to_save=path_to_save,
            is_delete_folder_with_same_name=is_delete_folder_with_same_name,
            logger=logger,
        )

    def load_data(self, *args, **kwargs):
        pass

    def __get_deep_path(self, start_path: Path, paths: List[str]) -> Optional[Path]:
        """

        :param start_path:
        :param paths:
        :return:
        """
        actual_path = start_path

        for path in paths:
            tmp_path = actual_path / path
            if not tmp_path.exists():
                self.__logger.warning(f"Not exists path: {tmp_path}")
                return None
            actual_path = tmp_path
        return actual_path

    def get_paths(self, paths: List[str]) -> Optional[Tuple[List[str], List[str]]]:
        """

        :param paths:
        :return: list fies and folders founded by path steps
        :rtype: Optional[Tuple[List[str],List[str]]]
        """

        def get_folders_files(_path: Path) -> Tuple[List[str], List[str]]:
            _files = list()
            _folders = list()
            for name in os.listdir(_path):

                if name in NAMES_TO_IGNORE:
                    continue
                _tmp = _path / str(name)
                if _tmp.is_file():
                    _files.append(str(_tmp.name))
                if _tmp.is_dir():
                    _folders.append(str(_tmp.name))
            return _files, _folders

        actual_path = self.__get_deep_path(self.__git_worker.git_folder, paths=paths)
        if not actual_path:
            return [], []

        files, folders = get_folders_files(actual_path)
        return files, folders

    def load_file(
        self,
        paths: List[str],
        path_to_save: Union[str, Path] = None,
        is_overwrite: bool = False,
    ):

        path_to_file = self.__get_deep_path(self.__git_worker.git_folder, paths=paths)
        if not path_to_save:
            path_to_save = path_to_file
        saved_file = FileExtractor(self.__logger).extract_file(
            path_to_storage=path_to_file, path_to_save=path_to_save
        )
        return saved_file
