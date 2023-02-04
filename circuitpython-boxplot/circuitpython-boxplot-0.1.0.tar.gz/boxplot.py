# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`boxplot`
================================================================================

Calculates boxplot and creates its graphical representation


* Author(s): Jose D. Montoya

Implementation Notes
--------------------


**Hardware:**
Boards with CircuitPython >8.0.0 RC2

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads


"""

try:
    from typing import Union, Tuple
except ImportError:
    pass

from ulab import numpy as np
from bitmaptools import draw_line
import displayio

__version__ = "0.1.0"
__repo__ = "https://github.com/jposada202020/CircuitPython_boxplot.git"

# pylint: disable=too-many-instance-attributes, too-many-arguments, invalid-name
class Boxplot(displayio.TileGrid):
    """A BoxPlot TileGrid. The origin is set using ``x`` and ``y``.

    :param (list, tuple) data: source data to calculate the boxplot
    :param int x: x position of the boxplot origin
    :param int y: y position of the boxplot origin

    :param int width: requested width, in pixels. Defaults to 20 pixels.
    :param int height: requested height, in pixels.

    :param int background_color: background color to use defaults to black (0x000000)
    :param int fill_color: background color to use defaults to black (0x000000)
    :param int line_color: background color to use defaults to white (0xFFFFFF)


    **Quickstart: Importing and using Boxplot**

    Here is one way of importing the `Boxplot` class so you can use it as
    the name ``Boxplot``:

    .. code-block:: python

        from boxplot import Boxplot
        import displayio

    Now you can create a boxplot at pixel position x=20, y=30 using:

    .. code-block:: python

        a=[1, 1, 4, 5, 6, 7, 7, 7, 8, 9, 10, 15, 16, 17, 24, 56, 76, 87, 87]
        my_boxplot=Boxplot(a, x=50, y=50) # instance the boxplot at x=50, y=50
        my_group = displayio.Group()

    Once you set up your display, you can now add ``my_boxplot`` to your display.Group() using:

    .. code-block:: python

        my_group.append(my_boxplot)
        display.show(my_group) # add the group to the display


    **Summary: Boxplot Features and input variables**

    The `boxplot` TileGrid has some options for controlling its position, visible appearance,
    through a collection of input variables:

        - **position**: ``x``, ``y``

        - **size**: ``width`` and ``height``

        - **color**: ``background_color``, ``fill_color``, ``line_color``


        - **range**: ``xrange`` and ``yrange`` This is the range in absolute units.
          For example, when using (20-90), the X axis will start at 20 finishing at 90.
          However, the height of the graph is given by the height parameter. The scale
          is handled internally to provide a 1:1 experience when you update the graph.


    .. figure:: boxplot.jpg
       :scale: 100 %
       :figwidth: 50%
       :align: center
       :alt: Diagram of the boxplot TileGrid with the pointer in motion.

       This is a diagram of a boxplot


    """

    def __init__(
        self,
        data: Union[list, Tuple],
        x: int,
        y: int,
        height: int,
        width: int = 20,
        background_color: int = 0x000000,
        fill_color: int = 0xFFFFFF,
        line_color: int = 0xFFFFFF,
    ) -> None:
        self.data = np.array(data)
        self._width = width
        self.ynorm = np.array(
            self.normalize(np.min(self.data), np.max(self.data), 0, height, self.data),
            dtype=np.uint16,
        )
        self._whisker_width = width / 4
        self._color_palette = displayio.Palette(4)
        self._color_palette[0] = background_color
        self._color_palette[1] = fill_color
        self._color_palette[2] = line_color
        self._color_palette[3] = 0x0000FF
        bq3, bq2, bq1, minimum, maximum = self.find_points(self.ynorm)
        self._bitmap = displayio.Bitmap(width + 1, height + 1, 3)
        self._new_max = int(self.normalize(minimum, maximum, maximum, minimum, maximum))
        self._new_q3 = int(self.normalize(minimum, maximum, maximum, minimum, bq3))
        self._new_q2 = int(self.normalize(minimum, maximum, maximum, minimum, bq2))
        self._new_q1 = int(self.normalize(minimum, maximum, maximum, minimum, bq1))
        self._new_min = int(self.normalize(minimum, maximum, maximum, minimum, minimum))

        self._whiskerxs = int(self._width / 2 - self._whisker_width / 2)
        self._whiskerse = int(self._width / 2 + self._whisker_width / 2)
        self._middle = int(self._width / 2)

        super().__init__(self._bitmap, pixel_shader=self._color_palette, x=x, y=y)

    @staticmethod
    def find_points(data):
        """
        this function finds the quartiles, minimum and maximum for the box plot

        :param data: data to be processed
        :return: tuple with the values

        """
        q2 = np.median(data)

        for i, element in enumerate(data):
            if element >= q2:
                pos = i
                break

        q1 = np.median(data[0:pos])
        q3 = np.median(data[pos:])
        lower_whisker = np.min(data[0:pos])
        upper_whisker = np.max(data[pos:])

        return q3, q2, q1, lower_whisker, upper_whisker

    @staticmethod
    def normalize(oldrangemin, oldrangemax, newrangemin, newrangemax, value):
        """
        This function converts the original value into a new defined value in the new range

        :param oldrangemin: minimum of the original range
        :param oldrangemax: maximum of the original range
        :param newrangemin: minimum of the new range
        :param newrangemax: maximum of the new range
        :param value: value to be converted
        :return: converted value

        """
        return (
            ((value - oldrangemin) * (newrangemax - newrangemin))
            / (oldrangemax - oldrangemin)
        ) + newrangemin

    def print_data(self):
        """
        This function prints the quartiles data

        :return: None
        """
        q3, q2, q1, lower_whisker, upper_whisker = self.find_points(self.data)

        print("q1: ", q1)
        print("q2: ", q2)
        print("q3: ", q3)
        print("IQR: ", q3 - q1)
        print("Minium: ", lower_whisker)
        print("Maximum: ", upper_whisker)

    def draw(self):
        """
        This function draws the boxplot

        :return: None
        """
        draw_line(self._bitmap, 0, self._new_q3, self._width, self._new_q3, 2)
        draw_line(self._bitmap, 0, self._new_q3, 0, self._new_q1, 2)
        draw_line(self._bitmap, 0, self._new_q1, self._width, self._new_q1, 2)
        draw_line(self._bitmap, self._width, self._new_q3, self._width, self._new_q1, 2)
        draw_line(self._bitmap, 0, self._new_q2, self._width, self._new_q2, 2)
        draw_line(
            self._bitmap, self._middle, self._new_max, self._middle, self._new_q3, 2
        )
        draw_line(
            self._bitmap, self._middle, self._new_min, self._middle, self._new_q1, 2
        )
        draw_line(
            self._bitmap,
            self._whiskerxs,
            self._new_max,
            self._whiskerse,
            self._new_max,
            2,
        )
        draw_line(
            self._bitmap,
            self._whiskerxs,
            self._new_min,
            self._whiskerse,
            self._new_min,
            2,
        )
