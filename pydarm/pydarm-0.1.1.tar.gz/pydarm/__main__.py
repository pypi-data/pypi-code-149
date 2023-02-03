# Copyright (C) Jameson Rollins (2021)
#               Evan Goetz (2021)
#
# This file is part of pyDARM.
#
# pyDARM is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pyDARM is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# pyDARM. If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import signal
import logging
import argparse
from importlib import import_module

from . import __version__
from .cmd import CMDS, CMDError, logger


logger.setLevel(os.getenv('LOG_LEVEL', 'INFO').upper())
formatter = logging.Formatter('%(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

########################################

parser = argparse.ArgumentParser(
    prog='pydarm',
    description="""aLIGO calibration interface

""",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    '--version', '-v', action='version', version=__version__)
subparsers = parser.add_subparsers(
    metavar='COMMAND',
)


def add_subcommand(name):
    """helper function for adding subcommand to the parser from cmd modules

    The name provided should be the name of a module in the `cmd`
    sub-package.  Each module should include an `add_args` function
    for adding argparse arguments to the argparse parser, and a `main`
    function with the main subcommand logic.  The docstring of the
    main function will be the doc for the sub-command.

    """
    mod = import_module(f'.{name}', 'pydarm.cmd')
    func = mod.main
    sp = subparsers.add_parser(
        name,
        help=func.__doc__.splitlines()[0],
        description=func.__doc__.strip(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sp.set_defaults(func=func)
    mod.add_args(sp)
    return sp


def main():
    for name in CMDS:
        add_subcommand(name)
    args = parser.parse_args()
    if 'func' not in args:
        parser.print_help()
        parser.exit()
    func = args.func
    del args.func
    logger.debug(args)
    func(args)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    try:
        main()
    except CMDError as e:
        sys.exit(f"ERROR: {e}")
