#-----------------------------------
# Imports
#-----------------------------------
# General Imports
from typing import Generic, Iterable, Type, TypeVar, List, Any

# PyQt5 Imports
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QSizeF, pyqtSignal
from PyQt5.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem

# Project Imports
from muphyn.packages.interface.models.graphical_models.abstract_moveable_graphical_element import AbstractMoveableGraphicalElement
from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel

#-----------------------------------
# Generic Type
#-----------------------------------

T = TypeVar('T', bound = AbstractLinkModel)

#-----------------------------------
# Class
#-----------------------------------


class AbstractNodeModel (Generic[T], AbstractMoveableGraphicalElement) :
    """Est la classe abstraite commune aux noeuds capables d'être affiché dans l'interface."""
    
    
    # -------------
    # Signals
    # -------------
    links_count_changed = pyqtSignal()

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, position : QPointF, size : QSizeF, links : Iterable[Type[T]],
                  text : str = '', parent : QGraphicsItem = None) :

        AbstractMoveableGraphicalElement.__init__(self, name, position, size, 0, text, parent)

        self._links : List[Type[T]] = []

        self.connector_center = QPointF(0, 0)
        
        self.setFlag(QGraphicsItem.ItemIsMovable, False)

        for link in links :
            self._links.append(link)
        self.links_count_changed.emit()

    # -------------
    # Properties
    # -------------

    @property 
    def links (self) -> Iterable[Type[T]] :
        """Permet de récuperer la liste des liens connectés au noeud."""

        for link in self._links :
            yield link

    # -------------
    # Methods
    # -------------
 
    def __len__ (self) -> int :
        """Permet de récuperer le nombre de liens connectés au noeud."""
        return self._links.__len__()

    def setRotation (self, angle: float) -> None :
        ...

    def add_link (self, link : Any) -> None :
        """Permet d'ajouter un lien à la position données."""

        if link is None : 
            return

        self._links.append(link)
        self.links_count_changed.emit()

    def insert_link (self, index : int, link : Any) -> None :
        """Permet d'insérer un lien à la position données."""

        if link is None : 
            return

        if index > len(self._links) :
            return

        self._links.insert(index, link)
        self.links_count_changed.emit()

    def remove_link (self, link : Type[T]) -> None :
        """Permet de supprimer un lien."""

        if link is None : 
            return

        self._links.remove(link)
        self.links_count_changed.emit()
    
    def paint (self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        ...