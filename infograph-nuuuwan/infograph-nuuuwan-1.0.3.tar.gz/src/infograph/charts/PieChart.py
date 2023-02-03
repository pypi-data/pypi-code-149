import matplotlib.pyplot as plt

from infograph.charts.GenericChart import GenericChart
from infograph.core.DataColor import DataColor
from infograph.core.DEFAULT import DEFAULT


class PieChart(GenericChart):
    def render_custom(self):
        ax = plt.gca()
        x = self.x
        y = self.y
        colors = [DataColor.from_label(xi) for xi in x]
        ax.pie(
            y,
            labels=x,
            startangle=90,
            colors=colors,
            textprops={'fontsize': DEFAULT.FONT_SIZE_BASE},
        )
        ax.set_yticklabels(['{:,.0f}'.format(x) for x in ax.get_yticks()])
