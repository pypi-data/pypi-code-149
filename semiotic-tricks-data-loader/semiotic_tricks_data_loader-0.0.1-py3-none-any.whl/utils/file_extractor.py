import os
import re
from logging import Logger
from pathlib import Path
from shutil import copy
from typing import Optional, Tuple, Union

from ..config import DEFAULT_LOGGER

REGEX_SHA_256 = r"\b[A-Fa-f0-9]{64}\b"


class FileExtractor:
    """ """

    def __init__(
        self,
        logger: Optional[Logger],
    ):
        self._logger = logger or DEFAULT_LOGGER

    @staticmethod
    def is_need_to_download_file(
        path_to_storage: Union[str, Path], path_to_save: Union[str, Path]
    ) -> bool:
        """
        Helper method to check if the file needs to be loaded
        if the file to upload does not exist  - load
        if the date of modification of the lfs file is earlier
        than the date of modification of the file where to save - do not load
        :param str path_to_storage: path to the file with lfs data
        :param str path_to_save: path where to save
        :return: bool download file or not
        """
        # check is exist file
        # if file not exist need to download
        if os.path.isfile(path_to_save):
            # if in lfs file last updated before last update file in folder
            if os.path.getmtime(path_to_save) > os.path.getmtime(path_to_storage):
                return False
        return True

    @staticmethod
    def standardize_inputted_data(
        path_to_storage: Union[str, Path],
        path_to_save: Union[str, Path] = None,
        file_name: str = "",
        is_check_file_existence: bool = True,
    ) -> Tuple[Path, Path, str]:
        """
        Method for check and format correct data for execute `load_model`
        :param str path_to_storage: path to the file with lfs data
        :type path_to_storage: Union[str, Path]
        :param path_to_save: path where to save
        :type path_to_save: Union[str, Path]
        :param file_name:
        :type file_name:
        :param is_check_file_existence:
        :type is_check_file_existence: bool
        :return:
        :rtype: Tuple[Path, Path, str]
        """
        if not path_to_storage:
            raise ValueError("The storage path must be specified")
        if isinstance(path_to_storage, str):
            path_to_storage = Path(path_to_storage)
        if isinstance(path_to_save, str):
            path_to_save = Path(path_to_save)
        if not path_to_save:
            path_to_save = Path("")
            if not file_name:
                path_to_save = path_to_save / path_to_storage.name

        if file_name:
            path_to_storage = path_to_storage / Path(file_name)
            path_to_save = path_to_save / Path(file_name)
        else:
            file_name = path_to_storage.name
        if is_check_file_existence and not path_to_storage.is_file():
            raise ValueError(f"No file at the specified path: `{path_to_storage}`")

        return path_to_storage, path_to_save, file_name

    def extract_file(
        self,
        path_to_storage: Union[str, Path],
        path_to_save: Union[str, Path],
        file_name: str = "",
    ) -> Path:
        """
         Method for download file from lfs(if correct file)
        if the file is incorrect, then we consider that it is not an image and copy it
        :param path_to_storage:
        :type path_to_storage: Union[str, Path]
        :param path_to_save:
        :type path_to_save: Union[str, Path]
        :param file_name:
        :type file_name: str
        :return:
        :rtype:
        """
        path_to_storage, path_to_save, file_name = self.standardize_inputted_data(
            path_to_storage, path_to_save, file_name
        )
        if not self.is_need_to_download_file(
            path_to_storage=path_to_storage, path_to_save=path_to_save
        ):
            self._logger.info(
                f"File `{path_to_storage}` is not extracted "
                f"because there is an actual version.",
            )
            return path_to_save

        os.makedirs(path_to_save.parent, exist_ok=True)
        with open(path_to_storage, "rb") as file:
            try:
                file.readline().decode("utf-8")
                # try extracting oid from lfs_file
                oid = file.readline().decode("utf-8").split(":")[1]

                if re.match(REGEX_SHA_256, oid) is None:
                    # if the file is not an image of a file with
                    # a link to the storage, then copy the file
                    copy(path_to_storage, path_to_save)
                    self._logger.info(
                        "LFS fetch failed because the file is not an image."
                        " File copied - `%s`.",
                        path_to_storage,
                    )
                    return path_to_save

                oid = re.sub(r"\W+", "", oid)
                # print(oid)
                cmd = "curl " + str(path_to_storage) + oid + " > " + str(path_to_save)
                if os.system(cmd):
                    self._logger.info("LFS fetch failed for %s", file_name)
                else:
                    self._logger.info("LFS fetch done for %s", file_name)
            except UnicodeDecodeError:
                self._logger.info(
                    "LFS fetch failed because the file is not an image."
                    " File copied - `%s`.",
                    path_to_storage,
                )

                copy(path_to_storage, path_to_save)
            except IndexError:
                self._logger.info(
                    "LFS fetch failed because the file is not an image."
                    " File copied - `%s`.",
                    path_to_storage,
                )
                if path_to_storage != path_to_save:
                    copy(path_to_storage, path_to_save)
        return path_to_save
