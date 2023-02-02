import numpy as np


def vectorize_mapping(mapping_fn):
    def go(x):
        if x.ndim > 1:
            return np.apply_along_axis(mapping_fn, -1, x)
        else:
            return mapping_fn(x)
    return go

""" Schlumbup
[:::= //fn
    f{x-y-z} |==>> stdkwds.main::outwrite{{[[x`-`y]]`+`1`*`[[z<<~f~>>]]}}

<<:::~= \\stdwkds.fn::multilnfn
    f{x-y} |===>>)
        : stdkwds.main::outwrite{{...}}
        : stdkwds.main::outwrite{{...}}
        : stdkwds.main::outwrite{{...}}
        >> resstck<<~~0~>>
"""

IDENTITY = lambda x: x

def EQUALS(index_groups):
    def go(x):
        res = ''
        for ixs in index_groups:
            k = len(ixs)
            s = x[ixs].sum()
            if s == 0:
                res += '0'
            elif s == k:
                res += '1'
            else:
                res += '*'
        return res
    return go