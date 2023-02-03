#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import typing

# PyQt5 Imports
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QSizeF
from PyQt5.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem, QWidget

# Project Imports
from muphyn.packages.interface.models.graphical_models.abstract_moveable_graphical_element import AbstractMoveableGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class TextModel (AbstractMoveableGraphicalElement) :
    """Est le modèle pour afficher du texte à l'écran."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, position : QPointF, size : QSizeF, rotation : float = 0.0, text : str = '', parent : QGraphicsItem = None) :
        
        AbstractMoveableGraphicalElement.__init__(self, name, position, size, rotation, text, parent)
    
    # -------------
    # Methods
    # -------------

    def paint (self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget] = ...) -> None :
        painter.drawText(self.position, self.rendered_text)