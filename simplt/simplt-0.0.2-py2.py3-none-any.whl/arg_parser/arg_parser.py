"""Parses CLI arguments that specify on which platform to simulate the spiking
neural network (SNN)."""
import argparse

from typeguard import typechecked


@typechecked
def parse_cli_args() -> argparse.Namespace:
    """Reads command line arguments and converts them into python arguments."""

    # Instantiate the parser
    parser = argparse.ArgumentParser(
        description="Optional description for arg parser"
    )

    parser.add_argument(
        "-d",
        "--delete-images",
        action="store_true",
        default=False,
        help=(
            "Delete the images in the (specified) output directory at start."
        ),
    )

    parser.add_argument(
        "-b",
        "--box-plot",
        action="store_true",
        default=False,
        help=("Create a box-plot based on your input data."),
    )

    parser.add_argument(
        "-l",
        "--line-plot",
        action="store_true",
        default=False,
        help=("Create a box-plot based on your input data."),
    )

    parser.add_argument(
        "-o",
        "--output-path",
        action="store",
        type=str,
        help=("Specify output path of graph and/or table file."),
    )

    parser.add_argument(
        "-t",
        "--latex-table",
        action="store_true",
        default=False,
        help=("Create a latex_table based on your input data."),
    )

    # Load the arguments that are given.
    args = parser.parse_args()
    return args
