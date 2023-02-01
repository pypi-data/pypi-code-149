"""@package docstring
Documentation for this module.

More details.
"""

import errno
import os
import random
import shutil
from typing import Any, Generator, List, Tuple

from auto_od.core.logger import logger
from auto_od.data_processing.dataset_processing.base import BasePrepareData
from auto_od.utils.decorators import error_handler
from auto_od.utils.info_messages import (file_not_ex, folder_exist,
                                         folder_not_ex)


class PrepareDataAll(BasePrepareData):
    def __init__(self, config_path: str):
        super().__init__(config_path=config_path)
        if not os.path.isdir(self.settings.dataset_dir):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.settings.dataset_dir)
        self.train_set_percent: float = self.settings.train_set_percent
        self.test_dir: str = os.path.join(self.settings.dataset_dir, self.settings.test_folder)
        self.train_dir: str = os.path.join(self.settings.dataset_dir, self.settings.train_folder)
        self.all_data_dir: str = os.path.join(self.settings.dataset_dir, self.settings.all_data_folder)

    def create_additional_folders(self) -> None:
        """!
        Create test, train, additional folders.
        @return
        """
        all_folders = {
            self.train_dir: self.settings.train_folder,
            self.test_dir: self.settings.test_folder,
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

    def clear_data(self) -> Tuple[List[str], List[str]]:
        """!
        Divide all data from dataset folder into annotations and images.
        @return Correct xml and images' files.
        """
        self.remove_unreadable_images(self.settings.dataset_dir)
        xml_names, image_names, extra = self.divide_xml_image(self.settings.dataset_dir)
        xml_names, image_names = self.remove_files_without_pair(self.settings.dataset_dir, xml_names,
                                                                image_names, extra)

        return xml_names, image_names

    def move_files(self, sample: Generator[str, Any, None], folder: str) -> None:
        """!
        Move divided files into train and test folders.
        @param sample: Moving data
        @param folder: Folder for data
        @return
        """

        folder = os.path.join(self.settings.dataset_dir, folder)
        if not os.path.isdir(folder):
            logger.info(folder_not_ex.format(folder))
            raise KeyError

        for name in sample:
            try:
                shutil.copy(os.path.join(self.settings.dataset_dir, name), folder)
                print('name', name, ' folder', folder)
            except FileNotFoundError:
                logger.info(file_not_ex.format(os.path.join(self.settings.dataset_dir, name)))

    def divide_test_and_train(self) -> None:
        """!
        Divide the dataset into test and train samples.
        @return
        """
        xmls, images = self.clear_data()
        xmls, images = sorted(xmls), sorted(images)
        shuffle_list = [[jpg, xml] for jpg, xml in zip(images, xmls)]
        if self.settings.is_shuffle:
            random.shuffle(shuffle_list)

        images_res, xml_res = [], []
        for element in shuffle_list:
            images_res.append(element[0])
            xml_res.append(element[1])

        split = int(self.train_set_percent * len(images_res))

        image_train = (idx for idx in images_res[:split])
        xml_train = (idx for idx in xml_res[:split])

        image_test = (idx for idx in images_res[split:])
        xml_test = (idx for idx in xml_res[split:])

        samples = {
            image_train: self.settings.train_folder, image_test: self.settings.test_folder,
            xml_train: self.settings.train_folder, xml_test: self.settings.test_folder
        }
        for sample, folder in samples.items():
            self.move_files(sample, folder)

    @error_handler
    def move_data(self) -> None:
        """!
        Move data to the shared folder.
        @return:
        """
        file_names = os.listdir(self.settings.dataset_dir)
        for file_name in file_names:
            if file_name.endswith(self.settings.allowed_extensions) or file_name.endswith('xml'):
                shutil.move(os.path.join(self.settings.dataset_dir, file_name), self.all_data_dir)

    def run(self) -> None:
        """! Run data preparation. """
        self.create_additional_folders()
        self.divide_test_and_train()
        self.move_data()
