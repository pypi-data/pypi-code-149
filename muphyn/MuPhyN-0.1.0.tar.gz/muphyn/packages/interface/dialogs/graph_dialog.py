from PyQt5.QtWidgets import QDialog, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import Cursor

from matplotlib.figure import Figure

class GraphWindow(QDialog):

    def __init__(self, parent=None , box = None):
        super().__init__(parent)

        self.figure = Figure()
        self.box = box

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        self.setWindowTitle(str(self.box.index) + '-' +  str(self.box['title']))
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.setStretch(1, 1)
        self.setLayout(layout)
        self.plot()

    def plot(self):
        data_y: dict = self.box['data_y']

        #fig = plt.figure(str(self.box.index) + '-' +  str(self.box['title'])) 
        self.figure.clear()
        
        
        ax = self.figure.add_subplot(111)
        ax.grid(True)
        
        ax.set_xlabel(self.box['t'])
        ax.set_ylabel(self.box['label_y'])

        for key, values in data_y.items() :
            ax.plot(self.box['data_x'], values, label=key)

        ax.legend(loc="upper right")

        cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True, color = 'r', linewidth = 1)
        self.annot = ax.annotate("", xy=(0,0), xytext=(-40,40),textcoords="offset points",
                    bbox=dict(boxstyle='round4', fc='linen',ec='k',lw=1),
                    arrowprops=dict(arrowstyle='-|>'))
        self.annot.set_visible(False)

        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.canvas.draw()

    def onclick(self, event):
        i, x = _closest(event.xdata, self.box['data_x'])

        key = list(self.box['data_y'].keys())[0]
        y = self.box['data_y'][key][i]

        self.annot.xy = (x,y)
        text = "({:.2g}, {:.2g})".format(x,y)
        self.annot.set_text(text)
        self.annot.set_visible(True)
        self.canvas.draw()

def _closest(a:float, b:list):
    c = [abs(x-a) for x in b]
    i = c.index(min(c))
    return (i, b[i])