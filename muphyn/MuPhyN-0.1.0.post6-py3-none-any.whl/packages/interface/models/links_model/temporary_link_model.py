#-----------------------------------
# Imports
#-----------------------------------

# General Imports

# Project Imports
from PyQt5.QtCore import QSizeF
from PyQt5.QtWidgets import QWidget

# Project Imports
from muphyn.packages.interface.models.graphical_models.abstract_moveable_graphical_element import AbstractMoveableGraphicalElement
from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel
from muphyn.packages.interface.models.links_model.link_type import LinkType
from muphyn.packages.interface.models.signals_model.abstract_connection_model import AbstractConnectionModel

#-----------------------------------
# Class
#-----------------------------------
class TemporaryLink(AbstractLinkModel):
    def __init__(self, mouse_item: QWidget, signal_creator: AbstractConnectionModel):

        # Init Input Model (end of connector)
        input_model = AbstractMoveableGraphicalElement('mouse', mouse_item.pos(), QSizeF(0, 0))
        mouse_item.changeEvent()

        super().__init__(input_model, signal_creator, LinkType.SQUARE)

        
