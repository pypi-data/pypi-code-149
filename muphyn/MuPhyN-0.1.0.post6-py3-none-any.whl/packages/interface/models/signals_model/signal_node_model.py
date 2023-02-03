#-----------------------------------
# Imports
#-----------------------------------

from signal import signal
from typing import Iterable, List

from PyQt5 import QtGui
from PyQt5.QtCore import QMimeData, QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsSceneMouseEvent, QStyleOptionGraphicsItem

from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.interface.models.signals_model.abstract_connection_model import AbstractConnectionModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.models.links_model.temporary_link_model import TemporaryLink

#-----------------------------------
# Fnctions
#-----------------------------------

def start_drag (signal_creator : AbstractConnectionModel, event: QGraphicsSceneMouseEvent) -> bool :
    mimeData : QMimeData = QMimeData()
    mimeData.setData('action', bytearray('new link'.encode()))
    mimeData.setData('link', bytearray(str(id(signal_creator)).encode()))
    mimeData.setData('type', bytearray(signal_creator.data_type.__str__().encode()))

    drag : QtGui.QDrag = QtGui.QDrag(signal_creator)
    drag.setMimeData(mimeData)
    da : Qt.DropAction = drag.exec(Qt.LinkAction)

    # del temporary_link

#-----------------------------------
# Class
#-----------------------------------

class SignalNodeModel (AbstractConnectionModel) :
    """Est le modèle des noeuds permettant de diviser les liens en plusieurs segments."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF, links : Iterable[SignalLinkModel] = [],
                  text : str = '', is_infinite : bool = False, parent : QGraphicsItem = None) :

        AbstractConnectionModel.__init__(self, name, data_type, position, size, links, text, is_infinite, parent)
        
    # -------------
    # Properties
    # -------------

    @property 
    def is_input (self) -> bool :
        """Permet de savoir si l'élément est une entrée."""
        return False

    @property
    def is_connected_to_input (self) -> bool :
        """Permet de savoir si l'élément actuel est connecté à une entrée (ou est un entrée)."""

        if self.is_input :
            return True
        
        is_connected = False

        lst_already_passed : List[AbstractConnectionModel] = [self]
        lst_to_pass : List[AbstractConnectionModel] = [] 

        for link in self._links :

            if not(link.node_1 in lst_already_passed) :
                if not(link.node_1 in lst_to_pass) :
                    lst_to_pass.append(link.node_1)
            
            if not(link.node_2 in lst_already_passed) :
                if not(link.node_2 in lst_to_pass) :
                    lst_to_pass.append(link.node_2)

        while lst_to_pass.__len__() > 0 :
            
            connectionModel : AbstractConnectionModel = lst_to_pass[0]
            
            if connectionModel.is_input :
                return True
            
            for link in connectionModel._links :

                if not(link.node_1 in lst_already_passed) :
                    if not(link.node_1 in lst_to_pass) :
                        lst_to_pass.append(link.node_1)
                
                if not(link.node_2 in lst_already_passed) :
                    if not(link.node_2 in lst_to_pass) :
                        lst_to_pass.append(link.node_2)

            lst_to_pass.remove(connectionModel)
            lst_already_passed.append(connectionModel)
        
        return is_connected

    # -------------
    # Methods
    # -------------
    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None :

        if (event.button() == Qt.LeftButton and event.modifiers() == Qt.ControlModifier) :
            start_drag(self, event)
            event.accept() 

        return super().mousePressEvent(event)