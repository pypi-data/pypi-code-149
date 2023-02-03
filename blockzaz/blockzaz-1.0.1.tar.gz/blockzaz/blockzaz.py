from typing import Optional

from prefect.blocks.core import Block
from pydantic import SecretStr

class CubeJs(Block):
    urlCube: Optional[str] = None
    apiSecret: Optional[SecretStr] = None
    urlAtualizacao: Optional[str] = None