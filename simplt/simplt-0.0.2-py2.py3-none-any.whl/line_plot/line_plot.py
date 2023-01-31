"""File used to create and export plots and tables directly into latex. Can be
used to automatically update your results each time you run latex.

For copy-pastable examples, see:     example_create_a_table()
example_create_multi_line_plot()     example_create_single_line_plot()
at the bottom of this file.
"""
from typing import List

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import lines
from typeguard import typechecked


@typechecked
def example_create_multi_line_plot(
    output_dir: str, filename: str, extensions: List[str]
) -> None:
    """Example that creates a plot with multiple lines.

    Copy paste it in your own code and modify the values accordingly.
    """

    multiple_y_series = np.zeros((2, 2), dtype=int)
    # actually fill with data
    multiple_y_series[0] = [1, 2]
    lineLabels = [
        "first-line",
        "second_line",
    ]  # add a label for each dataseries
    single_x_series = [3, 5]

    plot_multiple_lines(
        extensions=extensions,
        filename=filename,
        label=lineLabels,
        legendPosition=0,
        output_dir=output_dir,
        x=single_x_series,
        x_axis_label="x-axis label [units]",
        y_axis_label="y-axis label [units]",
        y_series=multiple_y_series,
    )


# plot graphs
@typechecked
def plot_multiple_lines(
    extensions: List[str],
    filename: str,
    label: List,
    legendPosition: int,
    output_dir: str,
    x: List,
    x_axis_label: str,
    y_axis_label: str,
    y_series: np.ndarray,
) -> None:
    """

    :param x:
    :param y_series:
    :param x_axis_label:
    :param y_axis_label:
    :param label:
    :param filename:
    :param legendPosition:
    :param y_series:
    :param filename:
    """
    # pylint: disable=R0913
    # TODO: reduce 9/5 arguments to at most 5/5 arguments.
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Set line colours in plot object.
    set_cmap(plt, len(y_series[:, 0]))

    # Generate line types.
    lineTypes = generateLineTypes(y_series)

    # Geneterate lines.
    for i in range(0, len(y_series)):
        ax.plot(
            x,
            y_series[i, :],
            ls=lineTypes[i],
            label=label[i],
            fillstyle="none",
        )

    # configure plot layout
    plt.legend(loc=legendPosition)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    for extension in extensions:
        plt.savefig(f"{output_dir}/{filename}{extension}")
    plt.clf()
    plt.close()


# Generate random line colours
# Source: https://stackoverflow.com/questions/14720331/
# how-to-generate-random-colors-in-matplotlib
@typechecked
def set_cmap(
    some_plt: matplotlib.pyplot,
    nr_of_colours: int,
    name: str = "hsv",
) -> None:
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.

    :param n: param name:  (Default value = "hsv")
    :param name: Default value = "hsv")
    """
    some_plt.cm.get_cmap(name, nr_of_colours)


@typechecked
def generateLineTypes(y_series: np.ndarray) -> List:
    """

    :param y_series:

    """
    # generate varying linetypes
    typeOfLines = list(lines.lineStyles.keys())

    while len(y_series) > len(typeOfLines):
        typeOfLines.append("-.")

    # remove void lines
    for i in range(0, len(y_series)):
        if typeOfLines[i] == "None":
            typeOfLines[i] = "-"
        if typeOfLines[i] == "":
            typeOfLines[i] = ":"
        if typeOfLines[i] == " ":
            typeOfLines[i] = "--"
    return typeOfLines
