#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable
from PyQt5 import QtGui

from PyQt5.QtCore import QPointF, QRectF, QSizeF
from PyQt5.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem

from muphyn.packages.interface.models.links_model.abstract_node_model import AbstractNodeModel
from muphyn.packages.interface.models.links_model.link_model import LinkModel

#-----------------------------------
# Class
#-----------------------------------

class NodeModel (AbstractNodeModel[LinkModel]) :
    """Est le type générique de noeud pour afficher des liens non typés dans l'interface."""

    connector_size: QSizeF = QSizeF(20, 20)
    line_length: float = 20.0

    node_size: QSizeF = QSizeF(connector_size.x(), connector_size.y()+line_length)
    
    # -------------
    # Constructors
    # -------------
    
    def __init__ (self, position : QPointF, size : QSizeF, links : Iterable[LinkModel] = [], text : str = '', parent : QGraphicsItem = None) :

        AbstractNodeModel.__init__(self, 'node', position, size, links, text, parent)

    # -------------
    # Methods
    # -------------

    def insert_link (self, index : int, link : LinkModel) -> None :
        """Permet d'insérer un lien à la position données."""

        if link is None : 
            return

        if index < 0 :
            return

        if index > self._links.__len__() :
            return

        self._links.insert(index, link)

    def remove_link (self, link : LinkModel) -> None :
        """Permet de supprimer un lien."""
        self._links.remove(link)
    
    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawEllipse(QRectF(self.position, NodeModel.connector_size))
        painter.drawLine(
            QPointF(NodeModel.width(), NodeModel.height()/2), 
            QPointF(NodeModel.width() + NodeModel.line_length, NodeModel.height()/2)
        )
        super().paint(painter, option, widget)