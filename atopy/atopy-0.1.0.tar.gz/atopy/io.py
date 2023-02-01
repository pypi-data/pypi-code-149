from json import dump as _dump
from json import load as _load
from os import makedirs as _makedirs
from pathlib import Path
from typing import Any, Optional


def makedirs(path_dir: str) -> None:
    _makedirs(path_dir, exist_ok=True)


def json_read(fpath: str, /) -> Optional[Any]:
    if not Path(fpath).exists():
        return None
    with open(fpath, "rt", encoding="UTF-8") as fp:
        return _load(fp)


def json_write(fpath: str, /, data: Any, *, indent: Optional[int] = 4) -> None:
    with open(fpath, "wt", encoding="UTF-8") as fp:
        _dump(data, fp, indent=indent)
