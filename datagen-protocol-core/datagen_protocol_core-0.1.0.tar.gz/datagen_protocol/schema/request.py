from typing import List, Union

from pydantic import BaseModel

import __version__ as __datagen_protocol_version__
from datagen_protocol.schema.hic.sequence import DataSequence
from datagen_protocol.schema.humans import HumanDatapoint


class DataRequest(BaseModel):
    __protocol_version__: str = __datagen_protocol_version__

    data: List[Union[DataSequence, HumanDatapoint]]
