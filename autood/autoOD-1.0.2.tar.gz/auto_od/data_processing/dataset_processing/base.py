import abc
import glob
import itertools
import os
from typing import Tuple, List
import cv2
from skimage import io

from auto_od.core.logger import logger
from auto_od.core.settings import Settings
from auto_od.utils.info_messages import (extra_file, file_deleted,
                                         unreadable_file)


class BasePrepareData:
    def __init__(self, config_path: str):
        self.settings = Settings(config_path=config_path)

        self.additional_dir: str = os.path.join(self.settings.path_to_work_dir, self.settings.additional_folder)
        self.annotations_dir: str = os.path.join(self.additional_dir, self.settings.annotations_folder)
        self.models_dir: str = os.path.join(self.additional_dir, self.settings.models_folder)
        self.result_dir: str = os.path.join(self.additional_dir, self.settings.result_folder)

    @abc.abstractmethod
    def create_additional_folders(self) -> None:
        pass

    @abc.abstractmethod
    def clear_data(self, **kwargs):
        pass

    @abc.abstractmethod
    def move_data(self, **kwargs) -> None:
        pass

    def remove_unreadable_images(self, directory: str) -> None:
        """!
        Check if image is unreadable and delete it.
        @return
        """
        files = [glob.glob(directory + '/*.' + extension) for extension in self.settings.allowed_extensions]
        files = list(itertools.chain(*files))

        for i in range(len(files)):
            try:
                _ = io.imread(files[i])
                _ = cv2.imread(files[i])
            except Exception as _:
                logger.info(unreadable_file.format(files[i]))
                os.remove(files[i])
                logger.info(file_deleted.format(files[i]))

    def divide_xml_image(self, directory: str) -> Tuple[List[str], List[str], List[str]]:
        """!
        Divide all data from directory into annotations and images;
        @param directory: Directory
        @return
        """
        xml_names, image_names, extra = [], [], []
        for entry in os.listdir(directory):
            if entry.endswith('xml'):
                xml_names.append(entry)
            elif entry.endswith(self.settings.allowed_extensions):
                image_names.append(entry)
            elif not os.path.isdir(os.path.join(directory, entry)):
                extra.append(entry)
        return xml_names, image_names, extra

    @staticmethod
    def remove_files_without_pair(directory: str, xmls: List[str], images: List[str],
                                  extra_files: List[str]) -> Tuple[List[str], List[str]]:
        """!
        Handling cases when an image or annotation does not have a corresponding file.
        Right case: (1.jpg, 1.xml)
        Wrong case: (1.jpg, None)/(None, 1.xml).
        @param directory: Directory
        @param xmls: Images' annotations
        @param images: Images
        @param extra_files: Any extra files to delete (except directories)
        @return Correct xml and images' files.
        """
        xmls_prep = list(map(lambda x: x.split('.')[0], xmls))
        images_prep = list(map(lambda x: x.split('.')[0], images))
        intersection = list(set(xmls_prep) & set(images_prep))

        xmls_res = [i for i in xmls if i.split('.')[0] in intersection]
        images_res = [i for i in images if i.split('.')[0] in intersection]
        extra = list(set(xmls) - set(xmls_res)) + list(set(images) - set(images_res)) + extra_files

        if extra:
            logger.info(extra_file.format(', '.join(extra)))

        for file in extra:
            os.remove(os.path.join(directory, file))
            logger.info(file_deleted.format(os.path.join(directory, file)))

        return xmls_res, images_res


