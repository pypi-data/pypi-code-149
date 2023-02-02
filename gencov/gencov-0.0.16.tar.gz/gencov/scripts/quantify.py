import itertools
from os.path import basename, splitext
import sys
import json

from ..util import ArgumentParser
from ..io.loci import Loci
from ..cov_util import (
    parse_window_setting,
    get_windows_bounds,
    get_coverage_at_loci,
    parse_sample_setting,
    transform_coverage,
    sample_coverage,
    parse_average_setting,
    average_coverage)
from ..io import read_loci_signal
from ..config import DATA_SERVER_DIR


def main(raw_args):

    info = '''
quantify coverage at loci

arguments:
    -l --loci ::::: path to loci files (tsv, csv, bed or excel)
                    required
    -t --targets :: path to coverage files (bigwig or indexed bam)
                    required
    -w --window ::: coverage window as < center/left/right >
                    required (eg: summit/-2000/2001)
    --clean-chr ::: remove non standard chromosomes (mitochondrial, unlocalized
                    and unplaced sequences) using chromosomes ids
    -s --strand ::: consider strand using information in < column >
                    write strand if input is bed
                    strand not considered by default
    -b --bin-size : coverage bin size in base pairs (report one every x values)
                    binning is done before sampling
                    10 by default
    -d --default :: replace missing values (nan) by this value
                    write nan to keep missing values as missing
                    0 by default
    --transform ::: apply function to transform values with x as variable
                    eg, log10(x + 1)
                    none by default
    --sample :::::: output size as < row_count(/method) >
                    with row_count as all, integer
                    and method as nearest, area_mean/median/min/max/l2norm
                    all/nearest by default
    -a --average :: output averaging as < method >
                    with method as mean, sd, sem, quantile:number, l1norm, l2norm
                    mean by default
    -o --output ::: output file path (append to file if existing)
                    /dev/stdout by default
    -f --format ::: output format as raw, full or json
                    raw by default
'''

    if "-h" in raw_args or "--help" in raw_args:
        sys.stderr.write(info.strip() + "\n")
        return
        
    parser = ArgumentParser()
    parser.add_argument("-l", "--loci", nargs="+", required=True)
    parser.add_argument("-t", "--targets", nargs="+", required=True)
    parser.add_argument("-w", "--window", required=True)
    parser.add_argument("--clean-chr", action="store_true")
    parser.add_argument("-s", "--strand", default=None)
    parser.add_argument("-b", "--bin-size", type=int, default=10)
    parser.add_argument("-d", "--default", type=float, default=0)
    parser.add_argument("--transform", default=None)
    parser.add_argument("--sample", default="all/nearest")
    parser.add_argument("-a", "--average", default="mean")
    parser.add_argument("-o", "--output", default="/dev/stdout")
    parser.add_argument("-f", "--format", default="raw")
    args = parser.parse_args(raw_args)

    center, left, right = parse_window_setting(args.window)
    row_count, col_count, sample_method = parse_sample_setting(args.sample, col_count="all")
    average_method, average_args = parse_average_setting(args.average)
    result = []
    for loci_path in args.loci:
        if loci_path.startswith("//coordinates/"):
            loci = Loci.read_coordinates(loci_path[14:])
        else:
            loci = Loci.read_file(loci_path)
        if args.clean_chr:
            loci.clean_chr()
        loci.set_types({center: int})
        chr_ids = loci.get_col("chr")
        centers = loci.get_col(center)
        strands = None if args.strand is None else loci.get_col(args.strand)
        starts, ends = get_windows_bounds(centers, left, right, strands)
        for target_path in args.targets:
            if target_path.startswith("//data_server/"):
                target_path = f"{DATA_SERVER_DIR}/{target_path[14:]}"
            values = read_loci_signal(
                target_path, chr_ids, starts, ends,
                bin_size=args.bin_size,
                default_value=args.default,
                strands=strands)
            values = transform_coverage(values, args.transform, is_literal=True)
            values = sample_coverage(values, row_count, col_count, sample_method)
            signal = average_coverage(values, "columns", average_method, *average_args)
            result.append([loci_path, target_path, signal])

    if args.format in ["raw", "full"]:
        with open(args.output, "a") as file:
            output = [
                [splitext(basename(loci_path))[0], splitext(basename(target_path))[0], *signal]
                if args.format == "full" else signal
                for loci_path, target_path, signal in result]
            output = map(list, itertools.zip_longest(*output, fillvalue=""))
            for row in output:
                file.write("\t".join(str(value) for value in row) + "\n")
    elif args.format == "json":
        with open(args.output, "a") as file:
            output = [
                {"loci_path": loci_path, "target_path": target_path, "values": values}
                for loci_path, target_path, values in result]
            json.dump(output, file)
    else:
        raise ValueError(f"invalid output format: {args.format}")
        
    return result
