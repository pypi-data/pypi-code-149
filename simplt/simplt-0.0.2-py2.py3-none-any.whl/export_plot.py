"""Exports a plot/image to a file."""
import os

from typeguard import typechecked


@typechecked
def create_target_dir_if_not_exists(some_path: str) -> None:
    """

    :param path:
    :param new_dir_name:

    """
    if not os.path.exists(some_path):
        os.makedirs(some_path)
    if not os.path.exists(some_path):
        raise Exception(f"Error, path={some_path} did not exist.")
