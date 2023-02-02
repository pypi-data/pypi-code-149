from typing import Generator


def median_flow(hydrogram: list) -> tuple:
    hist = {}
    for d in hydrogram:
        bucket = int(d[1])
        hist[bucket] = hist.get(bucket, 0) + 1

    # import pdb; pdb.set_trace()
    l = len(hist) / 2
    c = 0
    for b in sorted(hist.keys()):
        if c + hist[b] > l:
            return b, int(hydrogram[c][0])

        c += hist[b]

    return 0, 0

def gen_hydrogram(
    hydrogram: list
) -> Generator[float, None, float]:
    t = 0
    r = tuple(float(v) for v in hydrogram.pop(0))
    median, mtime = median_flow(hydrogram)
    while True:
        if r[1] <= median and t >= mtime:
            yield median
        else:
            if t >= float(hydrogram[0][0]):
                r = tuple(float(v) for v in hydrogram.pop(0))
    
            if len(hydrogram) == 0:
                yield r[1]
                break
    
            yield r[1] + (float(hydrogram[0][1]) - r[1]) / (float(hydrogram[0][0]) - t)
            t += 1

    return 0

