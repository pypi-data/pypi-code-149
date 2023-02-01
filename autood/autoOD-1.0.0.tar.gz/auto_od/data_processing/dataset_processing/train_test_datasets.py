import errno
import os
import shutil

from auto_od.core.logger import logger
from auto_od.data_processing.dataset_processing.base import BasePrepareData
from auto_od.utils.decorators import error_handler
from auto_od.utils.info_messages import folder_exist


class PrepareDivideData(BasePrepareData):
    def __init__(self, config_path: str):
        super().__init__(config_path=config_path)
        if not os.path.isdir(self.settings.dataset_dir):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.settings.dataset_dir)

        self.test_dir: str = os.path.join(self.settings.dataset_dir, self.settings.test_folder)
        if not os.path.isdir(self.test_dir):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.test_dir)
        self.train_dir: str = os.path.join(self.settings.dataset_dir, self.settings.train_folder)
        if not os.path.isdir(self.train_dir):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.train_dir)
        self.all_data_dir: str = os.path.join(self.settings.dataset_dir, self.settings.all_data_folder)

    def create_additional_folders(self) -> None:
        """!
        Create additional folders.
        @return
        """
        all_folders = {
            self.additional_dir: self.settings.additional_folder,
            self.annotations_dir: self.settings.annotations_folder,
            self.result_dir: self.settings.result_folder,
            self.models_dir: self.settings.models_folder,
            self.all_data_dir: self.settings.all_data_folder
        }

        for directory, folder in all_folders.items():
            try:
                os.makedirs(directory)
            except FileExistsError:
                logger.info(folder_exist.format(folder))

    def clear_data(self):
        """!
        Divide all data from dataset folder into annotations and images.
        @return Correct xml and images' files.
        """
        directories = [self.test_dir, self.train_dir]
        for directory in directories:
            self.remove_unreadable_images(directory)
            xml_names, image_names, extra = self.divide_xml_image(directory)
            _, _ = self.remove_files_without_pair(directory, xml_names, image_names, extra)

    @error_handler
    def move_data(self) -> None:
        """!
        Move data to the shared folder.
        @return
        """
        directories = [self.test_dir, self.train_dir]
        for directory in directories:
            file_names = os.listdir(directory)
            for file_name in file_names:
                if file_name.endswith(self.settings.allowed_extensions) or file_name.endswith('xml'):
                    shutil.copy(os.path.join(directory, file_name), self.all_data_dir)

    def run(self) -> None:
        """! Run data preparation. """
        self.create_additional_folders()
        self.clear_data()
        self.move_data()