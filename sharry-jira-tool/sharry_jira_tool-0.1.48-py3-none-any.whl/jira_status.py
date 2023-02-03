from json import loads
from pathlib import Path
from typing import Optional

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"

__all__ = ["get_no_need_sort_statuses"]


def get_no_need_sort_statuses(file: "Optional[str | Path]" = None) -> "list[str]":
    file_path: Optional[str | Path] = None
    if file is None:
        file_path = ASSETS / "jira_status_mapping.json"
    else:
        file_path = file

    with open(file=file_path, mode="r") as status_mapping_file:
        try:
            raw_data = loads(status_mapping_file.read())

            return [item for item in raw_data["StatusesNoNeedAnticipateSort"]]
        except Exception:
            raise ValueError(
                "The JSON file structure is invalid. Please check the documentation: https://github.com/SharryXu/jira-tool"
            )
        finally:
            status_mapping_file.close()
