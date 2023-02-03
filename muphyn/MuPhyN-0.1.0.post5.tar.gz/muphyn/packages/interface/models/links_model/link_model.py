#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel
from muphyn.packages.interface.models.links_model.link_type import LinkType

#-----------------------------------
# Class
#-----------------------------------

class LinkModel (AbstractLinkModel) :
    """Est le type générique de lien pour afficher des liens non typés dans l'interface."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, node_model_1 : Any, node_model_2 : Any, link_type : LinkType,
                  text : str = '') :

        AbstractLinkModel.__init__(self, node_model_1, node_model_2, link_type, text)

    # -------------
    # Methods
    # -------------
    