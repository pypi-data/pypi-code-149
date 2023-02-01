import abc


class BasePrepareXml:
    @abc.abstractmethod
    def add_extension(self):
        pass

    @abc.abstractmethod
    def remove_extra_objects(self, values: list[str], is_delete: bool = True) -> None:
        pass

    @abc.abstractmethod
    def change_labels_name(self, replace_val: dict[str]) -> None:
        pass
