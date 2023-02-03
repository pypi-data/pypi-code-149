import numpy as np
import corner
from matplotlib.colors import colorConverter
from matplotlib.patches import Patch as mplpatches
from matplotlib.lines import Line2D


def print_mcmc_params(mcmcParams, quantileLevels):
    '''
    This function is just for printing MCMC parameters for easy copy/pasting
    to alog. Update of Jeff's existing code for prettier formatting.

    Prints in two formats: first the quantile values,
    then in the format 'X (+Y/-Z)'.

    Parameters
    ----------
    mcmcParams: dict
        Keys should be parameter names, values include quantiles, errbars, labels
        TODO improve documentation

    Returns
    -------
    tableQuant: str
        Printable table of values in quantile format
    tablePM: str
        Printable table of values in +/- format

    '''

    # Set up lists to hold the tables (will be joined with newline later)
    tableQuant = []
    tablePM = []

    # Define a column spacer
    spacer = " | "

    # Set up left column width for parameter labels
    ncharsLabel = max([len(p['label']) for p in mcmcParams.values()])

    # Set up widths for the quantiles section
    ncharsCol = max([len(f"{x:4.4g}") for p in mcmcParams.values()
                    for x in p['quantiles']])

    # Set up the header for the quantiles section
    tag = "(quantile)"
    pline = [f"{'Parameter':<{ncharsLabel-len(tag)}s}{tag}"]
    for x in quantileLevels:
        pline += [f"{str(x):<{ncharsCol}s}"]
    header = spacer.join(pline)
    tableQuant += [header]
    tableQuant += ["-"*len(header)]

    # Set up each line for the quantiles section
    for param in mcmcParams.values():
        pline = [f"{param['label']:<{ncharsLabel}s}"]
        for x in param['quantiles']:
            valstr = f"{x:4.4g}"
            pline += [f"{valstr:<{ncharsCol}s}"]
        tableQuant += [spacer.join(pline)]
    tableQuant += ["-"*len(header)]

    # Set up column widths for the +/- section
    ncharsCol = max([len(f"{param[key]:4.4g} ({abs(param[key]/param['median']):.2f}%)")
                    for param in mcmcParams.values()
                    for key in ['median', 'errplus', 'errminus']])

    # Set up head for the +/- section
    tag = "(value +/-)"
    pline = [f"{'Parameter':<{ncharsLabel-len(tag)}s}{tag}"]
    for x in ["value", " +", " -"]:
        pline += [f"{str(x):<{ncharsCol}s}"]
    header = spacer.join(pline)
    tablePM += [header]
    tablePM += ["-"*len(header)]

    # Set up each line for the +/- section
    for param in mcmcParams.values():
        pline = [f"{param['label']:<{ncharsLabel}s}"]
        for key in ['median', 'errplus', 'errminus']:
            if key == 'median':
                fmat = f"{param[key]:4.4g}"
            else:
                fmat = f"{param[key]:4.4g} ({(param[key]/param['median']):.2f}%)"
            pline += [f"{fmat:<{ncharsCol}s}"]
        tablePM += [spacer.join(pline)]

    tablePM = "\n".join(tablePM)
    tableQuant = "\n".join(tableQuant)

    return tableQuant, tablePM


def make_corner_plot(chains, mcmcparams, quantilelevels, outfile,
                     title):
    '''
    Make an MCMC corner plot
    parameters
    ----------
    chains: 2d array
        size: (number of mcmc params),(number of steps in mcmc chain)

    mcmcparams: dict
        keys should be parameter names, values include quantiles, errbars, labels

    quantilelevels: 1d array

    outfile
        path to save corner plot

    title
        plot title

    returns
    -------
    none
        just saves figures
    '''

    color = 'C3'  # base fill color for contours
    truthcolor = 'C0'  # color for median markers
    nbins = 100  # number of bins for histogram

    # === create main plot
    cp = corner.corner(
        np.transpose(chains),
        bins=nbins,
        quantiles=[quantilelevels[0], quantilelevels[-1]],
        smooth=2.0,
        labels=[param['mathlabel'] for param in mcmcparams.values()],
        verbose=False,
        label_kwargs={'fontsize': 12},
        show_titles=True,
        title_fmt='.3e',
        title_kwargs={'fontsize': 12},
        plot_datapoints=False,
        plot_density=True,
        plot_contours=True,
        fill_contours=True,
        color=color,
        use_math_text=True,
        truths=[param['median'] for param in mcmcparams.values()],
        truth_color=truthcolor
    )
    cp.suptitle(title, fontsize=20)

    # ==== reproducing the contour colors
    # annoying as this is, corner does not provide a way to get
    # the contour fill color maps, nor the default levels.
    # we copy the following from its definition in
    # https://github.com/dfm/corner.py/blob/e65dd4cdeb7a9f7f75cbcecb4f07a07de65e2cea/src/corner/core.py
    levels = 1.0 - np.exp(-0.5 * np.arange(0.5, 2.1, 0.5) ** 2)
    rgba_color = colorConverter.to_rgba(color)
    contour_cmap = [list(rgba_color) for lev in levels] + [rgba_color]
    for i, l in enumerate(levels):
        contour_cmap[i][-1] *= float(i) / (len(levels) + 1)
    contour_cmap = contour_cmap[-3:][::-1]

    # === generating custom legend

    # shaded rectangle for each contour fill color
    legend_symbols = [mplpatches(
        facecolor=contour_cmap[i],
        edgecolor=contour_cmap[i]) for i in range(len(contour_cmap))]
    # line for the "truth" values (mcmcparam median values)
    legend_symbols.append(Line2D([0], [0], color=truthcolor, lw=3))
    # empty rectangle to make space for bin count label
    legend_symbols.append(mplpatches(alpha=0))

    # create legend
    cp.legend(
        legend_symbols,
        [r'$1\sigma$',
         r'$2\sigma$',
         r'$3\sigma$',
         'map',
         f'({nbins} bins for 1d pdf)'],
        fontsize=15,
        title_fontsize=15,
        title="2d pdf contours",
        frameon=True,
        markerscale=20.0,
    )

    # === fix up the histogram axes

    # grab all subplot axes
    axes = cp.get_axes()

    # determine which ones are histograms
    nparams = len(mcmcparams.values())
    length_sides = np.arange(nparams)
    histogram_indices = (nparams+1)*length_sides

    # create right-side axis for each histogram
    for i in histogram_indices:
        ax = axes[i]
        ax2 = ax.twinx()
        ax2.set_ylabel('1d norm. pdf \n (percent per bin)')
        axes += [ax2]
        ax2.set_ylim(0, 1.1)

    # resize the tick params to make them smaller
    for ax in axes:
        ax.tick_params(axis='both', labelsize=10)

    # save figure
    cp.set_size_inches(10, 10)
    cp.tight_layout()
    cp.savefig(outfile)
    return cp
