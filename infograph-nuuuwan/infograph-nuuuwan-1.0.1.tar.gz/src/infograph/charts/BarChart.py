import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from infograph.charts.GenericChart import GenericChart
from infograph.core.DEFAULT import DEFAULT


class BarChart(GenericChart):
    def __init__(self, title, x, y, func_color=None):
        self.title = title
        self.x = x
        self.y = y
        self.func_color = func_color

    @property
    def colors(self):
        if self.func_color:
            return [self.func_color(xi, yi) for xi, yi in zip(self.x, self.y)]
        else:
            return None

    def render_custom_inner(self):
        ax = plt.gca()
        x = self.x
        y = self.y
        ax.bar(x, y, color=self.colors)

    def render_custom(self):
        ax = plt.gca()
        self.render_custom_inner()

        ticks_loc = ax.get_yticks().tolist()
        ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
        ax.set_yticklabels([f'{x:,.0f}' for x in ticks_loc])

        for tick in ax.get_xticklabels():
            tick.set_rotation(90)
        ax.tick_params(labelsize=DEFAULT.FONT_SIZE_BASE)
