import json
from pathlib import Path
from typing import Any


def dump_json(file_path: Path, data: Any) -> None:
    with file_path.open(mode="w+", encoding="utf-8") as f:
        return json.dump(data, f, ensure_ascii=False, indent=4)
