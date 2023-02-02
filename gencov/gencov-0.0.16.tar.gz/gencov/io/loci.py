import math
import os
import re

from .config import CACHE, BIN_SIZE, DEFAULT_VALUE
from .sequence import get_sequence_reader
from .signal import get_signal_reader
from .util import \
    DiskCache, \
    filter_rows, \
    group_rows_by, \
    infer_format_from_path, \
    LazyImport, \
    read_csv, \
    sample_rows, \
    set_columns_types, \
    write_csv

pd = LazyImport("pandas")


class Loci:

    def __init__(self, header, loci, origin=None, chr_col="chr"):
        self.header = header
        self.loci = loci
        self.origin = origin
        self.chr_col = chr_col

    @classmethod
    def read_file(cls, path, format=None, **read_kargs):
        format = format or infer_format_from_path(path)
        if format in ("csv", "tsv", "txt"):
            return cls.read_csv(path, **read_kargs)
        if format[:3] in ("xls", "ods"):
            return cls.read_excel(path, **read_kargs)
        if format == "bed":
            return cls.read_bad(path, **read_kargs)
        raise ValueError(f"unrecognized file format: {format} for {path}")

    @classmethod
    def read_csv(cls, path, delimiter="infer"):
        loci, header = read_csv(path, delimiter=delimiter, header=True)
        return cls(header, loci, origin=os.path.basename(path))

    @classmethod
    def read_excel(cls, path, sheet=None):
        loci = pd.read_excel(path, sheet_name=sheet)
        header = loci.columns.tolist()
        loci = loci.values.tolist()
        return cls(header, loci, origin=os.path.basename(path))

    @classmethod
    def read_bed(cls, path, header=None):
        loci = read_csv(path, delimiter="\t", header=False)
        header = header or [
            "chr", "start", "end", "name", "score", "strand",
            "thick_start", "thick_end", "item_rgb",
            "block_count", "block_sizes", "block_starts"]
        header = header[:len(loci[0])] if loci else header
        return cls(header, loci, origin=os.path.basename(path))

    @classmethod
    def read_coordinates(cls, coordinates):
        header = ["chr", "start", "end"]
        parser = re.compile(r"^([^:]+):([^-]+)-(.+)$")
        loci = [
            list(parser.match(coordinate).groups())
            for coordinate in coordinates.split("/")]
        return cls(header, loci)

    def write_file(self, path, format=None, **write_kargs):
        format = format or infer_format_from_path(path)
        if format in ("csv", "tsv", "txt"):
            if format in ("tsv", "txt"):
                write_kargs.setdefault("delimiter", "\t")
            return self.write_csv(path, **write_kargs)
        if format[:3] in ("xls", "ods"):
            return self.write_excel(path, **write_kargs)
        if format == "bed":
            return self.write_bed(path, **write_kargs)
        raise ValueError(f"unrecognized file format: {format} for {path}")

    def write_csv(self, path, delimiter=","):
        write_csv(path, self.loci, delimiter=delimiter, header=self.header)

    def write_excel(self, path, sheet="data"):
        data = pd.DataFrame(self.loci, columns=self.header)
        data.to_excel(path, sheet_name=sheet, index=False)

    def write_bed(self, path, header=None):
        header = header or [
            "chr", "start", "end", "name", "score", "strand",
            "thick_start", "thick_end", "item_rgb",
            "block_count", "block_sizes", "block_starts"]
        for index, key in enumerate(header):
            if key not in self.header:
                header = header[:index]
                break
        write_csv(path, self.loci, delimiter="\t")

    def error(self, message, error_type=RuntimeError, raise_error=True):
        origin = f" in {self.origin}" if self.origin else ""
        error = error_type(f"{message}{origin}")
        if raise_error:
            raise error
        return error

    def set_col(self, key, values, replace=True):
        if key in self.header:
            if not replace:
                self.error(f"column {key} already specified")
            index = self.header.index(key)
            for row, value in zip(self.loci, values):
                row[index] = value
        else:
            self.header.append(key)
            for row, value in zip(self.loci, values):
                row.append(value)

    def get_col_index(self, key):
        try:
            index = self.header.index(key)
        except Exception:
            self.error(f"column {key} not found")
        return index

    def get_col(self, key):
        index = self.get_col_index(key)
        try:
            values = [row[index] for row in self.loci]
        except Exception:
            self.error(f"column {key} incomplete")
        return values
    
    def clean_chr(self):
        regex = re.compile(r"^(chr)?(\d+|x|y)$", re.I)
        chr_ids = self.get_col(self.chr_col)
        self.loci = [
            row
            for chr_id, row in zip(chr_ids, self.loci)
            if regex.match(chr_id)]
    
    def set_types(self, types):
        set_columns_types(self.loci, types, header=self.header)

    def filter(self, key, value, mode="==", reverse=False):
        self.loci = filter_rows(self.loci, self.get_col_index(key), value, mode, reverse)
    
    def sample(self, to, down=True, up=True, order=True, seed=None):
        self.loci = sample_rows(self.loci, to, down, up, order, seed)

    def group_by(self, key):
        groups = group_rows_by(self.loci, self.get_col_index(key))
        groups = {
            ref_value: Loci(self.header, loci, origin=self.origin)
            for ref_value, loci in groups.items()}
        return groups


