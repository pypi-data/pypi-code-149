import numpy as np


def estimate_rank(mat, th = 0.9):
    _, S, _ = np.linalg.svd(mat)
    S = np.cumsum(S)
    threshold = th*S[-1]
    r = np.argmax(S > threshold)
    return r+1
