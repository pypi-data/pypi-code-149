#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable

from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QGraphicsItem

from muphyn.packages.core.plci_core_data import Data
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.interface.models.graphical_models.abstract_box_IO_model import AbstractBoxIOModel
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel

#-----------------------------------
# Class
#-----------------------------------

class BoxOutputModel (AbstractBoxIOModel) :
    """Est la classe des sorties des boxes composite."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF,
                 rotation : float = 0.0, links : Iterable[SignalLinkModel] = [], text : str = '',
                 color: QColor = Qt.GlobalColor.black, parent : QGraphicsItem = None) :

        AbstractBoxIOModel.__init__(self, name, data_type, position, size, rotation, text, parent)

        self._inputs.append(InputConnectionModel('', data_type, QPointF(0, 0), '', color, self))
    
    # -------------
    # Properties
    # -------------

    @property
    def default_value (self) -> Data :
        """Permet de récuperer la valeur par défaut du lien."""
        return self._default_value

    @default_value.setter
    def default_value (self, default_value_ : Data) :
        """Permet de modifier la valeur par défaut du lien."""

        if default_value_ is None :
            self._default_value = Data(self.data_type)

        elif not default_value_._data_type == self.data_type :
            self._default_value = Data(self.data_type)
        
        else :
            self._default_value = default_value_