class LociDataReader:

    def __init__(self, chr_ids, starts, ends, strands=None, cache=CACHE):
        self.chr_ids = list(chr_ids)
        self.starts = list(starts)
        self.ends = list(ends)
        self.strands = None if strands is None else list(strands)
        self.cache = cache
        self.sorting_indices = None
        if self.cache is not None:
            locations = [
                [str(chr_id), int(start), int(end), index]
                for index, (chr_id, start, end) in
                enumerate(zip(self.chr_ids, self.starts, self.ends))]
            for index in range(2, -1, -1):
                locations.sort(key=lambda location: location[index])
            self.chr_ids, self.starts, self.ends, self.sorting_indices = zip(*locations)
            cache_data = [self.chr_ids, self.starts, self.ends]
            self.cache = DiskCache(self.cache, "loci_data", cache_data)

    @classmethod
    def from_starts(cls, chr_ids, starts, span, cache=CACHE):
        starts = list(starts)
        ends = (start + span for start in starts)
        return cls(chr_ids, starts, ends, cache)

    @classmethod
    def from_centers(cls, chr_ids, centers, span, cache=CACHE):
        centers = list(centers)
        left_span = math.floor(span / 2)
        right_span = math.ceil(span / 2)
        starts = (center - left_span for center in centers)
        ends = (center + right_span for center in centers)
        return cls(chr_ids, starts, ends, cache)

    def read_signal(self, path, bin_size=BIN_SIZE, default_value=DEFAULT_VALUE):
        if self.cache:
            cache_path = self.cache.get_path([path, bin_size, default_value])
            if self.cache.exists(cache_path):
                return self.cache.read(cache_path)
        type, reader_class = get_signal_reader(path, return_type=True)
        arguments = [path, bin_size, default_value] if type == "bigwig" else [path, bin_size]
        with reader_class(*arguments) as reader:
            data = reader.read_loci_values(self.chr_ids, self.starts, self.ends)
        if self.cache is not None:
            self.cache.write(cache_path, data)
        if self.sorting_indices is not None:
            data = [data[index] for index in self.sorting_indices]
        if self.strands is not None:
            data = list(strand_loci_values(data, self.strands))
        return data

    def read_sequence(self, path):
        if self.cache:
            cache_path = self.cache.get_path([path])
            if self.cache.exists(cache_path):
                return self.cache.read(cache_path)
        reader_class = get_sequence_reader(path)
        with reader_class(path) as reader:
            data = reader.read_loci_sequence(self.chr_ids, self.starts, self.ends)
        if self.cache is not None:
            self.cache.write(cache_path, data)
        if self.sorting_indices is not None:
            data = [data[index] for index in self.sorting_indices]
        if self.strands is not None:
            data = list(strand_loci_values(data, self.strands))
        return data


def read_loci_signal(path, chr_ids, starts, ends, strands=None, bin_size=BIN_SIZE, default_value=DEFAULT_VALUE, cache=CACHE):
    reader = LociDataReader(chr_ids, starts, ends, strands=strands, cache=cache)
    return reader.read_signal(path, bin_size=bin_size, default_value=default_value)


def read_loci_sequence(path, chr_ids, starts, ends, strands=None, cache=CACHE):
    reader = LociDataReader(chr_ids, starts, ends, strands=strands, cache=cache)
    return reader.read_sequence(path)


def strand_loci_values(loci_values, strands, sense="+", antisense="-"):
    for values, strand in zip(loci_values, strands):
        if strand == antisense:
            values = reversed(values)
        elif strand != sense:
            raise ValueError(f"invalid strand: {strand} ({sense} or {antisense})")
        yield values
