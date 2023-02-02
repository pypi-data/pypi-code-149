import click

from semiotic_tricks_data_loader.config import DEFAULT_LOGGER
from semiotic_tricks_data_loader.data_loader import DataLoader
from semiotic_tricks_data_loader.utils.command_utils import (
    GroupWithCommandOptions,
    PythonLiteralOption,
)
from semiotic_tricks_data_loader.utils.utils import get_version

__description_field_path_in_commands = """
Name folders with deep
For example folder structure
├── file_1
├── file_2
│
├── folder_1
│   ├── folder_1_1
│   │   ├── file_1_1_1
│   │   └── file_1_1_2
│   │
│   └── folder_1_2
│       └── file_1_2_1
│
└── folder_2
    └── file_2_1

>>> `get`
<<< files: [file_1, file_2], folders:[folder_1, folder_2]

>>> `get -p folder_1`
<<< files: [] folders: [folder_1_1, folder_1_2]

>>> `get -p "folder_1 folder_1_1"`
<<< files: [file_1_1_1, file_1_1_2] folders: []

"""


@click.group(
    help="Utility for generating project documentation from docstrings",
    cls=GroupWithCommandOptions,
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option(
    "-v",
    "--version",
    "version",
    is_flag=True,
    required=False,
    default=False,
    help="Get library version",
    type=bool,
)
# @click.option(
#     "-g",
#     "--get",
#     "get",
#     is_flag=True,
#     required=False,
#     default=False,
#     help="Get allowed wiles",
#     type=bool,
# )
@click.pass_context
def entry_point(ctx, version):
    if version:
        print("Semiotic Tricks Data Loader Version:", get_version())


@entry_point.command(
    "get",
    help="To get allowed files by path in lfs storage",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option(
    "-p",
    "--path",
    "path",
    # show_default=True,
    required=False,
    default=[],
    help=__description_field_path_in_commands,
    type=list[str],
    cls=PythonLiteralOption,
)
def get_allowed_files(path):
    dl = DataLoader(is_delete_folder_with_same_name=True)
    files, folders = dl.get_paths(paths=path)
    DEFAULT_LOGGER.info("Files: %s", str(files))
    DEFAULT_LOGGER.info("Folders: %s", str(folders))


@entry_point.command(
    "load",
    help="Load file by path",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option(
    "-p",
    "--path",
    "path",
    required=False,
    default=[],
    help=__description_field_path_in_commands,
    type=list[str],
    cls=PythonLiteralOption,
)
@click.option(
    "-p2s",
    "--path2save",
    "path_to_save",
    required=False,
    default=None,
    help="Path to save",
    type=str,
)
@click.option(
    "-o",
    "--overwrite",
    "is_overwrite",
    required=False,
    default=False,
)
def load_file(path, path_to_save, is_overwrite):
    dl = DataLoader(is_delete_folder_with_same_name=True)
    saved_file = dl.load_file(
        paths=path, path_to_save=path_to_save, is_overwrite=is_overwrite
    )
    DEFAULT_LOGGER.info("File saved. Path to file: %s", str(saved_file))


if __name__ == "__main__":
    entry_point()
