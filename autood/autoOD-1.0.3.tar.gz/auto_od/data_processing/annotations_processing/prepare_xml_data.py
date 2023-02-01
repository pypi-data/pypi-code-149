import errno
import os
import xml.etree.ElementTree
from pathlib import Path
from typing import Dict, List

from auto_od.core.logger import logger
from auto_od.core.settings import Settings
from auto_od.utils.info_messages import file_deleted, xml_deleting


class PrepareXml:
    def __init__(self, directory: str, config_path: str):
        super().__init__()
        self.settings = Settings(config_path=config_path)
        self.directory = os.path.join(self.settings.path_to_work_dir, directory)
        if not os.path.isdir(self.directory):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.directory)

        self.xml_files = sorted(Path(self.directory).glob('*.xml'))

    def is_delete_false(self, values: List[str]) -> None:
        """!
        Delete tag <object>.
        @param values: Labels' list to delete.
        @return
        """
        for i in self.xml_files:
            tree = xml.etree.ElementTree.parse(i)
            root = tree.getroot()
            cnt = 0
            for item in root.findall('object'):
                cnt += 1
                if item.find('.//name').text in values:
                    removing_obj = str(item.find('.//name').text)
                    root.remove(item)
                    logger.info(xml_deleting.format(i, removing_obj))
            tree.write(i) if cnt > 1 else os.remove(i)

    def is_delete_true(self, values: List[str]) -> None:
        """!
        Delete the whole file with extra object.
        @param values: Labels' list to delete.
        @return
        """
        to_delete = []
        for i in self.xml_files:
            tree = xml.etree.ElementTree.parse(i)
            root = tree.getroot()
            for item in root.findall('object'):
                if item.find('.//name').text in values:
                    to_delete.append(i)
        for file in set(to_delete):
            os.remove(file)
            logger.info(file_deleted.format(file))

    def remove_extra_objects(self, values: List[str], is_delete: bool = True) -> None:
        """!
        Remove extra tags <object> from annotations.
        @param values: Labels' list to delete.
        @param is_delete: True -- delete the whole file with extra object. False -- delete tag <object>.
        @return
        """
        if not is_delete:
            self.is_delete_false(values)
        else:
            self.is_delete_true(values)

    def change_labels_name(self, replace_val: Dict[str]) -> None:
        """!
        Replace values from dict keys with values from dict values inside annotations' tag <object>.
        @param replace_val: key - value to replace, value - required value.
        @return
        """
        for i in self.xml_files:
            for key, value in replace_val.items():
                tree = xml.etree.ElementTree.parse(i)
                root = tree.getroot()
                for item in root.findall('object'):
                    if item.find('.//name').text == key:
                        item.find('.//name').text = value
                tree.write(i)

    def add_extension(self, real_extension: str, future_extension: str) -> None:
        """!

        @param real_extension:
        @param future_extension:
        """
        for i in self.xml_files:
            tree = xml.etree.ElementTree.parse(i)
            root = tree.getroot()
            root.find('filename').text = root.find('filename').text.replace(real_extension, '') + future_extension
            tree.write(i)

    def change_filename(self):
        # для себя
        for i in self.xml_files:
            tree = xml.etree.ElementTree.parse(i)
            root = tree.getroot()
            print(str(i).split('/')[-1].split('.')[0] + '.jpg')
            var = str(i).split('/')[-1].split('.')[0] + '.jpg'
            root.find('filename').text = var
            # root.find('filename').text = root.find('filename').text.replace(real_extension, '') + future_extension
            tree.write(i)

