import os
import argparse
import subprocess

from ._const import (
    CAL_CONFIG_ROOT,
    CAL_TEMPLATE_ROOT,
    CAL_MEASUREMENT_ROOT,
)
from .measurement_set import (
    list_all_measurement_sets,
    MeasurementSet,
)


def shell_list(directory):
    """long list contents of directory"""
    subprocess.run(f"ls -Alth --full-time {directory}", shell=True)
    # subprocess.run(f"find {directory} -ls", shell=True)


def iterate_dir(path):
    """iterate over files in a directory

    filters out directories and files that end with '~'

    """
    for f in sorted(os.listdir(path)):
        if os.path.isdir(os.path.join(path, f)):
            continue
        if f[-1] == '~':
            continue
        yield f


def print_path(root, name, full=False):
    """print file name or path"""
    if full:
        path = os.path.join(root, name)
    else:
        path = name
    print(' ', path)


def add_args(parser):
    parser.add_argument(
        '--mset', '-m', metavar="MEAS_ID", nargs='?', default=argparse.SUPPRESS,
        help="list measurement set files for measurement set ID, or 'last' if none specified")
    parser.add_argument(
        '--full', '-f', action='store_true',
        help="list files with full path")


def main(args):
    """list config and measurement files, or measurement set contents

    """
    if hasattr(args, 'mset'):
        mset = MeasurementSet(args.mset)
        for f in iterate_dir(mset.path):
            print_path(mset.path, f, full=args.full)
        return

    print(f"config: {CAL_CONFIG_ROOT}")
    for f in iterate_dir(CAL_CONFIG_ROOT):
        print_path(CAL_CONFIG_ROOT, f, full=args.full)

    print(f"templates: {CAL_TEMPLATE_ROOT}")
    for f in iterate_dir(CAL_TEMPLATE_ROOT):
        print_path(CAL_TEMPLATE_ROOT, f, full=args.full)

    print(f"measurements: {CAL_MEASUREMENT_ROOT}")
    for meas_id in list_all_measurement_sets():
        print_path(CAL_MEASUREMENT_ROOT, meas_id, full=args.full)
