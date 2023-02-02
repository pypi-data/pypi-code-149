#!/usr/bin/env python3
"""
Generate opt file from the information entered in the DIA,
typically returning the vendor HV.

Usage:
    km3dia_generate_opt DOM_UPI FILENAME
    km3dia_generate_opt (-h | --help)
    km3dia_generate_opt --version

Options:
    DOM_UPI       DOM UPI in DIA DB (can be temporary one)
    FILENAME      Output OPT file
    -h --help     Show this screen.

"""
from docopt import docopt
import km3dia


def main():
    args = docopt(__doc__, version=km3dia.version)
    DOM_UPI = args["DOM_UPI"]
    output_file = args["FILENAME"]
    print(f"DOM UPI : {DOM_UPI}")
    print(f"\t OPT file will be saved here : {output_file}")
    km3dia.save_opt_file(DOM_UPI, output_file)


if __name__ == "__main__":
    main()
