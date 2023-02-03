from typing import Optional
from pathlib import Path


def path_exists(__path: Optional[str]):
    return __path is not None and Path(__path).exists()


def read_text(__path: Optional[str]):
    return Path(__path).read_text()


def write_text(path: Optional[str], data: str):
    Path(path).write_text(data=data)
