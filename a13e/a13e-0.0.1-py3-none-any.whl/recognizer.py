import abc
from pathlib import Path
from typing import List

from a13e.tag import SongData


class RecognizeResult(SongData):
    url: str
    recognizer_name: str


class BaseRecognizer(abc.ABC):
    """Abstract base recognizer.

    Inherit this abstract base class and decorate with the PluginManager.register
    decorator to 'enable' this recognizer. A recognizer should only correspond to one API platform

    Methods:
        recognize: The method actually called by the external function.

    Attributes:
        name: It is used to distinguish the recognizers.
        The name is generally the API platform used and uses Pascal nomenclature.
    """

    @abc.abstractmethod
    def recognize(self, audio_fp: Path, **kwargs) -> List[RecognizeResult]:
        """The method actually called by the external function.

        Args:
            audio_fp: Audio file path.
            **kwargs: Recognizer extra parameters, if needed

        Returns:
            List of recognition results.
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """It is used to distinguish the recognizers.
        The name is generally the API platform used and uses Pascal nomenclature."""
        raise NotImplementedError


