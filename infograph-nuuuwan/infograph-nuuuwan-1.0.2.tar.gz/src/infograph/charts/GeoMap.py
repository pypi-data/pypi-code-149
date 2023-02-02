import matplotlib.pyplot as plt
from utils import Log

from infograph.charts.GenericChart import GenericChart

log = Log('GeoMap')


class GeoMap(GenericChart):
    def __init__(self, title, ent_list: list, id_to_color):
        super().__init__(title, None, None)
        self.ent_list = ent_list
        self.id_to_color = id_to_color

    def render_custom(self):
        ax = plt.gca()

        for ent in self.ent_list:
            ent.geo().plot(ax=ax, color=self.id_to_color[ent.id])

        plt.axis('off')
