"""Creates a box plot."""
from typing import Dict, List, Union, Optional

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from typeguard import typechecked


@typechecked
def example_box_plot(
    output_dir: str, filename: str, extensions: List[str]
) -> None:
    """Example that creates a box plot.

    Copy paste it in your own code and modify the values accordingly.
    """

    # Fixing random state for reproducibility
    np.random.seed(7)

    # fake up some data
    first = [39, 44, 50, 50, 58, 63]
    second = [80, 100, 100, 120]

    # Add a name for each boxplot for in the legend, and y values.
    y_series = {"data_1": first, "data_2": second}

    create_box_plot(
        extensions=extensions,
        filename=filename,
        legendPosition=0,
        output_dir=output_dir,
        x_axis_label="x-axis label [units]",
        y_axis_label="y-axis label [units]",
        y_series=y_series,
    )


@typechecked
def set_boxplot_colours(
    box_plot: Dict[str, Union[str, List]],
    colour_pattern: str,
    nr_of_colours: int,
) -> None:
    """Generates the colours for the boxes and applies the colours to those
    boxes."""

    hex_colours: List[str] = get_hex_boxplot_colours(
        colour_pattern, nr_of_colours
    )

    # Apply the colours to the boxplots.
    for patch, color in zip(box_plot["boxes"], hex_colours):
        patch.set_facecolor(color)


@typechecked
def get_hex_boxplot_colours(
    colour_pattern: str, nr_of_colours: int
) -> List[str]:
    """Creates a cmap (colour map) for the specified nr of boxes and returns a
    list of Hexcodes."""
    hex_colours: List[str] = []

    colours = matplotlib.pyplot.cm.get_cmap(colour_pattern, nr_of_colours)

    for i in range(colours.N):
        rgba = colours(i)

        # rgb2hex accepts rgb or rgba
        hex_colours.append(matplotlib.colors.rgb2hex(rgba))
    return hex_colours


# pylint: disable=R0913
@typechecked
def create_box_plot(
    extensions: List[str],
    filename: str,
    legendPosition: int,
    output_dir: str,
    x_axis_label: str,
    y_axis_label: str,
    y_series: Dict[str, List[Union[int, float]]],
    title:Optional[str]="",
    x_axis_label_rotation: Optional[int]=0,
) -> None:
    """
    TODO: remove labels and legend they are double up because they are already
     on the x-axis.
    :param x:
    :param y_series:
    :param x_label:
    :param y_label:
    :param label:
    :param filename:
    :param legendPosition:
    :param y_series:
    :param y_label:
    :param filename:
    :param y_label:
    :
    """
    _, ax1 = plt.subplots()

    # ha stands for horizontal alignment, the top right of the x-axis label
    # is positioned below the respective x-tick.
    ax1.set_xticklabels(list(y_series.keys()),rotation=x_axis_label_rotation, ha='right')
    plt.tight_layout() # Ensure the bottom x-tick labels are within the image.
    #plt.xticks(rotation=45, ha='right')
    ax1.set_title(title)

    # Create box plot, patch_artist is to colour the boxes.
    box_plot = ax1.boxplot(x=list(y_series.values()), patch_artist=True)
    set_boxplot_colours(
        box_plot=box_plot, colour_pattern="hsv", nr_of_colours=len(y_series)
    )

    # configure plot layout
    plt.legend(loc=legendPosition)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    for extension in extensions:
        plt.savefig(f"{output_dir}/{filename}.{extension}")
    plt.clf()
    plt.close()
