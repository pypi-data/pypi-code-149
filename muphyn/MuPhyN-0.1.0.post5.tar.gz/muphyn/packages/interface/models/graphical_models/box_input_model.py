#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QGraphicsItem

from muphyn.packages.core.plci_core_data_type import DataType

from muphyn.packages.interface.models.graphical_models.abstract_box_IO_model import AbstractBoxIOModel

from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel

from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel

#-----------------------------------
# Class
#-----------------------------------

class BoxInputModel (AbstractBoxIOModel) :
    """Est la classe des entrées des boxes composite."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF,
                  rotation : float = 0.0, link : SignalLinkModel = None, text : str = '',
                  color: QColor = Qt.GlobalColor.black, parent : QGraphicsItem = None) :

        AbstractBoxIOModel.__init__(self, name, data_type, position, size, rotation, text, parent)
        
        self._outputs.append(OutputConnectionModel('', data_type, QPointF(0, 0), link, None, '', color, self))
