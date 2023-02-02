def interpolate_random_loci(chr_ids, locs, count, min_distance=10000):
    error_message = \
        f"failed to interpolate {count} random loci " \
        f"at a min distance of {min_distance} bp " \
        f"using {min(len(chr_ids), len(locs))} input loci as bounds " \
        f"(likely because of an input loci count too low)"
    ranges = dict()
    for chr_id, loc in zip(chr_ids, locs):
        try:
            chr_range = ranges[chr_id]
            if loc > chr_range["max"]:
                chr_range["max"] = loc
            elif loc < chr_range["min"]:
                chr_range["min"] = loc
        except KeyError:
            chr_range = dict(chr_id=chr_id, min=loc, max=loc)
            ranges[chr_id] = chr_range
    for chr_id, chr_range in ranges.items():
        chr_range["span"] = chr_range["max"] - chr_range["min"]
    ranges = list(ranges.values())
    ranges.sort(key=lambda chr_range: chr_range["span"], reverse=True)
    total_span = sum(chr_range["span"] for chr_range in ranges)
    if not total_span:
        raise RuntimeError(error_message)
    for chr_range in ranges:
        chr_range["count"] = int(round(chr_range["span"] / total_span * count))
    ranges = [chr_range for chr_range in ranges if chr_range["count"]]
    if ranges and sum(chr_range["count"] for chr_range in ranges) < count:
        ranges[0]["count"] += count - sum(chr_range["count"] for chr_range in ranges)
    else:
        while sum(chr_range["count"] for chr_range in ranges) > count:
            if ranges[-1]["count"] > 1:
                ranges[-1]["count"] -= 1
            else:
                del ranges[-1]
    if count and not ranges:
        raise RuntimeError(error_message)
    out_chr_ids, out_locs = [], []
    for chr_range in ranges:
        start, end, n = chr_range["min"], chr_range["max"], chr_range["count"] + 2
        step = (end - start) / (n - 1)
        if int(step) < min_distance:
            raise RuntimeError(error_message)
        chr_locs = [int(start + step * i) for i in range(n)][1:-1]
        out_chr_ids += [chr_range["chr_id"]] * chr_range["count"]
        out_locs += chr_locs
    return out_chr_ids, out_locs
