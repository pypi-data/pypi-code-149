"""Cropping image tools and related functions."""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from drapo import Cursor, rinput


# ======================= IMCROP and related functions =======================


def _cropzone_draw(ax, cropzone, c='r', linewidth=2):
    """Draw cropzone on axes."""
    x, y, w, h = cropzone
    rect = patches.Rectangle((x - 1 / 2, y - 1 / 2), w, h, linewidth=linewidth,
                             edgecolor=c, facecolor='none')
    ax.add_patch(rect)
    ax.figure.canvas.draw()
    return rect


def imcrop(*args, cmap='gray', c='r', closefig=True, cursor=None,
           draggable=False, message='Crop Image', ax=None):
    """Interactive (or not)image cropping function using Numpy and Matplotlib.

    The *args allow to use the function in the two following ways:

    Main parameters (*args)
    -----------------------

    Depending on how the function is called, the cropping is interactive
    (manual selection on image) or imperative (crop zone (x, y, w, h) as input):

    *INTERACTIVE*

    `img_crop, cropzone = imcrop(img)`
    Input --> image (numpy array or equivalent)
    Output --> tuple (cropped image, crop rectangle (x, y, w, h))

    *IMPERATIVE*

    `img_crop = imcrop(img, cropzone)`
    Input --> image (numpy array or equivalent), crop zone (x, y, w, h)
    Output --> cropped image

    Other optional parameters
    -------------------------

    - cmap: colormap to display image in matplotlib imshow

    - c: color of lines / cursors in interactive mode

    - closefig: if True (default), close figure at end of interactive selection

    - cursor: appears to help selection by default but not in draggable mode
      (but can be forced in draggable mode by setting it to true, or can be
      completely suppressed by setting it to False). Default: None.

    - draggable: if True, use a draggable rectangle instead of clicks
      (only in interactive mode, see above)

    - message: message to show as title of the matplotlib window
      (only in interactive mode, see above)

    - ax: if not None, image shown in the ax matplotlib axes
      (only in interactive mode, see above)

    Note: when selecting, the pixels taken into account are those which have
    their centers closest to the click, not their edges closest to the click.
    For example, to crop to a single pixel, one needs to click two times in
    this pixel (possibly at the same location). For images with few pixels,
    this results in a visible offset between the dotted lines plotted after the
    clicks (running through the centers of the pixels clicked) and the final
    rectangle which runs along the edges of all pixels selected.

    Contrary to the Matlab imcrop function, the cropped rectangle is really of
    the width and height requested (w*h), not w+1 and h+1 as in Matlab.
    """
    img = args[0]  # load image
    sy, sx = img.shape  # size of image in pixels

    if len(args) == 2:
        interactive = False
        xmin, ymin, w, h = args[1]
    else:
        interactive = True

    if interactive:  # Interactive Drawing of Crop Rectangle -----------------

        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure

        ax.imshow(img, cmap=cmap)
        ax.set_title(message)
        ax.set_xlabel('Click 2 pts to define crop (opposite corners of rectangle)')

        # Manage cursor visibility depending on mode -------------------------

        if cursor is None:
            cursor = False if draggable else True

        if cursor:
            Cursor()

        # --------------------------------------------------------------------

        if draggable:

            x_min, y_min, _w, _h = rinput(c=c)

            x_max = x_min + _w
            y_max = y_min + _h

        else:

            clicks = []

            for i in range(2):  # two clicks for two corners

                [(x_click, y_click)] = plt.ginput(1)
                clicks.append((x_click, y_click))

                # now, draw for visual clues ---------------------------------

                x_draw, y_draw = round(x_click), round(y_click)

                # draw lines corresponding to click (the -1/2 are used so that
                # the lines extend to the edges of the pixels)
                ax.plot([-1 / 2, sx - 1 / 2], [y_draw, y_draw], ':', color=c)
                ax.plot([x_draw, x_draw], [-1 / 2, sy - 1 / 2], ':', color=c)

                fig.canvas.draw()

            [(x1, y1), (x2, y2)] = clicks

            x_min, x_max = sorted((x1, x2))
            y_min, y_max = sorted((y1, y2))

        # Now, get pixels correspongind to clicks (center of a pixel is a
        # round number)
        xmin, xmax = round(x_min), round(x_max)
        ymin, ymax = round(y_min), round(y_max)

        # Calculate witdh and height in pixels
        w = xmax - xmin + 1
        h = ymax - ymin + 1

        cropzone = xmin, ymin, w, h

        _cropzone_draw(ax, cropzone, c)

        if closefig:
            plt.pause(0.2)
            plt.close(fig)

    # Now, in all cases, crop image to desired dimensions --------------------

    img_crop = img[ymin: ymin + h, xmin: xmin + w]

    if not interactive:
        return img_crop
    else:
        return img_crop, cropzone
