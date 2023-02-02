import matplotlib.pyplot as plt


class GenericChart:
    def __init__(self, title, x, y):
        self.title = title
        self.x = x
        self.y = y

    def render(self):
        ax = plt.gca()
        plt.axis('on')
        ax.set_title(self.title)
        self.render_custom()
