# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

import logging
LOGGER = logging.getLogger(__name__)
try:
    import matplotlib.pyplot as plt
except ImportError:
    LOGGER.warning("can't import matplotlib")
try:
    import networkx as nx
except ImportError:
    LOGGER.warning("can't import networkx")

def draw_matrix(matrix, clm_name, pos=None, layout_type="circular", **kwargs):
    """
    Creates a NetworkX graph for any matrix

    Args:
    matrix (square matrix, required):
        matrix for which graphical visualization is created
    clm_name (list, required):
        list of strings for the columns names for the matrix
    pos (dict, optional):
        dict having info about the position of node on networkX graph
    layout_type (string, optional):
        layout type for network x graph. refer-
        https://networkx.github.io/documentation/networkx-1.10/reference/drawing.html#layout

    Returns:
    pos (dict): dict having info about the position of node on networkX graph is return for
    the new graph.
    graph (graph type obj): graph object from network x is returned.
    """

    if len(matrix) != len(clm_name):
        raise Exception("Number of column does not match with column name")

    # prepare an edge
    r_set = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if abs(matrix[i][j]) > 0:
                r_set.append((clm_name[i], clm_name[j], matrix[i][j]))

    graph = nx.Graph()
    graph.add_weighted_edges_from(r_set)
    graph.remove_edges_from(nx.selfloop_edges(graph))

    # selecting the layout type
    if not pos:
        if layout_type == "circular":
            pos = nx.circular_layout(graph)
        elif layout_type == "random":
            pos = nx.random_layout(graph)
        elif layout_type == "spring":
            pos = nx.spring_layout(graph)
        elif layout_type == "spectral":
            pos = nx.spectral_layout(graph)
        elif layout_type == "kamada_kawai":
            pos = nx.kamada_kawai_layout(graph)

    edges = graph.edges()
    weights = [graph[u][v]["weight"] for u, v in edges]
    # width parameter for weighted or custom edges
    _width = []
    if "width" not in kwargs:
        _width = weights * 4
    else:
        _width = kwargs["width"]
        del kwargs["width"]

    # node lables
    _with_label = []
    if "with_label" not in kwargs:
        _with_label = True
    else:
        _with_label = kwargs["with_label"]
        del kwargs["with_label"]

    # plotting the graph
    nx.draw(graph, pos, edgelist=edges, width=_width, with_labels=_with_label, **kwargs)
    return graph, pos


def plot_matrix(matrix, num_plots_row=7, clm_name=None):
    """
    Plots multiple line plots for numpy array

    Args:
        matrix(numpy array, required):
            2d array for which each row has to be plotted into a line plot
        num_plots_row (int, optional):
            Number of plots in 1 row (Maximum value is 7)
        clm_name (list of strings, optional):
            rows/variables names in the numpy array
    """

    if clm_name is not None and len(matrix) != len(clm_name):
        raise Exception("Number of column does not match with column name")

    x = range(len(matrix[0]))

    left = 0.125  # the left side of the subplots of the figure
    right = 3  # the right side of the subplots of the figure
    bottom = 0  # the bottom of the subplots of the figure
    top = 24 - 3 * num_plots_row  # the top of the subplots of the figure
    wspace = 0.3  # the amount of width reserved for blank space between subplots
    hspace = 0.7  # the amount of height reserved for white space between subplots

    fig = plt.figure()
    plt.subplots_adjust(left, bottom, right, top, wspace, hspace)

    for i in range(len(matrix)):
        ax = fig.add_subplot(int((len(matrix)) / num_plots_row) + 1, num_plots_row, i + 1)
        ax.plot(x, matrix[i])
        if clm_name is None:
            ax.set_title("x" + str(i))
        else:
            ax.set_title(clm_name[i])
