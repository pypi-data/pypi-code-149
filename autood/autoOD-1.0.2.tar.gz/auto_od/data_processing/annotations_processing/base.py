import abc
from typing import List, Dict


class BasePrepareXml:
    @abc.abstractmethod
    def add_extension(self):
        pass

    @abc.abstractmethod
    def remove_extra_objects(self, values: List[str], is_delete: bool = True) -> None:
        pass

    @abc.abstractmethod
    def change_labels_name(self, replace_val: Dict[str]) -> None:
        pass
