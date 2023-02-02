from json import dump as _dump
from json import load as _load
from pathlib import Path
from typing import Any, Optional


def mkdir(path: str) -> None:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)


def rmdir(path: str) -> None:
    p = Path(path)
    p.rmdir()


def json_read(path: str, /) -> Optional[Any]:
    p = Path(path)
    if not p.exists():
        return None
    with open(p, "rt", encoding="UTF-8") as fp:
        return _load(fp)


def json_write(path: str, /, data: Any, *, indent: Optional[int] = 4) -> None:
    p = Path(path)
    with open(p, "wt", encoding="UTF-8") as fp:
        _dump(data, fp, indent=indent)
