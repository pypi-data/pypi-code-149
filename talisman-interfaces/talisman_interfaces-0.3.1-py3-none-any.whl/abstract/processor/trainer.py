from abc import ABCMeta, abstractmethod
from typing import Dict, Generic, Iterable, Optional, Tuple, TypeVar, Union

from tdm.abstract.datamodel import AbstractTreeDocumentContent
from tdm.datamodel import TalismanDocument

from .processor import AbstractDocumentProcessor

_DocumentContent = TypeVar('_DocumentContent', bound=AbstractTreeDocumentContent)
_Processor = TypeVar('_Processor', bound=AbstractDocumentProcessor)


class AbstractTrainer(Generic[_Processor, _DocumentContent], metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def from_config(cls, config: dict):
        pass

    @abstractmethod
    def train(
            self,
            train_docs: Iterable[TalismanDocument[_DocumentContent]],
            dev_docs: Optional[Iterable[TalismanDocument[_DocumentContent]]] = None,
            *,
            pretrained_model: Optional[_Processor] = None
    ) -> Union[_Processor, Tuple[_Processor, Dict[str, float]]]:
        """Trains either model initialized in trainer constructor or a pretrained model given as an argument.
        If `dev_docs` is specified, model will be evaluated once fully trained and evaluation scores will be returned
        alongside with trained model."""
        pass
