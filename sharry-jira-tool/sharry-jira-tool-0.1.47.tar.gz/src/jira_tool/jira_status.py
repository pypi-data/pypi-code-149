import pathlib
from json import loads

HERE = pathlib.Path(__file__).resolve().parent
ASSETS = HERE / "assets"

__all__ = ["get_no_need_sort_statuses"]


def get_no_need_sort_statuses() -> "list[str]":
    with open(
        file=ASSETS / "jira_status_mapping.json", mode="r"
    ) as status_mapping_file:
        try:
            raw_data = loads(status_mapping_file.read())

            return [item for item in raw_data["StatusesNoNeedAnticipateSort"]]
        finally:
            status_mapping_file.close()
