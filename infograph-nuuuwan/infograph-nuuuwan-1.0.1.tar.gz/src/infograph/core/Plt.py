import matplotlib.pyplot as plt

from infograph.core.DEFAULT import DEFAULT


class Plt:
    @staticmethod
    def text(xy, text, p_font_size=1, color="#000000"):
        x, y = xy
        plt.gcf().text(
            x=x,
            y=y,
            s=text,
            fontsize=DEFAULT.FONT_SIZE_BASE * p_font_size,
            verticalalignment='center',
            horizontalalignment='center',
            color=color,
        )
