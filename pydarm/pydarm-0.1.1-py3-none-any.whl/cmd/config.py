from . import _util
from ._util import logger


def add_args(parser):
    _util.add_model_option(parser)


def main(args):
    """edit and maintain config files

    """
    logger.error("not implemented!")
