import argparse, os, re
from pbandplot import plots, readdata

def main():
    parser = argparse.ArgumentParser(description='Plot the phonon band structure from phonopy result.',
                                     epilog='''
Example:
pbandplot -i band.dat -p pband.png
''',
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-v', "--version",  action="version", version="pbandplot 0.0.1.3")
    parser.add_argument('-k', "--kpoints",  default=[], type=str.upper, nargs='+')
    parser.add_argument('-s', "--size",     type=int,   nargs=2)
    parser.add_argument('-b', "--broken",   type=float, nargs=3)
    parser.add_argument('-y', "--vertical", type=float, nargs=2, help="vertical axis")
    parser.add_argument('-i', "--input",    default="BAND.dat", type=str, help="plot figure from .dat file")
    parser.add_argument('-o', "--output",   default="BAND.png", type=str, help="plot figure filename")
    parser.add_argument('-d', "--dos",      type=str, help="plot Phonon DOS from .dat file")
    parser.add_argument('-e', "--elements", type=str, nargs='+', help="PDOS labels")

    args = parser.parse_args()

    labels = [re.sub("'|‘|’", '′', re.sub('"|“|”', '″', re.sub('^GA[A-Z]+$|^G$', 'Γ', i))) for i in args.kpoints]

    if os.path.exists(args.input):
        arr, fre, ticks = readdata.bands(args.input)
        if args.dos is None:
            if args.broken is None:
                plots.Nobroken(arr, fre, ticks, args.output, labels, args.size, args.vertical)
            else:
                plots.Broken(arr, fre, ticks, args.output, labels, args.size, args.vertical, args.broken)
        elif os.path.exists(args.dos):
            darr, dele = readdata.dos(args.dos)
            if args.broken is None:
                plots.NobrokenWd(arr, fre, ticks, args.output, labels, args.size, args.vertical, darr, dele, args.elements)
            else:
                plots.BrokenWd(arr, fre, ticks, args.output, labels, args.size, args.vertical, args.broken, darr, dele, args.elements)

