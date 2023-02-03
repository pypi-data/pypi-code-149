#-----------------------------------
# Imports
#-----------------------------------

from typing import Any, Iterable

from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QSizeF, Qt, pyqtSignal, QObject
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsItem

from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.links_model.abstract_node_model import AbstractNodeModel
from muphyn.packages.interface.models.signals_model.abstract_signal_model import AbstractSignalModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.shapes.basic_shape.abstract_shape import AbstractShape

#-----------------------------------
# Class
#-----------------------------------

static_io_size = QSizeF(10, 22)
static_io_size_2 = QSizeF(static_io_size.width() / 2, static_io_size.height() / 2)
static_io_path = QtGui.QPainterPath(QPointF(-static_io_size_2.width(), -static_io_size_2.height()))

static_io_path.lineTo(-static_io_size_2.width(), (-static_io_size_2.height()) + 1)
static_io_path.lineTo(static_io_size_2.width(), 0)
static_io_path.lineTo(-static_io_size_2.width(), static_io_size_2.height() + 1)
static_io_path.lineTo(-static_io_size_2.width(), static_io_size_2.height())

class AbstractConnectionModel (AbstractSignalModel, AbstractNodeModel[AbstractSignalModel]) : 
    """Est la classe abstraite communes aux models représentant des connexions entre les boxes et les signaux."""
    # -------------
    # Static Values
    # -------------
    ConnectorSide = 15
    ConnectorLineLength = 10

    ItemWidth = ConnectorSide + ConnectorLineLength
    ItemHeight = 2 * ConnectorSide - 3
    ItemSize = QSizeF(ItemWidth, ItemHeight)

    # -------------
    # Signals
    # -------------
    is_connected_changed = pyqtSignal()

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF, links : Iterable[SignalLinkModel] = [],
                  text : str = '', is_infinite : bool = False, parent : QGraphicsItem = None) :
        
        AbstractSignalModel.__init__(self, data_type)
        AbstractNodeModel.__init__(self, name, position, size, links, text, parent)

        self._connector: AbstractShape = None
        self._lbl: AbstractShape = None
        self._line: AbstractShape = None
        
        self._color = QColor(Qt.GlobalColor.black)

        self._is_infinite = is_infinite

        self.is_connected = self._links.__len__() > 0
        self.links_count_changed.connect(self.on_links_count_changed)

    # -------------
    # Properties
    # -------------
    @property
    def color(self) -> QColor:
        return self._color

    @color.setter
    def color(self, new_color: QColor | Qt.GlobalColor):
        if new_color != self._color:
            LogManager().debug("change color")
            if type(new_color) == Qt.GlobalColor:
                self._color = QColor(new_color)
            elif type(new_color) == QColor:
                self._color = new_color
            else:
                raise(TypeError(f"{self.__class__.name}.color: Wrong type provided {type(new_color)} instead of QColor or Qt.GlobalColor"))

            self._lbl._pen.setColor(self._color)
            self._line._pen.setColor(self._color)
            self._connector._pen.setColor(self._color)

    @property
    def is_infinite (self) -> bool :
        """Permet de savoir si la connexion est ou fait partit d'un nombre infinie de connexion."""
        return self._is_infinite

    @property
    def diagram_model (self) -> Any :
        """Permet de récuperer l'éditeur visuel."""
        # Get parent item
        parent = self.parent() if self.parent() is not None else self.parentItem()
        if parent is not None and hasattr(parent, "diagram_model"):
            return parent.diagram_model
        else:
            return

    @property
    def absolute_connector_center(self) -> QPointF:
        return self._connector.scenePos() + self._connector.boundingRect().center()

    @property
    def box_model(self):
        return self.parent().parent()

    # -------------
    # Methods
    # -------------
    def on_links_count_changed(self):
        is_connected = self._links.__len__() > 0
        if self.is_connected != is_connected:
            self.is_connected = is_connected
            self.is_connected_changed.emit()
