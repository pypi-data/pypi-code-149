import itertools
import random
from pathlib import Path
from typing import Sequence, Tuple, List, TYPE_CHECKING

from requests import RequestException

from a13e.plugin import PluginRegister
if TYPE_CHECKING:
    from a13e.recognizer import RecognizeResult


def recognize(
        audio_fp: Path, name: Sequence[str] = (), **kwargs
) -> Tuple['RecognizeResult', ...]:
    """Call the recognize method of all registered recognizers and return the result tuple.

    Args:
        audio_fp: Audio file path.
        name: Pass a sequence of names to specify the recognizers to use.
        **kwargs: Recognizer extra parameters

    Returns:
        Recognition result tuple.
    """
    result: List[List['RecognizeResult']] = []
    for recognizer in PluginRegister.recognizers.values():
        if not name or recognizer.name in name:
            try:
                result.append(recognizer.recognize(audio_fp, **kwargs))
            except RequestException as e:
                print(e)
                continue
    return tuple(itertools.chain.from_iterable(result))


def random_recognize(audio_fp: Path, name: Sequence[str] = (), **kwargs) -> 'RecognizeResult':
    """Randomly returns one from recognition results."""
    return random.choice(recognize(audio_fp, name=name, **kwargs))

