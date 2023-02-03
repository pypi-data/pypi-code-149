from ._const import (
    CAL_CONFIG_ROOT,
    CAL_DATA_ROOT,
)


def add_args(parser):
    pass


def main(args):
    """print environment and exit

    """
    print(f"CAL_CONFIG_ROOT: {CAL_CONFIG_ROOT}")
    print(f"CAL_DATA_ROOT  : {CAL_DATA_ROOT}")
