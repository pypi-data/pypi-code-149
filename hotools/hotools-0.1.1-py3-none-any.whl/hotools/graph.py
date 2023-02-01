"""Create a graph
"""
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def _plot(plt: plt, filename: Any):
    if filename == "":
        plt.show()
    else:
        if isinstance(filename, str):
            path = Path(filename)
        elif isinstance(filename, Path):
            path = filename
        else:
            raise NotImplementedError()
        path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(str(path))


def draw_line_graph(x: list, y: list, ylim=[], yscale_log=False, labels=[], title="", filename=""):
    y_np = np.array(y)
    if y_np.ndim == 1:
        y_np = y_np[np.newaxis, :]
    elif y_np.ndim != 2:
        raise ValueError(f"A dimension of Y is {y_np.ndim}. It must be 1 or 2.")

    if len(labels) > 0 and len(labels) != y_np.shape[0]:
        raise ValueError(f"A number of Y {y_np.ndim} and a number of labels{len(labels)} are not the same value."
                         "It must be the same value.")

    plt.cla()
    if len(labels) > 0:
        for y, l in zip(y_np, labels):
            plt.plot(x, y, label=l)
    else:
        for y in y_np:
            plt.plot(x, y)

    if len(ylim) == 2:
        plt.ylim(ylim)
    plt.title(title)
    plt.grid()
    if yscale_log:
        plt.yscale("log")
    if y_np.ndim > 1 and len(labels) > 0:
        plt.legend()

    _plot(plt, filename)
